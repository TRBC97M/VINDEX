#!/usr/bin/env python3
"""P16-XI-A: fontes PNG in asseta SIMG II deterministica convertit."""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

FAMILIA = {
    "programmata": 101,
    "tabula": 102,
    "terminale": 103,
    "officina": 104,
}
SCALAE = (
    ("1x", 1000, 48),
    ("1_5x", 1500, 72),
    ("2x", 2000, 96),
)


def importator():
    via = Path(__file__).resolve().with_name("simg_ii_importa_png.py")
    spec = importlib.util.spec_from_file_location("simg_ii_importa_png", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("importator SIMG II importari non potest")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def radices() -> tuple[Path, Path]:
    radix = Path(__file__).resolve().parents[1]
    fons = radix / "res" / "jlux" / "assetta" / "premium-i" / "png"
    destinatio = radix / "res" / "jlux" / "assetta" / "premium-i" / "simg"
    return fons, destinatio


def genera(destinatio: Path | None = None, *, verbose: bool = True) -> list[Path]:
    m = importator()
    fons, canonica = radices()
    outdir = canonica if destinatio is None else destinatio
    outdir.mkdir(parents=True, exist_ok=True)
    scripta: list[Path] = []
    for nomen in FAMILIA:
        for suffixum, scala, latus in SCALAE:
            png = fons / f"{nomen}@{suffixum}.png"
            si_non = outdir / f"{nomen}@{suffixum}.simg"
            w, h, rgba = m.png_rgba(png.read_bytes())
            if (w, h) != (latus, latus):
                raise RuntimeError(f"{png}: geometria {w}x{h}, exspectata {latus}x{latus}")
            corpus, compressio = m.simg_ii(
                w,
                h,
                rgba,
                kind=2,
                scale=scala,
                compression="auto",
                nine=None,
                hotspot=None,
            )
            si_non.write_bytes(corpus)
            scripta.append(si_non)
            if verbose:
                print(
                    f"RECTE: {png.name} -> {si_non.name}: "
                    f"{w}x{h}, scala={scala}, genus=icona, {compressio}, {len(corpus)} octeta"
                )
    return scripta


def argumenta(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="P16-XI-A PNG fontes in SIMG II convertit")
    p.add_argument("--destinatio", type=Path, help="directorium SIMG II alternum")
    p.add_argument("--quietum", action="store_true", help="lineas singulorum assetorum tace")
    return p.parse_args(argv)


def principale(argv: list[str] | None = None) -> int:
    ns = argumenta(sys.argv[1:] if argv is None else argv)
    try:
        scripta = genera(ns.destinatio, verbose=not ns.quietum)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"DEFECIT: {exc}", file=sys.stderr)
        return 2
    print(f"RECTE: {len(scripta)} asseta SIMG II P16-XI-A generata sunt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
