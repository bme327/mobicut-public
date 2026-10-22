---
title: Export
parent: Funkce
nav_order: 17
---

# Export hotového videa
{: .no_toc }

Export z tvých úprav vytvoří nové video. Originálu se nedotkne.

{: .important }
> **Export je velmi rychlý.** Video se vytváří v telefonu jeho vestavěným video hardwarem.
> Nic se nenahrává a smazané části se přeskakují.

1. TOC
{:toc}

---

## Export {#export}

1. Klepni na **Export** nahoře v editoru.
2. Nahoře v panelu zkontroluj délku a počet úseků a pak vyber:
   - **Resolution**: *Original*, nebo menší (1080p, 720p) pro menší soubor. Nabízejí se jen
     rozměry menší než originál.
   - **Frame rate**: *Original*, nebo *30 fps* (nabízí se u videí s 50/60 fps). 30 fps zmenší
     soubor a na sdílení to bohatě stačí.
   - **Text** (má-li projekt texty): *Burn into video* nebo *Off*. Grafika se vpálí vždy.
3. Klepni na **Export to gallery**.

Pokud některé spoje ještě nemají přechod, mobiCut se nejdřív zeptá, jestli je přidat; viz
[Přechody]({{ "/cs/operations/transitions/#when-you-export" | relative_url }}).

{% include screen.html name="export" alt="Panel Export s volbami rozlišení, snímkové frekvence a textů." %}

## Během exportu {#while-it-exports}

Ukazatel průběhu ukazuje, kolik je hotovo. **Nech mobiCut otevřený**, dokud export neskončí;
obrazovka zůstane zapnutá sama. **Cancel** export zastaví.

{% include screen.html name="export-progress" alt="Dialog Exporting… na 42 % s tlačítkem Cancel." %}

{: .note }
> Pokud telefon nezvládne kódovat původní nastavení (velmi vysoké rozlišení nebo snímkovou
> frekvenci), export automaticky sníží nastavení a řekne, co změnil.

## Hotovo {#when-its-done}

Video se uloží do **`Movies/MobiCut`** a objeví se v galerii. Z dialogu můžeš:

- **Play**: přehrát ho,
- **Share**: rovnou ho poslat do aplikace na zprávy,
- **Close**: zavřít.

{% include screen.html name="export-done" alt="Dialog Saved to gallery s Play, Share a Close." %}

## Logo mobiCutu {#the-mobicut-logo}

Edice Free přidá do pravého horního rohu exportovaného videa malé logo **(mc) mobiCut** (vidíš ho
i v náhledu, takže žádná překvapení). Pro exportuje bez něj. Ve Free ukazuje panel exportu
**Remove watermark** se štítkem **PRO**.

Žádné reklamy se neukazují před exportem, během něj ani po něm, v žádné edici. Viz [Free a Pro]({{ "/cs/editions/" | relative_url }}).
