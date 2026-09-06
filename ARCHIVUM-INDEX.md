# ARCHIVUM — index de la mémoire partagée

Toutes les archives sont volontairement **visibles directement à la racine de `main`**.

Voir `ARCHIVUM-LEGE-ME.md` pour les règles de provenance, de tri et de sécurité.

## Sessions Claude

| Session | Brut | Extrait |
|---|---:|---:|
| [2026-08-09 — VINDEX language bootstrapping](ARCHIVUM-CLAUDE-2026-08-09-13-55-26-vindex-language-bootstrapping.md) | 3337 Ko | 218 Ko |
| [2026-08-10 — VINDEX language bootstrapping](ARCHIVUM-CLAUDE-2026-08-10-01-30-32-vindex-language-bootstrapping.md) | 3168 Ko | 124 Ko |
| [2026-08-11 01:50 — VINDEX language bootstrapping](ARCHIVUM-CLAUDE-2026-08-11-01-50-04-vindex-language-bootstrapping.md) | 3375 Ko | 133 Ko |
| [2026-08-11 22:20 — VINDEX language bootstrapping](ARCHIVUM-CLAUDE-2026-08-11-22-20-29-vindex-language-bootstrapping.md) | 4091 Ko | 174 Ko |
| [2026-08-13 — VINDEX language bootstrapping v2](ARCHIVUM-CLAUDE-2026-08-13-02-22-54-vindex-language-bootstrapping-v2.md) | 3268 Ko | 149 Ko |
| [2026-08-14 — compiler session v3](ARCHIVUM-CLAUDE-2026-08-14-15-04-38-vindex-compiler-session-v3.md) | 3429 Ko | 135 Ko |
| [2026-08-18 — compiler session v4](ARCHIVUM-CLAUDE-2026-08-18-20-30-40-vindex-compiler-session-v4.md) | 3387 Ko | 137 Ko |
| [2026-08-20 — compiler/OS session v5](ARCHIVUM-CLAUDE-2026-08-20-02-12-06-vindex-compiler-os-session-v5.md) | 2958 Ko | 155 Ko |
| [2026-08-21 — OS/windowing session v6](ARCHIVUM-CLAUDE-2026-08-21-10-26-57-vindex-os-windowing-session-v6.md) | 2022 Ko | 76 Ko |
| [2026-08-21 — PE/terminal integration v7](ARCHIVUM-CLAUDE-2026-08-21-23-30-22-vindex-pe-terminal-integration-v7.md) | 3175 Ko | 145 Ko |
| [2026-08-23 — PE integration v8](ARCHIVUM-CLAUDE-2026-08-23-04-19-00-vindex-pe-integration-session-v8.md) | 2676 Ko | 116 Ko |
| [2026-08-30 — PE integration v9](ARCHIVUM-CLAUDE-2026-08-30-13-00-40-vindex-pe-integration-session-v9.md) | 3110 Ko | 138 Ko |
| [2026-09-02 — P12/PCI session v10](ARCHIVUM-CLAUDE-2026-09-02-12-30-36-vindex-p12-pci-session-v10.md) | 2506 Ko | 177 Ko |

**Claude : 13 sessions, 39 Mo bruts -> 1883 Ko extraits (5 %).**

## Sessions ChatGPT

Les quatre premières entrées proviennent de partages publics récupérés et nettoyés. Les cinq suivantes sont des reconstructions de coordination explicitement marquées non verbatim et recoupées avec les PR/commits canoniques.

| Session | Provenance | Taille |
|---|---|---:|
| [2026-08-23 — Compilator dynamicus et synchronisation Windows](ARCHIVUM-CHATGPT-2026-08-23-compilator-dynamicus.md) | partage public | 2 Ko |
| [2026-08-23 — Purificatio VINDEX 0.53](ARCHIVUM-CHATGPT-2026-08-23-vindex-053-purificatio.md) | partage public | 2 Ko |
| [2026-08-24 — Sylvia Laboratorium : bureau, texte et souris UEFI](ARCHIVUM-CHATGPT-2026-08-24-sylvia-laboratorium-visuel.md) | partage public | 3 Ko |
| [2026-08-26 — P9 : documentation canonique et bibliothèque standard](ARCHIVUM-CHATGPT-2026-08-26-p9-documentatio-bibliotheca.md) | partage public | 3 Ko |
| [2026-08-29 — Graphica X : P16-XII A à E](ARCHIVUM-CHATGPT-2026-08-29-graphica-x-p16-xii-a-e.md) | reconstruction | 2 Ko |
| [2026-08-30/09-02 — Backend Graphica X et P12 matériel](ARCHIVUM-CHATGPT-2026-08-30-2026-09-02-backend-gpu-p12.md) | reconstruction | 2 Ko |
| [2026-09-03 — ATMOS // TERMINAL DEPTH et Passe Génocidaire](ARCHIVUM-CHATGPT-2026-09-03-atmos-terminal-depth.md) | reconstruction | 3 Ko |
| [2026-09-04 — P0/P9 : diagnostics stricts du compilateur](ARCHIVUM-CHATGPT-2026-09-04-diagnostica-p0-p9.md) | reconstruction | 3 Ko |
| [2026-09-05/06 — F9 : VIRGL, residentia 3D et SUBMIT_3D](ARCHIVUM-CHATGPT-2026-09-05-2026-09-06-f9-virgl.md) | reconstruction | 4 Ko |

**ChatGPT : 9 entrées actuellement archivées.**

## Outils

- `ARCHIVUM-extrahe_archivum.py` — régénère les sessions Claude directement à la racine et reconstruit cet index sans supprimer les entrées ChatGPT.
- `ARCHIVUM-verifica_secreta.py` — refuse les motifs de secrets évidents dans `ARCHIVUM-*.md`.

La prochaine session archivée doit continuer la même convention : `ARCHIVUM-CLAUDE-*` ou `ARCHIVUM-CHATGPT-*`, directement à la racine.