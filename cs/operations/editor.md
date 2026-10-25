---
title: Editor
parent: Funkce
nav_order: 3
---

# Editor: přehrávání a časová osa
{: .no_toc }

1. TOC
{:toc}

---

{% include screen.html name="editor" alt="Editor s časovou osou ve spodní polovině." %}

## Přehrát a pozastavit {#play-and-pause}

Klepni na **▶** pod náhledem. Přehrávání už odpovídá tvým úpravám: smazané úseky se přeskakují,
zrychlené úseky hrají rychle, texty a grafika se ve videu objevují i s animací, prolínačky ztmavují obraz
a Interleave se prolínají.

Dva malé časy vedle tlačítek jsou pozice v **hotovém videu** (nahoře) a jeho celková délka
(dole), například `0:21.4` nad `0:48.0`. Mění se, jak mažeš a zrychluješ úseky.

## Skoky {#jump}

Tlačítka kolem **▶** posouvají přehrávací hlavu, i během přehrávání:

| Tlačítko | Skočí |
|---|---|
| **⏮** | Na začátek hotového videa (jeho první ponechaný snímek) |
| **↺ 5** | O 5 sekund zpět |
| **↻ 5** | O 5 sekund vpřed |
| **⏭** | Na konec (přehrávání se tam zastaví) |

Těch 5 sekund je 5 sekund **hotového** videa: smazané části se přeskočí a přes úsek zrychlený
na 4× posune skok originálem o 20 sekund.

## Pohyb po videu {#move-around-the-video}

- **Klepni** kamkoli na časovou osu a skočíš tam.
- **Táhni** po časové ose a projíždíš videem.

Bílá čára s tečkou je **přehrávací hlava**: aktuální pozice. Úsek pod ní je **vybraný** (oranžový
obrys); nástroje pracují s vybraným úsekem.

## Čtení časové osy {#read-the-timeline}

| Vidíš | Znamená to |
|---|---|
| Pás obrázků | Snímky z videa, abys místa našel podle pohledu |
| `1×`, `4×`, `0.5×` v rohu | Rychlost úseku (oranžově, když není 1×) |
| `1× · muted` | Zvuk úseku je [ztlumený]({{ "/cs/operations/mute/" | relative_url }}) |
| `Picture`, `Zoom in`, `Zoom out`, `Slide in` | Úsek s [obrázkem]({{ "/cs/operations/pictures/" | relative_url }}) a jeho efekt |
| Bílá čára přes pás | Tady končí jedno video nebo obrázek a začíná další ([více videí]({{ "/cs/operations/videos/" | relative_url }})) |
| Oranžová čára s ▼ nahoře | Střih mezi dvěma úseky |
| Krátká červená čára | Tady jsou skryté smazané záběry |
| Kulaté tlačítko na střihu | Přechod (viz [Přechody]({{ "/cs/operations/transitions/" | relative_url }})) |
| ⓘ na vybraném úseku | [Podrobnosti úseku]({{ "/cs/operations/segment-info/" | relative_url }}) |
| Časy nad pásem | Časy v *původním* videu (videa a obrázky za sebou) |
| Zelené štítky pod texty | [Hudba]({{ "/cs/operations/soundtracks/" | relative_url }}); stopa se ukáže, až nějakou přidáš |

## Přiblížení {#zoom-in}

U dlouhého videa potřebuje střih přesnost. Použij cokoli z toho:

- **🔍+ / 🔍−** pod časovou osou (každé klepnutí přiblížení zdvojnásobí nebo zmenší na polovinu),
- **roztažení dvěma prsty** na časové ose,
- **posuvník** mezi nimi pro pohyb po přiblížené ose.

## Přiblížení náhledu {#zoom-the-preview}

**Roztáhni video** dvěma prsty a podíváš se zblízka (až 6×); stejnými dvěma prsty ho posouváš.
Funguje to všude, kde je náhled: při přehrávání, úpravě textu nebo grafiky, kreslení i nahrávání
dráhy. Štítek na náhledu ukazuje, jak moc je přiblíženo (např. *2.5×*); klepnutím uvidíš zase
celý snímek. Přiblížení mění jen tvůj pohled, ne exportované video.

## Celá obrazovka {#full-screen}

Klepni na tlačítko **celé obrazovky** v rohu náhledu a uvidíš střih ve velkém. Video na šířku
otočí obrazovku. Ovládání dole (přehrát/pozastavit, čas, posuvník) se při přehrávání schová;
dotkni se obrazovky a vrátí se. Velké tlačítko nahoře tě vrátí zpět.

## Zpět {#undo}

**↶** (vpravo nahoře u ovládání) vrátí poslední změnu: střih, smazání, změnu rychlosti, text, grafiku,
přechod, ztlumení, obrázek, hudbu nebo přidané video. Opakovaným klepnutím jdeš dál do historie.

## Otočení obrazovky {#turn-the-screen}

Na **telefonu** zůstává editor na výšku, i když telefon otočíš na šířku.
**Tablet** můžeš držet jakkoli; na šířku je náhled mnohem větší. Viz
[Tablety a režim na šířku]({{ "/cs/operations/tablet/" | relative_url }}).
