#!/usr/bin/env python3
"""Compatibilitas nominis P16-IX; canon hodiernus probationem P16-XI-B synchronam exercet."""
from __future__ import annotations

import importlib.util
from pathlib import Path


def principale() -> int:
    via = Path(__file__).resolve().with_name("proba_initium_sylviae_xib_sync.py")
    spec = importlib.util.spec_from_file_location("proba_initium_xib_sync", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("probator INITII P16-XI-B synchronus importari non potest")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return int(mod.principale())


if __name__ == "__main__":
    raise SystemExit(principale())
