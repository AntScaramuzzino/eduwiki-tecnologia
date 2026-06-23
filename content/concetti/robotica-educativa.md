---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Upgrade Robotica - Delpiano, Coding e robotica - Barbero/Vaschetto, Technologica Coding - Romiti]
ultima_revisione: 2026-06-22
---

# La robotica educativa

## Definizione breve

La robotica educativa è l'uso di robot programmabili (come mBot o piccoli robot costruiti con micro:bit) come strumento per imparare. Più che costruire macchine, serve a sviluppare il **pensiero computazionale**: si scrive un programma, lo si carica nel robot, si osserva cosa fa e lo si corregge. Un robot è una macchina capace di "sentire" l'ambiente con i sensori, "decidere" tramite un programma e "agire" sul mondo con gli attuatori (motori, LED, cicalino).

## Spiegazione per docenti

La robotica educativa porta il coding fuori dallo schermo: il programma non muove più solo uno sprite, ma un oggetto fisico che si muove nello spazio reale. Questo passaggio rende immediatamente visibili gli errori (il robot va contro il muro) e trasforma il **debugging** in un'esperienza concreta e motivante.

I testi analizzati descrivono un robot reale a partire da tre blocchi funzionali:

- **Sensori (ingressi):** "come noi usiamo i cinque sensi per capire ciò che succede attorno a noi, anche un robot ha bisogno di sentire il mondo esterno". Esempi citati: sensore di luce, sensore a ultrasuoni per gli ostacoli, sensore di inseguimento linea, accelerometro, GPS.
- **Computer / programma (la "decisione"):** nei robot semplici "c'è di solito un microcontrollore, cioè un computer che sta in un unico chip". Il software "legge le informazioni dei sensori, le esamina e, in base a esse, sceglie quali comandi mandare agli attuatori". Concetto chiave da trasmettere: un robot "non capisce, può solo eseguire un programma".
- **Attuatori (uscite):** "per agire sul mondo esterno il robot deve mettere in pratica (attuare) le proprie decisioni"; gli attuatori meccanici sono di solito comandati da motori elettrici.

Lo strumento più documentato per la secondaria di I grado è **mBot** (ditta Makeblock): possiede una scheda programmabile mCore, una serie di sensori e due motori, e si programma con **mBlock**, un ambiente a blocchi molto simile a Scratch. Esiste anche il percorso con la scheda **micro:bit** ("Costruisci un robot con micro:bit"). La somiglianza con Scratch è il principale ponte didattico: chi sa programmare a blocchi può passare al robot senza imparare un nuovo linguaggio.

Da segnalare in classe anche il legame storico e culturale: le **tre leggi della robotica** di Asimov e la distinzione tra robot autonomo e dispositivo telecomandato ("un'auto che si guida da sola è un robot, mentre un'auto guidata da una persona non lo è: la differenza la fa il cervello, cioè il software").

## Spiegazione per studenti

Un robot è una macchina che fa tre cose, un po' come te:

1. **Sente** quello che ha intorno con i sensori (i suoi "sensi"): la luce, gli ostacoli davanti, una linea sul pavimento.
2. **Decide** cosa fare seguendo le istruzioni del programma che hai scritto tu.
3. **Agisce** muovendo i motori, accendendo i LED o facendo un suono con il cicalino.

Attenzione: il robot non è furbo. Non "capisce" niente, esegue solo gli ordini del tuo programma, uno dopo l'altro. Se sbaglia, l'errore è quasi sempre nelle istruzioni che gli hai dato, non nel robot. Con mBot scrivi il programma con blocchi colorati (come in Scratch), lo invii al robot e lo guardi muoversi davvero. Se va contro il muro, torni al codice, capisci cosa non va e lo aggiusti: questo si chiama debugging, ed è la parte più divertente.

## Versione ultra-semplice (BES/DSA)

Un robot fa 3 cose:

- **SENTE** con i sensori (occhi e orecchie del robot).
- **PENSA** seguendo il tuo programma.
- **FA** muovendo le ruote o accendendo le luci.

Il robot fa solo quello che gli dici tu. Se sbaglia, cambi il programma e riprovi. Va bene riprovare tante volte: serve proprio a quello.

## Esempio concreto in classe

**Il robot che segue la linea (mBot).** Sul pavimento si attacca una striscia di nastro scuro su fondo chiaro che forma un percorso. mBot ha sotto il **sensore di inseguimento linea**: il programma dice al robot "finché vedi la linea vai avanti; se la linea finisce a destra, gira a destra; se finisce a sinistra, gira a sinistra".

Gli studenti, divisi in coppie, costruiscono il programma a blocchi in mBlock, lo caricano e fanno partire il robot. Quasi mai funziona al primo colpo: il robot esce dal tracciato. La classe osserva, ipotizza la causa (la velocità è troppo alta? il controllo destra/sinistra è invertito?), modifica un blocco e riprova. In una lezione si vede l'intero ciclo programma → prova → errore → correzione, cioè il cuore del pensiero computazionale.

## Dal concetto all'attività

### Livello base
Coding unplugged e primo contatto con il robot. Si "programma" un compagno bendato che fa da robot (avanti, gira, fermati) per fargli raggiungere un oggetto: si capisce che servono istruzioni precise e ordinate. Poi si accende mBot e si fa un primo programma semplice: accendi i due LED di rosso per 2 secondi e poi spegnili (esempio presente nei testi). Obiettivo: capire il ciclo scrivi → invia → osserva.

### Livello intermedio
Si usano i sensori. Programmare mBot per **muoversi ed evitare gli ostacoli** usando il sensore a ultrasuoni (se trovi un ostacolo, fermati e gira), oppure per **seguire la linea**. Si introduce il blocco "se… allora…" come decisione del robot basata su ciò che il sensore rilegge. Lavoro a coppie con debugging guidato.

### Livello avanzato
Mini-progetto a squadre: il robot deve completare un percorso con più regole (segui la linea, ma se incontri un ostacolo fermati e suona il cicalino). Gli studenti scompongono il problema, scrivono il programma combinando più sensori e attuatori, documentano le versioni successive del codice e presentano alla classe scelte ed errori risolti. Variante: costruire un piccolo robot con micro:bit.

## Misconcezioni frequenti

- **"Il robot è intelligente / capisce."** No: "un robot non capisce, può solo eseguire un programma". Decide chi scrive il codice.
- **"Robotica = costruire automi complicati."** A scuola la robotica serve soprattutto a imparare a programmare e a ragionare; il robot è il mezzo, non il fine.
- **"Ogni cosa telecomandata è un robot."** Un dispositivo telecomandato dipende sempre da una persona; un vero robot svolge da solo almeno una parte del lavoro.
- **"Se il robot sbaglia, è rotto."** Quasi sempre l'errore è nel programma (bug), non nell'hardware: si corregge il codice.
- **"Un robot deve avere forma umana o braccia."** Un robot può essere fisso o mobile, senza braccia: anche un'auto che si guida da sola è un robot.

## Collegamenti interdisciplinari

- **Matematica:** angoli e gradi di rotazione, distanze, misure dei sensori, sequenze e cicli.
- **Scienze:** i sensi e i sensori (analogia corpo-robot), energia e alimentazione del robot, ultrasuoni ed eco (come i pipistrelli).
- **Italiano / Storia:** Asimov, le tre leggi della robotica, fantascienza; impatto dei robot sul lavoro e sulla società (rivoluzione industriale).
- **Educazione civica:** automazione e occupazione, robot in ambienti pericolosi (soccorso, esplorazione), responsabilità nell'uso dei robot. **(proposta progettuale)**
- **Arte/Tecnologia:** progettazione e costruzione del telaio, design del robot in base alla funzione.

## Strumenti digitali utili

- **mBot** con il software **mBlock** (programmazione a blocchi, ambiente simile a Scratch); collegamento PC-robot via chiavetta USB 2.4G.
- **micro:bit** come microcontrollore per costruire piccoli robot.
- **Scratch** come ambiente di base prima del passaggio al robot fisico.
- **Arduino** per percorsi avanzati su sensori e attuatori.
- Nastro adesivo scuro, ostacoli e cartoncini per costruire i percorsi (materiale unplugged a basso costo).

## Valutazione e rubriche

Valutare il processo (come si arriva alla soluzione) più del risultato finale. **(proposta progettuale)**

| Criterio | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Comprensione del funzionamento del robot (sensori/programma/attuatori) | Confonde i ruoli, pensa che il robot "decida da sé" | Riconosce sensori e motori con aiuto | Spiega il ciclo sente-decide-agisce | Spiega il ciclo e lo applica a robot diversi |
| Costruzione del programma a blocchi | Copia il codice senza capirlo | Compone una sequenza semplice | Usa correttamente blocchi condizionali e sensori | Combina più sensori/attuatori in autonomia |
| Debugging | Si blocca all'errore | Individua l'errore con aiuto | Isola e corregge il bug per tentativi mirati | Spiega causa dell'errore e previene casi simili |
| Collaborazione e documentazione | Lavora isolato, non documenta | Partecipa, annota poco | Collabora e tiene traccia delle versioni | Coordina la coppia e documenta scelte ed errori |

## Inclusione e adattamenti

- **Ruoli a coppie:** chi programma e chi gestisce/osserva il robot, a rotazione, così tutti partecipano. **(proposta progettuale)**
- **Per DSA:** blocchi colorati e icone riducono il carico di lettura/scrittura; fornire una "palette" dei blocchi essenziali già pronta. **(proposta progettuale)**
- **Multisensorialità:** il robot dà feedback visivo (LED), sonoro (cicalino) e di movimento, utile per diversi stili di apprendimento.
- **Unplugged come rampa di accesso:** il gioco del "compagno-robot" prepara al coding senza tecnologia e include chi è meno a suo agio con il computer.
- **Gradualità:** partire da programmi brevissimi (accendi un LED) e aumentare un passo alla volta, valorizzando ogni tentativo. **(proposta progettuale)**

## Fonti

- Upgrade. Tecnologia al futuro - Delpiano (volume Robotica) (p.62-87, mBot, mBlock, sensore inseguimento linea, micro:bit)
- Coding e robotica - Barbero, Vaschetto (struttura coding + robotica con mBot e micro:bit)
- Technologica - Romiti (volume Coding) (p.82-88, robot/automi/androidi, tre leggi di Asimov, sensori, attuatori, microcontrollore, AI)
- Parti su metodologia, rubrica e adattamenti inclusivi: contenuti come proposta progettuale da validare

## Pagine collegate

- [[pensiero-computazionale]]
- [[coding-e-programmazione-a-blocchi]]
- [[sensori-e-attuatori]]
- [[mbot]]
- [[micro-bit]]
- [[debugging-come-strategia]]


## Micro-competenze collegate (ProfTecnologIA)

<div style="border:1.5px solid #3b82f633;border-radius:12px;padding:16px 20px;margin:12px 0;background:#fafafe;font-family:sans-serif">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
    <span style="background:#3b82f6;color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.5px">MC-DIG-3-01</span>
    <span style="color:#3b82f6;font-size:11px;font-weight:600">Digitale</span>
  </div>
  <strong style="font-size:15px;color:#0f172a">Robotica educativa e pensiero computazionale avanzato</strong>
  <p style="font-size:13px;color:#475569;margin:6px 0 10px">Lo studente sa programmare robot educativi (micro:bit, mBot, EV3 o equivalenti) usando strutture avanzate (funzioni, parametri, gestione eventi multipli), sa decomporre problemi co…</p>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px"><span style="background:#6366f1;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">IN 2025</span><span style="background:#0ea5e9;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">DigComp 3.0</span><span style="background:#f59e0b;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">EntreComp</span><span style="background:#10b981;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">LifeComp</span><span style="background:#84cc16;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">Agenda 2030</span></div>
  <svg viewBox="0 0 560 44" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:44px;border-radius:6px;overflow:hidden"><rect x="2" y="2" width="104" height="40" rx="6" fill="#3b82f6"/><text x="52" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">⚡ INNESCA</text><text x="108" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="114" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="164" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">📖 ESPLORA</text><text x="220" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="226" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="276" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔍 OSSERVA</text><text x="332" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="338" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="388" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔬 SPERIMENTA</text><text x="444" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="450" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="500" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🌍 AGISCI</text></svg>
  <div style="margin-top:10px;font-size:12px;color:#64748b;border-top:1px solid #e2e8f0;padding-top:8px">
    <strong>Compito di realtà:</strong> Progetta un robot che risolve un problema reale della scuola (es. misura il livello di rumore in corridoio, indica la disponibilità di posti in mensa, guida chi…
  </div>
  <a href="https://proftecnologia.vercel.app/mc/MC-DIG-3-01/" target="_blank" style="display:inline-block;margin-top:10px;background:#3b82f6;color:#fff;padding:6px 14px;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none">
    Apri scheda completa →
  </a>
</div>


## Risorse multimediali


[![▶ La robotica educativa e il pensiero computazionale](https://img.youtube.com/vi/pzg1-UpMypA/hqdefault.jpg)](https://www.youtube.com/watch?v=pzg1-UpMypA)
*📺 La robotica educativa e il pensiero computazionale · YouTube EDU*
