#!/usr/bin/env python3
"""Extrait les transcriptions Claude vers la mémoire partagée à la racine.

Convention du dépôt :
  ARCHIVUM-CLAUDE-*.md   sessions Claude
  ARCHIVUM-CHATGPT-*.md  sessions ChatGPT (gérées côté ChatGPT)
  ARCHIVUM-INDEX.md      index commun

Le raisonnement interne et les sorties brutes d'outils sont omis. Les secrets
connus sont expurgés avant écriture.
"""

from pathlib import Path
import glob
import json
import os
import re

SOURCE = Path("/mnt/transcripts")
RACINE = Path(__file__).resolve().parent

SECRETA = [
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{20,255}"), "[TOKEN-GITHUB-EXPURGATUM]"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,255}"), "[TOKEN-GITHUB-EXPURGATUM]"),
    (re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,255}"), "[CLAVIS-OPENAI-EXPURGATA]"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,255}"), "[TOKEN-SLACK-EXPURGATUM]"),
    (re.compile(r"glpat-[A-Za-z0-9_-]{10,255}"), "[TOKEN-GITLAB-EXPURGATUM]"),
    (re.compile(r"hf_[A-Za-z0-9]{20,255}"), "[TOKEN-HF-EXPURGATUM]"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "[CLAVIS-AWS-EXPURGATA]"),
    (
        re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----.*?"
            r"-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
            re.S,
        ),
        "[CLAVIS-PRIVATA-EXPURGATA]",
    ),
]


def expurga(texte: str) -> str:
    """Retire les motifs de secrets connus avant toute écriture."""
    for rx, remplacement in SECRETA:
        texte = rx.sub(remplacement, texte)
    return texte


def extrait_blocs(raw: str):
    """Récupère les tableaux JSON intégrés dans les transcriptions Claude."""
    return re.findall(r"\[\s*\{.*?\n\]", raw, re.S)


def traite(chemin: Path):
    raw = chemin.read_text(encoding="utf-8", errors="replace")
    lignes = []
    for bloc in extrait_blocs(raw):
        try:
            items = json.loads(bloc)
        except Exception:
            continue
        for item in items:
            typ = item.get("type")
            if typ == "text" and item.get("text"):
                lignes.append(item["text"].strip())
            elif typ == "tool_use":
                entree = item.get("input") or {}
                desc = entree.get("description")
                cmd = entree.get("command")
                if desc:
                    lignes.append(f"    [action] {desc}")
                elif cmd and len(str(cmd)) < 200:
                    lignes.append(f"    [action] {cmd}")
    return lignes


def titre_markdown(chemin: Path) -> str:
    """Lit le premier titre H1 d'un fichier ChatGPT pour l'index."""
    try:
        for ligne in chemin.read_text(encoding="utf-8", errors="replace").splitlines():
            if ligne.startswith("# "):
                return ligne[2:].strip()
    except OSError:
        pass
    return chemin.stem


def verifie_aucun_secret_manifeste():
    """Refuse l'archive si un motif connu subsiste dans un Markdown ARCHIVUM."""
    fautes = []
    for chemin in sorted(RACINE.glob("ARCHIVUM-*.md")):
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        for rx, _ in SECRETA:
            if rx.search(texte):
                fautes.append(str(chemin.name))
                break
    if fautes:
        raise SystemExit("secret potentiel restant dans: " + ", ".join(fautes))


def main():
    fichiers = sorted(SOURCE.glob("*.txt"))
    claude = []
    brut_total = 0
    net_total = 0

    for source in fichiers:
        if source.name == "journal.txt":
            continue

        taille_brute = source.stat().st_size
        lignes = traite(source)
        if not lignes:
            continue

        base = source.stem
        nom_sortie = f"ARCHIVUM-CLAUDE-{base}.md"
        destination = RACINE / nom_sortie

        contenu = (
            f"# Session Claude — {base}\n\n"
            "_Extrait lisible. Raisonnement interne et sorties brutes d'outils omis._\n\n"
            "---\n\n"
            + "\n\n".join(lignes)
            + "\n"
        )
        destination.write_text(expurga(contenu), encoding="utf-8")

        taille_nette = destination.stat().st_size
        brut_total += taille_brute
        net_total += taille_nette
        claude.append((base, nom_sortie, taille_brute, taille_nette))

    chatgpt = sorted(RACINE.glob("ARCHIVUM-CHATGPT-*.md"))

    index = []
    index.append("# ARCHIVUM — index de la mémoire partagée\n")
    index.append(
        "Toutes les archives sont volontairement visibles directement à la racine de `main`. "
        "Voir `ARCHIVUM-LEGE-ME.md` pour les règles de provenance, tri et sécurité.\n"
    )
    index.append("## Sessions Claude\n")
    index.append("| Session | Brut | Extrait |\n|---|---:|---:|")
    for base, nom, brut, net in claude:
        index.append(f"| [{base}]({nom}) | {brut//1024} Ko | {net//1024} Ko |")
    if brut_total:
        index.append(
            f"\n**Claude : {len(claude)} sessions, {brut_total//1024//1024} Mo bruts -> "
            f"{net_total//1024} Ko extraits ({100*net_total/brut_total:.0f} %).**\n"
        )

    index.append("## Sessions ChatGPT\n")
    index.append("| Session | Taille |\n|---|---:|")
    for chemin in chatgpt:
        titre = titre_markdown(chemin)
        index.append(f"| [{titre}]({chemin.name}) | {chemin.stat().st_size//1024} Ko |")
    index.append(f"\n**ChatGPT : {len(chatgpt)} entrées actuellement archivées.**\n")

    (RACINE / "ARCHIVUM-INDEX.md").write_text("\n".join(index), encoding="utf-8")

    verifie_aucun_secret_manifeste()

    print(f"{len(claude)} sessions Claude extraites à la racine")
    print(f"{len(chatgpt)} entrées ChatGPT conservées à la racine")
    if brut_total:
        print(f"Claude brut: {brut_total//1024//1024} Mo")
        print(f"Claude archive: {net_total//1024} Ko ({100*net_total/brut_total:.1f} %)")
    print("RECTE: aucun motif de secret connu dans ARCHIVUM-*.md")


if __name__ == "__main__":
    main()
