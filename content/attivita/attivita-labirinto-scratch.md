---
tipo: attività_didattica
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Techno logics - Laboratorio sperimentale STEAM, Tecnologia (Pearson 9788891561633)]
ultima_revisione: 2026-06-22
---

# Attività: il labirinto in Scratch

Attività di coding a blocchi in cui gli studenti programmano uno sprite (un topo, il gatto di Scratch o un personaggio a scelta) per attraversare un labirinto e raggiungere un traguardo. È un'attività ponte tra il pensiero algoritmico e la codifica: lo stesso labirinto serve a far scoprire la differenza tra un algoritmo "su misura" per un singolo schema e una procedura generale capace di risolvere molti labirinti diversi.

L'attività riprende il laboratorio "Il topo nel labirinto" del testo *Techno logics*, dove il topo deve raggiungere un muffin spostandosi con i blocchi «avanti» e con le rotazioni di 90° a destra e a sinistra.

## Target

- Classe: prima, seconda o terza della scuola secondaria di I grado.
- Adatta come prima esperienza strutturata di programmazione a blocchi, ma anche come consolidamento dopo attività introduttive su Scratch.
- Si lavora individualmente nella prima fase (progettazione dell'algoritmo) e in coppia/gruppo nelle fasi di confronto e debugging (apprendimento cooperativo). **(proposta progettuale)**

## Durata

- 2-3 ore di lezione (2 unità da 50-60 minuti più un'eventuale terza per le estensioni). **(proposta progettuale)**
  - Fase 1-2 (programmare la via d'uscita e provare un nuovo labirinto): circa 1 ora.
  - Fase 3-4 (debug, confronto in classe, riapplicazione): circa 1 ora.
  - Fase 5 (estensione: costruire il proprio labirinto): 1 ora aggiuntiva.

## Materiali

- Computer o tablet con connessione a Internet.
- Scratch, gratuito, utilizzabile online dal sito `scratch.mit.edu` cliccando su "Crea", oppure installato come programma su qualsiasi sistema operativo: entrambe le opzioni danno accesso allo stesso ambiente di lavoro.
- Il progetto Scratch del labirinto già predisposto (nel testo *Techno logics* è raggiungibile tramite QR code): contiene il labirinto, lo sprite del topo e i blocchi di movimento. In alternativa il labirinto può essere costruito dal docente o dagli studenti.
- Carta quadrettata e matita per progettare e provare l'algoritmo "a secco" prima o accanto al lavoro al computer.
- Videoproiettore o LIM per il confronto collettivo dei codici. **(proposta progettuale)**

## Prerequisiti

- Conoscere il concetto di algoritmo come sequenza ordinata di istruzioni (vedi [[algoritmo-e-diagrammi-di-flusso]]).
- Saper distinguere, almeno a livello intuitivo, tra pensiero algoritmico (trovare una procedura) e codifica (scrivere il programma): è proprio questa distinzione l'obiettivo concettuale dell'attività.
- Familiarità di base con l'interfaccia di Scratch: la **scena** con gli **sprite** sulla destra, l'**area degli script** dove si trascinano i blocchi e le **categorie di blocchi** (vedi [[scratch]] e [[coding-e-programmazione-a-blocchi]]).
- Conoscere il significato di **sprite** (gli oggetti o personaggi che eseguono le azioni nel programma) e di **debug** (la fase in cui si individuano e si correggono gli errori, i *bug*, nel codice).

## Procedura (fasi)

1. **Avvio e attivazione (10 min).** Si presenta il labirinto e si pone la domanda guida: come facciamo a dare al topo le istruzioni giuste per raggiungere il muffin? Si recupera la differenza tra "conoscere cos'è un algoritmo" e "pensare in modo algoritmico".

2. **Programmare la via d'uscita (20-25 min).** Gli studenti osservano il labirinto e i blocchi di movimento disponibili: «avanti» (uno o più passi) e le rotazioni di 90° verso destra e verso sinistra. Completano lo script trascinando i blocchi nell'area degli script fino a far raggiungere al topo il traguardo. Possono progettare prima la sequenza su carta (anche in pseudocodice) e poi tradurla nei blocchi.

3. **Debug (15 min).** Si esegue il programma e si verifica se il topo arriva al muffin senza attraversare le pareti. Anche se nel progetto non è impostata la fine del gioco al tocco del muro, l'attraversamento della parete va considerato una soluzione non accettabile. Gli errori si correggono modificando l'ordine o il numero dei blocchi.

4. **Riapplicare l'algoritmo a un nuovo labirinto (15-20 min).** Si cambia schema (nel progetto Scratch si preme la barra spaziatrice per passare al secondo labirinto) e si verifica: il mio algoritmo funziona ancora? La scoperta chiave è che lo specifico insieme di istruzioni pensato per il primo labirinto non si adatta a uno schema diverso. Da qui la riflessione: per risolvere ogni labirinto serve il pensiero algoritmico, cioè una procedura generale, non una sequenza valida una sola volta.

5. **Confronto in classe (10 min).** Si confrontano gli algoritmi prodotti: tutti hanno scelto lo stesso numero e lo stesso ordine di istruzioni? Si discute perché esistono soluzioni diverse ugualmente corrette e quali sono più efficienti (meno passi).

6. **Estensione - verso una procedura generale (facoltativa).** Si introduce un metodo generale di risoluzione, ad esempio il *wall follower* ("segui il muro"): tenere sempre una mano (sinistra o destra) a contatto con la parete porta con certezza all'uscita, anche se non per la via più breve. Si può poi proporre di costruire il proprio labirinto con l'algoritmo di "divisione ricorsiva", lavorando in gruppo su carta quadrettata. **(estensione presente nel testo Techno logics)**

## Prodotto finale

- Il progetto Scratch funzionante: lo sprite raggiunge il traguardo in uno o più labirinti senza attraversare le pareti.
- Lo storyboard/pseudocodice dell'algoritmo su carta (la sequenza di istruzioni progettata prima della codifica).
- Facoltativo: un breve testo o screenshot in cui lo studente spiega perché l'algoritmo del primo labirinto non funzionava sul secondo e come ha modificato la soluzione (evidenza della riflessione sul pensiero algoritmico). **(proposta progettuale)**

## Valutazione

La rubrica seguente è una **(proposta progettuale)** da validare, costruita sui contenuti dell'attività.

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Progettazione dell'algoritmo (pseudocodice/storyboard) | Elenca istruzioni in disordine o incomplete | Scrive una sequenza che funziona solo se molto guidato | Scrive una sequenza ordinata e corretta in autonomia | Scrive una sequenza corretta e ottimizzata (pochi passi) e la motiva |
| Codifica in Scratch (uso dei blocchi) | Usa i blocchi a caso, con molti errori di sequenza | Compone lo script con aiuto e qualche errore | Compone lo script corretto in autonomia | Compone lo script corretto e lo riadatta a un nuovo labirinto |
| Debug | Non riconosce gli errori | Individua l'errore solo se segnalato | Individua e corregge gli errori da solo | Individua, corregge e spiega la causa dell'errore |
| Pensiero algoritmico (generalizzazione) | Non coglie la differenza tra algoritmo specifico e generale | Riconosce che l'algoritmo non funziona sul nuovo schema | Spiega perché serve una procedura generale | Propone o applica una procedura generale (es. wall follower) |
| Collaborazione e confronto | Non partecipa al confronto | Partecipa se sollecitato | Confronta il proprio codice con i compagni | Argomenta scelte diverse e ne valuta l'efficienza |

Vedi anche i criteri trasversali in [[valutazione-coding-robotica]].

## Adattamenti inclusivi

### BES/DSA
- Fornire il progetto Scratch già pronto con il labirinto e lo sprite, in modo da concentrarsi solo sulla sequenza dei movimenti.
- Mettere a disposizione una versione cartacea del labirinto su griglia quadrettata per provare il percorso "a secco" prima di codificare.
- Ridurre il numero di blocchi disponibili e usare cartellini-blocco fisici da ordinare prima di trascinarli a schermo.
- Valorizzare il canale visivo (esecuzione passo-passo, evidenziazione del blocco in esecuzione) e dare tempi più lunghi. **(proposta progettuale, in linea con [[inclusione-coding-robotica]])**

### Plusdotati
- Chiedere di risolvere il labirinto con il minor numero possibile di blocchi e di confrontare due soluzioni per efficienza.
- Introdurre i cicli (ripeti) e le condizioni (se tocca il muro) per scrivere una procedura più generale.
- Proporre la sfida del *wall follower* e la costruzione di un labirinto con divisione ricorsiva. **(estensione presente nel testo Techno logics)**

### L2
- Affiancare ai termini chiave (avanti, ruota, sprite, blocco, labirinto, traguardo) immagini e icone; sfruttare il fatto che i blocchi di Scratch sono visivi e colorati e che il programma può essere impostato in più lingue.
- Lavorare in coppia con un compagno tutor per la parte verbale del confronto. **(proposta progettuale)**

## Pagine collegate

- [[scratch]] — l'ambiente di programmazione a blocchi usato in questa attività
- [[coding-e-programmazione-a-blocchi]] — la logica dei blocchi che si trascinano e incastrano
- [[pensiero-computazionale]] — la cornice (astrazione, scomposizione, algoritmi) in cui si colloca l'attività
- [[algoritmo-e-diagrammi-di-flusso]] — il concetto di algoritmo e di sequenza di istruzioni
- [[debugging-come-strategia]] — il debug come strategia didattica per imparare dagli errori
- [[valutazione-coding-robotica]] — criteri e rubriche per valutare le attività di coding

## Fonti

- Techno logics - Laboratorio sperimentale STEAM (F. Furci, E. Pozzi, G. Monti), Raffaello Scuola, ISBN 9788847241206 (Attività 5 "Il topo nel labirinto", pp. 51-52; Attività 6 "Mettiti in salvo con il pensiero algoritmico", pp. 53-54; Attività 7 "Costruisci il tuo labirinto", pp. 54-55; glossario sprite/debug p. 47)
- Tecnologia (Pearson), ISBN 9788891561633 (descrizione dell'ambiente Scratch e dell'interfaccia, p. 435)
- nessuna fonte diretta per le sezioni di durata, organizzazione della classe, rubrica e adattamenti inclusivi: contenuti come proposta progettuale da validare
