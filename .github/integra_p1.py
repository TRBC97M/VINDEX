#!/usr/bin/env python3
from pathlib import Path
import sys

p = Path(sys.argv[1])
lines = p.read_text().splitlines()

initia = sum(1 for x in lines if x.startswith('<<<<<<<'))
media = sum(1 for x in lines if x == '=======')
fines = sum(1 for x in lines if x.startswith('>>>>>>>'))
if (initia, media, fines) != (1, 1, 1):
    raise SystemExit(f'ERRATUM: conflictus inexspectati: {initia}/{media}/{fines}')

# Conflictus unicus tantum nuntium usus tangit. Utrumque contractum servamus:
# PROIECTUM hodiernum + novum target UEFI; vetus nuntium [pe] removemus.
out = []
for line in lines:
    if line.startswith('<<<<<<<') or line == '=======' or line.startswith('>>>>>>>'):
        continue
    if 'USUS: compilator_vindex <fons.vindex> <exsecutabile> [pe]".' in line:
        continue
    out.append(line)
lines = out

# Git textualiter agnitionem UEFI extra custodiam argc >= 4 collocavit.
# Hanc in custodiam propriam redigimus, ne argv[3] sine argumento legatur.
target = '        SI arg3[0] == 117 && arg3[1] == 101 && arg3[2] == 102 && arg3[3] == 105 && arg3[4] == 0 TUNC'
out = []
i = 0
reparata = 0
while i < len(lines):
    line = lines[i]
    if line == target:
        if i + 2 >= len(lines) or lines[i + 1].strip() != 'modus_pe = 2.' or lines[i + 2] != '        FIN-SI.':
            raise SystemExit('ERRATUM: corpus recognitionis UEFI inexspectatum est')
        out.append('        SI argc >= 4 TUNC')
        out.append('            DECLARA arg3_uefi SICUT ACUS<LITTERA> VALENS argv[3].')
        out.append('            SI arg3_uefi[0] == 117 && arg3_uefi[1] == 101 && arg3_uefi[2] == 102 && arg3_uefi[3] == 105 && arg3_uefi[4] == 0 TUNC')
        out.append('                modus_pe = 2.')
        out.append('            FIN-SI.')
        out.append('        FIN-SI.')
        reparata += 1
        i += 3
        continue
    out.append(line)
    i += 1

if reparata != 1:
    raise SystemExit(f'ERRATUM: recognitiones UEFI reparatae={reparata}')

text = '\n'.join(out) + '\n'
if '<<<<<<<' in text or '\n=======\n' in text or '>>>>>>>' in text:
    raise SystemExit('ERRATUM: signa conflictus residualia manent')
if '[pe|uefi]' not in text or 'PROIECTUM <proiectum.vindex>' not in text:
    raise SystemExit('ERRATUM: contractus usus post reconciliationem incompletus est')

p.write_text(text)
print('RECTE: conflictus P1 et custodia argc reconciliata sunt.')
