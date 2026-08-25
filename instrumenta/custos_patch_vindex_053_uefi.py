#!/usr/bin/env python3
"""Extensio minima VINDEX 0.53: vocatio indirecta UEFI Microsoft x64."""
from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
VIA = RADIX / "Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex"
textus = VIA.read_text(encoding="utf-8")

if "FUNCTIO COMPONE_VOCA_UEFI6" in textus:
    print("RECTE: UEFI_VOCA6 iam adest.")
    raise SystemExit(0)

ancora = '''FUNCTIO COMPONE_VOCA_NUCLEUM REDDENS NUMERUS.\n    ACCIPIT codex SICUT ACUS<NUMERUS>.\n    ACCIPIT indice SICUT NUMERUS.\n    CODEX_SCRIBE(codex, indice, 15).\n    CODEX_SCRIBE(codex, indice + 1, 5).\n    REDDE indice + 2.\nFIN-FUNCTIO.\n'''

adiunctum = ancora + '''\n// Vocatio firmware Microsoft x64: RAX functio; RCX,RDX,R8,R9 argumenta I-IV;\n// R10,R11 argumenta V-VI ante emissionem. Shadow space et alignmentum hic fiunt.\nFUNCTIO COMPONE_VOCA_UEFI6 REDDENS NUMERUS.\n    ACCIPIT codex SICUT ACUS<NUMERUS>.\n    ACCIPIT indice SICUT NUMERUS.\n    DECLARA p SICUT NUMERUS VALENS indice.\n    CODEX_SCRIBE(codex, p, 65). CODEX_SCRIBE(codex, p + 1, 84). p = p + 2.\n    CODEX_SCRIBE(codex, p, 73). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 228). p = p + 3.\n    CODEX_SCRIBE(codex, p, 72). CODEX_SCRIBE(codex, p + 1, 131). CODEX_SCRIBE(codex, p + 2, 228). CODEX_SCRIBE(codex, p + 3, 240). p = p + 4.\n    CODEX_SCRIBE(codex, p, 72). CODEX_SCRIBE(codex, p + 1, 131). CODEX_SCRIBE(codex, p + 2, 236). CODEX_SCRIBE(codex, p + 3, 48). p = p + 4.\n    CODEX_SCRIBE(codex, p, 76). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 84). CODEX_SCRIBE(codex, p + 3, 36). CODEX_SCRIBE(codex, p + 4, 32). p = p + 5.\n    CODEX_SCRIBE(codex, p, 76). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 92). CODEX_SCRIBE(codex, p + 3, 36). CODEX_SCRIBE(codex, p + 4, 40). p = p + 5.\n    CODEX_SCRIBE(codex, p, 255). CODEX_SCRIBE(codex, p + 1, 208). p = p + 2.\n    CODEX_SCRIBE(codex, p, 76). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 228). p = p + 3.\n    CODEX_SCRIBE(codex, p, 65). CODEX_SCRIBE(codex, p + 1, 92). p = p + 2.\n    REDDE p.\nFIN-FUNCTIO.\n'''

if textus.count(ancora) != 1:
    raise SystemExit("ERRATUM: ancora COMPONE_VOCA_NUCLEUM VINDEX 0.53 non unica est")
textus = textus.replace(ancora, adiunctum, 1)

vetus = '''    SI fons[CONTENTUM(pos_fontis)] == 80 && CONTENTUM(pos_fontis) + 4 < n && fons[CONTENTUM(pos_fontis)+1] == 79 && fons[CONTENTUM(pos_fontis)+2] == 76 && fons[CONTENTUM(pos_fontis)+3] == 76 && fons[CONTENTUM(pos_fontis)+4] == 69 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 5.\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 50333704).\n        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 0).\n        CODEX_SCRIBE(codex, CONTENTUM(pos_codicis), 255).\n        CODEX_SCRIBE(codex, CONTENTUM(pos_codicis) + 1, 208).\n        CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 2.\n        REDDE 0.\n    FIN-SI.\n'''

novus = '''    SI fons[CONTENTUM(pos_fontis)] == 85 && CONTENTUM(pos_fontis) + 10 < n && fons[CONTENTUM(pos_fontis)+1] == 69 && fons[CONTENTUM(pos_fontis)+2] == 70 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 95 && fons[CONTENTUM(pos_fontis)+5] == 86 && fons[CONTENTUM(pos_fontis)+6] == 79 && fons[CONTENTUM(pos_fontis)+7] == 67 && fons[CONTENTUM(pos_fontis)+8] == 65 && fons[CONTENTUM(pos_fontis)+9] == 54 && fons[CONTENTUM(pos_fontis)+10] == 40 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 11.\n        DECLARA ig_uefi SICUT NUMERUS VALENS 0.\n        ig_uefi = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).\n        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).\n        DECLARA arg_uefi SICUT NUMERUS VALENS 0.\n        DUM arg_uefi < 6 PERFICE\n            ig_uefi = IGNORA_SPATIA(fons, pos_fontis, n).\n            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n            ig_uefi = IGNORA_SPATIA(fons, pos_fontis, n).\n            ig_uefi = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).\n            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).\n            arg_uefi = arg_uefi + 1.\n        FIN-DUM.\n        ig_uefi = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 11).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 9).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 8).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 0).\n        CONTENTUM(pos_codicis) = COMPONE_VOCA_UEFI6(codex, CONTENTUM(pos_codicis)).\n        REDDE 0.\n    FIN-SI.\n'''

if textus.count(vetus) != 1:
    raise SystemExit("ERRATUM: intrinsecum POLLE VINDEX 0.53 non unicum est")
textus = textus.replace(vetus, novus, 1)

if "50333704" in textus:
    raise SystemExit("ERRATUM: callback POLLE historicus adhuc in compilatore est")
VIA.write_text(textus, encoding="utf-8")
print("RECTE: VINDEX 0.53 UEFI_VOCA6 directe sustinet; POLLE remotum est.")
