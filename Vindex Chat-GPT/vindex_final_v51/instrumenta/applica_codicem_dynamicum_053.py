#!/usr/bin/env python3
"""VINDEX 0.53: migrationem codicis dynamicam applicat et descriptorium rite collocat."""

from pathlib import Path

import applica_codicem_dynamicum_053_basis as basis

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")

VETUS = '''    DECLARA codex SICUT ORDO DE NUMERUS CAPACITAS 3.
    DECLARA status_initii_codicis SICUT NUMERUS VALENS INITIA_CODEX(codex, 65536).
    SI status_initii_codicis != 0 TUNC
        PROCLAMA "ERRATUM: memoria codicis reservata non est".
        REDDE 71.
    FIN-SI.
'''

NOVUS = '''    DECLARA codex SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(24).
    SI codex < 0 TUNC
        PROCLAMA "ERRATUM: descriptorium codicis reservatum non est".
        REDDE 71.
    FIN-SI.
    DECLARA status_initii_codicis SICUT NUMERUS VALENS INITIA_CODEX(codex, 65536).
    SI status_initii_codicis != 0 TUNC
        PROCLAMA "ERRATUM: memoria codicis reservata non est".
        REDDE 71.
    FIN-SI.
'''


def corrige_descriptorium() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if NOVUS in textus:
        print("RECTE: descriptorium codicis iam in memoria dynamica est.")
        return
    si = textus.count(VETUS)
    if si != 1:
        raise SystemExit(f"ERRATUM: descriptorium codicis vetus {si} vicibus inventum est")
    VIA.write_text(textus.replace(VETUS, NOVUS, 1), encoding="utf-8")
    print("RECTE: descriptorium codicis XXIV octeta dynamice reservat.")


if __name__ == "__main__":
    basis.applica()
    corrige_descriptorium()
