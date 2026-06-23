---
tipo: attività_didattica
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Futura - Corso di tecnologia (Disegno/Coding e Robotica), Guida Technologica]
ultima_revisione: 2026-06-22
---

# Attività: il robot che segue un percorso (mBot)

Attività di robotica educativa in cui gli studenti programmano il robot **mBot 2** (Makeblock) perché percorra in autonomia un tracciato, usando il **sensore seguilinea** a infrarossi e i blocchi di controllo della piattaforma **mBlock 5**. È un'attività concreta per portare il pensiero computazionale "fuori dallo schermo": l'algoritmo scritto a blocchi diventa un comportamento fisico osservabile, e gli errori si vedono subito nel movimento del robot.

## Target

Classi seconde e terze della scuola secondaria di primo grado. Si lavora in piccoli gruppi (2-3 studenti per robot), così tutti possono alternarsi tra programmazione, gestione del percorso e osservazione.

## Durata

2-3 ore, articolabili in 2 incontri:
- **Incontro 1** (1 ora): presentazione del robot, dei sensori e della piattaforma mBlock 5; primo script di movimento.
- **Incontro 2** (1-2 ore): costruzione del percorso, programmazione del comportamento seguilinea, test e debugging.

## Materiali

- Robot **mBot 2** (Makeblock) con scheda **mCORE** e cavo USB in dotazione (o collegamento Bluetooth tramite il modulo wireless della scheda).
- PC o tablet con la piattaforma **mBlock 5** (utilizzabile online oppure scaricabile per l'uso offline).
- **Sensore seguilinea** (segui traccia) a infrarossi, montato sulla base del robot. *(Su mBot 2 questo sensore non richiede estensioni aggiuntive: è sufficiente collegarlo perché mBlock ne rilevi la presenza.)*
- Fogli bianchi e nastro/pennarello nero per tracciare la linea da seguire (linee nere su superficie bianca).
- In opzione: **sensore a ultrasuoni** frontale per il rilevamento degli ostacoli; cartoncini colorati per varianti del percorso.

## Prerequisiti

- Aver incontrato la **programmazione a blocchi** (es. Scratch), in particolare la sequenza, il ciclo (ripeti) e il blocco condizionale **se… allora… altrimenti**.
- Conoscere a grandi linee il concetto di **algoritmo** come sequenza ordinata di istruzioni.
- Saper distinguere un **sensore** (che rileva) da un **attuatore** (i motori delle ruote, i led, il display). *(proposta progettuale)*

## Procedura (fasi)

**Fase 1 — Conosciamo il robot (15 min).**
Si presenta mBot 2: un robot di piccole dimensioni dotato di due motori, ciascuno collegato alla scheda elettronica, e di alcuni sensori che gli permettono di interagire con l'ambiente. Si mostra il sensore seguilinea sulla base (led che illuminano la superficie + sensori ottici che rilevano la luce riflessa) e, se disponibile, il sensore a ultrasuoni frontale per gli ostacoli. Punto chiave da far emergere: poiché i due motori sono collegati separatamente alla scheda, si può **programmare la velocità di ogni singola ruota**, ed è proprio questo che permette al robot di curvare e di correggere la traiettoria.

**Fase 2 — Colleghiamo e proviamo i blocchi (15 min).**
Si connette mBot 2 al PC/tablet via USB o Bluetooth e si apre mBlock 5. Primo esperimento di verifica: far comparire in mBlock il valore letto da un sensore (per esempio la distanza dal sensore a ultrasuoni, oppure lo stato del seguilinea). Serve a far capire che il robot "legge" continuamente l'ambiente e che il programma decide cosa fare in base a quella lettura.

**Fase 3 — Costruiamo il percorso (20 min).**
Su un foglio bianco si traccia una **linea nera** continua (un percorso con qualche curva). Gli studenti progettano prima il tracciato su carta, decidendo punto di partenza e di arrivo. *(proposta progettuale)*

**Fase 4 — Programmiamo il comportamento seguilinea (40 min).**
Il cuore del programma è il blocco **se… allora… altrimenti** dentro un ciclo che si ripete: il robot legge il sensore seguilinea e, a seconda di ciò che "legge", esegue una di due azioni alternative (per esempio: *se* sono sulla linea nera → vai dritto; *altrimenti* → correggi sterzando, regolando la velocità delle due ruote). Si parte da una versione minima e funzionante, poi la si raffina.

**Fase 5 — Test e debugging (30 min).**
Si fa partire il robot sul percorso e si osserva. Quando esce dalla linea o sbaglia una curva, gli studenti tornano allo script, formulano un'ipotesi sulla causa (velocità troppo alta? soglia del sensore? curva troppo stretta?), modificano un blocco alla volta e riprovano. Il ciclo *osserva → ipotizza → modifica → riprova* è la parte didatticamente più ricca. *(proposta progettuale per la struttura del ciclo di debugging)*

**Fase 6 — Estensioni (facoltative).**
- Far accendere i led di un colore diverso a seconda della direzione o del tratto percorso.
- Inserire il **sensore a ultrasuoni**: se il robot si avvicina a meno di una soglia (es. 15 cm) da un ostacolo, si ferma, emette un suono e indietreggia.
- Trasformare il percorso in un piccolo labirinto e sfidare altri gruppi.

## Prodotto finale

Un robot mBot 2 che percorre autonomamente il tracciato seguendo la linea, accompagnato da:
- lo **script a blocchi** in mBlock 5 (salvato o esportato);
- un breve **diario di bordo del gruppo** con il disegno del percorso, le versioni dello script provate e le correzioni applicate (registro del debugging). *(proposta progettuale)*

## Valutazione

Si valuta più il **processo** (progettazione, correzione degli errori, collaborazione) che il solo risultato finale. Rubrica a 4 livelli — *(proposta progettuale)*:

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Comprensione dell'algoritmo (sequenza, ciclo, condizione) | Esegue solo con guida costante | Riconosce i blocchi principali | Costruisce uno script funzionante in autonomia | Spiega le scelte e propone alternative |
| Uso dei sensori e dei motori | Non collega lettura sensore e azione | Usa il sensore con aiuto | Usa il blocco se…allora…altrimenti in modo corretto | Combina più sensori/azioni in modo efficace |
| Debugging | Si blocca davanti all'errore | Prova modifiche casuali | Isola la causa e corregge un elemento per volta | Documenta e generalizza la strategia di correzione |
| Collaborazione e ruoli | Lavora isolato | Partecipa se sollecitato | Si alterna nei ruoli e ascolta il gruppo | Coordina il gruppo e porta idee per i problemi |

## Adattamenti inclusivi

### BES/DSA
- Fornire lo **script-base già pronto** da completare o modificare, riducendo la parte di costruzione da zero. *(proposta progettuale)*
- Usare schede visive con i blocchi-chiave (ripeti, se…allora…altrimenti, sensore) e una legenda dei colori dei led.
- Valorizzare il canale concreto e manuale: chi fatica con il testo scritto può eccellere nella gestione del percorso e nell'osservazione del comportamento del robot.

### Plusdotati
- Proporre le estensioni: aggiunta del sensore a ultrasuoni, gestione di più variabili (es. una variabile *Distanza oggetto* aggiornata in tempo reale), conteggio degli errori in una gara. *(spunto sostenuto dalle attività del testo Futura)*
- Sfida sul passaggio dai blocchi al codice testuale **Python**, supportato da mBlock 5. *(proposta progettuale)*

### L2
- Affiancare alle istruzioni testuali le **icone dei blocchi** e parole-chiave bilingui (avanti, indietro, gira, sensore, se/altrimenti).
- Favorire il lavoro in coppia con un compagno tutor; il linguaggio a blocchi e l'osservazione del robot riducono la dipendenza dalla lingua scritta. *(proposta progettuale)*

## Pagine collegate

- [[robotica-educativa]]
- [[mbot]]
- [[sensori-e-attuatori]]
- [[coding-e-programmazione-a-blocchi]]
- [[debugging-come-strategia]]
- [[algoritmo-e-diagrammi-di-flusso]]

## Fonti

- Futura - Corso di tecnologia (A. Delpiano, M. Giusiano, E. Goldschmidt), volume Disegno / Area 6 "Coding e Robotica" (pp. 238-241, p. 246-247): mBot 2, scheda mCORE, piattaforma mBlock 5, sensore seguilinea a infrarossi, sensore RGB, sensore a ultrasuoni, blocco se…allora…altrimenti, attività "percorso" e "labirinto".
- Guida Technologica (Benedetti, Romiti), sezione "Robotica con mBot": mBot come kit di robotica a programmazione a blocchi adatto alle attività didattiche della secondaria di primo grado.
- Nota: parti della metodologia (struttura del ciclo di debugging, rubrica di valutazione, adattamenti inclusivi) sono proposta progettuale da validare, non derivata direttamente dai testi.
