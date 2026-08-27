#!/usr/bin/env python3
from pathlib import Path
import re

R = Path('Vindex Chat-GPT/vindex_final_v51')
PONS = R / 'systema/uefi/ponticulus_uefi_purus.vindex'
MUS = R / 'systema/rectores/murus_ps2.vindex'
NUC = R / 'systema/nucleus.vindex'
INPUT = R / 'bibliotheca/fenestrale_input_i.vindex'
FEN = R / 'systema/fenestrale_ii_purus_i.vindex'
BUILD = R / 'systema/uefi/construe_uefi_purum.sh'
TESTM = R / 'instrumenta/proba_murem_uefi_053.py'

# I. Ponticulus: paginam separatam rectori PS/2 reserva et per metadata trade.
p = PONS.read_text(encoding='utf-8')
old = '''    CONTENTUM(locus_mem) = meta.
    DECLARA sc2 SICUT NUMERUS VALENS UEFI_VOCA6(alloca, 2, 2, 64, locus_mem, 0, 0).

    SI reservata == 0 TUNC REDDE 14. FIN-SI.
'''
new = '''    CONTENTUM(locus_mem) = meta.
    DECLARA sc2 SICUT NUMERUS VALENS UEFI_VOCA6(alloca, 2, 2, 64, locus_mem, 0, 0).

    // Rectoribus nativis pagina propria extra COMMUNIS/acervum datur. Sic
    // stubs I/O PS/2 neque a volumine neque ab allocationibus dynamicis delentur.
    CONTENTUM(locus_mem) = 0.
    DECLARA sr_rect SICUT NUMERUS VALENS UEFI_VOCA6(alloca, 0, 2, 1, locus_mem, 0, 0).
    SI sr_rect != 0 || CONTENTUM(locus_mem) == 0 TUNC REDDE 19. FIN-SI.
    DECLARA sedes_rectorum SICUT NUMERUS VALENS CONTENTUM(locus_mem).

    SI reservata == 0 TUNC REDDE 14. FIN-SI.
'''
if old not in p: raise SystemExit('ponticulus: contractus memoriae non inventus')
p = p.replace(old, new, 1)
old = '    CONTENTUM(50334504) = moderatores_n.\n'
new = old + '    CONTENTUM(50334512) = sedes_rectorum.\n'
if old not in p: raise SystemExit('ponticulus: metadata moderatorum non inventa')
p = p.replace(old, new, 1)
PONS.write_text(p, encoding='utf-8')

# II. Rector PS/2: regio dedicata + eventus crudus, sine dependentia a nucleo.
m = MUS.read_text(encoding='utf-8')
for a, expr in [
    ('50432000', 'PS2_BASIS()'), ('50432016', 'PS2_BASIS() + 16'),
    ('50432064', 'PS2_BASIS() + 64'), ('50432065', 'PS2_BASIS() + 65'),
    ('50432066', 'PS2_BASIS() + 66'), ('50432067', 'PS2_BASIS() + 67'),
    ('50432068', 'PS2_BASIS() + 68'), ('50432069', 'PS2_BASIS() + 69'),
    ('50432070', 'PS2_BASIS() + 70'), ('50432071', 'PS2_BASIS() + 71'),
]:
    m = m.replace(a, expr)
# Commentarium telemetriae post substitutionem nimis mechanicum; canonice rescribe.
start = m.index('// Telemetria rectoris:')
end = m.index('\n\nFUNCTIO PS2_STUBS_PARA', start)
comment = '''// Regio rectoris a ponticulo UEFI in metadata 50334512 traditur.
// Si metadata deest (via historica non-UEFI), basis 50432000 adhibetur.
// Offsets intra regionem:
//   +64 status initializationis (9 = paratus); +65 ACK F6; +66 ACK F4;
//   +67 numerus fasciculorum; +68 status 8042; +69 positio fasciculi;
//   +70 flags; +71 dx octetum; +72 dx signatum; +80 dy signatum; +88 bullae.

FUNCTIO PS2_BASIS REDDENS NUMERUS.
    DECLARA basis SICUT NUMERUS VALENS CONTENTUM(50334512).
    SI basis == 0 TUNC basis = 50432000. FIN-SI.
    REDDE basis.
FIN-FUNCTIO.'''
m = m[:start] + comment + m[end:]
# Status crudus initur.
old = '''    SCRIBE_OCTETUM_AB(PS2_BASIS() + 69, 0).
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 70, 0).
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 71, 0).
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 64, 9).
'''
new = '''    SCRIBE_OCTETUM_AB(PS2_BASIS() + 69, 0).
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 70, 0).
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 71, 0).
    CONTENTUM(PS2_BASIS() + 72) = 0.
    CONTENTUM(PS2_BASIS() + 80) = 0.
    CONTENTUM(PS2_BASIS() + 88) = 0.
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 64, 9).
'''
if old not in m: raise SystemExit('murus: initium telemetriae non inventum')
m = m.replace(old, new, 1)
# Accessores crudi post PARATUS.
anchor = '''FUNCTIO PS2_PARATUS_EST REDDENS NUMERUS.
    SI OCTETUS_AB(PS2_BASIS() + 64) == 9 TUNC REDDE 1. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

'''
extra = anchor + '''FUNCTIO PS2_DX REDDENS NUMERUS.
    REDDE CONTENTUM(PS2_BASIS() + 72).
FIN-FUNCTIO.

FUNCTIO PS2_DY REDDENS NUMERUS.
    REDDE CONTENTUM(PS2_BASIS() + 80).
FIN-FUNCTIO.

FUNCTIO PS2_BULLAE REDDENS NUMERUS.
    REDDE CONTENTUM(PS2_BASIS() + 88).
FIN-FUNCTIO.

'''
if anchor not in m: raise SystemExit('murus: PS2_PARATUS_EST non inventa')
m = m.replace(anchor, extra, 1)
# Finis packet decoder: nunc eventum crudum publicat, non statum nuclei.
old = '''    DECLARA x SICUT NUMERUS VALENS CONTENTUM(50331648) + dx.
    DECLARA y SICUT NUMERUS VALENS CONTENTUM(50331656) - dy.
    DECLARA bullae SICUT NUMERUS VALENS flags & 7.
    DECLARA mutatum SICUT NUMERUS VALENS UEFI_MURIS_PUBLICA(x, y, bullae).
    SI mutatum != 0 TUNC
        SCRIBE_OCTETUM_AB(PS2_BASIS() + 67, (OCTETUS_AB(PS2_BASIS() + 67) + 1) & 255).
    FIN-SI.
    REDDE mutatum.
'''
new = '''    DECLARA bullae SICUT NUMERUS VALENS flags & 7.
    CONTENTUM(PS2_BASIS() + 72) = dx.
    CONTENTUM(PS2_BASIS() + 80) = dy.
    CONTENTUM(PS2_BASIS() + 88) = bullae.
    SCRIBE_OCTETUM_AB(PS2_BASIS() + 67, (OCTETUS_AB(PS2_BASIS() + 67) + 1) & 255).
    REDDE 1.
'''
if old not in m: raise SystemExit('murus: publicatio nuclei non inventa')
m = m.replace(old, new, 1)
MUS.write_text(m, encoding='utf-8')

# III. Nucleus historicus: eventum crudum in coordinatas 320x200 convertit.
n = NUC.read_text(encoding='utf-8')
old = '''        ma = PS2_POLLE().
'''
new = '''        DECLARA fasciculus_ps2 SICUT NUMERUS VALENS PS2_POLLE().
        SI fasciculus_ps2 != 0 TUNC
            DECLARA ps2_x SICUT NUMERUS VALENS CONTENTUM(50331648) + PS2_DX().
            DECLARA ps2_y SICUT NUMERUS VALENS CONTENTUM(50331656) - PS2_DY().
            ma = UEFI_MURIS_PUBLICA(ps2_x, ps2_y, PS2_BULLAE()).
        FIN-SI.
'''
if old not in n: raise SystemExit('nucleus: PS2_POLLE non inventum')
n = n.replace(old, new, 1)
NUC.write_text(n, encoding='utf-8')

# IV. Fenestrale input: PS/2 nativus prima via, firmware fallback.
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
    // Omnes allocationes Fenestralis iam factae sunt cum IN_PARA vocatur;
    // rector PS/2 igitur hic, proxime ante ansam eventuum, paratur.
    s[30]=PS2_PARA().
    REDDE 1.
FIN-FUNCTIO.
'''
if old not in i: raise SystemExit('input: finis IN_PARA non inventus')
i = i.replace(old, new, 1)
anchor = '''FUNCTIO IN_STALL REDDENS NUMERUS.
'''
fun = '''FUNCTIO IN_MURUS REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    SI PS2_PARATUS_EST()==1 TUNC
        DECLARA eventus SICUT NUMERUS VALENS 0.
        DECLARA i SICUT NUMERUS VALENS 0.
        // Usque ad octo octeta ex canali AUX haurimus. Octetum claviaturae
        // non consumitur quia PS2_POLLE bit AUX ante 0x60 inspicit.
        DUM i<8 PERFICE
            DECLARA p SICUT NUMERUS VALENS PS2_POLLE().
            SI p!=0 TUNC eventus=1. FIN-SI.
            i=i+1.
        FIN-DUM.
        SI eventus==0 TUNC REDDE 0. FIN-SI.
        s[11]=s[11]+PS2_DX().
        s[12]=s[12]-PS2_DY().
        SI s[11]<0 TUNC s[11]=0. FIN-SI. SI s[12]<0 TUNC s[12]=0. FIN-SI.
        SI s[11]>=CONTENTUM(50333728) TUNC s[11]=CONTENTUM(50333728)-1. FIN-SI.
        SI s[12]>=CONTENTUM(50333736) TUNC s[12]=CONTENTUM(50333736)-1. FIN-SI.
        REDDE (PS2_BULLAE()&3)+1.
    FIN-SI.
    DECLARA muris SICUT NUMERUS VALENS IN_MURUS_ABS(s[29],s).
    SI muris==0 TUNC muris=IN_MURUS_REL(s[28],s). FIN-SI.
    REDDE muris.
FIN-FUNCTIO.

'''
if anchor not in i: raise SystemExit('input: IN_STALL non inventa')
i = i.replace(anchor, fun + anchor, 1)
INPUT.write_text(i, encoding='utf-8')

# V. Fenestrale I: rectorem top-level importa; PS/2 ante claviaturam pollitur.
f = FEN.read_text(encoding='utf-8')
imp_anchor = 'IMPORTA "bibliotheca/fenestrale_ii_purus.vindex".\n'
if imp_anchor not in f: raise SystemExit('fenestrale: import anchor deest')
f = f.replace(imp_anchor, 'IMPORTA "systema/rectores/murus_ps2.vindex".\n' + imp_anchor, 1)
loop_anchor = '''    DUM finis==0 PERFICE
        DECLARA redde SICUT NUMERUS VALENS 0.
        DECLARA q SICUT NUMERUS VALENS IN_CLAVIS().
'''
loop_new = '''    DUM finis==0 PERFICE
        DECLARA redde SICUT NUMERUS VALENS 0.
        // AUX/PS2 ante claviaturam firmware pollitur ne byte commune 8042 rapiatur.
        DECLARA muris SICUT NUMERUS VALENS IN_MURUS(s).
        DECLARA q SICUT NUMERUS VALENS IN_CLAVIS().
'''
if loop_anchor not in f: raise SystemExit('fenestrale: initium ansae deest')
f = f.replace(loop_anchor, loop_new, 1)
old = '''        DECLARA muris SICUT NUMERUS VALENS IN_MURUS_ABS(s[29],s).
        SI muris==0 TUNC muris=IN_MURUS_REL(s[28],s). FIN-SI.
'''
if old not in f: raise SystemExit('fenestrale: lectio muris vetus deest')
f = f.replace(old, '', 1)
FEN.write_text(f, encoding='utf-8')

# VI. Constructor UEFI: fons payload potest override fieri; default historicus manet.
b = BUILD.read_text(encoding='utf-8')
anchor = 'PONTICULUS="${PONTICULUS_FONS:-$RADIX/systema/uefi/ponticulus_uefi_purus.vindex}"\n'
if anchor not in b: raise SystemExit('build: PONTICULUS deest')
b = b.replace(anchor, anchor + 'NUCLEUS_FONS="${NUCLEUS_FONS:-$RADIX/systema/nucleus.vindex}"\n', 1)
old = '"$RADIX/compilator_vindex" "$RADIX/systema/nucleus.vindex" "$TEMPORARIUM/NUCLEUS.BIN"\n'
new = '"$RADIX/compilator_vindex" "$NUCLEUS_FONS" "$TEMPORARIUM/NUCLEUS.BIN"\n'
if old not in b: raise SystemExit('build: compilatio nuclei deest')
b = b.replace(old, new, 1)
BUILD.write_text(b, encoding='utf-8')

# VII. Probatio nuclei historici: basis rectoris ex metadata, non ex sede fixa.
t = TESTM.read_text(encoding='utf-8')
old = '''def status_ps2(monitor: socket.socket) -> list[int]:
    return hexa_hmp(hmp(monitor, "xp /9bx 0x03018840"))[:9]
'''
new = '''def basis_ps2(monitor: socket.socket) -> int:
    valores = hexa_hmp(hmp(monitor, "xp /1gx 0x03000b30"))
    return valores[0] if valores else 0


def status_ps2(monitor: socket.socket) -> list[int]:
    basis = basis_ps2(monitor)
    if basis == 0:
        return []
    return hexa_hmp(hmp(monitor, f"xp /9bx 0x{basis + 64:x}"))[:9]
'''
if old not in t: raise SystemExit('test muris: status_ps2 vetus deest')
t = t.replace(old, new, 1)
TESTM.write_text(t, encoding='utf-8')

print('RECTE: strata P3 Fenestrale/PS2/UEFI praeparata sunt.')
