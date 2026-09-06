#!/usr/bin/env python3
"""Extrait les transcriptions de session vers une archive lisible.

But: rendre l'historique des echanges lisible par l'autre agent (ChatGPT)
et par un humain, sans deverser 40 Mo de JSON brut dans le depot.

Ce qui est conserve:
  - les messages de l'utilisateur (Numi)
  - les reponses textuelles de l'assistant
  - les commandes executees et leur description

Ce qui est ecarte:
  - le raisonnement interne (thinking): non destine a autrui, et c'est
    la majeure partie du volume;
  - les sorties brutes d'outils: souvent des milliers de lignes de logs
    dont la conclusion est deja dans la reponse textuelle.

Resultat mesure: environ 6 a 10 % du volume brut, sans perte du contenu
qui sert a la coordination.
"""

import json
import re
import os
import glob

SOURCE = "/mnt/transcripts"
SORTIE = "/home/claude/archivum"


# Motifs de secrets a expurger avant ecriture. GitHub refuse tout push
# contenant un jeton, et il a raison: une archive de conversation contient
# tout ce qui a ete tape, jetons compris.
SECRETA = [
    (re.compile(r'ghp_[A-Za-z0-9]{36}'), '[TOKEN-EXPURGATUM]'),
    (re.compile(r'github_pat_[A-Za-z0-9_]{22,}'), '[TOKEN-EXPURGATUM]'),
    (re.compile(r'gho_[A-Za-z0-9]{36}'), '[TOKEN-EXPURGATUM]'),
    (re.compile(r'sk-[A-Za-z0-9]{32,}'), '[CLAVIS-EXPURGATA]'),
]


def expurga(texte):
    """Retire les secrets. Applique systematiquement, sans exception."""
    for rx, rep in SECRETA:
        texte = rx.sub(rep, texte)
    return texte


def extrait_blocs(raw):
    """Recupere les tableaux JSON du transcript."""
    return re.findall(r'\[\s*\{.*?\n\]', raw, re.S)


def traite(chemin):
    raw = open(chemin, encoding='utf-8', errors='replace').read()
    lignes = []
    for bloc in extrait_blocs(raw):
        try:
            items = json.loads(bloc)
        except Exception:
            continue
        for it in items:
            t = it.get('type')
            if t == 'text' and it.get('text'):
                lignes.append(it['text'].strip())
            elif t == 'tool_use':
                desc = (it.get('input') or {}).get('description')
                cmd = (it.get('input') or {}).get('command')
                if desc:
                    lignes.append(f"    [action] {desc}")
                elif cmd and len(str(cmd)) < 200:
                    lignes.append(f"    [action] {cmd}")
    return lignes


def main():
    os.makedirs(SORTIE, exist_ok=True)
    fichiers = sorted(glob.glob(f"{SOURCE}/*.txt"))
    index = []
    brut_total = 0
    net_total = 0

    for f in fichiers:
        nom = os.path.basename(f)
        if nom == 'journal.txt':
            continue
        taille_brute = os.path.getsize(f)
        brut_total += taille_brute

        lignes = traite(f)
        if not lignes:
            continue

        base = nom.replace('.txt', '')
        dest = f"{SORTIE}/{base}.md"
        with open(dest, 'w', encoding='utf-8') as out:
            out.write(f"# Session {base}\n\n")
            out.write("_Extrait lisible. Raisonnement interne et sorties brutes d'outils omis._\n\n---\n\n")
            out.write(expurga("\n\n".join(lignes)))
        taille_nette = os.path.getsize(dest)
        net_total += taille_nette
        index.append((base, taille_brute, taille_nette))

    # index
    with open(f"{SORTIE}/INDEX.md", 'w', encoding='utf-8') as idx:
        idx.write("# Archive des sessions\n\n")
        idx.write("Historique des echanges entre Numi et Claude sur le projet VINDEX.\n")
        idx.write("Destine a la coordination entre agents: ChatGPT peut y lire ce qui a\n")
        idx.write("ete tente, decide et ecarte, et reciproquement.\n\n")
        idx.write("Chaque fichier est un extrait lisible du transcript de session.\n")
        idx.write("Le raisonnement interne et les sorties brutes d'outils sont omis:\n")
        idx.write("ils representent plus de 90 % du volume sans servir la coordination.\n\n")
        idx.write("| Session | Brut | Extrait |\n|---|---|---|\n")
        for base, b, n in index:
            idx.write(f"| [{base}]({base}.md) | {b//1024} Ko | {n//1024} Ko |\n")
        idx.write(f"\n**Total : {brut_total//1024//1024} Mo bruts -> {net_total//1024} Ko extraits ")
        idx.write(f"({100*net_total/brut_total:.0f} %)**\n")

    print(f"{len(index)} sessions extraites")
    print(f"brut  : {brut_total//1024//1024} Mo")
    print(f"archive: {net_total//1024} Ko ({100*net_total/brut_total:.1f} %)")


if __name__ == '__main__':
    main()
