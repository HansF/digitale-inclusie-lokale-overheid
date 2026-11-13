---
name: skill-template
description: >
  Vervang deze beschrijving. Zeg in één zin welk concreet probleem de skill
  oplost, en daarna wanneer een agent ze moet laden ("Gebruik wanneer iemand
  vraagt ..."). Houd het onder 1024 tekens.
license: CC-BY-NC-SA-4.0
---

# Skill: [naam]

Een skill is één werkwijze voor één taak. Splits liever in twee skills dan één skill alles te laten doen.

## Wanneer gebruiken

- Trigger of vraag 1.
- Trigger of vraag 2.
- Trigger of vraag 3.

## Inputs

Wat je van de gebruiker nodig hebt voor je begint. Ontbreekt het, werk dan met expliciete aannames.

## Stap 1 — [naam van de stap]

Wat je doet, welke bron je raadpleegt (verwijs naar `kennis/` of `materiaal/`) en wanneer je mag doorgaan.

## Stap 2 — [naam van de stap]

Beschrijf de tussenstappen kort en concreet.

## Output

- Document of artifact 1.
- Document of artifact 2.
- Bronnenlijst met URL en peildatum.

## Kwaliteitscheck

- [ ] Zijn aannames expliciet?
- [ ] Heeft elk cijfer een bron en een peildatum?
- [ ] Heeft elke actie een actor en een timing?
- [ ] Is er minstens één meetbare indicator?
- [ ] Zijn de niet-digitale kanalen meegenomen?

## Veelgemaakte fouten

- Fout 1, met wat je in de plaats doet.
- Fout 2, met wat je in de plaats doet.

## Referenties

Maak alleen de mappen aan die je nodig hebt:

- `references/` — achtergrond, technische documentatie of langere toelichting.
- `scripts/` — uitvoerbare hulpmiddelen.
- `assets/` — sjablonen, schema's of vaste bestanden.

Verwijs vanuit deze skill naar de gedeelde kennisbank met een pad vanaf de repo-root, bijvoorbeeld `kennis/07-digipunten.md`. Laat geen lege mappen staan.
