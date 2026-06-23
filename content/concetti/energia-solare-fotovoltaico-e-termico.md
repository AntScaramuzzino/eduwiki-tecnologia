---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: []
stato: da_validare
fonti:
  - Techno logics — Furci, Pozzi, Monti (Raffaello Scuola)
  - Come funziona la tecnologia
  - Tecnomedia DIGIT Arduino (Lattes)
  - Futura — Delpiano, Giusiano, Goldschmidt (Paravia)
  - Infinito Tecnologico — Betto (Lattes)
  - STEAM Generation — Bruno, Brunetto (Le Monnier)
ultima_revisione: 2026-06-22
---

# L'energia solare: fotovoltaico e solare termico

## Definizione breve

L'energia solare è l'energia proveniente dal Sole sotto forma di radiazioni elettromagnetiche. Viene sfruttata in due modi principali: **solare termico** (i collettori catturano il calore per produrre acqua calda) e **fotovoltaico** (le celle convertono direttamente la luce in energia elettrica tramite l'effetto fotovoltaico nei materiali semiconduttori come il silicio).

---

## Spiegazione per docenti

### Caratteristiche generali

L'energia solare è una fonte rinnovabile, pulita e inesauribile. La potenza di irraggiamento media è di circa 1 kW/m² nelle ore centrali della giornata alle latitudini europee mediterranee. Non è distribuita uniformemente: le regioni più favorite si trovano tra i 45° di latitudine Nord e Sud dell'Equatore. Presenta due limiti strutturali: è assente di notte e variabile in funzione delle stagioni e della copertura nuvolosa.

Fonti: *Come funziona la tecnologia* (p.187); *Tecnomedia DIGIT Arduino* (p.370).

### Il solare termico: collettori solari

Il collettore solare (o pannello solare termico) è un sistema a bassa temperatura (60–70 °C) che sfrutta il calore del Sole per produrre acqua calda sanitaria o per integrare il riscaldamento degli ambienti. Il funzionamento si basa sull'**effetto serra**: i raggi solari attraversano una lastra di vetro trasparente, colpiscono una piastra metallica scura che assorbe le radiazioni, e il calore riscalda il fluido che scorre nei tubi interni. Il vetro impedisce alle radiazioni infrarosse di disperdersi all'esterno. Un sistema di tubi isolati trasferisce il calore a un serbatoio (boiler).

Un pannello solare può produrre da 80 a 130 litri al giorno di acqua calda per ogni metro quadrato di superficie esposta.

**Componenti principali**:
- **Piastra captante metallica** (alluminio, acciaio o rame, verniciata di nero): assorbe le radiazioni.
- **Vetro di copertura**: fa entrare i raggi solari, trattiene le radiazioni infrarosse (effetto serra).
- **Strato isolante posteriore**: riduce le dispersioni termiche.
- **Tubi di circolazione con fluido** (acqua e sostanze antigelo): trasportano il calore.
- **Scambiatore di calore**: cede il calore all'acqua sanitaria.
- **Boiler/serbatoio**: accumula l'acqua calda prodotta.

Esiste anche il **pannello a tubi sottovuoto**: tubi di vetro con vuoto interno contenenti tubi di rame percorsi da fluido; offre rese maggiori anche con irraggiamento basso.

**Applicazioni**: acqua calda sanitaria nelle abitazioni; riscaldamento di ambienti (spesso integrato con caldaie convenzionali in inverno, quando l'irraggiamento è insufficiente); usi agricoli e industriali (essiccazione).

Fonti: *Techno logics — Furci, Pozzi, Monti* (p.267–268); *Tecnomedia DIGIT Arduino* (p.371); *Futura — Delpiano* (p.296–297).

### Il fotovoltaico: dalla cella al parco

Il principio fisico alla base è l'**effetto fotovoltaico**: materiali semiconduttori come il silicio, quando colpiti dai fotoni (particelle di luce), liberano elettroni che generano una corrente elettrica. Le prime celle fotovoltaiche furono realizzate negli anni Cinquanta. Il nome esprime la scoperta: "foto" significa luce, "voltaico" deriva da Alessandro Volta.

**Struttura gerarchica di un impianto fotovoltaico**:
- **Cella fotovoltaica**: unità base in silicio (lato 10–15 cm), produce circa 1,5 W a circa 0,6 V in corrente continua.
- **Modulo**: 36, 48 o 72 celle collegate in serie o in parallelo; potenza 50–100 W.
- **Pannello**: più moduli assemblati; 8–10 pannelli bastano a coprire il fabbisogno di un nucleo familiare (~3 kWh).
- **Stringa / campo**: più pannelli per impianti di potenza maggiore.

**Tipi di impianto**:
- *Stand-alone* (a isola): non connesso alla rete, dotato di accumulatori per le ore notturne; adatto a zone isolate, abitazioni sulle isole minori, rifugi montani.
- *Grid-connected* (collegato alla rete): cede l'energia in eccesso alla rete elettrica nazionale; doppio contatore di produzione e di scambio.

**Inverter**: dispositivo essenziale che converte la corrente continua prodotta dai pannelli in corrente alternata (220 V) usabile dagli elettrodomestici.

**Parchi e centrali fotovoltaiche**: grandi impianti composti da migliaia di moduli, talvolta con sistemi a inseguimento solare (tracker) per massimizzare la resa. Le *centrali agrovoltaiche* integrano pannelli su strutture agricole (serre), consentendo anche la coltivazione del suolo sottostante.

**Vantaggi**: nessuna emissione inquinante durante il funzionamento; fonte illimitata e gratuita; bassa manutenzione; durata attorno ai 30 anni; installabile su tetti, industrie, terreni agricoli; pannelli sagomati disponibili per ridurre l'impatto visivo.

**Svantaggi**: fonte intermittente (notte, nuvolosità); costi iniziali elevati con tempi di ammortamento lunghi; impatto paesaggistico delle grandi centrali; sistema di accumulo su larga scala ancora in parte irrisolto.

Fonti: *Techno logics — Furci, Pozzi, Monti* (p.268–270); *Tecnomedia DIGIT Arduino* (p.374–375); *Infinito Tecnologico — Betto* (p.277–278); *STEAM Generation — Bruno, Brunetto* (p.294–295); *Come funziona la tecnologia* (p.187–188).

### Le centrali solari ad alta temperatura

Per la produzione su larga scala di energia elettrica esistono impianti a concentrazione che sfruttano il calore del Sole:

- **Centrale a concentrazione / a torre**: specchi piani orientabili (eliostati) riflettono i raggi verso un ricevitore in cima a una torre; temperature > 500–1000 °C; sali fusi come fluido termovettore; turbina a vapore e alternatore generano elettricità.
- **Centrale a collettori parabolici lineari**: specchi a sezione parabolica concentrano i raggi su un tubo ricevitore nel fuoco della parabola; temperatura ~500–550 °C; tecnologia matura (impianti nel deserto del Mojave, California, da oltre 20 anni; in Italia il Progetto Archimede di ENEA–ENEL a Priolo Gargallo, ideato dal prof. Rubbia, premio Nobel per la Fisica).
- **Sistema Fresnel** (tecnologia italiana di Giovanni Francia, 1911–1980): specchi piani modulari riflettono i raggi su un tubo assorbitore posto sopra; più semplice e meno costoso; acqua diretta come fluido.

Fonti: *Tecnomedia DIGIT Arduino* (p.372–374); *Infinito Tecnologico — Betto* (p.274–276); *Futura — Delpiano* (p.300).

---

## Spiegazione per studenti

Il Sole invia ogni giorno sulla Terra una quantità enorme di energia. Possiamo usarla in due modi.

**Il solare termico**: un pannello solare termico è una scatola con una lastra di vetro sopra e una piastra metallica nera all'interno, attraversata da tubi pieni di liquido. La piastra nera assorbe il calore del Sole; il vetro intrappola quel calore (come succede in una macchina parcheggiata al sole: la stessa cosa, stessa fisica, si chiama effetto serra). Il liquido riscaldato trasferisce il calore a un serbatoio d'acqua: acqua calda per lavarci o per riscaldare la casa, senza bruciare nulla.

**Il fotovoltaico**: se esponi al Sole una fettina di silicio (lo stesso materiale dei chip dei computer), le particelle di luce — i fotoni — colpiscono gli atomi e liberano degli elettroni che si mettono a scorrere. Questo flusso di elettroni è una corrente elettrica. Una singola cella produce poca corrente, ma collegandone tante insieme si formano pannelli sempre più potenti. Un dispositivo chiamato **inverter** trasforma la corrente prodotta dai pannelli (continua) in quella usata in casa (alternata a 220 V).

Di notte, o quando il cielo è molto coperto, i pannelli fotovoltaici producono meno o nulla. Per questo si usano batterie di accumulo oppure si rimane collegati alla rete elettrica nazionale, cedendo l'energia in eccesso di giorno e prelevandola di notte.

---

## Versione ultra-semplice (BES/DSA)

**Il Sole ci dà energia. La usiamo in due modi:**

1. **Calore → acqua calda** (solare termico)
   - Un pannello sul tetto cattura il calore del Sole.
   - Il calore scalda l'acqua in un serbatoio.
   - Usiamo quell'acqua per lavarci o riscaldare la casa.

2. **Luce → elettricità** (fotovoltaico)
   - Un pannello di silicio capta la luce del Sole.
   - La luce fa muovere gli elettroni nel silicio.
   - Gli elettroni in movimento = corrente elettrica.
   - L'inverter la trasforma: possiamo usarla in casa.

**Da ricordare:**
- Il Sole è gratuito e non finisce mai.
- Di notte i pannelli fotovoltaici non producono corrente.
- Non inquinano mentre funzionano.

---

## Esempio concreto in classe

**"Il tetto fotovoltaico della scuola"** (se presente) oppure **"Quanto paga la scuola di energia elettrica?"**

1. Il docente mostra la bolletta energetica dell'istituto (anonimizzata) o un documento pubblico del Comune relativo a un impianto fotovoltaico su un edificio scolastico.
2. Gli studenti confrontano la produzione stimata con i consumi della scuola.
3. Correlano i dati con le condizioni meteo del mese (ore di sole, giorni nuvolosi).
4. Discussione: cosa succede di notte? Come viene gestito il surplus di energia?

**Alternativa semplice**: una piccola cella fotovoltaica da 1–2 W collegata a un LED dimostra immediatamente la conversione luce → elettricità; coprendo parzialmente la cella si vede calare la luminosità del LED in tempo reale.

---

## Dal concetto all'attività

### Livello base

**Titolo**: Riconoscere e descrivere i componenti del pannello solare

**Descrizione**: Gli studenti completano uno schema muto di un collettore solare termico e di una cella fotovoltaica, etichettando le parti principali (piastra, vetro, isolante, fluido, cella di silicio, inverter). Rispondono poi a domande guidate: *Qual è la differenza tra solare termico e fotovoltaico? Perché la piastra è nera? Cosa fa l'inverter?*

**Obiettivo**: riconoscere e descrivere i componenti principali dei due sistemi.

**Tempi**: 1 ora.

---

### Livello intermedio

**Titolo**: Confronto e calcolo semplificato di un impianto fotovoltaico

**Descrizione**: Partendo da una tabella fornita dal docente (ore di sole medie mensili per la propria città, potenza tipica di un pannello 300–400 W), gli studenti:
1. Calcolano la produzione mensile stimata di energia (kWh) di un impianto domestico da 3 kWp.
2. Confrontano il dato con il consumo medio di una famiglia italiana (~300 kWh/mese).
3. Completano una tabella comparativa solare termico vs. fotovoltaico (applicazione, costo, vantaggi, svantaggi).
4. Discutono: conviene di più in Sicilia o in Lombardia? Perché?

**Obiettivo**: applicare il ragionamento causa-effetto; collegare dati quantitativi a scelte tecnologiche.

**Tempi**: 2 ore.

---

### Livello avanzato

**Titolo**: Progettare l'impianto energetico di un'abitazione **(proposta progettuale)**

**Descrizione**: In gruppi da 3–4, gli studenti ricevono la scheda di un'abitazione fittizia (metratura, numero di persone, posizione geografica, consumi stimati). Devono:
1. Decidere se installare solo fotovoltaico, solo solare termico o entrambi.
2. Stimare la superficie di pannelli necessaria.
3. Prevedere il sistema di accumulo o la connessione alla rete.
4. Preparare una presentazione che giustifichi le scelte con dati (rendimento, CO₂ risparmiata, payback period semplificato).

**Obiettivo**: progettare una soluzione tecnica argomentata; sviluppare competenze di problem solving e comunicazione.

**Tempi**: 3–4 ore (estendibile come UDA o lavoro per casa).

---

## Misconcezioni frequenti

| Misconcezione | Chiarimento |
|---|---|
| "I pannelli fotovoltaici non funzionano quando è nuvoloso." | I pannelli producono corrente anche con cielo coperto, perché sfruttano la radiazione diffusa; la produzione è ridotta, non azzerata. |
| "Solare termico e fotovoltaico fanno la stessa cosa." | Sono sistemi distinti: il solare termico produce calore (acqua calda), il fotovoltaico produce elettricità. |
| "I pannelli fotovoltaici producono direttamente corrente alternata." | Producono corrente continua; l'inverter la converte in corrente alternata. |
| "L'energia solare è gratuita, quindi l'impianto non costa nulla." | L'energia del Sole è gratuita, ma pannelli, inverter e installazione hanno un costo iniziale elevato; il risparmio in bolletta ammortizza la spesa in diversi anni. |
| "I pannelli fotovoltaici consumano energia di notte." | Un impianto grid-connected di notte preleva energia dalla rete; non è un dispositivo a consumo attivo. |
| "Il solare termico riscalda la casa da solo in inverno." | In inverno l'irraggiamento solare è spesso insufficiente: il sistema va integrato con una caldaia convenzionale. |

---

## Collegamenti interdisciplinari

- **Scienze**: effetto fotoelettrico (base fisica delle celle fotovoltaiche); effetto serra (funzionamento del pannello termico); fotosintesi (analogia con la captazione dell'energia solare nelle piante).
- **Fisica**: corrente elettrica, tensione, potenza (W, kW, kWh); trasformazioni energetiche (radiante → termica → meccanica → elettrica).
- **Geografia**: distribuzione dell'irraggiamento solare sulla Terra; latitudine e angolo di incidenza dei raggi; atlante solare in Italia.
- **Matematica**: calcolo di potenza e energia prodotta (P × t = E); percentuali; proporzionalità diretta.
- **Educazione civica / Agenda 2030**: Obiettivo 7 (Energia pulita e accessibile); decarbonizzazione; confronto con i combustibili fossili.
- **Arte e immagine / Design**: impatto paesaggistico dei parchi fotovoltaici; soluzioni architettoniche integrate (BIPV — Building Integrated Photovoltaics). **(proposta progettuale)**

---

## Strumenti digitali utili

- **PVGIS** (ec.europa.eu/jrc/en/pvgis): strumento gratuito della Commissione Europea per calcolare la produzione fotovoltaica stimata in qualsiasi luogo europeo; ideale per attività con dati reali.
- **Google Maps / Google Earth**: localizzazione e visualizzazione di parchi fotovoltaici; confronto visivo con campi da calcio per percepire le dimensioni.
- **PhET Interactive Simulations** (phet.colorado.edu): simulazioni su energia, circuiti elettrici, effetto fotoelettrico.
- **Simulatori di risparmio energetico domestico** (disponibili su siti di gestori energetici nazionali): per calcolare il risparmio in bolletta. **(proposta progettuale: verificare disponibilità strumenti aggiornati)**
- **Canale RAI Scuola / sito ENEA**: materiali video e documentali in italiano sull'energia solare.

---

## Valutazione e rubriche

### Rubrica — L'energia solare: fotovoltaico e solare termico

| Criterio | Livello 1 — Iniziale | Livello 2 — Base | Livello 3 — Intermedio | Livello 4 — Avanzato |
|---|---|---|---|---|
| **Comprensione dei concetti** | Confonde solare termico e fotovoltaico; non descrive il funzionamento. | Distingue i due sistemi a grandi linee; descrive il funzionamento con imprecisioni. | Descrive correttamente entrambi i sistemi; usa la terminologia specifica in modo adeguato. | Descrive in modo preciso e completo; collega i principi fisici (effetto fotovoltaico, effetto serra) al funzionamento. |
| **Conoscenza dei componenti** | Non riconosce i componenti principali. | Riconosce alcuni componenti (piastra, pannello) senza saperne spiegare la funzione. | Riconosce e descrive la funzione dei componenti principali (piastra, vetro, silicio, inverter, boiler). | Descrive la catena tecnologica completa (cella → modulo → pannello → inverter → rete) con la funzione di ogni elemento. |
| **Vantaggi e limiti** | Non sa indicare vantaggi o limiti. | Cita uno o due vantaggi generici (non inquina, è gratuita). | Elenca vantaggi e limiti principali; collega l'intermittenza alle soluzioni tecniche (accumulo, rete). | Confronta criticamente vantaggi e limiti in relazione al contesto (latitudine, stagione, costo); propone soluzioni motivate. |
| **Applicazione e calcolo** | Non applica i dati forniti. | Effettua calcoli elementari con assistenza. | Calcola autonomamente la produzione stimata di un impianto partendo da un set di dati. | Progetta un sistema semplice, giustifica le scelte con dati quantitativi e argomenta criticamente le decisioni. |

---

## Inclusione e adattamenti

### Studenti con DSA (dislessia, disgrafia, discalculia)

- Fornire la **versione ultra-semplice** e schemi con etichette da collegare (frecce + parole chiave, non testo continuo).
- Usare **mappe visive** con icone: Sole → piastra nera → fluido caldo → boiler (termico) / Sole → silicio → elettroni → corrente → inverter → presa (fotovoltaico).
- Evitare calcoli con moltiplicazioni a più cifre senza calcolatrice; privilegiare la comprensione qualitativa del processo.
- Per la verifica: domande a scelta multipla o vero/falso con immagini di supporto.

### Studenti con BES generici

- Ridurre il numero di termini tecnici richiesti per la memorizzazione; costruire con la classe un piccolo glossario illustrato condiviso.
- Privilegiare attività laboratoriali (celletta fotovoltaica + LED) rispetto alla sola lettura.

### Studenti con livello avanzato

- Approfondimento sul **Progetto Archimede** (ENEA) e su tecnologie emergenti (perovskite, pannelli bifacciali, agrovoltaico).
- Ricerca su PVGIS con presentazione alla classe: produzione stimata nella propria città vs. una città del Sud.

### Studenti di origine straniera o con difficoltà linguistiche

- Usare tabelle comparative visive (solare termico / fotovoltaico) con traduzione dei termini chiave nelle principali lingue di origine della classe.
- Il termine "fotovoltaico" è internazionale (photovoltaic in inglese, photovoltaïque in francese): utile aggancio per studenti bilingui.

---

## Fonti

- Furci, Pozzi, Monti — *Techno logics*, Raffaello Scuola (p.267–270)
- Furci, Pozzi, Monti — *Techno logics, Volume Didattica inclusiva*, Raffaello Scuola (p.140–142)
- *Come funziona la tecnologia* (p.187–188)
- G.P. Benente — *Tecnomedia DIGIT Arduino*, Lattes (p.357–361 / pp.370–375)
- Delpiano, Giusiano, Goldschmidt — *Futura*, Paravia (p.280–300)
- Betto — *Infinito Tecnologico*, Lattes (p.274–278)
- Bruno, Brunetto — *STEAM Generation*, Le Monnier (p.294–295)

> Nota: le sezioni "Esempio concreto in classe", "Livello avanzato", parte di "Strumenti digitali utili" e alcune voci di "Misconcezioni frequenti" sono **proposte progettuali** non direttamente trascritte dai testi sorgente. I contenuti scientifici e tecnici descritti sono ricavati dai testi elencati sopra.

---

## Pagine collegate

- [[fonti-rinnovabili-e-non-rinnovabili]]
- [[forme-e-trasformazioni-dell-energia]]
- [[risparmio-energetico-e-efficienza]]
- [[energia-eolica]]
- [[uda-energia-sostenibile]]
- [[inclusione-energia]]


## Micro-competenze collegate (ProfTecnologIA)

<div style="border:1.5px solid #f9731633;border-radius:12px;padding:16px 20px;margin:12px 0;background:#fafafe;font-family:sans-serif">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
    <span style="background:#f97316;color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.5px">MC-ENE-3-03</span>
    <span style="color:#f97316;font-size:11px;font-weight:600">Energia</span>
  </div>
  <strong style="font-size:15px;color:#0f172a">Fonti rinnovabili e transizione energetica</strong>
  <p style="font-size:13px;color:#475569;margin:6px 0 10px">Lo studente conosce le principali fonti rinnovabili (solare fotovoltaico, eolico, idroelettrico, geotermico, biomasse), ne comprende il principio di funzionamento, sa confrontarne …</p>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px"><span style="background:#6366f1;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">IN 2025</span><span style="background:#0ea5e9;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">DigComp 3.0</span><span style="background:#f59e0b;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">EntreComp</span><span style="background:#10b981;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">LifeComp</span><span style="background:#84cc16;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">Agenda 2030</span></div>
  <svg viewBox="0 0 560 44" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:44px;border-radius:6px;overflow:hidden"><rect x="2" y="2" width="104" height="40" rx="6" fill="#f97316"/><text x="52" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">⚡ INNESCA</text><text x="108" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="114" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="164" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">📖 ESPLORA</text><text x="220" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="226" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="276" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔍 OSSERVA</text><text x="332" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="338" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="388" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔬 SPERIMENTA</text><text x="444" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="450" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="500" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🌍 AGISCI</text></svg>
  <div style="margin-top:10px;font-size:12px;color:#64748b;border-top:1px solid #e2e8f0;padding-top:8px">
    <strong>Compito di realtà:</strong> Progetta il piano energetico della scuola: stima il consumo annuo (bollette se disponibili, o dato medio per m²), dimensiona un impianto fotovoltaico e calcola …
  </div>
  <a href="https://proftecnologia.vercel.app/mc/MC-ENE-3-03/" target="_blank" style="display:inline-block;margin-top:10px;background:#f97316;color:#fff;padding:6px 14px;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none">
    Apri scheda completa →
  </a>
</div>


## Risorse multimediali


[![▶ Come funziona un pannello solare](https://img.youtube.com/vi/mj6_WVh2HwU/hqdefault.jpg)](https://www.youtube.com/watch?v=mj6_WVh2HwU)
*📺 Come funziona un pannello solare · YouTube EDU*
