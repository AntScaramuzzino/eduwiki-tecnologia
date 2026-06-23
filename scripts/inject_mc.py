"""
inject_mc.py — inietta card MC + mappa nei concetti EduWiki.

Per ogni mapping slug → [mc_ids] aggiunge in fondo alla pagina .md
una sezione ## Micro-competenze collegate con le card HTML inline.
"""

import json, re
from pathlib import Path

# ─── percorsi ────────────────────────────────────────────────────────────────
CONTENT   = Path("/Users/antonioscaramuzzino/Projects/eduwiki-tecnologia/content")
MC_DIR    = Path("/Users/antonioscaramuzzino/Projects/ProfTecnologIA/data/mc")
BASE_URL  = "https://proftecnologia.vercel.app/mc"

# ─── mapping slug EduWiki → [MC ID] ─────────────────────────────────────────
MAPPING = {
    # Coding / Robotica / Pensiero computazionale
    "pensiero-computazionale":        ["MC-DIG-3-01"],
    "coding-e-programmazione-a-blocchi": ["MC-DIG-2-01"],
    "intelligenza-artificiale-a-scuola": ["MC-DIG-3-02"],
    "scratch":                        ["MC-DIG-2-01"],
    "micro-bit":                      ["MC-DIG-3-01"],
    "robotica-educativa":             ["MC-DIG-3-01"],
    "dati-e-sensori":                 ["MC-DIG-3-03"],
    # Digitale / Sicurezza
    "cittadinanza-digitale":          ["MC-DIG-1-01", "MC-DIG-1-02"],
    "social-network-e-cittadinanza-digitale": ["MC-COM-3-02", "MC-COM-3-06"],
    "privacy-e-dati-personali":       ["MC-DIG-2-02"],
    "sicurezza-informatica":          ["MC-DIG-2-04"],
    "intelligenza-artificiale-etica-e-societa": ["MC-DIG-3-02"],
    # Disegno tecnico
    "norme-del-disegno-tecnico":      ["MC-DIS-1-01"],
    "scale-di-rappresentazione":      ["MC-DIS-1-02"],
    "proiezioni-ortogonali":          ["MC-DIS-2-01"],
    "assonometria":                   ["MC-DIS-2-02"],
    "disegno-cad-e-modellazione-3d":  ["MC-DIS-3-02"],
    # Materiali
    "classificazione-dei-materiali":  ["MC-MAT-1-01"],
    "ciclo-di-vita-dei-materiali":    ["MC-MAT-1-02"],
    "materiali-innovativi-e-nanotecnologie": ["MC-MAT-1-03", "MC-MAT-1-06"],
    "riciclaggio-e-economia-circolare": ["MC-MAT-1-04"],
    # Agricoltura / Alimentazione
    "agricoltura-sostenibile-e-biologica": ["MC-ALI-2-01"],
    "industria-alimentare-e-conservazione": ["MC-ALI-2-02"],
    "etichette-e-tracciabilita-degli-alimenti": ["MC-ALI-2-04"],
    "sprechi-alimentari-e-sostenibilita": ["MC-ALI-2-05"],
    # Edilizia / Abitazione
    "strutture-edilizie-e-materiali-da-costruzione": ["MC-AMB-2-01"],
    "impianti-domestici":             ["MC-AMB-2-02"],
    "citta-e-spazio-urbano":          ["MC-AMB-2-03"],
    "smart-city-e-mobilita-sostenibile": ["MC-AMB-2-05"],
    "bioedilizia-ed-efficienza-energetica": ["MC-AMB-2-04"],
    # Energia
    "fonti-rinnovabili-e-non-rinnovabili": ["MC-ENE-3-03", "MC-ENE-3-02"],
    "energia-solare-fotovoltaico":    ["MC-ENE-3-03"],
    "energia-eolica":                 ["MC-ENE-3-03"],
    "energia-nucleare":               ["MC-ENE-3-02"],
    "impianto-elettrico-domestico":   ["MC-ENE-3-04", "MC-AMB-2-02"],
    # Macchine / Motori
    "macchine-semplici-leve-e-ingranaggi": ["MC-ENE-3-01"],
    "il-motore-elettrico":            ["MC-ENE-3-04", "MC-ENE-3-05"],
    "motore-a-combustione-interna":   ["MC-ENE-3-05"],
    "accumulatori-e-batterie":        ["MC-ENE-3-06"],
    # Comunicazione / Media
    "la-comunicazione-elementi-e-modello": ["MC-COM-3-01"],
    "telefonia-e-telecomunicazioni":  ["MC-COM-3-01"],
    "reti-di-computer-e-internet":    ["MC-COM-3-05"],
    "social-network-e-cittadinanza-digitale": ["MC-COM-3-02", "MC-COM-3-06"],
    "domotica-e-industria-4-0":       ["MC-COM-3-04"],
    "sistema-dei-trasporti-e-mobilita": ["MC-COM-3-03"],
    "mobilita-sostenibile-e-trasporto-green": ["MC-COM-3-03"],
    # Economia
    "sistema-economico-e-mercato":    ["MC-SIS-3-01"],
    "settori-produttivi":             ["MC-SIS-3-04"],
    "globalizzazione-ed-economia-sostenibile": ["MC-SIS-3-02"],
    "imprenditorialita-e-innovazione": ["MC-SIS-3-03"],
}

# ─── colori area ─────────────────────────────────────────────────────────────
AREA_COLOR = {
    "DIG": "#3b82f6", "DIS": "#8b5cf6", "MAT": "#f59e0b",
    "ENE": "#f97316", "AMB": "#10b981", "ALI": "#84cc16",
    "COM": "#06b6d4", "SIS": "#ec4899",
}
AREA_LABEL = {
    "DIG": "Digitale", "DIS": "Disegno", "MAT": "Materiali",
    "ENE": "Energia",  "AMB": "Edilizia/Ambiente", "ALI": "Alimentazione",
    "COM": "Comunicazione", "SIS": "Sistema produttivo",
}

FW_COLOR = {
    "IN":  "#6366f1", "DC": "#0ea5e9", "EC": "#f59e0b",
    "LC":  "#10b981", "EV": "#84cc16",
}
FW_LABEL = {
    "IN": "IN 2025",  "DC": "DigComp 3.0",  "EC": "EntreComp",
    "LC": "LifeComp", "EV": "Agenda 2030",
}

# ─── carica tutti gli MC in memoria ─────────────────────────────────────────
MC_DATA = {}
for f in MC_DIR.rglob("*.json"):
    d = json.loads(f.read_text())
    MC_DATA[d["id"]] = d

# ─── genera HTML card per un MC ─────────────────────────────────────────────
def mc_card(mc_id: str) -> str:
    d = MC_DATA.get(mc_id)
    if not d:
        return f'<p><a href="{BASE_URL}/{mc_id}" target="_blank">{mc_id}</a></p>'

    area  = d["area"]
    color = AREA_COLOR.get(area, "#64748b")
    fw    = d.get("frameworks", {})
    zona_tabs = ["⚡ INNESCA", "📖 ESPLORA", "🔍 OSSERVA", "🔬 SPERIMENTA", "🌍 AGISCI"]

    # badge framework
    fw_badges = "".join(
        f'<span style="background:{FW_COLOR.get(k,"#94a3b8")};color:#fff;'
        f'padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;'
        f'margin-right:4px">{FW_LABEL.get(k,k)}</span>'
        for k, v in fw.items() if v
    )

    # mini-mappa SVG a 5 zone
    svg = _zone_svg(zona_tabs, color)

    descr = (d.get("descrizione","")[:180] + "…") if len(d.get("descrizione","")) > 180 else d.get("descrizione","")

    return f"""<div style="border:1.5px solid {color}33;border-radius:12px;padding:16px 20px;margin:12px 0;background:#fafafe;font-family:sans-serif">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
    <span style="background:{color};color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.5px">{mc_id}</span>
    <span style="color:{color};font-size:11px;font-weight:600">{AREA_LABEL.get(area, area)}</span>
  </div>
  <strong style="font-size:15px;color:#0f172a">{d.get("titolo","")}</strong>
  <p style="font-size:13px;color:#475569;margin:6px 0 10px">{descr}</p>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px">{fw_badges}</div>
  {svg}
  <div style="margin-top:10px;font-size:12px;color:#64748b;border-top:1px solid #e2e8f0;padding-top:8px">
    <strong>Compito di realtà:</strong> {d.get("compito_realta","")[:160]}…
  </div>
  <a href="{BASE_URL}/{mc_id}/" target="_blank" style="display:inline-block;margin-top:10px;background:{color};color:#fff;padding:6px 14px;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none">
    Apri scheda completa →
  </a>
</div>"""

def _zone_svg(zones: list, color: str) -> str:
    """Mini SVG a 5 caselle orizzontali con frecce."""
    n = len(zones)
    w, h = 560, 44
    step = w // n
    rects = ""
    for i, z in enumerate(zones):
        x = i * step
        bg = color if i == 0 else "#e2e8f0"
        fg = "#fff" if i == 0 else "#334155"
        # arrow right (tranne l'ultimo)
        arr = (f'<text x="{x+step-4}" y="{h//2+5}" text-anchor="middle" '
               f'font-size="13" fill="#94a3b8">▶</text>') if i < n-1 else ""
        rects += (
            f'<rect x="{x+2}" y="2" width="{step-8}" height="{h-4}" rx="6" fill="{bg}"/>'
            f'<text x="{x+step//2-4}" y="{h//2+5}" text-anchor="middle" '
            f'font-size="10" font-weight="700" fill="{fg}">{z}</text>'
            + arr
        )
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;max-width:{w}px;height:{h}px;border-radius:6px;overflow:hidden">'
            + rects + '</svg>')

# ─── sezione Markdown da iniettare ───────────────────────────────────────────
MC_MARKER = "## Micro-competenze collegate (ProfTecnologIA)"

def section_html(mc_ids: list) -> str:
    cards = "\n".join(mc_card(mid) for mid in mc_ids)
    return f"\n\n{MC_MARKER}\n\n{cards}\n"

# ─── inietta nelle pagine ────────────────────────────────────────────────────
updated = 0
for slug, mc_ids in MAPPING.items():
    # cerca la pagina in qualsiasi sottocartella
    hits = list(CONTENT.rglob(f"{slug}.md"))
    if not hits:
        print(f"  SKIP (non trovato): {slug}")
        continue
    page = hits[0]
    txt  = page.read_text(encoding="utf-8")
    # rimuovi eventuale sezione precedente
    txt = re.sub(rf"\n\n{re.escape(MC_MARKER)}.*", "", txt, flags=re.S)
    txt += section_html(mc_ids)
    page.write_text(txt, encoding="utf-8")
    print(f"  OK: {slug} ← {mc_ids}")
    updated += 1

print(f"\nTotale pagine aggiornate: {updated}")
