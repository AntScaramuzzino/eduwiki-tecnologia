---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Tecnomedia DIGIT (Lattes), Tecnologia (De Agostini 9788805079292), Tecnologia (Mondadori 9788891561633), Presente e Futuro Fablab (Rizzoli), Techno logics (Raffaello)]
ultima_revisione: 2026-06-22
---

# Algoritmi e diagrammi di flusso

## Definizione breve

Un **algoritmo** è un insieme finito e preciso di istruzioni che, eseguite nell'ordine giusto, risolvono un problema o portano a termine un compito. Il **diagramma di flusso** (in inglese *flowchart*) è la rappresentazione grafica di un algoritmo: uno schema fatto di forme geometriche collegate, dove ogni forma corrisponde a un tipo di comando.

![Diagramma di flusso](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/LampFlowchart-it.svg/langit-330px-LampFlowchart-it.svg.png)
*📖 diagramma a blocchi usato per rappresentare il flusso di operazioni logiche, di algoritmi o di dati, attraverso l'uso di simboli grafici e forme geometriche interconnesse da linee/segmenti orientati/frecce · [Wikipedia](https://it.wikipedia.org/wiki/Diagramma_di_flusso) · CC BY-SA*
## Spiegazione per docenti

L'algoritmo è il ponte tra il pensiero computazionale e il coding: è il risultato della fase in cui la soluzione di un problema viene scritta "passo dopo passo", in una forma che possa essere eseguita da un sistema di calcolo. Nei testi di tecnologia per la secondaria di primo grado il concetto viene introdotto a partire da esempi quotidiani (la ricetta di cucina, le indicazioni stradali, il puzzle) per poi formalizzarsi.

Le quattro proprietà che definiscono un algoritmo corretto, ricorrenti nei manuali, sono:

- **Numero finito di passaggi**: l'algoritmo deve terminare. È formato da un numero finito di passaggi logici, ciascuno definito in modo chiaro.
- **Istruzioni non ambigue e quantitative**: ogni istruzione descrive esattamente l'operazione da eseguire, senza lasciare spazio a interpretazioni diverse ("versa esattamente 400 g di farina", non "versa un po' di farina").
- **Istruzioni elementari e ordine preciso**: i singoli passi sono semplici e vanno eseguiti in un ordine univoco; cambiare l'ordine può cambiare il risultato.
- **Indipendenza dall'esecutore**: lo stesso algoritmo, seguito da esecutori diversi (persone o macchine), deve portare sempre allo stesso risultato.

Tre elementi interagiscono sempre: il **problema** da risolvere, la **persona** che definisce la soluzione e il **sistema di calcolo** che la esegue. Il sistema di calcolo non "capisce" il significato di ciò che fa: esegue in successione i comandi che riceve, scelti da un insieme limitato di operazioni che sa svolgere.

Il diagramma di flusso rende immediatamente visibile la struttura dell'algoritmo e il flusso dei dati. Distinguere tra *avere un algoritmo* e *pensare in modo algoritmico* è importante: l'obiettivo didattico non è memorizzare i simboli, ma allenare la capacità di scomporre un problema in passi precisi.

## Spiegazione per studenti

Immagina di dover spiegare a un amico come preparare una torta. Non puoi dirgli solo "fai una torta": devi indicargli ogni passaggio, nell'ordine giusto, con quantità precise. Quell'elenco ordinato di istruzioni è un **algoritmo**.

Un algoritmo parte da alcuni dati di partenza (l'**input** — per la torta sono gli ingredienti), segue le istruzioni una dopo l'altra e arriva a un risultato finale (l'**output** — la torta pronta).

Perché funzioni sempre, un algoritmo deve avere alcune regole:

- ha un **numero limitato di passi** e prima o poi finisce;
- ogni istruzione è **chiara e precisa**, non si può capire in due modi diversi;
- i passi vanno fatti **nell'ordine giusto**;
- deve funzionare **per chiunque** lo esegua, anche per una macchina.

Quando disegni l'algoritmo invece di scriverlo a parole, ottieni un **diagramma di flusso**: usi forme diverse collegate da frecce. Le frecce ti dicono dove andare al passo dopo.

## Versione ultra-semplice (BES/DSA)

Un **algoritmo** è una lista di passi per fare una cosa. Come le istruzioni per montare un mobile o la ricetta di una torta.

Regole semplici:

1. I passi sono **in ordine**.
2. Ogni passo dice **una cosa sola e chiara**.
3. C'è un **inizio** e una **fine**.

Il **diagramma di flusso** è lo stesso elenco, ma **disegnato** con forme e frecce:

- **Ovale** = inizio e fine
- **Rettangolo** = fai un'azione
- **Rombo** = fai una domanda (sì / no)
- **Freccia** = vai al passo dopo

## Esempio concreto in classe

**Problema:** confrontare due numeri e dire qual è il più grande.

Algoritmo a parole:

1. Inizio
2. Leggi il primo numero (p1) e il secondo numero (p2)
3. p1 è maggiore di p2?
   - **Vero** → mostra p1
   - **Falso** → mostra p2
4. Fine

Lo stesso algoritmo come diagramma di flusso:

```
        ( inizio )
            |
      [ leggi p1, p2 ]
            |
        < p1 > p2 ? >
         /         \
     VERO           FALSO
       |              |
  [ mostra p1 ]  [ mostra p2 ]
         \          /
          ( fine )
```

Questo esempio, tratto dai manuali, è ideale perché contiene tutti i blocchi fondamentali (inizio/fine, input, controllo, output) e introduce in modo naturale la **selezione** (il rombo con la domanda).

I cinque blocchi del diagramma di flusso da presentare:

| Blocco | Forma | Cosa fa |
|---|---|---|
| Inizio / Fine | ovale | apre e chiude l'algoritmo |
| Ingresso/Uscita (input/output) | parallelogramma | legge i dati o mostra i risultati |
| Elaborazione | rettangolo | esegue un calcolo o un'azione |
| Controllo / test | rombo | verifica una condizione (vero/falso) |
| Freccia | linea con punta | indica l'ordine dei passi |

## Dal concetto all'attività

### Livello base
Coding unplugged. Gli studenti scrivono a parole l'algoritmo di un'azione quotidiana (lavarsi i denti, fare uno zaino, preparare un panino). In coppia, uno legge le istruzioni alla lettera e l'altro le esegue: si scoprono i passaggi ambigui o mancanti. Si introduce così l'idea di istruzione "non ambigua". **(proposta progettuale)**

### Livello intermedio
Si trasforma l'algoritmo a parole in un diagramma di flusso con i cinque blocchi, su carta o con uno strumento digitale. Si parte da problemi con una decisione (es. "se piove prendo l'ombrello, altrimenti no") per usare il blocco di controllo.

### Livello avanzato
Si traduce il diagramma di flusso in un programma a blocchi in Scratch o in codice per un robot, verificando che l'output corrisponda a quanto previsto. Si introducono iterazione (cicli) e selezioni annidate, e si testa l'algoritmo su casi diversi per controllare che resti valido (collegamento con il debugging). **(proposta progettuale)**

## Misconcezioni frequenti

- **"Algoritmo = computer."** No: un algoritmo è una procedura logica; una ricetta o le indicazioni stradali sono algoritmi senza alcun computer.
- **"Algoritmo e programma sono la stessa cosa."** L'algoritmo è la soluzione logica; il **programma** è la sua traduzione in un linguaggio di programmazione. Prima si pensa l'algoritmo, poi si scrive il codice.
- **"L'ordine dei passi non conta."** Conta moltissimo: cambiare l'ordine può cambiare o impedire il risultato.
- **"Istruzioni generiche vanno bene."** Un'istruzione ambigua ("aggiungi un po' di sale") fa fallire l'esecutore: serve precisione quantitativa.
- **"Il diagramma di flusso è solo un disegno decorativo."** È uno strumento di progettazione: rende visibile la struttura dell'algoritmo prima di programmare.
- **"Il rombo è un passaggio qualsiasi."** Il rombo è sempre una domanda con due (o più) uscite: vero/falso.

## Collegamenti interdisciplinari

- **Matematica:** sequenze di operazioni, procedure di calcolo, condizioni (maggiore/minore), insiemi (diagrammi di Eulero-Venn accanto ai diagrammi di flusso).
- **Italiano:** scrittura di istruzioni chiare e non ambigue; il testo regolativo (ricetta, istruzioni di montaggio).
- **Geografia/Educazione civica:** descrivere un percorso con istruzioni precise (svolta a destra, prosegui dritto).
- **Scienze:** procedura sperimentale come sequenza ordinata di passi ripetibili.
- **Arte e immagine:** linguaggio grafico e simbolico del diagramma di flusso. **(proposta progettuale)**

## Strumenti digitali utili

- **Carta e penna / lavagna:** per la prima formalizzazione, prima di qualsiasi software.
- **Scratch:** per tradurre l'algoritmo in programmazione a blocchi e vederlo "in azione".
- **Code.org / App Lab:** percorsi guidati su sequenze, cicli e condizioni.
- **Strumenti di diagrammi (es. draw.io, Lucidchart, lo strumento diagrammi di Google/Office):** per disegnare flowchart puliti. **(proposta progettuale)**
- **micro:bit, Arduino, mBot:** per eseguire l'algoritmo su un dispositivo fisico.

## Valutazione e rubriche

Rubrica per la progettazione di un algoritmo e del relativo diagramma di flusso (4 livelli). **(proposta progettuale)**

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Scomposizione del problema | Elenca azioni in modo disordinato | Individua i passi principali con aiuto | Scompone il problema in passi ordinati | Scompone in sotto-problemi e generalizza la soluzione |
| Chiarezza delle istruzioni | Istruzioni ambigue o incomplete | Alcune istruzioni precise, altre vaghe | Istruzioni per lo più chiare e non ambigue | Tutte le istruzioni precise, quantitative, eseguibili da chiunque |
| Uso del diagramma di flusso | Usa i simboli a caso | Usa i blocchi principali con qualche errore | Usa correttamente blocchi e frecce | Usa correttamente anche controlli e percorsi alternativi |
| Verifica e correzione | Non controlla il risultato | Si accorge degli errori se segnalati | Testa l'algoritmo e corregge gli errori | Testa su casi diversi e migliora l'algoritmo (debugging) |

## Inclusione e adattamenti

- Partire sempre da attività **unplugged** e da esempi corporei/quotidiani prima del digitale.
- Fornire i **simboli del diagramma di flusso già stampati** da ritagliare e incollare, per ridurre il carico grafico (utile per disgrafia). **(proposta progettuale)**
- Usare **colori e icone** costanti per ciascun blocco (ovale = verde inizio/fine, rombo = giallo domanda).
- Permettere la **descrizione orale** dell'algoritmo come alternativa allo scritto.
- Lavorare in **coppie eterogenee** (uno descrive, uno esegue) per valorizzare ruoli diversi.
- Ridurre il numero di passi per chi ne ha bisogno, mantenendo la struttura logica. **(proposta progettuale)**

## Fonti

- Tecnomedia DIGIT (Lattes, 9788869170874) — "Il concetto di algoritmo", "Scrivere un algoritmo", pp. 170-173
- Tecnologia (De Agostini, 9788805079292) — "Il pensiero computazionale", "I linguaggi di programmazione", pp. 349-351
- Tecnologia (Mondadori, 9788891561633) — "Algoritmi e diagrammi di flusso", "Il coding e le strutture di base", pp. 416 e segg.
- Presente e Futuro Fablab (Rizzoli, guida 9156088) — sezione Coding (algoritmo, diagramma di flusso, blocchi input/output)
- Techno logics (Raffaello, 9788847241206) — definizione di algoritmo e pensiero algoritmico

## Pagine collegate

- [[pensiero-computazionale]]
- [[coding-e-programmazione-a-blocchi]]
- [[coding-unplugged]]
- [[debugging-come-strategia]]
- [[scratch]]
- [[attivita-labirinto-scratch]]
