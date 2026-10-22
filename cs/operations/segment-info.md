---
title: Podrobnosti úseku
parent: Funkce
nav_order: 16
---

# Podrobnosti úseku

Klepni na **ⓘ** na vybraném úseku a uvidíš přesně, co pokrývá a jak skončí v hotovém videu.

{% include screen.html name="segment-info" alt="Podrobnosti úseku 2 ze 3: časy ve videu a v exportu, délka, rychlost a zvuk." %}

| Řádek | Význam |
|---|---|
| **Video** / **Picture** | Ze kterého souboru úsek je (u [více videí]({{ "/cs/operations/videos/" | relative_url }}) nebo obrázku) |
| **In the video** | Začátek a konec v jeho původním videu |
| **Shown** | U obrázku: kterou část délky obrázku tento úsek ukazuje |
| **Length** | Jeho délka v originálu |
| **Speed** / **Effect** | Jeho rychlost, nebo efekt obrázku |
| **In the export** | Začátek a konec v hotovém videu, nebo *Deleted* |
| **Export length** | Jak dlouho trvá v hotovém videu |
| **Audio** | *On*, *On, natural pitch* (zrychlený nebo zpomalený), *Muted* ([ztlumil jsi ho]({{ "/cs/operations/mute/" | relative_url }})) nebo *Muted (8× and above)*. U obrázků se neukazuje. |
| **Texts** | Kolik textů se úseku dotýká, pokud nějaké |

U smazaného úseku má dialog tlačítko **Restore**.

## Obrázky a celá videa {#pictures-and-whole-videos}

{% include screen.html name="segment-info-picture" alt="Podrobnosti úseku 2 ze 4 u obrázku: název, zobrazeno 0:00.0 až 0:03.0, efekt Zoom in, s Duration & effect… a Remove this picture." %}

- **Duration & effect…** (obrázky): otevře [nastavení obrázku]({{ "/cs/operations/pictures/" | relative_url }}#change-or-remove-a-picture).
- **Remove this picture** / **Remove this whole video**: po potvrzení odebere z projektu celý
  soubor, všechny jeho úseky i texty na něm. **Undo** ho vrátí.
  Ukazuje se, když má projekt víc než jedno video nebo obrázek; poslední odstranit nejde.
