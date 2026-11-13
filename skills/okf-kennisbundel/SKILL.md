---
type: skill
name: okf-kennisbundel
license: CC-BY-NC-SA-4.0
description: Voeg een kennisdocument of sjabloon toe aan de kennisbank volgens de Open Knowledge Format-specificatie (OKF v0.2), met frontmatter, bronnen, index en wijzigingslog. Gebruik wanneer iemand vraagt "voeg dit toe aan de kennisbank", "maak een nieuw kennisdocument", "zet dit in OKF", "de kennisbank is niet conform" of "de validator faalt".
---

# Skill: okf-kennisbundel

De kennisbank in deze repo is geen map met losse markdown. `kennis/` en `materiaal/` zijn twee **OKF-bundels**: elk document is een concept met frontmatter, elk bundel heeft een vaste ingang (`index.md`) en een wijzigingslog (`log.md`), en verwijzingen zijn markdown-links.

Deze skill bewaakt die structuur wanneer je iets toevoegt of wijzigt.

## Wanneer gebruiken

- Je voegt een kennisdocument of sjabloon toe.
- Je wijzigt een bestaand document zo grondig dat titel, beschrijving, tags of bronnen niet meer kloppen.
- `python3 tests/validate_okf.py` of `okflint validate` faalt.
- Iemand vraagt de kennisbank als overdraagbare kennisbundel te publiceren of te valideren.

## Inputs

- De inhoud, of een bestaand document dat je wil omzetten.
- De bronnen met URL. Zonder URL geen `sources`-item: verzin er geen.
- Of het een kennisdocument, sjabloon, canvas, checklist of draaiboek is.

## Stap 1 — Kies het juiste `type`

`type` is het enige verplichte veld en bepaalt hoe een lezer het document benadert:

| Type | Gebruik voor |
| :--- | :--- |
| `kennisdocument` | Achtergrond, cijfers, beleid, doelgroepen, modellen |
| `bronnenregister` | Een document dat zelf alleen bronnen oplijst |
| `sjabloon` | Een document dat de gebruiker invult |
| `draaiboek` | Een stapsgewijze uitvoering met fasen en beslissingen |
| `checklist` | Een afvinkbare controle |
| `canvas` | Een werksjabloon voor een workshop of analyse |

Twijfel je? Kies `kennisdocument` en splits later. Een verkeerd type is geen fout in de validatie, maar wel een slechte ingang.

## Stap 2 — Schrijf de frontmatter

```yaml
---
type: kennisdocument
title: "Korte titel zonder nummer"
description: "Eén zin: wat staat erin en wanneer gebruik je het."
tags: [thema, thema, thema]
stale_after: 2027-06-30T00:00:00Z
sources:
  - resource: "https://voorbeeld.be/pagina"
    title: "Titel van de bron"
---
```

Regels:

- `title` is de menselijke titel; het cijfer in de bestandsnaam hoort er niet in.
- `description` is één zin en begint met het zelfstandig naamwoord, niet met "Dit document".
- `tags` zijn korte, kebab-case thema's, drie tot vijf.
- `stale_after` zet je alleen op inhoud die verandert: cijfers, beleid, financiering, bronnen. Denk aan een half jaar tot een jaar.
- `sources` bevat alleen URL's die **in de tekst zelf** voorkomen. Kopieer geen bronnen uit een ander document "voor de volledigheid".
- `generated` en `verified` laat je weg tenzij je de auteur kent en het document echt hebt nagekeken. Een onterechte `verified` is erger dan geen.

## Stap 3 — Schrijf de body

- Begin met één `# `-kop. De frontmatter is de metadata, de body is de inhoud.
- Verwijs naar een ander document met een link, niet met een backtick-pad:
  - binnen dezelfde bundel: `[kennis/07-digipunten.md](./07-digipunten.md)`
  - naar de andere bundel: `[materiaal/bouwstenen-canvas.md](../materiaal/bouwstenen-canvas.md)`
- Verwijs naar een skill met `` `skills/<id>/SKILL.md` `` in backticks: dat is een werkwijze, geen kennisconcept.
- Voeg bij elk cijfer de bron en de peildatum toe in de tekst, ook als de URL al in `sources` staat.

## Stap 4 — Werk de bundel bij

1. Zet het document in `index.md` van de bundel, met de beschrijving uit de frontmatter.
2. Voeg een regel toe aan `log.md` onder de datum van vandaag, bovenaan. Bestaat die datum nog niet, maak dan een nieuwe `## YYYY-MM-DD`-kop.
3. Verwijder je een document, dan haal je het uit `index.md` en meld je het in `log.md`. Een verdwenen document laat je niet stil verdwijnen.

## Stap 5 — Valideer

```bash
python3 tests/validate_okf.py     # eigen controle, dependency-vrij
okflint validate                   # strengere linter, leest okf-base.yaml
```

Beide moeten slagen. `okflint` is optioneel; installeer het met `uv tool install okflint`.

Wat de controles afdwingen: elk concept heeft een `type`, `index.md` bevat alle concepten, `log.md` staat met de nieuwste datum bovenaan, links wijzen naar bestaande bestanden, en verstreken `stale_after`-data geven een waarschuwing.

## Output

- Het nieuwe of gewijzigde concept met volledige frontmatter.
- Een bijgewerkte `index.md` en `log.md`.
- De uitvoer van beide validaties, met nul fouten.
- Bij twijfel over een bron: een expliciete vraag aan de gebruiker in plaats van een verzonnen URL.

## Kwaliteitscheck

- [ ] Heeft elk nieuw bestand een `type`, `title` en `description`?
- [ ] Komt elke URL in `sources` ook echt in de tekst voor?
- [ ] Staat het document in `index.md`?
- [ ] Staat de wijziging in `log.md` met de juiste datum?
- [ ] Zijn de verwijzingen links geworden, en werken ze?
- [ ] Geven beide validaties nul fouten?
- [ ] Heb ik `verified` weggelaten omdat niemand het echt heeft nagekeken?

## Veelgemaakte fouten

- **Frontmatter vergeten bij een nieuw bestand.** Dan faalt de controle met "geen YAML-frontmatter". Voeg de frontmatter toe, ook bij een kort document.
- **Bronnen aanvullen met URL's die niet in de tekst staan.** Dat geeft schijnprovenance. Zet de bron in de tekst, dan in `sources`.
- **Het document wel in de map zetten maar niet in `index.md`.** De controle waarschuwt, maar een agent vindt het document dan niet terug.
- **`stale_after` op alles zetten.** Een denkkader veroudert niet in zes maanden; een subsidiebedrag wel.
- **Frontmatter laten staan in een sjabloon dat je aan de gebruiker geeft.** Verwijder de metadata zodra het sjabloon een echt document wordt.

## Referenties

- Specificatie: [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format) en [agentskills.io](https://agentskills.io/specification) voor de skill-specificatie.
- Bundelmanifest: `okf-base.yaml` in de repo-root; daar staan de roots, de reservemapbestanden en de profieltypes in.
- Werkafspraken: `AGENTS.md`, sectie 9.
