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
    # Fisica / Elettricità / Macchine
    "algoritmo-e-diagrammi-di-flusso":     "Diagramma di flusso",
    "analogico-e-digitale-il-segnale":     "Segnale analogico",
    "attrito-e-vantaggio-meccanico":       "Forza",
    "carrucola-verricello-paranco":        "Carrucola",
    "effetti-della-corrente-elettrica":    "Corrente elettrica",
    "elettronica-di-base":                 "Elettronica",
    "forme-e-trasformazioni-dell-energia": "Energia",
    "generatori-e-pile":                   "Pila elettrica",
    "grandezze-elettriche-e-circuito":     "Circuito elettrico",
    "il-motore-elettrico":                 "Motore elettrico",
    "macchine-semplici-leva":              "Leva (fisica)",
    "magnetismo-ed-elettromagnetismo":     "Elettromagnetismo",
    "motore-a-combustione-interna":        "Motore a combustione interna",
    "motore-diesel":                       "Motore diesel",
    "motori-e-propulsione":                "Motore",
    "piano-inclinato-vite-cuneo":          "Piano inclinato",
    "trasmissione-del-moto":               "Ingranaggio",
    "trasformazione-del-moto":             "Meccanismo biella-manovella",
    # Materiali
    "i-materiali-ceramici":                "Ceramica",
    "i-metalli-e-le-leghe":               "Metallurgia",
    "i-nuovi-materiali":                   "Nanotecnologia",
    "il-legno":                            "Legno",
    "la-carta":                            "Carta",
    "le-fibre-tessili":                    "Seta",
    "materie-plastiche-e-gomme":           "Materia plastica",
    "materiali-da-costruzione-e-cemento-armato": "Cemento armato",
    "proprieta-e-classificazione-dei-materiali": "Scienza dei materiali",
    # Edilizia / Strutture / Disegno
    "arco-e-strutture-spingenti":          "Arco (architettura)",
    "assonometrie":                        "Assonometria",
    "bioedilizia-ed-efficienza-energetica": "Casa passiva",
    "costruire-un-edificio-dalle-fondazioni-al-tetto": "Edilizia",
    "costruzioni-geometriche":             "Geometria euclidea",
    "impianti-dell-abitazione":            "Termosifone",
    "impianto-elettrico-domestico":        "Impianto elettrico",
    "ponti-tipologie-e-forze":             "Ponte",
    "poligoni-regolari-e-curve":           "Poligono regolare",
    "scale-di-riduzione-e-quotatura":      "Disegno tecnico",
    "strumenti-del-disegno-tecnico":       "Disegno tecnico",
    "struttura-modulare-e-disegno-geometrico": "Modulo (architettura)",
    "strutture-portanti-e-sollecitazioni": "Struttura portante",
    # Energia / Ambiente / Clima
    "cambiamento-climatico-ed-effetto-serra": "Riscaldamento globale",
    "combustibili-fossili-carbone-petrolio-gas": "Combustibile fossile",
    "energia-solare-fotovoltaico-e-termico": "Pannello fotovoltaico",
    "fonti-rinnovabili-e-non-rinnovabili": "Energia rinnovabile",
    "geotermia-e-biomasse":                "Energia geotermica",
    "inquinamento-aria-acqua-suolo":       "Inquinamento",
    "rifiuti-e-raccolta-differenziata":    "Raccolta differenziata",
    "riciclo-e-sostenibilita-dei-materiali": "Riciclaggio",
    "risorse-rinnovabili-e-non-rinnovabili": "Risorsa rinnovabile",
    "risparmio-energetico-e-efficienza":   "Efficienza energetica",
    # Digitale / AI / Comunicazione
    "coding-e-programmazione-a-blocchi":   "Linguaggio di programmazione visuale",
    "diritto-d-autore-e-licenze":          "Copyright",
    "domotica-e-casa-intelligente":        "Domotica",
    "grafica-raster-e-vettoriale":         "Elaborazione digitale delle immagini",
    "intelligenza-artificiale-a-scuola":   "Intelligenza artificiale",
    "internet-e-il-web":                   "Internet",
    "la-comunicazione-elementi-e-modello": "Comunicazione",
    "la-fotografia-dall-analogico-al-digitale": "Fotografia digitale",
    "pensiero-computazionale":             "Pensiero computazionale",
    "radio-televisione-e-cinema":          "Televisione",
    "realta-aumentata":                    "Realtà aumentata",
    "realta-virtuale":                     "Realtà virtuale",
    "robotica-educativa":                  "Robotica",
    "sensori-e-attuatori":                 "Termometro",
    "social-network-e-cittadinanza-digitale": "Instagram",
    "tecnologia-e-tecnica":                "Tecnologia",
    "telefonia-e-telecomunicazioni":       "Telefono cellulare",
    # Trasporti
    "infrastrutture-di-trasporto":         "Infrastruttura",
    "logistica-e-trasporto-intermodale":   "Trasporto intermodale",
    "mobilita-sostenibile-e-trasporto-green": "Mobilità sostenibile",
    "sistema-dei-trasporti-e-mobilita":    "Sistema di trasporto",
    "smart-city-e-mobilita-sostenibile":   "Città intelligente",
    "trasporto-aereo":                     "Aviazione",
    "trasporto-spaziale":                  "Esplorazione spaziale",
    "trasporto-su-acqua-e-navi":           "Nave",
    "trasporto-su-gomma-e-automobile":     "Automobile",
    # Economia
    "agenda-2030":                         "Obiettivi di sviluppo sostenibile",
    "bisogni-e-risorse":                   "Piramide di Maslow",
    "fattori-e-ciclo-della-produzione":    "Catena del valore",
    "globalizzazione-ed-economia-sostenibile": "Globalizzazione",
    "i-settori-produttivi":                "Settore economico",
    "il-mondo-del-lavoro":                 "Mercato del lavoro",
    "moneta-banche-e-finanza":             "Banca",
    "moneta-elettronica-e-pagamenti-digitali": "Moneta elettronica",
    "settore-primario-agricoltura-allevamento-pesca": "Settore primario",
    "settore-secondario-industria-e-artigianato": "Industria",
    "settore-terziario-commercio-trasporti-servizi": "Commercio",
    "sistema-economico-e-mercato":         "Mercato",
    # Agricoltura / Alimentazione
    "agricoltura-sostenibile-e-biologica": "Agricoltura biologica",
    "alimentazione-equilibrata-e-piramide-alimentare": "Dieta mediterranea",
    "alimenti-da-fermentazione-vino-birra-olio": "Vino",
    "allevamento-e-zootecnia":             "Allevamento",
    "carne-pesce-e-uova":                  "Carne",
    "coltivazioni-fuori-suolo-serra-idroponica": "Idroponica",
    "conservazione-degli-alimenti":        "Frigorifero",
    "etichette-e-sicurezza-alimentare":    "Additivo alimentare",
    "filiera-agroalimentare":              "Industria alimentare",
    "macchine-e-tecniche-agricole":        "Macchina agricola",
    "ogm-e-biotecnologie-agrarie":         "Biotecnologia",
    "pesca-e-acquacoltura":                "Acquacoltura",
    "principi-nutritivi":                  "Nutriente",
    "produzioni-vegetali-e-colture":       "Cereale",
    "terreno-e-clima-in-agricoltura":      "Pedologia",
    "trasformazione-dei-cereali-pane-e-pasta": "Pane",
    "latte-e-derivati":                    "Latte",
    "citta-e-urbanistica":                 "Urbanistica",
    "dalla-scrittura-alla-stampa":         "Stampa",
    "sicurezza-elettrica":                 "Sicurezza elettrica",
}

# ── YouTube mapping ────────────────────────────────────────────────────────────
# slug → (video_id, titolo, canale) — titolo/canale verificati via YouTube oEmbed API
# Solo fonti autorevoli: Geopop (divulgazione scientifica) e canali istituzionali.
# Video da canali minori/non verificabili rimossi (2026-07-06): in attesa di
# sostituzione con fonti Geopop, istituzionali o canali di editori scolastici.
YT_MAP = {
    # Energia
    "energia-nucleare":               ("o9AKgqvEI4E", "Fusione nucleare USA, perché sono tutti così eccitati per la scoperta?", "Geopop"),
    "energia-solare-fotovoltaico-e-termico": ("mj6_WVh2HwU", "Come funziona un pannello solare dall'interno?", "Geopop"),
    # Ambiente / Clima
    "sviluppo-sostenibile":           ("JQ5Dq74GhnU", "Il riscaldamento globale e le sue cause spiegate con un cicchetto", "Geopop"),
    "agenda-2030":                    ("JQ5Dq74GhnU", "Il riscaldamento globale e le sue cause spiegate con un cicchetto", "Geopop"),
    "impronta-ecologica":             ("JQ5Dq74GhnU", "Il riscaldamento globale e le sue cause spiegate con un cicchetto", "Geopop"),
    # Digitale
    "internet-e-il-web":              ("njPXISDTodo", "Come funziona davvero una rete Wi-Fi pubblica", "Geopop"),
    # Motori / Macchine
    "motore-a-combustione-interna":   ("9zCOpQ8pEgg", "Guardiamo attraverso un motore 4 tempi: come funziona dall'interno", "Geopop"),
    # Materiali / Economia circolare
    "economia-circolare":             ("ni8-BuHUzUg", "Economia circolare - L'economia circolare spiegata bene", "Ministero Ambiente e Sicurezza Energetica"),
    "riciclo-e-sostenibilita-dei-materiali": ("1EoeGgrAtJ4", "Il riciclo della plastica", "CONAI"),
    # Fonti rinnovabili — S. Lattes & C. Editori
    "fonti-rinnovabili-e-non-rinnovabili": ("Z6KbUUakaYE", "Le energie rinnovabili", "S. Lattes & C. Editori"),
    # Cambiamento climatico — Mondadori Education
    "cambiamento-climatico-ed-effetto-serra": ("J-joQ3l_xGk", "Webinar - Evidenze scientifiche del cambiamento climatico", "Mondadori Education"),
    # Intelligenza artificiale — Zanichelli (serie "Dentro l'IA")
    "intelligenza-artificiale-a-scuola": ("MJlrabo6ARk", "Dentro l'IA - 1. Come imparano le reti neurali?", "Zanichelli editore"),
    # Pensiero computazionale — Mondadori Education
    "pensiero-computazionale":         ("JBofYa87CRU", "Webinar - Il pensiero computazionale", "Mondadori Education"),
    # Coding a blocchi — Mondadori Education
    "coding-e-programmazione-a-blocchi": ("zxF5aybKJMY", "Coding a blocchi con Scratch", "Mondadori Education"),
    # Robotica educativa — Mondadori Education
    "robotica-educativa":             ("nEq-BUaR3GQ", "Webinar - Tinkering e robotica educativa: la robotica educativa per il curriculum scientifico", "Mondadori Education"),
    # Smart city e mobilità sostenibile — Zanichelli editore
    "smart-city-e-mobilita-sostenibile": ("JuyPkww6s-U", "La città ideale e le città sostenibili (tratto da Artelogia)", "Zanichelli editore"),
    # Cittadinanza digitale — Mondadori Education
    "social-network-e-cittadinanza-digitale": ("-kr34d7b1IQ", "Cittadinanza digitale | con Daniele Aristarco", "Mondadori Education"),
    # Energia eolica — Geopop
    "energia-eolica":                  ("GmZCO7TZd9U", "Haliade X: la pala eolica più grande del mondo", "Geopop"),
    # Motore elettrico — Tecnologia Duepuntozero
    "il-motore-elettrico":             ("2LIO7TEKook", "Laboratorio: motorino elettrico", "Tecnologia Duepuntozero"),
    # Domotica — S. Lattes & C. Editori
    "domotica-e-casa-intelligente":    ("dAIkxQUDRI0", "Alcuni esempi di domotica", "S. Lattes & C. Editori"),
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

# ── Markdown builder ─────────────────────────────────────────────────────────

# Pattern per rimuovere immagini Wikipedia precedentemente iniettate
WIKI_IMG_RE = re.compile(
    r'\n\n!\[[^\]]*\]\(https://upload\.wikimedia\.org/[^\)]+\)\n\*📖[^\n]*\*',
)

# Pattern per rimuovere il blocco video precedentemente iniettato (in qualsiasi posizione)
VIDEO_FIGURE_RE = re.compile(
    r'\n*<figure>\n<iframe src="https://www\.youtube-nocookie\.com/embed/.*?</figure>\n*',
    re.S,
)

def md_wiki(info):
    desc  = info["caption"] if info["caption"] else info["title"]
    wikil = f"[Wikipedia]({info['wiki']})" if info["wiki"] else "Wikipedia"
    return f"![{info['title']}]({info['src']})\n*📖 {desc} · {wikil} · CC BY-SA*"

def md_yt(video_id, title, channel):
    """iframe reale: supportato nativamente sia da Quartz che da Obsidian Reading View.
    figure/figcaption in un unico blocco HTML: evita che la riga successiva
    (senza riga vuota) venga inglobata come HTML raw invece che come markdown."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    return (
        f'<figure>\n'
        f'<iframe src="https://www.youtube-nocookie.com/embed/{video_id}" '
        f'width="100%" style="aspect-ratio:16/9;border:none;border-radius:8px" '
        f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
        f'referrerpolicy="strict-origin-when-cross-origin" '
        f'allowfullscreen loading="lazy" title="{title}"></iframe>\n'
        f'<figcaption>📺 {title} · {channel} · '
        f'<a href="{url}" target="_blank">Guarda su YouTube</a></figcaption>\n'
        f'</figure>'
    )

def insert_after_definition(text, block):
    """Inserisce un blocco (immagine e/o video) subito dopo ## Definizione breve,
    quindi prima di ## Spiegazione per docenti. Riga vuota dopo il blocco
    obbligatoria: senza, l'heading successivo viene inglobato nell'HTML raw."""
    m = re.search(r'(## Definizione breve\n(?:(?!^##).)*)', text, re.S | re.M)
    if not m:
        return text + "\n\n" + block + "\n"  # fallback in fondo
    end = m.end()
    return text[:end].rstrip('\n') + '\n\n' + block + '\n\n' + text[end:].lstrip('\n')

# ── main ──────────────────────────────────────────────────────────────────────

def process_folder(content_dir: Path, label: str):
    updated = no_media = 0
    for page in sorted(content_dir.glob("*.md")):
        if page.name == "README.md":
            continue
        slug = page.stem
        txt  = page.read_text(encoding="utf-8")

        # Rimuovi eventuale vecchia sezione "Risorse multimediali" in fondo (idempotente)
        txt_clean = re.sub(rf"\n\n{re.escape(MARKER)}.*", "", txt, flags=re.S)
        # Rimuovi immagine Wikipedia e video YouTube eventualmente già iniettati
        txt_clean = WIKI_IMG_RE.sub("", txt_clean)
        txt_clean = VIDEO_FIGURE_RE.sub("\n\n", txt_clean)

        h1   = extract_h1(txt_clean)
        wiki = get_wiki_info(h1, slug) if h1 else None
        yt   = YT_MAP.get(slug)

        if not wiki and not yt:
            no_media += 1
            continue

        # Immagine Wikipedia e video YouTube, entrambi subito dopo ## Definizione breve
        blocks = []
        if wiki:
            blocks.append(md_wiki(wiki))
        if yt:
            vid, title, ch = yt
            blocks.append(md_yt(vid, title, ch))
        result = insert_after_definition(txt_clean, "\n\n".join(blocks))

        page.write_text(result, encoding="utf-8")
        parts = []
        if wiki: parts.append(f"🖼 {wiki['title'][:35]}")
        if yt:   parts.append(f"📺 {yt[0]}")
        print(f"  OK  {slug:55s} {' + '.join(parts)}")
        updated += 1

    print(f"\n[{label}] ✓ Aggiornate: {updated}  ·  Senza media: {no_media}\n")

print("=== Quartz (content/concetti) — iframe YouTube ===")
process_folder(CONTENT_QUARTZ, "Quartz")
print("=== Obsidian (wiki/02-concetti) — iframe YouTube ===")
process_folder(CONTENT_OBSIDIAN, "Obsidian")
