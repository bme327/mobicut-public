---
title: Funkce
nav_order: 4
has_children: true
permalink: /cs/operations/
---

# Funkce

Každá stránka níže popisuje jednu věc, kterou v mobiCutu uděláš. Jsi-li tu nový, začni
**Projekty** a pak **Editorem**, kde je prohlídka obrazovky.

## Editor na první pohled

{% include screen.html name="editor" alt="Obrazovka editoru s očíslovanými značkami u každé oblasti." %}

1. **Název projektu a údaje o videu.** Klepnutím [přejmenuješ]({{ "/cs/operations/projects/#rename-a-project" | relative_url }}).
2. **Export**: vytvoří hotové video. Viz [Export]({{ "/cs/operations/export/" | relative_url }}).
3. **Náhled.** Ukazuje video tak, jak bude vypadat: smazané části se přeskakují, rychlost,
   přechody a titulky jsou použité. Klepnutím na titulek ve videu ho umístíš a nastavíš mu vzhled.
   Štítek v rohu ukazuje rychlost vybraného úseku.
4. **Přehrát / pozastavit**, kolem toho **na začátek**, **o 5 s zpět**, **o 5 s vpřed** a **na konec**.
   Malé časy vedle ukazují pozici (nahoře) a délku (dole) *hotového* videa, ne originálu.
5. **Zpět** (Undo) vrátí poslední změnu.
6. **Časová osa.** Každý blok je úsek; oranžové značky jsou střihy; bílá čára je přehrávací
   hlava. Viz [Editor]({{ "/cs/operations/editor/" | relative_url }}).
7. **Stopa titulků.** Modré štítky jsou titulky: klepnutím titulek upravíš, tažením ho posuneš
   v čase. Viz [Titulky]({{ "/cs/operations/subtitles/" | relative_url }}).
8. **Zobrazit smazané, oddálit, posuvník, přiblížit.**
9. **Nástroje:** [Split]({{ "/cs/operations/split/" | relative_url }}),
   [Delete / Restore]({{ "/cs/operations/delete/" | relative_url }}),
   [Speed]({{ "/cs/operations/speed/" | relative_url }}),
   [Mute]({{ "/cs/operations/mute/" | relative_url }}),
   [Subtitle]({{ "/cs/operations/subtitles/" | relative_url }}) a **Add**.

## Add: obrázky, hudba, další videa

**Add** (poslední nástroj) přidá do projektu další obsah:

{% include screen.html name="add" alt="Panel Add: Picture at the pointer, Soundtrack at the pointer, Video from Gallery a Video from files (PRO)." %}

- [Picture at the pointer]({{ "/cs/operations/pictures/" | relative_url }}): statický nebo pohyblivý obrázek vložený do videa.
- [Soundtrack at the pointer]({{ "/cs/operations/soundtracks/" | relative_url }}): hudba pod videem, ve vlastní stopě.
- [Video from Gallery / from files]({{ "/cs/operations/videos/" | relative_url }}): další video na konec časové osy (Pro).
