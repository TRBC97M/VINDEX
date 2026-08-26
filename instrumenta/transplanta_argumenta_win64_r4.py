#!/usr/bin/env python3
"""R4: argc/argv Win64 historica selective in compilatorem canonicum transplantat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = VIA.read_text(encoding="utf-8")

if "FUNCTIO COMPONE_ARGUMENTA_PE REDDENS NUMERUS." in textus:
    print("RECTE: argumenta Win64 R4 iam adsunt.")
    raise SystemExit(0)


def muta_semel(vetus: str, novus: str, titulus: str) -> None:
    global textus
    n = textus.count(vetus)
    if n != 1:
        raise SystemExit(f"ERRATUM: ancora {titulus} inventa est {n} vicibus")
    textus = textus.replace(vetus, novus, 1)

muta_semel(
    "    DECLARA numerus_functionum_pe SICUT NUMERUS VALENS 7.",
    "    DECLARA numerus_functionum_pe SICUT NUMERUS VALENS 8.",
    "numerus-functionum-pe",
)
muta_semel(
    "    DECLARA off_hint_ch SICUT NUMERUS VALENS off_hint_rf + 12.\n    DECLARA off_nomen_dll SICUT NUMERUS VALENS off_hint_ch + 14.",
    "    DECLARA off_hint_ch SICUT NUMERUS VALENS off_hint_rf + 12.\n    DECLARA off_hint_gcl SICUT NUMERUS VALENS off_hint_ch + 14.\n    DECLARA off_nomen_dll SICUT NUMERUS VALENS off_hint_gcl + 18.",
    "offset-getcommandline",
)
muta_semel(
    "    DECLARA rva_hint_ch SICUT NUMERUS VALENS rva_idata + off_hint_ch.\n    DECLARA rva_nomen_dll SICUT NUMERUS VALENS rva_idata + off_nomen_dll.",
    "    DECLARA rva_hint_ch SICUT NUMERUS VALENS rva_idata + off_hint_ch.\n    DECLARA rva_hint_gcl SICUT NUMERUS VALENS rva_idata + off_hint_gcl.\n    DECLARA rva_nomen_dll SICUT NUMERUS VALENS rva_idata + off_nomen_dll.",
    "rva-getcommandline",
)
muta_semel(
    "    DECLARA igp_ch_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 48, rva_hint_ch).\n    DECLARA igp15 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 56, 0).",
    "    DECLARA igp_ch_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 48, rva_hint_ch).\n    DECLARA igp_gcl_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 56, rva_hint_gcl).\n    DECLARA igp15 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 64, 0).",
    "ilt-getcommandline",
)
muta_semel(
    "    DECLARA igp_ch_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 48, rva_hint_ch).\n    DECLARA igp20 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 56, 0).",
    "    DECLARA igp_ch_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 48, rva_hint_ch).\n    DECLARA igp_gcl_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 56, rva_hint_gcl).\n    DECLARA igp20 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 64, 0).",
    "iat-getcommandline",
)

nomen_gcl = '''    DECLARA igp_gcl SICUT NUMERUS VALENS SCRIBE_U16(codex, pos_idata + off_hint_gcl, 0).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 2, 71).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 3, 101).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 4, 116).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 5, 67).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 6, 111).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 7, 109).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 8, 109).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 9, 97).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 10, 110).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 11, 100).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 12, 76).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 13, 105).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 14, 110).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 15, 101).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 16, 65).
    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 17, 0).

'''
muta_semel(
    "    CODEX_SCRIBE(codex, pos_idata + off_nomen_dll, 107).",
    nomen_gcl + "    CODEX_SCRIBE(codex, pos_idata + off_nomen_dll, 107).",
    "nomen-getcommandline",
)

argumenta = '''// Lineam mandatorum Win64 in argc et argv sine bibliotheca C convertit.
FUNCTIO COMPONE_ARGUMENTA_PE REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.

    DECLARA p SICUT NUMERUS VALENS pos.
    p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 7).
    p = COMPONE_TRANSCRIBE(codex, p, 6, 0).

    p = COMPONE_ONERA(codex, p, 1, 0).
    p = COMPONE_ONERA(codex, p, 2, 262144).
    p = COMPONE_ONERA(codex, p, 8, 12288).
    p = COMPONE_ONERA(codex, p, 9, 4).
    p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 1).

    p = COMPONE_ONERA(codex, p, 3, 0).
    p = COMPONE_CMP(codex, p, 0, 3).
    DECLARA loci_memoria_parata SICUT NUMERUS VALENS 0.
    p = COMPONE_JNE_FUTURUM(codex, p, SEDES(loci_memoria_parata)).
    p = COMPONE_ONERA(codex, p, 1, 71).
    p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 0).
    p = COMPONE_HLT(codex, p).
    DECLARA ig_memoria_parata SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_memoria_parata, p).

    p = COMPONE_TRANSCRIBE(codex, p, 12, 0).
    p = COMPONE_TRANSCRIBE(codex, p, 8, 12).
    p = COMPONE_TRANSCRIBE(codex, p, 7, 12).
    p = COMPONE_ONERA(codex, p, 0, 32768).
    p = COMPONE_ADD(codex, p, 7, 0).
    p = COMPONE_ONERA(codex, p, 15, 0).
    p = COMPONE_ONERA(codex, p, 10, 0).
    p = COMPONE_ONERA(codex, p, 11, 0).

    DECLARA initium_ansae SICUT NUMERUS VALENS p.
    p = COMPONE_MOVZX(codex, p, 3, 6).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 3, 0).
    DECLARA loci_finis SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(loci_finis)).

    p = COMPONE_ONERA(codex, p, 0, 34).
    p = COMPONE_CMP(codex, p, 3, 0).
    DECLARA loci_signum_duplex SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(loci_signum_duplex)).

    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 10, 0).
    DECLARA loci_littera_ordinaria SICUT NUMERUS VALENS 0.
    p = COMPONE_JNE_FUTURUM(codex, p, SEDES(loci_littera_ordinaria)).
    p = COMPONE_ONERA(codex, p, 0, 32).
    p = COMPONE_CMP(codex, p, 3, 0).
    DECLARA loci_separator_spatium SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(loci_separator_spatium)).
    p = COMPONE_ONERA(codex, p, 0, 9).
    p = COMPONE_CMP(codex, p, 3, 0).
    DECLARA loci_separator_tabula SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(loci_separator_tabula)).

    DECLARA pos_litterae SICUT NUMERUS VALENS p.
    DECLARA ig_littera_ordinaria SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_littera_ordinaria, pos_litterae).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 11, 0).
    DECLARA loci_argumentum_inceptum SICUT NUMERUS VALENS 0.
    p = COMPONE_JNE_FUTURUM(codex, p, SEDES(loci_argumentum_inceptum)).
    p = COMPONE_SERVA_INDIRECTUM(codex, p, 8, 7).
    p = COMPONE_ONERA(codex, p, 0, 8).
    p = COMPONE_ADD(codex, p, 8, 0).
    p = COMPONE_ONERA(codex, p, 11, 1).
    DECLARA ig_argumentum_inceptum SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_argumentum_inceptum, p).
    p = COMPONE_SERVA_OCTETUM(codex, p, 7, 3).
    p = COMPONE_ONERA(codex, p, 0, 1).
    p = COMPONE_ADD(codex, p, 7, 0).
    p = COMPONE_ADD(codex, p, 6, 0).
    p = COMPONE_JMP_RETRO(codex, p, initium_ansae).

    DECLARA pos_signi_duplicis SICUT NUMERUS VALENS p.
    DECLARA ig_signum_duplex SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_signum_duplex, pos_signi_duplicis).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 11, 0).
    DECLARA loci_signum_argumenti_inceptum SICUT NUMERUS VALENS 0.
    p = COMPONE_JNE_FUTURUM(codex, p, SEDES(loci_signum_argumenti_inceptum)).
    p = COMPONE_SERVA_INDIRECTUM(codex, p, 8, 7).
    p = COMPONE_ONERA(codex, p, 0, 8).
    p = COMPONE_ADD(codex, p, 8, 0).
    p = COMPONE_ONERA(codex, p, 11, 1).
    DECLARA ig_signum_argumenti_inceptum SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_signum_argumenti_inceptum, p).

    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 10, 0).
    DECLARA loci_signum_clauditur SICUT NUMERUS VALENS 0.
    p = COMPONE_JNE_FUTURUM(codex, p, SEDES(loci_signum_clauditur)).
    p = COMPONE_ONERA(codex, p, 10, 1).
    DECLARA loci_post_signum SICUT NUMERUS VALENS 0.
    p = COMPONE_JMP_FUTURUM(codex, p, SEDES(loci_post_signum)).
    DECLARA pos_signi_clausi SICUT NUMERUS VALENS p.
    DECLARA ig_signum_clauditur SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_signum_clauditur, pos_signi_clausi).
    p = COMPONE_ONERA(codex, p, 10, 0).
    DECLARA ig_post_signum SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_post_signum, p).
    p = COMPONE_ONERA(codex, p, 0, 1).
    p = COMPONE_ADD(codex, p, 6, 0).
    p = COMPONE_JMP_RETRO(codex, p, initium_ansae).

    DECLARA pos_separatoris SICUT NUMERUS VALENS p.
    DECLARA ig_separator_spatium SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_separator_spatium, pos_separatoris).
    DECLARA ig_separator_tabula SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_separator_tabula, pos_separatoris).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 11, 0).
    DECLARA loci_separator_avanza SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(loci_separator_avanza)).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_SERVA_OCTETUM(codex, p, 7, 0).
    p = COMPONE_ONERA(codex, p, 0, 1).
    p = COMPONE_ADD(codex, p, 7, 0).
    p = COMPONE_ADD(codex, p, 15, 0).
    p = COMPONE_ONERA(codex, p, 11, 0).
    DECLARA ig_separator_avanza SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_separator_avanza, p).
    p = COMPONE_ONERA(codex, p, 0, 1).
    p = COMPONE_ADD(codex, p, 6, 0).
    p = COMPONE_JMP_RETRO(codex, p, initium_ansae).

    DECLARA pos_finis SICUT NUMERUS VALENS p.
    DECLARA ig_finis SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_finis, pos_finis).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_CMP(codex, p, 11, 0).
    DECLARA loci_argumenta_parata SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(loci_argumenta_parata)).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_SERVA_OCTETUM(codex, p, 7, 0).
    p = COMPONE_ONERA(codex, p, 0, 1).
    p = COMPONE_ADD(codex, p, 15, 0).
    DECLARA ig_argumenta_parata SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_argumenta_parata, p).

    p = COMPONE_TRANSCRIBE(codex, p, 7, 15).
    p = COMPONE_TRANSCRIBE(codex, p, 6, 12).
    REDDE p.
FIN-FUNCTIO.

'''
muta_semel(
    "FUNCTIO COMPONE_SCRIBE_STDOUT_DYNAMICA REDDENS NUMERUS.",
    argumenta + "FUNCTIO COMPONE_SCRIBE_STDOUT_DYNAMICA REDDENS NUMERUS.",
    "compone-argumenta-pe",
)

muta_semel(
    "                    pos = COMPONE_VOCA_IAT_DYNAMICA(codex, pos, contextus_parseris, 2).\n                    pos = COMPONE_ONERA(codex, pos, 2, 16777216).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0).",
    "                    pos = COMPONE_VOCA_IAT_DYNAMICA(codex, pos, contextus_parseris, 2).\n                    pos = COMPONE_ONERA(codex, pos, 2, 16777216).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0).\n                    pos = COMPONE_ARGUMENTA_PE(codex, pos, contextus_parseris).",
    "ingressus-argumenta-pe",
)

for fragmentum in (
    "numerus_functionum_pe SICUT NUMERUS VALENS 8",
    "GetCommandLineA" if False else "off_hint_gcl",
    "FUNCTIO COMPONE_ARGUMENTA_PE REDDENS NUMERUS.",
    "COMPONE_ARGUMENTA_PE(codex, pos, contextus_parseris)",
):
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: fragmentum R4 deest: {fragmentum}")

VIA.write_text(textus, encoding="utf-8")
print("RECTE: argumenta Win64 R4 transplantata sunt.")
