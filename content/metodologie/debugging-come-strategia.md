---
tipo: metodologia
disciplina: tecnologia
ordine_scolastico: secondaria_primo_grado
competenze: [pensiero computazionale, competenza digitale]
stato: da_validare
fonti: [Techno logics - Laboratorio sperimentale STEAM, Guida Presente e Futuro (FabLab), Tecnologia (problem solving Lego)]
ultima_revisione: 2026-06-22
---

# Il debugging come strategia didattica

## Definizione breve

Il **debugging** è la fase della programmazione che consiste nel **rilevare gli errori (bug) inseriti nel codice e correggerli** (Techno logics - STEAM, p.48). Un *bug* è quindi un errore di codice: quando un programma non si comporta come ci si aspettava, si applica una **procedura di debugging, cioè di ricerca dell'errore** (Techno logics - STEAM, p.106).

Dal punto di vista didattico, il debugging non è solo un'operazione tecnica ma una **strategia di apprendimento**: trasforma l'errore da fallimento a informazione utile. Come ricorda un testo sul problem solving, "nel processo di problem solving anche l'errore può essere utile perché può servire a trovare soluzioni corrette escludendo via via quelle che risultano sbagliate" (Tecnologia - problem solving Lego, p.96). Usare il debugging come strategia significa insegnare agli studenti a leggere i propri errori, formulare ipotesi sulla causa e verificarle in modo sistematico.

## Quando ha senso usarla

Il debugging come strategia è particolarmente efficace quando:

- gli studenti programmano in ambienti a blocchi (Scratch, micro:bit, Tinkercad Circuits) o controllano robot e schede e **il risultato non corrisponde a quanto progettato** — è il momento naturale per fermarsi e indagare;
- si vuole sviluppare il **pensiero computazionale** e l'autonomia: anziché ricevere la soluzione corretta dal docente, lo studente impara a trovarla;
- si lavora con un **diagramma di flusso** o un algoritmo già scritto e bisogna confrontare il comportamento atteso con quello reale (Techno logics - STEAM, p.106);
- si vuole costruire un clima di classe in cui **"l'errore e lo sbaglio non coincidano con il fallimento"** (Guida Presente e Futuro - FabLab) e gli studenti si sentano liberi di sperimentare.

**(proposta progettuale)** È utile anche come momento trasversale: lo stesso atteggiamento (osservare, isolare, correggere) si applica a un disegno tecnico, a un esperimento o a un testo, rendendo il debugging una competenza spendibile oltre il coding.

## Come si struttura (fasi)

La procedura prende spunto dall'esempio reale del triangolo in Scratch (Techno logics - STEAM, p.106), dove il codice viene rivisto "passo passo, apportando eventualmente una modifica alla volta per circoscrivere l'errore a uno specifico blocco".

1. **Osservare il comportamento atteso vs. quello reale.** Si confronta ciò che il programma dovrebbe fare (descritto nell'algoritmo o nel diagramma di flusso) con ciò che effettivamente accade. *(esempio dal testo: "il triangolo non è stato disegnato come ce lo saremmo immaginato")*.
2. **Localizzare l'errore.** Si esamina meglio il punto critico: dove si manifesta il problema? Nell'esempio, "il problema si trova nella rotazione del gatto".
3. **Formulare un'ipotesi sulla causa.** Si prova a spiegare *perché* succede (es. l'angolo di rotazione impostato non corrisponde a quello geometrico richiesto).
4. **Modificare una cosa alla volta.** "Rivedi passo passo il codice, apportando eventualmente una modifica alla volta per circoscrivere l'errore a uno specifico blocco" (Techno logics - STEAM). Cambiare più cose insieme rende impossibile capire cosa ha funzionato.
5. **Riprovare e verificare.** Si esegue di nuovo il programma. Se l'errore persiste, si torna al punto 2. È un processo **ciclico**, come nel problem solving: "in caso di problemi, rivedere le procedure, ricercare l'errore e apportare le modifiche necessarie, fino a che il gioco rispetti le impostazioni stabilite all'inizio" (Tecnologia, p.96 e procedura Scratch).
6. **Usare gli strumenti di osservazione.** Con Arduino su Tinkercad Circuits il **Monitor seriale** permette di "visualizzare i dati letti dalla scheda, uno strumento davvero utile per il debug" (Techno logics - STEAM, p.79): guardare i valori reali aiuta a capire cosa non funziona.

## Esempio in classe

**Attività: il triangolo che non si chiude (Scratch)** — ripresa dall'esempio del libro.

- Gli studenti costruiscono il diagramma di flusso per disegnare un triangolo equilatero (tre lati uguali, angoli di 60°) e traducono i passi in blocchi Scratch.
- Premono "spazio": il triangolo non viene come previsto. Si crea il momento di debug.
- Il docente non corregge: invita a confrontare disegno atteso e disegno ottenuto (fase 1) e a indicare dove "qualcosa non torna" (fase 2: la rotazione).
- A coppie, gli studenti formulano l'ipotesi: il blocco "ruota di 60°" non produce l'angolo interno corretto. Provano a modificare **solo** quel blocco (fase 4) e rieseguono (fase 5).
- Si discute insieme: cosa avete cambiato? Perché ha funzionato?

**Variante peer-debug (Techno logics - STEAM, p.48):** dopo aver scritto la sequenza di uno storyboard/programma, "controlla l'efficacia con un compagno o una compagna, verificando se è in grado di ripetere la sequenza dalla lettura delle tue istruzioni passo passo. Che cosa puoi migliorare?". Far eseguire il proprio codice a un compagno è un potente test degli errori.

## Ruolo del docente / degli studenti

**Docente:**
- Predispone situazioni in cui l'errore può emergere e **resiste alla tentazione di dare subito la soluzione**.
- Fa domande-guida ("Cosa ti aspettavi? Cosa è successo? Dove guarderesti per primo?") invece di indicare il blocco sbagliato.
- Dà "il giusto valore didattico all'errore, se supportato da un processo mentale che viene spiegato" (Guida Presente e Futuro - FabLab): valuta il ragionamento, non solo il risultato.
- Garantisce un clima in cui "l'errore e lo sbaglio non coincidano con il fallimento" (Guida Presente e Futuro - FabLab).

**Studenti:**
- Osservano, isolano, ipotizzano, modificano una cosa alla volta e verificano.
- Lavorano spesso in coppia o in piccolo gruppo (apprendimento cooperativo) testando il codice a vicenda.
- Documentano cosa hanno cambiato e perché, sviluppando metacognizione.

## Vantaggi e limiti

**Vantaggi**
- Sviluppa pensiero computazionale, autonomia e tolleranza alla frustrazione.
- Rende l'errore una risorsa di apprendimento, non un voto negativo.
- È trasferibile: la stessa logica vale per più discipline.
- Spinge a un metodo ordinato (una modifica alla volta) anziché a tentativi casuali.

**Limiti / attenzioni** **(proposta progettuale)**
- Senza guida può degenerare in "prova ed errore" caotico: serve la disciplina della modifica singola.
- Richiede tempo: non sempre compatibile con lezioni brevi.
- Può scoraggiare se l'errore è troppo complesso per il livello della classe: meglio graduare la difficoltà.
- Necessita di un clima di fiducia; in classi competitive l'errore esposto può creare imbarazzo.

## Adattamenti inclusivi

**(proposta progettuale, in coerenza con la cornice della Guida Presente e Futuro - FabLab)**

- **Coppie eterogenee / peer tutoring:** abbinare chi è più sicuro a chi ha più difficoltà nel test del codice (variante peer-debug).
- **Checklist visiva del debug:** una scheda con le 6 fasi in icone, da seguire passo passo, sostiene studenti con DSA o con difficoltà di pianificazione.
- **Errore come tappa attesa:** dichiarare in anticipo che "il programma quasi sempre non funziona la prima volta" abbassa l'ansia da prestazione.
- **Strumenti di osservazione concreti:** il Monitor seriale o l'esecuzione passo passo rendono visibile l'errore, utile per chi apprende meglio con supporti concreti.
- **Valutazione del processo:** valorizzare il ragionamento spiegato, non solo il codice corretto, in linea con il "giusto valore didattico all'errore".

## Pagine collegate

- [[pensiero-computazionale]]
- [[algoritmo-e-diagrammi-di-flusso]]
- [[coding-e-programmazione-a-blocchi]]
- [[scratch]]
- [[tinkering-e-making]]
- [[inclusione-coding-robotica]]

## Fonti

- Techno logics - Laboratorio sperimentale STEAM (Furci, Pozzi, Monti, Raffaello Scuola), box "Debug" p.48; attività peer-debug p.48; debug con Monitor seriale Tinkercad/Arduino p.79; esempio del triangolo e procedura di debugging p.106
- Guida Presente e Futuro - FabLab (Tubia, Rizzoli): il valore didattico dell'errore; "l'errore e lo sbaglio non coincidano con il fallimento"
- Tecnologia (problem solving con robot Lego): processo ciclico, "anche l'errore può essere utile", p.96; procedura "rivedere le procedure, ricercare l'errore" (Scratch)
- Alcuni contenuti su fasi operative, limiti e adattamenti inclusivi sono indicati come **(proposta progettuale)** da validare.
