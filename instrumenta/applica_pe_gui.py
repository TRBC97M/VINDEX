from pathlib import Path

p = Path('Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex')
s = p.read_text(encoding='utf-8')
orig = s

s = s.replace('USUS: compilator_vindex <fons.vindex> <exsecutabile> [pe|uefi]',
              'USUS: compilator_vindex <fons.vindex> <exsecutabile> [pe|gui|uefi]')

old_sub = '''    DECLARA subsystema_pe SICUT NUMERUS VALENS 3.\n    SI MODUS_PE_LEGE(contextus_parseris) == 2 TUNC\n        subsystema_pe = 10.\n    FIN-SI.\n'''
new_sub = '''    DECLARA subsystema_pe SICUT NUMERUS VALENS 3.\n    SI MODUS_PE_LEGE(contextus_parseris) == 3 TUNC\n        subsystema_pe = 2.\n    FIN-SI.\n    SI MODUS_PE_LEGE(contextus_parseris) == 2 TUNC\n        subsystema_pe = 10.\n    FIN-SI.\n'''
if old_sub in s:
    s = s.replace(old_sub, new_sub, 1)
elif new_sub not in s:
    raise SystemExit('ancora subsystematis PE non inventa est')

old_cli = '''        SI argc >= 4 TUNC\n            DECLARA arg3_uefi SICUT ACUS<LITTERA> VALENS argv[3].\n            SI arg3_uefi[0] == 117 && arg3_uefi[1] == 101 && arg3_uefi[2] == 102 && arg3_uefi[3] == 105 && arg3_uefi[4] == 0 TUNC\n                modus_pe = 2.\n            FIN-SI.\n        FIN-SI.\n'''
new_cli = '''        SI argc >= 4 TUNC\n            DECLARA arg3_gui SICUT ACUS<LITTERA> VALENS argv[3].\n            SI arg3_gui[0] == 103 && arg3_gui[1] == 117 && arg3_gui[2] == 105 && arg3_gui[3] == 0 TUNC\n                modus_pe = 3.\n            FIN-SI.\n        FIN-SI.\n        SI argc >= 4 TUNC\n            DECLARA arg3_uefi SICUT ACUS<LITTERA> VALENS argv[3].\n            SI arg3_uefi[0] == 117 && arg3_uefi[1] == 101 && arg3_uefi[2] == 102 && arg3_uefi[3] == 105 && arg3_uefi[4] == 0 TUNC\n                modus_pe = 2.\n            FIN-SI.\n        FIN-SI.\n'''
if old_cli in s:
    s = s.replace(old_cli, new_cli, 1)
elif new_cli not in s:
    raise SystemExit('ancora targeti GUI non inventa est')

if s != orig:
    p.write_text(s, encoding='utf-8')
    print('RECTE: target GUI PE applicatus est')
else:
    print('RECTE: target GUI PE iam adest')
