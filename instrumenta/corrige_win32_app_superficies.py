from pathlib import Path

LIB = Path('Vindex Chat-GPT/vindex_final_v51/bibliotheca/win32_app.vindex')
TEST = Path('Vindex Chat-GPT/vindex_final_v51/tests/casus/win32_app.vindex')

s = LIB.read_text(encoding='utf-8')
old = '''FUNCTIO WINAPP_PRAESENTA REDDENS NUMERUS.\n    ACCIPIT ctx SICUT NUMERUS.\n    ACCIPIT hdc SICUT NUMERUS.\n    ACCIPIT dw SICUT NUMERUS.\n    ACCIPIT dh SICUT NUMERUS.\n    ACCIPIT sw SICUT NUMERUS.\n    ACCIPIT sh SICUT NUMERUS.\n    ACCIPIT pixels SICUT NUMERUS.\n    ACCIPIT bmi SICUT NUMERUS.\n    DECLARA args SICUT NUMERUS VALENS WINAPP_ARG_CREA().\n    SI args == 0 TUNC REDDE 0. FIN-SI.\n    CONTENTUM(args + 0) = hdc.\n    CONTENTUM(args + 8) = 0.\n    CONTENTUM(args + 16) = 0.\n    CONTENTUM(args + 24) = dw.\n    CONTENTUM(args + 32) = dh.\n    CONTENTUM(args + 40) = 0.\n    CONTENTUM(args + 48) = 0.\n    CONTENTUM(args + 56) = sw.\n    CONTENTUM(args + 64) = sh.\n    CONTENTUM(args + 72) = pixels.\n    CONTENTUM(args + 80) = bmi.\n    CONTENTUM(args + 88) = 0.\n    CONTENTUM(args + 96) = 13369376.\n    DECLARA fn SICUT NUMERUS VALENS CONTENTUM(ctx + 136).\n    REDDE MSX64_VOCA(fn, args).\nFIN-FUNCTIO.\n'''
new = '''// Superficies BGRA applicationis. Descriptor LVI octeta:\n// +0 pixels, +8 BITMAPINFO, +16/+24 source w/h,\n// +32 HDC, +40/+48 destination w/h.\nFUNCTIO WINAPP_SUPERFICIES_CREA REDDENS NUMERUS.\n    ACCIPIT pixels SICUT NUMERUS.\n    ACCIPIT bmi SICUT NUMERUS.\n    ACCIPIT sw SICUT NUMERUS.\n    ACCIPIT sh SICUT NUMERUS.\n    SI pixels <= 0 || bmi <= 0 || sw <= 0 || sh <= 0 TUNC REDDE 0. FIN-SI.\n    DECLARA superficies SICUT NUMERUS VALENS RESERVA_OCTETA(56).\n    SI superficies <= 0 TUNC REDDE 0. FIN-SI.\n    CONTENTUM(superficies + 0) = pixels.\n    CONTENTUM(superficies + 8) = bmi.\n    CONTENTUM(superficies + 16) = sw.\n    CONTENTUM(superficies + 24) = sh.\n    CONTENTUM(superficies + 32) = 0.\n    CONTENTUM(superficies + 40) = sw.\n    CONTENTUM(superficies + 48) = sh.\n    REDDE superficies.\nFIN-FUNCTIO.\n\nFUNCTIO WINAPP_SUPERFICIES_DESTINATIO REDDENS NUMERUS.\n    ACCIPIT superficies SICUT NUMERUS.\n    ACCIPIT hdc SICUT NUMERUS.\n    ACCIPIT dw SICUT NUMERUS.\n    ACCIPIT dh SICUT NUMERUS.\n    SI superficies <= 0 || hdc <= 0 || dw <= 0 || dh <= 0 TUNC REDDE 0. FIN-SI.\n    CONTENTUM(superficies + 32) = hdc.\n    CONTENTUM(superficies + 40) = dw.\n    CONTENTUM(superficies + 48) = dh.\n    REDDE 1.\nFIN-FUNCTIO.\n\nFUNCTIO WINAPP_PRAESENTA REDDENS NUMERUS.\n    ACCIPIT ctx SICUT NUMERUS.\n    ACCIPIT superficies SICUT NUMERUS.\n    SI ctx <= 0 || superficies <= 0 TUNC REDDE 0. FIN-SI.\n    DECLARA args SICUT NUMERUS VALENS WINAPP_ARG_CREA().\n    SI args == 0 TUNC REDDE 0. FIN-SI.\n    CONTENTUM(args + 0) = CONTENTUM(superficies + 32).\n    CONTENTUM(args + 8) = 0.\n    CONTENTUM(args + 16) = 0.\n    CONTENTUM(args + 24) = CONTENTUM(superficies + 40).\n    CONTENTUM(args + 32) = CONTENTUM(superficies + 48).\n    CONTENTUM(args + 40) = 0.\n    CONTENTUM(args + 48) = 0.\n    CONTENTUM(args + 56) = CONTENTUM(superficies + 16).\n    CONTENTUM(args + 64) = CONTENTUM(superficies + 24).\n    CONTENTUM(args + 72) = CONTENTUM(superficies + 0).\n    CONTENTUM(args + 80) = CONTENTUM(superficies + 8).\n    CONTENTUM(args + 88) = 0.\n    CONTENTUM(args + 96) = 13369376.\n    DECLARA fn SICUT NUMERUS VALENS CONTENTUM(ctx + 136).\n    REDDE MSX64_VOCA(fn, args).\nFIN-FUNCTIO.\n'''
if old in s:
    s = s.replace(old, new)
elif 'FUNCTIO WINAPP_SUPERFICIES_CREA' not in s:
    raise SystemExit('ERRATUM: WINAPP_PRAESENTA vetus non inventa est')
LIB.write_text(s, encoding='utf-8')

t = TEST.read_text(encoding='utf-8')
old_call = '''    PROCLAMA "WINAPP GRADUS 5 BUFFER".\n    DECLARA lineae SICUT NUMERUS VALENS WINAPP_PRAESENTA(ctx, hdc, dw, dh, 8, 8, pixels, bmi).\n    SI lineae != 8 TUNC REDDE 17. FIN-SI.\n    PROCLAMA "WINAPP GRADUS 6 PRAESENTA".\n'''
new_call = '''    PROCLAMA "WINAPP GRADUS 5 BUFFER".\n    DECLARA superficies SICUT NUMERUS VALENS WINAPP_SUPERFICIES_CREA(pixels, bmi, 8, 8).\n    SI superficies == 0 TUNC REDDE 17. FIN-SI.\n    SI WINAPP_SUPERFICIES_DESTINATIO(superficies, hdc, dw, dh) == 0 TUNC REDDE 18. FIN-SI.\n    DECLARA lineae SICUT NUMERUS VALENS WINAPP_PRAESENTA(ctx, superficies).\n    SI lineae != 8 TUNC REDDE 19. FIN-SI.\n    PROCLAMA "WINAPP GRADUS 6 PRAESENTA".\n'''
if old_call in t:
    t = t.replace(old_call, new_call)
elif 'WINAPP_SUPERFICIES_CREA' not in t:
    raise SystemExit('ERRATUM: vocatio WINAPP_PRAESENTA vetus non inventa est')
TEST.write_text(t, encoding='utf-8')
print('RECTE: superficies Win32 App applicata est.')
