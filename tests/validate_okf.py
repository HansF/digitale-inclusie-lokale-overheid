#!/usr/bin/env python3
"""Controleer of de kennisbank en het materiaal OKF v0.2-conform zijn.

Gebruik:
    python3 tests/validate_okf.py

De check is dependency-vrij, zodat hij lokaal en in GitHub Actions zonder
installatiestap draait. Gecontroleerd wordt:

  E1  elk conceptbestand heeft YAML-frontmatter
  E2  de frontmatter heeft een niet-lege `type`
  E3  `index.md` heeft geen frontmatter behalve `okf_version`
  E4  `log.md` gebruikt ISO 8601-datumkoppen, nieuwste eerst
  W1  `title` of `description` ontbreekt
  W2  een relatieve link wijst naar een bestand dat niet bestaat
  W3  `stale_after` is verstreken
  W4  een `sources`-item heeft geen `resource`
  W5  een bestand in de bundel staat niet in `index.md`
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUNDLES = ("kennis", "materiaal")
RESERVED = ("index.md", "log.md")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

FENCE_RE = re.compile(r"```.*?```", re.S)
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """Haal codeblokken en inline code weg: daarin staan geen echte links."""
    return CODE_SPAN_RE.sub("", FENCE_RE.sub("", text))
DATE_HEADING_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})$", re.M)


class Result:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.concepts = 0
        self.sourced = 0

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"{where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"{where}: {message}")


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Geef (frontmatter, body). frontmatter is None als er geen is."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def top_level_keys(front: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in front.split("\n"):
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def source_entries(front: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    inside = False
    for line in front.split("\n"):
        if line.startswith("sources:"):
            inside = True
            continue
        if inside and line and not line.startswith((" ", "\t")):
            inside = False
        if not inside:
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            current = {}
            entries.append(current)
            stripped = stripped[2:]
        if current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip().strip('"')
    return entries


def check_links(where: str, path: Path, body: str, result: Result) -> None:
    for target in LINK_RE.findall(strip_code(body)):
        target = target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        if not (path.parent / target).exists() and not (ROOT / target).exists():
            result.warn(where, f"link naar een niet-bestaand bestand: {target}")


def check_concept(path: Path, rel: str, result: Result) -> None:
    text = path.read_text(encoding="utf-8")
    front, body = split_frontmatter(text)
    if front is None:
        result.error(rel, "E1 geen YAML-frontmatter")
        return
    keys = top_level_keys(front)
    if not keys.get("type"):
        result.error(rel, "E2 frontmatter heeft geen niet-lege 'type'")
    result.concepts += 1

    for key in ("title", "description"):
        if not keys.get(key):
            result.warn(rel, f"W1 aanbevolen veld '{key}' ontbreekt")

    sources = source_entries(front)
    if sources:
        result.sourced += 1
    for entry in sources:
        if not entry.get("resource"):
            result.warn(rel, "W4 een sources-item heeft geen 'resource'")

    stale = keys.get("stale_after", "")
    if stale:
        try:
            moment = dt.datetime.fromisoformat(stale.replace("Z", "+00:00"))
        except ValueError:
            result.warn(rel, f"W3 'stale_after' is geen ISO 8601-datum: {stale}")
        else:
            if moment < dt.datetime.now(dt.timezone.utc):
                result.warn(rel, f"W3 inhoud is verouderd volgens stale_after ({stale})")

    check_links(rel, path, body, result)


def check_index(bundle: Path, result: Result) -> set[str]:
    index = bundle / "index.md"
    rel = f"{bundle.name}/index.md"
    if not index.exists():
        result.error(rel, "E3 index.md ontbreekt")
        return set()
    text = index.read_text(encoding="utf-8")
    front, body = split_frontmatter(text)
    if front is not None:
        keys = top_level_keys(front)
        unknown = set(keys) - {"okf_version"}
        if unknown:
            result.error(rel, f"E3 index.md heeft onverwachte frontmattervelden: {', '.join(sorted(unknown))}")
    if not LINK_RE.search(body):
        result.error(rel, "E3 index.md bevat geen links naar de concepten")
    return {target.split("#", 1)[0].removeprefix("./") for target in LINK_RE.findall(body)}


def check_log(bundle: Path, result: Result) -> None:
    log = bundle / "log.md"
    rel = f"{bundle.name}/log.md"
    if not log.exists():
        result.error(rel, "E4 log.md ontbreekt")
        return
    front, body = split_frontmatter(log.read_text(encoding="utf-8"))
    if front is not None:
        result.error(rel, "E4 log.md hoort geen frontmatter te hebben")
    dates = DATE_HEADING_RE.findall(log.read_text(encoding="utf-8"))
    if not dates:
        result.error(rel, "E4 log.md heeft geen ISO 8601-datumkoppen (## YYYY-MM-DD)")
        return
    if dates != sorted(dates, reverse=True):
        result.error(rel, "E4 log.md staat niet met de nieuwste datum bovenaan")


def main() -> int:
    result = Result()
    for name in BUNDLES:
        bundle = ROOT / name
        if not bundle.is_dir():
            result.error(name, "bundelmap ontbreekt")
            continue
        listed = check_index(bundle, result)
        check_log(bundle, result)
        for path in sorted(bundle.glob("*.md")):
            if path.name in RESERVED:
                continue
            check_concept(path, f"{name}/{path.name}", result)
            if path.name not in listed:
                result.warn(f"{name}/{path.name}", "W5 staat niet in index.md")

    for warning in result.warnings:
        print(f"waarschuwing  {warning}")
    for error in result.errors:
        print(f"fout          {error}")

    print(
        f"\n{result.concepts} concepten gecontroleerd, "
        f"{len(result.errors)} fouten, {len(result.warnings)} waarschuwingen, "
        f"{result.sourced} met bronnen"
    )
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
