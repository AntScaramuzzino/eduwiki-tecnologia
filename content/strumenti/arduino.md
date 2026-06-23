---
tipo: strumento_digitale
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [MyTech Edizione Green (Le Monnier), Presente e futuro Tecnologia (RCS)]
ultima_revisione: 2026-06-22
---

# Arduino

Arduino è un progetto open source formato da una serie di schede elettroniche (hardware) e da un software, l'ambiente di sviluppo integrato chiamato IDE (Integrated Development Environment). La scheda permette di realizzare in modo semplice e rapido prototipi di apparecchiature elettroniche programmabili: collegando sensori e attuatori, la scheda acquisisce stimoli dall'esterno e restituisce azioni, in base alle istruzioni che vi carichiamo.

## Cos'è

Arduino è una piccola scheda elettronica costruita attorno a un **microcontrollore**, una sorta di minicomputer che è il "cervello" della scheda. Nel microcontrollore viene memorizzato lo **sketch**, cioè il programma che specifica le azioni che Arduino deve eseguire.

La scheda base è la **Arduino UNO**, la più semplice e diffusa; ne esistono altri tipi per usi più complessi o specifici. Tutte le schede Arduino condividono alcune caratteristiche:

- una serie di **piedini (PIN)** attraverso cui il microcontrollore riceve gli stimoli in ingresso (input) e restituisce i segnali in uscita (output);
- i PIN si distinguono in **analogici** (sulla UNO sono 6, A0–A5, solo di input, usati per i sensori) e **digitali** (14, programmabili come input o output, usati ad esempio per accendere/spegnere un LED o leggere un pulsante);
- i pin **5V** e **GND** funzionano come il polo positivo e negativo di una pila;
- una **porta USB** per collegare la scheda al computer e alimentarla, oppure un **connettore di alimentazione** esterno;
- un **pulsante di reset** che riavvia la scheda e fa ricominciare lo sketch.

La scheda può essere ampliata con schede aggiuntive chiamate **shield**, che si innestano sui piedini e ne estendono le funzionalità.

Arduino comunica con il mondo reale grazie a [[sensori-e-attuatori]]:
- i **sensori** rilevano grandezze come luce, suono, movimento, temperatura, umidità e le trasformano in un segnale elettrico inviato al microcontrollore;
- gli **attuatori** (LED, motori elettrici, altoparlanti, buzzer) eseguono le azioni decise dal microcontrollore dopo l'elaborazione.

Si può programmare Arduino scrivendo codice nell'IDE, oppure con software a blocchi simili a [[scratch]] (come Visualino o l'ambiente integrato in [[tinkercad]]), che generano automaticamente il codice dello sketch.

## A cosa serve in classe

Arduino è un ponte concreto tra il [[pensiero-computazionale]] e il mondo fisico: gli studenti non programmano solo lo schermo, ma un oggetto reale che si accende, si muove o suona. È un'ottima porta d'ingresso alla [[robotica-educativa]] e al rapporto tra [[sensori-e-attuatori]] e codice.

In classe permette di:

- rendere visibile il legame **input → elaborazione → output**: un sensore raccoglie un dato, il microcontrollore decide, un attuatore agisce;
- realizzare prototipi di oggetti "smart" che interagiscono con l'ambiente, ad esempio serre automatizzate, stazioni meteorologiche, semafori, robot interattivi, strumenti musicali;
- consolidare le strutture di base della programmazione (sequenza, ripetizione, selezione) già viste con il [[coding-e-programmazione-a-blocchi]], applicandole a un compito reale;
- praticare il [[debugging-come-strategia]]: quando il LED non si accende, l'errore va cercato sia nel circuito sia nello sketch.

## Come iniziare (setup minimo)

Esistono due strade, complementari.

**1. Solo simulazione (consigliata per partire, costo zero).** Con [[tinkercad]] (sezione Circuiti) si disegna il circuito a video — scheda Arduino, breadboard, LED, resistori, sensori — e si programma con i blocchi, che generano in automatico lo sketch. Si testa tutto senza acquistare componenti: ideale per le prime lezioni e per chi non ha ancora il kit.

**2. Con hardware reale.** Serve almeno:
- una scheda **Arduino UNO**;
- una **breadboard** (basetta sperimentale, base in plastica traforata che facilita i collegamenti senza saldature);
- alcuni **LED**, **resistori da 220 Ω**, cavetti;
- un computer con l'**IDE di Arduino** installato.

L'IDE di Arduino è gratuito, multipiattaforma (Windows, macOS, Linux) e scaricabile dal sito ufficiale **arduino.cc**; esiste anche una versione online previa registrazione. In alternativa al codice si può usare un ambiente a blocchi come **Visualino** (open source, multilingua) collegato all'IDE.

**La struttura di uno sketch.** Ogni sketch contiene due funzioni:
- **setup()**: le istruzioni di inizializzazione, eseguite una sola volta all'accensione (ad esempio stabilire quali PIN sono di input o output);
- **loop()**: i comandi veri e propri, ripetuti ciclicamente finché la scheda resta accesa.

Per un primo collegamento di un LED: il piedino più lungo (anodo, +) va verso il PIN di alimentazione, quello più corto (catodo, −) va alla resistenza e poi al PIN GND. La resistenza protegge il LED.

> Nota di sicurezza: se si lavora con l'hardware reale, è opportuno che gli alunni operino sempre sotto la supervisione di un adulto.

## Esempi d'uso didattico

Tre attività di difficoltà crescente, tutte realizzabili con Arduino UNO + breadboard e programmabili a blocchi:

1. **Lampeggiatore.** Far accendere e spegnere un LED a intervalli regolari. Si introducono il comando di scrittura digitale su un PIN, il comando "attendi" (tempo in millisecondi) e il ciclo `loop`. Domanda di rilancio: come si modifica il programma per far restare il LED acceso più a lungo?

2. **Semaforo** → vedi [[attivita-semaforo-arduino]]. Con tre LED (verde, giallo, rosso) collegati a tre PIN si programma la sequenza: verde 8 secondi, poi giallo 2 secondi, poi rosso 5 secondi, in ciclo continuo. Variante: aggiungere il giallo anche nel passaggio dal rosso al verde, come in alcuni Paesi europei.

3. **Effetto "Supercar".** Una fila di LED che si accendono in sequenza per simulare un effetto di scorrimento luminoso. Consolida l'uso di più PIN e dei tempi.

Da qui si può salire verso progetti con sensori (es. una luce che si accende quando la stanza diventa buia, usando un sensore di luminosità) e collegarsi a percorsi più strutturati come una [[uda-robotica-micro-bit]] o ad altre piattaforme come [[mbot]] e [[micro-bit]].

## Costi / account / privacy

- **Software IDE / Visualino**: gratuiti e open source. Tinkercad è gratuito (richiede però la creazione di un account, quindi attenzione all'età degli alunni e alle policy sui dati). *(proposta progettuale)* Per la scuola secondaria di I grado conviene usare account gestiti dal docente o dall'istituto, evitando registrazioni individuali dei minori.
- **Hardware**: la scheda Arduino UNO e i kit base (es. starter kit con scheda, breadboard, componenti e manuale) hanno un costo contenuto ma non nullo. *(proposta progettuale)* Per contenere la spesa si può lavorare a piccoli gruppi su pochi kit, oppure partire interamente in simulazione con Tinkercad.
- **Privacy**: Arduino in sé non raccoglie dati personali. Le cautele riguardano gli ambienti online (account, salvataggi nel cloud). *(proposta progettuale)* Verificare sempre i termini d'uso dei servizi e preferire soluzioni che non richiedano dati personali degli studenti.

## Limiti e rischi educativi

- **Curva iniziale**: i collegamenti sulla breadboard (anodo/catodo, resistenze, GND) possono confondere; senza una guida chiara il rischio è la frustrazione invece dell'apprendimento.
- **Errore "doppio"**: un progetto può non funzionare per un problema di circuito o di codice. È un'occasione per il [[debugging-come-strategia]], ma richiede tempo e metodo.
- *(proposta progettuale)* **Effetto kit**: limitarsi a copiare il circuito proposto senza capire il perché. Conviene far variare i parametri (tempi, PIN, sequenze) e chiedere previsioni prima di eseguire.
- *(proposta progettuale)* **Sicurezza**: l'uso reale di componenti elettronici va supervisionato; per le prime esperienze la simulazione riduce i rischi.

## Adattamenti inclusivi

*(proposta progettuale — da validare; vedi [[inclusione-coding-robotica]])*

- Iniziare con la **programmazione a blocchi** (Tinkercad/Visualino) prima del codice testuale, riducendo il carico legato a sintassi e digitazione.
- Usare **schede-guida visive** con foto dei collegamenti passo passo e codici colore per i cavi (rosso = positivo, nero = negativo).
- Lavorare in **coppie o piccoli gruppi con ruoli** (chi monta il circuito, chi programma, chi documenta), così ogni alunno contribuisce secondo i propri punti di forza.
- Per chi ha difficoltà di motricità fine, privilegiare la **simulazione** dove i collegamenti si fanno con il trascinamento a video.
- Prevedere obiettivi a difficoltà graduata (dal solo lampeggiatore fino al semaforo) per garantire a tutti un risultato visibile.

## Attività che lo usano

- [[attivita-semaforo-arduino]] — il semaforo a tre LED programmato a blocchi.
- [[uda-robotica-micro-bit]] — percorso più ampio su prototipi programmabili (trasferibile ad Arduino).

## Pagine collegate

- [[sensori-e-attuatori]] — Arduino vive del rapporto tra input dei sensori e output degli attuatori.
- [[tinkercad]] — l'ambiente per simulare e programmare circuiti Arduino senza hardware.
- [[robotica-educativa]] — Arduino è una delle piattaforme cardine della robotica a scuola.
- [[coding-e-programmazione-a-blocchi]] — la programmazione a blocchi che genera lo sketch.
- [[debugging-come-strategia]] — quando il circuito o il codice non funzionano.
- [[micro-bit]] — piattaforma alternativa/complementare per gli stessi obiettivi.

## Fonti

- MyTech – Edizione Green. Tecnologia (Brunetto, Bruno — Le Monnier/Mondadori Education), `9788800360043_Tecnologia` (pp. 406–414, 421–429): definizione di Arduino, scheda UNO, microcontrollore, PIN analogici/digitali, alimentazione, shield, sensori e attuatori, IDE, funzioni setup e loop, software Visualino, laboratori Lampeggiatore / Semaforo / Supercar.
- Presente e futuro. Tecnologia (Tubia, Pasquale — RCS), `9788891561633_Tecnologia` (pp. 433–435, 447–449): scheda Arduino UNO Rev3, microcontrollore e sketch, pin 5V/GND, monitor seriale, prototipi "smart", breadboard, LED/anodo/catodo, resistori, sensori, buzzer, funzioni setup() e loop(), IDE da arduino.cc e versione online, programmazione a blocchi con Tinkercad.
- Le sezioni "Costi / account / privacy", "Limiti e rischi educativi" e "Adattamenti inclusivi" contengono in parte proposte progettuali (segnalate nel testo) da validare: nessuna fonte diretta per tali parti.
