#!/usr/bin/env python3
from pathlib import Path
p=Path('Vindex Chat-GPT/vindex_final_v51/bibliotheca/fenestrale_gestor_i.vindex')
t=p.read_text(encoding='utf-8')
old='        SI !(my>=taskbar_top && mx>=6 && mx<110) TUNC s[38]=0. FIN-SI.'
new='        SI my<taskbar_top || mx<6 || mx>=110 TUNC s[38]=0. FIN-SI.'
if old not in t: raise SystemExit('DEFECIT: condicio INITIUM temporaria deest')
p.write_text(t.replace(old,new,1),encoding='utf-8')
print('RECTE: clausura INITIUM sine negatione composita exprimitur.')
