---
title: Grafika
parent: Funkce
nav_order: 9
---

# Grafika <span class="label label-yellow">PRO</span>
{: .no_toc }

Smajlíci, šipky, kruhy, hvězdy a vlastní obrázky přes video: ukaž na místo přistání, zakroužkuj
druhého paraglidistu, dej smějícího se smajlíka na pád. Grafika funguje jako
[texty]({{ "/cs/operations/subtitles/" | relative_url }}): umístíš ji, zvětšíš a natočíš přímo ve
videu, dáš jí vzhled a pohyb a export ji vpálí přesně tak, jak ji ukazuje náhled.

1. TOC
{:toc}

---

## Přidat grafiku {#add-a-graphic}

1. Posuň přehrávací hlavu tam, kde se má grafika objevit.
2. Klepni na **Graphic** v liště nástrojů.
3. Vyber tvar, nebo **Your own picture from Gallery** (vlastní obrázek z galerie).

{% include screen.html name="graphic-picker" alt="Panel Graphic: Appears at the pointer, in the middle of the video; řada šesti smajlíků, pod ní šipky, obdélník, zaoblený obdélník, kruh, hvězda, čára, bublina, zvýrazňovač, fajfka a křížek, a tlačítko Your own picture from Gallery." %}

Nová grafika se objeví **u přehrávací hlavy**, **uprostřed videa**, na **5 s** a s pohybem
grafiky, kterou jsi upravoval naposledy. Hned se otevře její editor a na stopě překryvů pod
časovou osou se objeví fialový štítek s názvem tvaru.

### Tvary {#the-shapes}

| Skupina | Tvary |
|---|---|
| **Smajlíci** | Happy, Laughing, Wink, Sad, Surprised, Cool |
| **Šipky a čáry** | Arrow, Block arrow, Curved arrow, Line |
| **Tvary** | Rectangle, Rounded, Circle, Star, Speech bubble, Marker (tah zvýrazňovačem) |
| **Značky** | Tick (fajfka), Cross (křížek) |
| **Obrázek** | Vlastní obrázek: logo, mapa, fotka startoviště |

Smajlíci, hvězda, fajfka, křížek a obrázky si drží proporce; šipky, čáry, obdélníky a kruhy se
roztáhnou podle rámečku, takže z kruhu může být elipsa.

## Editor grafiky {#the-graphic-editor}

{% include screen.html name="graphic-editor" alt="Zahnutá šipka ve videu s čárkovaným rámečkem, úchyty v rozích a úchytem na otáčení, pod ní karta Look s barvami čáry, Width a Opacity." %}

Ve videu se grafika chová jako text:

- **táhni** ji a posuneš ji (přichytává se k vodorovnému středu),
- **táhni roh** a změníš velikost,
- **táhni kulatý úchyt** nad ní a otočíš ji; přichytí se na rovnou polohu a na bok, s cvaknutím.

Pod náhledem jsou tři karty:

### Tvar (Shape) {#shape}

- Stejné tvary jako při přidání: klepnutím na jiný tvar ho vyměníš. Změněný vzhled se přenese na
  tvary stejného druhu (z jednoho smajlíka na jiného, z obdélníku na hvězdu).
- U obrázku místo toho: **Another picture from Gallery** (jiný obrázek z galerie).
- **Duration** a **Starts at**, stejně jako u textů.

### Vzhled (Look) {#look}

Co jde nastavit, záleží na tvaru:

| Tvar | Nastavení |
|---|---|
| Smajlíci | **Features & rim** (rysy a obrys: barva, šířka, krytí) a **Face colour** (barva obličeje, krytí) |
| Obdélník, kruh, hvězda, bublina, zvýrazňovač, plná šipka | **Outline** (obrys: zap/vyp, barva, šířka, krytí) a **Fill** (výplň: zap/vyp, barva, krytí) |
| Šipka, zahnutá šipka, čára, fajfka, křížek | **Line** (čára: barva, šířka, krytí) |
| Obrázek | **Opacity** (krytí) a **Border** (rámeček: zap/vyp, barva, šířka) |

Šířky jsou v procentech kratší strany videa, takže grafika vypadá stejně v 720p i 4K. Níž jsou
**Position (or drag it on the video)**, **Rotation** s **Reset** a
**Use this look and motion for all graphics**.

### Pohyb (Motion) {#motion}

Stejné **Ease in**, **Ease out** a **Effect while shown** jako u textů (chybí jen *Type*, ten je
pro písmena) a **Follow something moving**, aby grafika
[sledovala dráhu]({{ "/cs/operations/paths/" | relative_url }}).

**Done** editor zavře; všechny změny jsou pro **Undo** jeden krok. Ikona koše grafiku smaže.

## Vlastní obrázek {#your-own-picture}

Vyber obrázek z galerie a zkopíruje se do projektu (velké fotky se zmenší na 1600 px). Obrázky
s průhledností, třeba logo v PNG, si ji ponechají. Kopie se zálohuje s projektem, takže grafika
zůstane, i když originál z galerie smažeš.

## Posun v čase {#move-it-in-time}

Táhni její štítek po stopě překryvů, nebo použij **Starts at** na kartě **Shape**. Funguje to
přesně jako u [textů]({{ "/cs/operations/subtitles/#move-it-in-time" | relative_url }}).

## V exportu {#in-the-export}

Grafika se do exportovaného videa vpálí vždy, přesně jak ji ukazuje náhled. Volba **Text**
v exportu (*Burn into video* / *Off*) rozhoduje jen o textech; grafika zůstane v každém případě.

## Free a Pro {#free-and-pro}

Grafika je **Pro**. Ve verzi Free má nástroj **Graphic** odznak **PRO**. Projekt, který už grafiku
má, si ji po přepnutí na Free ponechá: jen se neukazuje ani neexportuje a s Pro se vrátí. Viz
[Free a Pro]({{ "/cs/editions/" | relative_url }}).
