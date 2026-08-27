#!/usr/bin/env python3
from pathlib import Path

R = Path('Vindex Chat-GPT/vindex_final_v51')
VIS = R / 'bibliotheca/fenestrale_ii_purus.vindex'
GEST = R / 'bibliotheca/fenestrale_gestor_i.vindex'
REG = R / 'bibliotheca/fenestrae_registrum_i.vindex'
SYS = R / 'systema/fenestrale_ii_purus_i.vindex'
HAR = R / 'instrumenta/proba_fenestrale_uefi_purum.sh'


def munus_muta(textus: str, nomen: str, sequens: str, novum: str) -> str:
    initium = textus.index(f'FUNCTIO {nomen} REDDENS NUMERUS.')
    finis = textus.index(f'\nFUNCTIO {sequens} REDDENS NUMERUS.', initium)
    return textus[:initium] + novum.rstrip() + '\n' + textus[finis:]


# I. Metrica canonica et textus scalaris.
t = VIS.read_text(encoding='utf-8')
ancora = '\nFUNCTIO FV_FUNDUM REDDENS NUMERUS.\n'
if 'FUNCTIO FV_METRUM_TASKBAR REDDENS NUMERUS.' not in t:
    add = '''
FUNCTIO FV_METRUM_TASKBAR REDDENS NUMERUS.
    REDDE 40.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_TITULUS REDDENS NUMERUS.
    REDDE 36.
FIN-FUNCTIO.

FUNCTIO FV_METRUM_CLIENTIS REDDENS NUMERUS.
    REDDE 60.
FIN-FUNCTIO.

FUNCTIO FV_TEXTUM_SCALA REDDENS NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    ACCIPIT y SICUT NUMERUS.
    ACCIPIT textus SICUT TEXTUS.
    ACCIPIT color SICUT NUMERUS.
    ACCIPIT scala SICUT NUMERUS.
    SI scala < 1 TUNC scala = 1. FIN-SI.
    DECLARA forma SICUT NUMERUS VALENS CONTENTUM(50333784).
    SI forma == 0 TUNC REDDE 0. FIN-SI.
    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(textus).
    DECLARA i SICUT NUMERUS VALENS 0.
    DUM i < longitudo PERFICE
        DECLARA littera SICUT NUMERUS VALENS OCTETUS_AB(textus + 8 + i).
        DECLARA py SICUT NUMERUS VALENS 0.
        DUM py < 8 PERFICE
            DECLARA bits SICUT NUMERUS VALENS OCTETUS_AB(forma + littera * 8 + py).
            DECLARA px SICUT NUMERUS VALENS 0.
            DUM px < 8 PERFICE
                SI (bits & (128 >> px)) != 0 TUNC
                    DECLARA f SICUT NUMERUS VALENS FV_RECT(x + i * 8 * scala + px * scala, y + py * scala, scala, scala, color).
                FIN-SI.
                px = px + 1.
            FIN-DUM.
            py = py + 1.
        FIN-DUM.
        i = i + 1.
    FIN-DUM.
    REDDE 1.
FIN-FUNCTIO.
'''
    if ancora not in t:
        raise SystemExit('visualia: ancora FV_FUNDUM deest')
    t = t.replace(ancora, add + ancora, 1)

fenestra = '''FUNCTIO FV_FENESTRA REDDENS NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    ACCIPIT y SICUT NUMERUS.
    ACCIPIT w SICUT NUMERUS.
    ACCIPIT h SICUT NUMERUS.
    ACCIPIT titulus SICUT TEXTUS.
    ACCIPIT activa SICUT NUMERUS.
    DECLARA ebur SICUT NUMERUS VALENS FV_COLOR(241, 238, 228).
    DECLARA argentum SICUT NUMERUS VALENS FV_COLOR(185, 196, 207).
    DECLARA profundum SICUT NUMERUS VALENS FV_COLOR(8, 35, 61).
    DECLARA vitrum SICUT NUMERUS VALENS FV_COLOR(14, 66, 111).
    DECLARA medium SICUT NUMERUS VALENS FV_COLOR(26, 93, 146).
    DECLARA aqua SICUT NUMERUS VALENS FV_COLOR(98, 215, 242).
    DECLARA lux SICUT NUMERUS VALENS FV_COLOR(234, 248, 255).
    DECLARA bronzeum SICUT NUMERUS VALENS FV_COLOR(185, 138, 82).
    DECLARA rubrum SICUT NUMERUS VALENS FV_COLOR(168, 58, 58).
    DECLARA tituli_h SICUT NUMERUS VALENS FV_METRUM_TITULUS().
    DECLARA clientis_y SICUT NUMERUS VALENS FV_METRUM_CLIENTIS().
    DECLARA margo SICUT NUMERUS VALENS argentum.
    SI activa == 1 TUNC margo = bronzeum. FIN-SI.
    DECLARA f SICUT NUMERUS VALENS FV_RECT(x + 7, y + 8, w, h, FV_COLOR(4, 18, 31)).
    f = FV_RECT(x, y, w, h, ebur).
    f = FV_RECT(x, y, w, 2, margo).
    f = FV_RECT(x, y, 2, h, argentum).
    f = FV_RECT(x + w - 2, y, 2, h, profundum).
    f = FV_RECT(x, y + h - 2, w, 2, profundum).
    f = FV_RECT(x + 2, y + 2, w - 4, tituli_h - 3, vitrum).
    f = FV_RECT(x + 2, y + 2, w - 4, 2, aqua).
    SI activa == 0 TUNC f = FV_RECT(x + 2, y + 4, w - 4, tituli_h - 5, medium). FIN-SI.
    f = FV_TEXTUM_SCALA(x + 12, y + 10, titulus, lux, 2).
    f = FV_RECT(x + w - 92, y + 6, 24, 24, argentum).
    f = FV_RECT(x + w - 62, y + 6, 24, 24, argentum).
    f = FV_RECT(x + w - 32, y + 6, 24, 24, rubrum).
    f = FV_RECT(x + w - 86, y + 23, 12, 2, profundum).
    f = FV_RECT(x + w - 56, y + 11, 12, 2, profundum).
    f = FV_RECT(x + w - 56, y + 11, 2, 12, profundum).
    f = FV_RECT(x + w - 46, y + 11, 2, 12, profundum).
    f = FV_RECT(x + w - 56, y + 21, 12, 2, profundum).
    f = FV_RECT(x + w - 26, y + 12, 12, 2, lux).
    f = FV_RECT(x + w - 21, y + 7, 2, 12, lux).
    f = FV_RECT(x + 2, y + tituli_h, w - 4, clientis_y - tituli_h, ebur).
    f = FV_RECT(x + 2, y + clientis_y - 1, w - 4, 1, argentum).
    f = FV_RECT(x + 2, y + h - 20, w - 4, 18, argentum).
    REDDE 1.
FIN-FUNCTIO.'''
t = munus_muta(t, 'FV_FENESTRA', 'FV_PROGRAMMATA', fenestra)

taskbar = '''FUNCTIO FV_TASKBAR REDDENS NUMERUS.
    ACCIPIT status_programmata SICUT NUMERUS.
    ACCIPIT status_tabula SICUT NUMERUS.
    ACCIPIT activum SICUT NUMERUS.
    DECLARA w SICUT NUMERUS VALENS CONTENTUM(50333728).
    DECLARA h SICUT NUMERUS VALENS CONTENTUM(50333736).
    DECLARA th SICUT NUMERUS VALENS FV_METRUM_TASKBAR().
    DECLARA top SICUT NUMERUS VALENS h - th.
    DECLARA profundum SICUT NUMERUS VALENS FV_COLOR(8, 35, 61).
    DECLARA vitrum SICUT NUMERUS VALENS FV_COLOR(14, 66, 111).
    DECLARA medium SICUT NUMERUS VALENS FV_COLOR(26, 93, 146).
    DECLARA aqua SICUT NUMERUS VALENS FV_COLOR(98, 215, 242).
    DECLARA lux SICUT NUMERUS VALENS FV_COLOR(234, 248, 255).
    DECLARA f SICUT NUMERUS VALENS FV_RECT(0, top, w, th, profundum).
    f = FV_RECT(0, top, w, 1, aqua).
    f = FV_RECT(6, top + 6, 104, th - 12, vitrum).
    f = FV_RECT(12, top + 11, 16, 16, medium).
    f = FV_RECT(15, top + 14, 10, 10, aqua).
    f = FV_TEXTUM(36, top + 16, "INITIUM", lux).
    SI status_programmata != 2 TUNC
        DECLARA cp SICUT NUMERUS VALENS vitrum.
        SI activum == 1 && status_programmata == 0 TUNC cp = medium. FIN-SI.
        f = FV_RECT(118, top + 6, 188, th - 12, cp).
        f = FV_TEXTUM(130, top + 16, "PROGRAMMATA", lux).
    FIN-SI.
    SI status_tabula != 2 TUNC
        DECLARA ct SICUT NUMERUS VALENS vitrum.
        SI activum == 2 && status_tabula == 0 TUNC ct = medium. FIN-SI.
        f = FV_RECT(312, top + 6, 138, th - 12, ct).
        f = FV_TEXTUM(324, top + 16, "TABULA", lux).
    FIN-SI.
    DECLARA tray SICUT NUMERUS VALENS w - 126.
    f = FV_RECT(tray, top + 6, 120, th - 12, vitrum).
    f = FV_RECT(tray + 8, top + 11, 16, 16, medium).
    f = FV_RECT(tray + 11, top + 14, 10, 10, aqua).
    f = FV_TEXTUM(tray + 32, top + 16, "SYLVIA", lux).
    REDDE 1.
FIN-FUNCTIO.'''
t = munus_muta(t, 'FV_TASKBAR', 'FV_CURSOR', taskbar)
VIS.write_text(t, encoding='utf-8')


# II. Gestor: eadem metrica ad hit-testing et clientem.
t = GEST.read_text(encoding='utf-8')
gi_taskbar = '''FUNCTIO GI_TASKBAR REDDENS NUMERUS.
    ACCIPIT s SICUT ORDO DE NUMERUS.
    ACCIPIT registrum SICUT NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    SI registrum==0 || x<118 TUNC REDDE 0. FIN-SI.
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
    SI my>=CONTENTUM(50333736)-taskbar_h TUNC REDDE GI_TASKBAR(s,registrum,mx). FIN-SI.
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


# III. Registrum fenestrarum: maximizationes et limites supra taskbar novam.
t = REG.read_text(encoding='utf-8')
substitutiones = {
    'CONTENTUM(n+16)=0. CONTENTUM(n+24)=0. CONTENTUM(n+32)=sw. CONTENTUM(n+40)=sh-28.':
        'CONTENTUM(n+16)=0. CONTENTUM(n+24)=0. CONTENTUM(n+32)=sw. CONTENTUM(n+40)=sh-FV_METRUM_TASKBAR().',
    'DECLARA sw SICUT NUMERUS VALENS CONTENTUM(50333728). DECLARA sh SICUT NUMERUS VALENS CONTENTUM(50333736)-28.':
        'DECLARA sw SICUT NUMERUS VALENS CONTENTUM(50333728). DECLARA sh SICUT NUMERUS VALENS CONTENTUM(50333736)-FV_METRUM_TASKBAR().',
}
for vetus, novum in substitutiones.items():
    if vetus not in t:
        raise SystemExit('registrum: metrum vetus non inventum')
    t = t.replace(vetus, novum)
REG.write_text(t, encoding='utf-8')


# IV. Systema I: clientis offset, taskbar dynamica et geometria initialis.
t = SYS.read_text(encoding='utf-8')
ii_fenestra = '''FUNCTIO II_FENESTRA REDDENS NUMERUS.
    ACCIPIT fenestrae SICUT NUMERUS.
    ACCIPIT clientes SICUT NUMERUS.
    ACCIPIT nodus SICUT NUMERUS.
    SI nodus==0 || CONTENTUM(nodus+48)!=0 TUNC REDDE 0. FIN-SI.
    DECLARA id SICUT NUMERUS VALENS CONTENTUM(nodus).
    DECLARA cliens SICUT NUMERUS VALENS CONTENTUM(nodus+8).
    DECLARA genus SICUT NUMERUS VALENS CH_GENUS(clientes,cliens).
    DECLARA superficies SICUT NUMERUS VALENS CH_SUPERFICIES(clientes,cliens).
    DECLARA x SICUT NUMERUS VALENS CONTENTUM(nodus+16). DECLARA y SICUT NUMERUS VALENS CONTENTUM(nodus+24).
    DECLARA w SICUT NUMERUS VALENS CONTENTUM(nodus+32). DECLARA h SICUT NUMERUS VALENS CONTENTUM(nodus+40).
    DECLARA activa SICUT NUMERUS VALENS 0.
    SI FI_FOCUS_ID(fenestrae)==id TUNC activa=1. FIN-SI.
    DECLARA f SICUT NUMERUS VALENS 0.
    SI genus==1 TUNC f=FV_FENESTRA(x,y,w,h,"PROGRAMMATA",activa). FIN-SI.
    SI genus==2 TUNC f=FV_FENESTRA(x,y,w,h,"TABULA",activa). FIN-SI.
    SI genus!=1 && genus!=2 TUNC f=FV_FENESTRA(x,y,w,h,"APPLICATIO",activa). FIN-SI.
    SI superficies!=0 TUNC
        DECLARA clientis_y SICUT NUMERUS VALENS FV_METRUM_CLIENTIS().
        DECLARA maxw SICUT NUMERUS VALENS w-20. DECLARA maxh SICUT NUMERUS VALENS h-clientis_y-22.
        SI maxw>0 && maxh>0 TUNC f=FS_BLIT(superficies,x+10,y+clientis_y,maxw,maxh). FIN-SI.
    FIN-SI.
    REDDE 1.
FIN-FUNCTIO.'''
t = munus_muta(t, 'II_FENESTRA', 'II_TASKBAR', ii_fenestra)

ii_taskbar = '''FUNCTIO II_TASKBAR REDDENS NUMERUS.
    ACCIPIT fenestrae SICUT NUMERUS.
    ACCIPIT clientes SICUT NUMERUS.
    DECLARA w SICUT NUMERUS VALENS CONTENTUM(50333728). DECLARA h SICUT NUMERUS VALENS CONTENTUM(50333736).
    DECLARA th SICUT NUMERUS VALENS FV_METRUM_TASKBAR().
    DECLARA top SICUT NUMERUS VALENS h-th.
    DECLARA profundum SICUT NUMERUS VALENS FV_COLOR(8,35,61).
    DECLARA vitrum SICUT NUMERUS VALENS FV_COLOR(14,66,111).
    DECLARA medium SICUT NUMERUS VALENS FV_COLOR(26,93,146).
    DECLARA aqua SICUT NUMERUS VALENS FV_COLOR(98,215,242).
    DECLARA lux SICUT NUMERUS VALENS FV_COLOR(234,248,255).
    DECLARA f SICUT NUMERUS VALENS FV_RECT(0,top,w,th,profundum).
    f=FV_RECT(0,top,w,1,aqua).
    f=FV_RECT(6,top+6,104,th-12,vitrum).
    f=FV_RECT(12,top+11,16,16,medium).
    f=FV_RECT(15,top+14,10,10,aqua).
    f=FV_TEXTUM(36,top+16,"INITIUM",lux).
    DECLARA tray SICUT NUMERUS VALENS w-126.
    f=FV_RECT(tray,top+6,120,th-12,vitrum).
    f=FV_RECT(tray+8,top+11,16,16,medium).
    f=FV_RECT(tray+11,top+14,10,10,aqua).
    f=FV_TEXTUM(tray+32,top+16,"SYLVIA",lux).
    DECLARA numerus SICUT NUMERUS VALENS FI_APERTA_NUM(fenestrae).
    SI numerus<=0 TUNC REDDE 1. FIN-SI.
    DECLARA basis SICUT NUMERUS VALENS 118.
    DECLARA spatium SICUT NUMERUS VALENS tray-basis-6.
    SI spatium<=0 TUNC REDDE 1. FIN-SI.
    DECLARA bw SICUT NUMERUS VALENS spatium/numerus.
    SI bw>196 TUNC bw=196. FIN-SI. SI bw<1 TUNC bw=1. FIN-SI.
    DECLARA i SICUT NUMERUS VALENS 0.
    DUM i<numerus PERFICE
        DECLARA bx SICUT NUMERUS VALENS basis+i*bw.
        SI bx>=tray-6 TUNC DESINE. FIN-SI.
        DECLARA id SICUT NUMERUS VALENS FI_APERTA_N(fenestrae,i).
        DECLARA n SICUT NUMERUS VALENS FI_QUAERE(fenestrae,id).
        SI n!=0 TUNC
            DECLARA color SICUT NUMERUS VALENS vitrum.
            SI FI_FOCUS_ID(fenestrae)==id && CONTENTUM(n+48)==0 TUNC color=medium. FIN-SI.
            DECLARA lat SICUT NUMERUS VALENS bw-8. SI lat<1 TUNC lat=1. FIN-SI.
            f=FV_RECT(bx,top+6,lat,th-12,color).
            DECLARA cliens SICUT NUMERUS VALENS CONTENTUM(n+8).
            DECLARA genus SICUT NUMERUS VALENS CH_GENUS(clientes,cliens).
            SI bw>=104 && genus==1 TUNC f=FV_TEXTUM(bx+10,top+16,"PROGRAMMATA",lux). FIN-SI.
            SI bw>=80 && genus==2 TUNC f=FV_TEXTUM(bx+10,top+16,"TABULA",lux). FIN-SI.
            SI bw<104 && bw>=28 && genus==1 TUNC f=FV_TEXTUM(bx+10,top+16,"P",lux). FIN-SI.
            SI bw<80 && bw>=28 && genus==2 TUNC f=FV_TEXTUM(bx+10,top+16,"T",lux). FIN-SI.
        FIN-SI.
        i=i+1.
    FIN-DUM.
    REDDE 1.
FIN-FUNCTIO.'''
t = munus_muta(t, 'II_TASKBAR', 'II_REDDE', ii_taskbar)

old = '''    DECLARA w SICUT NUMERUS VALENS CONTENTUM(50333728). DECLARA h SICUT NUMERUS VALENS CONTENTUM(50333736).
    s[11]=w/2. s[12]=h/2.'''
new = '''    DECLARA w SICUT NUMERUS VALENS CONTENTUM(50333728). DECLARA h SICUT NUMERUS VALENS CONTENTUM(50333736).
    DECLARA utilis_h SICUT NUMERUS VALENS h-FV_METRUM_TASKBAR().
    s[11]=w/2. s[12]=h/2.'''
if old not in t:
    raise SystemExit('systema: initium geometriae deest')
t = t.replace(old, new, 1)
t = t.replace('DECLARA pw SICUT NUMERUS VALENS w*58/100. DECLARA ph SICUT NUMERUS VALENS (h-28)*66/100.',
              'DECLARA pw SICUT NUMERUS VALENS w*58/100. DECLARA ph SICUT NUMERUS VALENS utilis_h*66/100.', 1)
t = t.replace('DECLARA tw SICUT NUMERUS VALENS w*42/100. DECLARA th SICUT NUMERUS VALENS (h-28)*52/100.',
              'DECLARA tw SICUT NUMERUS VALENS w*42/100. DECLARA th SICUT NUMERUS VALENS utilis_h*52/100.', 1)
t = t.replace('SI pw>w TUNC pw=w. FIN-SI. SI ph>h-28 TUNC ph=h-28. FIN-SI.',
              'SI pw>w TUNC pw=w. FIN-SI. SI ph>utilis_h TUNC ph=utilis_h. FIN-SI.', 1)
t = t.replace('SI tw>w TUNC tw=w. FIN-SI. SI th>h-28 TUNC th=h-28. FIN-SI.',
              'SI tw>w TUNC tw=w. FIN-SI. SI th>utilis_h TUNC th=utilis_h. FIN-SI.', 1)
t = t.replace('SI px+pw>w TUNC px=w-pw. FIN-SI. SI py+ph>h-28 TUNC py=h-28-ph. FIN-SI.',
              'SI px+pw>w TUNC px=w-pw. FIN-SI. SI py+ph>utilis_h TUNC py=utilis_h-ph. FIN-SI.', 1)
t = t.replace('SI tx<0 TUNC tx=0. FIN-SI. SI ty+th>h-28 TUNC ty=h-28-th. FIN-SI.',
              'SI tx<0 TUNC tx=0. FIN-SI. SI ty+th>utilis_h TUNC ty=utilis_h-th. FIN-SI.', 1)
SYS.write_text(t, encoding='utf-8')


# V. Harnais Fenestralis: probator substituibilis sine duplicatione QEMU.
t = HAR.read_text(encoding='utf-8')
old = 'MORA_INITII="${MORA_INITII:-28}"\n'
new = 'MORA_INITII="${MORA_INITII:-28}"\nPROBATOR_FENESTRALIS="${PROBATOR_FENESTRALIS:-$RADIX/instrumenta/proba_fenestrale_uefi_purum.py}"\n'
if 'PROBATOR_FENESTRALIS=' not in t:
    if old not in t:
        raise SystemExit('harnais: MORA_INITII deest')
    t = t.replace(old, new, 1)
old = 'if ! python3 "$RADIX/instrumenta/proba_fenestrale_uefi_purum.py" "$MONITOR" "$QMP" "$TEMPORARIUM" "$MORA_INITII"; then\n'
new = 'if ! python3 "$PROBATOR_FENESTRALIS" "$MONITOR" "$QMP" "$TEMPORARIUM" "$MORA_INITII"; then\n'
if old not in t and '$PROBATOR_FENESTRALIS' not in t:
    raise SystemExit('harnais: probator vetus deest')
t = t.replace(old, new, 1)
HAR.write_text(t, encoding='utf-8')

print('RECTE: P16-I metra visualia parata sunt.')
