# Log del Wiki

Registro cronologico append-only. Formato: `AAAA-MM-GG [INGEST|QUERY|LINT] descrizione`.

2026-06-22 [LINT] Inizializzato lo scaffold EduWiki LLM: schema (CLAUDE.md/AGENTS.md), 12 aree in wiki/, raw/ con 5 categorie, _template/ con i modelli di pagina, libreria prompt in 09-prompt/, pagina di esempio realta-aumentata (demo).
2026-06-22 [INGEST] Ingest pilota tema Coding/Robotica/Pensiero computazionale: create 21 pagine didattiche (workflow multi-agente), stato da_validare. Fonti: layer _md di libri-di-testo-tecnologia, guide-docenti, wiki-tecnologia.
2026-06-22 [INGEST] Ingest temi restanti (workflow multi-agente): create 98 pagine didattiche (stato da_validare). Run interrotto dal limite di sessione: ~80 pagine pianificate non scritte e fase Assembla saltata.
2026-06-22 [LINT] Assemblaggio eseguito manualmente: index.md rigenerato (122 pagine per area). 17 link rotti = pagine mancanti da completare (es. riciclo-e-sostenibilita-dei-materiali, fonti-rinnovabili-e-non-rinnovabili, serie disegno-tecnico) + placeholder della pagina demo realta-aumentata. Da risolvere ricompletando l'ingest.
2026-06-22 [INGEST] Ingest temi restanti (12 temi): create 181 pagine didattiche (workflow multi-agente), stato da_validare. Fonti: layer _md.
2026-06-23 [LINT] Ingest completato — 202 pagine in 02-08. Lint su wikilink (02-08): 5 link rotti reali (app-ar, apprendimento-esperienziale, didattica-immersiva, realta-virtuale, valutazione-museo-aumentato) + 2 non-pagine (udl, wikilink — termini usati come anchor, non slug). 1 pagina orfana (realta-aumentata, già nota come demo placeholder). Tutti i 181 nuovi slug sono raggiungibili da almeno un wikilink. Index.md, glossario.md aggiornati (sezione Temi + 24 voci glossario).
