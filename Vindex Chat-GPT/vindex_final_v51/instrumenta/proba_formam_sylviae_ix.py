#!/usr/bin/env python3
"""Compatibilitas nominis P16-IX; canon hodiernus probationem P16-XI-B exercet."""
from __future__ import annotations

import importlib.util
from pathlib import Path


def principale() -> int:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_xib.py")
    spec = importlib.util.spec_from_file_location("proba_formam_xib", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("probator P16-XI-B importari non potest")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return int(mod.principale())


if __name__ == "__main__":
    raise SystemExit(principale())
