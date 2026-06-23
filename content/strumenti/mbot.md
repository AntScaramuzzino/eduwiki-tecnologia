---
tipo: strumento_digitale
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Futura Tech Volume A, Upgrade App Scenari di Tecnologia (guida), Settori Produttivi - Coding Robotica]
ultima_revisione: 2026-06-22
---

# mBot

mBot è un piccolo robot didattico prodotto dalla Makeblock, dotato di due motori e di alcuni sensori, che si programma a blocchi (e in Python) tramite la piattaforma mBlock 5. È pensato per avvicinare gli studenti alla robotica educativa "divertendosi", sviluppando il pensiero computazionale e la capacità di osservare, risolvere problemi e tradurre un'idea in una sequenza di istruzioni.

## Cos'è

mBot è un robot di piccole dimensioni montato su due ruote, ciascuna mossa da un motore collegato alla scheda elettronica: questo permette di programmare separatamente la velocità di ogni singola ruota. Il "cervello" del robot è la scheda elettronica (mCore nella versione classica, mCORE nella versione mBot 2), su cui vengono caricate le sequenze programmate.

Dotazione tipica di sensori e attuatori:
- un **sensore segui-linea** (segui-traccia) posto sotto la base, costituito da LED che illuminano la superficie e da sensori ottici (fotodiodi) che rilevano la luce riflessa, distinguendo il bianco dal nero;
- un **sensore a ultrasuoni** (di prossimità), montabile sulla parte frontale, che misura la distanza dagli ostacoli;
- LED RGB, un display e, nella versione mBot 2, un sensore RGB di colore e un sensore di luminosità;
- un modulo wireless sulla scheda che consente la comunicazione con PC o tablet via Bluetooth, oltre al collegamento via cavo USB.

Il sensore segui-linea, nelle attività dei testi, lavora con due fotodiodi affiancati — uno di sinistra (S1) e uno di destra (S2) — che generano un valore numerico in base alla combinazione di colore letta: 0 (entrambi su nero), 1 (S1 nero, S2 bianco), 2 (S1 bianco, S2 nero), 3 (entrambi su bianco). Questi valori si usano per decidere il movimento del robot con istruzioni condizionali.

## A cosa serve in classe

mBot serve a portare il coding "fuori dallo schermo": il programma scritto a blocchi produce un comportamento fisico osservabile (il robot si muove, accende luci, suona, evita un ostacolo). Questo rende concreti concetti che a video restano astratti: sequenza, ciclo, condizione, lettura di un sensore, attuazione.

In particolare è utile per:
- collegare **algoritmo** e azione reale: la differenza tra "muovi in avanti" e "muovi in avanti finché non rilevi un ostacolo" diventa immediatamente visibile;
- introdurre **sensori e attuatori** in modo tangibile (segui-linea, ultrasuoni, LED, display);
- allenare il **debugging**: quando il robot non fa quello che ci si aspetta, gli studenti devono osservare, formulare ipotesi e correggere il programma;
- lavorare per **problemi aperti** (problem solving): per esempio trovare come agganciare un pennarello al robot perché tracci un percorso.

I testi lo collocano dentro percorsi di pensiero computazionale, non per "formare piccoli informatici", ma per sviluppare la logica con cui si affrontano problemi complessi.

## Come iniziare (setup minimo)

1. **Hardware**: un mBot già assemblato (motori, ruote, scheda, sensore segui-linea; opzionale il sensore a ultrasuoni). Batterie o pacco di alimentazione carichi.
2. **Software**: la piattaforma **mBlock 5**, usabile online dal browser oppure scaricabile su PC/tablet per l'uso offline. Programmazione a blocchi tipo Scratch; mBlock consente anche il linguaggio testuale Python.
3. **Connessione**: collegare il robot al PC o al tablet con il **cavo USB** in dotazione, oppure via **Bluetooth** (in questo caso il robot deve essere acceso per essere riconosciuto dal software; per il PC serve il supporto Bluetooth).
4. **Primo programma**: caricare sulla scheda uno script semplice — far muovere il robot in avanti per qualche secondo, poi fermarlo (blocco di stop) — e verificare che il comportamento corrisponda alle istruzioni.
5. **Spazio**: un'area liscia e libera; per le attività segui-linea serve un foglio bianco con una linea nera spessa (i testi suggeriscono almeno circa 3 cm, così da coprire entrambi i fotodiodi del sensore).

**(proposta progettuale)** Conviene una prima lezione "a vuoto" senza obiettivi di prodotto, solo per far prendere confidenza con i blocchi di movimento e con il ciclo connetti-programma-prova.

## Esempi d'uso didattico

Esempi tratti dalle attività dei testi:

- **Il robot che segue un percorso**: si disegna su un foglio un percorso curvilineo (meglio chiuso, senza angoli netti), si guida prima mBot con i tasti freccia della tastiera per tracciarlo con un pennarello agganciato, poi si programma il sensore segui-linea perché percorra autonomamente la linea nera. È un percorso completo di problem solving (come e dove fissare il pennarello, che spessore dare alla linea).
- **Motore… azione!**: script che muovono mBot avanti e indietro a velocità diverse, lo fanno ruotare di 90°, oppure lo fanno avanzare con i LED verdi accesi fermandolo e accendendo i LED rossi quando il sensore a ultrasuoni rileva un ostacolo a 20 cm.
- **Misura con il sensore di prossimità**: misurare costantemente la distanza tra mBot e un oggetto e reagire (suono di allerta, colori dei LED diversi a seconda della distanza), costruendo anche una tabella di misurazioni.
- **Gioca con la luce / con suoni e luci / schiaccia il pulsante**: attività con i LED RGB, le note musicali e il pulsante della scheda, fino a comunicare una parola in codice Morse.
- **Un percorso sano ed equilibrato (mBot 2, piramide alimentare)**: il robot attraversa cartoncini colorati che rappresentano i livelli della piramide alimentare mediterranea; usando il sensore RGB accende il LED del colore corrispondente e mostra sul display la frequenza di assunzione consigliata. È un esempio di integrazione tra robotica ed educazione alimentare.

## Costi / account / privacy

**(proposta progettuale, da verificare al momento dell'acquisto)**
- mBot è un kit a pagamento prodotto da Makeblock; il costo va verificato presso i rivenditori. Un singolo robot è condivisibile a piccoli gruppi, riducendo la spesa.
- mBlock è disponibile gratuitamente, sia online sia come applicazione offline.
- **Account**: per l'uso base (programmazione a blocchi e caricamento sulla scheda) di norma non è indispensabile un account personale degli studenti; alcune funzioni online (salvataggio in cloud, condivisione) possono richiedere registrazione. Privilegiare l'uso offline o account gestiti dalla scuola.
- **Privacy**: con studenti minori evitare la creazione di account individuali con dati personali; preferire installazione offline o profili di classe. Verificare l'informativa del fornitore e le indicazioni del Garante/della scuola prima di far registrare i ragazzi.

## Limiti e rischi educativi

- **Costo e numeri**: un robot per studente è raramente sostenibile; con il lavoro a gruppi alcuni ragazzi rischiano di "guardare" mentre altri programmano. Va organizzata la rotazione dei ruoli. **(proposta progettuale)**
- **Connessione e setup**: Bluetooth e driver USB possono dare problemi; senza una prova preventiva si perde tempo prezioso. La guida segnala che per il Bluetooth il robot deve essere acceso e il PC deve supportarlo.
- **Effetto "giocattolo"**: il fascino del robot può spostare l'attenzione dal ragionamento (algoritmo, debugging) al semplice farlo muovere. L'obiettivo didattico va tenuto esplicito. **(proposta progettuale)**
- **Spazio e gestione classe**: i robot in movimento richiedono spazio e regole (per evitare urti e cadute dal banco).
- **Dipendenza dall'hardware**: rotture, batterie scariche o sensori starati possono bloccare l'attività; utile avere un piano B (simulazione su schermo o lavoro su Scratch). **(proposta progettuale)**

## Adattamenti inclusivi

**(proposta progettuale)**
- **Ruoli differenziati nel gruppo**: programmatore, "collaudatore" che osserva il robot, responsabile dei materiali, narratore che spiega cosa fa il programma. Così ciascuno partecipa secondo i propri punti di forza.
- **Schede-blocco con immagini**: fornire una mini-legenda visiva dei blocchi mBlock più usati (avanti, ruota, ripeti, se… allora) per chi ha difficoltà di lettura o di memoria di lavoro.
- **Compiti scomposti in passi brevi**: dividere l'attività in micro-obiettivi ("prima fallo andare avanti", "poi fallo fermare") riduce il carico cognitivo.
- **Canale fisico-multisensoriale**: il feedback concreto (luci, suoni, movimento) favorisce gli studenti che apprendono meglio con il fare e con stimoli percettivi.
- **Coppia tutor**: abbinare uno studente più sicuro a uno in difficoltà, alternando chi tiene la tastiera.

Per i criteri generali vedi [[inclusione-coding-robotica]].

## Attività che lo usano

- [[attivita-robot-percorso-mbot]] — Il robot che segue un percorso (mBot)

## Pagine collegate

- [[robotica-educativa]] — mBot è uno strumento tipico della robotica educativa
- [[sensori-e-attuatori]] — segui-linea, ultrasuoni, LED, motori
- [[coding-e-programmazione-a-blocchi]] — si programma a blocchi con mBlock
- [[debugging-come-strategia]] — il robot rende visibile l'errore da correggere
- [[micro-bit]] — altra scheda/robot per il coding a scuola, spesso proposta insieme
- [[attivita-robot-percorso-mbot]] — attività didattica dedicata

## Fonti

- Futura Tech — Corso di Tecnologia (A. Delpiano, M. Giusiano, E. Goldschmidt), Volume A (pp. 238-239: mBot 2, mCORE, sensori RGB/colore/segui-traccia/ultrasuoni, attività piramide alimentare)
- Upgrade. App Scenari di Tecnologia (Pearson) — Guida per l'insegnante (p. 619: mBot per la robotica educativa; pp. 248-253: attività con i sensori, LED, ultrasuoni, motori)
- Coding Robotica / Settori Produttivi (mBot versione 5, mBlock5) (pp. 55 e segg.: sensore segui-linea a due fotodiodi, valori 0-3, attività "percorrere la strada a occhi chiusi", collegamento USB/Bluetooth)
- Alcune sezioni (costi, account/privacy, adattamenti inclusivi, parte dei limiti) sono proposta progettuale da validare: non basate direttamente sui testi.
