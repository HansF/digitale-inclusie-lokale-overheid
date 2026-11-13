---
name: toegankelijkheidsaudit
license: CC-BY-NC-SA-4.0
description: Voer een toegankelijkheidsaudit uit op een website, formulier, app, document of loket. Gebruik wanneer iemand vraagt "is onze website toegankelijk", "check ons formulier", "WCAG-audit" of "onze dienstverlening is niet bruikbaar voor iedereen".
---

# Skill: toegankelijkheidsaudit

Deze skill leidt je door een **praktische toegankelijkheidsaudit**: van scope en testplan tot een rapport dat je bestuur kan gebruiken om te herstellen en te verankeren.

**Tijd:** 1-3 weken voor een website of formulier; 1 dag voor een quick scan van één pagina.
**Output:** een auditrapport met bevindingen, ernst, bewijs, aanbeveling, verantwoordelijke en termijn.

---

## Wanneer gebruiken

- Een bestuur lanceert een nieuwe website, app of formulier.
- Inwoners of medewerkers melden dat iets niet werkt.
- Een bestuur wil voldoen aan WCAG 2.2 AA of de European Accessibility Act.
- Een bestek moet toegankelijkheid afdwingen.
- Een digipunt of loket wil fysiek toegankelijker worden.

## Inputs

1. Scope: welke pagina's, formulieren, apps, documenten of loketten?
2. Toegang: testaccounts, staging-omgeving, contentbeheer.
3. Standaard en niveau (meestal WCAG 2.2 AA).
4. Beschikbare gebruikers met een beperking of belangenorganisaties.
5. Deadline en gewenste rapportvorm.

---

## Stap 1 — Scope en standaard bepalen

Baken af:

- **Top-taken** — de 5-10 taken die inwoners het meest doen (itsme, aanvraag, afspraak, melding, betaling).
- **Kanalen** — website, formulier, app, PDF, e-mail, telefoon, loket.
- **Componenten** — navigatie, zoekfunctie, formulier, login, betaalstap.
- **Standaard** — WCAG 2.2 AA, aangevuld met klare taal en gebruiksvriendelijkheid.

**Advies:** audit niet "de hele website" als je weinig tijd hebt. Kies de top-taken en de componenten die iedereen gebruikt.

## Stap 2 — Voorbereiding

- Verzamel URL's, testaccounts en reproductiestappen.
- Zet een testomgeving klaar die lijkt op productie.
- Voorzie een toetsenbord, een schermlezer (NVDA, VoiceOver), een contrastmeter en zoom.
- Nodig minstens twee gebruikers met een beperking uit.
- Spreek af wie herstelt en wie het rapport ontvangt.

## Stap 3 — Vier testlagen

| Laag | Wat je test | Wie |
| :--- | :--- | :--- |
| **Automatisch** | Ontbrekende alt-tekst, contrast, labels, koppenstructuur | Iedereen |
| **Handmatig** | Toetsenbord, zoom 200%, focus, schermlezer, formulieren | Auditor |
| **Gebruikerstest** | Echte taken met echte gebruikers | Gebruikers met een beperking |
| **Inhoud** | Klare taal, structuur, alternatieven, foutmeldingen | Communicatie en jurist |

**Let op:** automatische tools vinden ongeveer **een derde** van de problemen. Ze zijn een startpunt, geen audit.

### 3.1 Handmatige checklist

- [ ] Alles bereikbaar met **toetsenbord**, zonder muis.
- [ ] **Focus** is zichtbaar op elk element.
- [ ] **Zoom 200%** zonder verlies van inhoud of functie.
- [ ] **Contrast** minstens 4,5:1 voor gewone tekst en 3:1 voor grote tekst.
- [ ] **Klikdoelen** minstens 44 bij 44 pixels.
- [ ] **Koppen** in logische volgorde (H1, H2, H3).
- [ ] **Alt-tekst** bij betekenisvolle afbeeldingen; decoratieve beelden genegeerd.
- [ ] **Formulieren** hebben zichtbare labels, geen placeholder als enig label.
- [ ] **Foutmeldingen** zeggen wat er mis is en wat je moet doen.
- [ ] **Video** heeft ondertitels; **audio** heeft een transcript.
- [ ] **Geen tekst in afbeeldingen** zonder tekstalternatief.
- [ ] **Taal** van de pagina is correct ingesteld.
- [ ] **Geen tijdslimiet** zonder mogelijkheid om te verlengen.
- [ ] **Beweging** kan worden gepauzeerd of uitgezet.
- [ ] **Links** zijn beschrijvend ("Download het reglement, pdf, 120 kB").

## Stap 4 — Bevindingen registreren

Noteer per bevinding:

1. **Locatie** — pagina, component, stap.
2. **Wat** — wat werkt niet, voor wie?
3. **Ernst** — kritiek, hoog, middel, laag.
4. **Bewijs** — screenshot, foutcode, reproductiestappen.
5. **Aanbeveling** — wat moet er gebeuren?
6. **Verantwoordelijke** — wie lost het op?
7. **Termijn** — tegen wanneer?

### Ernst schalen

| Ernst | Betekenis | Voorbeeld |
| :--- | :--- | :--- |
| **Kritiek** | Taak is onmogelijk voor een groep | Formulier niet te verzenden met schermlezer |
| **Hoog** | Taak is zeer moeilijk of riskant | itsme-stap zonder alternatief |
| **Middel** | Taak lukt, maar met veel moeite | Slecht contrast, onduidelijke foutmelding |
| **Laag** | Kleine hinder of cosmetisch | Onduidelijke linktekst |

## Stap 5 — Prioriteren

Gebruik de impact-haalbaarheidsmatrix:

|  | Hoge impact | Lage impact |
| :--- | :--- | :--- |
| **Haalbaar** | Meteen doen | Later |
| **Moeilijk** | Inplannen met budget | Schrappen of accepteren |

**Advies:** herstel eerst **kritieke** en **hoog**-bevindingen op de top-taken. Dat levert het meeste op voor de minste moeite.

## Stap 6 — Herstel en hertest

- Koppel elke bevinding aan een ticket en een eigenaar.
- Voorzie een **hersteltermijn** per ernst.
- Hertest na herstel, met dezelfde methode.
- Noteer wat **nog niet** conform is in de toegankelijkheidsverklaring.

## Stap 7 — Verankeren

Een audit is een momentopname. Veranker toegankelijkheid:

- **beleid** — toegankelijkheidsverklaring en interne richtlijn;
- **proces** — toegankelijkheid als vaste stap in elk project en elke release;
- **rollen** — een verantwoordelijke en een aanspreekpunt;
- **budget** — middelen voor audits, herstel en opleiding;
- **cultuur** — bewustzijn bij contentmakers, ontwikkelaars en inkopers;
- **inkoop** — WCAG 2.2 AA in specificaties, gunningscriteria en uitvoeringsvoorwaarden;
- **klachtenprocedure** — melden per e-mail, telefoon of formulier, met ontvangstbevestiging, termijn en opvolging;
- **monitoring** — jaarlijkse audit en rapportage aan college en raad.

---

## Output

- Auditrapport met scope, methode, bevindingen en bewijs.
- Prioriteitenlijst met eigenaar en termijn.
- Ingevulde `materiaal/toegankelijkheidschecklist.md`.
- Concept toegankelijkheidsverklaring.
- Voorstel voor klachtenprocedure.
- Plan voor hertest en verankering.

## Kwaliteitscheck

- [ ] De scope en standaard zijn expliciet.
- [ ] Minstens de vier testlagen zijn gebruikt.
- [ ] Elke bevinding heeft bewijs en een reproductiestap.
- [ ] De ernst is onderbouwd vanuit de gebruiker, niet vanuit de techniek.
- [ ] Gebruikers met een beperking zijn betrokken.
- [ ] Elke bevinding heeft een eigenaar en een termijn.
- [ ] Er is een hertest voorzien.
- [ ] Het rapport is leesbaar voor een niet-technische lezer.
- [ ] Toegankelijkheid is verankerd in proces en inkoop.
- [ ] Er is een klachtenprocedure.

## Veelgemaakte fouten

- Alleen automatische tools gebruiken.
- WCAG verwarren met gebruiksvriendelijkheid.
- Geen gebruikerstest met mensen met een beperking.
- PDF's publiceren zonder tags of alt-tekst.
- Formulieren zonder offline of telefonisch alternatief.
- Een loket sluiten zonder click-call-connect.
- Geen verantwoordelijke voor toegankelijkheid.
- Een audit als eenmalig project zien.
- Alleen technische bevindingen rapporteren en de inhoud vergeten.
- Herstel niet opvolgen.

---

**Gebruik ook:** `kennis/09-toegankelijke-dienstverlening.md`, `kennis/04-beleid-en-regelgeving.md`, `materiaal/toegankelijkheidschecklist.md`, agent `toegankelijkheidsauditor`.
