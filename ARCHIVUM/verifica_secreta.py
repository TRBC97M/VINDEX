#!/usr/bin/env python3
"""Refuse les motifs de secrets évidents dans les Markdown de ARCHIVUM/."""

from pathlib import Path
import re

ARCHIVUM = Path(__file__).resolve().parent

MOTIFS = [
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,255}")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]{20,255}")),
    ("OpenAI API key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,255}")),
    ("Slack token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,255}")),
    ("GitLab token", re.compile(r"glpat-[A-Za-z0-9_-]{10,255}")),
    ("HuggingFace token", re.compile(r"hf_[A-Za-z0-9]{20,255}")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]

fautes = []
for chemin in sorted(ARCHIVUM.glob("*.md")):
    texte = chemin.read_text(encoding="utf-8", errors="replace")
    for nom, rx in MOTIFS:
        if rx.search(texte):
            fautes.append((chemin.name, nom))

if fautes:
    for chemin, nom in fautes:
        print(f"SECRETUM: {chemin}: {nom}")
    raise SystemExit(1)

print("RECTE: nullum secretum manifestum in ARCHIVUM/*.md inventum est.")
