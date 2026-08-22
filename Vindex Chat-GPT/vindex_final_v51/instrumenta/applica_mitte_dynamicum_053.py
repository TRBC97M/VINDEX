#!/usr/bin/env python3
"""VINDEX 0.53: bufferum fixum MITTE memoria dynamica substituit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA_VETUS = "COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, 0 - 6500000)"
MARCA_NOVA = "COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis))"


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    numerus = textus.count(exemplar)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA_VETUS not in textus and "0 - 6500000" not in textus and MARCA_NOVA in textus:
        print("RECTE: MITTE memoria dynamica iam utitur.")
        return

    vetus_initium = '''        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 0).
        ig_mi = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.

        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 0).
'''
    novum_initium = '''        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 0).
        ig_mi = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.

        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 7).
        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 6).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 0, 6).
        CONTENTUM(pos_codicis) = COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis)).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 11, 0).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).

        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 0).
'''
    exige_unum(textus, vetus_initium, "initium-mitte")
    textus = textus.replace(vetus_initium, novum_initium, 1)

    vetus_buffer = '''        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, 0 - 6500000).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 3, 1).
'''
    novum_buffer = '''        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 3, 11).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 3, 1).
'''
    exige_unum(textus, vetus_buffer, "buffer-mitte")
    textus = textus.replace(vetus_buffer, novum_buffer, 1)

    vetus_fin = '''        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 6).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 6, 0 - 6500000).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
'''
    novum_fin = '''        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 6).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 11).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
'''
    exige_unum(textus, vetus_fin, "finis-mitte")
    textus = textus.replace(vetus_fin, novum_fin, 1)

    vetus_pila = '''                DECLARA spatium_necessarium1 SICUT NUMERUS VALENS (0 - tabula[51]) + 10000.
                SI spatium_necessarium1 < 7000000 TUNC
                    spatium_necessarium1 = 7000000.
                FIN-SI.
                DECLARA ig_corr1 SICUT NUMERUS VALENS CORRIGE_PILA(codex, positio_reservationis1, spatium_necessarium1).
'''
    novum_pila = '''                DECLARA spatium_necessarium1 SICUT NUMERUS VALENS (0 - tabula[51]) + 10000.
                DECLARA ig_corr1 SICUT NUMERUS VALENS CORRIGE_PILA(codex, positio_reservationis1, spatium_necessarium1).
'''
    exige_unum(textus, vetus_pila, "pila-principalis")
    textus = textus.replace(vetus_pila, novum_pila, 1)

    if "6500000" in textus or "7000000" in textus:
        raise SystemExit("ERRATUM: limes pilae fixus adhuc in compilatore manet")

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: MITTE bufferum dynamicum adhibet et limes pilae VII MiB remotus est.")


if __name__ == "__main__":
    applica()
