"""
export_sfera.py — esporta i concetti EduWiki come grafo JSON per la Sfera della Conoscenza.

Le relazioni NON sono inventate: derivano dai wikilink [[...]] realmente presenti
nelle pagine. Il tema viene dal campo `tema:` nel frontmatter. La definizione dalla
sezione "## Definizione breve", ripulita dagli embed di immagine e video.

Output: quartz/static/sfera.json  →  pubblicato su /static/sfera.json
Rieseguire dopo ogni modifica ai concetti.
"""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT = ROOT / "quartz" / "static" / "sfera.json"

# cartelle le cui pagine sono "risorse operative" collegate a un concetto
RISORSE = {"attivita": "attivita", "uda": "uda", "valutazione": "valutazione",
           "inclusione": "inclusione", "strumenti": "strumenti", "metodologie": "metodologie"}


def campo(testo, nome):
    m = re.search(rf'^{nome}:\s*"?(.*?)"?\s*$', testo, re.M)
    return m.group(1) if m else ""


def definizione(testo):
    """Testo della sezione 'Definizione breve', senza immagini/video iniettati."""
    m = re.search(r"^## Definizione breve\s*\n(.*?)(?=^## )", testo, re.S | re.M)
    if not m:
        return ""
    t = m.group(1)
    t = re.sub(r"<figure>.*?</figure>", "", t, flags=re.S)      # embed video
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)                   # immagine
    t = re.sub(r"^\*📖.*$", "", t, flags=re.M)                   # didascalia immagine
    t = re.sub(r"^---+$", "", t, flags=re.M)                     # separatori
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)                       # grassetto
    t = re.sub(r"\s+", " ", t).strip()
    return t


def main():
    # 1. indice di tutte le pagine: slug -> (cartella, titolo)
    pagine = {}
    for f in CONTENT.rglob("*.md"):
        if f.name == "index.md":
            continue
        pagine[f.stem] = (f.parent.name, campo(f.read_text(encoding="utf-8"), "title") or f.stem)

    concetti_dir = CONTENT / "concetti"
    slug_concetti = {f.stem for f in concetti_dir.glob("*.md")}

    nodi, non_risolti = {}, defaultdict(list)

    for f in sorted(concetti_dir.glob("*.md")):
        testo = f.read_text(encoding="utf-8")
        link = [l.split("|")[0].split("#")[0].strip()
                for l in re.findall(r"\[\[([^\]]+)\]\]", testo)]

        relazioni, risorse = [], defaultdict(list)
        for l in link:
            if l == f.stem:
                continue
            if l in slug_concetti:
                if l not in relazioni:
                    relazioni.append(l)
            elif l in pagine:
                cart = pagine[l][0]
                if cart in RISORSE and l not in risorse[RISORSE[cart]]:
                    risorse[RISORSE[cart]].append(l)
            else:
                non_risolti[f.stem].append(l)

        nodi[f.stem] = {
            "id": f.stem,
            "titolo": campo(testo, "title"),
            "tema": campo(testo, "tema"),
            "url": f"/concetti/{f.stem}",
            "definizione": definizione(testo),
            "relazioni": relazioni,
            "risorse": dict(risorse),
        }

    # 2. grado = vicini unici considerando anche i link entranti (grafo non orientato)
    vicini = defaultdict(set)
    for id_, n in nodi.items():
        for r in n["relazioni"]:
            vicini[id_].add(r)
            vicini[r].add(id_)
    for id_, n in nodi.items():
        n["grado"] = len(vicini[id_])

    # 3. "fondamentale": selezione STRATIFICATA per tema, non per grado assoluto.
    #    Il grado grezzo premia i temi le cui sezioni "Pagine collegate" sono state
    #    scritte più densamente (artefatto dei lotti di ingest), non i concetti più
    #    importanti: a grado puro il pensiero computazionale resterebbe fuori.
    #    Quindi: i più connessi DENTRO ciascun tema, con un minimo garantito per tema.
    PER_TEMA, TARGET = 5, 70
    for n in nodi.values():
        n["fondamentale"] = False

    per_tema = defaultdict(list)
    for n in nodi.values():
        per_tema[n["tema"]].append(n)

    for gruppo in per_tema.values():
        for n in sorted(gruppo, key=lambda x: (-x["grado"], x["titolo"]))[:PER_TEMA]:
            n["fondamentale"] = True

    # completa fino al target con i più connessi fra i restanti
    restanti = sorted((n for n in nodi.values() if not n["fondamentale"]),
                      key=lambda x: (-x["grado"], x["titolo"]))
    for n in restanti[:max(0, TARGET - sum(x["fondamentale"] for x in nodi.values()))]:
        n["fondamentale"] = True

    temi = sorted({n["tema"] for n in nodi.values() if n["tema"]})
    dati = {
        "generato_da": "scripts/export_sfera.py (EduWiki Tecnologia)",
        "fonte": "https://eduwiki-tecnologia.vercel.app",
        "licenza": "CC BY-SA 4.0",
        "totale_concetti": len(nodi),
        "totale_fondamentali": sum(1 for n in nodi.values() if n["fondamentale"]),
        "temi": temi,
        "nodi": [nodi[k] for k in sorted(nodi)],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dati, ensure_ascii=False, indent=1), encoding="utf-8")

    archi = sum(len(n["relazioni"]) for n in nodi.values())
    isolati = [n["id"] for n in nodi.values() if n["grado"] == 0]
    print(f"  concetti:      {len(nodi)}")
    print(f"  archi:         {archi}  (grado medio {2*archi/len(nodi):.1f})")
    print(f"  fondamentali:  {dati['totale_fondamentali']}  (stratificati: min {PER_TEMA}/tema)")
    print(f"  temi:          {len(temi)}")
    print(f"  isolati:       {len(isolati)} {isolati or ''}")
    if non_risolti:
        tot = sum(len(v) for v in non_risolti.values())
        mancanti = sorted({l for v in non_risolti.values() for l in v})
        print(f"  link non risolti: {tot} verso {len(mancanti)} pagine inesistenti")
        print(f"     {', '.join(mancanti[:12])}{' ...' if len(mancanti) > 12 else ''}")
    print(f"\n  scritto: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
