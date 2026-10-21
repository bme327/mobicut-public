---
title: Úvod
layout: home
nav_order: 1
permalink: /cs/
---

# mobiCut

**Malý střihač videa pro Android, udělaný na rychlé úpravy akčních záběrů přímo v telefonu.**
{: .fs-6 .fw-300 }

[Nainstalovat aplikaci]({{ "/cs/installation/" | relative_url }}){: .btn .btn-primary .mr-2 }
[Co umí]({{ "/cs/operations/" | relative_url }}){: .btn .mr-2 }
[Free a Pro]({{ "/cs/editions/" | relative_url }}){: .btn }

{% include downloads.html %}

---

## K čemu mobiCut je

Přistaneš s paraglidem nebo sjedeš sjezdovku a máš dlouhé video. Většinu z něj tvoří čekání,
chůze nebo plachtění; jen pár okamžiků stojí za to sdílet. mobiCut z takového surového záznamu
udělá krátké video, ještě než dojedeš domů:

- **rozstřihneš ho na úseky** a nudné části zahodíš,
- dlouhé pasáže **zrychlíš** (až 16×) nebo nejlepší okamžik zpomalíš (až na 0,25×),
- **přidáš titulky**, kde to je a co to je,
- části **spojíš prolínačkami**, aby střihy vypadaly záměrně,
- **vložíš fotky** s pomalým přiblížením nebo vjezdem a pod to všechno **hudbu**,
- **ztlumíš** šum větru a (Pro) **spojíš víc videí** do jednoho,
- **exportuješ** nové video do galerie, připravené ke sdílení.

## Tvoje video zůstává, kde je

{: .important }
> **mobiCut tvoje zdrojové video nikdy nekopíruje, nestahuje ani nenahrává. Jen na něj odkazuje.**
> Projekt je jen seznam tvých úprav (pár kilobajtů), který ukazuje na původní soubor v galerii,
> na SD kartě nebo v kameře. Originál se nikdy nemění a projekt ze 4GB záznamu nezabere žádné
> místo navíc ani čekání.

- **Nic neopouští telefon.** mobiCut vůbec nemá přístup k internetu: žádný účet, žádný cloud,
  žádné nahrávání. Všechno se děje v zařízení.
- **Žádné kopie, které žerou místo.** Jediný nový soubor je hotové video, které exportuješ.
- Když originál přesuneš nebo smažeš, projekt tě požádá, abys
  [mu video znovu ukázal]({{ "/cs/operations/missing-video/" | relative_url }}).

## Velmi rychlý export

{: .important }
> **Export je velmi rychlý.** mobiCut vytváří hotové video přímo v telefonu pomocí jeho
> vestavěného video hardwaru, takže se nic nenahrává a nečeká se ve frontě na serveru.

- Smazané části se přeskakují, takže krátký sestřih dlouhého letu se exportuje rychle.
- Menší rozlišení (720p) nebo 30 fps export ještě zrychlí a soubor zmenší.
- Výsledek je rovnou v galerii, připravený ke sdílení.

{% include screen.html name="editor" alt="Editor mobiCutu: náhled videa nahoře, časová osa se třemi úseky, štítky titulků a dole nástroje Split, Delete, Speed, Mute, Subtitle a Add." caption="Editor, kde se odehrává všechna práce." %}

## Jak to funguje, za minutu

1. Založ **projekt** z videa v galerii, na SD kartě nebo v USB kameře.
2. Celé video je na časové ose jeden **úsek**. **Rozstřihni** ho tam, kde se něco mění.
3. Každému úseku dej, co potřebuje: **smaž** ho, změň mu **rychlost**, přidej přes něj **titulek**.
4. **Exportuj.** Nové video najdeš v galerii ve složce `Movies/MobiCut`.

Úpravy se ukládají samy, takže můžeš aplikaci zavřít a k projektu se kdykoli vrátit.

## Edice

mobiCut má dvě edice: **Free** a **Pro**.

{: .important }
> **Free bude vždy zdarma a vždy bez reklam.** Žádné reklamy v žádné edici, nikdy.
> Free je plnohodnotný střihač s několika omezeními, ne zkušební verze.

Jediná omezení Free: zdrojová videa **do 1 hodiny**, **jedno video na projekt**, malé
**logo (mc) mobiCut** v pravém horním rohu exportu a **Fade out-in** jako jediný přechod.
Pro je odstraní.

Během testování **jde Pro zapnout zdarma** v **⚙ Settings**. Po spuštění v Obchodě Play bude Pro
placené: předplatné, krátká měsíční propustka nebo jednorázový nákup.

[Porovnat Free a Pro →]({{ "/cs/editions/" | relative_url }}){: .btn .btn-outline }

## Zpětná vazba

Našel jsi chybu nebo ti něco chybí? [Nahlas chybu nebo navrhni funkci]({{ "/cs/feedback/" | relative_url }})
na GitHubu a **hlasuj 👍** pro funkce, které chceš nejvíc. U každého hlášení je vidět jeho stav:
**new**, **accepted**, **closed** po vydání, nebo **rejected** i s důvodem.

## Požadavky

- Android 10 nebo novější
- Dost volného místa na exportované video (zhruba velikost části, kterou ponecháš)

---

Tyto stránky popisují mobiCut **{{ site.app_version }}**. Obrazovky jsou kreslené ilustrace
aplikace (v angličtině, stejně jako aplikace); postupně je nahrazují skutečné snímky obrazovky.
