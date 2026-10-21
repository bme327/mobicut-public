---
title: Projekty
parent: Funkce
nav_order: 2
---

# Projekty
{: .no_toc }

Projekt je jedno video a všechno, co jsi s ním udělal. mobiCut projekty ukládá automaticky;
úvodní obrazovka je ukazuje od nejnovějšího. (Před ní mobiCut krátce ukáže
[uvítací obrazovku]({{ "/cs/operations/welcome/" | relative_url }}).)

1. TOC
{:toc}

---

{% include screen.html name="home" alt="Úvodní obrazovka se třemi nedávnými projekty, tlačítky Settings a New project a tlačítkem nabídky ⋮ u projektu." %}

1. **Settings**: edice, zásady ochrany soukromí a verze aplikace.
2. **New project**: nový projekt.
3. **Projekt**: miniatura, délka hotového videa, počet úseků a titulků a kdy byl naposledy
   upravený. Klepnutím ho otevřeš.
4. **Nabídka ⋮**: přejmenovat nebo smazat.

## Nový projekt {#start-a-new-project}

1. Klepni na **New project**.
2. Vyber, kde video je:
   - **Gallery**: videa v tomto telefonu.
   - **Browse files**: SD karta, USB kamera nebo disk, Stažené soubory, Disk Google a další
     poskytovatelé souborů. Použij pro akční kamery připojené přes USB.
3. Vyber video. Otevře se editor a celé video je jeden úsek.

{: .note }
> V edici **Free** může mít zdrojové video **nejvýš 1 hodinu**. Delší videa potřebují
> [Pro]({{ "/cs/editions/" | relative_url }}).

{% include screen.html name="new-project" alt="Panel 'New project from…' s Gallery a Browse files." %}

{: .tip }
Začít můžeš i z jiné aplikace: v galerii video **Sdílej** a vyber **MobiCut**.

## Otevřít projekt {#open-a-project}

Klepni na něj na úvodní obrazovce. Všechny úpravy jsou tak, jak jsi je nechal. Přehrávací hlava
začíná na začátku videa, nebo hned po roztmívání, pokud se video
[na začátku roztmívá]({{ "/cs/operations/transitions/" | relative_url }}), aby se náhled neotevřel
na černém snímku. Klepnutím na **←** (nebo gestem zpět) se vrátíš na seznam; nic není potřeba
ukládat.

## Přejmenovat projekt {#rename-a-project}

Nové projekty dostanou jméno podle souboru s videem. Přejmenuješ je:

- na úvodní obrazovce přes **⋮ → Rename**, nebo
- v editoru klepnutím na název projektu nahoře.

Napiš nový název a klepni na **Rename**.

{% include screen.html name="project-menu" alt="Nabídka ⋮ projektu s Rename a Delete." %}
{% include screen.html name="rename-project" alt="Dialog Rename project s vybraným současným názvem." %}

## Smazat projekt {#delete-a-project}

Klepni na **⋮ → Delete** a potvrď. Smaže se jen projekt (tvoje úpravy). **Původní video
a všechno, co jsi exportoval, zůstane v galerii.**

{% include screen.html name="delete-project" alt="Potvrzení Delete project?." %}

## Kde co je uložené {#where-things-are-kept}

| Co | Kde |
|---|---|
| Tvoje úpravy | V aplikaci a v tvé záloze Google. Při odinstalaci zůstanou, když zaškrtneš **Zachovat data aplikace** (viz [Odinstalace]({{ "/cs/installation/#uninstalling" | relative_url }})). |
| Původní video | **Tam, kde bylo.** mobiCut na něj jen odkazuje: nikdy ho nekopíruje, nestahuje ani nenahrává. |
| Exportovaná videa | `Movies/MobiCut` (objeví se v galerii) |
| Soubory titulků (.srt) | `Download/MobiCut` |

Pokud se původní video přesune nebo smaže, viz [Chybějící video]({{ "/cs/operations/missing-video/" | relative_url }}).
