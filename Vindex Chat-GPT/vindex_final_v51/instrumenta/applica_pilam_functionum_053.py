#!/usr/bin/env python3
"""VINDEX 0.53: pilam functionum exacte dimensam et per paginas probatam applicat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS."


def exige(textus: str, fragmentum: str, numerus: int, nomen: str) -> None:
    inventa = textus.count(fragmentum)
    if inventa != numerus:
        raise SystemExit(
            f"ERRATUM: ancora {nomen} {inventa} vicibus inventa est; {numerus} exspectabantur"
        )


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("RECTE: pila functionum iam structurata est.")
        return

    ancora = "FUNCTIO COMPONE_ARITHMETICA REDDENS NUMERUS.\n"
    exige(textus, ancora, 1, "emissoris-pilae")

    adiutor = '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT indice SICUT NUMERUS.
    ACCIPIT spatium SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.

    // mov r11, imm64. Octeta immediata a CORRIGE_PILA post analysin corporis mutantur.
    CODEX_SCRIBE(codex, p, 73).
    CODEX_SCRIBE(codex, p + 1, 187).
    CODEX_SCRIBE(codex, p + 2, spatium & 255).
    CODEX_SCRIBE(codex, p + 3, (spatium >> 8) & 255).
    CODEX_SCRIBE(codex, p + 4, (spatium >> 16) & 255).
    CODEX_SCRIBE(codex, p + 5, (spatium >> 24) & 255).
    CODEX_SCRIBE(codex, p + 6, (spatium >> 32) & 255).
    CODEX_SCRIBE(codex, p + 7, (spatium >> 40) & 255).
    CODEX_SCRIBE(codex, p + 8, (spatium >> 48) & 255).
    CODEX_SCRIBE(codex, p + 9, (spatium >> 56) & 255).

    // cmp r11, 4096; jbe finis.
    CODEX_SCRIBE(codex, p + 10, 73).
    CODEX_SCRIBE(codex, p + 11, 129).
    CODEX_SCRIBE(codex, p + 12, 251).
    CODEX_SCRIBE(codex, p + 13, 0).
    CODEX_SCRIBE(codex, p + 14, 16).
    CODEX_SCRIBE(codex, p + 15, 0).
    CODEX_SCRIBE(codex, p + 16, 0).
    CODEX_SCRIBE(codex, p + 17, 118).
    CODEX_SCRIBE(codex, p + 18, 28).

    // Per singulas paginas: sub rsp,4096; or qword [rsp],0; sub r11,4096; cmp; ja retro.
    CODEX_SCRIBE(codex, p + 19, 72).
    CODEX_SCRIBE(codex, p + 20, 129).
    CODEX_SCRIBE(codex, p + 21, 236).
    CODEX_SCRIBE(codex, p + 22, 0).
    CODEX_SCRIBE(codex, p + 23, 16).
    CODEX_SCRIBE(codex, p + 24, 0).
    CODEX_SCRIBE(codex, p + 25, 0).
    CODEX_SCRIBE(codex, p + 26, 72).
    CODEX_SCRIBE(codex, p + 27, 131).
    CODEX_SCRIBE(codex, p + 28, 12).
    CODEX_SCRIBE(codex, p + 29, 36).
    CODEX_SCRIBE(codex, p + 30, 0).
    CODEX_SCRIBE(codex, p + 31, 73).
    CODEX_SCRIBE(codex, p + 32, 129).
    CODEX_SCRIBE(codex, p + 33, 235).
    CODEX_SCRIBE(codex, p + 34, 0).
    CODEX_SCRIBE(codex, p + 35, 16).
    CODEX_SCRIBE(codex, p + 36, 0).
    CODEX_SCRIBE(codex, p + 37, 0).
    CODEX_SCRIBE(codex, p + 38, 73).
    CODEX_SCRIBE(codex, p + 39, 129).
    CODEX_SCRIBE(codex, p + 40, 251).
    CODEX_SCRIBE(codex, p + 41, 0).
    CODEX_SCRIBE(codex, p + 42, 16).
    CODEX_SCRIBE(codex, p + 43, 0).
    CODEX_SCRIBE(codex, p + 44, 0).
    CODEX_SCRIBE(codex, p + 45, 119).
    CODEX_SCRIBE(codex, p + 46, 228).

    // Reliquum spatium subtrahitur et ultima pagina tangitur.
    CODEX_SCRIBE(codex, p + 47, 76).
    CODEX_SCRIBE(codex, p + 48, 41).
    CODEX_SCRIBE(codex, p + 49, 220).
    CODEX_SCRIBE(codex, p + 50, 72).
    CODEX_SCRIBE(codex, p + 51, 131).
    CODEX_SCRIBE(codex, p + 52, 12).
    CODEX_SCRIBE(codex, p + 53, 36).
    CODEX_SCRIBE(codex, p + 54, 0).

    REDDE p + 55.
FIN-FUNCTIO.

'''
    textus = textus.replace(ancora, adiutor + ancora, 1)

    vetus_prologus = (
        "                pos = COMPONE_ONERA(codex, pos, 0, 30000).\n"
        "                pos = COMPONE_SUB(codex, pos, 4, 0)."
    )
    novus_prologus = "                pos = COMPONE_RESERVA_PILA_PROBATA(codex, pos, 30000)."
    exige(textus, vetus_prologus, 2, "prologus-functionum")
    textus = textus.replace(vetus_prologus, novus_prologus)

    vetus1 = "DECLARA spatium_necessarium1 SICUT NUMERUS VALENS (0 - tabula[51]) + 10000."
    novum1 = "DECLARA spatium_necessarium1 SICUT NUMERUS VALENS (((0 - tabula[51]) + 15) / 16) * 16."
    exige(textus, vetus1, 1, "mensura-principalis")
    textus = textus.replace(vetus1, novum1, 1)

    vetus2 = "DECLARA spatium_necessarium2 SICUT NUMERUS VALENS (0 - tabula[51]) + 10000."
    novum2 = "DECLARA spatium_necessarium2 SICUT NUMERUS VALENS (((0 - tabula[51]) + 15) / 16) * 16."
    exige(textus, vetus2, 1, "mensura-functionis")
    textus = textus.replace(vetus2, novum2, 1)

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: pila functionum exacte dimensata et per paginas probata est.")


if __name__ == "__main__":
    applica()
