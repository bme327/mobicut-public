---
title: Titulky
parent: Funkce
nav_order: 8
---

# Titulky
{: .no_toc }

Krátké texty přes video: místo, jméno, výška. Umístíš a nastyluješ je přímo ve videu a to, co
vidíš v náhledu, export přesně vpálí. Exportovat je jde i jako samostatný soubor `.srt`.

1. TOC
{:toc}

---

{% include screen.html name="subtitles-timeline" alt="Štítky titulků na stopě titulků pod časovou osou a titulek ve videu v náhledu." %}

## Přidat titulek {#add-a-subtitle}

1. Posuň přehrávací hlavu tam, kde se má text objevit.
2. Klepni na **Subtitle** v liště nástrojů (značka 2).
3. Pod náhledem se otevře editor titulku s připravenou klávesnicí: napiš text.
4. Klepni na **Done**.

Nový titulek začíná u přehrávací hlavy, zůstává na obrazovce **5 s** a vypadá jako titulek, který
jsi upravoval naposledy (stejná pozice, vzhled i pohyb). Na stopě titulků se objeví modrý štítek
(značka 1). Začíná malým **T**, takže titulek poznáš, i když je štítek moc krátký na text.

Když klepneš na **Done** a nic nenapíšeš, prázdný titulek se zahodí.

## Editor titulku {#the-subtitle-editor}

Titulek otevřeš klepnutím na něj **ve videu** (při pozastavení) nebo na jeho **modrý štítek** na
časové ose. Editor nahradí časovou osu; náhled zůstane nad ním a každou změnu hned ukáže.

{% include screen.html name="subtitle-editor" alt="Editor titulku: titulek ve videu s čárkovaným rámečkem a oranžovými úchyty v rozích, pod ním karta Text s textem, Duration a Starts at." %}

1. **Táhni titulek** a posuneš ho ve videu. Přichytává se k vodorovnému středu.
2. **Táhni roh** a změníš velikost rámečku. Text se zalamuje na šířku rámečku; potřebuje-li víc
   místa, rámeček se protáhne do výšky.
3. **Karty**: *Text*, *Look* a *Motion*.
4. **Starts at**: posun titulku v čase (viz [níže](#move-it-in-time)).
5. **▶** přehraje titulek i s nástupem a odchodem, od půl sekundy před do půl sekundy po něm.
   Editor zůstane otevřený.
6. **Done** editor zavře. Všechno, cos změnil, je pro **Undo** **jeden** krok.

Ikona koše titulek smaže. Tlačítko **Zpět** telefonu editor zavře, stejně jako **Done**.

### Text {#text}

- Samotný text; zalamuje se do rámečku.
- **Duration**: jak dlouho zůstane na obrazovce v hotovém videu, **−** / **+** po půl sekundě
  (0,5–60 s).
- **Starts at**: kdy se objeví.

{: .note }
> Časy se počítají v **hotovém** videu. Titulek na 5 s přes úsek zrychlený na 4× zůstane na
> obrazovce pořád 5 s; jen pokryje víc původního záznamu.

### Vzhled (Look) {#look}

{% include screen.html name="subtitle-look" alt="Karta Look: volba písma, Bold a Italic, zarovnání, Size, vzorky barev textu a posuvníky průhlednosti. Titulek ve videu je tučný patkový žlutý bez pozadí." %}

- **Font**: Sans, Serif, Mono, Condensed, Casual, Cursive, Small caps.
- **Bold**, **Italic** a **zarovnání** (vlevo, na střed, vpravo) v rámečku.
- **Size**: 2–16 % kratší strany videa, takže vypadá stejně v 720p i 4K.
- **Text colour** a **Text opacity**: barva a krytí textu.
- **Background colour** a **Background opacity**: zaoblený pruh za textem. Pod 40 % dostane text
  jemný stín, aby zůstal čitelný i proti sněhu a obloze.
- **Position**: *Top*, *Middle*, *Bottom* a *Centre* tam rámeček umístí jedním klepnutím; jinam ho
  přetáhni ve videu.
- **Use this position, look and motion for all subtitles** zkopíruje styl tohoto titulku na všechny
  titulky v projektu.

### Pohyb (Motion) {#motion}

{% include screen.html name="subtitle-motion" alt="Karta Motion: Ease in Zoom 0,4 s, Ease out Fade 0,3 s a efekt Wobble." %}

- **Ease in** a **Ease out**: jak se titulek objeví a jak zmizí.
  - *None*: prostě se zapne a vypne,
  - *Fade*: plynule se objeví a vytratí,
  - *Slide*: přijede zespodu, odjede dolů a přitom se prolne,
  - *Zoom*: zvětší se dovnitř, zmenší se ven,
  - *Type*: vypíše se písmeno po písmenu (při odchodu se vytratí).

  Každý má **Duration** 0,1–2 s; žádný nezabere víc než polovinu času titulku na obrazovce.
- **Effect while shown**: *Wobble* (jemně se kolébá), *Pulse* (dýchá větší a menší),
  *Shake* (třese se), *Float* (pohupuje se nahoru a dolů).

Při pozastavení ukazuje náhled titulek v klidu, aby se snadno umisťoval. Pohyb uvidíš klepnutím na **▶**.

## Posun v čase {#move-it-in-time}

Dvěma způsoby:

- **Táhni jeho štítek** po stopě titulků pod časovou osou. Přehrávací hlava jde s ním, takže
  náhled ukazuje, kam dopadne. Každé tažení je pro **Undo** jeden krok; klepnutí pořád otevře editor.
- V editoru přes **Starts at** s **−1 s**, **−0.1**, **+0.1** a **+1 s**. Zobrazený čas je čas
  v hotovém videu, stejně jako časy pod náhledem.

V obou případech si titulek ponechá dobu na obrazovce, i když se přesune na zrychlený úsek.
U konce videa se zkrátí, aby nepřesahoval jeho konec.

## Několik najednou {#several-at-once}

Titulky se můžou v čase překrývat, třeba nadpis nahoře a popisek dole. Ukážou se všechny, každý
ve svém rámečku.

## Titulky v exportu {#subtitles-in-the-export}

Při [exportu]({{ "/cs/operations/export/" | relative_url }}) vyber:

- **Burn into video**: titulky se stanou součástí obrazu, s pozicí, vzhledem i pohybem, přesně
  jako v náhledu. Prolínačky z [přechodů]({{ "/cs/operations/transitions/" | relative_url }})
  ztmaví i je.
- **Separate .srt file**: uloží se do `Download/MobiCut` vedle čistého videa. Soubor `.srt`
  obsahuje jen text a časy; přehrávače ho ukazují ve vlastním stylu.
- **Off**: bez titulků.

Titulky z projektů vytvořených před zavedením stylů si ponechají klasický vzhled: bílý text na
tmavém pruhu u spodního okraje.
