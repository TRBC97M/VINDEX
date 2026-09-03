#!/usr/bin/env python3
"""P11-B: canonize abstract descriptor 0 as Win64 STD_INPUT_HANDLE.

This helper is intentionally narrow and self-checking. It exists so the large
self-hosted VINDEX compiler can be modified reproducibly inside CI without
copying or hand-editing the whole source file through a remote API.
"""

from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "Vindex Chat-GPT" / "vindex_final_v51" / "src" / "compilator_vindex.vindex"

text = FONS.read_text(encoding="utf-8")

marker = "valor_neg_std_input_prologus"
if marker in text:
    print("RECTE: patch stdin Win64 iam adest.")
    raise SystemExit(0)

old_prologue = """                    DECLARA valor_neg_std_output_prologus SICUT NUMERUS VALENS 0 - 11.\n                    pos = COMPONE_ONERA(codex, pos, 1, valor_neg_std_output_prologus).\n                    pos = COMPONE_VOCA_IAT_DYNAMICA(codex, pos, contextus_parseris, 2).\n                    pos = COMPONE_ONERA(codex, pos, 2, 16777216).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0)."""

new_prologue = """                    // Descriptor abstractus 1 = stdout; handle Win32 ad +0 servatur.\n                    DECLARA valor_neg_std_output_prologus SICUT NUMERUS VALENS 0 - 11.\n                    pos = COMPONE_ONERA(codex, pos, 1, valor_neg_std_output_prologus).\n                    pos = COMPONE_VOCA_IAT_DYNAMICA(codex, pos, contextus_parseris, 2).\n                    pos = COMPONE_ONERA(codex, pos, 2, 16777216).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0).\n                    // Descriptor abstractus 0 = stdin; handle Win32 ad +8 servatur.\n                    DECLARA valor_neg_std_input_prologus SICUT NUMERUS VALENS 0 - 10.\n                    pos = COMPONE_ONERA(codex, pos, 1, valor_neg_std_input_prologus).\n                    pos = COMPONE_VOCA_IAT_DYNAMICA(codex, pos, contextus_parseris, 2).\n                    pos = COMPONE_ONERA(codex, pos, 2, 16777224).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0)."""

old_transfer = """    SI id_api == 3 TUNC\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 1).\n        p_tr = COMPONE_CMP(codex, p_tr, 7, 0).\n        DECLARA loci_descriptor_stdout SICUT NUMERUS VALENS 0.\n        p_tr = COMPONE_JNE_FUTURUM(codex, p_tr, SEDES(loci_descriptor_stdout)).\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 16777216).\n        p_tr = COMPONE_SUME_INDIRECTUM(codex, p_tr, 7, 0).\n        DECLARA pos_descriptor_stdout SICUT NUMERUS VALENS p_tr.\n        DECLARA ign_descriptor_stdout SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_descriptor_stdout, pos_descriptor_stdout).\n    FIN-SI.\n\n    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 1, 7)."""

new_transfer = """    SI id_api == 3 TUNC\n        // MITTE(1, ...) -> verum STD_OUTPUT_HANDLE Win32.\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 1).\n        p_tr = COMPONE_CMP(codex, p_tr, 7, 0).\n        DECLARA loci_descriptor_stdout SICUT NUMERUS VALENS 0.\n        p_tr = COMPONE_JNE_FUTURUM(codex, p_tr, SEDES(loci_descriptor_stdout)).\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 16777216).\n        p_tr = COMPONE_SUME_INDIRECTUM(codex, p_tr, 7, 0).\n        DECLARA pos_descriptor_stdout SICUT NUMERUS VALENS p_tr.\n        DECLARA ign_descriptor_stdout SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_descriptor_stdout, pos_descriptor_stdout).\n    FIN-SI.\n\n    SI id_api == 5 TUNC\n        // LEGE(0, ...) -> verum STD_INPUT_HANDLE Win32.\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 0).\n        p_tr = COMPONE_CMP(codex, p_tr, 7, 0).\n        DECLARA loci_descriptor_stdin SICUT NUMERUS VALENS 0.\n        p_tr = COMPONE_JNE_FUTURUM(codex, p_tr, SEDES(loci_descriptor_stdin)).\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 16777224).\n        p_tr = COMPONE_SUME_INDIRECTUM(codex, p_tr, 7, 0).\n        DECLARA pos_descriptor_stdin SICUT NUMERUS VALENS p_tr.\n        DECLARA ign_descriptor_stdin SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_descriptor_stdin, pos_descriptor_stdin).\n    FIN-SI.\n\n    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 1, 7)."""

if text.count(old_prologue) != 1:
    raise SystemExit(f"ERRATUM: prologus exspectatus {text.count(old_prologue)} vice inventus est")
if text.count(old_transfer) != 1:
    raise SystemExit(f"ERRATUM: translatio descriptoris {text.count(old_transfer)} vice inventa est")

text = text.replace(old_prologue, new_prologue, 1)
text = text.replace(old_transfer, new_transfer, 1)
FONS.write_text(text, encoding="utf-8")
print("RECTE: descriptor 0 stdin Win64 in compilatore canonico additus est.")
