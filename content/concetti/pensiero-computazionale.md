---
tipo: concetto
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Progettare il futuro (Conti), Tecnomondo (Pinotti), APP Scenari di Tecnologia (Pearson), Presente e Futuro (Castronovo)]
ultima_revisione: 2026-06-22
---

# Il pensiero computazionale

## Definizione breve

Il pensiero computazionale è il modo di ragionare che usiamo per risolvere un problema in modo che anche una macchina possa eseguirlo: si scompone il problema in parti più semplici, si individua ciò che conta davvero e si descrive la soluzione come una sequenza precisa di istruzioni (un algoritmo). Non riguarda solo i computer: è una competenza logica e di problem solving utile in qualsiasi attività.

## Spiegazione per docenti

Nei libri di testo di tecnologia il pensiero computazionale viene presentato come il "lato scientifico-culturale dell'informatica", cioè una competenza che aiuta a "sviluppare competenze logiche e capacità di risolvere problemi in modo creativo ed efficiente", qualità ritenute importanti per tutti i futuri cittadini (Tecnomondo, Pinotti). Il coding è descritto come il modo più semplice e divertente per svilupparlo, ma l'obiettivo dichiarato non è formare "tanti piccoli informatici", bensì stimolare "l'applicazione della logica per affrontare problemi complessi, trovare e applicare delle soluzioni" (APP Scenari di Tecnologia, Pearson).

I testi convergono su alcuni "concetti fondamentali del pensiero computazionale" (Progettare il futuro, Conti):
1. scomporre domande e problemi in tanti piccoli eventi semplici (decomposizione);
2. creare modelli che si possano riutilizzare (riconoscimento di schemi / generalizzazione);
3. astrarre un problema reale per riportarlo nel mondo del computer (astrazione);
4. elaborare un algoritmo, cioè un procedimento verificato di istruzioni eseguibile senza errori.

Lo stesso testo sottolinea l'abilità chiave di "astrarre e ridurre qualunque problema complesso della vita reale in una serie ben definita, rigorosa e semplificata di piccole istruzioni" che la macchina possa eseguire rispondendo con sì o no.

Tra gli effetti formativi attesi, i manuali elencano: maturare un pensiero progettuale, superare le complessità scomponendole in unità più semplici, pianificare e ottimizzare le azioni, sviluppare un'idea, cercare i bug con un continuo processo di autocorrezione, e lavorare in gruppo (Progettare il futuro, Conti).

Quattro pilastri di riferimento (sintesi diffusa, allineata ai testi citati):
- **decomposizione**: spezzare un problema grande in problemi piccoli;
- **riconoscimento di schemi**: notare ciò che si ripete e ciò che è simile;
- **astrazione**: tenere solo le informazioni essenziali, ignorare i dettagli inutili;
- **algoritmo**: scrivere i passi precisi della soluzione.

## Spiegazione per studenti

Immagina di dover spiegare a un robot come fare una cosa. Il robot è "un instancabile esecutore di comandi", ma capisce solo istruzioni "molto chiare, precise e semplici", a cui si può rispondere con sì o no, acceso o spento (Progettare il futuro, Conti).

Per riuscirci usi quattro mosse:
1. **Scomponi** il problema in pezzi piccoli (es. "preparare la colazione" = scaldare il latte + versarlo + prendere i biscotti).
2. **Cerca le ripetizioni**: quali passi si fanno sempre uguali?
3. **Tieni solo l'essenziale**: per dire al robot di versare il latte non gli serve sapere il colore della tazza.
4. **Scrivi l'algoritmo**: l'elenco ordinato dei passi, uno dopo l'altro.

Questo è il pensiero computazionale. Lo usi anche senza computer: quando organizzi lo zaino, quando spieghi a un amico la strada di casa, quando segui una ricetta.

## Versione ultra-semplice (BES/DSA)

Pensiero computazionale = pensare per piccoli passi chiari.

- Problema grande -> lo divido in pezzi piccoli.
- Scrivo i passi in ordine: prima, poi, infine.
- Ogni passo deve essere facile e preciso, come parlare a un robot.
- Se qualcosa non funziona, cerco l'errore e lo correggo. Sbagliare e correggere fa parte del gioco.

Esempio: per lavarsi le mani -> 1) apro l'acqua, 2) prendo il sapone, 3) strofino, 4) sciacquo, 5) chiudo l'acqua.

## Esempio concreto in classe

Dai libri di testo (Progettare il futuro, Conti, p.18). Il coniglio Rabbit vuole che il robot Miky gli versi il latte nella tazza ogni mattina.

- **Codice errato:** "Miky versa il latte." Risultato: il latte trabocca, perché l'istruzione è troppo vaga.
- **Codice corretto:**
  1. Miky controlla la tazza: è piena? No.
  2. Allora versa il latte per 1 secondo.
  3. Controlla di nuovo: è piena? No.
  4. Versa per 1 secondo.
  5. Controlla: è piena? Sì.
  6. Allora si ferma.

In classe: si fa "eseguire" l'algoritmo agli studenti a turno (uno fa il robot, gli altri danno i comandi). Si scopre così che servono un controllo (la tazza è piena?), una ripetizione (versa finché non è piena) e una condizione (sì/no). Sono le strutture base che ritroveranno in Scratch.

## Dal concetto all'attività

### Livello base
Coding unplugged (senza computer). Attività "il robot umano": uno studente è il robot, gli altri scrivono su biglietti le istruzioni per fargli attraversare l'aula evitando gli ostacoli (avanti 1, gira a destra, avanti 2...). Si introducono decomposizione e sequenza. Tempo: 1 ora. **(proposta progettuale)**

### Livello intermedio
In Scratch si realizza un breve programma in cui uno sprite si muove seguendo una sequenza di blocchi, con almeno una ripetizione (ciclo) e una condizione (se... allora). Si parte dalla scomposizione del comportamento desiderato in passi. Collegamento: [[scratch]], [[coding-e-programmazione-a-blocchi]].

### Livello avanzato
Progetto su micro:bit o mBot in cui il problema reale (es. far seguire una linea al robot, far accendere un semaforo) viene scomposto, astratto e tradotto in algoritmo con diagramma di flusso, poi programmato e testato con cicli di debugging. Collegamento: [[uda-robotica-micro-bit]], [[attivita-robot-percorso-mbot]].

## Misconcezioni frequenti

- **"Pensiero computazionale = saper usare il computer."** Falso: è un modo di ragionare; si può allenare anche senza dispositivi (coding unplugged).
- **"Pensiero computazionale = coding."** Il coding è uno strumento per svilupparlo, non la stessa cosa. I testi lo ribadiscono: l'obiettivo non è formare informatici (APP Scenari, Pearson).
- **"Più dettagli do, meglio è."** No: l'astrazione richiede di togliere i dettagli inutili e tenere l'essenziale.
- **"Se sbaglio ho fallito."** L'errore (bug) fa parte del metodo: si cerca e si corregge ("continuo processo di autocorrezione", Conti).
- **"Il computer capisce quello che intendo."** No: esegue solo istruzioni precise e univoche (vedi esempio di Miky).

## Collegamenti interdisciplinari

- **Matematica:** logica, sequenze, condizioni, problem solving, coordinate.
- **Italiano:** scrivere istruzioni chiare e ordinate; testo regolativo.
- **Educazione civica / cittadinanza digitale:** comprendere "il digitale oltre la superficie", non essere solo consumatori ma progettisti (APP Scenari, Pearson).
- **Scienze:** procedure sperimentali, ipotesi e verifica.
- **Arte e tecnologia:** progettazione, tinkering e making. Collegamento: [[tinkering-e-making]].

## Strumenti digitali utili

- [[scratch]] — programmazione visuale a blocchi, gratuito, nato al MIT; il più diffuso per i ragazzi.
- [[code-org-e-app-lab]] — percorsi guidati tipo "Ora del codice".
- [[micro-bit]] — scheda programmabile per progetti fisici.
- [[mbot]] — robot didattico per attività di percorso e sensori.
- Coding unplugged per chi non ha dotazione tecnologica. Collegamento: [[coding-unplugged]].

## Valutazione e rubriche

Rubrica di osservazione del pensiero computazionale **(proposta progettuale da validare)**:

| Dimensione | Iniziale | Base | Intermedio | Avanzato |
|---|---|---|---|---|
| Decomposizione | Affronta il problema in blocco, senza scomporlo | Scompone con aiuto in pochi passi | Scompone in modo autonomo in passi gestibili | Scompone in sotto-problemi e li ordina con efficienza |
| Astrazione | Si perde nei dettagli irrilevanti | Distingue alcune informazioni utili | Tiene l'essenziale nella maggior parte dei casi | Generalizza e crea modelli riutilizzabili |
| Algoritmo | Istruzioni vaghe o disordinate | Sequenza corretta in casi semplici | Usa sequenza, ripetizioni e condizioni | Algoritmo efficiente, con controlli e casi limite |
| Debugging | Si blocca davanti all'errore | Trova l'errore con aiuto | Individua e corregge l'errore in autonomia | Previene gli errori e ottimizza la soluzione |

Collegamento: [[valutazione-coding-robotica]], [[debugging-come-strategia]].

## Inclusione e adattamenti

- Privilegiare attività **unplugged** e concrete (corpo, oggetti) prima del digitale: rendono visibile il ragionamento e abbassano il carico cognitivo.
- Fornire le istruzioni anche con **icone/colori** (in Scratch i blocchi sono già colorati per area).
- Lavorare in **coppie o piccoli gruppi**: i testi valorizzano il lavorare in team e il confrontarsi.
- Scomporre i compiti in **passi brevi** con checklist visiva per studenti DSA/BES.
- Valorizzare l'errore come parte del percorso, riducendo l'ansia da prestazione.
- Tempi flessibili e consegne graduate (livello base/intermedio/avanzato).

Collegamento: [[inclusione-coding-robotica]].

## Fonti

- Progettare il futuro (A. Conti), sezione Informatica e coding (pp.15-18)
- Tecnomondo (A. Pinotti), guida docenti (sezione coding e pensiero computazionale)
- APP Scenari di Tecnologia (Pearson), guida docenti (sezione coding/Scratch)
- Presente e Futuro (Castronovo e altri), sezione "Coding e pensiero computazionale"
- Le sezioni "Dal concetto all'attività" (livello base), rubrica e parte degli adattamenti per l'inclusione sono proposta progettuale da validare.

## Pagine collegate

- [[algoritmo-e-diagrammi-di-flusso]]
- [[coding-e-programmazione-a-blocchi]]
- [[coding-unplugged]]
- [[scratch]]
- [[debugging-come-strategia]]
- [[robotica-educativa]]
- [[intelligenza-artificiale-a-scuola]]
