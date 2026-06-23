---
tipo: strumento_digitale
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [competenza digitale, pensiero computazionale, competenza matematica, cittadinanza economica]
stato: da_validare
fonti: [Informaticamente vol. 1 (Ghini), Come funziona l'informatica (AA.VV.), Techno logics Laboratorio STEAM (Furci-Pozzi-Monti), NEXT Guida docente (De Agostini), Progettare il futuro Guida (Conti), Settori (Zanichelli)]
ultima_revisione: 2026-06-22
---

# Il foglio di calcolo per i dati economici

## Cos'è

Il foglio di calcolo — detto anche **foglio elettronico** — è un'applicazione software che organizza i dati in una griglia di **celle** disposte in righe e colonne. Ogni cella può contenere testo (etichette), numeri (valori) o formule che eseguono calcoli automatici sui valori di altre celle. Le principali versioni in uso scolastico sono **Microsoft Excel** (pacchetto Office) e **Fogli Google** (Google Workspace), che funziona direttamente dal browser senza installazione.

Excel è definito dai testi di informatica come software che serve "per memorizzare ed elaborare dati", con la possibilità di creare tabelle per l'elaborazione dei dati, trasformare i dati in grafici (diagrammi, istogrammi), creare modelli per problemi complessi (fatture, bilanci, note spese) e gestire grandi quantità di informazioni.

Fogli Google offre funzionalità equivalenti con il vantaggio del salvataggio automatico in cloud, della collaborazione in tempo reale e della possibilità di importare dati direttamente da pagine web tramite la funzione `IMPORTHTML`.

## A cosa serve in classe

In una UDA su economia, lavoro e settori produttivi, il foglio di calcolo è lo strumento che trasforma i dati grezzi (prezzi, occupazione, produzione, spesa familiare) in informazioni leggibili e confrontabili. Consente agli studenti di:

- **organizzare dati** in tabelle strutturate (settori produttivi, prodotti, prezzi, quantità);
- **eseguire calcoli automatici** su serie di numeri: somme, medie, percentuali, totali parziali;
- **visualizzare i dati** attraverso grafici (istogrammi, grafici a torta, grafici a linee) che rendono immediatamente visibili tendenze e proporzioni;
- **simulare scenari** modificando i dati e osservando come cambiano i totali — ad esempio in un bilancio familiare;
- **importare dati aperti** da fonti online (ISTAT, Banca d'Italia, Wikipedia) e lavorarci direttamente.

I testi scolastici di Tecnologia citano attività che prevedono il foglio di calcolo per rilevare e rappresentare dati statistici, per compilare prospetti di costi, per costruire rubriche alimentari settimanali e per realizzare grafici esplicativi su fenomeni economici e produttivi.

## Come iniziare (setup minimo)

**Opzione A — Fogli Google (consigliata per la classe)**

1. Accedere a `https://sheets.google.com` con un account Google (molte scuole hanno Google Workspace for Education gratuito).
2. Cliccare su "Foglio vuoto" per aprire un nuovo file.
3. Il file è salvato automaticamente su Google Drive; può essere condiviso con il docente con un link.
4. Non serve installare nulla; funziona su qualsiasi dispositivo con browser.

**Opzione B — Microsoft Excel**

1. Aprire Excel dal menu delle applicazioni (è incluso in Microsoft 365 o nelle versioni desktop di Office installate a scuola).
2. Scegliere "Cartella di lavoro vuota".
3. Il file si salva con estensione `.xlsx` (formato compatibile anche con Fogli Google e LibreOffice Calc).

**Concetti base da spiegare prima di iniziare:**

- La **cella attiva** è quella selezionata, identificata da una lettera (colonna) e un numero (riga), per esempio `B3`.
- Le **etichette** sono testi descrittivi (nomi, categorie); i **valori** sono numeri su cui si possono fare calcoli.
- Una **formula** inizia sempre con il segno `=` e usa le coordinate delle celle: `=B3+B4` somma i valori di B3 e B4; `=SOMMA(B3:B10)` somma tutti i valori da B3 a B10.
- Il **riempimento automatico** consente di copiare una formula lungo una colonna o una riga trascinando il quadratino nell'angolo in basso a destra della cella.

**Requisiti minimi:** computer o tablet con browser aggiornato e connessione a internet (per Fogli Google). In alternativa, versione offline di LibreOffice Calc (gratuita e open source).

## Esempi d'uso didattico

**1. Bilancio familiare simulato**

Gli studenti ricevono una scheda con le voci di entrata e uscita di una famiglia tipo (stipendio, affitto, spesa alimentare, trasporti, bollette, svago). Inseriscono i valori nel foglio, costruiscono formule per calcolare il totale delle uscite e il saldo mensile, poi realizzano un grafico a torta per visualizzare come si distribuiscono le spese. Questo tipo di esercizio è esplicitamente citato nelle guide docente come obiettivo: "comprendere gli elementi base di un semplice bilancio familiare".

**2. Confronto tra settori produttivi**

La classe raccoglie dati sulla distribuzione degli occupati nei tre settori (primario, secondario, terziario) in Italia e in un altro Paese europeo. I dati vengono inseriti in una tabella a doppia entrata e trasformati in un istogramma comparativo. Questa attività è indicata dalla guida NEXT come parte del percorso "L'economia e il commercio".

**3. Rilevazione periodica dei prezzi**

Gli studenti monitorano il prezzo di un paniere di beni (pane, latte, benzina, abbonamento internet) su più settimane, inseriscono i dati nel foglio e costruiscono un grafico a linee per vedere l'andamento nel tempo — un'introduzione pratica al concetto di inflazione.

**4. Import di dati aperti con Fogli Google** **(proposta progettuale)**

Usando la funzione `=IMPORTHTML("url";"table";1)` di Fogli Google, gli studenti importano una tabella da Wikipedia o dall'ISTAT direttamente nel foglio, la filtrano e la rappresentano graficamente. Il laboratorio STEAM del testo Techno logics (Raffaello Scuola) mostra questo approccio con dati di popolazione regionale e temperature climatiche, applicabile anche a dati economici.

**5. Confronto costi di produzione**

Partendo da una simulazione di micro-impresa (settore scelto dalla classe), gli studenti compilano un prospetto di costi fissi e variabili, calcolano il totale e simulano scenari "cosa succede se...?" modificando i prezzi delle materie prime. Il testo Informaticamente vol. 1 propone esercizi analoghi con file come `BILANCIO FAMIGLIA.xls`, `ANDAMENTO SPESA PENSIONI.xls`, `COSTI MERCE.xls`.

## Costi / account / privacy

| Strumento | Costo | Account richiesto | Note privacy |
|---|---|---|---|
| Fogli Google | Gratuito | Account Google (preferibile Google Workspace for Education) | I dati sono su server Google; per i minorenni serve consenso informato o account scolastico gestito dall'istituto |
| Microsoft Excel Online | Gratuito con account Microsoft | Account Microsoft (o Microsoft 365 Education) | Valgono le stesse considerazioni di Google |
| LibreOffice Calc | Gratuito, open source | Nessun account richiesto | I file rimangono in locale; nessun dato caricato in cloud |
| Microsoft Excel desktop | Incluso in pacchetti Office a pagamento | Nessun account per uso offline | Licenza scolastica spesso disponibile tramite accordi Microsoft 365 A1 gratuito per le scuole |

**Consiglio pratico:** per attività che non richiedono condivisione in tempo reale, LibreOffice Calc è la scelta più sicura dal punto di vista della privacy e non richiede connessione.

## Limiti e rischi educativi

- **Dipendenza dalla formula senza comprensione.** Gli studenti possono inserire formule che funzionano senza capire l'operazione aritmetica sottostante. È fondamentale affiancare sempre la verifica manuale del risultato su almeno un esempio.
- **Errori nella selezione dell'intervallo.** Una formula come `=SOMMA(B3:B10)` applicata a una colonna che contiene anche etichette produce risultati errati senza avviso. Occorre insegnare la distinzione tra valori e testo.
- **Grafici fuorvianti.** Scegliere il tipo di grafico sbagliato (es. grafico a torta per dati che non sommano al 100%) o non includere titolo, legenda e unità di misura può rendere i dati incomprensibili o ingannevoli. Il testo MyTech specifica esplicitamente come descrittore di competenza che il grafico deve essere "completo (titolo, legenda ecc.)".
- **Rischio di copia passiva.** Se le attività sono troppo guidate (dati già inseriti, formule già scritte), il foglio di calcolo diventa un esercizio di digitazione, non di pensiero. Le attività più efficaci partono da un problema reale e affidano agli studenti la struttura del foglio.
- **Accessibilità dei dispositivi.** Fogli Google richiede connessione stabile; in assenza di banda sufficiente, la versione offline di LibreOffice Calc è preferibile.

## Adattamenti inclusivi

**Per studenti con DSA (in particolare dislessia e discalculia):**

- Usare colori di sfondo diversi per distinguere visivamente le aree dati dalle aree formula (funzione già presente nei fogli come "stili cella").
- Aumentare la dimensione del carattere nelle celle e ridurre il numero di colonne visibili alla volta.
- Fornire un foglio parzialmente compilato (scaffolding) con le etichette già inserite e alcune formule già scritte; lo studente completa le parti mancanti.
- Preferire formule semplici (`=SOMMA` e `=MEDIA`) evitando funzioni logiche complesse nelle prime fasi.
- Consentire l'uso di calcolatrice parallela per verificare un singolo calcolo manualmente, prima di affidarsi alla formula.

**Per studenti con BES o difficoltà linguistiche (L2):**

- Utilizzare icone o simboli nelle intestazioni di colonna per ridurre la dipendenza dalla comprensione del testo.
- Semplificare il numero di variabili nel problema (es. bilancio con sole 4-5 voci invece di 10-12).

**Per studenti con plusdotazione o interesse avanzato:** **(proposta progettuale)**

- Proporre l'importazione di dati reali da ISTAT o Eurostat tramite `IMPORTHTML` e la costruzione autonoma di grafici comparativi.
- Introdurre funzioni statistiche più avanzate (`=SE`, `=CONTA.SE`, `=MEDIA.SE`) per analisi condizionate (es. "quante famiglie spendono più del 30% del reddito in affitto?").

## Attività che lo usano

- [[attivita-simulazione-bilancio-familiare]]
- [[attivita-mappa-dei-settori-del-territorio]]
- [[uda-economia-lavoro-settori]]

## Pagine collegate

- [[sistema-economico-e-mercato]]
- [[i-settori-produttivi]]
- [[il-mondo-del-lavoro]]
- [[compito-di-realta-in-economia]]
- [[inclusione-economia]]
- [[valutazione-economia]]

## Fonti

- Informaticamente vol. 1 — Excel, gestione e elaborazione dati (Ghini, Mondadori) (p. 4–35)
- Come funziona l'informatica (AA.VV., Giunti Scuola) (p. 52–63, Schede 24–28)
- Techno logics — Laboratorio sperimentale STEAM (Furci, Pozzi, Monti, Raffaello Scuola) (p. 40–43, Laboratorio 5 — Fogli Google)
- NEXT — Guida per il docente (De Agostini Scuola) (p. 38, L'economia e il commercio)
- Progettare il futuro — Guida per il docente (Conti, Minerva Scuola Mondadori) (p. 17, bilancio familiare; p. 15, tabelle e grafici)
- Settori (volume unico Zanichelli) — attività con foglio Excel su alimentazione e dieta (p. 242)
- Le attività con grafici a torta e confronto tra dati economici sono in gran parte **(proposta progettuale)** adattata ai contesti economici a partire da esercizi proposti per altri contesti disciplinari (alimentazione, rilevazioni periodiche, costi).
