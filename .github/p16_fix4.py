#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
FV = R / 'bibliotheca/fenestrale_ii_purus.vindex'
FS = R / 'bibliotheca/fenestrale_ii_superficies.vindex'

# TEXTUS + numerus concatenatio est; ante offseta memoriae ad NUMERUS convertendum est.
t = FV.read_text(encoding='utf-8')
if 'FUNCTIO FV_TEXTUS_SEDES REDDENS NUMERUS.' not in t:
    ancora = 'FUNCTIO FV_TEXTUM REDDENS NUMERUS.\n'
    adiutor = '''FUNCTIO FV_TEXTUS_SEDES REDDENS NUMERUS.
    ACCIPIT textus SICUT TEXTUS.
    REDDE textus.
FIN-FUNCTIO.

'''
    if ancora not in t:
        raise SystemExit('FV: FV_TEXTUM deest')
    t = t.replace(ancora, adiutor + ancora, 1)

vetus = '    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(textus).\n    DECLARA i SICUT NUMERUS VALENS 0.\n'
novum = '    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(textus).\n    DECLARA descriptor SICUT NUMERUS VALENS FV_TEXTUS_SEDES(textus).\n    DECLARA i SICUT NUMERUS VALENS 0.\n'
n = t.count(vetus)
if n != 2:
    raise SystemExit(f'FV: II corpora textus exspectata sunt, inventa={n}')
t = t.replace(vetus, novum)
n2 = t.count('OCTETUS_AB(textus + 16 + i)')
if n2 != 2:
    raise SystemExit(f'FV: II lectiones textus typatae exspectatae sunt, inventae={n2}')
t = t.replace('OCTETUS_AB(textus + 16 + i)', 'OCTETUS_AB(descriptor + 16 + i)')
FV.write_text(t, encoding='utf-8')


t = FS.read_text(encoding='utf-8')
if 'FUNCTIO FS_TEXTUS_SEDES REDDENS NUMERUS.' not in t:
    ancora = 'FUNCTIO FS_TEXTUM REDDENS NUMERUS.\n'
    adiutor = '''FUNCTIO FS_TEXTUS_SEDES REDDENS NUMERUS.
    ACCIPIT textus SICUT TEXTUS.
    REDDE textus.
FIN-FUNCTIO.

'''
    if ancora not in t:
        raise SystemExit('FS: FS_TEXTUM deest')
    t = t.replace(ancora, adiutor + ancora, 1)

vetus = '    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(textus).\n    DECLARA i SICUT NUMERUS VALENS 0.\n'
novum = '    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(textus).\n    DECLARA descriptor SICUT NUMERUS VALENS FS_TEXTUS_SEDES(textus).\n    DECLARA i SICUT NUMERUS VALENS 0.\n'
if t.count(vetus) != 1:
    raise SystemExit('FS: corpus textus unicum non inventum')
t = t.replace(vetus, novum, 1)
if t.count('OCTETUS_AB(textus + 16 + i)') != 1:
    raise SystemExit('FS: lectio textus typata non inventa')
t = t.replace('OCTETUS_AB(textus + 16 + i)', 'OCTETUS_AB(descriptor + 16 + i)', 1)
FS.write_text(t, encoding='utf-8')

print('RECTE: TEXTUS ad sedem numericam ante offseta graphica convertitur.')
