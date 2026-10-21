---
title: Zpětná vazba
nav_order: 5
---

# Nahlásit chybu nebo navrhnout funkci

Zpětná vazba se posílá přes [GitHub issues](https://github.com/bme327/mobicut-public/issues).
Potřebuješ bezplatný účet na GitHubu. Formuláře jsou v angličtině, ale psát můžeš i česky.

[🐞 Nahlásit chybu](https://github.com/bme327/mobicut-public/issues/new?template=bug.yml){: .btn .btn-primary .mr-2 }
[💡 Navrhnout funkci](https://github.com/bme327/mobicut-public/issues/new?template=feature.yml){: .btn .mr-2 }
[👍 Hlasovat o funkcích](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement+sort%3Areactions-%2B1-desc){: .btn }

## Hlášení chyb

Formulář chce dvě věci, díky kterým jde chybu opravit:

1. **Snímek obrazovky s verzí.** Na úvodní obrazovce klepni na **⚙ Settings**; verze je dole
   (například *mobiCut {{ site.app_version }}*). Udělej snímek a vlož ho do formuláře.

2. **Postup, jak chybu vyvolat**: přesně co jsi dělal, krok za krokem, a co jsi čekal a co se
   stalo místo toho.

{% include screen.html name="settings-edition" alt="Panel Settings; verze aplikace je dole." caption="Kde najdeš verzi: ⚙ Settings, úplně dole." %}

## Návrhy funkcí

Popiš, co by měl mobiCut umět a s čím by ti to pomohlo.

### Hlasování

**Hlasuj reakcí 👍** u návrhu (tlačítko se smajlíkem pod popisem). Seznam
[nejžádanějších funkcí](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement+sort%3Areactions-%2B1-desc)
je seřazený podle 👍 a to pořadí pomáhá rozhodnout, co přijde dál. Místo zakládání duplicit
prosím hlasuj a nepiš komentáře „+1“.

## Co se s hlášením nebo návrhem stane

Každé hlášení chyby i návrh funkce má právě jeden stavový štítek a prochází jimi takto:

<div class="lifecycle">
  <span class="label label-grey">new</span> →
  <span class="label label-green">accepted</span> →
  <span class="label label-purple">closed</span>
  <span class="lc-or">nebo</span>
  <span class="label label-grey">new</span> →
  <span class="label label-red">rejected</span>
</div>


| Stav | Význam |
|---|---|
| <span class="label label-grey">status: new</span> | Zatím neprohlédnuto |
| <span class="label label-green">status: accepted</span> | V plánu pro mobiCut; issue zůstává otevřené, dokud nevyjde |
| <span class="label label-red">status: rejected</span> | Nebude se dělat. Důvod je v komentáři a issue je zavřené jako *not planned* |
| <span class="label label-purple">status: closed</span> | Opraveno nebo hotovo a vydáno. Komentář říká, ve kterém sestavení; issue je zavřené jako *completed* |

Chyba jde **new → accepted → closed**, jakmile vyjde sestavení s opravou (nebo **rejected**,
třeba když ji nejde zopakovat). Návrh funkce jde **new → accepted → closed**, když funkce vyjde.

Zavřená i zamítnutá issues zůstávají ke čtení. Před nahlášením je prohledej, odpověď už tam může
být: [zavřené chyby](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+label%3Abug+is%3Aclosed),
[zamítnuté návrhy s důvody](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+label%3A%22status%3A+rejected%22).

{: .tip }
> Když je chyba, kterou jsi nahlásil, **closed**, závěrečný komentář uvádí sestavení s opravou.
> [Aktualizuj aplikaci]({{ "/cs/installation/#updating" | relative_url }}) a máš ji.
