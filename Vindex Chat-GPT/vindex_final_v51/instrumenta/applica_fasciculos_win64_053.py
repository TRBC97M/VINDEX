#!/usr/bin/env python3
"""VINDEX 0.53: stratum fasciculorum Win64 in compilatorem applicat."""

from __future__ import annotations

import argparse
from pathlib import Path


def substitue_unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(
            f"ERRATUM: segmentum {nomen} {numerus} vicibus inventum est; 1 exspectabatur"
        )
    return textus.replace(vetus, novum, 1)


def scribe_api(off: str, nomen: str, praefixum: str) -> str:
    lineae = [
        f"    DECLARA {praefixum} SICUT NUMERUS VALENS SCRIBE_U16(codex, pos_idata + {off}, 0)."
    ]
    for i, ch in enumerate(nomen.encode("ascii"), start=2):
        lineae.append(f"    CODEX_SCRIBE(codex, pos_idata + {off} + {i}, {ch}).")
    lineae.append(
        f"    CODEX_SCRIBE(codex, pos_idata + {off} + {len(nomen) + 2}, 0)."
    )
    return "\n".join(lineae)


AUXILIA_WIN64 = r"""
FUNCTIO COMPONE_RESERVA_OCTETA_DYNAMICA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    DECLARA p_mem_dyn SICUT NUMERUS VALENS pos.
    SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
        p_mem_dyn = COMPONE_TRANSCRIBE(codex, p_mem_dyn, 12, 0).
        CODEX_SCRIBE(codex, p_mem_dyn, 72).
        CODEX_SCRIBE(codex, p_mem_dyn + 1, 131).
        CODEX_SCRIBE(codex, p_mem_dyn + 2, 236).
        CODEX_SCRIBE(codex, p_mem_dyn + 3, 40).
        p_mem_dyn = p_mem_dyn + 4.
        p_mem_dyn = COMPONE_ONERA(codex, p_mem_dyn, 1, 0).
        p_mem_dyn = COMPONE_TRANSCRIBE(codex, p_mem_dyn, 2, 12).
        p_mem_dyn = COMPONE_ONERA(codex, p_mem_dyn, 8, 12288).
        p_mem_dyn = COMPONE_ONERA(codex, p_mem_dyn, 9, 4).
        p_mem_dyn = COMPONE_VOCA_IAT_DYNAMICA(codex, p_mem_dyn, contextus_parseris, 1).
        CODEX_SCRIBE(codex, p_mem_dyn, 72).
        CODEX_SCRIBE(codex, p_mem_dyn + 1, 131).
        CODEX_SCRIBE(codex, p_mem_dyn + 2, 196).
        CODEX_SCRIBE(codex, p_mem_dyn + 3, 40).
        p_mem_dyn = p_mem_dyn + 4.
    ALITER
        p_mem_dyn = COMPONE_RESERVA_OCTETA(codex, p_mem_dyn).
    FIN-SI.
    REDDE p_mem_dyn.
FIN-FUNCTIO.

FUNCTIO COMPONE_APERI_FASCICULUM_PE REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    ACCIPIT accessus SICUT NUMERUS.
    ACCIPIT communio SICUT NUMERUS.
    ACCIPIT dispositio SICUT NUMERUS.
    DECLARA p_ap SICUT NUMERUS VALENS pos.

    CODEX_SCRIBE(codex, p_ap, 72).
    CODEX_SCRIBE(codex, p_ap + 1, 131).
    CODEX_SCRIBE(codex, p_ap + 2, 236).
    CODEX_SCRIBE(codex, p_ap + 3, 56).
    p_ap = p_ap + 4.
    p_ap = COMPONE_TRANSCRIBE(codex, p_ap, 1, 7).
    p_ap = COMPONE_ONERA(codex, p_ap, 2, accessus).
    p_ap = COMPONE_ONERA(codex, p_ap, 8, communio).
    p_ap = COMPONE_ONERA(codex, p_ap, 9, 0).

    p_ap = COMPONE_ONERA(codex, p_ap, 0, dispositio).
    CODEX_SCRIBE(codex, p_ap, 72).
    CODEX_SCRIBE(codex, p_ap + 1, 137).
    CODEX_SCRIBE(codex, p_ap + 2, 68).
    CODEX_SCRIBE(codex, p_ap + 3, 36).
    CODEX_SCRIBE(codex, p_ap + 4, 32).
    p_ap = p_ap + 5.

    p_ap = COMPONE_ONERA(codex, p_ap, 0, 128).
    CODEX_SCRIBE(codex, p_ap, 72).
    CODEX_SCRIBE(codex, p_ap + 1, 137).
    CODEX_SCRIBE(codex, p_ap + 2, 68).
    CODEX_SCRIBE(codex, p_ap + 3, 36).
    CODEX_SCRIBE(codex, p_ap + 4, 40).
    p_ap = p_ap + 5.

    p_ap = COMPONE_ONERA(codex, p_ap, 0, 0).
    CODEX_SCRIBE(codex, p_ap, 72).
    CODEX_SCRIBE(codex, p_ap + 1, 137).
    CODEX_SCRIBE(codex, p_ap + 2, 68).
    CODEX_SCRIBE(codex, p_ap + 3, 36).
    CODEX_SCRIBE(codex, p_ap + 4, 48).
    p_ap = p_ap + 5.
    p_ap = COMPONE_VOCA_IAT_DYNAMICA(codex, p_ap, contextus_parseris, 4).

    CODEX_SCRIBE(codex, p_ap, 72).
    CODEX_SCRIBE(codex, p_ap + 1, 131).
    CODEX_SCRIBE(codex, p_ap + 2, 196).
    CODEX_SCRIBE(codex, p_ap + 3, 56).
    p_ap = p_ap + 4.
    REDDE p_ap.
FIN-FUNCTIO.

FUNCTIO COMPONE_TRANSFER_FASCICULUM_PE REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    ACCIPIT id_api SICUT NUMERUS.
    DECLARA p_tr SICUT NUMERUS VALENS pos.

    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 12, 2).
    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 13, 6).
    CODEX_SCRIBE(codex, p_tr, 72).
    CODEX_SCRIBE(codex, p_tr + 1, 131).
    CODEX_SCRIBE(codex, p_tr + 2, 236).
    CODEX_SCRIBE(codex, p_tr + 3, 56).
    p_tr = p_tr + 4.

    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 1, 7).
    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 2, 13).
    p_tr = COMPONE_TRANSCRIBE(codex, p_tr, 8, 12).
    CODEX_SCRIBE(codex, p_tr, 76).
    CODEX_SCRIBE(codex, p_tr + 1, 141).
    CODEX_SCRIBE(codex, p_tr + 2, 76).
    CODEX_SCRIBE(codex, p_tr + 3, 36).
    CODEX_SCRIBE(codex, p_tr + 4, 40).
    p_tr = p_tr + 5.

    CODEX_SCRIBE(codex, p_tr, 72).
    CODEX_SCRIBE(codex, p_tr + 1, 199).
    CODEX_SCRIBE(codex, p_tr + 2, 68).
    CODEX_SCRIBE(codex, p_tr + 3, 36).
    CODEX_SCRIBE(codex, p_tr + 4, 40).
    CODEX_SCRIBE(codex, p_tr + 5, 0).
    CODEX_SCRIBE(codex, p_tr + 6, 0).
    CODEX_SCRIBE(codex, p_tr + 7, 0).
    CODEX_SCRIBE(codex, p_tr + 8, 0).
    p_tr = p_tr + 9.

    CODEX_SCRIBE(codex, p_tr, 72).
    CODEX_SCRIBE(codex, p_tr + 1, 199).
    CODEX_SCRIBE(codex, p_tr + 2, 68).
    CODEX_SCRIBE(codex, p_tr + 3, 36).
    CODEX_SCRIBE(codex, p_tr + 4, 32).
    CODEX_SCRIBE(codex, p_tr + 5, 0).
    CODEX_SCRIBE(codex, p_tr + 6, 0).
    CODEX_SCRIBE(codex, p_tr + 7, 0).
    CODEX_SCRIBE(codex, p_tr + 8, 0).
    p_tr = p_tr + 9.

    p_tr = COMPONE_VOCA_IAT_DYNAMICA(codex, p_tr, contextus_parseris, id_api).
    p_tr = COMPONE_ONERA(codex, p_tr, 3, 0).
    p_tr = COMPONE_CMP(codex, p_tr, 0, 3).
    DECLARA loci_transfer_err SICUT NUMERUS VALENS 0.
    p_tr = COMPONE_JE_FUTURUM(codex, p_tr, SEDES(loci_transfer_err)).

    CODEX_SCRIBE(codex, p_tr, 72).
    CODEX_SCRIBE(codex, p_tr + 1, 139).
    CODEX_SCRIBE(codex, p_tr + 2, 68).
    CODEX_SCRIBE(codex, p_tr + 3, 36).
    CODEX_SCRIBE(codex, p_tr + 4, 40).
    p_tr = p_tr + 5.
    CODEX_SCRIBE(codex, p_tr, 72).
    CODEX_SCRIBE(codex, p_tr + 1, 131).
    CODEX_SCRIBE(codex, p_tr + 2, 196).
    CODEX_SCRIBE(codex, p_tr + 3, 56).
    p_tr = p_tr + 4.
    DECLARA loci_transfer_fin SICUT NUMERUS VALENS 0.
    p_tr = COMPONE_JMP_FUTURUM(codex, p_tr, SEDES(loci_transfer_fin)).

    DECLARA pos_transfer_err SICUT NUMERUS VALENS p_tr.
    DECLARA ig_transfer_err SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_transfer_err, pos_transfer_err).
    CODEX_SCRIBE(codex, p_tr, 72).
    CODEX_SCRIBE(codex, p_tr + 1, 131).
    CODEX_SCRIBE(codex, p_tr + 2, 196).
    CODEX_SCRIBE(codex, p_tr + 3, 56).
    p_tr = p_tr + 4.
    p_tr = COMPONE_ONERA(codex, p_tr, 0, 0 - 1).

    DECLARA pos_transfer_fin SICUT NUMERUS VALENS p_tr.
    DECLARA ig_transfer_fin SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_transfer_fin, pos_transfer_fin).
    REDDE p_tr.
FIN-FUNCTIO.

FUNCTIO COMPONE_CLAUDE_FASCICULUM_PE REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    DECLARA p_cl SICUT NUMERUS VALENS pos.
    CODEX_SCRIBE(codex, p_cl, 72).
    CODEX_SCRIBE(codex, p_cl + 1, 131).
    CODEX_SCRIBE(codex, p_cl + 2, 236).
    CODEX_SCRIBE(codex, p_cl + 3, 40).
    p_cl = p_cl + 4.
    p_cl = COMPONE_TRANSCRIBE(codex, p_cl, 1, 7).
    p_cl = COMPONE_VOCA_IAT_DYNAMICA(codex, p_cl, contextus_parseris, 6).
    p_cl = COMPONE_ONERA(codex, p_cl, 3, 0).
    p_cl = COMPONE_CMP(codex, p_cl, 0, 3).
    DECLARA loci_cl_err SICUT NUMERUS VALENS 0.
    p_cl = COMPONE_JE_FUTURUM(codex, p_cl, SEDES(loci_cl_err)).
    CODEX_SCRIBE(codex, p_cl, 72).
    CODEX_SCRIBE(codex, p_cl + 1, 131).
    CODEX_SCRIBE(codex, p_cl + 2, 196).
    CODEX_SCRIBE(codex, p_cl + 3, 40).
    p_cl = p_cl + 4.
    p_cl = COMPONE_ONERA(codex, p_cl, 0, 0).
    DECLARA loci_cl_fin SICUT NUMERUS VALENS 0.
    p_cl = COMPONE_JMP_FUTURUM(codex, p_cl, SEDES(loci_cl_fin)).
    DECLARA pos_cl_err SICUT NUMERUS VALENS p_cl.
    DECLARA ig_cl_err SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_cl_err, pos_cl_err).
    CODEX_SCRIBE(codex, p_cl, 72).
    CODEX_SCRIBE(codex, p_cl + 1, 131).
    CODEX_SCRIBE(codex, p_cl + 2, 196).
    CODEX_SCRIBE(codex, p_cl + 3, 40).
    p_cl = p_cl + 4.
    p_cl = COMPONE_ONERA(codex, p_cl, 0, 0 - 1).
    DECLARA pos_cl_fin SICUT NUMERUS VALENS p_cl.
    DECLARA ig_cl_fin SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_cl_fin, pos_cl_fin).
    REDDE p_cl.
FIN-FUNCTIO.
"""


def transforma(textus: str) -> str:
    if "FUNCTIO COMPONE_APERI_FASCICULUM_PE REDDENS NUMERUS." in textus:
        return textus

    textus = substitue_unum(textus,
        "    DECLARA numerus_functionum_pe SICUT NUMERUS VALENS 4.",
        "    DECLARA numerus_functionum_pe SICUT NUMERUS VALENS 7.",
        "numeri importationum PE")

    textus = substitue_unum(textus,
        """    DECLARA off_hint_wf SICUT NUMERUS VALENS off_hint_gsh + 16.
    DECLARA off_nomen_dll SICUT NUMERUS VALENS off_hint_wf + 12.
    DECLARA mensura_idata SICUT NUMERUS VALENS off_nomen_dll + 13.""",
        """    DECLARA off_hint_wf SICUT NUMERUS VALENS off_hint_gsh + 16.
    DECLARA off_hint_cf SICUT NUMERUS VALENS off_hint_wf + 12.
    DECLARA off_hint_rf SICUT NUMERUS VALENS off_hint_cf + 14.
    DECLARA off_hint_ch SICUT NUMERUS VALENS off_hint_rf + 12.
    DECLARA off_nomen_dll SICUT NUMERUS VALENS off_hint_ch + 14.
    DECLARA mensura_idata SICUT NUMERUS VALENS off_nomen_dll + 13.""",
        "offsetorum nominum Win32")

    textus = substitue_unum(textus,
        """    DECLARA rva_hint_wf SICUT NUMERUS VALENS rva_idata + off_hint_wf.
    DECLARA rva_nomen_dll SICUT NUMERUS VALENS rva_idata + off_nomen_dll.""",
        """    DECLARA rva_hint_wf SICUT NUMERUS VALENS rva_idata + off_hint_wf.
    DECLARA rva_hint_cf SICUT NUMERUS VALENS rva_idata + off_hint_cf.
    DECLARA rva_hint_rf SICUT NUMERUS VALENS rva_idata + off_hint_rf.
    DECLARA rva_hint_ch SICUT NUMERUS VALENS rva_idata + off_hint_ch.
    DECLARA rva_nomen_dll SICUT NUMERUS VALENS rva_idata + off_nomen_dll.""",
        "RVA nominum Win32")

    vetus_thunks = """    DECLARA igp11 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt, rva_hint_ep).
    DECLARA igp12 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 8, rva_hint_va).
    DECLARA igp13 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 16, rva_hint_gsh).
    DECLARA igp14 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 24, rva_hint_wf).
    DECLARA igp15 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 32, 0).
    DECLARA igp16 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat, rva_hint_ep).
    DECLARA igp17 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 8, rva_hint_va).
    DECLARA igp18 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 16, rva_hint_gsh).
    DECLARA igp19 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 24, rva_hint_wf).
    DECLARA igp20 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 32, 0)."""
    nova_thunks = """    DECLARA igp11 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt, rva_hint_ep).
    DECLARA igp12 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 8, rva_hint_va).
    DECLARA igp13 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 16, rva_hint_gsh).
    DECLARA igp14 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 24, rva_hint_wf).
    DECLARA igp_cf_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 32, rva_hint_cf).
    DECLARA igp_rf_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 40, rva_hint_rf).
    DECLARA igp_ch_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 48, rva_hint_ch).
    DECLARA igp15 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 56, 0).
    DECLARA igp16 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat, rva_hint_ep).
    DECLARA igp17 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 8, rva_hint_va).
    DECLARA igp18 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 16, rva_hint_gsh).
    DECLARA igp19 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 24, rva_hint_wf).
    DECLARA igp_cf_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 32, rva_hint_cf).
    DECLARA igp_rf_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 40, rva_hint_rf).
    DECLARA igp_ch_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 48, rva_hint_ch).
    DECLARA igp20 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 56, 0)."""
    textus = substitue_unum(textus, vetus_thunks, nova_thunks, "ILT/IAT")

    terminus_wf = "    CODEX_SCRIBE(codex, pos_idata + off_hint_wf + 11, 0)."
    nomina_nova = (terminus_wf + "\n\n" +
        scribe_api("off_hint_cf", "CreateFileA", "igp25") + "\n\n" +
        scribe_api("off_hint_rf", "ReadFile", "igp26") +
        "\n    CODEX_SCRIBE(codex, pos_idata + off_hint_rf + 11, 0).\n\n" +
        scribe_api("off_hint_ch", "CloseHandle", "igp27"))
    textus = substitue_unum(textus, terminus_wf, nomina_nova, "nominum API Win32")

    finis_allocatoris = """FUNCTIO COMPONE_RESERVA_OCTETA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    DECLARA p_mem SICUT NUMERUS VALENS pos.
    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).
    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).
    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).
    p_mem = COMPONE_ONERA(codex, p_mem, 10, 34).
    p_mem = COMPONE_ONERA(codex, p_mem, 8, 0).
    p_mem = COMPONE_ONERA(codex, p_mem, 9, 0).
    p_mem = COMPONE_ONERA(codex, p_mem, 0, 9).
    p_mem = COMPONE_VOCA_NUCLEUM(codex, p_mem).
    REDDE p_mem.
FIN-FUNCTIO."""
    textus = substitue_unum(textus, finis_allocatoris,
        finis_allocatoris + "\n" + AUXILIA_WIN64.rstrip(), "auxiliorum Win64")

    numerus_reservarum = textus.count("COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis))")
    if numerus_reservarum != 4:
        raise SystemExit(f"ERRATUM: {numerus_reservarum} vocationes allocatoris runtime inventae sunt; 4 exspectabantur")
    textus = textus.replace(
        "COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis))",
        "COMPONE_RESERVA_OCTETA_DYNAMICA(codex, CONTENTUM(pos_codicis), contextus_parseris)")

    textus = substitue_unum(textus,
        "            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 4194304 + sedes_viae).",
        """            SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
                CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 5368709120 + 4096 - 512 + sedes_viae).
            ALITER
                CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 4194304 + sedes_viae).
            FIN-SI.""", "viae APERI_LEGERE")

    textus = substitue_unum(textus,
        """        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 6, 0).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 2).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 69 && CONTENTUM(pos_fontis) + 9 < n""",
        """        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_APERI_FASCICULUM_PE(codex, CONTENTUM(pos_codicis), contextus_parseris, 2147483648, 1, 3).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 6, 0).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 0).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 2).
            CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 69 && CONTENTUM(pos_fontis) + 9 < n""", "APERI_LEGERE")

    textus = substitue_unum(textus,
        "            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 4194304 + sedes_viae2).",
        """            SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
                CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 5368709120 + 4096 - 512 + sedes_viae2).
            ALITER
                CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 4194304 + sedes_viae2).
            FIN-SI.""", "viae APERI_SCRIBERE")

    textus = substitue_unum(textus,
        """        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 6, 577).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 420).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 2).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 65 && CONTENTUM(pos_fontis) + 13 < n && fons[CONTENTUM(pos_fontis)+1] == 80""",
        """        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_APERI_FASCICULUM_PE(codex, CONTENTUM(pos_codicis), contextus_parseris, 1073741824, 0, 2).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 6, 577).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 420).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 2).
            CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 65 && CONTENTUM(pos_fontis) + 13 < n && fons[CONTENTUM(pos_fontis)+1] == 80""", "APERI_SCRIBERE")

    textus = substitue_unum(textus,
        "        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 4194304 + sedes_viae3).",
        """        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 5368709120 + 4096 - 512 + sedes_viae3).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 4194304 + sedes_viae3).
        FIN-SI.""", "viae APERI_ADICERE")

    textus = substitue_unum(textus,
        """        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 6, 1089).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 420).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 2).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 67 && CONTENTUM(pos_fontis) + 5 < n""",
        """        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_APERI_FASCICULUM_PE(codex, CONTENTUM(pos_codicis), contextus_parseris, 4, 0, 4).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 6, 1089).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 420).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 2).
            CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 67 && CONTENTUM(pos_fontis) + 5 < n""", "APERI_ADICERE")

    textus = substitue_unum(textus,
        """        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 7, 0).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 3).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 83 && CONTENTUM(pos_fontis) + 18 < n""",
        """        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 7, 0).
        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_CLAUDE_FASCICULUM_PE(codex, CONTENTUM(pos_codicis), contextus_parseris).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 3).
            CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 83 && CONTENTUM(pos_fontis) + 18 < n""", "CLAUDE")

    textus = substitue_unum(textus,
        """        CONTENTUM(pos_codicis) = COMPONE_SUME_PILA(codex, CONTENTUM(pos_codicis), 6, STATUS_LECTIONIS_LEGE(contextus_parseris)).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 0).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 79 && CONTENTUM(pos_fontis) + 6 < n""",
        """        CONTENTUM(pos_codicis) = COMPONE_SUME_PILA(codex, CONTENTUM(pos_codicis), 6, STATUS_LECTIONIS_LEGE(contextus_parseris)).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_TRANSFER_FASCICULUM_PE(codex, CONTENTUM(pos_codicis), contextus_parseris, 5).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 0).
            CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 79 && CONTENTUM(pos_fontis) + 6 < n""", "LEGE")

    textus = substitue_unum(textus,
        """        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 6).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 11).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI (fons[CONTENTUM(pos_fontis)] >= 65 && fons[CONTENTUM(pos_fontis)] <= 90) TUNC""",
        """        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 6).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 11).
        SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_TRANSFER_FASCICULUM_PE(codex, CONTENTUM(pos_codicis), contextus_parseris, 3).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
            CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI (fons[CONTENTUM(pos_fontis)] >= 65 && fons[CONTENTUM(pos_fontis)] <= 90) TUNC""", "MITTE")

    return textus


def principale() -> int:
    parser = argparse.ArgumentParser(description="Stratum fasciculorum Win64 VINDEX 0.53 applicat.")
    parser.add_argument("fons", type=Path)
    parser.add_argument("exitus", nargs="?", type=Path)
    args = parser.parse_args()
    exitus = args.exitus or args.fons
    textus = args.fons.read_text(encoding="utf-8")
    novus = transforma(textus)
    exitus.write_text(novus, encoding="utf-8", newline="\n")
    print(f"RECTE: stratum fasciculorum Win64 scriptum est: {exitus}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
