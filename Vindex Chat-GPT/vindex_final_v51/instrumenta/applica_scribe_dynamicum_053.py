#!/usr/bin/env python3
"""VINDEX 0.53: bufferum occultum SCRIBE e pila fixa ad memoriam dynamicam migrat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")

ANCORA_INITII = '''                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 0).

                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 0).
                                    DECLARA pos_ansae_scribe SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
'''

NOVUM_INITIUM = '''                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 0).

                                    CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 6).
                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 0, 6).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 0, 3).
                                    CONTENTUM(pos_codicis) = COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis)).
                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 8, 0).
                                    CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).

                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 0).
                                    DECLARA pos_ansae_scribe SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
'''

VETUS_COPIA = '''                                    CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, 0 - 6000000).
'''
NOVUM_COPIA = '''                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 3, 8).
'''

VETUS_FINIS = '''                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 10).
                                    CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 2, 0 - 6000000).
                                    CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 2, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_SERVA_OCTETUM(codex, CONTENTUM(pos_codicis), 2, 3).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 1, 3).

                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 6, 0 - 6000000).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
'''

NOVUS_FINIS = '''                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 10).
                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 8).
                                    CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 2, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_SERVA_OCTETUM(codex, CONTENTUM(pos_codicis), 2, 3).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 1, 3).

                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 9, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 8).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 1).
                                    CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).

                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 7, 8).
                                    CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 9).
                                    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 11).
                                    CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).
'''


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    numerus = textus.count(exemplar)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if "0 - 6000000" not in textus and "pos_ansae_scribe" in textus:
        print("RECTE: SCRIBE iam memoria dynamica utitur.")
        return

    exige_unum(textus, ANCORA_INITII, "initium-scribe")
    exige_unum(textus, VETUS_COPIA, "copia-scribe")
    exige_unum(textus, VETUS_FINIS, "finis-scribe")

    textus = textus.replace(ANCORA_INITII, NOVUM_INITIUM, 1)
    textus = textus.replace(VETUS_COPIA, NOVUM_COPIA, 1)
    textus = textus.replace(VETUS_FINIS, NOVUS_FINIS, 1)

    if "0 - 6000000" in textus:
        raise SystemExit("ERRATUM: intervallum occultum -6000000 adhuc manet")

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: SCRIBE bufferum memoriae amplitudine executionis reservat et post scripturam liberat.")


if __name__ == "__main__":
    applica()
