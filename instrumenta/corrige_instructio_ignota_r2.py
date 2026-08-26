#!/usr/bin/env python3
"""R2: impedit ut verbum maiusculum sine '(' pro vocatione accipiatur."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = VIA.read_text(encoding="utf-8")

signum = "DECLARA idx_instructio_ignota SICUT NUMERUS"
if signum in textus:
    print("RECTE: correctio instructionis ignotae iam adest.")
    raise SystemExit(0)

vetus = '''        DECLARA positio_vocationis SICUT NUMERUS VALENS CONTENTUM(pos_fontis).
        DECLARA nomen_fn SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).
        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.

        DECLARA numerus_argumentorum SICUT NUMERUS VALENS 0.'''

novus = '''        DECLARA positio_vocationis SICUT NUMERUS VALENS CONTENTUM(pos_fontis).
        DECLARA nomen_fn SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).
        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).

        SI CONTENTUM(pos_fontis) >= n || fons[CONTENTUM(pos_fontis)] != 40 TUNC
            DECLARA idx_instructio_ignota SICUT NUMERUS VALENS PARES_QUANTITAS(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris)).
            DECLARA ig_instructio_ignota SICUT NUMERUS VALENS PARES_SCRIBE(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris), idx_instructio_ignota, 0, 0).
            ig_instructio_ignota = PARES_SCRIBE(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris), idx_instructio_ignota, 1, 0).
            ig_instructio_ignota = PARES_SCRIBE(POSITIONES_PENDENTES_LEGE(contextus_parseris), idx_instructio_ignota, 0, positio_vocationis).
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 0).
            DUM CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] != 46 PERFICE
                CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
            FIN-DUM.
            REDDE 0.
        FIN-SI.

        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.

        DECLARA numerus_argumentorum SICUT NUMERUS VALENS 0.'''

numerus = textus.count(vetus)
if numerus != 1:
    raise SystemExit(f"ERRATUM: ancora vocationis genericae inventa est {numerus} vicibus")

textus = textus.replace(vetus, novus, 1)
VIA.write_text(textus, encoding="utf-8")
print("RECTE: instructio ignota sine '(' ad diagnosticum stabile ducitur.")
