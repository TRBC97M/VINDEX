#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
VIS = R / 'bibliotheca/fenestrale_ii_purus.vindex'
GEST = R / 'bibliotheca/fenestrale_gestor_i.vindex'
SYS = R / 'systema/fenestrale_ii_purus_i.vindex'
FORMA = R / 'instrumenta/proba_formam_sylviae_i.py'


def munus_muta(textus: str, nomen: str, sequens: str, novum: str) -> str:
    initium = textus.index(f'FUNCTIO {nomen} REDDENS NUMERUS.')
    finis = textus.index(f'\nFUNCTIO {sequens} REDDENS NUMERUS.', initium)
    return textus[:initium] + novum.rstrip() + '\n' + textus[finis:]


# I. Metra bureau communia.
t = VIS.read_text(encoding='utf-8')
ancora = '''FUNCTIO FV_METRUM_INITIUM_ITEM REDDENS NUMERUS.
    REDDE 44.
FIN-FUNCTIO.
'''
if 'FUNCTIO FV_METRUM_BUREAU_X REDDENS NUMERUS.' not in t:
    add = ancora + '''
FUNCTIO FV_METRUM_BUREAU_X REDDENS NUMERUS.
    REDDE 18.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_BUREAU_LATITUDO REDDENS NUMERUS.
    REDDE 108.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_BUREAU_ALTITUDO REDDENS NUMERUS.
    REDDE 88.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_BUREAU_PROGRAMMATA_Y REDDENS NUMERUS.
    REDDE 72.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_BUREAU_TABULA_Y REDDENS NUMERUS.
    REDDE 176.
FIN-FUNCTIO.
'''
    if ancora not in t:
        raise SystemExit('VIS: metrum INITIUM item deest')
    t = t.replace(ancora, add, 1)
VIS.write_text(t, encoding='utf-8')


# II. Gestor: desktop tantum si nulla fenestra super coordinata est.
t = GEST.read_text(encoding='utf-8')
if 'FUNCTIO GI_BUREAU REDDENS NUMERUS.' not in t:
    ancora = 'FUNCTIO GI_MOUSE_DOWN REDDENS NUMERUS.\n'
    add = '''FUNCTIO GI_BUREAU REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    ACCIPIT registrum SICUT NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    ACCIPIT y SICUT NUMERUS.
    DECLARA bx SICUT NUMERUS VALENS FV_METRUM_BUREAU_X().
    DECLARA bw SICUT NUMERUS VALENS FV_METRUM_BUREAU_LATITUDO().
    DECLARA bh SICUT NUMERUS VALENS FV_METRUM_BUREAU_ALTITUDO().
    DECLARA py SICUT NUMERUS VALENS FV_METRUM_BUREAU_PROGRAMMATA_Y().
    DECLARA ty SICUT NUMERUS VALENS FV_METRUM_BUREAU_TABULA_Y().
    SI x>=bx && x<bx+bw && y>=py && y<py+bh TUNC
        REDDE GI_INITIUM_ELIGE(s,registrum,1).
    FIN-SI.
    SI x>=bx && x<bx+bw && y>=ty && y<ty+bh TUNC
        REDDE GI_INITIUM_ELIGE(s,registrum,2).
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO GI_MOUSE_DOWN REDDENS NUMERUS.
'''
    if ancora not in t:
        raise SystemExit('GEST: GI_MOUSE_DOWN deest')
    t = t.replace(ancora, add, 1)
old = '    DECLARA id SICUT NUMERUS VALENS FI_HIT(registrum,mx,my).\n    SI id==0 TUNC REDDE 0. FIN-SI.\n'
new = '    DECLARA id SICUT NUMERUS VALENS FI_HIT(registrum,mx,my).\n    SI id==0 TUNC REDDE GI_BUREAU(s,registrum,mx,my). FIN-SI.\n'
if old not in t:
    raise SystemExit('GEST: exitus sine fenestra deest')
t = t.replace(old, new, 1)
GEST.write_text(t, encoding='utf-8')


# III. Systema: bureau pingitur ante fenestras; fenestrae initio clausae sunt.
t = SYS.read_text(encoding='utf-8')
if 'FUNCTIO II_BUREAU REDDENS NUMERUS.' not in t:
    ancora = 'FUNCTIO II_INITIUM REDDENS NUMERUS.\n'
    bureau = '''FUNCTIO II_BUREAU REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    DECLARA bx SICUT NUMERUS VALENS FV_METRUM_BUREAU_X().
    DECLARA bw SICUT NUMERUS VALENS FV_METRUM_BUREAU_LATITUDO().
    DECLARA bh SICUT NUMERUS VALENS FV_METRUM_BUREAU_ALTITUDO().
    DECLARA py SICUT NUMERUS VALENS FV_METRUM_BUREAU_PROGRAMMATA_Y().
    DECLARA ty SICUT NUMERUS VALENS FV_METRUM_BUREAU_TABULA_Y().
    DECLARA profundum SICUT NUMERUS VALENS FV_COLOR(8,35,61).
    DECLARA vitrum SICUT NUMERUS VALENS FV_COLOR(14,66,111).
    DECLARA medium SICUT NUMERUS VALENS FV_COLOR(26,93,146).
    DECLARA aqua SICUT NUMERUS VALENS FV_COLOR(98,215,242).
    DECLARA lux SICUT NUMERUS VALENS FV_COLOR(234,248,255).
    DECLARA argentum SICUT NUMERUS VALENS FV_COLOR(185,196,207).
    DECLARA f SICUT NUMERUS VALENS FV_TEXTUM_SCALA(18,18,"SYLVIA",lux,2).
    f=FV_TEXTUM(20,48,"SYSTEMA VINDEX",aqua).
    DECLARA cp SICUT NUMERUS VALENS vitrum.
    DECLARA ct SICUT NUMERUS VALENS vitrum.
    SI s[11]>=bx && s[11]<bx+bw && s[12]>=py && s[12]<py+bh TUNC cp=argentum. FIN-SI.
    SI s[11]>=bx && s[11]<bx+bw && s[12]>=ty && s[12]<ty+bh TUNC ct=argentum. FIN-SI.
    f=FV_RECT(bx,py,bw,bh,cp).
    f=FV_RECT(bx+30,py+10,48,38,profundum).
    f=FV_RECT(bx+34,py+14,40,30,aqua).
    f=FV_RECT(bx+40,py+20,10,8,medium).
    f=FV_RECT(bx+56,py+20,12,8,medium).
    f=FV_RECT(bx+40,py+32,28,8,medium).
    f=FV_TEXTUM(bx+10,py+66,"PROGRAMMATA",lux).
    f=FV_RECT(bx,ty,bw,bh,ct).
    f=FV_RECT(bx+30,ty+10,48,38,profundum).
    f=FV_RECT(bx+35,ty+15,14,12,aqua).
    f=FV_RECT(bx+55,ty+15,18,12,medium).
    f=FV_RECT(bx+35,ty+33,38,10,aqua).
    f=FV_TEXTUM(bx+26,ty+66,"TABULA",lux).
    REDDE 1.
FIN-FUNCTIO.

FUNCTIO II_INITIUM REDDENS NUMERUS.
'''
    if ancora not in t:
        raise SystemExit('SYS: II_INITIUM deest')
    t = t.replace(ancora, bureau, 1)
old = '    DECLARA f SICUT NUMERUS VALENS FV_FUNDUM().\n    DECLARA focus SICUT NUMERUS VALENS FI_RELEGE_FOCUS(fenestrae).\n'
new = '    DECLARA f SICUT NUMERUS VALENS FV_FUNDUM().\n    f=II_BUREAU(s).\n    DECLARA focus SICUT NUMERUS VALENS FI_RELEGE_FOCUS(fenestrae).\n'
if old not in t:
    raise SystemExit('SYS: initium II_REDDE deest')
t = t.replace(old, new, 1)
old = '''    DECLARA fp SICUT NUMERUS VALENS FI_ADDE(s[37],1,px,py,pw,ph).
    DECLARA ft SICUT NUMERUS VALENS FI_ADDE(s[37],2,tx,ty,tw,th).
    SI fp==0 || ft==0 || FI_NUMERUS(s[37])!=2 TUNC REDDE 71. FIN-SI.
    DECLARA foc SICUT NUMERUS VALENS FI_FOCUS(s[37],fp).
'''
new = '''    DECLARA fp SICUT NUMERUS VALENS FI_ADDE(s[37],1,px,py,pw,ph).
    DECLARA ft SICUT NUMERUS VALENS FI_ADDE(s[37],2,tx,ty,tw,th).
    SI fp==0 || ft==0 || FI_NUMERUS(s[37])!=2 TUNC REDDE 71. FIN-SI.
    DECLARA sp SICUT NUMERUS VALENS FI_STATUS_PONE(s[37],fp,2).
    DECLARA st SICUT NUMERUS VALENS FI_STATUS_PONE(s[37],ft,2).
    SI sp==0 || st==0 TUNC REDDE 71. FIN-SI.
'''
if old not in t:
    raise SystemExit('SYS: fenestrae initiales deest')
t = t.replace(old, new, 1)
SYS.write_text(t, encoding='utf-8')


# IV. Probatio P16-I nunc faciem fundamentalem bureau, non fenestram initio apertam, custodit.
t = FORMA.read_text(encoding='utf-8')
old = '''        # Fenestra PROGRAMMATA initialiter focus habet: x≈76, y≈56.
        # Ad x=300 titulus novus usque ad y+35 manet; corpus incipit ad y+36.
        if pixel(pix, w, 300, 88) != vitrum:
            print(f"DEFECIT: titulus fenestrae XXXVI px non detectus: {pixel(pix,w,300,88)}", file=sys.stderr)
            return 9
        if pixel(pix, w, 300, 96) != ebur:
            print(f"DEFECIT: regio sub titulo non detecta: {pixel(pix,w,300,96)}", file=sys.stderr)
            return 10

        # Titulus 2× debet multo plures pixeles lucidos quam vetus 8×8 simplex.
        lux_tituli = numerus_coloris_in_recto(pix, w, 86, 62, 260, 92, lux)
        if lux_tituli < 300:
            print(f"DEFECIT: titulus 2x non videtur: lux={lux_tituli}", file=sys.stderr)
            return 11
'''
new = '''        # P16-III bootat in bureau mundo; duae tesserae applicationum debent adesse.
        if pixel(pix, w, 20, 74) != vitrum:
            print(f"DEFECIT: tessera PROGRAMMATA bureau deest: {pixel(pix,w,20,74)}", file=sys.stderr)
            return 9
        if pixel(pix, w, 20, 178) != vitrum:
            print(f"DEFECIT: tessera TABULA bureau deest: {pixel(pix,w,20,178)}", file=sys.stderr)
            return 10

        # Textus 2× manet contractus P16-I; nunc marca SYLVIA in bureau eum exercet.
        lux_tituli = numerus_coloris_in_recto(pix, w, 16, 16, 150, 48, lux)
        if lux_tituli < 250:
            print(f"DEFECIT: marca SYLVIA 2x non videtur: lux={lux_tituli}", file=sys.stderr)
            return 11
'''
if old not in t:
    raise SystemExit('FORMA: contractus fenestrae P16-I deest')
t = t.replace(old, new, 1)
t = t.replace('print(f"FORMA: linea_aqua={linea_aqua} linea_profunda={linea_profunda} lux_tituli={lux_tituli}")',
              'print(f"FORMA: linea_aqua={linea_aqua} linea_profunda={linea_profunda} lux_bureau_2x={lux_tituli}")', 1)
FORMA.write_text(t, encoding='utf-8')

print('RECTE: P16-III bureau functionale paratum est.')
