#!/usr/bin/env python3
"""Vocationes Win64 ad RSP XVI-alineatum independentem a conventione interna VINDEX redigit."""

from __future__ import annotations

import argparse
from pathlib import Path


def unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    n = textus.count(vetus)
    if n != 1:
        raise SystemExit(f"ERRATUM: {n} segmenta {nomen}; 1 exspectabatur")
    return textus.replace(vetus, novum, 1)


def plura(textus: str, vetus: str, novum: str, numerus: int, nomen: str) -> str:
    n = textus.count(vetus)
    if n != numerus:
        raise SystemExit(f"ERRATUM: {n} segmenta {nomen}; {numerus} exspectabantur")
    return textus.replace(vetus, novum)


def apta_indentum(textus: str, indentum: int) -> str:
    si indentum == 8:
        return textus
    praefixum = " " * indentum
    return "\n".join(praefixum + linea[8:] if linea.startswith("        ") else linea for linea in textus.splitlines())


def prologus(var: str, spatium: int, indentum: int = 8) -> str:
    textus = f"""        CODEX_SCRIBE(codex, {var}, 73).
        CODEX_SCRIBE(codex, {var} + 1, 137).
        CODEX_SCRIBE(codex, {var} + 2, 230).
        {var} = {var} + 3.
        CODEX_SCRIBE(codex, {var}, 72).
        CODEX_SCRIBE(codex, {var} + 1, 131).
        CODEX_SCRIBE(codex, {var} + 2, 228).
        CODEX_SCRIBE(codex, {var} + 3, 240).
        {var} = {var} + 4.
        CODEX_SCRIBE(codex, {var}, 72).
        CODEX_SCRIBE(codex, {var} + 1, 131).
        CODEX_SCRIBE(codex, {var} + 2, 236).
        CODEX_SCRIBE(codex, {var} + 3, {spatium}).
        {var} = {var} + 4."""
    return apta_indentum(textus, indentum)


def epilogus(var: str, indentum: int = 8) -> str:
    textus = f"""        CODEX_SCRIBE(codex, {var}, 76).
        CODEX_SCRIBE(codex, {var} + 1, 137).
        CODEX_SCRIBE(codex, {var} + 2, 244).
        {var} = {var} + 3."""
    return apta_indentum(textus, indentum)


def vetus_sub(var: str, spatium: int, indentum: int = 8) -> str:
    textus = f"""        CODEX_SCRIBE(codex, {var}, 72).
        CODEX_SCRIBE(codex, {var} + 1, 131).
        CODEX_SCRIBE(codex, {var} + 2, 236).
        CODEX_SCRIBE(codex, {var} + 3, {spatium}).
        {var} = {var} + 4."""
    return apta_indentum(textus, indentum)


def vetus_add(var: str, spatium: int, indentum: int = 8) -> str:
    textus = f"""        CODEX_SCRIBE(codex, {var}, 72).
        CODEX_SCRIBE(codex, {var} + 1, 131).
        CODEX_SCRIBE(codex, {var} + 2, 196).
        CODEX_SCRIBE(codex, {var} + 3, {spatium}).
        {var} = {var} + 4."""
    return apta_indentum(textus, indentum)


def intra_functio(textus: str, nomen: str, sequens: str, mutator) -> str:
    initium = textus.find(nomen)
    if initium < 0:
        raise SystemExit(f"ERRATUM: functio {nomen} deest")
    finis = textus.find(sequens, initium + len(nomen))
    if finis < 0:
        raise SystemExit(f"ERRATUM: terminus post {nomen} deest")
    pars = textus[initium:finis]
    nova = mutator(pars)
    return textus[:initium] + nova + textus[finis:]


def transforma(textus: str) -> str:
    si_marker = "CODEX_SCRIBE(codex, p_ap + 2, 230)."
    if si_marker in textus:
        return textus

    def allocator(pars: str) -> str:
        pars = unum(pars, vetus_sub("p_mem_dyn", 40), prologus("p_mem_dyn", 32), "prologi allocatoris")
        return unum(pars, vetus_add("p_mem_dyn", 40), epilogus("p_mem_dyn"), "epilogi allocatoris")

    textus = intra_functio(
        textus,
        "FUNCTIO COMPONE_RESERVA_OCTETA_DYNAMICA REDDENS NUMERUS.",
        "FUNCTIO COMPONE_APERI_FASCICULUM_PE REDDENS NUMERUS.",
        allocator,
    )

    def aperi(pars: str) -> str:
        pars = unum(pars, vetus_sub("p_ap", 56, 4), prologus("p_ap", 64, 4), "prologi CreateFileA")
        return unum(pars, vetus_add("p_ap", 56, 4), epilogus("p_ap", 4), "epilogi CreateFileA")

    textus = intra_functio(
        textus,
        "FUNCTIO COMPONE_APERI_FASCICULUM_PE REDDENS NUMERUS.",
        "FUNCTIO COMPONE_TRANSFER_FASCICULUM_PE REDDENS NUMERUS.",
        aperi,
    )

    def transfer(pars: str) -> str:
        pars = unum(pars, vetus_sub("p_tr", 56, 4), prologus("p_tr", 64, 4), "prologi transferendi")
        return plura(pars, vetus_add("p_tr", 56, 4), epilogus("p_tr", 4), 2, "epilogorum transferendi")

    textus = intra_functio(
        textus,
        "FUNCTIO COMPONE_TRANSFER_FASCICULUM_PE REDDENS NUMERUS.",
        "FUNCTIO COMPONE_CLAUDE_FASCICULUM_PE REDDENS NUMERUS.",
        transfer,
    )

    def claude(pars: str) -> str:
        pars = unum(pars, vetus_sub("p_cl", 40, 4), prologus("p_cl", 32, 4), "prologi CloseHandle")
        return plura(pars, vetus_add("p_cl", 40, 4), epilogus("p_cl", 4), 2, "epilogorum CloseHandle")

    textus = intra_functio(
        textus,
        "FUNCTIO COMPONE_CLAUDE_FASCICULUM_PE REDDENS NUMERUS.",
        "FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.",
        claude,
    )
    return textus


def principale() -> int:
    p = argparse.ArgumentParser(description="Alignationem API Win64 VINDEX 0.53 corrigit.")
    p.add_argument("fons", type=Path)
    p.add_argument("exitus", nargs="?", type=Path)
    args = p.parse_args()
    exitus = args.exitus or args.fons
    textus = args.fons.read_text(encoding="utf-8")
    exitus.write_text(transforma(textus), encoding="utf-8", newline="\n")
    print(f"RECTE: pila API Win64 XVI-alineata est: {exitus}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
