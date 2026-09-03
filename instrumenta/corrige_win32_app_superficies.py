from pathlib import Path
import re

LIB = Path('Vindex Chat-GPT/vindex_final_v51/bibliotheca/win32_app.vindex')
TEST = Path('Vindex Chat-GPT/vindex_final_v51/tests/casus/win32_app.vindex')

s = LIB.read_text(encoding='utf-8')
new = '''// Superficies BGRA applicationis. Descriptor LVI octeta:
// +0 pixels, +8 BITMAPINFO, +16/+24 source w/h,
// +32 HDC, +40/+48 destination w/h.
FUNCTIO WINAPP_SUPERFICIES_CREA REDDENS NUMERUS.
    ACCIPIT pixels SICUT NUMERUS.
    ACCIPIT bmi SICUT NUMERUS.
    ACCIPIT sw SICUT NUMERUS.
    ACCIPIT sh SICUT NUMERUS.
    SI pixels <= 0 || bmi <= 0 || sw <= 0 || sh <= 0 TUNC REDDE 0. FIN-SI.
    DECLARA superficies SICUT NUMERUS VALENS RESERVA_OCTETA(56).
    SI superficies <= 0 TUNC REDDE 0. FIN-SI.
    CONTENTUM(superficies + 0) = pixels.
    CONTENTUM(superficies + 8) = bmi.
    CONTENTUM(superficies + 16) = sw.
    CONTENTUM(superficies + 24) = sh.
    CONTENTUM(superficies + 32) = 0.
    CONTENTUM(superficies + 40) = sw.
    CONTENTUM(superficies + 48) = sh.
    REDDE superficies.
FIN-FUNCTIO.

FUNCTIO WINAPP_SUPERFICIES_DESTINATIO REDDENS NUMERUS.
    ACCIPIT superficies SICUT NUMERUS.
    ACCIPIT hdc SICUT NUMERUS.
    ACCIPIT dw SICUT NUMERUS.
    ACCIPIT dh SICUT NUMERUS.
    SI superficies <= 0 || hdc <= 0 || dw <= 0 || dh <= 0 TUNC REDDE 0. FIN-SI.
    CONTENTUM(superficies + 32) = hdc.
    CONTENTUM(superficies + 40) = dw.
    CONTENTUM(superficies + 48) = dh.
    REDDE 1.
FIN-FUNCTIO.

// Praesentat BGRA top-down. Reddit numerum scanlinearum a StretchDIBits.
FUNCTIO WINAPP_PRAESENTA REDDENS NUMERUS.
    ACCIPIT ctx SICUT NUMERUS.
    ACCIPIT superficies SICUT NUMERUS.
    SI ctx <= 0 || superficies <= 0 TUNC REDDE 0. FIN-SI.
    DECLARA a SICUT ORDO DE NUMERUS CAPACITAS 16.
    DECLARA p SICUT NUMERUS VALENS SEDES(a).
    DECLARA ig SICUT NUMERUS VALENS MSX64_ARGUMENTA_VACUA(p).
    CONTENTUM(p + 0) = CONTENTUM(superficies + 32).
    CONTENTUM(p + 8) = 0. CONTENTUM(p + 16) = 0.
    CONTENTUM(p + 24) = CONTENTUM(superficies + 40).
    CONTENTUM(p + 32) = CONTENTUM(superficies + 48).
    CONTENTUM(p + 40) = 0. CONTENTUM(p + 48) = 0.
    CONTENTUM(p + 56) = CONTENTUM(superficies + 16).
    CONTENTUM(p + 64) = CONTENTUM(superficies + 24).
    CONTENTUM(p + 72) = CONTENTUM(superficies + 0).
    CONTENTUM(p + 80) = CONTENTUM(superficies + 8).
    CONTENTUM(p + 88) = 0. CONTENTUM(p + 96) = 13369376.
    REDDE MSX64_VOCA(CONTENTUM(ctx + 136), p).
FIN-FUNCTIO.'''

if 'FUNCTIO WINAPP_SUPERFICIES_CREA' not in s:
    pattern = r'// Praesentat BGRA top-down\. Reddit numerum scanlinearum a StretchDIBits\.\nFUNCTIO WINAPP_PRAESENTA REDDENS NUMERUS\..*?FIN-FUNCTIO\.'
    s2, n = re.subn(pattern, new, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'ERRATUM: WINAPP_PRAESENTA vetus non inventa est (n={n})')
    s = s2
LIB.write_text(s, encoding='utf-8')

t = TEST.read_text(encoding='utf-8')
old_call = '''    PROCLAMA "WINAPP GRADUS 5 BUFFER".
    DECLARA lineae SICUT NUMERUS VALENS WINAPP_PRAESENTA(ctx, hdc, dw, dh, 8, 8, pixels, bmi).
    SI lineae != 8 TUNC REDDE 17. FIN-SI.
    PROCLAMA "WINAPP GRADUS 6 PRAESENTA".
'''
new_call = '''    PROCLAMA "WINAPP GRADUS 5 BUFFER".
    DECLARA superficies SICUT NUMERUS VALENS WINAPP_SUPERFICIES_CREA(pixels, bmi, 8, 8).
    SI superficies == 0 TUNC REDDE 17. FIN-SI.
    SI WINAPP_SUPERFICIES_DESTINATIO(superficies, hdc, dw, dh) == 0 TUNC REDDE 18. FIN-SI.
    DECLARA lineae SICUT NUMERUS VALENS WINAPP_PRAESENTA(ctx, superficies).
    SI lineae != 8 TUNC REDDE 19. FIN-SI.
    PROCLAMA "WINAPP GRADUS 6 PRAESENTA".
'''
if 'WINAPP_SUPERFICIES_CREA' not in t:
    if old_call not in t:
        raise SystemExit('ERRATUM: vocatio WINAPP_PRAESENTA vetus non inventa est')
    t = t.replace(old_call, new_call)
TEST.write_text(t, encoding='utf-8')
print('RECTE: superficies Win32 App applicata est.')
