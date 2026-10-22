---
title: Instalace
nav_order: 2
---

# Instalace
{: .no_toc }

Dokud mobiCut není na Google Play, instaluje se ze **souboru APK**, instalačního balíčku aplikace
pro Android. Každé nové sestavení aplikace se zveřejní automaticky a jeden stálý odkaz vždy vede
na to nejnovější.

1. TOC
{:toc}

---

## Než začneš

- Telefon s **Androidem 10 nebo novějším**.
- Asi 70 MB volného místa na stažení a aplikaci, plus místo na exportovaná videa.
- Povolení instalovat aplikace z prohlížeče (Android se na něj poprvé zeptá, viz níže).

## Instalace nejnovějšího sestavení

{% include downloads.html %}

1. **V telefonu** otevři v prohlížeči (Chrome, Firefox, …) tento odkaz:

   [**Stáhnout nejnovější APK mobiCutu**]({{ site.apk_url }}){: .btn .btn-primary }

   Soubor se jmenuje `mobicut.apk` (asi 65 MB). Všechna sestavení najdeš i na
   [stránce vydání](https://github.com/bme327/mobicut-public/releases).

2. Po stažení klepni na **Otevřít** v oznámení nebo v liště stahování prohlížeče.
   Později ho najdeš i v aplikaci **Soubory** ve složce **Stažené soubory**.

3. Poprvé Android oznámí, že prohlížeč nesmí instalovat aplikace.
   Klepni na **Nastavení**, zapni **Povolit z tohoto zdroje** a vrať se zpět.

4. Klepni na **Instalovat**.

5. Pokud **Google Play Protect** upozorní, že aplikaci nezná, klepni na **Další podrobnosti →
   Přesto nainstalovat**. Objeví se to proto, že sestavení zatím není z Obchodu Play.

6. Klepni na **Otevřít**. mobiCut se spustí na seznamu projektů, který je napoprvé prázdný.

{% include screen.html name="home-empty" alt="Úvodní obrazovka mobiCutu bez projektů: 'No projects yet' a tlačítko New project." caption="První spuštění: zatím žádné projekty." %}

## Aktualizace {#updating}

Otevři stejný odkaz znovu a nainstaluj. **Nové sestavení se nainstaluje přes staré a zachová
všechny tvoje projekty**, protože všechna sestavení jsou podepsaná stejným klíčem.

{: .note }
> Kvůli aktualizaci není potřeba mobiCut odinstalovat. Pokud ho přesto odinstaluješ, v části
> [Odinstalace](#uninstalling) najdeš, jak si projekty zachovat.

Kterou verzi máš, zjistíš na úvodní obrazovce v **⚙ Settings**; verze je dole (například
*mobiCut {{ site.app_version }}*).

## Odinstalace {#uninstalling}

Podrž ikonu mobiCutu → **Informace o aplikaci** → **Odinstalovat**.

- **Chceš-li si projekty zachovat**, zaškrtni v dialogu odinstalace **Zachovat data aplikace**.
  Po nové instalaci mobiCutu budou projekty zpátky.
- Projekty se ukládají i do tvé **zálohy Google**, takže se přenesou i do nového telefonu.
- Po přeinstalaci nebo v novém telefonu může projekt hlásit, že
  [nemůže najít své video]({{ "/cs/operations/missing-video/" | relative_url }}). Vyber znovu stejné
  video a všechny úpravy zůstanou.

Exportovaná videa zůstanou v `Movies/MobiCut` v každém případě.

## Řešení potíží

| Co vidíš | Co udělat |
|---|---|
| *Aplikace nebyla nainstalována* / *balíček je v konfliktu s existujícím balíčkem* | Už je nainstalované sestavení podepsané jinak (vzácné). Nejdřív ho odinstaluj. |
| *Při analýze balíčku došlo k problému* | Stahování se nedokončilo. Smaž `mobicut.apk` ze Stažených souborů a stáhni ho znovu. |
| Tlačítko **Instalovat** nic nedělá | Zavři jiné aplikace, které kreslí přes obrazovku (bubliny, ztmavovače obrazovky), a zkus to znovu. |

Něco jiného? [Nahlas chybu]({{ "/cs/feedback/" | relative_url }}) se snímkem své verze a postupem, který k ní vede.
