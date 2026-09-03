#!/usr/bin/env python3
"""P11-C: TEXTUS VINDEX ad LPCSTR Win32 convertit in intrinsecis FFI.

TEXTUS ABI: [longitudo:u64][capacitas:u64][octeta UTF-8...][NUL].
Ergo API Win32 quae LPCSTR exspectant accipiunt descriptor + 16.
Instrumentum temporarium est et ante fusionem removendum.
"""
from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
VIA = RADIX / "Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex"
textus = VIA.read_text(encoding="utf-8")

marca = "// P11-C — TEXTUS descriptor ad LPCSTR: basis octetorum est + XVI."
if marca in textus:
    print("RECTE: pontis TEXTUS/Win32 iam adest.")
    raise SystemExit(0)

vetus_dll = '''        DECLARA ig_dll SICUT NUMERUS VALENS ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        ig_dll = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 1, 0).
'''
novus_dll = '''        DECLARA ig_dll SICUT NUMERUS VALENS ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        // P11-C — TEXTUS descriptor ad LPCSTR: basis octetorum est + XVI.
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 16).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 0, 1).
        ig_dll = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 1, 0).
'''

vetus_sym = '''        ig_sym = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
'''
novus_sym = '''        ig_sym = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 16).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 0, 2).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
'''

for vetus, novus, nomen in (
    (vetus_dll, novus_dll, "WIN_DLL_APERI"),
    (vetus_sym, novus_sym, "WIN_DLL_SYMBOLUM"),
):
    n = textus.count(vetus)
    if n != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} non unica est ({n})")
    textus = textus.replace(vetus, novus, 1)

VIA.write_text(textus, encoding="utf-8")
print("RECTE: TEXTUS VINDEX ad LPCSTR Win32 convertitur.")
