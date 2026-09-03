#!/usr/bin/env python3
"""P11-C: literalem TEXTUS secundum target ELF/PE adressat.

Historice COMPONE_LITTERALE_TEXTUS 0x400000 semper addebat. Hoc sub PE32+
invalidum est. Instrumentum temporarium est et ante fusionem removendum.
"""
from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
VIA = RADIX / "Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex"
textus = VIA.read_text(encoding="utf-8")
marca = "// P11-C — locus litteralis TEXTUS secundum target ELF/PE."
if marca in textus:
    print("RECTE: litterale TEXTUS PE iam target-aware est.")
    raise SystemExit(0)

vetus_sig = '''    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    DECLARA loci_saltus_textus SICUT NUMERUS VALENS 0.
'''
novus_sig = '''    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT NUMERUS.
    DECLARA loci_saltus_textus SICUT NUMERUS VALENS 0.
'''
if textus.count(vetus_sig) != 1:
    raise SystemExit(f"ERRATUM: signatura COMPONE_LITTERALE_TEXTUS non unica ({textus.count(vetus_sig)})")
textus = textus.replace(vetus_sig, novus_sig, 1)

vetus_call = "COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n)"
if textus.count(vetus_call) != 1:
    raise SystemExit(f"ERRATUM: vocatio COMPONE_LITTERALE_TEXTUS non unica ({textus.count(vetus_call)})")
textus = textus.replace(vetus_call, vetus_call[:-1] + ", contextus_parseris)", 1)

vetus_fin = '''    ign_textus = CORRIGE_SALTUM(codex, loci_saltus_textus, CONTENTUM(pos_codicis)).
    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 4194304 + sedes_textus).
    REDDE 0.
FIN-FUNCTIO.
'''
novus_fin = '''    ign_textus = CORRIGE_SALTUM(codex, loci_saltus_textus, CONTENTUM(pos_codicis)).
    // P11-C — locus litteralis TEXTUS secundum target ELF/PE.
    DECLARA locus_textus_reale SICUT NUMERUS VALENS 4194304 + sedes_textus.
    SI MODUS_PE_LEGE(contextus_parseris) >= 1 TUNC
        locus_textus_reale = 5368709120 + 4096 - 512 + sedes_textus.
    FIN-SI.
    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, locus_textus_reale).
    REDDE 0.
FIN-FUNCTIO.
'''
if textus.count(vetus_fin) != 1:
    raise SystemExit(f"ERRATUM: finis litteralis TEXTUS non unicus ({textus.count(vetus_fin)})")
textus = textus.replace(vetus_fin, novus_fin, 1)

VIA.write_text(textus, encoding="utf-8")
print("RECTE: litteralia TEXTUS ELF/PE target-aware sunt.")
