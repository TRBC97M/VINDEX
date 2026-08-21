#!/usr/bin/env python3
"""VINDEX 0.53: receptaculum occultum LEGE e pila fixa ad memoriam dynamicam migrat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
VETUS = "COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 6, 0 - 5000000)"
NOVUM = "tabula[2999] = tabula[51]"


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    numerus = textus.count(exemplar)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if "5000000" not in textus and NOVUM in textus:
        print("RECTE: LEGE memoria dynamica iam utitur.")
        return

    vetus_lege = '''        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 1000000).
        CONTENTUM(pos_codicis) = COMPONE_SUB(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_JGE_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(ig_lg)).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1000000).
        DECLARA pos_lege_recte SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
        ig_lg = CORRIGE_SALTUM(codex, ig_lg, pos_lege_recte).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 6, 0 - 5000000).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
'''
    novum_lege = '''        tabula[2999] = tabula[51].
        tabula[51] = tabula[51] - 8.
        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
        CONTENTUM(pos_codicis) = COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis)).
        CONTENTUM(pos_codicis) = COMPONE_SERVA_PILA(codex, CONTENTUM(pos_codicis), tabula[2999], 0).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).
        CONTENTUM(pos_codicis) = COMPONE_SUME_PILA(codex, CONTENTUM(pos_codicis), 6, tabula[2999]).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
'''
    exige_unum(textus, vetus_lege, "corpus-lege")
    textus = textus.replace(vetus_lege, novum_lege, 1)

    vetus_octetus = "        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, 0 - 5000000).\n"
    novum_octetus = "        CONTENTUM(pos_codicis) = COMPONE_SUME_PILA(codex, CONTENTUM(pos_codicis), 3, tabula[2999]).\n"
    exige_unum(textus, vetus_octetus, "octetus-lege")
    textus = textus.replace(vetus_octetus, novum_octetus, 1)

    vetus_scriptio = "                                    CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 6, 0 - 5000000).\n"
    novum_scriptio = "                                    CONTENTUM(pos_codicis) = COMPONE_SUME_PILA(codex, CONTENTUM(pos_codicis), 6, tabula[2999]).\n"
    exige_unum(textus, vetus_scriptio, "scribe-lectus")
    textus = textus.replace(vetus_scriptio, novum_scriptio, 1)

    if "5000000" in textus:
        raise SystemExit("ERRATUM: receptaculum fixum LEGE adhuc manet")

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: LEGE et OCTETUS receptaculum dynamicum commune adhibent.")


if __name__ == "__main__":
    applica()
