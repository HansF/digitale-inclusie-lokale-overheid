#!/usr/bin/env python3
"""Valideer de skills in deze repo tegen de Agent Skills-specificatie.

Gebruik:
    python3 tests/validate_skills.py            # valideer alle skills
    python3 tests/validate_skills.py skills/x   # valideer één skill

De check is bewust dependency-vrij: geen PyYAML, geen netwerk. Zo kan hij
zowel lokaal als in GitHub Actions zonder installatiestap draaien.

Gecontroleerd per skill:
  - de map bevat een SKILL.md
  - de frontmatter is geldig en bevat name, description en license
  - name is kebab-case, 1-64 tekens en gelijk aan de mapnaam
  - description is niet leeg en hoogstens 1024 tekens
  - relatieve links naar kennis/, materiaal/ of andere bestanden bestaan
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

REQUIRED_KEYS = ("name", "description", "license")
MAX_NAME_LEN = 64
MAX_DESCRIPTION_LEN = 1024


class Result:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.skills = 0

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"{where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"{where}: {message}")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Lees een eenvoudige `key: value`-frontmatter. Geen geneste YAML."""
    if not text.startswith("---\n"):
        raise ValueError("bestand begint niet met '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("frontmatter wordt niet afgesloten met '---'")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    key = None
    for line in raw.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if key is None:
                raise ValueError(f"vervolgregel zonder sleutel: {line!r}")
            data[key] += " " + line.strip()
            continue
        if ":" not in line:
            raise ValueError(f"regel zonder dubbele punt: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in (">", "|", ">-", "|-"):
            value = ""
        data[key] = value
    return data, body


def check_links(where: str, path: Path, body: str, result: Result) -> None:
    """Controleer relatieve links. Paden mogen vanaf de skillmap of de repo-root lopen."""
    for target in LINK_RE.findall(body):
        target = target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        if target.startswith(("kennis/", "materiaal/", "skills/", "templates/")):
            ok = (ROOT / target).exists()
        else:
            ok = (path.parent / target).exists()
        if not ok:
            result.warn(where, f"link wijst naar een niet-bestaand bestand: {target}")


def validate_skill(skill_dir: Path, result: Result) -> None:
    where = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        result.error(where, "geen SKILL.md gevonden")
        return
    result.skills += 1

    try:
        front, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    except ValueError as exc:
        result.error(where, f"frontmatter ongeldig: {exc}")
        return

    for key in REQUIRED_KEYS:
        if not front.get(key):
            result.error(where, f"frontmatter mist het veld '{key}'")

    name = front.get("name", "")
    if name and not NAME_RE.match(name):
        result.error(where, f"name '{name}' is geen kebab-case (a-z, 0-9, -)")
    if name and name != where:
        result.error(where, f"name '{name}' is niet gelijk aan de mapnaam '{where}'")
    if len(name) > MAX_NAME_LEN:
        result.error(where, f"name is langer dan {MAX_NAME_LEN} tekens")

    description = front.get("description", "")
    if description:
        if len(description) > MAX_DESCRIPTION_LEN:
            result.error(
                where, f"description is {len(description)} tekens, maximum is {MAX_DESCRIPTION_LEN}"
            )
        if len(description) < 40:
            result.warn(where, "description is erg kort; het model heeft weinig om op te matchen")
    if "Gebruik wanneer" not in description:
        result.warn(where, "description bevat geen 'Gebruik wanneer'; triggers ontbreken")

    if not body.strip():
        result.error(where, "SKILL.md heeft geen inhoud na de frontmatter")

    expected = ("## Wanneer gebruiken", "## Output")
    for heading in expected:
        if heading not in body:
            result.warn(where, f"vaste sectie ontbreekt: '{heading}'")

    check_links(where, skill_md, body, result)


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv[1:]] or sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not targets:
        print(f"Geen skills gevonden in {SKILLS_DIR}")
        return 1

    result = Result()
    for target in targets:
        validate_skill(target, result)

    for warning in result.warnings:
        print(f"waarschuwing  {warning}")
    for error in result.errors:
        print(f"fout          {error}")

    print(
        f"\n{result.skills} skills gecontroleerd, "
        f"{len(result.errors)} fouten, {len(result.warnings)} waarschuwingen"
    )
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
