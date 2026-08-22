#!/usr/bin/env python3
"""VINDEX 0.53: primitivam RESERVA_OCTETA in compilatore auto-hospite addit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO COMPONE_RESERVA_OCTETA REDDENS NUMERUS."


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    numerus = textus.count(exemplar)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("RECTE: memoria dynamica 0.53 iam applicata est.")
        return

    ancora_adiutoris = "FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.\n"
    exige_unum(textus, ancora_adiutoris, "adiutor-memoriae")

    adiutor = '''FUNCTIO COMPONE_RESERVA_OCTETA REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
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
FIN-FUNCTIO.

'''
    textus = textus.replace(ancora_adiutoris, adiutor + ancora_adiutoris, 1)

    initium = textus.find(ancora_adiutoris)
    finis = textus.find("FIN-FUNCTIO.\n", initium)
    if initium < 0 or finis < 0:
        raise SystemExit("ERRATUM: ANALYSA_FACTOR inveniri non potest")
    finis += len("FIN-FUNCTIO.\n")
    corpus = textus[initium:finis]

    ancora_rami = '''    SI fons[CONTENTUM(pos_fontis)] == 34 TUNC
        REDDE COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n).
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 40 TUNC
'''
    exige_unum(corpus, ancora_rami, "ramus-reserva-octeta")

    ramus = '''    SI fons[CONTENTUM(pos_fontis)] == 34 TUNC
        REDDE COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n).
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 82 && CONTENTUM(pos_fontis) + 14 < n && fons[CONTENTUM(pos_fontis)+1] == 69 && fons[CONTENTUM(pos_fontis)+2] == 83 && fons[CONTENTUM(pos_fontis)+3] == 69 && fons[CONTENTUM(pos_fontis)+4] == 82 && fons[CONTENTUM(pos_fontis)+5] == 86 && fons[CONTENTUM(pos_fontis)+6] == 65 && fons[CONTENTUM(pos_fontis)+7] == 95 && fons[CONTENTUM(pos_fontis)+8] == 79 && fons[CONTENTUM(pos_fontis)+9] == 67 && fons[CONTENTUM(pos_fontis)+10] == 84 && fons[CONTENTUM(pos_fontis)+11] == 69 && fons[CONTENTUM(pos_fontis)+12] == 84 && fons[CONTENTUM(pos_fontis)+13] == 65 && fons[CONTENTUM(pos_fontis)+14] == 40 TUNC
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 15.
        ignoratum = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, tabula).
        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        CONTENTUM(pos_codicis) = COMPONE_RESERVA_OCTETA(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 40 TUNC
'''
    corpus = corpus.replace(ancora_rami, ramus, 1)
    textus = textus[:initium] + corpus + textus[finis:]

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: RESERVA_OCTETA in compilatore 0.53 addita est.")


if __name__ == "__main__":
    applica()
