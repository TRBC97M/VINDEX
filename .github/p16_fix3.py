#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
viae = [
    R / 'bibliotheca/fenestrale_ii_purus.vindex',
    R / 'bibliotheca/fenestrale_ii_superficies.vindex',
]

mutationes = 0
for p in viae:
    t = p.read_text(encoding='utf-8')
    n = t.count('OCTETUS_AB(textus + 8 + i)')
    if n:
        t = t.replace('OCTETUS_AB(textus + 8 + i)', 'OCTETUS_AB(textus + 16 + i)')
        mutationes += n
        p.write_text(t, encoding='utf-8')

if mutationes < 3:
    raise SystemExit(f'DEFECIT: saltem III lectiones TEXTUS veteres exspectatae sunt; inventae={mutationes}')
print(f'RECTE: {mutationes} lectiones graphicae ad TEXTUS + XVI correctae sunt.')
