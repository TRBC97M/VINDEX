from pathlib import Path

P = Path('Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex')
s = P.read_text(encoding='utf-8')
old = '''FUNCTIO EXTRAHE_ET_SIGNA REDDENS NUMERUS.\n    ACCIPIT fons SICUT ACUS<LITTERA>.\n    ACCIPIT pos SICUT ACUS<NUMERUS>.\n    ACCIPIT n SICUT NUMERUS.\n    DECLARA verbum SICUT ORDO DE LITTERA CAPACITAS 32.\n    DECLARA mensura SICUT NUMERUS VALENS 0.\n    DUM CONTENTUM(pos) < n && ((fons[CONTENTUM(pos)] >= 65 && fons[CONTENTUM(pos)] <= 90) || (fons[CONTENTUM(pos)] >= 97 && fons[CONTENTUM(pos)] <= 122) || fons[CONTENTUM(pos)] == 95 || (fons[CONTENTUM(pos)] >= 48 && fons[CONTENTUM(pos)] <= 57)) PERFICE\n        SCRIBE_OCTETUM_AB(verbum + mensura, fons[CONTENTUM(pos)]).\n        mensura = mensura + 1.\n        CONTENTUM(pos) = CONTENTUM(pos) + 1.\n    FIN-DUM.\n    REDDE SIGNUM_VERBI(verbum, mensura).\nFIN-FUNCTIO.\n'''
new = '''// Signum identificatoris sine tampone computatur, littera post litteram.\n// Correctio ex opere Claude #168 adoptata: tampon historicus XXXII octetorum\n// memoriam corrumpere poterat et nomina longa male resolvebat.\nFUNCTIO EXTRAHE_ET_SIGNA REDDENS NUMERUS.\n    ACCIPIT fons SICUT ACUS<LITTERA>.\n    ACCIPIT pos SICUT ACUS<NUMERUS>.\n    ACCIPIT n SICUT NUMERUS.\n    DECLARA signum SICUT NUMERUS VALENS 0.\n    DUM CONTENTUM(pos) < n && ((fons[CONTENTUM(pos)] >= 65 && fons[CONTENTUM(pos)] <= 90) || (fons[CONTENTUM(pos)] >= 97 && fons[CONTENTUM(pos)] <= 122) || fons[CONTENTUM(pos)] == 95 || (fons[CONTENTUM(pos)] >= 48 && fons[CONTENTUM(pos)] <= 57)) PERFICE\n        signum = signum * 31 + fons[CONTENTUM(pos)].\n        CONTENTUM(pos) = CONTENTUM(pos) + 1.\n    FIN-DUM.\n    REDDE signum.\nFIN-FUNCTIO.\n'''
if old in s:
    s = s.replace(old, new, 1)
elif 'Correctio ex opere Claude #168 adoptata' not in s:
    raise SystemExit('ERRATUM: EXTRAHE_ET_SIGNA historicus non inventus est')
P.write_text(s, encoding='utf-8')
print('RECTE: identificatores longi sine tampone corriguntur.')
