---
title: Přechody
parent: Funkce
nav_order: 12
---

# Přechody
{: .no_toc }

Zjemni střihy mezi úseky a nech video na začátku plynule naběhnout a na konci zmizet.

1. TOC
{:toc}

---

{% include screen.html name="transition-buttons" alt="Kulatá tlačítka přechodů na časové ose: na každém střihu, na začátku a na konci. Jedno je vyplněné oranžově, protože má přechod." %}

## Kde přechody jsou {#where-transitions-go}

Když jsou smazané úseky skryté, ukazuje časová osa **kulaté tlačítko**:

- na **začátku** videa (značka 2): roztmívání z černé,
- na **každém střihu** (značka 1): přechod mezi dvěma úseky,
- na **konci**: zatmívání do černé.

Tlačítko s přechodem je **oranžové**.

## Přidat přechod {#add-a-transition}

1. Klepni na kulaté tlačítko.
2. Mezi úseky vyber **typ**:
   - **Fade out-in**: obraz se ztmaví do černé a zase se vrátí.
   - **Interleave** <span class="label label-yellow">PRO</span>: prolínání, konec jednoho úseku
     přejde do začátku dalšího. Video se zkrátí o délku přechodu.
3. Nastav **Duration** (0,5–10 s; celkem, v hotovém videu).
4. Klepni na **Save**, nebo na **Save & play** a hned se podíváš: náhled přehraje přechod
   i s 1,5 s před ním a po něm.

Na začátku a na konci se typ nevybírá: video se roztmí z černé nebo zatmí do černé, obraz i zvuk
společně.

{% include screen.html name="transition" alt="Dialog Add transition s vybraným Fade out-in a délkou 1,0 s." %}

## Přechody na všech spojích {#transitions-at-every-join}

Chceš-li dát celému videu stejné přechody najednou, klepni na **Add** → **Transitions at every join**.

{% include screen.html name="transitions-every-join" alt="Dialog Transitions at every join: Type Fade out-in (vybráno) nebo Interleave s odznakem PRO, Duration 2.0 s každý v exportu, zapnuté Fade in & out, Replace existing a Adds 3 transitions." %}

- **Type**: *Fade out-in* nebo *Interleave* <span class="label label-yellow">PRO</span>.
- **Duration**: délka každého přechodu v exportu.
- **Fade in & out**: video navíc roztmí na začátku a zatmí na konci.
- **Replace existing** (když už některé spoje přechod mají): nastaví tenhle přechod na všech
  spojích. Jinak ho dostanou jen spoje bez přechodu.

Řádek dole říká, co **Apply** udělá (*Adds 3 transitions.*). Celá změna je pro **Undo** jeden
krok a volba se zapamatuje na příště (na začátku Fade, 2 s, s roztmíváním a zatmíváním).

### Při exportu {#when-you-export}

Když některé spoje při klepnutí na **Export** nemají přechod, mobiCut se jednou zeptá: **Add
transitions?** Napíše, kolik míst přechod nemá, a nabídne zapamatovaný typ a délku:

- **Add & export** je přidá a pokračuje exportem,
- **Export as is** exportuje bez nich (pro tenhle projekt se znovu nezeptá, dokud aplikaci
  neotevřeš znovu),
- **Change type or duration…** otevře **Transitions at every join**.

## V náhledu {#in-the-preview}

Náhled přehrává přechody tak, jak je bude mít export: prolínačky ztmaví obraz do černé a zpět
a **Interleave** je skutečné prolínání, další úsek se roztmí přes konec předchozího a zvuk se
smíchá stejně. Když přechod uprostřed pozastavíš, vidíš přesně ten snímek, i při projíždění.

## Změnit nebo odstranit {#change-or-remove}

Klepni znovu na oranžové tlačítko, změň nastavení, nebo klepni na **Remove transition**.

{: .note }
> Přechod nemůže být delší, než dovolí sousední úseky. Jsou-li krátké, dialog hlásí, že je přechod
> *currently limited*; použije nejdelší délku, která se vejde.

## Free a Pro {#free-and-pro}

| Přechod | Free | Pro |
|---|---|---|
| Roztmívání na začátku, zatmívání na konci | ✓ | ✓ |
| **Fade out-in** mezi úseky | ✓ | ✓ |
| **Interleave** (prolínání) mezi úseky | | ✓ |

Ve Free má **Interleave** štítek **PRO**; klepnutím se dozvíš, co funkce dělá. Viz [Free a Pro]({{ "/cs/editions/" | relative_url }}).
