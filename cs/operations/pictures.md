---
title: Obrázky
parent: Funkce
nav_order: 13
---

# Přidat obrázek
{: .no_toc }

Vlož do videa fotku: snímek z vrcholu, mapu letu, úvodní titulní kartu. Obrázek se stane
samostatným úsekem, který se ukazuje tak dlouho, jak zvolíš, v klidu nebo v pohybu.

1. TOC
{:toc}

---

## Vložit obrázek {#insert-a-picture}

1. Posuň přehrávací hlavu tam, kam má obrázek přijít.
2. Klepni na **Add** a pak **Picture at the pointer**.
3. Klepni na **Gallery** nebo **Browse files** a vyber obrázek. Jeho název se ukáže pod tlačítky.
4. Nastav **Duration** pomocí **−** a **+** (po 0,5 s, od 0,5 s do 60 s; začíná na 3 s).
5. Vyber **Effect** (viz níže) a klepni na **Insert**.

{% include screen.html name="picture-add" alt="Dialog Add picture: tlačítka Gallery a Browse files, název vybraného obrázku, Duration 3,0 s a efekty Still, Slow zoom in (vybraný), Slow zoom out a Slide in." %}

Video se v místě přehrávací hlavy rozstřihne a obrázek přijde mezi; všechno za ním se posune
o délku obrázku, texty také. Je-li přehrávací hlava méně než desetinu sekundy od střihu, obrázek
přijde přímo na ten střih a nevznikne drobný úsek.

## Snímek z videa {#a-still-from-the-video}

Chceš-li použít snímek ze samotného videa, třeba podržet okamžik startu na pár sekund, klepni
v dialogu **Add picture** na **Video still**. Vezme snímek videa **u přehrávací hlavy** v plném
rozlišení a vedle názvu (*Still 1:12.4*) ukáže jeho malý náhled. Délku a efekt nastav jako
u každého obrázku a klepni na **Insert**.

Snímek se uloží s projektem (a zálohuje se s ním), takže zůstane, i když se video později
přesune. Pod tlačítkem dialog napíše, proč snímek teď vzít nejde: třeba *The playhead is on a
picture*, *on a text slide* nebo *on a deleted part* (hlava stojí na obrázku, na textovém slidu
nebo na smazané části).

## Efekty {#effects}

| Efekt | Co dělá |
|---|---|
| **Still** | Bez pohybu |
| **Slow zoom in** | Po celou dobu se přibližuje |
| **Slow zoom out** | Začne zblízka a vzdaluje se |
| **Slide in** | Přijede zprava (asi za sekundu) a pak zůstane |

Náhled ukazuje efekt tak, jak bude v exportu. Obrázky se vejdou do rámu videa, s černými
pruhy, pokud mají jiný tvar.

## Na časové ose {#on-the-timeline}

Úsek s obrázkem ukazuje obrázek a jako popisek jeho efekt (**Picture**, **Zoom in**,
**Zoom out**, **Slide in**). Bílá čára značí, kde začíná a končí
(viz [Více videí]({{ "/cs/operations/videos/" | relative_url }}#on-the-timeline)).

Funguje jako každý jiný úsek:

- můžeš ho [smazat a obnovit]({{ "/cs/operations/delete/" | relative_url }}),
- před něj nebo za něj dát [přechod]({{ "/cs/operations/transitions/" | relative_url }}), třeba
  fade out-in, nebo Interleave, aby se s videem prolnul,
- můžou přes něj běžet [texty]({{ "/cs/operations/subtitles/" | relative_url }}) a [grafika]({{ "/cs/operations/graphics/" | relative_url }}).

**Speed** a **Mute** se na obrázky nevztahují a jsou zašedlé, když je obrázek vybraný.

## Změnit nebo odstranit obrázek {#change-or-remove-a-picture}

Vyber ho a klepni na **ⓘ**. V [podrobnostech úseku]({{ "/cs/operations/segment-info/" | relative_url }})
je **Duration & effect…** pro změnu a **Remove this picture**.

{: .note }
> Délka jde měnit jen dokud je obrázek jeden úsek. Když ho rozstřihneš, jeho délka je pevná
> (dialog to řekne); efekt jde měnit dál.

Obrázky jsou v obou edicích.
