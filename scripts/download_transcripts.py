"""
download_transcripts.py — scarica le trascrizioni italiane dei video YouTube
citati nel wiki e le salva come fonte immutabile in raw/trascrizioni/.

Richiede yt-dlp (brew install yt-dlp).
"""
import re
import subprocess
import tempfile
from pathlib import Path

RAW_DIR = Path(
    "/Users/antonioscaramuzzino/Library/CloudStorage/GoogleDrive-antonio.scaramuzzino@coopinrete.it/"
    "Il mio Drive/Antonio Scaramuzzino/Brain Tecnologia/eduwiki-llm/raw/trascrizioni"
)

# video_id → (slug, titolo reale, canale, [concetti collegati])
VIDEOS = {
    # Fonti rinnovabili / non rinnovabili — S. Lattes & C. Editori
    "Z6KbUUakaYE": ("video-energie-rinnovabili-lattes", "Le energie rinnovabili", "S. Lattes & C. Editori", ["fonti-rinnovabili-e-non-rinnovabili"]),
    "O8jhHsQ-aHI": ("video-energie-non-rinnovabili-combustibili", "Le energie non rinnovabili: i combustibili", "S. Lattes & C. Editori", ["fonti-rinnovabili-e-non-rinnovabili"]),
    "UXN6hVga3as": ("video-energie-non-rinnovabili-centrali", "Le energie non rinnovabili: le centrali", "S. Lattes & C. Editori", ["fonti-rinnovabili-e-non-rinnovabili"]),
    # Cambiamento climatico — Mondadori Education / Zanichelli
    "4htweLAPj6g": ("video-rampini-riscaldamento-climatico", "Federico Rampini - Il problema del riscaldamento climatico", "Mondadori Education", ["cambiamento-climatico-ed-effetto-serra"]),
    "Z_EBGQ7kZLw": ("video-scenari-climatici-webinar", "Webinar - Scenari climatici cosa sono e come si ottengono", "Mondadori Education", ["cambiamento-climatico-ed-effetto-serra"]),
    "J-joQ3l_xGk": ("video-evidenze-scientifiche-cambiamento-climatico", "Webinar - Evidenze scientifiche del cambiamento climatico", "Mondadori Education", ["cambiamento-climatico-ed-effetto-serra"]),
    "rMff6k0hikQ": ("video-effetti-riscaldamento-globale-geoagenda", "Quali effetti ha il riscaldamento globale (tratto da GeoAgenda)", "Zanichelli editore", ["cambiamento-climatico-ed-effetto-serra"]),
    # Intelligenza artificiale — Zanichelli (serie "Dentro l'IA")
    "MJlrabo6ARk": ("video-dentro-ia-1-reti-neurali", "Dentro l'IA - 1. Come imparano le reti neurali?", "Zanichelli editore", ["intelligenza-artificiale-a-scuola"]),
    "hFyi2sSsm4E": ("video-dentro-ia-2-nlp", "Dentro l'IA - 2. Come funziona l'elaborazione del linguaggio naturale (NLP)?", "Zanichelli editore", ["intelligenza-artificiale-a-scuola"]),
    "BkRKu3mn-o4": ("video-dentro-ia-3-llm", "Dentro l'IA - 3. Come funzionano i grandi modelli linguistici (LLM)?", "Zanichelli editore", ["intelligenza-artificiale-a-scuola"]),
    # Pensiero computazionale / Coding — Mondadori Education / Tecnologia Duepuntozero
    "TIXp9lFHTXo": ("video-esame-stato-pensiero-computazionale", "Esame di Stato e quesito sui metodi del pensiero computazionale", "Mondadori Education", ["pensiero-computazionale"]),
    "JBofYa87CRU": ("video-webinar-pensiero-computazionale", "Webinar - Il pensiero computazionale", "Mondadori Education", ["pensiero-computazionale"]),
    "zxF5aybKJMY": ("video-coding-a-blocchi-scratch", "Coding a blocchi con Scratch", "Mondadori Education", ["pensiero-computazionale", "coding-e-programmazione-a-blocchi"]),
    "JuM9ZLvjqRk": ("video-snap-programmazione-visuale", "Webinar - Snap! Programmazione visuale anche su tablet", "Mondadori Education", ["coding-e-programmazione-a-blocchi"]),
    "ejx7Fv7h9Xo": ("video-scratch-interfaccia-sprite-stage", "Scratch - Interfaccia, Sprite, Stage", "Tecnologia Duepuntozero", ["coding-e-programmazione-a-blocchi"]),
    # Robotica educativa — Mondadori Education / S. Lattes
    "nEq-BUaR3GQ": ("video-robotica-educativa-curriculum-scientifico", "Webinar - Tinkering e robotica educativa: la robotica educativa per il curriculum scientifico", "Mondadori Education", ["robotica-educativa"]),
    "zt4yqJb9x6w": ("video-robotica-educativa-robot-amico", "Webinar - Robotica educativa - un robot per amico", "Mondadori Education", ["robotica-educativa"]),
    "E5tJgzBbyrY": ("video-robotica-educativa-assemblaggio-mbot", "Robotica Educativa Video Tutorial n.1 - Assemblaggio mBot", "S. Lattes & C. Editori", ["robotica-educativa"]),
    # Smart city e mobilità sostenibile — Zanichelli / Geopop / Lattes (domotica)
    "JuyPkww6s-U": ("video-citta-ideale-sostenibile-artelogia", "La città ideale e le città sostenibili (tratto da Artelogia)", "Zanichelli editore", ["smart-city-e-mobilita-sostenibile"]),
    "2qRlgfDaE-k": ("video-google-maps-traffico-tempo-reale", "Come fa Google Maps a rilevare il traffico in tempo reale e a calcolare l'itinerario migliore?", "Geopop", ["smart-city-e-mobilita-sostenibile"]),
    "dAIkxQUDRI0": ("video-esempi-domotica-lattes", "Alcuni esempi di domotica", "S. Lattes & C. Editori", ["smart-city-e-mobilita-sostenibile", "domotica-e-casa-intelligente"]),
    # Energia eolica — Geopop (unico trovato tra i canali autorizzati)
    "GmZCO7TZd9U": ("video-haliade-x-pala-eolica", "Haliade X: la pala eolica più grande del mondo", "Geopop", ["energia-eolica"]),
    # Motore elettrico — Tecnologia Duepuntozero (unico trovato tra i canali autorizzati)
    "2LIO7TEKook": ("video-laboratorio-motorino-elettrico", "Laboratorio: motorino elettrico", "Tecnologia Duepuntozero", ["il-motore-elettrico"]),
}


def vtt_to_text(vtt_path: Path) -> str:
    lines = vtt_path.read_text(encoding="utf-8").splitlines()
    text_lines = []
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            continue
        clean = re.sub(r"<[^>]+>", "", line).strip()
        if clean:
            text_lines.append(clean)
    deduped = []
    for i, line in enumerate(text_lines):
        nxt = text_lines[i + 1] if i + 1 < len(text_lines) else None
        if nxt and nxt.startswith(line):
            continue
        if deduped and deduped[-1] == line:
            continue
        deduped.append(line)
    return " ".join(deduped)


def download_transcript(video_id: str, tmpdir: Path) -> Path | None:
    url = f"https://www.youtube.com/watch?v={video_id}"
    subprocess.run(
        [
            "yt-dlp", "--skip-download", "--write-auto-sub",
            "--sub-lang", "it", "--sub-format", "vtt",
            "-o", str(tmpdir / "%(id)s"), url,
        ],
        capture_output=True, text=True, timeout=60,
    )
    vtt = tmpdir / f"{video_id}.it.vtt"
    return vtt if vtt.exists() else None


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    ok = fail = 0
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        for vid, (slug, title, channel, concepts) in VIDEOS.items():
            vtt = download_transcript(vid, tmpdir)
            if not vtt:
                print(f"  FAIL {vid}  {title[:50]}")
                fail += 1
                continue
            text = vtt_to_text(vtt)
            url = f"https://www.youtube.com/watch?v={vid}"
            concepts_list = "\n".join(f"- [[{c}]]" for c in concepts)
            content = f"""---
tipo: fonte_raw
categoria: trascrizioni
sottotipo: video_youtube
video_id: {vid}
titolo: "{title}"
canale: "{channel}"
url: {url}
lingua_trascrizione: it (automatica)
concetti_collegati:
{chr(10).join(f'  - {c}' for c in concepts)}
---

# Trascrizione — {title}

**Canale:** {channel}
**URL:** {url}
**Concetti collegati:** {concepts_list}

## Trascrizione (sottotitoli automatici IT)

{text}
"""
            out_path = RAW_DIR / f"{slug}.md"
            out_path.write_text(content, encoding="utf-8")
            print(f"  OK   {vid}  {slug}  ({len(text)} caratteri)")
            ok += 1

    print(f"\nTotale: {ok} scaricate, {fail} fallite")


if __name__ == "__main__":
    main()
