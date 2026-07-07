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
ENRICH_SCRIPT = Path(__file__).parent / "enrich_multimedia.py"

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
WIKI_IMG_RE = re.compile(r"!\[[^\]]*\]\((https://upload\.wikimedia\.org/[^\)]+)\)")


def extract_wiki_image(text):
    """Estrae l'URL dell'immagine Wikipedia già iniettata da enrich_multimedia.py
    (prima immagine upload.wikimedia.org trovata nella pagina)."""
    m = WIKI_IMG_RE.search(text)
    return m.group(1) if m else None


def extract_stato(text):
    """Legge il campo 'stato:' dal frontmatter YAML (bozza | da_validare |
    validato) senza un parser YAML completo: una riga sola, valore semplice."""
    fm = FRONTMATTER_RE.match(text)
    if not fm:
        return None
    m = re.search(r"^stato:\s*(\S+)\s*$", fm.group(0), re.M)
    return m.group(1) if m else None


def clean_text(text):
    """Rimuove wikilink, grassetto/corsivo markdown e spazi ridondanti.
    Nessun troncamento: la descrizione riporta il testo integrale della
    sezione sorgente."""
    # taglia via immagini iniettate (Wikipedia) e relativa didascalia, che
    # 'enrich_multimedia.py' inserisce subito dopo Definizione breve senza
    # un heading separato (spesso precedute da un separatore "---")
    text = text.split("![", 1)[0]
    text = re.sub(r"\n---\s*$", "", text.rstrip())
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


def parse_yt_map():
    """Rilegge YT_MAP da enrich_multimedia.py (slug concetto → video YouTube),
    senza importare il modulo (che ha effetti collaterali: chiamate di rete
    e scritture su disco al top-level)."""
    src = ENRICH_SCRIPT.read_text(encoding="utf-8")
    m = re.search(r"YT_MAP = \{(.*?)\n\}", src, re.S)
    entries = re.findall(
        r'"([\w-]+)":\s*\("([\w-]+)",\s*"([^"]+)",\s*"([^"]+)"\)', m.group(1)
    )
    return {slug: {"video_id": vid, "title": title, "channel": ch}
            for slug, vid, title, ch in entries}


def parse_content_files(dir_path, area_type, yt_map=None):
    elements = {}
    for f in sorted(dir_path.glob("*.md")):
        if f.name == "README.md":
            continue
        slug = f.stem
        raw = f.read_text(encoding="utf-8")
        title, desc = extract_title_and_description(raw)
        if area_type == "Prompt":
            title = re.sub(r"^Prompt\s*—\s*", "", title or slug)
        el = {
            "id": slug,
            "label": title or slug,
            "type": area_type,
            "description": desc,
        }
        if area_type == "Concetto":
            img = extract_wiki_image(raw)
            if img:
                el["Image"] = img
        stato = extract_stato(raw)
        if stato:
            el["stato"] = stato
        video = yt_map.get(slug) if yt_map else None
        if video:
            # sintassi widget di Kumu per l'embed YouTube nel pannello elemento:
            # [[youtube/VIDEO_ID]] dentro il campo description
            el["description"] += (
                f"\n\n📺 {video['title']} · {video['channel']}\n"
                f"[[youtube/{video['video_id']}]]"
            )
            el["video"] = True
        elements[slug] = el
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
    yt_map = parse_yt_map()
    for area_dir, area_type in AREE.items():
        folder = WIKI / area_dir
        if folder.exists():
            map_for_area = yt_map if area_dir == "02-concetti" else None
            elements.update(parse_content_files(folder, area_type, map_for_area))

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

    # 4. conteggio connessioni per elemento (centralità/grado), per dimensionare
    # i nodi via `element-size: scale("connessioni", min, max)` in Kumu
    degree = {}
    for c in connections:
        degree[c["from"]] = degree.get(c["from"], 0) + 1
        degree[c["to"]] = degree.get(c["to"], 0) + 1
    for el in elements.values():
        el["connessioni"] = degree.get(el["id"], 0)

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
    with_video = sum(1 for e in elements.values() if e.get("video"))
    with_image = sum(1 for e in elements.values() if e.get("Image"))
    with_stato = sum(1 for e in elements.values() if e.get("stato"))
    top_hubs = sorted(elements.values(), key=lambda e: -e["connessioni"])[:5]
    print(f"\nTotale elementi:    {len(elements)}")
    print(f"Totale connessioni: {len(connections)}")
    print(f"Elementi con video embeddato: {with_video}")
    print(f"Elementi con immagine (Image): {with_image}")
    print(f"Elementi con campo stato: {with_stato}")
    print("Concetti più connessi (hub):")
    for e in top_hubs:
        print(f"  {e['connessioni']:3d}  {e['id']}")
    print(f"Scritto in: {OUT}")


if __name__ == "__main__":
    main()
