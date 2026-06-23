"""
enrich_multimedia.py — aggiunge immagine Wikipedia + video YouTube ai concetti EduWiki.

Wikipedia REST API (it): https://it.wikipedia.org/api/rest_v1/page/summary/{title}
YouTube: video curati (Geopop e fonti autorevoli italiane).
"""

import json, re, time, urllib.request, urllib.parse
from pathlib import Path

CONTENT_QUARTZ  = Path("/Users/antonioscaramuzzino/Projects/eduwiki-tecnologia/content/concetti")
CONTENT_OBSIDIAN = Path("/Users/antonioscaramuzzino/Library/CloudStorage/GoogleDrive-antonio.scaramuzzino@coopinrete.it/Il mio Drive/Antonio Scaramuzzino/Brain Tecnologia/eduwiki-llm/wiki/02-concetti")
MARKER = "## Risorse multimediali"

# ── Wikipedia override: slug → titolo articolo it.wikipedia.org ──────────────
WIKI_OVERRIDE = {
    # Fisica / Elettricità
    "algoritmo-e-diagrammi-di-flusso":     "Algoritmo",
    "analogico-e-digitale-il-segnale":     "Segnale analogico",
    "attrito-e-vantaggio-meccanico":       "Attrito",
    "carrucola-verricello-paranco":        "Carrucola",
    "effetti-della-corrente-elettrica":    "Corrente elettrica",
    "elettronica-di-base":                 "Elettronica",
    "forme-e-trasformazioni-dell-energia": "Energia",
    "generatori-e-pile":                   "Pila elettrica",
    "grandezze-elettriche-e-circuito":     "Circuito elettrico",
    "macchine-semplici-leva":              "Leva (fisica)",
    "magnetismo-ed-elettromagnetismo":     "Elettromagnetismo",
    "motore-diesel":                       "Motore diesel",
    "motori-e-propulsione":                "Motore",
    "piano-inclinato-vite-cuneo":          "Piano inclinato",
    "trasmissione-del-moto":               "Ingranaggio",
    "trasformazione-del-moto":             "Meccanismo biella-manovella",
    # Materiali
    "i-materiali-ceramici":                "Ceramica",
    "i-metalli-e-le-leghe":               "Metallurgia",
    "i-nuovi-materiali":                   "Nanomateriale",
    "il-legno":                            "Legno",
    "la-carta":                            "Carta",
    "le-fibre-tessili":                    "Fibra tessile",
    "materie-plastiche-e-gomme":           "Materia plastica",
    "materiali-da-costruzione-e-cemento-armato": "Cemento armato",
    # Edilizia / Strutture
    "arco-e-strutture-spingenti":          "Arco (architettura)",
    "assonometrie":                        "Assonometria",
    "costruire-un-edificio-dalle-fondazioni-al-tetto": "Edilizia",
    "impianti-dell-abitazione":            "Impianto termico",
    "impianto-elettrico-domestico":        "Impianto elettrico",
    "ponti-tipologie-e-forze":             "Ponte (costruzione)",
    "strumenti-del-disegno-tecnico":       "Disegno tecnico",
    "strutture-portanti-e-sollecitazioni": "Struttura portante",
    # Energia / Ambiente
    "bioedilizia-ed-efficienza-energetica": "Bioedilizia",
    "combustibili-fossili-carbone-petrolio-gas": "Combustibile fossile",
    "geotermia-e-biomasse":                "Energia geotermica",
    "inquinamento-aria-acqua-suolo":       "Inquinamento",
    "rifiuti-e-raccolta-differenziata":    "Raccolta differenziata",
    "risorse-rinnovabili-e-non-rinnovabili": "Risorsa rinnovabile",
    "risparmio-energetico-e-efficienza":   "Efficienza energetica",
    # Digitale / Comunicazione
    "coding-e-programmazione-a-blocchi":   "Linguaggio di programmazione visuale",
    "diritto-d-autore-e-licenze":          "Diritto d'autore",
    "domotica-e-casa-intelligente":        "Domotica",
    "grafica-raster-e-vettoriale":         "Elaborazione digitale delle immagini",
    "la-comunicazione-elementi-e-modello": "Comunicazione",
    "la-fotografia-dall-analogico-al-digitale": "Fotografia digitale",
    "radio-televisione-e-cinema":          "Televisione",
    "realta-aumentata":                    "Realtà aumentata",
    "realta-virtuale":                     "Realtà virtuale",
    "sensori-e-attuatori":                 "Sensore",
    "social-network-e-cittadinanza-digitale": "Social network",
    "tecnologia-e-tecnica":                "Tecnologia",
    "telefonia-e-telecomunicazioni":       "Telefonia",
    # Trasporti
    "infrastrutture-di-trasporto":         "Infrastruttura",
    "logistica-e-trasporto-intermodale":   "Logistica",
    "mobilita-sostenibile-e-trasporto-green": "Mobilità sostenibile",
    "sistema-dei-trasporti-e-mobilita":    "Sistema di trasporto",
    "trasporto-aereo":                     "Aviazione",
    "trasporto-spaziale":                  "Esplorazione spaziale",
    "trasporto-su-acqua-e-navi":           "Nave",
    "trasporto-su-gomma-e-automobile":     "Automobile",
    # Economia
    "bisogni-e-risorse":                   "Bisogno (economia)",
    "fattori-e-ciclo-della-produzione":    "Fattori di produzione",
    "globalizzazione-ed-economia-sostenibile": "Globalizzazione",
    "i-settori-produttivi":                "Settore economico",
    "moneta-banche-e-finanza":             "Banca",
    "moneta-elettronica-e-pagamenti-digitali": "Moneta elettronica",
    "sistema-economico-e-mercato":         "Economia di mercato",
    "il-mondo-del-lavoro":                 "Mercato del lavoro",
    # Agricoltura / Alimentazione
    "agricoltura-sostenibile-e-biologica": "Agricoltura biologica",
    "alimentazione-equilibrata-e-piramide-alimentare": "Dieta mediterranea",
    "alimenti-da-fermentazione-vino-birra-olio": "Fermentazione",
    "allevamento-e-zootecnia":             "Zootecnia",
    "carne-pesce-e-uova":                  "Carne",
    "coltivazioni-fuori-suolo-serra-idroponica": "Idroponica",
    "conservazione-degli-alimenti":        "Conservazione degli alimenti",
    "etichette-e-sicurezza-alimentare":    "Etichettatura degli alimenti",
    "filiera-agroalimentare":              "Filiera agroalimentare",
    "macchine-e-tecniche-agricole":        "Macchina agricola",
    "ogm-e-biotecnologie-agrarie":         "Organismo geneticamente modificato",
    "pesca-e-acquacoltura":                "Acquacoltura",
    "principi-nutritivi":                  "Nutriente",
    "produzioni-vegetali-e-colture":       "Cereale",
    "terreno-e-clima-in-agricoltura":      "Pedologia",
    "trasformazione-dei-cereali-pane-e-pasta": "Pane",
    "latte-e-derivati":                    "Latte",
    "citta-e-urbanistica":                 "Urbanistica",
    "dalla-scrittura-alla-stampa":         "Stampa (editoria)",
    "sicurezza-elettrica":                 "Sicurezza elettrica",
}

# ── YouTube mapping ────────────────────────────────────────────────────────────
# slug → (video_id, titolo, canale)
YT_MAP = {
    # Energia
    "energia-nucleare":               ("o9AKgqvEI4E", "Fusione nucleare: la grande sfida tecnologica", "Geopop"),
    "energia-solare-fotovoltaico-e-termico": ("mj6_WVh2HwU", "Come funziona un pannello solare", "YouTube EDU"),
    "energia-eolica":                 ("y7wD5uajZBI", "Cosa sono le turbine eoliche", "YouTube EDU"),
    "fonti-rinnovabili-e-non-rinnovabili": ("WI9kdCnU3i0", "L'energia rinnovabile è davvero sostenibile?", "YouTube EDU"),
    # Ambiente / Clima
    "cambiamento-climatico-ed-effetto-serra": ("l6P3m74VtIA", "Il cambiamento climatico e l'effetto serra", "Geopop"),
    "sviluppo-sostenibile":           ("JQ5Dq74GhnU", "Il riscaldamento globale: le cause", "Geopop"),
    "agenda-2030":                    ("JQ5Dq74GhnU", "Il riscaldamento globale: le cause", "Geopop"),
    "impronta-ecologica":             ("JQ5Dq74GhnU", "Il riscaldamento globale: le cause", "Geopop"),
    # Digitale / AI
    "intelligenza-artificiale-a-scuola": ("wchtRNrzB10", "L'intelligenza artificiale può pensare?", "Geopop"),
    "internet-e-il-web":              ("njPXISDTodo", "Come funziona una rete Wi-Fi pubblica", "Geopop"),
    # Motori / Macchine
    "motore-a-combustione-interna":   ("9zCOpQ8pEgg", "Come funziona un motore a 4 tempi", "YouTube EDU"),
    "il-motore-elettrico":            ("MSTcV0ubIk8", "Motore elettrico: spiegazione semplice", "YouTube EDU"),
    # Materiali
    "economia-circolare":             ("ni8-BuHUzUg", "L'economia circolare spiegata bene", "YouTube EDU"),
    "riciclo-e-sostenibilita-dei-materiali": ("hn09nndvpEI", "Come viene riciclata la plastica", "YouTube EDU"),
    # Coding / Robotica
    "pensiero-computazionale":        ("pzg1-UpMypA", "La robotica educativa e il pensiero computazionale", "YouTube EDU"),
    "robotica-educativa":             ("pzg1-UpMypA", "La robotica educativa e il pensiero computazionale", "YouTube EDU"),
    # Città / Trasporti
    "smart-city-e-mobilita-sostenibile": ("4ENRgYohsMU", "Urbanistica e mobilità sostenibile", "YouTube EDU"),
}

# ── Wikipedia ─────────────────────────────────────────────────────────────────

def extract_h1(text):
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else ""

def normalize_wiki_title(title):
    """Rimuove articoli italiani iniziali per il lookup Wikipedia."""
    return re.sub(r"^(L'|Il |La |I |Gli |Le |Lo |Un |Una |Un')", "", title)

def get_wiki_info(raw_title, slug=None):
    """Ritorna dict con src, caption, wiki, title oppure None."""
    # Se esiste un override per questo slug, usalo come primo tentativo
    override = WIKI_OVERRIDE.get(slug, "")
    attempts = []
    if override:
        attempts.append(override)
    attempts += [raw_title, normalize_wiki_title(raw_title)]
    # Dedup mantenendo ordine
    seen = set()
    attempts = [t for t in attempts if t not in seen and not seen.add(t)]
    for title in attempts:
        enc = urllib.parse.quote(title.strip(), safe='')
        url = f"https://it.wikipedia.org/api/rest_v1/page/summary/{enc}"
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "EduWiki-Tecnologia/1.0 (antonio.scaramuzzino@coopinrete.it)"}
            )
            with urllib.request.urlopen(req, timeout=8) as r:
                if r.status == 200:
                    d = json.loads(r.read())
                    # Salta disambiguation e redirect circolari
                    if d.get("type") in ("disambiguation",):
                        continue
                    thumb = d.get("thumbnail")
                    if thumb:
                        src = thumb["source"]
                        # Aumenta risoluzione: 320px → 640px
                        src = re.sub(r'/(\d+)px-', '/640px-', src)
                        return {
                            "src":     src,
                            "caption": d.get("description", ""),
                            "wiki":    d.get("content_urls", {}).get("desktop", {}).get("page", ""),
                            "title":   d.get("title", title),
                        }
        except Exception:
            pass
        time.sleep(0.15)
    return None

# ── Markdown builder (compatibile Obsidian + Quartz) ─────────────────────────
# Usa Markdown puro: niente <iframe> (bloccati in Obsidian),
# niente HTML inline non necessario. Le immagini YouTube diventano
# thumbnail cliccabili che aprono il video su YouTube.

def md_wiki(info):
    desc  = info["caption"] if info["caption"] else info["title"]
    wikil = f"[Wikipedia]({info['wiki']})" if info["wiki"] else "Wikipedia"
    return f"![{info['title']}]({info['src']})\n*📖 {desc} · {wikil} · CC BY-SA*"

def md_yt(video_id, title, channel):
    thumb = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    url   = f"https://www.youtube.com/watch?v={video_id}"
    return f"[![▶ {title}]({thumb})]({url})\n*📺 {title} · {channel}*"

def build_section(wiki_info, yt_tuple):
    parts = [f"\n\n{MARKER}\n"]
    if wiki_info:
        parts.append(md_wiki(wiki_info))
    if yt_tuple:
        vid, title, ch = yt_tuple
        parts.append(md_yt(vid, title, ch))
    return "\n\n".join(parts) + "\n"

# ── main ──────────────────────────────────────────────────────────────────────

def process_folder(content_dir: Path, label: str):
    updated = no_media = 0
    for page in sorted(content_dir.glob("*.md")):
        if page.name == "README.md":
            continue
        slug = page.stem
        txt  = page.read_text(encoding="utf-8")

        # Rimuovi sezione multimediale precedente (idempotente)
        txt_clean = re.sub(rf"\n\n{re.escape(MARKER)}.*", "", txt, flags=re.S)

        h1   = extract_h1(txt_clean)
        wiki = get_wiki_info(h1, slug) if h1 else None
        yt   = YT_MAP.get(slug)

        if not wiki and not yt:
            no_media += 1
            continue

        page.write_text(txt_clean + build_section(wiki, yt), encoding="utf-8")
        parts = []
        if wiki: parts.append(f"🖼 {wiki['title'][:35]}")
        if yt:   parts.append(f"📺 {yt[0]}")
        print(f"  OK  {slug:55s} {' + '.join(parts)}")
        updated += 1

    print(f"\n[{label}] ✓ Aggiornate: {updated}  ·  Senza media: {no_media}\n")

print("=== Quartz (content/concetti) ===")
process_folder(CONTENT_QUARTZ, "Quartz")
print("=== Obsidian (wiki/02-concetti) ===")
process_folder(CONTENT_OBSIDIAN, "Obsidian")
