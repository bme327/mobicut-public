---
title: Sledování dráhy
parent: Funkce
nav_order: 10
---

# Sledování dráhy
{: .no_toc }

Nech text nebo grafiku sledovat něco, co se hýbe: jméno, které drží u paraglidisty, šipku, která
ukazuje na lyžaře celou cestu dolů. Jde to dvěma způsoby: **zakroužkuj objekt** a **AI dráha**
ho bude sledovat (Free), nebo **nakresli dráhu rukou** prstem, zatímco video hraje (Pro). Tak
i tak po ní překryv jede v náhledu i v exportu.

1. TOC
{:toc}

---

## Dva způsoby {#two-ways}

Otevři [text]({{ "/cs/operations/subtitles/" | relative_url }}) nebo
[grafiku]({{ "/cs/operations/graphics/" | relative_url }}) a přejdi na kartu **Motion**. Pod
**Follow something moving** jsou dvě tlačítka, naposledy použité první:

- **AI path**: zakroužkuj objekt a mobiCut ho sleduje videem za tebe.
- **Draw by hand** <span class="label label-yellow">PRO</span>: sleduješ ho prstem sám.

## AI dráha {#ai-path}

1. Klepni na **AI path**. Video vyplní obrazovku, zastavené tam, kde překryv začíná.
2. **Zakroužkuj objekt**, který se má sledovat, jedním prstem a těsně kolem něj.
3. mobiCut ukáže *Following the object…* a video při tom běží s ním; trvá to pár sekund.
   **Stop** to ukončí dřív a nechá, co už má.
4. Prohlédni si výsledek přes **▶** a klepni na **Accept**, nebo na **Take again** a zakroužkuj
   znovu. **Cancel** nechá překryv, jak byl.

- Text nebo grafika si od objektu **drží vzdálenost**, takže je nejdřív dej tam, kde je chceš mít
  (vedle paraglidisty, nad lyžaře).
- *Too broad* nebo *Too small*: zakroužkuj znovu, těsněji jen kolem objektu.
- Když objekt zmizí na moc dlouho (za strom, ze záběru), mobiCut řekne, kde ho ztratil;
  **Accept** nechá dráhu až do toho místa.
- AI dráha sleduje věci ve **videu**; nenabízí se, když překryv začíná na obrázku nebo textovém
  slidu.
- Běží v telefonu. Nic se nikam nenahrává.

## Nakreslit dráhu rukou {#capture-a-path}

Klepni na **Draw by hand** (Pro).

{% include screen.html name="path-capture" alt="Capture path: nahoře Cancel a Done s jednořádkovou nápovědou a oranžovým ukazatelem průběhu; uprostřed orámované video s kotvou překryvu na paraglidistovi a stopou prstu za ní; dole Recording… 2.5 s of 5.0 s a volby ½×, 1× a Auto-play." %}

Obrazovka se přepne na **Capture path**: video vyplní obrazovku, okolí snímku se ztmaví a nic
nezakrývá obraz.

1. **Podrž prst na kotvě**, značce uprostřed překryvu, a dej ji tam, kde má překryv začít.
2. Drž dál: *Get ready… put the anchor on what you want to follow*. Za chvilku (¾ s) začne
   nahrávání.
3. **Veď prst za objektem**, zatímco video pokračuje. Spodní řádek ukazuje
   *Recording… 2.5 s of 5.0 s*.
4. **Zvedni prst** a skončíš, pak klepni na **Done**. **Cancel** nahrávku zahodí.

**Ukazatel průběhu** nahoře ukazuje oranžově dobu překryvu na obrazovce. Tmavší části před ní
a za ní jsou krátké čekání, než se připravíš, a půl sekundy za koncem, která jen dotváří konec
dráhy; ani jedno ve videu není vidět.

Když prst zvedneš dřív, než nahrávání začne, prostě se začne znovu. Celé nahrání je pro **Undo**
jeden krok.

## Rychlost a Auto-play {#steps-or-smooth}

Volby pod videem určují, jak video při kreslení pokračuje; mobiCut si je pamatuje:

- **½×** nebo **1×**: jak rychle video hraje. ½× je snazší na rychlé objekty.
- **Auto-play** vypnuté: video hraje, jen dokud se prst hýbe, a zastaví se, když se zastaví on,
  takže máš čas.
- **Auto-play** zapnuté: video hraje samo a ty jen držíš prst na objektu.

Prst je vždy kousek za tím, co vidíš, a tak mobiCut každý bod posune o něco dřív, aby to vyrovnal.

## Po nahrání {#after-capturing}

{% include screen.html name="path-row" alt="Text s nahranou dráhou slabě nakreslenou přes video a karta Motion posunutá dolů: Path: 5.0 s recorded s tlačítkem přehrát, Clear path, Capture again a Follow path from…." %}

Karta **Motion** teď ukazuje **Path: 5.0 s recorded** (u AI dráhy **AI path: 5.0 s**) a nabízí:

- **▶**: přehrát,
- **Clear path**: překryv zase zůstane na jednom místě,
- **Capture again**: udělat novou, stejným způsobem jako tuhle (AI nebo rukou).

Dokud překryv upravuješ, jeho dráha je slabě vidět v náhledu.

- **Posunutím překryvu** ve videu posuneš celou dráhu s ním, i s jejím tvarem.
- **Změna velikosti a natočení** fungují jako obvykle; překryv si po celé dráze drží velikost i úhel.
- Dráha drží na **záznamu**, ne na hodinách: zrychli úsek nebo smaž část pod překryvem a pořád
  sleduje stejný objekt.
- Tlačítka **Position** na kartě **Look** jsou, dokud má překryv dráhu, skrytá.

## Převzít dráhu jiného překryvu {#follow-path-from-another-overlay}

Je-li ve stejnou dobu na obrazovce jiný text nebo grafika **s dráhou**, karta **Motion** nabídne
**Follow path from…**. Vyber, který sledovat (nebo jen potvrď, je-li jediný), a klepni na
**Follow**: tenhle překryv pojede vedle něj a udrží si vzdálenost, jakou má teď. Hodí se na jméno
vedle šipky.

Dráha se zkopíruje jednou. Když první překryv později nahraješ znovu, použij **Follow path from…**
ještě jednou. Ve Free jde převzít jen AI dráhu.

## Free a Pro {#free-and-pro}

**AI dráha** je **Free**. Kreslení dráhy **rukou** je **Pro**; ve Free má tlačítko **Draw by hand**
odznak **PRO**. Dráhy kreslené rukou zůstanou po přepnutí na Free uložené: překryv jen zůstane
na místě a s Pro po dráze zase pojede. AI dráhy fungují i ve Free.
Viz [Free a Pro]({{ "/cs/editions/" | relative_url }}).
