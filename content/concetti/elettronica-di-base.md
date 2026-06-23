---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: []
stato: da_validare
fonti: [Pianeta tecnologia (Zanichelli), MyTech Edizione Green, Upgrade Tecnologia al futuro (Pearson), Tecnomedia DIGIT (Lattes), Come funziona la tecnologia]
ultima_revisione: 2026-06-22
---

# Elettronica di base: componenti e segnali

## Definizione breve

L'elettronica studia il moto degli elettroni all'interno di mezzi solidi o nel vuoto e impara a "guidarlo" e a "leggerlo" per gestire ed elaborare informazioni e controllare macchinari. Un **circuito elettronico** è composto da un supporto — il **PCB** (*Printed Circuit Board*, in italiano circuito stampato) — su cui vengono saldati i vari componenti collegati tra loro mediante piste metalliche. I componenti si dividono in **passivi** (restituiscono al circuito meno energia di quella ricevuta, dissipandone una parte sotto forma di calore: resistore, condensatore, induttore) e **attivi** (in grado di introdurre energia nel circuito, perché richiedono alimentazione esterna; il più diffuso è il **transistor**).

## Spiegazione per docenti

L'elettronica è il naturale passo successivo allo studio del circuito elettrico e della legge di Ohm. Il concetto-chiave da far emergere è la distinzione tra **circuito elettrico** (trasporta energia a un carico: lampadina, motore, resistenza scaldante) e **circuito elettronico** (manipola informazioni e segnali).

**I componenti fondamentali, così come li descrivono i libri di testo adottati nella secondaria di primo grado:**

- **Resistore**: limita la corrente che scorre nel circuito, dissipando energia sotto forma di calore. Si misura in ohm (Ω). Presente in quasi ogni circuito per proteggere gli altri componenti.
- **Condensatore**: accumula e cede cariche elettriche in base alla sua capacità; si carica e si scarica molto rapidamente. **(proposta progettuale)** l'applicazione nei touchscreen non è trattata esplicitamente dai testi della secondaria di primo grado consultati, ma è un esempio efficace da usare in aula.
- **Induttore**: si oppone alle variazioni di corrente tramite un campo magnetico. **(proposta progettuale)** il legame con i motori elettrici è utile didatticamente ma va presentato come semplificazione.
- **Diodo**: un semiconduttore che permette alla corrente di attraversarlo in un solo verso. È la "valvola" unidirezionale del circuito. Il testo Pianeta tecnologia (Zanichelli) lo descrive: "Il diodo si lascia attraversare dalla corrente in una sola direzione."
- **LED** (*Light Emitting Diode*, diodo a emissione di luce): è un componente elettronico basato sulla proprietà di alcuni materiali semiconduttori di produrre fotoni (luce) se attraversati dalla corrente. La luce emessa dipende dal materiale semiconduttore: può essere rossa, gialla, verde, blu, bianca. Secondo MyTech Edizione Green (p. 311–312): il LED è formato principalmente da un materiale semiconduttore che può essere sottile fino a 0,5 micron; gli elettroni, quando il materiale è sottoposto a tensione, emettono energia sotto forma di radiazione luminosa. Nel 1962 Nick Holonyak realizzò il primo LED; nel 1993 fu inventato il LED a luce blu, che rese possibili i LED di ogni colore incluso il bianco — ricerca premiata con il Nobel per la fisica 2014. I LED hanno una durata fino a 80 000 ore, consumano molto meno delle lampade tradizionali e non contengono vapori di mercurio. Rispetto alle fonti di illuminazione tradizionali hanno un consumo ridotto del 93%.
- **Transistor**: il testo Upgrade Tecnologia al futuro (Pearson) lo descrive come "un piccolo dispositivo costruito con materiali semiconduttori come il silicio che può essere montato insieme ad altri transistor per costruire un circuito integrato". Svolge due funzioni principali: (1) **amplificatore** — rende disponibile in uscita un segnale con tensione e/o corrente maggiori rispetto all'ingresso; (2) **interruttore elettronico comandato** — lascia scorrere la corrente (on) o la blocca (off) a seconda di un segnale che riceve. Questa seconda proprietà è alla base dei dispositivi digitali: ogni transistor in stato on/off rappresenta un **bit** (1 oppure 0); 8 bit formano 1 byte. Il testo Pianeta tecnologia (Zanichelli) esplicita: "1 byte corrisponde a 8 transistor" e segnala che in una memoria moderna ci sono miliardi di transistor grandi pochi miliardesimi di metro.
- **Circuito integrato (chip o microchip)**: circuito di pochi millimetri formato da moltissimi componenti elettronici integrati insieme su una piastrina di silicio. Secondo il testo Tecno App Arduino (Lattes), su ogni piastrina "sono realizzate molte migliaia di componenti elementari, soprattutto transistori; il continuo progresso nel tempo dei circuiti integrati, sempre più complessi e veloci, è stato uno dei fattori chiave per lo sviluppo dei PC."

**Semiconduttori**: i libri di testo li introducono come materiali "che hanno insieme caratteristiche metalliche e non metalliche" (es. silicio, germanio, arseniuro di gallio), utilizzati nell'industria elettronica per la fabbricazione di transistor e circuiti integrati (Tecnomedia DIGIT, Lattes). Anche il silicio puro, se "drogato" con altri elementi, diventa semiconduttore: non è consigliabile approfondire la fisica del drogaggio a questo livello scolastico; è sufficiente far capire che diodi, LED e transistor *sono fatti* di materiali semiconduttori.

**Segnale analogico vs digitale**: un segnale è *analogico* quando può assumere infiniti valori continui (il suono, la luce, la temperatura); è *digitale* quando è espresso con valori discreti, in pratica solo 1 e 0. Il testo Pianeta tecnologia (Zanichelli) spiega il campionamento digitale parlando della DAB Radio: "un segnale digitale composto da una serie di 0 e 1 [è] associato a un segnale analogico mediante il campionamento, cioè misurando il segnale a intervalli regolari." Il transistor, con i suoi stati on/off, è il ponte fisico tra i due mondi.

**Kit di elettronica didattica**: il testo Pianeta tecnologia (Zanichelli) descrive esplicitamente i kit a componenti magnetici su mattoncini come strumenti per "imparare l'elettronica per tentativi ma in sicurezza, perché i componenti sono su mattoncini magnetizzati; i magneti si oppongono per esempio ai collegamenti con poli invertiti, cioè sbagliati." Le categorie funzionali dei mattoncini (alimentatori, ingressi, uscite, collegamenti) corrispondono esattamente alle parti di qualsiasi circuito elettronico.

## Spiegazione per studenti

Hai già visto il circuito elettrico: pila, fili, lampadina che si accende. L'elettronica fa un passo in più. Invece di limitarsi ad accendere una lampadina, usa piccoli componenti per "comandare" la corrente: rallentarla, accumularla, lasciarla passare solo in un verso, o usarla per accendere e spegnere altre cose.

Eccoli, uno per uno:

- Il **resistore** è come una strozzatura nel tubo: lascia passare meno corrente, così non "brucia" gli altri componenti. Si misura in ohm.
- Il **condensatore** accumula cariche elettriche e le rilascia quando serve, come una piccola batteria istantanea.
- Il **diodo** è una porta a senso unico: lascia passare la corrente in una direzione e la blocca nell'altra.
- Il **LED** (*Light Emitting Diode*) è un diodo speciale fatto di materiali semiconduttori. Quando la corrente lo attraversa nel verso giusto, emette luce. È dappertutto: telecomandi, lampade di casa, semafori, schermi dei telefoni. Dura molto più delle lampadine tradizionali e consuma molto meno.
- Il **transistor** è un mini-interruttore comandato da un segnale elettrico: può stare acceso (1) o spento (0). Dentro il processore di un telefono ne trovano posto miliardi — ognuno rappresenta un "1" o uno "0", ed è così che il computer scrive testi, foto, musica usando solo due cifre.
- Tanti transistor messi insieme formano un **microchip**, il "cervello" di smartphone, computer, ma anche di lavatrici e spazzolini elettrici.

Tutti questi componenti stanno saldati su una tavoletta di plastica con piste metalliche: il **circuito stampato** (PCB). Quelle schede verdi che vedi quando apri un vecchio apparecchio.

La corrente nei circuiti elettronici trasporta non solo energia, ma anche **informazioni** (segnali): suoni, immagini, dati. Un segnale può essere *analogico* (valori continui, come la voce umana) oppure *digitale* (solo 0 e 1, come i dati di un telefono).

## Versione ultra-semplice (BES/DSA)

L'elettronica usa piccoli componenti per controllare la corrente. Il **resistore** la frena. Il **diodo** la fa passare in un solo verso. Il **LED** è un diodo che fa luce. Il **transistor** è un interruttore on/off. Tanti transistor insieme formano un **microchip**, il cervello dei telefoni e dei computer. Tutti i pezzi stanno su una tavoletta: il **circuito stampato** (PCB).

## Esempio concreto in classe

Porta (o proietta la foto di) una **scheda elettronica recuperata** da un apparecchio rotto: un vecchio modem, una radiolina, un giocattolo elettronico, un caricabatterie aperto. Insieme alla classe si fa una "caccia ai componenti": si cercano i resistori (piccoli cilindri con fasce colorate), i condensatori (cilindretti o dischetti), i LED, i microchip neri rettangolari con le zampette, e si seguono le piste metalliche che li collegano.

Domanda guida: *perché questa scheda non è semplicemente una pila con una lampadina?* Risposta: perché qui la corrente non serve solo a illuminare, serve a trattare informazioni e segnali.

Se disponibile, usa un **kit di elettronica didattica a mattoncini magnetici** (il testo Pianeta tecnologia cita questi kit come strumenti di elettronica didattica sicuri per la scuola): si possono collegare alimentatore, pulsante e LED per un primo circuito, poi aggiungere un motore. I magneti impediscono i collegamenti sbagliati, eliminando il rischio di bruciare i componenti.

Variante: confronto diretto tra un circuito pila-lampadina e un circuito pila-resistore-LED su breadboard per evidenziare la differenza tra circuito elettrico ed elettronico, e per vedere che il LED si accende solo nel verso giusto (proprietà del diodo).

## Dal concetto all'attività

### Livello base

"Riconosci il componente": scheda guidata con immagini (anche dalla scheda recuperata in classe) e nomi da abbinare — resistore, condensatore, diodo/LED, transistor, microchip, circuito stampato. Per ciascuno una frase semplice sulla funzione ("frena la corrente", "porta a senso unico", "fa luce", "interruttore on/off", "cervello del telefono"). Pochi strumenti, molta osservazione. Prodotto: cartellone o scheda compilata. **(proposta progettuale)** la scheda dettagliata va costruita con le immagini dei componenti disponibili nel laboratorio scolastico.

### Livello intermedio

Costruzione di un **circuito con LED e resistore** su breadboard o con kit a clip senza saldatura: pila, resistore di protezione, LED. Si osserva che:
- il LED si accende solo se collegato nel verso giusto (proprietà del diodo);
- senza resistore di protezione il LED rischia di danneggiarsi.

Si possono provare LED di colori diversi e verificare che emettono colori diversi a seconda del materiale semiconduttore. Prodotto: circuito funzionante + breve relazione con schema disegnato. **(proposta progettuale)** i dettagli del setup dipendono dal kit disponibile in laboratorio.

### Livello avanzato

Compito autentico: **progettare un piccolo dispositivo a semplice automazione** con micro:bit o Arduino (es. un LED che si accende al buio con un sensore di luce, o un semaforo a tre LED). Gli studenti documentano lo schema, il codice a blocchi e spiegano il ruolo di transistor e microchip nel rendere "intelligente" il comportamento del circuito. Collega all'idea di segnale digitale (on/off → 1/0). Prodotto: prototipo + documentazione tecnica. Vedi [[sensori-e-attuatori]] e [[robotica-educativa]]. **(proposta progettuale)** l'attività è coerente con le indicazioni dei manuali (es. sezioni Arduino di Lattes e Tecno App) ma va adattata al kit e al programma.

## Misconcezioni frequenti

- **"Elettrico ed elettronico sono la stessa cosa."** No: un circuito elettrico trasporta energia a un carico (lampadina, motore); un circuito elettronico controlla ed elabora segnali con componenti dedicati.
- **"Il LED è una lampadina come le altre."** Il LED è un diodo: si accende solo se collegato nel verso giusto (il catodo al polo negativo, l'anodo al polo positivo) e ha bisogno di un resistore di protezione; una lampadina a filamento funziona in entrambi i versi e non ha questo vincolo.
- **"Il diodo lascia passare la corrente in tutte le direzioni."** No: questa è la sua caratteristica fondamentale — la corrente passa in un solo verso.
- **"Il transistor serve solo ad amplificare il suono."** L'amplificazione è solo una delle sue funzioni; nei dispositivi digitali lavora soprattutto come interruttore on/off, e ogni stato on/off rappresenta un bit.
- **"Digitale vuol dire solo più moderno."** Digitale significa rappresentare informazione con soli 0 e 1; questo ha vantaggi concreti (compattezza, conservazione, copia senza perdita di qualità), non è una semplice etichetta di modernità.
- **"Il microchip è un pezzo unico e solido."** È in realtà un insieme di milioni o miliardi di transistor microscopici su una piastrina di silicio.

## Collegamenti interdisciplinari

- **Matematica**: sistema di numerazione binario (base 2), ordini di grandezza (miliardi di transistor, miliardesimi di metro).
- **Scienze/Fisica**: corrente elettrica, conduttori e isolanti, semiconduttori (silicio), campo magnetico (induttore), luce ed emissione luminosa (LED, fotoni).
- **Educazione civica / Sostenibilità**: rifiuti elettronici (RAEE) e raccolta differenziata; i circuiti elettronici contengono materiali preziosi da recuperare (oro, argento, rame) e sostanze da smaltire correttamente.
- **Storia della tecnologia**: evoluzione dell'illuminazione (fuoco → incandescenza → fluorescente → LED) e dell'informatica (invenzione del transistor, riduzione di dimensioni, aumento di potenza).
- **Italiano**: lessico tecnico, descrizione di un processo, relazione di laboratorio.

## Strumenti digitali utili

- **micro:bit** e **Arduino**: per costruire piccoli circuiti programmabili con LED, sensori e attuatori. Citati esplicitamente dalle serie Tecnomedia DIGIT Arduino (Lattes) e Tecno App Arduino (Lattes) come ambienti di laboratorio per la scuola secondaria di primo grado.
- **Tinkercad Circuits** (simulatore online): permette di montare e simulare circuiti con LED, resistori, breadboard e Arduino senza componenti fisici — utile se il laboratorio non è disponibile. **(proposta progettuale)** da valutare rispetto agli strumenti già adottati dalla scuola.
- **Kit di elettronica didattica a mattoncini**: menzionati nel testo Pianeta tecnologia (Zanichelli) come "elettronica didattica" sicura per la scuola, con componenti magnetizzati che impediscono errori di polarità.
- Video e audiolibri dei testi adottati (es. sezioni Genially e video integrati nei manuali Lattes e Le Monnier) per ripasso accessibile.

## Valutazione e rubriche

Oggetto di valutazione: riconoscere i componenti e la loro funzione, distinguere circuito elettrico ed elettronico, comprendere il legame transistor–bit–digitale, montare o leggere un semplice circuito con LED.

| Indicatore | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Riconoscere i componenti e la loro funzione | Riconosce solo qualche componente, anche con aiuto, senza collegarlo alla funzione | Riconosce i componenti principali (resistore, diodo/LED, transistor) e ne indica la funzione base se guidato | Riconosce autonomamente i componenti e ne spiega la funzione con parole proprie | Riconosce e spiega tutti i componenti usando esempi concreti e lessico tecnico corretto |
| Distinguere circuito elettrico ed elettronico | Confonde i due tipi di circuito | Coglie la differenza solo con esempi forniti | Distingue i due tipi e porta un esempio per ciascuno | Distingue con sicurezza e argomenta perché un dispositivo "elabora segnali" e non solo "porta energia" |
| Capire il legame transistor–bit–digitale | Non collega transistor e codice binario | Sa che il transistor può stare on/off | Collega on/off a 1/0 e al concetto di bit | Spiega il passaggio bit → byte → microchip con esempi di grandezza |
| Realizzare o leggere un circuito con LED | Non completa il circuito nemmeno con guida | Completa il circuito con guida costante | Monta un circuito LED+resistore funzionante e ne disegna lo schema | Progetta una variante (più LED, sensore) e ne spiega le scelte |

## Inclusione e adattamenti

- **BES/DSA**: usa la *Versione ultra-semplice*; privilegia immagini, oggetti reali e manipolazione (componenti veri, kit a clip o kit magnetici senza saldatura). Schede con abbinamento immagine–nome–funzione invece di testi lunghi. Glossario illustrato dei termini chiave.
- **Lavoro a coppie o piccoli gruppi**: ruoli definiti (chi monta, chi disegna lo schema, chi descrive) per favorire partecipazione e cooperazione.
- **L2/lessico**: introdurre i termini tecnici con immagine e gesto; mantenere costante l'associazione parola–componente–funzione.
- **Plusdotati**: estensione al livello avanzato (micro:bit/Arduino, automazioni), oppure approfondimento storico (invenzione del transistor, LED blu e Nobel 2014, miniaturizzazione dei chip).
- **Sicurezza**: lavorare sempre a bassa tensione (pile, kit didattici a 3–5 V); non aprire mai apparecchi collegati alla rete elettrica. Vedi [[sicurezza-elettrica]].
- Adattamenti specifici al gruppo classe: **(proposta progettuale)**, da calibrare sulla situazione reale.

## Fonti

- Pianeta tecnologia (Zanichelli) — "L'elettronica" e "L'elettronica didattica" (pp. 363–365): definizione di elettronica, circuiti elettronici, PCB, componenti passivi e attivi, resistore, diodo, LED, transistor, circuito integrato, condensatore, induttore; transistor come interruttore on/off e legame con bit e byte; kit di elettronica didattica a mattoncini magnetici; segnale analogico vs digitale e campionamento (pp. 396–397).
- MyTech Edizione Green, Brunetto, Bruno (Le Monnier / Mondadori Education) — "Dentro l'oggetto: la lampadina a LED" (pp. 311–312): struttura del LED, materiale semiconduttore, emissione di fotoni, storia (Holonyak 1962, LED blu 1993, Nobel 2014), impronta ecologica dei LED; attività "accendi un LED con i limoni" (p. 312–313).
- Upgrade Tecnologia al futuro, Delpiano (Pearson/Paravia) — "Elettronica e robot" (p. 334): definizione di elettronica, transistor e circuiti integrati; LED come dispositivi a semiconduttore (p. 332).
- Tecnomedia DIGIT Arduino, Lattes — "I semiconduttori" (p. 97 circa, sezione materiali): silicio, germanio e arseniuro di gallio come semiconduttori usati per transistor e circuiti integrati; componenti elettronici delle macchine (p. 284): transistor e microcircuiti integrati che trasportano segnali elettrici.
- Tecno App Arduino, Lattes — "I circuiti elettronici" (p. 122 circa sezione informatica): circuiti integrati su piastrina di silicio, transistori elementari, evoluzione dei circuiti integrati, scheda madre; televisione digitale e fotodiodo (p. 108).
- Come funziona la tecnologia — silicio e circuiti integrati (p. 75): concentrazione di migliaia di componenti elettronici su piastrina di silicio; LED come semiconduttori per l'illuminazione (p. 214).
- Le sezioni "Dal concetto all'attività", "Strumenti digitali utili" e parte di "Inclusione" contengono **proposte progettuali** dell'estensore, non tratte letteralmente dai testi: vanno validate dal docente prima dell'uso in aula.

## Pagine collegate

- [[grandezze-elettriche-e-circuito]] — tensione, corrente, resistenza: le grandezze su cui poggia l'elettronica.
- [[legge-di-ohm]] — relazione V, I, R: alla base del dimensionamento del resistore di protezione per il LED.
- [[circuiti-in-serie-e-in-parallelo]] — come collegare i componenti in un circuito.
- [[effetti-della-corrente-elettrica]] — cosa fa la corrente (luminoso, termico, magnetico): il LED sfrutta l'effetto luminoso.
- [[sicurezza-elettrica]] — lavorare in sicurezza con la corrente, indispensabile per le attività di laboratorio.
- [[esperimenti-con-i-circuiti-elettrici]] — attività di laboratorio collegate.
