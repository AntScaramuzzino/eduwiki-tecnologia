---
title: "Come si controlla cosa scorre in rete"
tipo: fonte_sintetizzata
titolo_fonte: "Come si controlla cosa scorre in rete"
autore_fonte: Focus.it
url: https://www.focus.it/tecnologia/innovazione/come-si-controlla-cosa-scorre-in-rete
data_pubblicazione: 2026-07-12
stato: da_validare
ultima_revisione: 2026-09-28
---

# Come si controlla cosa scorre in rete

**Fonte:** [Focus.it](https://www.focus.it/tecnologia/innovazione/come-si-controlla-cosa-scorre-in-rete) — 12/07/2026
**Nota sul copyright:** sintesi originale scritta per il wiki, non riproduzione del testo dell'articolo. Per il testo integrale vedi il link.

## Di cosa parla

Focus.it affronta un problema tecnico poco noto: per difendere una rete bisogna **vedere cosa vi scorre dentro**, in tempo reale e senza rallentarla. L'articolo distingue due modi di osservare il traffico: l'analisi **fuori banda** (uno strumento riceve una copia dei dati e la studia, senza poter intervenire) e quella **in linea** (lo strumento sta sul percorso e può bloccare un attacco, ma se si guasta rischia di fermare tutto, da cui i sistemi di bypass). Il passaggio più didattico è la metafora della **busta e della lettera**: con il protocollo HTTPS, ormai usato da oltre l'80% delle connessioni, il contenuto viaggia cifrato e non è leggibile, ma restano visibili indirizzi IP, porte, dimensione e ritmo dei pacchetti e, all'avvio, il nome del sito cercato. Molti attacchi si riconoscono proprio da questi segnali, senza aprire i contenuti. L'esempio italiano è la piattaforma contro lo streaming sportivo pirata, che blocca per indirizzo e non per contenuto, con il rischio di colpire anche risorse legittime. Chiudono l'articolo i dati del Rapporto Clusit sugli attacchi gravi in Italia e la presentazione dei prodotti di un'azienda italiana del settore.

## Punti chiave per la didattica

- La metafora **"si guarda la busta, non la lettera"** è perfetta per spiegare a ragazzi di 12 anni che cosa fa la cifratura: il postino sa a chi è indirizzata la lettera e quanto pesa, ma non ne legge il contenuto. Si collega direttamente a [[internet-e-il-web]] (pacchetti, indirizzi IP, protocolli).
- Il lucchetto di HTTPS nel browser diventa un oggetto da osservare: attività breve in cui gli studenti controllano quali siti che usano mostrano il lucchetto e discutono che cosa protegge e che cosa no (il nome del sito resta spesso visibile).
- La distinzione **osservare / intervenire** (fuori banda vs. in linea) è un buon esempio di scelta progettuale con vantaggi e rischi: più controllo significa anche più punti in cui qualcosa può rompersi.
- Il caso del blocco dello streaming pirata mostra un **effetto collaterale tecnico**: se si blocca un indirizzo, si blocca tutto ciò che sta dietro, anche ciò che è legale. Spunto su tecnologia e regole, collegato a [[social-network-e-cittadinanza-digitale]].
- Il video collegato riporta il tema sul piano personale: su una rete Wi-Fi pubblica, chi gestisce la rete è proprio chi "vede le buste".

## Concetto collegato

[[internet-e-il-web]] · [[telefonia-e-telecomunicazioni]] · [[social-network-e-cittadinanza-digitale]]

## Video di supporto

<figure>
<iframe src="https://www.youtube-nocookie.com/embed/njPXISDTodo" width="100%" style="aspect-ratio:16/9;border:none;border-radius:8px" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy" title="Come funziona davvero una rete Wi-Fi pubblica e come evitare i rischi che si corrono"></iframe>
<figcaption>📺 Come funziona davvero una rete Wi-Fi pubblica e come evitare i rischi che si corrono · Geopop · <a href="https://www.youtube.com/watch?v=njPXISDTodo" target="_blank">Guarda su YouTube</a></figcaption>
</figure>

## Criticità

- **L'ultima parte dell'articolo ha carattere promozionale**: presenta un'azienda italiana del settore e i suoi prodotti. Quella parte non è stata usata per la didattica e non va riportata in classe come informazione neutra.
- I dati del Rapporto Clusit (quota di attacchi gravi che colpiscono l'Italia) sono riportati dall'articolo e **non verificati** in questa sede; il confronto con il peso dell'Italia sul PIL mondiale è un'interpretazione della fonte.
- Il testo usa molti termini tecnici (SNI, ECH, DDoS, DNS, network packet broker): per la scuola secondaria di primo grado conviene tenere solo la metafora della busta e i concetti di indirizzo e cifratura.
- La fonte non tratta la privacy dal punto di vista dell'utente (che cosa può sapere il gestore della rete di scuola o di casa): se se ne parla in classe va segnalato come **proposta progettuale**, non come contenuto della fonte.
