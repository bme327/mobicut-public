---
title: Texty
parent: Funkce
nav_order: 8
---

# Texty
{: .no_toc }

Krátké texty přes video: místo, jméno, výška. Umístíš, natočíš a nastyluješ je přímo ve videu
a to, co vidíš v náhledu, export přesně vpálí.

1. TOC
{:toc}

---

{% include screen.html name="subtitles-timeline" alt="Štítky textů na stopě překryvů pod časovou osou a text ve videu v náhledu." %}

## Přidat text {#add-a-text}

1. Posuň přehrávací hlavu tam, kde se má text objevit.
2. Klepni na **Text** v liště nástrojů (značka 2).
3. Pod náhledem se otevře editor textu s připravenou klávesnicí: napiš text.
4. Klepni na **Done**.

Nový text začíná u přehrávací hlavy, zůstává na obrazovce **5 s** a vypadá jako text, který jsi
upravoval naposledy (stejná pozice, vzhled i pohyb; vždy ale začíná rovně, nenatočený). Na stopě
překryvů se objeví modrý štítek (značka 1). Začíná malým **T**, takže text poznáš, i když je
štítek moc krátký na slova.

Když klepneš na **Done** a nic nenapíšeš, prázdný text se zahodí.

## Editor textu {#the-text-editor}

Text otevřeš klepnutím na něj **ve videu** (při pozastavení) nebo na jeho **modrý štítek** na
časové ose. Editor nahradí časovou osu; náhled zůstane nad ním a každou změnu hned ukáže.

{% include screen.html name="subtitle-editor" alt="Editor textu: text ve videu s čárkovaným rámečkem, oranžovými úchyty v rozích a kulatým úchytem na otáčení nad ním, pod ním karta Text s textem, Duration a Starts at." %}

1. **Táhni text** a posuneš ho ve videu. Přichytává se k vodorovnému středu.
2. **Táhni roh** a změníš velikost rámečku. Text se zalamuje na šířku rámečku; potřebuje-li víc
   místa, rámeček se protáhne do výšky.
3. **Karty**: *Text*, *Look* a *Motion*.
4. **Starts at**: posun textu v čase (viz [níže](#move-it-in-time)).
5. **▶** přehraje text i s nástupem a odchodem, od půl sekundy před do půl sekundy po něm.
   Editor zůstane otevřený.
6. **Done** editor zavře. Všechno, cos změnil, je pro **Undo** **jeden** krok.
7. **Kulatý úchyt** na stopce nad rámečkem text otáčí (viz [Natočení](#turn-it)).

Ikona koše text smaže. Tlačítko **Zpět** telefonu editor zavře, stejně jako **Done**.

### Text {#text}

- Samotný text; zalamuje se do rámečku.
- **Duration**: jak dlouho zůstane na obrazovce v hotovém videu, **−** / **+** po půl sekundě
  (0,5–60 s).
- **Starts at**: kdy se objeví.

{: .note }
> Časy se počítají v **hotovém** videu. Text na 5 s přes úsek zrychlený na 4× zůstane na
> obrazovce pořád 5 s; jen pokryje víc původního záznamu.

### Vzhled (Look) {#look}

{% include screen.html name="subtitle-look" alt="Karta Look: volba písma, Bold a Italic, zarovnání, Size, vzorky barev textu a posuvníky průhlednosti. Text ve videu je tučný patkový žlutý bez pozadí." %}

- **Font**: Sans, Serif, Mono, Condensed, Casual, Cursive, Small caps.
- **Bold**, **Italic** a **zarovnání** (vlevo, na střed, vpravo) v rámečku.
- **Size**: 2–16 % kratší strany videa, takže vypadá stejně v 720p i 4K.
- **Text colour** a **Text opacity**: barva a krytí textu.
- **Background colour** a **Background opacity**: zaoblený pruh za textem. Pod 40 % dostane text
  jemný stín, aby zůstal čitelný i proti sněhu a obloze.
- **Position (or drag it on the video)**: *Top*, *Middle*, *Bottom* a *Centre* tam rámeček
  umístí jedním klepnutím. Když text [sleduje dráhu]({{ "/cs/operations/paths/" | relative_url }}),
  jsou skryté.
- **Rotation**: o kolik je text natočený, a **Reset**, který ho narovná.
- **Use this position, look and motion for all texts** zkopíruje styl tohoto textu na všechny
  texty v projektu.

### Pohyb (Motion) {#motion}

{% include screen.html name="subtitle-motion" alt="Karta Motion: Ease in Zoom 0,4 s, Ease out Fade 0,3 s a efekt Wobble." %}

- **Ease in** a **Ease out**: jak se text objeví a jak zmizí.
  - *None*: prostě se zapne a vypne,
  - *Fade*: plynule se objeví a vytratí,
  - *Slide*: přijede zespodu, odjede dolů a přitom se prolne,
  - *Zoom*: zvětší se dovnitř, zmenší se ven,
  - *Type*: vypíše se písmeno po písmenu (při odchodu se vytratí).

  Každý má **Duration** 0,1–2 s; žádný nezabere víc než polovinu času textu na obrazovce.
- **Effect while shown**: *Wobble* (jemně se kolébá), *Pulse* (dýchá větší a menší),
  *Shake* (třese se), *Float* (pohupuje se nahoru a dolů).
- **Follow something moving**: zakroužkuj objekt a **AI dráha** ho bude sledovat, nebo nakresli
  dráhu prstem (**Draw by hand**, Pro). Viz [Sledování dráhy]({{ "/cs/operations/paths/" | relative_url }}).

Při pozastavení ukazuje náhled text v klidu, aby se snadno umisťoval. Pohyb uvidíš klepnutím na **▶**.

## Natočení {#turn-it}

Táhni **kulatý úchyt** nad rámečkem a text se otočí kolem svého středu. **Přichytí se** na rovnou
polohu, vzhůru nohama a na obě polohy na bok, a telefon přitom lehce cvakne. Posun a změna
velikosti fungují u natočeného textu stejně: táhni ho, nebo zatáhni za roh (protější roh zůstane
na místě).

Karta **Look** ukazuje úhel; **Reset** text zase narovná. Efekty jako *Wobble* ho kolébají kolem
úhlu, který jsi nastavil.

## Posun v čase {#move-it-in-time}

Dvěma způsoby:

- **Táhni jeho štítek** po stopě překryvů pod časovou osou. Přehrávací hlava jde s ním, takže
  náhled ukazuje, kam dopadne. Každé tažení je pro **Undo** jeden krok; klepnutí pořád otevře editor.
- V editoru přes **Starts at** s **−1 s**, **−0.1**, **+0.1** a **+1 s**. Zobrazený čas je čas
  v hotovém videu, stejně jako časy pod náhledem.

V obou případech si text ponechá dobu na obrazovce, i když se přesune na zrychlený úsek.
U konce videa se zkrátí, aby nepřesahoval jeho konec.

## Několik najednou {#several-at-once}

Texty se můžou v čase překrývat, třeba nadpis nahoře a popisek dole. Ukážou se všechny, každý
ve svém rámečku, spolu s [grafikou]({{ "/cs/operations/graphics/" | relative_url }}).

## Texty v exportu {#texts-in-the-export}

Při [exportu]({{ "/cs/operations/export/" | relative_url }}) volba **Text** určí:

- **Burn into video**: texty se stanou součástí obrazu, s pozicí, natočením, vzhledem i pohybem,
  přesně jako v náhledu. Prolínačky z [přechodů]({{ "/cs/operations/transitions/" | relative_url }})
  ztmaví i je.
- **Off**: čisté video bez nich. V projektu zůstanou.

{: .note }
> Texty se dřív jmenovaly *titulky* a šly uložit i jako samostatný soubor `.srt`. Tahle možnost
> zmizela; starší projekty se otevřou se všemi texty, jak byly.

Na celoobrazovkovou titulní kartu mezi částmi videa použij raději
[textový slide]({{ "/cs/operations/text-slides/" | relative_url }}).
