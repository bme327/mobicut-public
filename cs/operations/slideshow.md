---
title: Prezentace
parent: Funkce
nav_order: 13.5
---

# Prezentace z obrázků
{: .no_toc }

Udělej z hromádky fotek video najednou: nejlepší záběry dne, výlet v obrázcích. Vyber fotky, řekni,
jak dlouhé má video být, a mobiCut založí nový projekt, ve kterém je každá fotka obyčejný úsek
s [obrázkem]({{ "/cs/operations/pictures/" | relative_url }}).

1. TOC
{:toc}

---

## Vytvořit prezentaci {#make-a-slideshow}

1. Na úvodní obrazovce klepni na **New project** a pak na **Slideshow from pictures**.
2. Vyber obrázky v galerii, **nejvýš 50**, v pořadí, v jakém se mají přehrát.
3. Nastav volby (níže) a klepni na **Create**.

{% include screen.html name="new-project" alt="Panel 'New project from…' s volbami Gallery, Browse files a Slideshow from pictures." %}

Editor se otevře s jedním úsekem na každý obrázek, v pořadí, v jakém jsi je vybral. Projekt se
jmenuje *Slideshow*; [přejmenuj ho]({{ "/cs/operations/projects/" | relative_url }}), jak chceš.

{% include screen.html name="slideshow" alt="Dialog Slideshow: 12 obrázků s náhledy, Length of the video 1:00 s posuvníkem a 'About 5.0 s per picture', tvary Landscape, Portrait a Square, rozlišení 720p, 1080p a 4K a pod nimi 1920×1080 · 30 fps, efekty Still, Zoom in, Zoom out a Slide in a přepínač Transitions between pictures." %}

## Volby {#options}

- **Length of the video**: táhni posuvníkem. Začíná na 5 sekundách na obrázek a jde od 1 do
  20 sekund na obrázek; řádek pod ním ukazuje čas, který dostane každý obrázek. Všechny obrázky
  se ukazují stejně dlouho.
- **Shape**: **Landscape** (16:9), **Portrait** (9:16) nebo **Square**. Začíná na tvaru prvního
  obrázku. Obrázky jiného tvaru se vejdou do rámečku.
- **Resolution**: **720p**, **1080p** nebo **4K**, pod volbami je velikost snímku v pixelech. Video
  má 30 fps. **4K je Pro**; Free exportuje nejvýš v 1080p.
- **Effect**: stejný pohyb pro všechny obrázky: **Still**, **Zoom in**, **Zoom out** nebo
  **Slide in** (viz [Obrázky]({{ "/cs/operations/pictures/" | relative_url }})).
- **Transitions between pictures**: dá přechod do každého spoje a roztmívání na začátek a zatmívání
  na konec, s typem a délkou naposledy použitými v
  [Přechodech v každém spoji]({{ "/cs/operations/transitions/" | relative_url }}).

Dialog si pamatuje rozlišení, efekt a přechody na příště.

## Potom {#after-that}

Prezentace je normální projekt. Délku nebo efekt kteréhokoli obrázku změníš v jeho
[Segment info]({{ "/cs/operations/segment-info/" | relative_url }}), obrázky můžeš mazat i přidávat
a přidat [texty]({{ "/cs/operations/subtitles/" | relative_url }}),
[grafiku]({{ "/cs/operations/graphics/" | relative_url }}),
[textové slidy]({{ "/cs/operations/text-slides/" | relative_url }}),
[hudbu]({{ "/cs/operations/soundtracks/" | relative_url }}) a dokonce i
[videa]({{ "/cs/operations/videos/" | relative_url }}). Snímek si drží tvar a rozlišení zvolené tady,
i když přidáš video.

{: .note }
> Prezentace nemá vlastní zvuk. Pro hudbu přidej [zvukovou stopu]({{ "/cs/operations/soundtracks/" | relative_url }});
> bez ní je exportované video tiché.

Prezentace jsou zdarma v obou edicích (4K potřebuje Pro).
