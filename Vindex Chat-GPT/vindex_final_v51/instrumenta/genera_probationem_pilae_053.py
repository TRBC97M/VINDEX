#!/usr/bin/env python3
"""Probationem VINDEX cum fasciculo pilae maiore quam unum MiB generat."""

from pathlib import Path
import sys

via = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/pila_magna_053.vindex")

textus = '''FUNCTIO MAGNA REDDENS NUMERUS.
    DECLARA memoria SICUT ORDO DE NUMERUS CAPACITAS 131072.
    memoria[0] = 39.
    memoria[131071] = 777.
    PROCLAMA memoria[0].
    PROCLAMA memoria[131071].
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA status SICUT NUMERUS VALENS MAGNA().
    REDDE status.
FIN-FUNCTIO.
'''

via.write_text(textus, encoding="utf-8")
print(f"RECTE: probatio pilae scripta est: {via}")
