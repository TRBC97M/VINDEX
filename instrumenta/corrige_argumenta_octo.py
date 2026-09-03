from pathlib import Path

P = Path('Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex')
s = P.read_text(encoding='utf-8')

old_caller = '''        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
        SI numerus_argumentorum >= 6 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 9).
        FIN-SI.
        SI numerus_argumentorum >= 5 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 8).
        FIN-SI.
        SI numerus_argumentorum >= 4 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
        FIN-SI.
        SI numerus_argumentorum >= 3 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).
        FIN-SI.
        SI numerus_argumentorum >= 2 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).
        FIN-SI.
        SI numerus_argumentorum >= 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
        FIN-SI.
        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 11, 0).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 11).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
'''

new_caller = '''        // P11-E — ABI ordinaria: sex argumenta prima in registris SysV,
        // VII et VIII in pila. Casus VIII retinet ordinem ut [rbp+16]=VII,
        // [rbp+24]=VIII apud callee; casus VII addit verbum alignmenti.
        SI numerus_argumentorum == 8 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 11).
        FIN-SI.
        SI numerus_argumentorum >= 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
        SI numerus_argumentorum >= 6 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 9).
        FIN-SI.
        SI numerus_argumentorum >= 5 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 8).
        FIN-SI.
        SI numerus_argumentorum >= 4 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
        FIN-SI.
        SI numerus_argumentorum >= 3 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).
        FIN-SI.
        SI numerus_argumentorum >= 2 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).
        FIN-SI.
        SI numerus_argumentorum >= 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
        FIN-SI.
        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 11, 0).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 11).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
        SI numerus_argumentorum == 8 TUNC
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 11).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
'''

old_cleanup = '''        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 11).
        FIN-SI.
'''
new_cleanup = '''        SI numerus_argumentorum == 7 || numerus_argumentorum == 8 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 11).
        FIN-SI.
'''

old_callee = '''                        SI numerus_parametrorum == 6 TUNC
                            pos = COMPONE_SUME_PILA(codex, pos, 10, 16).
                            pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, 10).
                        ALITER
                            pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, registrum_param).
                        FIN-SI.
'''
new_callee = '''                        SI numerus_parametrorum == 6 TUNC
                            pos = COMPONE_SUME_PILA(codex, pos, 10, 16).
                            pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, 10).
                        ALITER
                            SI numerus_parametrorum == 7 TUNC
                                pos = COMPONE_SUME_PILA(codex, pos, 10, 24).
                                pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, 10).
                            ALITER
                                pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, registrum_param).
                            FIN-SI.
                        FIN-SI.
'''

for label, old, new in [
    ('caller', old_caller, new_caller),
    ('cleanup', old_cleanup, new_cleanup),
    ('callee', old_callee, new_callee),
]:
    count = s.count(old)
    if count == 1:
        s = s.replace(old, new)
    elif new in s:
        print(f'RECTE: {label} iam correctus est.')
    else:
        raise SystemExit(f'ERRATUM: locus {label} singularis non inventus est (count={count})')

P.write_text(s, encoding='utf-8')
print('RECTE: contractus VIII argumentorum in fonte compilatoris applicatus est.')
