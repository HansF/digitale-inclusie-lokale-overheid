---
type: checklist
title: "Toegankelijkheidschecklist"
description: "Checklist voor website, formulieren en dienstverlening op basis van de vier WCAG-principes en klare taal."
tags: [toegankelijkheid, wcag, checklist]
---

# Toegankelijkheidschecklist — website, formulieren en dienstverlening

Deze checklist helpt je om de toegankelijkheid van je digitale dienstverlening te beoordelen. Ze is gebaseerd op de vier WCAG-principes en aangevuld met klare taal, click-call-connect en gebruikerstesten.

**Gebruik:** vul per onderdeel in. Noteer bewijs (screenshot, URL, testresultaat) en een verantwoordelijke.

> **Belangrijk:** deze checklist is een **praktisch hulpmiddel**, geen formele audit. Voor een wettelijke audit heb je een gespecialiseerde auditor en een volledige WCAG-test nodig.

---

## 0. Scope

| Veld | Invulling |
| :--- | :--- |
| Organisatie | |
| Website / app / formulier | |
| Verantwoordelijke | |
| Datum | |
| Uitgevoerd door | |
| Standaard | WCAG 2.2 AA |
| Gebruikte tools | |

---

## 1. Waarneembaar

### 1.1 Tekstalternatieven

- [ ] Alle afbeeldingen hebben een **alt-tekst** die de functie beschrijft.
- [ ] Decoratieve afbeeldingen hebben een **lege alt-tekst** (`alt=""`).
- [ ] Iconen met een functie hebben een **tekstalternatief**.
- [ ] Grafieken en kaarten hebben een **tekstuele samenvatting**.
- [ ] Complexe afbeeldingen hebben een **lange beschrijving**.

### 1.2 Video en audio

- [ ] Video’s hebben **ondertitels**.
- [ ] Audio heeft een **transcript**.
- [ ] Er is een **gebarentolk** of tekstalternatief waar nodig.
- [ ] Er is geen **flitsende content** die aanvallen kan uitlokken.

### 1.3 Structuur

- [ ] De pagina heeft een **duidelijke H1**.
- [ ] Koppen volgen een **logische hiërarchie** (H1 → H2 → H3).
- [ ] Lijsten zijn **echte lijsten**, geen losse streepjes.
- [ ] Tabellen hebben **kolomkoppen**.
- [ ] De leesvolgorde is **logisch**.

### 1.4 Kleur en contrast

- [ ] Contrast tekst/achtergrond is minstens **4,5:1**.
- [ ] Contrast grote tekst is minstens **3:1**.
- [ ] Informatie wordt **niet alleen via kleur** overgebracht.
- [ ] Links zijn **niet alleen door kleur** te onderscheiden.
- [ ] Er is een **hoog contrast-modus** of de site werkt met systeeminstellingen.

### 1.5 Aanpassing

- [ ] De pagina werkt bij **200% zoom**.
- [ ] De tekst is **schaalbaar**.
- [ ] De pagina werkt in **portret en landschap**.
- [ ] De inhoud blijft leesbaar bij **groot lettertype**.

---

## 2. Bedienbaar

### 2.1 Toetsenbord

- [ ] Alles is bereikbaar met **alleen een toetsenbord**.
- [ ] De **tab-volgorde** is logisch.
- [ ] De **focusindicator** is zichtbaar.
- [ ] Er zijn geen **toetsenbordvallen**.
- [ ] Sneltoetsen kunnen worden **uitgezet**.

### 2.2 Muis en aanraking

- [ ] Klikdoelen zijn minstens **44 bij 44 pixels**.
- [ ] Er is **geen sleepbeweging** nodig zonder alternatief.
- [ ] Er is **geen dubbele klik** nodig.
- [ ] De pagina werkt met **aanraking**.

### 2.3 Tijd

- [ ] Er zijn **geen tijdslimieten**, of ze kunnen worden verlengd.
- [ ] Sessies verlopen **niet zonder waarschuwing**.
- [ ] Er is **geen automatische vernieuwing** die de gebruiker stoort.

### 2.4 Beweging

- [ ] Er is **geen automatisch bewegende content** zonder pauzeknop.
- [ ] Animaties kunnen worden **uitgezet**.
- [ ] Er is **geen parallax** die duizelig maakt.
- [ ] `prefers-reduced-motion` wordt gerespecteerd.

### 2.5 Navigatie

- [ ] Er is een **duidelijke navigatie**.
- [ ] Er is een **zoeksfunctie**.
- [ ] Er is een **skip-link** naar de hoofdinhoud.
- [ ] De **huidige pagina** is aangeduid.
- [ ] Er zijn **geen verrassende contextwissels**.

---

## 3. Begrijpelijk

### 3.1 Taal

- [ ] De **pagina taal** is ingesteld (`lang="nl"`).
- [ ] **Anderstalige stukken** zijn aangeduid.
- [ ] De tekst is in **klare taal**.
- [ ] **Afkortingen** worden uitgelegd.
- [ ] **Jargon** wordt vermeden of uitgelegd.
- [ ] Er is een **woordenlijst** waar nodig.

### 3.2 Leesbaarheid

- [ ] Zinnen zijn **kort** (gemiddeld 10-15 woorden).
- [ ] Alinea’s zijn **kort**.
- [ ] De belangrijkste info staat **vooraan**.
- [ ] Er zijn **tussenkopjes**.
- [ ] Er is **geen tekst in hoofdletters** voor lange stukken.
- [ ] Er is **geen cursieve of onderstreepte** lopende tekst.

### 3.3 Voorspelbaarheid

- [ ] De navigatie is **consistent**.
- [ ] Dezelfde functie heeft **dezelfde naam**.
- [ ] Formulieren vragen **geen onverwachte acties**.
- [ ] **Geen automatische wijziging** van context bij focus.

### 3.4 Foutpreventie en hulp

- [ ] Formulieren hebben **duidelijke labels**.
- [ ] Verplichte velden zijn **aangeduid**.
- [ ] **Foutmeldingen** zeggen wat er fout is en wat je moet doen.
- [ ] Er is **hulp** bij het formulier (telefoon, uitleg).
- [ ] Er is een **bevestiging** voor definitieve acties.
- [ ] Er is een **offline alternatief**.

---

## 4. Robuust

### 4.1 Techniek

- [ ] De HTML is **semantisch**.
- [ ] **ARIA** wordt alleen gebruikt waar nodig en correct.
- [ ] De pagina werkt in **verschillende browsers**.
- [ ] De pagina werkt met **schermlezers** (NVDA, VoiceOver, TalkBack).
- [ ] De pagina werkt met **vergrotingssoftware**.
- [ ] De pagina werkt met **spraakbediening**.

### 4.2 Formulieren

- [ ] Elk veld heeft een **programmatisch label**.
- [ ] **Foutmeldingen** zijn gekoppeld aan het veld.
- [ ] **Instructies** zijn gekoppeld aan het veld.
- [ ] **Autocomplete** is correct ingesteld.
- [ ] **Geen CAPTCHA** zonder alternatief.
- [ ] **Geen tijdslimiet** op het invullen.

### 4.3 Documenten

- [ ] PDF’s zijn **getagd**.
- [ ] PDF’s hebben **alt-tekst**.
- [ ] PDF’s hebben een **leesvolgorde**.
- [ ] Er is een **HTML-alternatief** voor belangrijke PDF’s.
- [ ] Documenten hebben een **duidelijke titel**.

---

## 5. Klare taal

- [ ] De tekst is **getest met echte lezers**.
- [ ] Het leesniveau is **B1 of eenvoudiger** voor algemene info.
- [ ] Het leesniveau is **A2** voor cruciale info.
- [ ] Er is **geen jargon** zonder uitleg.
- [ ] Er zijn **voorbeelden** bij abstracte begrippen.
- [ ] Er is **geen ambtelijke taal**.
- [ ] De **je-vorm** wordt gebruikt waar passend.
- [ ] **Afkortingen** zijn uitgelegd.
- [ ] **Engelse termen** zijn vermeden of uitgelegd.

---

## 6. Click-call-connect

- [ ] Elk digitaal formulier vermeldt een **telefoonnummer**.
- [ ] Elk digitaal formulier vermeldt een **fysiek loket**.
- [ ] Er is **hulp aan het loket**.
- [ ] Er is **doorverwijzing naar een digipunt**.
- [ ] Er is **geen loket gesloten** zonder alternatief.
- [ ] De **wachttijd** aan de telefoon is redelijk.
- [ ] De **openingsuren** zijn afgestemd op werkenden.
- [ ] Er is **geen verplichte app** zonder alternatief.
- [ ] Er is **geen verplicht account** zonder alternatief.

---

## 7. Gebruikerstesten

- [ ] Er is getest met **mensen met een visuele beperking**.
- [ ] Er is getest met **mensen met een motorische beperking**.
- [ ] Er is getest met **mensen met een cognitieve beperking**.
- [ ] Er is getest met **anderstaligen**.
- [ ] Er is getest met **digistarters**.
- [ ] Er is getest op **een smartphone**.
- [ ] Er is getest met **een slechte verbinding**.
- [ ] De bevindingen zijn **gedocumenteerd** en **opgevolgd**.

---

## 8. Organisatie

- [ ] Er is een **toegankelijkheidsverklaring**.
- [ ] Er is een **verantwoordelijke** voor toegankelijkheid.
- [ ] Er is een **klachtenprocedure**.
- [ ] Er is een **termijn** voor antwoord op klachten.
- [ ] Toegankelijkheid is opgenomen in **bestekken**.
- [ ] Toegankelijkheid is opgenomen in **gunningscriteria**.
- [ ] Er is een **jaarlijkse audit**.
- [ ] Er is **budget** voor herstel en opleiding.
- [ ] Contentmakers krijgen **opleiding klare taal**.
- [ ] Ontwikkelaars krijgen **opleiding WCAG**.

---

## 9. Prioritering van bevindingen

| Bevinding | Ernst | Impact | Inspanning | Prioriteit | Verantwoordelijke | Termijn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | ☐ Kritiek ☐ Hoog ☐ Midden ☐ Laag | | | | | |

**Ernst:**

- **Kritiek:** blokkeert toegang voor een groep.
- **Hoog:** ernstige drempel, geen alternatief.
- **Midden:** drempel met workaround.
- **Laag:** verbetering van gebruiksvriendelijkheid.

---

## 10. Rapport

Een bruikbaar rapport bevat:

1. **Scope** en **methode**.
2. **Samenvatting** in één pagina.
3. **Bevindingen** per pagina of component.
4. **Bewijs** (screenshot, foutcode, reproductiestappen).
5. **Ernst** en **prioriteit**.
6. **Aanbeveling** en **termijn**.
7. **Verantwoordelijke**.
8. **Bijlagen** (testscripts, tools, deelnemers).

---

## 11. Snelle prioriteitenlijst

Begin met deze tien, als je niet alles tegelijk kan aanpakken:

1. **Contrast** verhogen.
2. **Alt-tekst** toevoegen.
3. **Koppenstructuur** herstellen.
4. **Formulierlabels** toevoegen.
5. **Foutmeldingen** verduidelijken.
6. **Toetsenbordnavigatie** herstellen.
7. **Focusindicator** zichtbaar maken.
8. **PDF’s** taggen of vervangen door HTML.
9. **Ondertitels** toevoegen.
10. **Telefoonnummer** toevoegen aan elk formulier.

---

**Verder lezen:** [kennis/09-toegankelijke-dienstverlening.md](../kennis/09-toegankelijke-dienstverlening.md), [kennis/04-beleid-en-regelgeving.md](../kennis/04-beleid-en-regelgeving.md), skill `toegankelijkheidsaudit`.
