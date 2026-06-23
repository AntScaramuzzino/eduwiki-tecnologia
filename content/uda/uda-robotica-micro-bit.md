---
tipo: uda
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Coding e Robotica - Barbero, Vaschetto (Paravia/Pearson), Upgrade. Tecnologia al futuro - Guida insegnante (Pearson)]
ultima_revisione: 2026-06-22
---

# UDA: progettiamo con micro:bit

## Contesto classe
Questa Unità di Apprendimento è pensata per una classe seconda o terza della scuola secondaria di primo grado, con un'aula informatica o un set di tablet/notebook con accesso a internet e almeno una scheda BBC micro:bit ogni 2-3 studenti. La scheda micro:bit è stata progettata appositamente per fare didattica, ha costi bassi e può essere programmata con ogni tipo di computer (Windows, macOS, Chromebook, Linux, Raspberry Pi) e anche con smartphone o tablet di qualsiasi marca e sistema operativo: questo la rende adatta anche a contesti con dotazioni eterogenee. *(proposta progettuale)* Si presuppone che la classe abbia già avuto un primo contatto con la programmazione a blocchi (per esempio con Scratch) e con il concetto di sequenza di istruzioni.

## Problema di partenza
Come possiamo trasformare una semplice scheda elettronica in un oggetto che "fa qualcosa di utile o divertente" nel mondo reale: misura la temperatura, reagisce a un movimento, comunica con i compagni o si muove come un robot? Il punto di partenza è una domanda concreta che gli studenti incontrano quando vedono la scheda per la prima volta: una scheda con 25 LED, due pulsanti e alcuni sensori, da sola, non fa nulla. Serve un programma. La sfida dell'UDA è progettare e costruire, in piccoli gruppi, un prototipo funzionante che risolva un piccolo problema scelto dalla classe. *(proposta progettuale)*

## Competenze attese
- **Pensiero computazionale**: scomporre un problema in passi (sequenze, cicli, condizioni), rappresentarlo come algoritmo e tradurlo in un programma a blocchi.
- **Competenza digitale**: usare in autonomia l'editor online MakeCode, il simulatore e la procedura di trasferimento del programma sulla scheda.
- **Progettare e risolvere problemi**: passare dall'idea al prototipo, provare, individuare gli errori e correggerli (debugging). *(proposta progettuale, in linea con i traguardi per lo sviluppo delle competenze richiamati nella guida Pearson)*
- **Collaborare e comunicare**: lavorare in gruppo e spiegare le scelte progettuali. *(proposta progettuale)*

## Obiettivi di apprendimento
Al termine dell'UDA lo studente è in grado di:
- riconoscere i componenti della scheda micro:bit (25 LED programmabili, pulsanti A e B, sensore di temperatura, sensore di luce, accelerometro, bussola, connessione radio e Bluetooth) e la loro funzione;
- collegare la scheda al computer tramite cavo micro-USB e trasferire un programma scaricando il file `.hex`;
- costruire programmi che usano i blocchi fondamentali: `on start`, `forever`, `show leds`, `show number`, `on button pressed`, `on shake`;
- usare le variabili come "contenitori" di un valore (per esempio `numero`, `tempo`, `punteggio`);
- usare i blocchi `pick random`, i cicli (`while`, `repeat`) e le condizioni (`if`) con gli operatori logici `and`, `not` e i confronti;
- leggere un valore da un sensore (per esempio `temperature (°C)`) e mostrarlo sul display;
- testare il programma nel simulatore e sulla scheda fisica, individuando e correggendo gli errori.

## Prerequisiti
- Concetto di algoritmo come sequenza ordinata di istruzioni.
- Prima esperienza di programmazione a blocchi (Scratch o ambiente analogico). *(proposta progettuale)*
- Concetto di istruzione condizionale "se... allora..." anche in forma intuitiva. La struttura `if CONDIZIONE then ISTRUZIONE` viene letta in classe come "se una condizione è vera allora esegui le istruzioni".
- Norme base di sicurezza nell'uso di cutter, batterie e piccoli utensili, indispensabili per la fase di costruzione del robot (da svolgere sempre con la guida di un adulto).

## Fasi operative
L'UDA è articolata in cinque fasi, indicativamente 8-10 ore. *(scansione oraria: proposta progettuale)*

**Fase 1 - Conoscere la scheda (1 ora).** Si presenta la scheda fronte/retro e i suoi componenti. Primo accesso al sito microbit.org: dalla home si clicca su *Let's Code* per aprire l'editor MakeCode e creare un *New Project*.

**Fase 2 - Primi programmi guidati (2-3 ore).** Attività a difficoltà crescente tratte dal testo:
- *Fai battere il cuore di micro:bit*: con il blocco `show leds` si disegna un cuore dentro `on start`, poi due immagini dentro `forever` per creare l'animazione.
- *micro:bit sorride!*: con `on button pressed` si mostra una faccia che ride premendo A, una triste premendo B, una "furbetta" premendo A+B.
- *Indovina il numero* e *Sasso, carta, forbice*: introduzione delle variabili e del blocco `pick random` per generare numeri casuali; uso di `if` per associare a ogni numero un'immagine.

**Fase 3 - Cicli, condizioni e sensori (2 ore).**
- *Crea un timer per i giochi*: si usa la variabile `tempo`, il ciclo `while`, gli operatori `not`, `pause (ms) 1000` e `change tempo by 1` per costruire un cronometro.
- *Misura la temperatura ambiente*: scuotendo la scheda (`on shake`) si legge il sensore con il blocco `temperature (°C)` e si memorizza il valore in una variabile.

**Fase 4 - Progettazione del prototipo di gruppo (2 ore).** Ogni gruppo sceglie un problema e progetta la soluzione: prima su carta (idea, blocchi necessari, diagramma di flusso), poi nel simulatore. Opzione avanzata: *Costruisci un robot con micro:bit e con materiali di recupero* — un robot con scocca in cartone, due servomotori a rotazione continua, ruote, breadboard e portabatterie, da assemblare con l'aiuto di un adulto.

**Fase 5 - Test, debugging e presentazione (1-2 ore).** Ogni gruppo trasferisce il programma sulla scheda (Download del file `.hex` sulla periferica MICROBIT), prova il prototipo, corregge gli errori e lo presenta alla classe spiegando le scelte fatte.

## Metodologie
- **Learning by doing / tinkering**: si impara costruendo e provando, con attività operative "In azione!" che partono subito dalla pratica.
- **Apprendimento per problemi e a piccoli passi**: ogni attività aggiunge un concetto nuovo (variabili, cicli, condizioni, sensori) su quanto già appreso.
- **Debugging come strategia didattica**: l'errore è parte del processo; il simulatore permette di verificare e correggere prima di trasferire il programma sulla scheda. *(proposta progettuale)*
- **Cooperative learning**: lavoro in gruppi di 2-3 con ruoli a rotazione (programmatore, costruttore, verificatore). *(proposta progettuale)*

## Strumenti
- Scheda **BBC micro:bit** (una ogni 2-3 studenti) con cavo micro-USB e portabatterie.
- Editor online **MakeCode** (makecode.microbit.org) con simulatore integrato; sito di riferimento microbit.org; guida ai blocchi su makecode.microbit.org/reference.
- Computer o tablet con browser e accesso a internet.
- Per la versione robot: scatola di cartone, cutter, cacciavite, nastro biadesivo e isolante, 2 servomotori a rotazione continua da 9 g, 2 ruote da 60 mm, cavi con morsetti a coccodrillo, jumper per breadboard, portabatterie e batterie AA/AAA.
- Quaderno o foglio di progettazione per disegnare l'algoritmo prima di programmare. *(proposta progettuale)*

## Prodotti finali
- Un **prototipo funzionante** programmato su micro:bit (gioco, strumento di misura, animazione interattiva o robot mobile).
- Il **programma a blocchi** salvato nell'editor e il file `.hex`.
- Una **scheda di progetto** del gruppo (problema, idea, algoritmo, blocchi usati, prove e correzioni). *(proposta progettuale)*
- Una breve **presentazione orale** alla classe. *(proposta progettuale)*

## Valutazione
La valutazione è di processo e di prodotto. Si osservano la progettazione, la correttezza del programma, la capacità di individuare e correggere gli errori e la collaborazione. *(rubrica: proposta progettuale da validare)*

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Scomposizione del problema (pensiero computazionale) | Non scompone il problema senza aiuto | Individua i passi principali con supporto | Scompone il problema in passi e li ordina correttamente | Scompone in modo autonomo e prevede casi particolari |
| Uso dei blocchi e dei concetti (variabili, cicli, condizioni, sensori) | Usa solo blocchi base con guida costante | Usa correttamente sequenze e qualche condizione | Usa variabili, cicli e condizioni in modo appropriato | Combina i costrutti in modo originale e legge i sensori |
| Test e debugging | Non riconosce gli errori | Individua gli errori se segnalati | Trova e corregge gli errori usando il simulatore | Corregge autonomamente e migliora il programma |
| Collaborazione e presentazione | Partecipa poco al lavoro di gruppo | Svolge il proprio compito su richiesta | Collabora e spiega le proprie scelte | Coordina il gruppo e presenta con chiarezza il prototipo |

## Inclusione
- L'editor MakeCode offre una funzione per **aumentare il contrasto dell'interfaccia** a favore delle persone ipovedenti e permette di **selezionare la lingua** dell'interfaccia e dell'aiuto: due leve concrete di accessibilità presenti nello strumento.
- La programmazione **a blocchi** riduce le barriere legate alla scrittura del codice e consente a tutti di partecipare; il **simulatore** permette di provare anche senza la scheda fisica.
- Lavoro in **coppie eterogenee** con ruoli assegnati, materiali a difficoltà graduata e tempi flessibili. *(proposta progettuale)*
- Per chi ha difficoltà motorie, privilegiare attività basate sui pulsanti o sui sensori (scuotere la scheda) rispetto al montaggio fine del robot. *(proposta progettuale)*

## Collegamenti interdisciplinari
- **Scienze**: lettura della temperatura ambientale con il sensore; concetto di sensore e di grandezza misurata.
- **Matematica**: numeri casuali, variabili, confronti e operatori logici (`and`, `not`), conteggio del tempo in millisecondi.
- **Educazione civica / sostenibilità**: costruzione del robot con materiali di recupero e riflessione sul riuso.
- **Italiano**: stesura della scheda di progetto e presentazione orale del prototipo. *(proposta progettuale)*

## Pagine collegate
- [[micro-bit]]
- [[coding-e-programmazione-a-blocchi]]
- [[robotica-educativa]]
- [[sensori-e-attuatori]]
- [[debugging-come-strategia]]
- [[valutazione-coding-robotica]]

## Fonti
- Coding e Robotica - Alberto Barbero, Francesco Vaschetto (Paravia/Pearson), Area 4 "Coding con BBC micro:bit", pp. 84-102 (componenti della scheda, uso di MakeCode, download del file .hex, attività guidate: cuore, faccine, indovina il numero, sasso-carta-forbice, timer, misura della temperatura) e p. 100-101 "Costruisci un robot con micro:bit e con materiali di recupero" (materiali e montaggio)
- Upgrade. Tecnologia al futuro - Guida insegnante (Pearson), pp. 11 e sgg., sezione "Coding e robotica educativa" (finalità del coding, pensiero computazionale, descrizione di BBC micro:bit e dei progetti realizzabili)
- Alcune indicazioni metodologiche, la scansione oraria e la rubrica di valutazione sono proposte progettuali da validare
