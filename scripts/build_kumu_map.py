"""
build_kumu_map.py — ricrea la struttura del wiki EduWiki LLM come mappa di rete
Kumu (https://kumu.io). Genera un blueprint JSON (elements + connections)
leggendo titolo e descrizione direttamente da ogni pagina (02-concetti,
03-metodologie, ..., 09-prompt), le voci di 11-glossario/glossario.md e i
wikilink [[...]] realmente presenti nelle pagine.

Uso: python3 scripts/build_kumu_map.py
Output: kumu/wiki-map.json (nel repo, servito via GitHub raw per il "remote JSON
link" di Kumu: Kumu non ha API pubblica, ma può linkare una mappa a un JSON
remoto e la ri-scarica a ogni refresh della pagina).
"""
import re
import json
from pathlib import Path

WIKI = Path("/Users/antonioscaramuzzino/Library/CloudStorage/GoogleDrive-antonio.scaramuzzino@coopinrete.it/Il mio Drive/Antonio Scaramuzzino/Brain Tecnologia/eduwiki-llm/wiki")
OUT = Path("/Users/antonioscaramuzzino/Projects/eduwiki-tecnologia/kumu/wiki-map.json")

# area folder → (etichetta tipo Kumu, sezione in index.md)
AREE = {
    "02-concetti":            "Concetto",
    "03-metodologie":         "Metodologia",
    "04-strumenti-digitali":  "Strumento digitale",
    "05-attivita-didattiche": "Attività didattica",
    "06-uda":                 "UDA",
    "07-valutazione":         "Valutazione",
    "08-inclusione":          "Inclusione",
    "09-prompt":              "Prompt",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.S)
MD_EMPHASIS_RE = re.compile(r"\*\*([^*]+)\*\*|\*([^*]+)\*")


def clean_text(text):
    """Rimuove wikilink, grassetto/corsivo markdown e spazi ridondanti.
    Nessun troncamento: la descrizione riporta il testo integrale della
    sezione sorgente."""
    # taglia via immagini iniettate (Wikipedia) e relativa didascalia, che
    # 'enrich_multimedia.py' inserisce subito dopo Definizione breve senza
    # un heading separato
    text = text.split("![", 1)[0]
    text = WIKILINK_RE.sub(lambda m: m.group(1), text)
    text = MD_EMPHASIS_RE.sub(lambda m: m.group(1) or m.group(2), text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_title_and_description(text):
    """Titolo = primo H1. Descrizione = testo della prima sezione '## ...'
    (Definizione breve, Target, ecc.), o il testo subito dopo l'H1 se non
    ci sono sezioni (es. pagine-stub)."""
    body = FRONTMATTER_RE.sub("", text, count=1)
    h1 = re.search(r"^#\s+(.+)$", body, re.M)
    title = h1.group(1).strip() if h1 else None

    after_h1 = body[h1.end():] if h1 else body
    first_section = re.search(r"^##\s+.+?\n(.*?)(?=\n##\s|\Z)", after_h1, re.S | re.M)
    if first_section:
        desc = clean_text(first_section.group(1))
    else:
        # pagina senza sezioni: testo (es. blockquote di stub) subito dopo l'H1
        desc = clean_text(after_h1)
    return title, desc


def parse_content_files(dir_path, area_type):
    elements = {}
    for f in sorted(dir_path.glob("*.md")):
        if f.name == "README.md":
            continue
        slug = f.stem
        title, desc = extract_title_and_description(f.read_text(encoding="utf-8"))
        if area_type == "Prompt":
            title = re.sub(r"^Prompt\s*—\s*", "", title or slug)
        elements[slug] = {
            "id": slug,
            "label": title or slug,
            "type": area_type,
            "description": desc,
        }
    return elements


def parse_glossario(glossario_path):
    """Estrae voci dal glossario: '- **Termine** — definizione. Vedi [[slug]].'
    Ogni voce diventa un elemento di tipo Glossario collegato al concetto."""
    text = glossario_path.read_text(encoding="utf-8")
    elements = {}
    links = []  # (glossario_id, concetto_slug)
    current_tema = None
    for line in text.splitlines():
        h2 = re.match(r"^## Tema: (.+)$", line)
        if h2:
            current_tema = h2.group(1).strip()
            continue
        m = re.match(r"^- \*\*(.+?)\*\*\s*—\s*(.+)$", line)
        if m:
            term, definition = m.groups()
            gid = "glossario:" + re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
            targets = WIKILINK_RE.findall(definition)
            clean_def = WIKILINK_RE.sub("", definition).replace("Vedi", "").strip(" .")
            elements[gid] = {
                "id": gid,
                "label": term,
                "type": "Glossario",
                "tema": current_tema or "",
                "description": clean_def,
            }
            for t in targets:
                links.append((gid, t))
    return elements, links


def extract_wikilinks(md_path):
    text = md_path.read_text(encoding="utf-8")
    # non contare i link nella sezione "Micro-competenze collegate" (card HTML iniettate)
    text = re.sub(r"\n\n## Micro-competenze collegate.*", "", text, flags=re.S)
    return WIKILINK_RE.findall(text)


def main():
    elements = {}
    connections = []
    seen_conn = set()

    # 1. elementi letti direttamente da ogni pagina di contenuto (titolo H1 +
    # descrizione dalla prima sezione "## ..."), non da index.md che contiene
    # solo estratti già troncati.
    for area_dir, area_type in AREE.items():
        folder = WIKI / area_dir
        if folder.exists():
            elements.update(parse_content_files(folder, area_type))

    # 2. voci di glossario + collegamenti verso i concetti
    gloss_elements, gloss_links = parse_glossario(WIKI / "11-glossario" / "glossario.md")
    elements.update(gloss_elements)

    def add_conn(src, dst, ctype="collegamento"):
        key = (src, dst, ctype)
        if src == dst or key in seen_conn:
            return
        seen_conn.add(key)
        connections.append({"from": src, "to": dst, "type": ctype})

    for gid, target_slug in gloss_links:
        if target_slug in elements:
            add_conn(gid, target_slug, "definisce")

    # 3. wikilink reali dentro ogni pagina delle aree di contenuto
    missing_added = set()
    for area_dir, area_type in AREE.items():
        folder = WIKI / area_dir
        if not folder.exists():
            continue
        for md_file in sorted(folder.glob("*.md")):
            if md_file.name == "README.md":
                continue
            slug = md_file.stem
            if slug not in elements:
                continue  # non dovrebbe accadere: ogni file reale è indicizzato
            targets = extract_wikilinks(md_file)
            for t in targets:
                t = t.strip()
                if t in ("index", "panoramica", "log"):
                    continue  # pagine meta, escluse dalla rete
                if t not in elements and t not in missing_added:
                    elements[t] = {
                        "id": t,
                        "label": t.replace("-", " ").capitalize(),
                        "type": "Pagina mancante",
                        "description": "Wikilink presente nel wiki ma pagina non ancora creata.",
                    }
                    missing_added.add(t)
                add_conn(slug, t, "collegamento")

    blueprint = {
        "elements": list(elements.values()),
        "connections": connections,
    }

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(blueprint, ensure_ascii=False, indent=2), encoding="utf-8")

    by_type = {}
    for el in elements.values():
        by_type[el["type"]] = by_type.get(el["type"], 0) + 1
    print("Elementi per tipo:")
    for t, n in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t:25s} {n}")
    print(f"\nTotale elementi:    {len(elements)}")
    print(f"Totale connessioni: {len(connections)}")
    print(f"Scritto in: {OUT}")


if __name__ == "__main__":
    main()
