#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
MUS = R / 'systema/rectores/murus_ps2.vindex'
INPUT = R / 'bibliotheca/fenestrale_input_i.vindex'
FEN = R / 'systema/fenestrale_ii_purus_i.vindex'
BUILD = R / 'systema/uefi/construe_uefi_purum.sh'
TESTM = R / 'instrumenta/proba_murem_uefi_053.py'
TESTF = R / 'instrumenta/proba_fenestrale_uefi_purum.py'

# I. Rector PS/2: mores nuclei historici servantur; telemetria cruda additur.
# Pagina 0x03019000 est prima pagina post volumen 32 KiB
# (0x03011000..0x03018fff) intra COMMUNIS iam reservatum.
m = MUS.read_text(encoding='utf-8')
mutationes = [
    ('50432071', '50434119'),
    ('50432070', '50434118'),
    ('50432069', '50434117'),
    ('50432068', '50434116'),
    ('50432067', '50434115'),
    ('50432066', '50434114'),
    ('50432065', '50434113'),
    ('50432064', '50434112'),
    ('50432016', '50434064'),
    ('50432000', '50434048'),
]
for vetus, novus in mutationes:
    m = m.replace(vetus, novus)

initium = m.index('// Telemetria rectoris:')
finis = m.index('\n\nFUNCTIO PS2_STUBS_PARA', initium)
commentarium = '''// Pagina rectoris canonica: 0x03019000, statim post volumen COMMUNIS.
// Offsets intra paginam:
//   +64 status initializationis (9 = paratus); +65 ACK F6; +66 ACK F4;
//   +67 numerus fasciculorum; +68 status 8042; +69 positio fasciculi;
//   +70 flags; +71 dx octetum; +72 dx signatum; +80 dy signatum; +88 bullae.
//
// Publicatio historica UEFI_MURIS_PUBLICA manet intacta. Telemetria cruda
// additiva Fenestrali II datur, ut nucleus vetus nullam mutationem morum patiatur.'''
m = m[:initium] + commentarium + m[finis:]

old = '''    SCRIBE_OCTETUM_AB(50434117, 0).
    SCRIBE_OCTETUM_AB(50434118, 0).
    SCRIBE_OCTETUM_AB(50434119, 0).
    SCRIBE_OCTETUM_AB(50434112, 9).
'''
new = '''    SCRIBE_OCTETUM_AB(50434117, 0).
    SCRIBE_OCTETUM_AB(50434118, 0).
    SCRIBE_OCTETUM_AB(50434119, 0).
    CONTENTUM(50434120) = 0.
    CONTENTUM(50434128) = 0.
    CONTENTUM(50434136) = 0.
    SCRIBE_OCTETUM_AB(50434112, 9).
'''
if old not in m:
    raise SystemExit('murus: initium telemetriae non inventum')
m = m.replace(old, new, 1)

anchor = '''FUNCTIO PS2_PARATUS_EST REDDENS NUMERUS.
    SI OCTETUS_AB(50434112) == 9 TUNC REDDE 1. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

'''
extra = anchor + '''FUNCTIO PS2_DX REDDENS NUMERUS.
    REDDE CONTENTUM(50434120).
FIN-FUNCTIO.

FUNCTIO PS2_DY REDDENS NUMERUS.
    REDDE CONTENTUM(50434128).
FIN-FUNCTIO.

FUNCTIO PS2_BULLAE REDDENS NUMERUS.
    REDDE CONTENTUM(50434136).
FIN-FUNCTIO.

'''
if anchor not in m:
    raise SystemExit('murus: PS2_PARATUS_EST non inventa')
m = m.replace(anchor, extra, 1)

old = '''    DECLARA x SICUT NUMERUS VALENS CONTENTUM(50331648) + dx.
    DECLARA y SICUT NUMERUS VALENS CONTENTUM(50331656) - dy.
    DECLARA bullae SICUT NUMERUS VALENS flags & 7.
    DECLARA mutatum SICUT NUMERUS VALENS UEFI_MURIS_PUBLICA(x, y, bullae).
'''
new = '''    DECLARA bullae SICUT NUMERUS VALENS flags & 7.
    CONTENTUM(50434120) = dx.
    CONTENTUM(50434128) = dy.
    CONTENTUM(50434136) = bullae.
    DECLARA x SICUT NUMERUS VALENS CONTENTUM(50331648) + dx.
    DECLARA y SICUT NUMERUS VALENS CONTENTUM(50331656) - dy.
    DECLARA mutatum SICUT NUMERUS VALENS UEFI_MURIS_PUBLICA(x, y, bullae).
'''
if old not in m:
    raise SystemExit('murus: finis fasciculi non inventus')
m = m.replace(old, new, 1)
MUS.write_text(m, encoding='utf-8')

# II. Input Fenestralis: PS/2 nativus est via prima; firmware manet fallback.
i = INPUT.read_text(encoding='utf-8')
old = '''    SI s[29]!=0 TUNC
        DECLARA a SICUT NUMERUS VALENS CONTENTUM(s[29]).
        SI a!=0 TUNC DECLARA ra SICUT NUMERUS VALENS UEFI_VOCA6(a,s[29],0,0,0,0,0). FIN-SI.
    FIN-SI.
    REDDE 1.
FIN-FUNCTIO.
'''
new = '''    SI s[29]!=0 TUNC
        DECLARA a SICUT NUMERUS VALENS CONTENTUM(s[29]).
        SI a!=0 TUNC DECLARA ra SICUT NUMERUS VALENS UEFI_VOCA6(a,s[29],0,0,0,0,0). FIN-SI.
    FIN-SI.
    // Allocationes Fenestralis iam perfectae sunt; nunc 8042 parari potest.
    s[30]=PS2_PARA().
    REDDE 1.
FIN-FUNCTIO.
'''
if old not in i:
    raise SystemExit('input: finis IN_PARA non inventus')
i = i.replace(old, new, 1)

anchor = '''FUNCTIO IN_STALL REDDENS NUMERUS.
'''
fun = '''FUNCTIO IN_MURUS REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    SI PS2_PARATUS_EST()==1 TUNC
        DECLARA eventus SICUT NUMERUS VALENS 0.
        DECLARA i SICUT NUMERUS VALENS 0.
        // AUX ante claviaturam firmware hauritur; PS2_POLLE byte non-AUX non legit.
        DUM i<8 PERFICE
            DECLARA p SICUT NUMERUS VALENS PS2_POLLE().
            SI p!=0 TUNC eventus=1. FIN-SI.
            i=i+1.
        FIN-DUM.
        SI eventus==0 TUNC REDDE 0. FIN-SI.
        s[11]=s[11]+PS2_DX().
        s[12]=s[12]-PS2_DY().
        SI s[11]<0 TUNC s[11]=0. FIN-SI.
        SI s[12]<0 TUNC s[12]=0. FIN-SI.
        SI s[11]>=CONTENTUM(50333728) TUNC s[11]=CONTENTUM(50333728)-1. FIN-SI.
        SI s[12]>=CONTENTUM(50333736) TUNC s[12]=CONTENTUM(50333736)-1. FIN-SI.
        REDDE (PS2_BULLAE()&3)+1.
    FIN-SI.
    DECLARA muris SICUT NUMERUS VALENS IN_MURUS_ABS(s[29],s).
    SI muris==0 TUNC muris=IN_MURUS_REL(s[28],s). FIN-SI.
    REDDE muris.
FIN-FUNCTIO.

'''
if anchor not in i:
    raise SystemExit('input: IN_STALL non inventa')
i = i.replace(anchor, fun + anchor, 1)
INPUT.write_text(i, encoding='utf-8')

# III. Fenestrale II: rectorem importa et adaptatorem publicationis historicae praebet.
f = FEN.read_text(encoding='utf-8')
imp = 'IMPORTA "bibliotheca/fenestrale_ii_purus.vindex".\n'
if imp not in f:
    raise SystemExit('fenestrale: ancora importationis deest')
f = f.replace(imp, 'IMPORTA "systema/rectores/murus_ps2.vindex".\n' + imp, 1)

post_imports = 'IMPORTA "bibliotheca/fenestrale_gestor_i.vindex".\n\n'
adaptor = '''IMPORTA "bibliotheca/fenestrale_gestor_i.vindex".

// Rector PS/2 historice hanc functionem vocat. Fenestrale coordinatas suas
// ex dx/dy crudis legit; hic adaptor tantum contractum rectoris implet.
FUNCTIO UEFI_MURIS_PUBLICA REDDENS NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    ACCIPIT y SICUT NUMERUS.
    ACCIPIT bullae SICUT NUMERUS.
    REDDE 1.
FIN-FUNCTIO.

'''
if post_imports not in f:
    raise SystemExit('fenestrale: finis importationum deest')
f = f.replace(post_imports, adaptor, 1)

old = '''    DUM finis==0 PERFICE
        DECLARA redde SICUT NUMERUS VALENS 0.
        DECLARA q SICUT NUMERUS VALENS IN_CLAVIS().
'''
new = '''    DUM finis==0 PERFICE
        DECLARA redde SICUT NUMERUS VALENS 0.
        // AUX/PS2 ante claviaturam firmware pollitur.
        DECLARA muris SICUT NUMERUS VALENS IN_MURUS(s).
        DECLARA q SICUT NUMERUS VALENS IN_CLAVIS().
'''
if old not in f:
    raise SystemExit('fenestrale: initium ansae deest')
f = f.replace(old, new, 1)
old = '''        DECLARA muris SICUT NUMERUS VALENS IN_MURUS_ABS(s[29],s).
        SI muris==0 TUNC muris=IN_MURUS_REL(s[28],s). FIN-SI.
'''
if old not in f:
    raise SystemExit('fenestrale: lectio muris vetus deest')
f = f.replace(old, '', 1)
FEN.write_text(f, encoding='utf-8')

# IV. Constructor UEFI: payload potest Fenestrale II esse; default nucleus manet.
b = BUILD.read_text(encoding='utf-8')
anchor = 'PONTICULUS="${PONTICULUS_FONS:-$RADIX/systema/uefi/ponticulus_uefi_purus.vindex}"\n'
if anchor not in b:
    raise SystemExit('build: PONTICULUS deest')
b = b.replace(anchor, anchor + 'NUCLEUS_FONS="${NUCLEUS_FONS:-$RADIX/systema/nucleus.vindex}"\n', 1)
old = '"$RADIX/compilator_vindex" "$RADIX/systema/nucleus.vindex" "$TEMPORARIUM/NUCLEUS.BIN"\n'
new = '"$RADIX/compilator_vindex" "$NUCLEUS_FONS" "$TEMPORARIUM/NUCLEUS.BIN"\n'
if old not in b:
    raise SystemExit('build: compilatio nuclei deest')
b = b.replace(old, new, 1)
BUILD.write_text(b, encoding='utf-8')

# V. Probationes: nova pagina fixa rectoris.
t = TESTM.read_text(encoding='utf-8')
if '0x03018840' not in t:
    raise SystemExit('probatio nuclei: vetus basis PS2 deest')
t = t.replace('0x03018840', '0x03019040')
TESTM.write_text(t, encoding='utf-8')

t = TESTF.read_text(encoding='utf-8')
old = '''def basis_ps2(monitor: socket.socket) -> int:
    v = hexa_hmp(hmp(monitor, "xp /1gx 0x03000b30"))
    return v[0] if v else 0
'''
new = '''def basis_ps2(monitor: socket.socket) -> int:
    # Contractus COMMUNIS: pagina rectoris PS/2 est 0x03019000.
    return 0x03019000
'''
if old not in t:
    raise SystemExit('probatio Fenestralis: basis metadata non inventa')
t = t.replace(old, new, 1)
TESTF.write_text(t, encoding='utf-8')

print('RECTE: P3 additive praeparatum est; nucleus historicus intactus manet.')
