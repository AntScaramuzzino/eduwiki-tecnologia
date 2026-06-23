---
tipo: strumento_digitale
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Technologica Coding (DeA), Coding e Robotica (Paravia), MyTech Coding (Le Monnier)]
ultima_revisione: 2026-06-22
---

# Scratch

## Cos'è

Scratch è un linguaggio di programmazione a blocchi sviluppato dal gruppo di ricerca Lifelong Kindergarten del MIT Media Lab di Boston, guidato dal professor Mitchel Resnick. È pensato per avvicinare alla programmazione anche chi non ha esperienza: invece di digitare righe di codice, si trascinano e si incastrano blocchi colorati, come i mattoncini delle costruzioni.

Scratch è insieme un linguaggio di programmazione e un ambiente di sviluppo visuale: i blocchi sono già pronti e se ne può verificare subito il funzionamento, senza dover usare un compilatore o un editor di testo. La versione attuale è **Scratch 3.0**.

L'ambiente usa una metafora teatrale, utile per spiegarlo in classe:

- **Stage** (palcoscenico): l'area bianca dove "va in scena" il programma; può avere uno o più **sfondi** che cambiano in base a ciò che accade.
- **Sprite** (gli "attori", letteralmente "folletti"): gli oggetti grafici che si muovono sullo stage, come il celebre gattino, simbolo di Scratch. Ogni sprite può avere più **costumi** per cambiare aspetto.
- **Script** (il "copione"): la sequenza di blocchi che dice a ciascuno sprite cosa fare. Un programma può contenere più sprite e ognuno viene programmato singolarmente; anche lo stage può essere programmato.

I blocchi sono circa un centinaio, suddivisi in categorie ("famiglie") riconoscibili dal colore (Movimento, Aspetto, Suono, Situazioni/Eventi, Controllo e così via). Si trascinano dalla **tavolozza dei blocchi** all'**area degli script**, agganciandoli uno sopra l'altro.

## A cosa serve in classe

Scratch è uno strumento per rendere concreto e visibile il **pensiero computazionale**: permette di costruire storie interattive, giochi, animazioni, simulazioni e quiz, vedendo immediatamente l'effetto di ogni istruzione sullo stage.

In una progressione didattica per la secondaria di primo grado serve a:

- tradurre un algoritmo in una sequenza di blocchi eseguibile e osservabile;
- introdurre i concetti chiave della programmazione (sequenza, eventi, ripetizioni/cicli, condizioni, variabili) in forma visuale e graduale;
- collegare il coding a contenuti di altre discipline (matematica, geometria, narrazione, scienze) attraverso progetti;
- avviare al **debugging**: quando lo script non fa ciò che ci si aspetta, si individua e si corregge l'errore.

I concetti appresi con Scratch sono trasferibili a linguaggi di programmazione testuali più avanzati, e la sua logica a blocchi ha ispirato anche ambienti come Code.org.

## Come iniziare (setup minimo)

1. **Versione online (consigliata per iniziare).** Si lavora direttamente dal browser su `https://scratch.mit.edu`: si può creare subito un progetto, provarlo e ispirarsi agli esempi della comunità. Non serve installare nulla.
2. **Versione offline.** Si scarica e si installa l'editor da `https://scratch.mit.edu/download`, utile dove la connessione è instabile o assente. È gratuita.
3. **Lingua.** Se l'interfaccia appare in inglese, l'icona a forma di mappamondo (vicino al logo) consente di passare all'italiano.
4. **Account (facoltativo).** Iscriversi alla comunità serve solo per salvare i progetti online e condividerli; per le prime attività in classe non è indispensabile.
5. **Primo contatto.** Conviene partire con un nuovo progetto, far cliccare un singolo blocco (es. *fai 10 passi* della categoria Movimento) per vedere il gattino spostarsi, poi mostrare come agganciare più blocchi e come avviare lo script con il blocco *quando si clicca su (bandierina verde)*. La bandierina verde avvia, il pulsante rosso di stop ferma tutto.

**Requisiti minimi:** un computer (o tablet) con browser aggiornato e, per la versione online, connessione a internet. **(proposta progettuale)** In laboratorio è sufficiente una postazione ogni due studenti, per favorire il lavoro in coppia (pair programming).

## Esempi d'uso didattico

- **Primo script con dialoghi.** Lo sprite "dice" delle frasi tramite i fumetti del blocco *dire ... per 2 secondi* (categoria Aspetto): introduce sequenza ed esecuzione.
- **Reagire agli eventi.** Si collega lo script al blocco *quando si clicca sulla bandierina verde* e si aggiunge un secondo script attivato dalla pressione di un tasto (es. *quando si preme il tasto [spazio]*), per far ruotare o muovere lo sprite. Introduce il concetto di evento.
- **Il labirinto.** Si disegna un labirinto come sfondo dello stage e si programma uno sprite che lo percorre senza toccare i bordi, controllando direzione e collisioni: un classico per cicli, condizioni e coordinate. Vedi [[attivita-labirinto-scratch]].
- **Animazione e storytelling.** Più sprite con costumi diversi recitano un "copione", cambiando sfondo a seconda della scena.
- **Quiz interattivo.** Lo stage pone domande e usa variabili per tenere il punteggio: introduce input dell'utente e variabili.

**(proposta progettuale)** Una progressione efficace va dal singolo blocco eseguito a mano, allo script con evento, fino al mini-progetto con più sprite, alternando sempre momenti di previsione ("cosa farà questo script?") ed esecuzione.

## Costi / account / privacy

- **Costo:** Scratch è **gratuito**, sia nella versione online sia in quella offline.
- **Account:** non è necessario per usare l'editor; serve solo per salvare e condividere i progetti nella comunità online. **(proposta progettuale)** Per l'uso scolastico è disponibile **Scratch for Educators**, che consente di creare account-classe gestiti dal docente, riducendo la raccolta di dati personali degli alunni — da verificare e configurare prima dell'attività.
- **Privacy:** la pubblicazione di progetti avviene in un ambiente "social" pubblico. **(proposta progettuale)** In classe è prudente non usare nomi e dati reali degli studenti negli username, evitare di pubblicare progetti contenenti dati personali o foto, e preferire account gestiti dal docente. La condivisione pubblica andrebbe usata solo con il consenso delle famiglie. **(dato mancante — ipotesi:** policy e impostazioni vanno verificate sui termini ufficiali del sito al momento dell'uso.)

## Limiti e rischi educativi

- **Rischio "trascinare senza capire".** La facilità di incastrare blocchi può portare a procedere per tentativi casuali; va accompagnata da momenti di previsione e di spiegazione, perché resti pensiero computazionale e non semplice manipolazione.
- **Dispersione creativa.** L'ampia libreria di sprite, suoni e sfondi può distrarre dall'obiettivo dell'attività: meglio dare consegne chiare e vincoli.
- **Dipendenza dalla connessione** nella versione online; la versione offline risolve il problema ma va installata su ogni postazione.
- **(proposta progettuale)** Esposizione alla comunità online: i progetti pubblici e i commenti vanno mediati dal docente, soprattutto con preadolescenti.
- **Transfer da governare.** Il passaggio dai blocchi al codice testuale non è automatico: va progettato esplicitamente se è un obiettivo.

## Adattamenti inclusivi

- **Codice come linguaggio visivo:** la natura grafica dei blocchi, con colori e forme, aiuta studentesse e studenti con difficoltà nella lettura e nella scrittura, riducendo il carico legato al testo.
- **(proposta progettuale)** Predisporre script parzialmente montati ("incompleti") da completare, per chi ha bisogno di un punto di partenza guidato.
- **(proposta progettuale)** Lavoro in coppia con ruoli a rotazione (chi programma / chi verifica) per valorizzare la cooperazione e il tutoraggio tra pari.
- **(proposta progettuale)** Consegne a più livelli di difficoltà sullo stesso progetto (versione base e versione con sfide aggiuntive), per la differenziazione.
- **(proposta progettuale)** Schede passo-passo con immagini dei blocchi per chi necessita di istruzioni esplicite e sequenziali.
- Vedi [[inclusione-coding-robotica]] per principi e strumenti trasversali.

## Attività che lo usano

- [[attivita-labirinto-scratch]] — Il labirinto in Scratch
- [[uda-robotica-micro-bit]] — UDA in cui Scratch/programmazione a blocchi può fare da ponte verso la robotica **(proposta progettuale)**

## Pagine collegate

- [[coding-e-programmazione-a-blocchi]]
- [[pensiero-computazionale]]
- [[algoritmo-e-diagrammi-di-flusso]]
- [[debugging-come-strategia]]
- [[code-org-e-app-lab]]
- [[attivita-labirinto-scratch]]

## Fonti

- Technologica — Coding con Scratch (DeA Scuola, Corinna Romiti), pp.6, 11, 13-17
- Coding e Robotica (Paravia/Pearson, A. Barbero, F. Vaschetto), pp.21-22
- MyTech — Coding (Le Monnier/Mondadori, Brunetto, Bruno), sezione "Che cos'è e a cosa serve Scratch"
- Le sezioni "Costi/account/privacy", "Limiti e rischi", "Adattamenti inclusivi" e parte di "Come iniziare" contengono contenuti marcati come proposta progettuale da validare: non derivano direttamente dai testi.


## Micro-competenze collegate (ProfTecnologIA)

<div style="border:1.5px solid #3b82f633;border-radius:12px;padding:16px 20px;margin:12px 0;background:#fafafe;font-family:sans-serif">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
    <span style="background:#3b82f6;color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.5px">MC-DIG-2-01</span>
    <span style="color:#3b82f6;font-size:11px;font-weight:600">Digitale</span>
  </div>
  <strong style="font-size:15px;color:#0f172a">Coding con linguaggi a blocchi</strong>
  <p style="font-size:13px;color:#475569;margin:6px 0 10px">Lo studente sa programmare in Scratch (o linguaggio a blocchi equivalente) usando le strutture fondamentali (sequenza, selezione, ciclo, variabili), sa decomporre un problema in so…</p>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px"><span style="background:#6366f1;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">IN 2025</span><span style="background:#0ea5e9;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">DigComp 3.0</span><span style="background:#f59e0b;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">EntreComp</span><span style="background:#10b981;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">LifeComp</span><span style="background:#84cc16;color:#fff;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px">Agenda 2030</span></div>
  <svg viewBox="0 0 560 44" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:44px;border-radius:6px;overflow:hidden"><rect x="2" y="2" width="104" height="40" rx="6" fill="#3b82f6"/><text x="52" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">⚡ INNESCA</text><text x="108" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="114" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="164" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">📖 ESPLORA</text><text x="220" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="226" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="276" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔍 OSSERVA</text><text x="332" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="338" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="388" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🔬 SPERIMENTA</text><text x="444" y="27" text-anchor="middle" font-size="13" fill="#94a3b8">▶</text><rect x="450" y="2" width="104" height="40" rx="6" fill="#e2e8f0"/><text x="500" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">🌍 AGISCI</text></svg>
  <div style="margin-top:10px;font-size:12px;color:#64748b;border-top:1px solid #e2e8f0;padding-top:8px">
    <strong>Compito di realtà:</strong> Crea un quiz interattivo in Scratch sull'alimentazione: almeno 5 domande, punteggio, feedback per risposta corretta/sbagliata, schermata finale con il risultato…
  </div>
  <a href="https://proftecnologia.vercel.app/mc/MC-DIG-2-01/" target="_blank" style="display:inline-block;margin-top:10px;background:#3b82f6;color:#fff;padding:6px 14px;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none">
    Apri scheda completa →
  </a>
</div>
