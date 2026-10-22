---
title: Hudba
parent: Funkce
nav_order: 14
---

# Přidat hudbu
{: .no_toc }

Dej pod video hudbu (nebo jakýkoli zvukový soubor). Přidat můžeš víc skladeb, za sebou
i přes sebe.

1. TOC
{:toc}

---

## Přidat hudbu {#add-a-soundtrack}

1. Posuň přehrávací hlavu tam, kde má hudba začít.
2. Klepni na **Add** a pak **Soundtrack at the pointer**.
3. Vyber zvukový soubor.

Skladba začne na místě přehrávací hlavy v hotovém videu (úplně na začátku, je-li přehrávací hlava
na konci). Pod stopou překryvů se objeví **stopa hudby**: jeden zelený štítek na skladbu, s **♪**
a jejím názvem. Překrývající se skladby se ve stopě skládají nad sebe a hrají společně.

{% include screen.html name="media-timeline" alt="Editor s úsekem obrázku, ztlumeným úsekem, dvěma videi a stopou hudby se dvěma skladbami pod texty." caption="Stopa hudby (značka 4) pod texty. Značka 5 je Add." %}

Hudba patří k časové ose **hotového videa**: zůstane na svém místě, když video pod ní stříháš,
mažeš nebo zrychluješ. Co přesahuje konec videa, se **ořízne**.
Štítek zčervená, když skladba začíná až po konci videa, takže by z ní nic nezaznělo.

## Nastavení skladby {#track-settings}

Klepni na štítek skladby.

{% include screen.html name="soundtrack" alt="Dialog Soundtrack: začátek a délka, Start at the pointer, Sound Mix nebo Replace (vybráno), Volume 80 %, Fade in 2,0 s, Fade out 3,0 s, Remove soundtrack." %}

| Nastavení | Co dělá |
|---|---|
| **Starts at … · plays …** | Kde v hotovém videu začíná a jak dlouho opravdu hraje |
| **Start at the pointer** | Přesune začátek skladby k přehrávací hlavě |
| **Mix** | Hraje spolu s vlastním zvukem videa |
| **Replace** | Po dobu skladby ztlumí zvuk videa (štítek ukazuje **♪ only**) |
| **Volume** | 0–100 %, po 5 % |
| **Fade in / Fade out** | Náběh a doznění, každé 0–10 s, po 0,5 s |
| **Remove soundtrack** | Skladbu odstraní (Undo ji vrátí) |

Klepnutím na **Save** nastavení použiješ.

- **Náběh a doznění** zaberou každé nejvýš polovinu toho, co hraje. Doznění končí tam, kde
  skladba končí, což je u oříznuté skladby konec videa, takže dlouhá píseň s videem pěkně dozní.
- S **Replace** a náběhem zvuk videa slábne, jak hudba nabíhá, a na konci se stejně vrátí.
- Roztmívání a zatmívání na začátku a konci videa ([přechody]({{ "/cs/operations/transitions/" | relative_url }}))
  ovlivní vlastní zvuk videa, ne hudbu; na tu použij náběh a doznění skladby.

Náhled přehrává hudbu spolu s videem. Hudba je v obou edicích.
