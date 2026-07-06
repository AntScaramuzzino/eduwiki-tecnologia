"""
build_kumu_map.py — ricrea la struttura del wiki EduWiki LLM come mappa di rete
Kumu (https://kumu.io). Genera un blueprint JSON (elements + connections) a
partire da 00-indice/index.md, 11-glossario/glossario.md e dai wikilink [[...]]
presenti nelle pagine del wiki.

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

INDEX_SECTIONS = {
    "Concetti":            "Concetto",
    "Metodologie":         "Metodologia",
    "Strumenti digitali":  "Strumento digitale",
    "Attività didattiche": "Attività didattica",
    "UDA":                 "UDA",
    "Valutazione":         "Valutazione",
    "Inclusione":          "Inclusione",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]")


def parse_index(index_path):
    """Estrae elementi da 00-indice/index.md: sezioni con righe
    '- [[slug]] — Titolo: descrizione…'"""
    text = index_path.read_text(encoding="utf-8")
    elements = {}
    current_type = None
    for line in text.splitlines():
        h2 = re.match(r"^## ([\w àèéìòù]+)", line)
        if h2:
            current_type = INDEX_SECTIONS.get(h2.group(1).strip())
            continue
        m = re.match(r"^- \[\[([\w-]+)\]\] — ([^:]+):?\s*(.*)$", line)
        if m and current_type:
            slug, title, desc = m.groups()
            elements[slug] = {
                "id": slug,
                "label": title.strip(),
                "type": current_type,
                "description": desc.strip()[:280],
            }
    return elements


def parse_prompt_files(dir_path):
    elements = {}
    for f in sorted(dir_path.glob("*.md")):
        if f.name == "README.md":
            continue
        slug = f.stem
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.M)
        title = m.group(1).strip() if m else slug
        title = re.sub(r"^Prompt\s*—\s*", "", title)
        elements[slug] = {
            "id": slug,
            "label": title,
            "type": "Prompt",
            "description": "",
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
                "description": clean_def[:280],
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

    # 1. elementi da index.md (concetti, metodologie, strumenti, attività, uda, valutazione, inclusione)
    elements.update(parse_index(WIKI / "00-indice" / "index.md"))

    # 2. elementi da 09-prompt (non listati in index.md)
    elements.update(parse_prompt_files(WIKI / "09-prompt"))

    # 3. voci di glossario + collegamenti verso i concetti
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

    # 4. wikilink reali dentro ogni pagina delle aree di contenuto
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
