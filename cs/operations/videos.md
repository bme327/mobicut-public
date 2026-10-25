---
title: Více videí
parent: Funkce
nav_order: 15
---

# Více videí v jednom projektu
{: .no_toc }

Dej let a přistání natočené jinou kamerou do jednoho videa: přidej do časové osy projektu další
videa a upravuj je společně. Ve Free i v Pro.

1. TOC
{:toc}

---

## Přidat video {#add-a-video}

1. Klepni na **Add**.
2. Klepni na **Video from Gallery** nebo **Video from files** (SD karta, USB, Stažené soubory, Disk…).

Video přijde na **konec** časové osy a přehrávací hlava skočí na jeho začátek. Pak jeho části
stříhej, maž, zrychluj a tlum jako jakékoli jiné.

Do [hodinového limitu]({{ "/cs/editions/" | relative_url }}) Free se počítají všechna videa projektu dohromady.

## Na časové ose {#on-the-timeline}

{% include screen.html name="media-timeline" alt="Editor s úsekem obrázku (značka 1), bílým spojem dvou videí (značka 2), ztlumeným úsekem (značka 3) a stopou hudby (značka 4)." %}

- **Bílá čára** (značka 2) značí, kde jedno video (nebo [obrázek]({{ "/cs/operations/pictures/" | relative_url }}),
  značka 1) končí a začíná další. Na rozdíl od oranžové značky střihu ji nejde posunout ani
  odstranit, protože na každé straně je jiný soubor.
- Kulaté tlačítko na ní přidá [přechod]({{ "/cs/operations/transitions/" | relative_url }}),
  stejně jako mezi jakýmikoli dvěma úseky.
- [Podrobnosti úseku]({{ "/cs/operations/segment-info/" | relative_url }}) přes **ⓘ** ukážou, ze
  kterého videa úsek je.

## Odstranit celé video {#remove-a-whole-video}

Vyber kterýkoli jeho úsek, klepni na **ⓘ**, pak **Remove this whole video** a potvrď. Zmizí
všechny jeho úseky i texty na něm. **Undo** ho vrátí. Poslední video projektu odstranit nejde.

## Export {#export}

- Hotové video má **rozměry a snímkovou frekvenci prvního videa** na časové ose. Videa jiné
  velikosti nebo orientace se do toho rámu vejdou, s černými pruhy tam, kde se tvary liší.
- Všechno hraje za sebou, takže export je dlouhý jako časová osa;
  [hudba]({{ "/cs/operations/soundtracks/" | relative_url }}) přesahující jeho konec se ořízne.

## Video nejde najít {#a-video-cant-be-found}

Chybí-li první video projektu, editor tě požádá, abys ho
[znovu našel]({{ "/cs/operations/missing-video/" | relative_url }}). Chybí-li některé z přidaných
videí nebo obrázků, mobiCut řekne, které nejde otevřít; jeho část náhledu zůstane černá.
