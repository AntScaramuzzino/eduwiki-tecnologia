---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Techno logics - Laboratorio sperimentale STEAM, Leonardo - Coding a scuola (Guida Scratch)]
ultima_revisione: 2026-06-22
---

# Coding e programmazione a blocchi

## Definizione breve

Il **coding** è la scrittura di un programma informatico attraverso uno specifico linguaggio di programmazione, al fine di trasformare la soluzione di un problema in una serie di istruzioni elementari eseguibili da una macchina. Nella scuola secondaria di primo grado si lavora soprattutto con la **programmazione a blocchi**: invece di scrivere righe di codice testuale, si incastrano blocchi grafici colorati (come in Scratch) che rappresentano le istruzioni e si combinano come i pezzi di un puzzle.

## Spiegazione per docenti

Il coding è la diretta applicazione del pensiero computazionale alla risoluzione di problemi informatici. Una volta che lo studente ha analizzato un problema con le quattro abilità chiave del pensiero computazionale (astrazione, scomposizione, riconoscimento di pattern, pensiero algoritmico), il coding traduce la soluzione algoritmica in istruzioni che la macchina può eseguire.

La **programmazione a blocchi** abbassa la soglia d'ingresso: lo studente non deve memorizzare la sintassi di un linguaggio testuale né preoccuparsi degli errori di battitura, ma concentra l'attenzione sulla logica della soluzione. I blocchi si incastrano solo nei modi consentiti, quindi il sistema "guida" la costruzione corretta della sequenza.

L'ambiente di riferimento è **Scratch**, creato dal Lifelong Kindergarten Group dei Media Lab del MIT, sotto la guida del prof. Mitchel Resnick. In Scratch i blocchi sono organizzati in **categorie** contrassegnate da colori diversi (Movimento, Aspetto, Suono, Situazioni, Controllo, Sensori, Operatori, Variabili), per facilitare la comprensione delle parti di un progetto e la scelta dei blocchi giusti. I personaggi e gli oggetti animati si chiamano **sprite**: a ogni sprite si assegna uno **script**, cioè la sequenza di istruzioni che deve eseguire, "proprio come a un attore attraverso il suo copione".

Sul piano didattico il coding non è fine a se stesso: serve a far progettare animazioni, storie animate, simulazioni e videogiochi, integrandosi naturalmente con le altre discipline (matematica, scienze, arte, italiano). È un terreno ideale per il lavoro a coppie e per il debugging come pratica di apprendimento dall'errore.

## Spiegazione per studenti

Quando usi un'app o giochi a un videogioco, dietro c'è un **programma**: una lista di ordini precisi che il computer esegue uno dopo l'altro. Scrivere questi ordini si chiama **coding**.

Con la **programmazione a blocchi** non devi scrivere parole strane in inglese: prendi dei blocchi colorati, ciascuno con un comando già scritto sopra (per esempio "fai 10 passi" o "ripeti 4 volte"), e li incastri tra loro come in un puzzle. L'ordine in cui li metti decide cosa succede.

In **Scratch** il tuo personaggio si chiama **sprite** (all'inizio c'è il gatto). Tu gli dai un **copione**, cioè una sequenza di blocchi che gli dice cosa fare: muoversi, parlare, cambiare aspetto, suonare. Quando clicchi sulla bandierina verde, lo sprite "recita" il tuo copione sullo schermo (lo **Stage**, cioè il palcoscenico). Se qualcosa non funziona, non hai sbagliato tu come persona: hai solo dato un ordine sbagliato. Lo cerchi, lo correggi e riprovi.

## Versione ultra-semplice (BES/DSA)

Programmare vuol dire dire al computer cosa fare, **un passo alla volta**.

In Scratch usi blocchi colorati. Ogni blocco è un ordine: "vai avanti", "girati", "dì ciao". Li incastri uno sotto l'altro, come mattoncini. Clicchi sulla bandierina verde e il gatto fa quello che hai scritto.

Se sbaglia, non importa: trovi il blocco sbagliato, lo cambi e riprovi. Provare e correggere fa parte del gioco.

## Esempio concreto in classe

Vogliamo far muovere il gatto di Scratch in un quadrato.

1. La classe scompone il problema: un quadrato è fatto di 4 lati uguali e 4 angoli di 90°.
2. Riconosciamo il **pattern**: "vai avanti, gira di 90°" si ripete 4 volte.
3. Costruiamo lo script con i blocchi: un blocco *Situazioni* "quando si clicca la bandierina verde", poi un blocco *Controllo* "ripeti 4 volte" che contiene i blocchi *Movimento* "fai 100 passi" e "ruota di 90 gradi".
4. Clicchiamo la bandierina verde e osserviamo: il gatto disegna un quadrato.

Se il gatto esce dallo schermo o disegna una figura storta, gli studenti aprono il loro codice, individuano l'errore (per esempio "ruota di 60" invece di "90") e lo correggono. È un'esperienza di **debugging** immediata e concreta.

## Dal concetto all'attività

### Livello base
Far compiere a uno sprite una sequenza semplice e lineare: muoversi, dire una frase, cambiare costume. Obiettivo: capire che i blocchi vengono eseguiti **in ordine, dall'alto verso il basso**, e che la bandierina verde avvia lo script. Adatto per i primi passi in Scratch.

### Livello intermedio
Introdurre il blocco di **ripetizione** (ciclo) e gli **eventi** (la pressione di un tasto, il clic su uno sprite). Esempio: muovere lo sprite con le frecce della tastiera, oppure far ripetere un'animazione. Si comincia a usare la categoria *Controllo* e *Situazioni* e a coordinare più sprite con i **messaggi** ("invia a tutti…", "quando ricevo…").

### Livello avanzato
Costruire un progetto completo con **variabili** (per esempio un punteggio), **condizioni** (se… allora) e **sensori** (rileva il tocco, il bordo). Esempi tipici: un piccolo videogioco, un labirinto, una storia interattiva multi-scena con regia degli sfondi. Qui lo studente progetta in autonomia e gestisce la complessità con scomposizione e debugging.

## Misconcezioni frequenti

- **"Coding = sapere l'inglese / la matematica difficile."** No: la programmazione a blocchi richiede soprattutto logica e ordine; i comandi sono già scritti sui blocchi, spesso in italiano.
- **"Se il programma non funziona, ho sbagliato io / non sono capace."** L'errore (bug) è normale e fa parte del processo: si individua e si corregge. È un'occasione di apprendimento, non un fallimento.
- **"Il computer capisce cosa voglio fare."** No: esegue **esattamente** gli ordini che gli do, nell'ordine in cui li ho messi. Se l'ordine è ambiguo o sbagliato, il risultato sarà sbagliato.
- **"Coding e pensiero computazionale sono la stessa cosa."** Il pensiero computazionale è l'abilità mentale di analizzare e risolvere problemi; il coding è uno dei modi per applicarla con la macchina.
- **"I blocchi sono un giocattolo, il vero coding è solo quello testuale."** La programmazione a blocchi usa gli stessi concetti fondamentali (sequenza, ciclo, condizione, variabile) del codice testuale; è una porta d'ingresso seria.

## Collegamenti interdisciplinari

- **Matematica:** coordinate del piano (lo Stage di Scratch usa coordinate x/y), angoli e rotazioni, variabili, operatori, sequenze e cicli.
- **Scienze:** simulazioni di fenomeni (per esempio il moto del sistema Sole-Terra-Luna realizzato con Scratch nel testo STEAM).
- **Italiano:** progettazione di storie animate, dialoghi e copioni degli sprite, narrazione per scene.
- **Arte e immagine:** disegno e modifica di sprite e sfondi, costumi, composizione visiva.
- **Musica:** uso dei blocchi *Suono* per comporre e sincronizzare audio con l'animazione.

## Strumenti digitali utili

- **[[scratch]]** — ambiente di programmazione a blocchi del MIT, riferimento principale per la secondaria di primo grado (online su scratch.mit.edu o app installabile).
- **[[code-org-e-app-lab]]** — corsi e attività guidate di coding, anche unplugged.
- **[[micro-bit]]** — scheda programmabile a blocchi con l'editor Microsoft MakeCode, per collegare il coding al mondo fisico.
- **[[arduino]]** e **[[tinkercad]]** — per chi vuole passare dalla programmazione a blocchi alla simulazione di circuiti e all'elettronica.

## Valutazione e rubriche

**(proposta progettuale)** Rubrica per valutare un progetto di programmazione a blocchi (Scratch), su quattro livelli.

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Logica della sequenza | Mette i blocchi senza un ordine coerente | Costruisce una sequenza lineare semplice che funziona | Usa cicli ed eventi in modo corretto | Coordina più sprite, condizioni e variabili in modo efficiente |
| Uso dei blocchi e delle categorie | Sceglie i blocchi a caso, con molte prove | Riconosce le categorie principali e i blocchi base | Sceglie i blocchi adatti alla funzione richiesta | Usa con padronanza blocchi di controllo, sensori e variabili |
| Debugging (correzione errori) | Si blocca davanti all'errore o chiede subito aiuto | Individua l'errore con il supporto del docente | Individua e corregge gli errori in autonomia | Previene gli errori e ottimizza il codice |
| Autonomia e creatività | Riproduce solo il modello dato | Completa il compito con qualche personalizzazione | Aggiunge elementi propri al progetto | Progetta un'idea originale e la realizza interamente |

Approfondimenti: vedi **[[valutazione-coding-robotica]]**.

## Inclusione e adattamenti

**(proposta progettuale)** La programmazione a blocchi è di per sé inclusiva: elimina la barriera della sintassi testuale, usa il colore e il riconoscimento visivo, e permette il "prova e correggi" senza penalizzare l'errore.

Adattamenti utili:
- **DSA:** privilegiare il riconoscimento visivo dei blocchi (colore + forma), fornire schemi di riferimento delle categorie, evitare la copiatura da testo, lasciare più tempo.
- **BES / difficoltà di pianificazione:** partire da progetti già impostati da remixare e completare; scomporre il compito in micro-passi con checklist.
- **Lavoro a coppie (pair programming):** uno "guida" e uno "scrive", con scambio di ruoli; favorisce verbalizzazione e cooperazione.
- **Coding unplugged:** per chi ha poca dimestichezza con il dispositivo, partire da attività senza computer (carta, gioco, percorsi) prima di passare allo schermo.

Approfondimenti: vedi **[[inclusione-coding-robotica]]**.

## Fonti

- Techno logics - Laboratorio sperimentale STEAM (Raffaello Scuola), Area 3 "Pensiero computazionale e coding" (p.44-46) e Appendice 1 "Primi passi in Scratch" (p.98-101)
- Leonardo - Coding a scuola, Guida Scratch "La catena del freddo" (Benedetti, Romiti) — concetti di sprite, script, sfondo, messaggi
- Le sezioni "Valutazione e rubriche" e "Inclusione e adattamenti" sono in gran parte proposta progettuale da validare

## Pagine collegate

- [[pensiero-computazionale]]
- [[algoritmo-e-diagrammi-di-flusso]]
- [[scratch]]
- [[coding-unplugged]]
- [[debugging-come-strategia]]
- [[attivita-labirinto-scratch]]
