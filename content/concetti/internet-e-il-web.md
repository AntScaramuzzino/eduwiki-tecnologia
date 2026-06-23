---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: []
stato: da_validare
fonti:
  - "NEXT (De Agostini)"
  - "Pianeta Tecnologia — Armaroli, Grosso, Mandrioli (Zanichelli)"
  - "Presente e Futuro — Castronovo et al. (Fabbri/Rizzoli)"
  - "Progettare il futuro — Conti (Minerva Scuola Mondadori)"
  - "Upgrade — Delpiano (Paravia/Pearson)"
  - "NEXT Guida docente (De Agostini)"
ultima_revisione: 2026-06-22
---

# Internet e il web

## Definizione breve

Internet è una rete mondiale di reti di computer che comunicano tra loro tramite un insieme di protocolli comuni (TCP/IP); il World Wide Web (WWW) è il principale servizio di Internet, formato da pagine multimediali collegate tra loro attraverso link ipertestuali.

---

## Spiegazione per docenti

Internet (da *Interconnected Networks*, reti collegate) è una rete distribuita di portata planetaria. La sua struttura fisica si basa su cavi elettrici e a fibra ottica che percorrono fondi oceanici, sottosuoli urbani e abitazioni, integrati da connessioni wireless (Wi-Fi, rete cellulare). Ogni dispositivo connesso è identificato da un **indirizzo IP** (*Internet Protocol*), una sequenza numerica univoca che permette ai pacchetti di dati di raggiungere la destinazione corretta.

Il traffico è smistato da dispositivi detti **router**, che instradano i pacchetti verso la destinazione, scegliendo tra percorsi alternativi: questa struttura a rete distribuita — in cui ogni nodo è collegato ad almeno altri due — garantisce la resilienza della rete anche in caso di guasto di un singolo nodo. L'accesso a Internet è mediato da un **provider** (ISP, *Internet Service Provider*), che possiede l'infrastruttura necessaria.

Il termine **protocollo** indica l'insieme di regole che governano lo scambio di dati tra due dispositivi; il protocollo di riferimento di Internet è **TCP/IP** (*Transmission Control Protocol / Internet Protocol*). I dati non viaggiano come blocchi unitari ma suddivisi in **pacchetti**, che possono seguire percorsi diversi e vengono riassemblati a destinazione (commutazione di pacchetto).

Il **World Wide Web** è il servizio Internet più noto e utilizzato. Nato nel 1991 al CERN di Ginevra grazie a Tim Berners-Lee, si basa sul protocollo **HTTP** (*HyperText Transfer Protocol*) e sul linguaggio **HTML** (*HyperText Markup Language*) per la struttura delle pagine. Un sito web è un insieme di pagine memorizzate su un **server web** e accessibili tramite un **browser**. Per semplificare la memorizzazione degli indirizzi, a ogni indirizzo IP è associato un nome di dominio (es. *wikipedia.org*), tradotto dai **DNS** (*Domain Name Server*).

La **banda larga** indica la capacità di trasmissione di una linea Internet; più è elevata, maggiore è la velocità di scambio dei dati. Il **divario digitale** (*digital divide*) descrive le disuguaglianze nell'accesso a Internet tra aree geografiche, classi sociali e generazioni.

Fonti primarie per questa sezione: NEXT p. 350–355; Pianeta Tecnologia pp. 405–408; Presente e Futuro pp. 388–391; Progettare il futuro p. 353; Upgrade p. 473.

---

## Spiegazione per studenti

**Cos'è Internet?**
Internet è una rete enorme che collega miliardi di computer, smartphone e altri dispositivi in tutto il mondo. La parola viene dall'inglese *Interconnected Networks*, cioè "reti collegate tra loro". L'idea è semplice: ogni dispositivo ha un indirizzo (l'**indirizzo IP**), proprio come ogni casa ha un numero civico, e i dati viaggiano attraverso cavi e onde radio da un indirizzo all'altro.

**Come funziona?**
Quando apri un'app o un sito, il tuo dispositivo invia una richiesta al router di casa tua (quel piccolo apparecchio con le antenne che probabilmente avete vicino al modem). Il router la consegna al provider — l'azienda che vi ha venduto la connessione — e da lì la richiesta percorre migliaia di chilometri di cavi fino al server dove si trova il contenuto. Il server risponde e la risposta torna indietro percorrendo lo stesso tipo di percorso. Tutto questo avviene in pochi secondi o meno.

**Cos'è il Web?**
Il **World Wide Web** (abbreviato WWW o semplicemente *web*) è il servizio Internet più usato: è l'insieme di tutte le pagine web collegate tra loro da **link** (collegamenti). Quando navighi, stai usando il web. Il web non è la stessa cosa di Internet: Internet è l'infrastruttura (i cavi, i dispositivi), il web è uno dei servizi che ci gira sopra — come la posta elettronica, i videogiochi online o lo streaming.

---

## Versione ultra-semplice (BES/DSA)

**Internet** = una rete gigante che collega tutti i computer del mondo.

**Indirizzo IP** = il numero del computer, come il numero di casa.

**Router** = l'apparecchio che smista i dati, come un vigile che dirige il traffico.

**Web** = le pagine e i siti che vedi nel browser (Chrome, Firefox, Safari...).

**Browser** = il programma che usi per "navigare" (aprire siti).

**Regola da ricordare:** Internet e Web non sono la stessa cosa. Internet è la rete; il Web è una delle cose che ci fai sopra.

---

## Esempio concreto in classe

**"Il viaggio di un messaggio"** — attività di simulazione narrativa (20 minuti).

Il docente assegna a gruppi di studenti i ruoli di: *mittente* (lo smartphone), *router di casa*, *provider*, *cavo sottomarino*, *server* (in un altro continente), *router di destinazione*, *destinatario*. Ogni gruppo riceve un cartellino con la descrizione del proprio ruolo.

Il docente "invia" un messaggio (una busta con un foglio) da un'estremità della classe all'altra: ogni gruppo legge il cartellino, "elabora" la busta e la passa al gruppo successivo, spiegando cosa fa il proprio componente.

Al termine la classe ricostruisce l'intero percorso su uno schema alla lavagna e risponde a: *Perché i dati arrivano in pochi secondi anche dall'altra parte del mondo?* e *Cosa succede se un router si rompe?*

Variante digitale: si usa il simulatore di rete Cisco Packet Tracer (versione gratuita per studenti) per visualizzare il percorso dei pacchetti. **(proposta progettuale)**

---

## Dal concetto all'attività

### Livello base

**"Mappa di Internet"** — Gli studenti, a coppie, costruiscono uno schema visivo con i componenti fondamentali di una connessione a Internet (dispositivo — router — provider — server — sito web) usando cartoncini colorati e frecce. Ogni componente è etichettato con una frase breve che ne descrive la funzione. Alla fine ogni coppia presenta il proprio schema alla classe.

Obiettivo: distinguere i componenti fisici di una connessione a Internet e descrivere il flusso dei dati.

### Livello intermedio

**"Internet vs. Web: caccia all'errore"** — Il docente prepara un testo con 5–6 affermazioni, alcune corrette e alcune errate (es. "Il Web è la stessa cosa di Internet", "Il browser è il programma che smista i dati", "L'indirizzo IP identifica il tuo dispositivo in rete"). Gli studenti, in piccoli gruppi, identificano gli errori, li correggono e motivano la correzione citando la spiegazione dal libro o dalla pagina wiki. Seguono confronto in plenaria.

Obiettivo: distinguere Internet, Web, browser, indirizzo IP, router; correggere misconcezioni frequenti.

### Livello avanzato

**"Dossier: il digital divide"** — Gli studenti, in gruppi, ricercano dati sul divario digitale in Italia (differenza Nord/Sud) e nel mondo (confronto con paesi in via di sviluppo), usando le informazioni del testo e, facoltativamente, una ricerca guidata online. Producono un breve dossier (1–2 pagine o una presentazione) che risponde a: *Perché l'accesso a Internet è considerato un diritto? Chi rimane escluso e con quali conseguenze?* Collegamento all'Agenda 2030, Obiettivo 9.

Obiettivo: collegare i concetti tecnici a questioni di equità e cittadinanza digitale; argomentare in forma scritta o orale. **(proposta progettuale nella parte di ricerca esterna)**

---

## Misconcezioni frequenti

| Misconcezione | Correzione |
|---|---|
| "Internet e il Web sono la stessa cosa." | Il Web è solo uno dei servizi di Internet. Internet è l'infrastruttura; il Web è un insieme di pagine accessibili tramite browser. |
| "Il router è il modem." | Sono due dispositivi distinti (anche se spesso integrati): il modem converte il segnale della linea telefonica/fibra in segnale digitale; il router smista i dati tra i dispositivi e la rete. |
| "I dati viaggiano 'nel cloud', quindi non esistono fisicamente." | I dati viaggiano fisicamente su cavi metallici e in fibra ottica, compresi cavi sottomarini che collegano i continenti. Il "cloud" è una metafora. |
| "Ogni sito web ha un solo indirizzo IP." | Un grande sito (es. Google, Wikipedia) usa centinaia di migliaia di server distribuiti nel mondo, ognuno con il proprio indirizzo IP. |
| "Il browser è lo stesso del motore di ricerca." | Il browser (Chrome, Firefox, Safari) è il programma per navigare; il motore di ricerca (Google, Bing) è un sito che aiuta a trovare altri siti. |
| "Più utenti usano Internet contemporaneamente, più la connessione rallenta per tutti." | La struttura distribuita di Internet permette percorsi multipli; la velocità dipende principalmente dall'infrastruttura locale e dalla banda del provider. |

---

## Collegamenti interdisciplinari

- **Matematica / Informatica:** sistemi di numerazione binaria e indirizzi IP; algoritmi di instradamento.
- **Scienze:** onde elettromagnetiche (Wi-Fi, rete cellulare); fibra ottica e velocità della luce.
- **Storia / Educazione civica:** origini di Internet (Arpanet, contesto Guerra Fredda); libertà di espressione online; diritto di accesso a Internet; Agenda 2030 Obiettivo 9.
- **Italiano / Media education:** linguaggio del web, ipertesti e lettura non lineare; fake news e verifica delle fonti.
- **Geografia:** mappe dei cavi sottomarini; divario digitale tra paesi sviluppati e in via di sviluppo.

---

## Strumenti digitali utili

- **Cisco Packet Tracer** (gratuito per studenti tramite registrazione su Cisco Networking Academy): simulatore di rete per visualizzare il percorso dei pacchetti. **(proposta progettuale)**
- **Wayback Machine** (archive.org): visualizza versioni storiche di siti web; utile per discutere l'evoluzione del Web.
- **Speedtest** (speedtest.net): misura la velocità della connessione a Internet della scuola; ottimo punto di partenza per discutere di banda larga.
- **Visual Subnet Calculator** o simulatori di indirizzi IP online: per esplorare in modo interattivo la struttura degli indirizzi IP. **(proposta progettuale)**
- **Google Maps / Submarine Cable Map** (submarinecablemap.com): mappa interattiva dei cavi sottomarini che connettono i continenti.

---

## Valutazione e rubriche

### Rubrica: Internet e il web

| Criterio | Livello 1 — Iniziale | Livello 2 — Base | Livello 3 — Intermedio | Livello 4 — Avanzato |
|---|---|---|---|---|
| **Comprensione dei concetti** | Non distingue Internet dal Web; non sa descrivere i componenti di una rete. | Distingue Internet dal Web in modo generico; conosce almeno due componenti (es. router, indirizzo IP). | Descrive correttamente il funzionamento di Internet (IP, router, pacchetti, provider) e del Web (HTTP, browser, server); usa la terminologia in modo sostanzialmente corretto. | Spiega con precisione tutti i componenti; usa correttamente la terminologia tecnica; collega i concetti tra loro in modo coerente (es. DNS, TCP/IP, banda larga). |
| **Applicazione** | Non riesce a riconoscere i componenti in uno schema o scenario. | Riconosce i componenti in uno schema già fornito, con qualche errore. | Costruisce autonomamente uno schema del percorso di un dato; individua e corregge misconcezioni. | Analizza situazioni nuove (es. perché la connessione è lenta? cosa succede se un router cade?) applicando correttamente i concetti. |
| **Collegamenti e pensiero critico** | Non collega il concetto a contesti più ampi. | Accenna a qualche implicazione (es. "Internet serve per comunicare"). | Collega Internet a temi di cittadinanza (digital divide, accesso come diritto) o ad altri saperi (scienze, storia). | Argomenta in modo articolato su implicazioni sociali, ambientali o etiche di Internet; produce riflessioni personali documentate. |
| **Comunicazione** | Espressione confusa; terminologia assente o molto scorretta. | Espressione comprensibile; usa almeno parte della terminologia corretta. | Si esprime in modo chiaro e organizzato; usa la terminologia tecnica in modo prevalentemente corretto. | Si esprime in modo preciso, organizzato e fluido; usa la terminologia tecnica con sicurezza; adatta il registro al contesto (spiegazione orale, testo scritto, schema). |

---

## Inclusione e adattamenti

**Studenti con DSA (dislessia, discalculia):**
- Fornire un glossario visivo con i termini chiave (massimo 8–10 voci) in formato carta o PDF accessibile, con definizione breve e icona o simbolo.
- Preferire schemi e mappe concettuali ai testi lineari per la spiegazione.
- Nelle verifiche, ammettere risposte brevi o a schema anziché testi estesi; consentire l'uso del glossario.
- La versione ultra-semplice di questa pagina è pensata come riferimento diretto.

**Studenti con difficoltà di comprensione (BES generici):**
- Usare l'analogia del servizio postale (mittente — corriere — destinatario) per spiegare il percorso dei dati.
- L'attività di simulazione narrativa "Il viaggio di un messaggio" è particolarmente indicata: coinvolge il corpo e la narrazione, riducendo il carico astratto.
- Ridurre il numero di termini tecnici da memorizzare nella fase iniziale; introdurre gradualmente router, IP, provider, server.

**Studenti con background linguistico diverso (alunni non italofoni):**
- I termini tecnici in inglese (router, browser, server, IP, Web) sono presenti in quasi tutte le lingue: usarli come ponte di accesso.
- Fornire, se possibile, un breve glossario bilingue.

**Studenti avanzati:**
- Approfondire il funzionamento del DNS, la struttura di un indirizzo IP (IPv4 vs IPv6), il concetto di cloud computing.
- Proporre la lettura di articoli di attualità sul digital divide o sulla governance di Internet e la produzione di un testo argomentativo.

---

## Fonti

- NEXT — Andrea Ferraresso, Enrico Colombini, Luca Scalzullo, Giuseppe Sardo (De Agostini) (p. 350–355)
- Pianeta Tecnologia — Armaroli, Grosso, Mandrioli (Zanichelli) (pp. 405–408)
- Presente e Futuro — Castronovo, Galli, Novembri, Pavolini (Fabbri/Rizzoli) (pp. 388–391)
- Progettare il futuro — Conti (Minerva Scuola Mondadori) (p. 353)
- Upgrade — Delpiano (Paravia/Pearson) (p. 473)
- NEXT Guida docente (De Agostini) — schede di verifica K9

> Nota: le sezioni "Esempio concreto in classe" (variante Cisco Packet Tracer), "Livello avanzato" (ricerca esterna) e "Strumenti digitali" (Cisco Packet Tracer, Visual Subnet Calculator) sono in parte **(proposta progettuale)** non direttamente tratte dai testi adottati.

---

## Pagine collegate

- [[la-comunicazione-elementi-e-modello]]
- [[analogico-e-digitale-il-segnale]]
- [[telefonia-e-telecomunicazioni]]
- [[social-network-e-cittadinanza-digitale]]
- [[attivita-riconoscere-le-fake-news]]
- [[uda-comunicazione-e-media]]


## Micro-competenze collegate (ProfTecnologIA)

<div style="border:1.5px solid #06b6d433;border-radius:12px;padding:16px 20px;margin:12px 0;background:#fafafe;font-family:sans-serif">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
    <span style="background:#06b6d4;color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.5px">MC-COM-3-05</span>
    <span style="color:#06b6d4;font-size:11px;font-weight:600">Comunicazione</span>
  </div>
  <strong style="font-size:15px;color:#0f172a">Reti globali, internet e infrastrutture</strong>
  <p style="font-size:13px;color:#475569;margin:6px 0 10px">Lo studente comprende internet come infrastruttura fisica e geopolitica globale: conosce i cavi sottomarini, i data center, il sistema DNS e i meccanismi di governance, e sa analiz…</p>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px"><span style="background:#6366f1;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">IN 2025</span><span style="background:#0ea5e9;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">DigComp 3.0</span><span style="background:#f59e0b;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">EntreComp</span><span style="background:#10b981;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">LifeComp</span><span style="background:#84cc16;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">Agenda 2030</span></div>
  <svg viewBox="0 0 560 44" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:44px;border-radius:6px;overflow:hidden"><rect x="2" y="2" width="104" height="40" rx="6" fill="#06b6d4"/><text x="52" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">⚡ INNESCA</text><text x="108" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="114" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="164" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">📖 ESPLORA</text><text x="220" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="226" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="276" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔍 OSSERVA</text><text x="332" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="338" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="388" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔬 SPERIMENTA</text><text x="444" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="450" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="500" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🌍 AGISCI</text></svg>
  <div style="margin-top:10px;font-size:12px;color:#64748b;border-top:1px solid #e2e8f0;padding-top:8px">
    <strong>Compito di realtà:</strong> Usando uno strumento di traceroute online (traceroute.org o simile), traccia il percorso di un pacchetto dati da Roma a tre destinazioni diverse (Tokyo, New Yor…
  </div>
  <a href="https://proftecnologia.vercel.app/mc/MC-COM-3-05/" target="_blank" style="display:inline-block;margin-top:10px;background:#06b6d4;color:#fff;padding:6px 14px;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none">
    Apri scheda completa →
  </a>
</div>
