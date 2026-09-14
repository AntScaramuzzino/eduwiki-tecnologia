---
title: "Argus, il robot che si muove in qualunque direzione"
tipo: fonte_sintetizzata
titolo_fonte: "Ecco Argus, il robot che si muove in qualunque direzione"
autore_fonte: Focus.it
url: https://www.focus.it/tecnologia/innovazione/ecco-argus-il-robot-che-si-muove-in-qualunque-direzione
data_pubblicazione: 2026-06-05
stato: da_validare
ultima_revisione: 2026-09-14
---

# Argus, il robot che si muove in qualunque direzione

**Fonte:** [Focus.it](https://www.focus.it/tecnologia/innovazione/ecco-argus-il-robot-che-si-muove-in-qualunque-direzione) — 05/06/2026
**Nota sul copyright:** sintesi originale scritta per il wiki, non riproduzione del testo dell'articolo. Per il testo integrale vedi il link.

## Di cosa parla

Argus è un robot sperimentale della Duke University con un corpo centrale a dodecaedro e **20 arti telescopici**, ciascuno con una videocamera in punta. Nasce da una domanda di progetto netta: un robot non deve per forza imitare un uomo o un animale: qual è allora la forma più efficiente per muoversi con la stessa facilità in ogni direzione (*isotropia dinamica*)? Il team ha simulato 1.500 design prima di costruire il prototipo. Nei test si è mosso su cemento, erba, vegetazione fitta, sabbia e superfici scivolose, superando ostacoli fino a circa 13 cm, continuando a funzionare con uno, due o tre arti disattivati e mantenendo quasi tutta la velocità con un carico laterale di circa 4,5 kg. Ma nei test reali di tracciamento e manipolazione le prestazioni sono crollate rispetto alle simulazioni, soprattutto per il surriscaldamento e la desincronizzazione delle videocamere di profondità.

## Punti chiave per la didattica

- **Il caso serve soprattutto a smontare un'idea implicita**: che un robot debba assomigliare a qualcosa di vivo. Domanda da porre in classe prima di mostrare l'immagine: "disegna un robot che deve muoversi ugualmente bene in tutte le direzioni". Poi si confronta con Argus. È un'attività di progettazione, non di ascolto.
- **La forma nasce dal requisito, non dall'estetica.** Dodecaedro e 20 arti non sono una scelta grafica: sono la conseguenza geometrica di "uguale in tutte le direzioni". Aggancio diretto a [[poligoni-regolari-e-curve]] e a [[struttura-modulare-e-disegno-geometrico]] — perché un solido regolare, e non una scatola?
- **1.500 simulazioni prima di costruire**: esempio concreto e comprensibile del ciclo di progettazione (ipotesi → simulazione → prototipo → test), che in [[robotica-educativa]] gli studenti percorrono in piccolo con mBot o micro:bit.
- **La ridondanza come scelta progettuale.** Funziona anche perdendo tre arti su venti: è il concetto di tolleranza al guasto, spiegabile senza formule e trasferibile a molti altri oggetti tecnici (un aereo, una rete elettrica).
- **Il divario simulazione/realtà è la parte più formativa.** Le videocamere si surriscaldano e si desincronizzano: un dettaglio banale, fisico, non previsto dal modello. Ottimo antidoto all'idea che "se funziona al computer funziona". Da usare esplicitamente quando gli studenti provano codice su un robot vero e non ottengono il comportamento simulato.
- Gli arti sono insieme **attuatori** (spingono) e supporti di **sensori** (le videocamere): esempio pulito della coppia di [[sensori-e-attuatori]] integrata in un unico organo.

## Concetto collegato

[[robotica-educativa]] · [[sensori-e-attuatori]] · [[struttura-modulare-e-disegno-geometrico]] · [[poligoni-regolari-e-curve]]

## Video di supporto

<figure>
<iframe src="https://www.youtube-nocookie.com/embed/nEq-BUaR3GQ" width="100%" style="aspect-ratio:16/9;border:none;border-radius:8px" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy" title="Webinar - Tinkering e robotica educativa. La robotica educativa per il curriculum scientifico"></iframe>
<figcaption>📺 Webinar - Tinkering e robotica educativa. La robotica educativa per il curriculum scientifico · Mondadori Education · <a href="https://www.youtube.com/watch?v=nEq-BUaR3GQ" target="_blank">Guarda su YouTube</a></figcaption>
</figure>

## Criticità

- **È un prototipo di ricerca, non un prodotto.** L'articolo lo dichiara e lo fa bene ("non è ancora pronto per andare sulla Luna"): il taglio va mantenuto anche in classe.
- **La pubblicazione scientifica di riferimento non è citata nell'articolo** e non è stata consultata per questa sintesi: tutti i numeri (1.500 simulazioni, 20 arti, 13 cm di ostacolo, 4,5 kg di carico) provengono dalla divulgazione, non dalla fonte primaria. Da riportare come dati **non verificati** presso l'originale.
- "Isotropia dinamica" è il termine usato nell'articolo; **la sua definizione tecnica esatta non è verificata** su fonte scientifica. In classe conviene usare la parafrasi ("muoversi ugualmente bene in tutte le direzioni") e non il termine come se fosse consolidato.
- Rischio di lettura spettacolare ("il robot alieno a venti braccia"): senza la domanda di progetto che lo precede, il caso diventa una curiosità e perde tutto il valore didattico.
