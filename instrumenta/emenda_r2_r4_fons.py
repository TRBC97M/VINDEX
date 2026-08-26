from pathlib import Path

via = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = via.read_text(encoding="utf-8")

vetus = """    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 1, 7).\n    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 2, 13).\n"""
novus = """    SI id_api == 3 TUNC\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 1).\n        p_tr = COMPONE_CMP(codex, p_tr, 7, 0).\n        DECLARA loci_descriptor_stdout SICUT NUMERUS VALENS 0.\n        p_tr = COMPONE_JNE_FUTURUM(codex, p_tr, SEDES(loci_descriptor_stdout)).\n        p_tr = COMPONE_ONERA(codex, p_tr, 0, 16777216).\n        p_tr = COMPONE_SUME_INDIRECTUM(codex, p_tr, 7, 0).\n        DECLARA pos_descriptor_stdout SICUT NUMERUS VALENS p_tr.\n        DECLARA ign_descriptor_stdout SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_descriptor_stdout, pos_descriptor_stdout).\n    FIN-SI.\n\n    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 1, 7).\n    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 2, 13).\n"""

si_iam = "DECLARA loci_descriptor_stdout SICUT NUMERUS VALENS 0."
if si_iam in textus:
    raise SystemExit(0)

quantitas = textus.count(vetus)
if quantitas != 1:
    raise SystemExit(f"ERRATUM: locus unicus exspectatus est, inventi sunt {quantitas}.")

via.write_text(textus.replace(vetus, novus, 1), encoding="utf-8")
