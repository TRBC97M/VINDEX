#!/usr/bin/env python3
"""VINDEX 0.53: characterem CR inter spatia canonica agnoscendum addit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")

VETUS = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 9) PERFICE\n"
)

NOVUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 13 || "
    "fons[CONTENTUM(pos)] == 9) PERFICE\n"
)


def main() -> None:
    textus = VIA.read_text(encoding="utf-8")

    if NOVUM in textus:
        print("RECTE: CR iam inter spatia VINDEX agnoscitur.")
        return

    numerus = textus.count(VETUS)
    if numerus != 1:
        raise SystemExit(
            f"ERRATUM: forma IGNORA_SPATIA {numerus} vicibus inventa est; una exspectabatur"
        )

    VIA.write_text(textus.replace(VETUS, NOVUM, 1), encoding="utf-8", newline="\n")
    print("RECTE: CR inter spatia VINDEX agnoscitur.")


if __name__ == "__main__":
    main()
