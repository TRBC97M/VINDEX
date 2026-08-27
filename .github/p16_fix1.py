#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
REG = R / 'bibliotheca/fenestrae_registrum_i.vindex'
PROBA = R / 'probationes/fenestrale_purus_i_fenestrae.vindex'

# Registrum fenestrarum est stratum inferius et separatim probatur; nullam
# functionem rendereris vocare debet. Limen areae operabilis ad P16-I XL px est.
t = REG.read_text(encoding='utf-8')
if 'FV_METRUM_TASKBAR()' not in t:
    raise SystemExit('registrum: relatio temporaria ad metrum rendereris deest')
t = t.replace('FV_METRUM_TASKBAR()', '40')
REG.write_text(t, encoding='utf-8')

# Probatio contractum geometriae novum sequitur: 720 - 40 = 680.
t = PROBA.read_text(encoding='utf-8')
old = 'SI CONTENTUM(n+32)!=1280 || CONTENTUM(n+40)!=692 TUNC REDDE 65. FIN-SI.'
new = 'SI CONTENTUM(n+32)!=1280 || CONTENTUM(n+40)!=680 TUNC REDDE 65. FIN-SI.'
if old not in t:
    raise SystemExit('probatio: altitudo historica DCXCII deest')
t = t.replace(old, new, 1)
PROBA.write_text(t, encoding='utf-8')

print('RECTE: registrum inferius a renderer separatum; limen XL px probatur.')
