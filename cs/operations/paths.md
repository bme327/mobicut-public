---
title: Sledování dráhy
parent: Funkce
nav_order: 10
---

# Sledování dráhy <span class="label label-yellow">PRO</span>
{: .no_toc }

Nech text nebo grafiku sledovat něco, co se hýbe: jméno, které drží u paraglidisty, šipku, která
ukazuje na lyžaře celou cestu dolů. Dráhu nakreslíš prstem, zatímco video hraje, a překryv po ní
jede v náhledu i v exportu.

1. TOC
{:toc}

---

## Nahrát dráhu {#capture-a-path}

1. Otevři [text]({{ "/cs/operations/subtitles/" | relative_url }}) nebo
   [grafiku]({{ "/cs/operations/graphics/" | relative_url }}) a přejdi na kartu **Motion**.
2. Pod **Follow something moving** klepni na **Capture path**.

{% include screen.html name="path-capture" alt="Capture path: nahoře Cancel a Done s jednořádkovou nápovědou a oranžovým ukazatelem průběhu; uprostřed orámované video s kotvou překryvu na paraglidistovi a stopou prstu za ní; dole Recording… 2.5 s of 5.0 s a volby Steps, Smooth, ½× a 1×." %}

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

## Steps, nebo Smooth {#steps-or-smooth}

Vyber, jak má video při kreslení pokračovat; mobiCut si volbu pamatuje:

- **Steps** (po krocích): video poskočí vždy o čtvrt sekundy, když se prst hýbe, a počká, když se
  zastaví. Pomalé a přesné, dobré na rychlé nebo trhané objekty.
- **Smooth** (plynule): video hraje rychlostí **½×** nebo **1×**, dokud se prst hýbe, a zastaví se,
  když se zastaví on. Přirozené pro paraglidisty a lyžaře na plynulé dráze. Prst je vždy kousek
  za tím, co vidíš, a tak v Smooth mobiCut každý bod posune o něco dřív, aby to vyrovnal.

## Po nahrání {#after-capturing}

{% include screen.html name="path-row" alt="Text s nahranou dráhou slabě nakreslenou přes video a karta Motion posunutá dolů: Path: 5.0 s recorded s tlačítkem přehrát, Clear path, Capture again a Follow path from…." %}

Karta **Motion** teď ukazuje **Path: 5.0 s recorded** a nabízí:

- **▶**: přehrát,
- **Clear path**: překryv zase zůstane na jednom místě,
- **Capture again**: nakreslit novou.

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
ještě jednou.

## Free a Pro {#free-and-pro}

Sledování dráhy je **Pro**; ve verzi Free má řádek **Follow something moving** odznak **PRO**.
Dráhy zůstanou po přepnutí na Free uložené: překryv jen zůstane na místě a s Pro po dráze zase
pojede. Viz [Free a Pro]({{ "/cs/editions/" | relative_url }}).
