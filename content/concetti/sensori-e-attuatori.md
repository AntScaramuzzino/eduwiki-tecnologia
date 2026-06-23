---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Coding e robotica (Barbero, Vaschetto - Paravia/Pearson)]
ultima_revisione: 2026-06-22
---

# Sensori e attuatori

## Definizione breve

I **sensori** sono i dispositivi che fanno "percepire" l'ambiente a una macchina: rilevano una grandezza fisica (luce, temperatura, pressione, distanza, movimento...) e la trasformano in un segnale elettrico, cioè in un **input** che la scheda può elaborare. Gli **attuatori** sono i dispositivi che fanno "agire" la macchina sul mondo: ricevono un comando dalla scheda, cioè un **output**, e lo trasformano in un effetto fisico (luce, suono, movimento). In mezzo c'è la scheda di controllo (Arduino, micro:bit, mCore di mBot), che riceve gli input dai sensori, li elabora secondo il programma e invia i comandi di output agli attuatori.

## Spiegazione per docenti

Il modello da tenere a mente è la catena **input → elaborazione → output**, che è la stessa logica del computer (periferiche di input e di output) applicata però agli oggetti fisici. Come sintetizza il testo *Coding e robotica*: "Arduino riceve gli input da dispositivi detti sensori, li elabora e invia i comandi di output a dispositivi detti attuatori" (p.117).

Esempi tratti dai libri di testo:

- **Sensori**: il pulsante (restituisce 1 logico se premuto, 0 se rilasciato); il potenziometro e lo slider (variano la quantità di corrente); il sensore di temperatura (genera un segnale che dipende dalla temperatura ambiente); il sensore di pressione (rileva la pressione delle dita); il sensore di luce; l'accelerometro (rileva il movimento); la bussola/sensore magnetico (rileva la direzione del campo magnetico).
- **Attuatori**: il LED (emette luce colorata); il buzzer (emette suoni); il motore (trasmette il movimento ad altri apparati).

Un punto tecnico utile da spiegare è il collegamento tramite **pin**. Sulla scheda Arduino i pin digitali (14) possono funzionare sia come input sia come output: vi si possono collegare sensori (input) o attuatori (output) per azioni di tipo acceso/spento. I pin analogici (6) possono solo acquisire un segnale dall'esterno (solo input), quindi vi si collegano solo sensori che inviano un segnale continuo (come il potenziometro): il valore letto viene restituito come numero compreso tra 0 e 1023 (p.118). Questo è il passaggio concettuale chiave: il mondo fisico, continuo, viene "tradotto" in numeri che il programma può confrontare e usare nelle decisioni.

Nella robotica educativa di base questa catena è già pronta: il robot **mBot** ha la scheda mCore con una serie di sensori e due motori che gli permettono di muoversi (p.64). Anche **micro:bit** integra sensori interni (luce, temperatura, accelerometro, bussola) senza bisogno di cablaggio (p.116). Conviene partire da queste schede "tutto incluso" prima di passare ai sensori e attuatori da cablare su breadboard con Arduino.

## Spiegazione per studenti

Immagina un robot come un essere vivente molto semplice. Per fare qualcosa di sensato deve prima **accorgersi** di cosa succede intorno a lui, poi **decidere**, poi **agire**.

- I **sensori** sono i suoi "sensi": gli occhi (sensore di luce), il tatto (pulsante o sensore di pressione), il senso dell'equilibrio (accelerometro). Trasformano ciò che c'è nel mondo (quanta luce, che temperatura, se è premuto un tasto) in un segnale elettrico, cioè in numeri.
- La **scheda** è il "cervello": legge i numeri arrivati dai sensori, esegue il programma che hai scritto e decide cosa fare.
- Gli **attuatori** sono i suoi "muscoli e la sua voce": il motore lo fa muovere, il LED si accende, il buzzer suona. Trasformano la decisione del programma in un effetto reale.

La regola d'oro è sempre la stessa: **leggo (input) → decido (elaborazione) → faccio (output)**. Un sensore senza programma non serve a niente, e un attuatore senza un comando non si muove.

## Versione ultra-semplice (BES/DSA)

Un robot funziona in tre passi.

1. **SENTE** con i sensori. Il sensore è come un senso: l'occhio, l'orecchio, il tatto del robot. Esempi: sensore di luce, pulsante, sensore di temperatura.
2. **PENSA** con la scheda. La scheda è il cervello: legge quello che il sensore ha sentito e decide.
3. **FA** con gli attuatori. L'attuatore è come un muscolo o la voce: motore (si muove), LED (si accende), buzzer (suona).

In una frase: **il sensore entra (input), l'attuatore esce (output).**

## Esempio concreto in classe

**La lampada automatica.** Vogliamo che un LED si accenda quando la stanza diventa buia.

- **Sensore (input)**: il sensore di luce misura quanta luce c'è e la trasforma in un numero.
- **Elaborazione**: il programma controlla "se il numero della luce è basso (è buio), allora...".
- **Attuatore (output)**: ...accendi il LED.

Con micro:bit si fa subito, perché il sensore di luce è già dentro la scheda. Si chiede agli studenti di indicare, per ogni pezzo, se è un sensore o un attuatore e se è un input o un output: questo fissa il concetto prima ancora di programmare. Si può poi variare l'idea: invece del LED, far suonare il buzzer (cambia l'attuatore); invece del buio, reagire allo scuotimento con l'accelerometro (cambia il sensore).

## Dal concetto all'attività

### Livello base
Riconoscimento e classificazione, senza coding. Si mostra una serie di dispositivi reali o in figura (pulsante, LED, motore, sensore di temperatura, buzzer, sensore di luce) e si chiede di classificarli in due colonne: **sensore/input** oppure **attuatore/output**. Poi si completa la catena input → elaborazione → output di alcuni oggetti di uso comune (porta automatica, luce con sensore di movimento, semaforo). **(proposta progettuale)**

### Livello intermedio
Un solo sensore e un solo attuatore con scheda "tutto incluso". Con **micro:bit**: "quando scuoto la scheda (accelerometro = input), mostra la temperatura (uso del sensore di temperatura) oppure accendi i LED (output)". Gli studenti scrivono lo script a blocchi e verificano la catena leggo → decido → faccio. Collegamento all'attività [[attivita-robot-percorso-mbot]], dove il sensore di linea (input) guida i motori (output).

### Livello avanzato
Più sensori/attuatori e logica condizionale, con cablaggio. Con **Arduino** su breadboard: collegare un sensore a un pin analogico (es. potenziometro o sensore di luce) e leggere il valore 0–1023, poi pilotare un attuatore (LED o motore) in base a soglie diverse. Esempio guida: il **semaforo** che cambia stato, vedi [[attivita-semaforo-arduino]]. Si introduce la distinzione tra pin digitali (input/output, acceso/spento) e pin analogici (solo input, segnale continuo).

## Misconcezioni frequenti

- **"Il sensore decide cosa fare."** No: il sensore solo rileva e trasforma in segnale. La decisione la prende il programma sulla scheda.
- **"Sensore e attuatore sono la stessa cosa."** Hanno ruoli opposti: il sensore porta informazione *dentro* (input), l'attuatore porta azione *fuori* (output).
- **"Il robot 'vede' o 'sente' come noi."** Il sensore misura una sola grandezza alla volta e la trasforma in numeri: non c'è comprensione, c'è misura.
- **"Un pulsante è un attuatore perché lo schiaccio io."** È un sensore: fornisce un input (1 se premuto, 0 se rilasciato). Confonde l'azione dell'utente con il ruolo del dispositivo nel circuito.
- **"Più sensori = robot più intelligente."** L'intelligenza apparente sta nel programma che usa i dati, non nel numero di sensori.
- **"I pin analogici e digitali sono uguali."** I digitali possono essere input o output; gli analogici solo input (acquisiscono un segnale continuo).

## Collegamenti interdisciplinari

- **Scienze**: organi di senso e sistema nervoso come analogia della catena sensore → cervello → muscolo; le grandezze fisiche misurate (temperatura, luce, pressione, accelerazione). **(proposta progettuale)**
- **Matematica**: lettura e interpretazione di valori numerici, intervalli (la scala 0–1023), soglie e disuguaglianze usate nelle condizioni. **(proposta progettuale)**
- **Educazione civica / tecnologia e società**: oggetti interattivi e automazione nella vita quotidiana (irrigazione automatica, illuminazione, domotica) e riflessione sull'affidabilità dei sistemi automatici. **(proposta progettuale)**
- **Italiano**: descrivere a parole il funzionamento di un dispositivo seguendo la struttura input-elaborazione-output. **(proposta progettuale)**

## Strumenti digitali utili

- [[micro-bit]] — sensori interni (luce, temperatura, accelerometro, bussola) e LED già integrati: ideale per iniziare senza cablaggio.
- [[mbot]] — robot con scheda mCore, sensori di bordo e due motori; si programma a blocchi con mBlock.
- [[arduino]] — per collegare sensori e attuatori reali tramite pin e breadboard; introduce input analogici e digitali.
- [[scratch]] / S4A (Scratch for Arduino) — estensione che fa interagire gli sprite con sensori e attuatori collegati alla scheda.
- [[tinkercad]] — simulazione di circuiti con Arduino, sensori e attuatori senza hardware fisico. **(proposta progettuale)**

## Valutazione e rubriche

Rubrica per la comprensione del concetto e il suo uso in attività di coding/robotica. **(proposta progettuale)**

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Distinguere sensore/attuatore | Confonde i due ruoli | Riconosce i casi più comuni con aiuto | Classifica correttamente dispositivi noti | Classifica e motiva anche casi nuovi o ambigui |
| Catena input → elaborazione → output | Non individua i tre passaggi | Riconosce i passaggi su un esempio dato | Ricostruisce la catena in autonomia | Progetta una catena nuova per un problema proposto |
| Uso nel programma | Non collega sensore e azione | Usa un sensore e un attuatore con guida | Usa una condizione (se... allora) sui dati del sensore | Combina più sensori/attuatori con logica appropriata |
| Linguaggio tecnico | Usa termini impropri | Usa input/output e sensore/attuatore con incertezza | Usa i termini correttamente | Spiega ad altri usando il lessico tecnico in modo preciso |

## Inclusione e adattamenti

- Fornire una **mappa visiva** della catena sensore → scheda → attuatore con icone (occhio, cervello, muscolo) e colori fissi: blu = input/sensore, rosso = output/attuatore. **(proposta progettuale)**
- Usare schede "tutto incluso" (micro:bit, mBot) per ridurre il carico del cablaggio e concentrarsi sul concetto. **(proposta progettuale)**
- Proporre prima attività di **classificazione concreta** con oggetti veri da toccare, poi passare al codice. **(proposta progettuale)**
- Lavoro a **coppie con ruoli** (chi legge i sensori, chi gestisce gli attuatori) per favorire la partecipazione e ridurre l'ansia da prestazione. **(proposta progettuale)**
- Glossario illustrato minimo con i termini chiave (sensore, attuatore, input, output, pin) sempre disponibile. **(proposta progettuale)**
- Vedi anche [[inclusione-coding-robotica]] per indicazioni trasversali.

## Fonti

- Coding e robotica (Barbero, Vaschetto - Paravia/Pearson) — p.64 (mBot e scheda mCore), p.116 (sensori interni di micro:bit), p.117 (definizione di sensori e attuatori, catena input/output, esempi), p.118 (pin digitali e analogici, valori 0–1023, S4A)
- Le sezioni metodologiche, le rubriche e gli adattamenti inclusivi sono proposta progettuale da validare.

## Pagine collegate

- [[robotica-educativa]]
- [[arduino]]
- [[micro-bit]]
- [[mbot]]
- [[attivita-semaforo-arduino]]
- [[pensiero-computazionale]]
