---
tipo: attività_didattica
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Techno logics - Laboratorio sperimentale STEAM (Raffaello Scuola), Guida docente NEXT - Robotica con Arduino UNO]
ultima_revisione: 2026-06-22
---

# Attività: il semaforo con Arduino

Costruire e programmare un semaforo a tre tempi (rosso, giallo, verde) è una delle attività più efficaci per introdurre alla scuola secondaria di primo grado il legame tra elettronica, coding e pensiero computazionale. Il semaforo è un oggetto familiare e dal funzionamento intuitivo: gli studenti sanno già "cosa deve fare" il dispositivo, quindi possono concentrarsi sul *come* tradurre quel comportamento in una sequenza di istruzioni.

L'attività può essere svolta interamente in simulazione con **Tinkercad Circuits** (senza acquistare componenti) oppure con una scheda **Arduino UNO** fisica, breadboard, LED e resistori. Entrambe le strade sono documentate nei testi di riferimento.

## Target

- Classi seconde o terze della scuola secondaria di primo grado.
- Adatta sia a gruppi alle prime esperienze con il coding a blocchi (versione Tinkercad) sia a classi che hanno già lavorato con Scratch o micro:bit. L'ambiente di programmazione a blocchi di Tinkercad usa una logica molto simile a quella di Scratch (blocchi trascinabili, ciclo "sempre"), quindi il passaggio è facilitato. *(proposta progettuale)*

## Durata

- **Versione simulata (Tinkercad):** 2-3 ore (1-2 lezioni), comprensive di assemblaggio del circuito, programmazione e test. *(proposta progettuale, sulla base della struttura a 6 step del laboratorio Techno logics)*
- **Versione con hardware fisico:** aggiungere 1 ora per il cablaggio reale su breadboard e l'eventuale uso dell'IDE di Arduino. *(proposta progettuale)*

## Materiali

**Versione simulata (consigliata per iniziare):**
- Computer con connessione a Internet.
- Applicazione web Tinkercad Circuits (`www.tinkercad.com/learn/circuits`).

**Versione con hardware fisico:**
- Scheda Arduino UNO (R3) e cavo USB.
- Breadboard (basetta sperimentale, senza saldature).
- 3 LED: rosso, giallo, verde.
- 3 resistori (vedi nota sui valori).
- Cavi di collegamento (jumper).

**Nota sui valori dei resistori.** I LED vanno sempre protetti da un resistore in serie, perché i 5V della scheda sono eccessivi e una corrente superiore ai ~20 mA riduce la durata del componente. I due testi indicano valori diversi, entrambi validi:
- *Techno logics*: una resistenza da **330 Ω** è più che sufficiente per LED rosso, giallo e verde con Arduino UNO.
- *Guida NEXT*: calcolando con la legge di Ohm (R = (V_alim − V_led) / I, con I = 20 mA) si ottengono valori più bassi (es. 150 Ω per il rosso); per prudenza la guida usa **180 Ω** per rosso e giallo e 150 Ω per il verde.

In classe conviene adottare un valore unico e abbondante (330 Ω) per semplicità: una resistenza maggiore è sempre sicura, al massimo rende il LED un po' meno luminoso.

## Prerequisiti

- Concetto di **algoritmo** come sequenza ordinata di istruzioni.
- Esperienza di base con la **programmazione a blocchi** (es. Scratch): blocchi trascinabili, ciclo che si ripete. *(proposta progettuale)*
- Nozioni elementari di circuito elettrico: il concetto di "circuito chiuso", polo positivo e negativo. Utile (non indispensabile) aver incontrato LED e resistore.
- Per la versione fisica: saper riconoscere anodo (+, terminale più lungo) e catodo (−, terminale più corto) di un LED.

## Procedura (fasi)

La sequenza segue i sei step del laboratorio *Techno logics* in Tinkercad. Tra parentesi le integrazioni per la versione con codice testuale dell'IDE Arduino (Guida NEXT).

**Fase 1 — Assemblare il circuito di base.**
Creare un nuovo circuito in Tinkercad, rinominarlo "Semaforo a tre tempi" e trascinare dallo starter-kit Arduino il blocco "Breadboard": la basetta arriva già collegata all'alimentazione della scheda (pin 5V con filo rosso, GND con filo nero).

**Fase 2 — Inserire il primo LED.**
Trascinare un LED sulla breadboard, sceglierne il colore (rosso). Collegare l'anodo (+) a un pin digitale, ad esempio il **pin 13**; collegare il catodo (−) alla pista di massa (GND). I 14 pin digitali (0-13) funzionano qui come uscite digitali: a due stati, BASSO = 0 V (spento) e ALTO = 5 V (acceso).

**Fase 3 — Primo test e scoperta del problema della corrente.**
Aprire l'area Codice, impostare il pin 13 su ALTO dentro il ciclo "sempre", avviare la simulazione. Tinkercad segnala un sovraccarico: la corrente supera i 20 mA consigliati. È un'occasione preziosa per far ragionare la classe: *come limitare la corrente?* La risposta è il resistore. (In simulazione non si danneggia nulla: ottimo esempio del perché si progetta prima al simulatore.)

**Fase 4 — Inserire il resistore.**
Aggiungere un resistore in serie con il LED, impostandone il valore (330 Ω). Far osservare che il resistore non ha polarità (può essere orientato liberamente) e che il suo valore è codificato dalle bande colorate. Rilanciare la simulazione: ora il LED si accende senza errori.

**Fase 5 — Completare il semaforo.**
Aggiungere il LED giallo (pin 12) e il LED verde (pin 11), ciascuno con il proprio resistore in serie. Far ragionare gli studenti su come portare tutti i catodi a un'unica pista GND, sfruttando i collegamenti interni della breadboard.

**Fase 6 — Programmare la sequenza.**
Tradurre in blocchi (o in codice) il comportamento del semaforo. Specifiche del laboratorio Techno logics:
- rosso acceso per 5 secondi;
- poi verde acceso (rosso spento) per 5 secondi;
- poi giallo acceso (verde spento) per 2 secondi;
- il ciclo ricomincia dal rosso.

Si usano i blocchi `imposta pin [11/12/13] su [ALTO/BASSO]` e il blocco `attendi (...) sec`. Avviare la simulazione e verificare. In caso di malfunzionamento, applicare il **debugging**: controllare i collegamenti, rivedere il codice un blocco alla volta per isolare l'errore.

**Versione con codice testuale (IDE Arduino, Guida NEXT).** Lo stesso comportamento si scrive così, con i pin 5 (rosso), 6 (giallo), 7 (verde):

```c
#define LEDrosso 5
#define LEDgiallo 6
#define LEDverde 7

void setup() {
  pinMode(LEDrosso, OUTPUT);
  pinMode(LEDgiallo, OUTPUT);
  pinMode(LEDverde, OUTPUT);
}

void loop() {
  digitalWrite(LEDverde, HIGH);
  delay(5000);
  digitalWrite(LEDverde, LOW);
  digitalWrite(LEDrosso, HIGH);
  delay(5000);
  digitalWrite(LEDrosso, LOW);
  digitalWrite(LEDgiallo, HIGH);
  delay(5000);
  digitalWrite(LEDgiallo, LOW);
}
```

La funzione `delay()` mette in pausa la scheda per i millisecondi indicati (5000 = 5 secondi). La Guida NEXT introduce anche la variante con **variabile contatore** e **ciclo `for`**, per far lampeggiare il semaforo un numero finito di volte (es. 10 cicli): un ottimo aggancio per spiegare i concetti di variabile e ciclo.

## Prodotto finale

Un semaforo a tre tempi funzionante — virtuale in Tinkercad oppure fisico su breadboard — che esegue ciclicamente la sequenza rosso → verde → giallo con i tempi programmati. A corredo: lo schema del circuito e lo script (a blocchi o testuale) commentato. *(proposta progettuale per la parte di documentazione)*

Possibili estensioni (da Guida NEXT, sezione esercizi):
- doppio semaforo sincronizzato (pedoni + automobili);
- semaforo accessibile per non vedenti, aggiungendo un **buzzer** che emette un suono durante il lampeggio del giallo.

## Valutazione

Si valutano tre dimensioni: il funzionamento del prodotto, la qualità del processo (incluso il debugging) e la comprensione dei concetti. *(proposta progettuale — rubrica da validare)*

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Costruzione del circuito | Assembla il circuito solo con aiuto costante; collegamenti spesso errati | Assembla il circuito di base con qualche indicazione; riconosce LED e resistore | Assembla autonomamente il circuito completo con i tre LED e i resistori | Realizza un circuito ordinato ed efficiente (es. catodi su unica pista GND) e sa spiegarne le scelte |
| Programmazione della sequenza | Compone la sequenza solo seguendo passo passo l'insegnante | Realizza la sequenza base rosso-verde-giallo con i tempi indicati | Realizza la sequenza in autonomia e ne modifica correttamente i tempi | Introduce varianti (ciclo for, contatore, doppio semaforo) spiegando la logica |
| Debugging e problem solving | Si blocca davanti all'errore e attende la soluzione | Individua l'errore con aiuto; prova una correzione alla volta | Isola l'errore in modo sistematico e lo corregge | Anticipa i problemi (es. corrente sul LED) e propone soluzioni motivate |
| Comprensione dei concetti | Usa i termini in modo impreciso | Riconosce pin digitale, stato ALTO/BASSO, funzione del resistore | Spiega correttamente il ruolo di pin, resistore e ciclo | Collega i concetti (legge di Ohm, uscita digitale, ciclo) e li trasferisce a nuovi casi |

## Adattamenti inclusivi

*(sezione in larga parte proposta progettuale; vedi anche [[inclusione-coding-robotica]])*

### BES/DSA
- Fornire lo schema del circuito già stampato e i blocchi di codice precompilati da riordinare, riducendo il carico di lettura/scrittura.
- Lavorare in coppia con ruoli definiti (chi cabla, chi programma), a rotazione.
- Privilegiare la versione simulata in Tinkercad: l'errore non ha conseguenze e si può ripetere all'infinito, abbassando l'ansia da prestazione.
- Usare un valore unico di resistore (330 Ω) per evitare il calcolo con la legge di Ohm a chi è in difficoltà con i numeri.

### Plusdotati
- Proporre subito le estensioni: ciclo `for` con contatore, doppio semaforo sincronizzato pedoni/automobili.
- Sfidarli a calcolare i valori dei resistori con la legge di Ohm partendo dalle tensioni dei diversi colori di LED (rosso ~2 V, verde ~2,4 V, blu ~3,2 V).
- Far progettare un semaforo "intelligente" con sensore (es. pulsante pedonale o sensore di distanza).

### L2
- Affiancare al testo un glossario visivo dei componenti (LED, resistore, breadboard, pin) con immagine + parola.
- Sfruttare il carattere visivo dell'ambiente a blocchi e della simulazione, che riduce la dipendenza dalla lingua.
- Usare il semaforo come oggetto-ponte: il suo significato (rosso/verde/giallo) è interculturale e immediatamente comprensibile.

## Pagine collegate

- [[arduino]]
- [[tinkercad]]
- [[sensori-e-attuatori]]
- [[coding-e-programmazione-a-blocchi]]
- [[debugging-come-strategia]]
- [[inclusione-coding-robotica]]

## Fonti

- Techno logics — Laboratorio sperimentale STEAM, Raffaello Scuola (Furci, Pozzi, Monti), Laboratorio 1 "Semaforo a tre tempi (Arduino UNO)", pp. 66-71 (## p.67-72 del testo estratto).
- Guida docente NEXT — "Robotica con Arduino UNO", sezione "Tre LED per un semaforo" e "Un LED esterno", pp. 54-58.
- Le sezioni Durata, parte dei Materiali, Prodotto finale (documentazione), Valutazione (rubrica) e Adattamenti inclusivi sono in larga parte proposta progettuale da validare.
