# Mappa Kumu del wiki

`wiki-map.json` è un blueprint Kumu (elementi + connessioni) generato da
`scripts/build_kumu_map.py` a partire dal wiki Obsidian in `eduwiki-llm/wiki/`.

Kumu non ha un'API pubblica: l'unico modo per far comparire questi dati in una
mappa è il "remote JSON link", che Kumu ri-scarica a ogni refresh della pagina.

## Come collegarlo alla mappa su kumu.io

1. Apri la mappa su kumu.io.
2. Clicca il pulsante verde **+** in basso, poi **Import**.
3. Incolla questo URL nel campo **"Link map to remote JSON"**:
   ```
   https://raw.githubusercontent.com/AntScaramuzzino/eduwiki-tecnologia/main/kumu/wiki-map.json
   ```
4. La mappa si aggiorna automaticamente ogni volta che riapri la pagina Kumu,
   perché rilegge questo file da GitHub.

## Come rigenerare la mappa dopo modifiche al wiki

```
python3 scripts/build_kumu_map.py
git add kumu/wiki-map.json
git commit -m "chore: aggiorna mappa kumu"
git push
```

## Cosa contiene

- **Elementi**: una voce per ogni pagina di `00-indice/index.md` (concetti,
  metodologie, strumenti digitali, attività, UDA, valutazione, inclusione),
  le pagine di `09-prompt/`, e ogni voce di `11-glossario/glossario.md`.
- **Connessioni**: i wikilink `[[...]]` realmente presenti nelle pagine
  (sezioni "Pagine collegate", "Collegamenti interdisciplinari", "Strumenti
  digitali utili", ecc.) più i collegamenti glossario → concetto.
- **Tipo "Pagina mancante"**: se un wikilink punta a una pagina che non esiste
  ancora, viene creato un nodo segnaposto — visualizza così anche i "buchi" del
  wiki, coerente con la regola del progetto ("un link a una pagina non ancora
  esistente segnala lavoro da fare").

La rete è densa (~250 elementi, ~1500 connessioni): usa i filtri di Kumu per
tipo o le funzioni di ricerca/focus per esplorarla senza restare disorientati
davanti al grafo completo.
