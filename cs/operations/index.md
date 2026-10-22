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
   přechody, texty a grafika jsou použité. Klepnutím na text nebo grafiku ve videu je umístíš,
   natočíš a nastavíš jim vzhled.
   Štítek v rohu ukazuje rychlost vybraného úseku.
4. **Přehrát / pozastavit**, kolem toho **na začátek**, **o 5 s zpět**, **o 5 s vpřed** a **na konec**.
   Malé časy vedle ukazují pozici (nahoře) a délku (dole) *hotového* videa, ne originálu.
5. **Zpět** (Undo) vrátí poslední změnu.
6. **Časová osa.** Každý blok je úsek; oranžové značky jsou střihy; bílá čára je přehrávací
   hlava. Viz [Editor]({{ "/cs/operations/editor/" | relative_url }}).
7. **Stopa překryvů.** Modré štítky jsou [texty]({{ "/cs/operations/subtitles/" | relative_url }}),
   fialové [grafika]({{ "/cs/operations/graphics/" | relative_url }}): klepnutím je upravíš, tažením
   posuneš v čase.
8. **Zobrazit smazané, oddálit, posuvník, přiblížit.**
9. **Nástroje:** [Split]({{ "/cs/operations/split/" | relative_url }}),
   [Delete / Restore]({{ "/cs/operations/delete/" | relative_url }}),
   [Speed]({{ "/cs/operations/speed/" | relative_url }}),
   [Mute]({{ "/cs/operations/mute/" | relative_url }}),
   [Text]({{ "/cs/operations/subtitles/" | relative_url }}),
   [Graphic]({{ "/cs/operations/graphics/" | relative_url }}) (Pro) a **Add**.

## Add: slidy, obrázky, hudba, přechody, další videa

**Add** (poslední nástroj) přidá do projektu další obsah:

{% include screen.html name="add" alt="Panel Add: Text slide at the pointer, Picture at the pointer, Soundtrack at the pointer, Transitions at every join a Video from Gallery a Video from files (PRO)." %}

- [Text slide at the pointer]({{ "/cs/operations/text-slides/" | relative_url }}): titulní karta ze šablony vložená do videa.
- [Picture at the pointer]({{ "/cs/operations/pictures/" | relative_url }}): statický nebo pohyblivý obrázek vložený do videa.
- [Soundtrack at the pointer]({{ "/cs/operations/soundtracks/" | relative_url }}): hudba pod videem, ve vlastní stopě.
- [Transitions at every join]({{ "/cs/operations/transitions/#transitions-at-every-join" | relative_url }}): jeden přechod všude, k tomu roztmívání a zatmívání.
- [Video from Gallery / from files]({{ "/cs/operations/videos/" | relative_url }}): další video na konec časové osy (Pro).
