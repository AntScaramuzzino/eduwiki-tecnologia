---
tipo: strumento_digitale
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Techno logics - Laboratorio sperimentale STEAM (Raffaello), Upgrade App Scenari di Tecnologia - Guida insegnante (Pearson)]
ultima_revisione: 2026-06-22
---

# micro:bit

## Cos'è

micro:bit (BBC micro:bit) è una piccola scheda a microcontrollore con diversi componenti integrati, progettata fin dall'inizio come strumento educativo per fare coding a scuola con una forte interattività con il mondo reale. È intuitiva da usare e semplice da programmare: le sue caratteristiche permettono di trasformare gli studenti da consumatori a creatori digitali, in grado di sviluppare rapidamente le proprie idee grazie ai componenti già presenti sulla scheda.

Il design è pensato per essere coinvolgente fin dal primo utilizzo: la parte anteriore ricorda il volto di un robot, i componenti sul retro sono etichettati con il proprio nome per favorire l'apprendimento e all'avvio la scheda esegue un programma preinstallato con giochi di luci, suoni e comandi interattivi. Dietro l'aspetto giocoso ci sono però uscite e sensori integrati che consentono di esplorare una vasta gamma di progetti senza bisogno di collegare componenti elettronici esterni.

Componenti principali (la maggior parte presenti nella versione V2):

- **Pulsanti A e B** sul fronte: programmabili separatamente o insieme, offrono tre diverse situazioni di avvio per gli script.
- **Display LED 5x5 e sensore di luce**: matrice di 25 LED rossi per visualizzare dati, testi e simboli animati; la stessa matrice rileva la luce ambientale.
- **Pin GPIO**: 25 strisce dorate sul bordo inferiore per collegare motori, sensori o buzzer tramite clip a coccodrillo o schede di espansione (i pin 0, 1 e 2 funzionano anche come sensori di tocco; il pin 3V alimenta dispositivi esterni; il pin GND è il riferimento di massa).
- **Logo touch** e **microfono** (V2): un ingresso tattile extra e un sensore che rileva il livello sonoro (es. uno script che si avvia con un battito di mani).
- **Sensori integrati**: sensore di temperatura nel processore (stima in °C), magnetometro (bussola) e accelerometro (movimento sui tre assi).
- **Radio bluetooth**: comunicazione con smartphone/tablet e scambio di pacchetti dati tra più schede micro:bit.
- **Porta micro USB**, **pulsante reset**, **altoparlante** (V2) e **connettore batteria** (due pile AAA da 1,5V per usarla senza cavo).

## A cosa serve in classe

micro:bit serve a portare il coding fuori dallo schermo: programmi a blocchi che producono effetti fisici (luci, suoni, lettura di sensori) e che reagiscono al mondo reale. È adatta a una grande varietà di progetti: creazione di giochi, robot, sperimentazioni scientifiche, strumenti musicali e dispositivi di misurazione.

Sul piano didattico, la versatilità e la semplicità d'uso, unite alla fantasia degli studenti, permettono di realizzare attività laboratoriali coinvolgenti che migliorano la capacità di osservazione, l'abilità pratica, la capacità di trovare e risolvere problemi, la creatività e l'immaginazione. La programmazione a blocchi rende immediato il collegamento con il [[pensiero-computazionale]] e con esperienze già note come [[scratch]].

## Come iniziare (setup minimo)

L'ambiente principale è **Microsoft MakeCode**, piattaforma open source gratuita sviluppata appositamente per micro:bit, utilizzabile da browser o app mobile.

Passi minimi:

1. Aprire il browser e andare su `makecode.microbit.org` (l'accesso non richiede registrazione).
2. Iniziare un nuovo progetto. L'interfaccia presenta cinque sezioni: barra superiore (impostazioni, condivisione, conversione da blocchi a JavaScript), istruzioni di programmazione divise per categorie (simili a Scratch, ampliabili con estensioni), area di script, pannello di simulazione, barra inferiore.
3. Costruire lo script con i blocchi: all'apertura sono già presenti i blocchi **"all'avvio"** (istruzioni eseguite una sola volta e inizializzazione delle variabili) e **"per sempre"** (istruzioni eseguite di continuo, ciclicamente). MakeCode è una programmazione basata su eventi.
4. Provare il programma nel **pannello di simulazione**, interattivo e utile per il debug: si possono cliccare i pulsanti virtuali o muovere i cursori per simulare i valori dei sensori. Se lo script misura una grandezza, durante la simulazione compaiono tabella e grafico dinamico dei dati.
5. Per trasferire il programma sulla scheda fisica: collegare micro:bit al computer via cavo micro USB (la scheda appare come una chiavetta chiamata "MICROBIT"), poi premere **Scarica** in basso, oppure scaricare il file **.hex** e trascinarlo nella finestra MICROBIT.

> Nota: senza scheda fisica si può lavorare interamente nel simulatore. **(proposta progettuale)** Per la classe è utile prevedere almeno una scheda ogni 2-3 studenti, così da alternare progettazione al PC e prova sulla scheda reale.

## Esempi d'uso didattico

- **Termometro digitale** (fonte: Techno logics, Lab. 4). Si usa il sensore di temperatura integrato per rilevare i gradi centigradi dell'ambiente: si programma il display per mostrare il valore, si introduce il monitor seriale per registrare i dati e, con la versione V2, si usa la scheda come data logger salvando le letture in una lista. È un'attività che collega coding e scienze (Green Lab / educazione ambientale).
- **Monitoraggio di una serra** (fonte: Techno logics, Lab. 5). Lettura di segnali analogici dai sensori e comunicazione **via radio tra due schede micro:bit**, per trasmettere a distanza i dati rilevati. Introduce i concetti di segnale analogico/digitale e di rete tra dispositivi.
- **micro:bit con Scratch 3.0** (fonte: guida Pearson). La scheda dialoga con Scratch: ad esempio, inclinando la scheda a sinistra/destra sul display compare una freccia nella direzione corrispondente, oppure premendo un pulsante micro:bit riproduce un suono. Buon ponte per chi arriva da [[scratch]].
- **Giochi, robot e strumenti musicali** (fonte: guida Pearson). Progetti creativi che sfruttano pulsanti, display, accelerometro e altoparlante.

## Costi / account / privacy

- **Costi**: l'editor MakeCode è gratuito e open source; la spesa riguarda l'acquisto delle schede fisiche e degli accessori (cavo USB, batterie, eventuali clip a coccodrillo o schede di espansione). **(proposta progettuale)** Conviene un piccolo parco schede condiviso a livello di laboratorio.
- **Account**: l'accesso a MakeCode da browser avviene senza registrazione; è quindi possibile lavorare in classe senza creare account per gli studenti.
- **Privacy**: lavorare senza login riduce la raccolta di dati personali. **(proposta progettuale)** Per la condivisione dei progetti e per attività con minori, verificare le impostazioni della scuola e preferire la condivisione interna; non far inserire dati personali negli script.

## Limiti e rischi educativi

**(proposta progettuale)**

- Il sensore di temperatura nasce per misurare la temperatura interna della scheda: la lettura dell'aria ambiente è approssimata di circa 2-3 °C (fonte: Techno logics). Utile per discutere in classe l'affidabilità delle misure, ma da non presentare come misura precisa.
- Senza schede fisiche sufficienti, l'attività rischia di restare solo simulata: va organizzata la rotazione per garantire l'esperienza con la scheda reale.
- Il fascino dell'oggetto può spostare l'attenzione sull'effetto finale a scapito della comprensione dell'algoritmo: serve dare spazio a progettazione e [[debugging-come-strategia]].
- Gestione del materiale: cavi, pile e clip richiedono cura e tempo di setup; prevedere un kit ordinato per gruppo.

## Adattamenti inclusivi

**(proposta progettuale)**

- **Lavoro in coppia/gruppo con ruoli** (chi programma, chi collega la scheda, chi documenta) per valorizzare punti di forza diversi e ridurre il carico individuale.
- **Output multisensoriale**: display LED, suoni dall'altoparlante e movimento rendono i risultati percepibili per canali diversi, utile per studenti con bisogni differenti.
- **Scaffolding a blocchi**: fornire script parzialmente pronti da completare, per chi ha difficoltà con la sintesi dell'algoritmo.
- **Anticipazione e unplugged**: introdurre i concetti con attività di [[coding-unplugged]] prima di passare alla scheda.
- Coordinare le scelte con i criteri condivisi in [[inclusione-coding-robotica]].

## Attività che lo usano

- [[uda-robotica-micro-bit]] — UDA: progettiamo con micro:bit
- [[attivita-semaforo-arduino]] — confronto con un dispositivo analogo su altra scheda

## Pagine collegate

- [[pensiero-computazionale]]
- [[coding-e-programmazione-a-blocchi]]
- [[scratch]]
- [[sensori-e-attuatori]]
- [[robotica-educativa]]
- [[debugging-come-strategia]]

## Fonti

- Techno logics — Laboratorio sperimentale STEAM (Raffaello Scuola), Appendice 4 "Programmare con micro:bit" (pp. 117-120) e Laboratori 4-5 "Realizzare un termometro" / "Monitorare una serra" (pp. 83-93)
- Upgrade App — Scenari di Tecnologia, Guida insegnante (Pearson), sezione "Coding con BBC micro:bit" e "Usa micro:bit con Scratch 3.0" (pp. 11, 17-18 e attività Area 4)
