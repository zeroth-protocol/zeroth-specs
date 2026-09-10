#!/usr/bin/env python3
"""Fail-closed validation for public Zeroth specification metadata and index integrity."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "SPEC-INDEX.md"
REQUIRED_FIELDS = (
    "Status",
    "Normative",
    "Version",
    "Published",
    "Security sensitivity",
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_field(text: str, field: str) -> str | None:
    match = re.search(rf"^- \*\*{re.escape(field)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def validate_spec(path: Path, errors: list[str]) -> tuple[str, str] | None:
    text = path.read_text(encoding="utf-8")
    filename_match = re.match(r"^(SPEC-\d{4})-[a-z0-9-]+\.md$", path.name)
    if not filename_match:
        fail(errors, f"{path.name}: filename must be SPEC-NNNN-kebab-case.md")
        return None

    spec_id = filename_match.group(1)
    heading_match = re.search(r"^#\s+(SPEC-\d{4})\s+[—-]\s+(.+)$", text, re.MULTILINE)
    if not heading_match:
        fail(errors, f"{path.name}: missing canonical '# SPEC-NNNN — Title' heading")
        return None

    if heading_match.group(1) != spec_id:
        fail(errors, f"{path.name}: heading ID {heading_match.group(1)} does not match filename ID {spec_id}")

    fields: dict[str, str] = {}
    for field in REQUIRED_FIELDS:
        value = parse_field(text, field)
        if value is None:
            fail(errors, f"{path.name}: missing metadata field '{field}'")
        else:
            fields[field] = value

    if fields.get("Status") == "Draft" and fields.get("Normative") != "No":
        fail(errors, f"{path.name}: Draft specifications must be marked 'Normative: No'")

    if fields.get("Normative") not in {"Yes", "No"}:
        fail(errors, f"{path.name}: Normative must be Yes or No")

    if fields.get("Status") not in {"Draft", "Review", "Accepted", "Final", "Deprecated", "Superseded"}:
        fail(errors, f"{path.name}: unsupported Status '{fields.get('Status')}'")

    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(errors, f"{path.name}: possible secret/private-key material detected")

    return spec_id, heading_match.group(2).strip()


def main() -> int:
    errors: list[str] = []

    if not INDEX.exists():
        print("ERROR: SPEC-INDEX.md is missing", file=sys.stderr)
        return 1

    spec_files = sorted(
        p for p in ROOT.glob("SPEC-*.md") if p.name != "SPEC-INDEX.md"
    )
    if not spec_files:
        fail(errors, "No published specification files found")

    ids: dict[str, Path] = {}
    for path in spec_files:
        result = validate_spec(path, errors)
        if result is None:
            continue
        spec_id, _ = result
        if spec_id in ids:
            fail(errors, f"duplicate specification ID {spec_id}: {ids[spec_id].name}, {path.name}")
        ids[spec_id] = path

    index_text = INDEX.read_text(encoding="utf-8")

    # Every Markdown link to a SPEC document in the index must resolve locally.
    for target in re.findall(r"\]\((SPEC-\d{4}-[a-z0-9-]+\.md)\)", index_text):
        if not (ROOT / target).is_file():
            fail(errors, f"SPEC-INDEX.md: linked file does not exist: {target}")

    # Every published spec file must be linked from the index.
    for path in spec_files:
        if f"]({path.name})" not in index_text:
            fail(errors, f"SPEC-INDEX.md: published spec is not linked: {path.name}")

    # Prevent accidental publication of common credential formats in the index too.
    for pattern in SECRET_PATTERNS:
        if pattern.search(index_text):
            fail(errors, "SPEC-INDEX.md: possible secret/private-key material detected")

    if errors:
        print("ZEROTH SPEC VALIDATION: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"ZEROTH SPEC VALIDATION: PASS ({len(spec_files)} specifications checked)")
    for spec_id, path in sorted(ids.items()):
        print(f"- {spec_id}: {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
