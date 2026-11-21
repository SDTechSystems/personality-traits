"""Lint SKILL.md files: frontmatter, size, hidden Unicode, encoded blobs, executables.

Runs in CI only. Uses the Python standard library; reads files, writes nothing.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = ("anthropic", "claude")
MAX_NAME = 64           # Agent Skills spec
MAX_DESC = 1024         # Agent Skills spec
MAX_SKILL_LINES = 500   # Anthropic best practices
# Zero-width, bidi-control and BOM characters that can hide instructions.
HIDDEN = re.compile("[​-‏‪-‮⁠-⁤﻿]")
# Long unbroken base64-like runs are a common way to smuggle content.
BLOB = re.compile(r"[A-Za-z0-9+/=]{120,}")
BLOCKED_EXT = {".sh", ".ps1", ".bat", ".cmd", ".exe", ".dll", ".py", ".js", ".bin"}

errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip('"')
    return fields


for path in SKILLS.rglob("*"):
    if path.is_file() and path.suffix.lower() in BLOCKED_EXT:
        err(path, "executable or script file not allowed in skills/")

for md in SKILLS.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    if HIDDEN.search(text):
        err(md, "contains hidden Unicode characters")
    if BLOB.search(text):
        err(md, "contains a long encoded-looking string")

skill_files = list(SKILLS.rglob("SKILL.md"))
if not skill_files:
    err(SKILLS, "no SKILL.md found")

for skill in skill_files:
    text = skill.read_text(encoding="utf-8").replace("\r\n", "\n")
    fm = frontmatter(text)
    if fm is None:
        err(skill, "missing or malformed frontmatter")
        continue
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not NAME_RE.match(name) or len(name) > MAX_NAME:
        err(skill, f"invalid name '{name}'")
    if any(word in name for word in RESERVED):
        err(skill, "name uses a reserved word")
    if name != skill.parent.name:
        err(skill, f"name '{name}' must match folder '{skill.parent.name}'")
    if not desc or len(desc) > MAX_DESC:
        err(skill, f"description must be 1-{MAX_DESC} characters")
    if text.count("\n") > MAX_SKILL_LINES:
        err(skill, f"longer than {MAX_SKILL_LINES} lines")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skill_files)} skill(s) checked")
