#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
VIS = R / 'bibliotheca/fenestrale_ii_purus.vindex'
GEST = R / 'bibliotheca/fenestrale_gestor_i.vindex'
SYS = R / 'systema/fenestrale_ii_purus_i.vindex'
CONS = Path('CONSILIUM.md')


def munus_muta(textus: str, nomen: str, sequens: str, novum: str) -> str:
    initium = textus.index(f'FUNCTIO {nomen} REDDENS NUMERUS.')
    finis = textus.index(f'\nFUNCTIO {sequens} REDDENS NUMERUS.', initium)
    return textus[:initium] + novum.rstrip() + '\n' + textus[finis:]

# I. Metra INITIUM canonica.
t = VIS.read_text(encoding='utf-8')
ancora = '''FUNCTIO FV_METRUM_CLIENTIS REDDENS NUMERUS.
    REDDE 60.
FIN-FUNCTIO.
'''
add = '''FUNCTIO FV_METRUM_CLIENTIS REDDENS NUMERUS.
    REDDE 60.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_INITIUM_LATITUDO REDDENS NUMERUS.
    REDDE 320.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_INITIUM_ALTITUDO REDDENS NUMERUS.
    REDDE 260.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_INITIUM_CAPUT REDDENS NUMERUS.
    REDDE 60.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_INITIUM_ITEM REDDENS NUMERUS.
    REDDE 44.
FIN-FUNCTIO.
'''
if 'FUNCTIO FV_METRUM_INITIUM_LATITUDO REDDENS NUMERUS.' not in t:
    if ancora not in t: raise SystemExit('VIS: metrum clientis deest')
    t = t.replace(ancora, add, 1)
VIS.write_text(t, encoding='utf-8')

# II. Gestor: status menu in s[38], toggle, selectio et clausura extra menu.
t = GEST.read_text(encoding='utf-8')
if 'FUNCTIO GI_INITIUM_FENESTRA REDDENS NUMERUS.' not in t:
    t = t.replace('FUNCTIO GI_TASKBAR REDDENS NUMERUS.\n', '''FUNCTIO GI_INITIUM_FENESTRA REDDENS NUMERUS.
    ACCIPIT registrum SICUT NUMERUS.
    ACCIPIT cliens SICUT NUMERUS.
    SI registrum==0 || cliens<=0 TUNC REDDE 0. FIN-SI.
    DECLARA n SICUT NUMERUS VALENS FI_PRIMUS(registrum).
    DUM n!=0 PERFICE
        SI CONTENTUM(n+8)==cliens TUNC REDDE CONTENTUM(n). FIN-SI.
        n=FI_PROXIMUS(n).
    FIN-DUM.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO GI_INITIUM_ELIGE REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    ACCIPIT registrum SICUT NUMERUS.
    ACCIPIT cliens SICUT NUMERUS.
    DECLARA id SICUT NUMERUS VALENS GI_INITIUM_FENESTRA(registrum,cliens).
    SI id==0 TUNC s[38]=0. REDDE 0. FIN-SI.
    DECLARA r SICUT NUMERUS VALENS FI_STATUS_PONE(registrum,id,0).
    DECLARA f SICUT NUMERUS VALENS FI_FOCUS(registrum,id).
    s[38]=0.
    REDDE f.
FIN-FUNCTIO.

FUNCTIO GI_TASKBAR REDDENS NUMERUS.
''', 1)

gi_taskbar = '''FUNCTIO GI_TASKBAR REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    ACCIPIT registrum SICUT NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    SI registrum==0 TUNC REDDE 0. FIN-SI.
    SI x>=6 && x<110 TUNC
        SI s[38]==0 TUNC s[38]=1. ALITER s[38]=0. FIN-SI.
        REDDE 1.
    FIN-SI.
    s[38]=0.
    SI x<118 TUNC REDDE 0. FIN-SI.
    DECLARA numerus SICUT NUMERUS VALENS FI_APERTA_NUM(registrum).
    SI numerus<=0 TUNC REDDE 0. FIN-SI.
    DECLARA sw SICUT NUMERUS VALENS CONTENTUM(50333728).
    DECLARA finis SICUT NUMERUS VALENS sw-132.
    SI x>=finis TUNC REDDE 0. FIN-SI.
    DECLARA spatium SICUT NUMERUS VALENS finis-118.
    SI spatium<=0 TUNC REDDE 0. FIN-SI.
    DECLARA bw SICUT NUMERUS VALENS spatium/numerus.
    SI bw>196 TUNC bw=196. FIN-SI. SI bw<1 TUNC bw=1. FIN-SI.
    DECLARA index SICUT NUMERUS VALENS (x-118)/bw.
    SI index<0 || index>=numerus TUNC REDDE 0. FIN-SI.
    DECLARA id SICUT NUMERUS VALENS FI_APERTA_N(registrum,index).
    SI id==0 TUNC REDDE 0. FIN-SI.
    DECLARA status SICUT NUMERUS VALENS FI_STATUS(registrum,id).
    SI status==1 TUNC DECLARA r SICUT NUMERUS VALENS FI_STATUS_PONE(registrum,id,0). DECLARA f SICUT NUMERUS VALENS FI_FOCUS(registrum,id). REDDE 1. FIN-SI.
    SI FI_FOCUS_ID(registrum)==id TUNC DECLARA m SICUT NUMERUS VALENS FI_MINIMIZA(registrum,id). REDDE 1. FIN-SI.
    DECLARA f2 SICUT NUMERUS VALENS FI_FOCUS(registrum,id).
    REDDE 1.
FIN-FUNCTIO.'''
t = munus_muta(t, 'GI_TASKBAR', 'GI_MOUSE_DOWN', gi_taskbar)

gi_mouse = '''FUNCTIO GI_MOUSE_DOWN REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    ACCIPIT registrum SICUT NUMERUS.
    ACCIPIT coda SICUT NUMERUS.
    DECLARA mx SICUT NUMERUS VALENS s[11]. DECLARA my SICUT NUMERUS VALENS s[12].
    DECLARA taskbar_h SICUT NUMERUS VALENS FV_METRUM_TASKBAR().
    DECLARA tituli_h SICUT NUMERUS VALENS FV_METRUM_TITULUS().
    DECLARA clientis_y SICUT NUMERUS VALENS FV_METRUM_CLIENTIS().
    DECLARA screen_h SICUT NUMERUS VALENS CONTENTUM(50333736).
    DECLARA taskbar_top SICUT NUMERUS VALENS screen_h-taskbar_h.
    SI s[38]==1 TUNC
        DECLARA menu_x SICUT NUMERUS VALENS 6.
        DECLARA menu_w SICUT NUMERUS VALENS FV_METRUM_INITIUM_LATITUDO().
        DECLARA menu_h SICUT NUMERUS VALENS FV_METRUM_INITIUM_ALTITUDO().
        DECLARA menu_y SICUT NUMERUS VALENS taskbar_top-menu_h.
        SI mx>=menu_x && mx<menu_x+menu_w && my>=menu_y && my<taskbar_top TUNC
            DECLARA item1_y SICUT NUMERUS VALENS menu_y+92.
            DECLARA item2_y SICUT NUMERUS VALENS menu_y+146.
            DECLARA item_h SICUT NUMERUS VALENS FV_METRUM_INITIUM_ITEM().
            SI my>=item1_y && my<item1_y+item_h TUNC REDDE GI_INITIUM_ELIGE(s,registrum,1). FIN-SI.
            SI my>=item2_y && my<item2_y+item_h TUNC REDDE GI_INITIUM_ELIGE(s,registrum,2). FIN-SI.
            REDDE 1.
        FIN-SI.
        SI !(my>=taskbar_top && mx>=6 && mx<110) TUNC s[38]=0. FIN-SI.
    FIN-SI.
    SI my>=taskbar_top TUNC REDDE GI_TASKBAR(s,registrum,mx). FIN-SI.
    DECLARA id SICUT NUMERUS VALENS FI_HIT(registrum,mx,my).
    SI id==0 TUNC REDDE 0. FIN-SI.
    DECLARA foc SICUT NUMERUS VALENS FI_FOCUS(registrum,id).
    DECLARA n SICUT NUMERUS VALENS FI_QUAERE(registrum,id).
    SI n==0 TUNC REDDE 0. FIN-SI.
    DECLARA x SICUT NUMERUS VALENS CONTENTUM(n+16). DECLARA y SICUT NUMERUS VALENS CONTENTUM(n+24).
    DECLARA w SICUT NUMERUS VALENS CONTENTUM(n+32). DECLARA h SICUT NUMERUS VALENS CONTENTUM(n+40).
    DECLARA maximus SICUT NUMERUS VALENS CONTENTUM(n+56).
    DECLARA lx SICUT NUMERUS VALENS mx-x. DECLARA ly SICUT NUMERUS VALENS my-y.
    SI ly>=6 && ly<30 && lx>=w-32 && lx<w-8 TUNC DECLARA c SICUT NUMERUS VALENS FI_CLAUDE(registrum,id). REDDE 1. FIN-SI.
    SI ly>=6 && ly<30 && lx>=w-92 && lx<w-68 TUNC DECLARA m SICUT NUMERUS VALENS FI_MINIMIZA(registrum,id). REDDE 1. FIN-SI.
    SI ly>=6 && ly<30 && lx>=w-62 && lx<w-38 TUNC
        DECLARA z SICUT NUMERUS VALENS FI_MAX_TOGGLE(registrum,id,CONTENTUM(50333728),CONTENTUM(50333736)).
        REDDE 1.
    FIN-SI.
    SI maximus==0 TUNC
        DECLARA margines SICUT NUMERUS VALENS 0.
        SI lx>=0 && lx<6 TUNC margines=margines|1. FIN-SI. SI lx>=w-6 && lx<w TUNC margines=margines|2. FIN-SI.
        SI ly>=0 && ly<6 TUNC margines=margines|4. FIN-SI. SI ly>=h-6 && ly<h TUNC margines=margines|8. FIN-SI.
        SI margines!=0 TUNC s[14]=id. s[27]=margines. s[15]=mx. s[16]=my. REDDE 1. FIN-SI.
    FIN-SI.
    SI ly>=0 && ly<tituli_h && lx>=0 && lx<w-100 && maximus==0 TUNC
        s[14]=id. s[27]=0. s[15]=mx-x. s[16]=my-y. REDDE 1.
    FIN-SI.
    SI lx>=10 && ly>=clientis_y && lx<w-10 && ly<h-22 TUNC
        DECLARA cliens SICUT NUMERUS VALENS CONTENTUM(n+8).
        DECLARA positum SICUT NUMERUS VALENS EG_PONE(coda,1,cliens,lx-10,ly-clientis_y,0).
        SI positum==0 TUNC s[35]=s[35]+1. FIN-SI.
        REDDE 1.
    FIN-SI.
    REDDE foc.
FIN-FUNCTIO.'''
t = munus_muta(t, 'GI_MOUSE_DOWN', 'GI_DRAG', gi_mouse)
GEST.write_text(t, encoding='utf-8')

# III. Systema: pannus INITIUM, hover, et status s[38].
t = SYS.read_text(encoding='utf-8')
if 'FUNCTIO II_INITIUM REDDENS NUMERUS.' not in t:
    ancora = 'FUNCTIO II_TASKBAR REDDENS NUMERUS.\n'
    menu = '''FUNCTIO II_INITIUM REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    DECLARA screen_h SICUT NUMERUS VALENS CONTENTUM(50333736).
    DECLARA x SICUT NUMERUS VALENS 6.
    DECLARA w SICUT NUMERUS VALENS FV_METRUM_INITIUM_LATITUDO().
    DECLARA h SICUT NUMERUS VALENS FV_METRUM_INITIUM_ALTITUDO().
    DECLARA y SICUT NUMERUS VALENS screen_h-FV_METRUM_TASKBAR()-h.
    DECLARA profundum SICUT NUMERUS VALENS FV_COLOR(8,35,61).
    DECLARA vitrum SICUT NUMERUS VALENS FV_COLOR(14,66,111).
    DECLARA medium SICUT NUMERUS VALENS FV_COLOR(26,93,146).
    DECLARA aqua SICUT NUMERUS VALENS FV_COLOR(98,215,242).
    DECLARA lux SICUT NUMERUS VALENS FV_COLOR(234,248,255).
    DECLARA ebur SICUT NUMERUS VALENS FV_COLOR(241,238,228).
    DECLARA argentum SICUT NUMERUS VALENS FV_COLOR(185,196,207).
    DECLARA umbra SICUT NUMERUS VALENS FV_COLOR(4,18,31).
    DECLARA f SICUT NUMERUS VALENS FV_RECT(x+7,y+7,w,h,umbra).
    f=FV_RECT(x,y,w,h,ebur).
    f=FV_RECT(x,y,w,2,aqua).
    f=FV_RECT(x,y,w,FV_METRUM_INITIUM_CAPUT(),vitrum).
    f=FV_RECT(x,y,w,2,aqua).
    f=FV_TEXTUM_SCALA(x+18,y+14,"SYLVIA",lux,2).
    f=FV_TEXTUM(x+20,y+45,"SYSTEMA VINDEX",aqua).
    f=FV_TEXTUM(x+18,y+74,"APPLICATIONES",profundum).
    DECLARA item_h SICUT NUMERUS VALENS FV_METRUM_INITIUM_ITEM().
    DECLARA i1y SICUT NUMERUS VALENS y+92.
    DECLARA i2y SICUT NUMERUS VALENS y+146.
    DECLARA c1 SICUT NUMERUS VALENS lux.
    DECLARA c2 SICUT NUMERUS VALENS lux.
    SI s[11]>=x+10 && s[11]<x+w-10 && s[12]>=i1y && s[12]<i1y+item_h TUNC c1=argentum. FIN-SI.
    SI s[11]>=x+10 && s[11]<x+w-10 && s[12]>=i2y && s[12]<i2y+item_h TUNC c2=argentum. FIN-SI.
    f=FV_RECT(x+10,i1y,w-20,item_h,c1).
    f=FV_RECT(x+18,i1y+6,32,32,profundum).
    f=FV_RECT(x+23,i1y+11,22,22,aqua).
    f=FV_TEXTUM(x+64,i1y+18,"PROGRAMMATA",profundum).
    f=FV_RECT(x+10,i2y,w-20,item_h,c2).
    f=FV_RECT(x+18,i2y+6,32,32,profundum).
    f=FV_RECT(x+23,i2y+11,8,8,aqua).
    f=FV_RECT(x+35,i2y+11,10,8,medium).
    f=FV_RECT(x+23,i2y+23,22,10,aqua).
    f=FV_TEXTUM(x+64,i2y+18,"TABULA",profundum).
    f=FV_RECT(x+10,y+h-48,w-20,1,argentum).
    f=FV_TEXTUM(x+18,y+h-30,"VINDEX 0.53",medium).
    f=FV_TEXTUM(x+w-86,y+h-30,"P16-II",medium).
    REDDE 1.
FIN-FUNCTIO.

FUNCTIO II_TASKBAR REDDENS NUMERUS.
'''
    if ancora not in t: raise SystemExit('SYS: II_TASKBAR deest')
    t = t.replace(ancora, menu, 1)

t = t.replace('// 34 coda eventuum; 35 eventa perdita; 36 registrum clientium; 37 registrum fenestrarum.',
              '// 34 coda eventuum; 35 eventa perdita; 36 registrum clientium; 37 registrum fenestrarum; 38 INITIUM apertum.', 1)
old = '    f=II_TASKBAR(fenestrae,clientes).\n    f=FV_CURSOR(s[11],s[12]).'
new = '    SI s[38]==1 TUNC f=II_INITIUM(s). FIN-SI.\n    f=II_TASKBAR(fenestrae,clientes).\n    f=FV_CURSOR(s[11],s[12]).'
if old not in t: raise SystemExit('SYS: compositio taskbar deest')
t = t.replace(old,new,1)
old = '    s[28]=0. s[29]=0. s[35]=0.\n'
new = '    s[28]=0. s[29]=0. s[35]=0. s[38]=0.\n'
if old not in t: raise SystemExit('SYS: initium status deest')
t = t.replace(old,new,1)
SYS.write_text(t, encoding='utf-8')

# IV. Tabula magistra: P16-I perfectum, P16-II activum/probandum in hoc ramo.
t = CONS.read_text(encoding='utf-8')
t = t.replace('**Status:** `PROBATUM / CANONIZANDUM — incrementum I`.',
              '**Status:** `PERFECTUM per PR #113 — incrementum I; ACTIVUM — incrementum II`.', 1)
t = t.replace('### Incrementa sequentia\n\nP16-II et posteriora iconographiam, fontem maturiorem, menu INITIUM functionale, widgeta communia, status interactionis et thema paulatim tractabunt.',
              '### Incrementum II activum\n\nP16-II menu **INITIUM** functionale construit: pannus systematis, applicationes PROGRAMMATA/TABULA, hover, apertio/clausura et focus/restauratio ex eodem contractu input. Incrementa posteriora iconographiam, fontem maturiorem, widgeta communia, status interactionis et thema paulatim tractabunt.', 1)
t = t.replace('1. P16-I canonizare et P16-II per iconographiam, fontem vel menu INITIUM parvum continuare;',
              '1. P16-II menu INITIUM functionale sub QEMU/OVMF probare et canonizare;', 1)
CONS.write_text(t, encoding='utf-8')

print('RECTE: P16-II INITIUM functionale paratum est.')
