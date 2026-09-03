#!/usr/bin/env python3
"""Remove use of PERGE from ATMOS POC II until that documented keyword is reconciled."""

from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "Vindex Chat-GPT" / "vindex_final_v51" / "exempla" / "atmos_terminal_depth" / "interactivum.vindex"
text = FONS.read_text(encoding="utf-8")

old = '''        SI n < 0 TUNC PROCLAMA "ERRATUM: stdin lectio". REDDE 76. FIN-SI.\n        SI n == 0 TUNC PERGE. FIN-SI.\n\n        DECLARA tractatum SICUT NUMERUS VALENS 0.\n        DECLARA mutatum SICUT NUMERUS VALENS 0.\n'''
new = '''        SI n < 0 TUNC PROCLAMA "ERRATUM: stdin lectio". REDDE 76. FIN-SI.\n\n        DECLARA tractatum SICUT NUMERUS VALENS 0.\n        DECLARA mutatum SICUT NUMERUS VALENS 0.\n        SI n == 0 TUNC tractatum = 1. FIN-SI.\n'''

if new in text:
    print("RECTE: correctio ATMOS II iam adest.")
    raise SystemExit(0)
if text.count(old) != 1:
    raise SystemExit(f"ERRATUM: locus ATMOS II exspectatus {text.count(old)} vice inventus est")
FONS.write_text(text.replace(old, new, 1), encoding="utf-8")
print("RECTE: ATMOS II PERGE non amplius requirit.")
