#!/usr/bin/env python3
"""VINDEX 0.53: statum DESINE ex tabula historica in contextum explicitum transfert."""

from pathlib import Path


FONS = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
BASIS = Path("Vindex Chat-GPT/vindex_final_v51/instrumenta/TABULA-LITTERALIA-053.txt")

VETUS_ADIUTOR = '''FUNCTIO STATUS_DESINE_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    REDDE tabula[227].
FIN-FUNCTIO.

FUNCTIO STATUS_DESINE_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT valor SICUT NUMERUS.
    tabula[227] = valor.
    REDDE 0.
FIN-FUNCTIO.
'''

NOVUS_ADIUTOR = '''FUNCTIO STATUS_DESINE_LEGE REDDENS NUMERUS.
    ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.
    REDDE CONTENTUM(contextus_desine).
FIN-FUNCTIO.

FUNCTIO STATUS_DESINE_SCRIBE REDDENS NUMERUS.
    ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.
    ACCIPIT valor SICUT NUMERUS.
    CONTENTUM(contextus_desine) = valor.
    REDDE 0.
FIN-FUNCTIO.
'''

VETUS_CAPUT = '''FUNCTIO ANALYSA_BLOCUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos_codicis SICUT ACUS<NUMERUS>.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
'''

NOVUM_CAPUT = '''FUNCTIO ANALYSA_BLOCUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos_codicis SICUT ACUS<NUMERUS>.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.
'''

VETUS_TABULA = "    DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 3000.\n"
NOVA_TABULA = VETUS_TABULA + "    DECLARA contextus_desine SICUT NUMERUS VALENS 0.\n"

VETUS_PRINCIPALIS = "                DECLARA ignoratum SICUT NUMERUS VALENS ANALYSA_BLOCUS(codex, SEDES(pos), fons, SEDES(i), n, tabula)."
NOVA_PRINCIPALIS = "                contextus_desine = 0.\n                DECLARA ignoratum SICUT NUMERUS VALENS ANALYSA_BLOCUS(codex, SEDES(pos), fons, SEDES(i), n, tabula, SEDES(contextus_desine))."

VETUS_ADIUTORIS = "                DECLARA ignoratum4 SICUT NUMERUS VALENS ANALYSA_BLOCUS(codex, SEDES(pos), fons, SEDES(i), n, tabula)."
NOVA_ADIUTORIS = "                contextus_desine = 0.\n                DECLARA ignoratum4 SICUT NUMERUS VALENS ANALYSA_BLOCUS(codex, SEDES(pos), fons, SEDES(i), n, tabula, SEDES(contextus_desine))."

VETUS_RECURSIO = "ANALYSA_BLOCUS(codex, pos_codicis, fons, pos_fontis, n, tabula)"
NOVA_RECURSIO = "ANALYSA_BLOCUS(codex, pos_codicis, fons, pos_fontis, n, tabula, contextus_desine)"


def muta_unum(textus: str, vetus: str, novum: str, nomen: str) -> tuple[str, bool]:
    nv = textus.count(vetus)
    nn = textus.count(novum)
    if nv == 1 and nn == 0:
        return textus.replace(vetus, novum, 1), True
    if nv == 0 and nn == 1:
        return textus, False
    raise SystemExit(f"ERRATUM: mutatio {nomen} ambigua est (vetus={nv}, nova={nn})")


def principale() -> None:
    textus = FONS.read_text(encoding="utf-8")
    mutatum = False

    for vetus, novum, nomen in (
        (VETUS_ADIUTOR, NOVUS_ADIUTOR, "adiutor-desine"),
        (VETUS_CAPUT, NOVUM_CAPUT, "caput-analysae"),
        (VETUS_TABULA, NOVA_TABULA, "contextus-principalis"),
        (VETUS_PRINCIPALIS, NOVA_PRINCIPALIS, "corpus-principale"),
        (VETUS_ADIUTORIS, NOVA_ADIUTORIS, "corpus-functionis"),
    ):
        textus, m = muta_unum(textus, vetus, novum, nomen)
        mutatum = mutatum or m

    nr_vetus = textus.count(VETUS_RECURSIO)
    nr_novus = textus.count(NOVA_RECURSIO)
    if nr_vetus > 0 and nr_novus == 0:
        textus = textus.replace(VETUS_RECURSIO, NOVA_RECURSIO)
        mutatum = True
    elif nr_vetus == 0 and nr_novus > 0:
        pass
    else:
        raise SystemExit(
            f"ERRATUM: recursionis ANALYSA_BLOCUS status ambiguus est "
            f"(vetus={nr_vetus}, novus={nr_novus})"
        )

    textus = textus.replace("STATUS_DESINE_LEGE(tabula)", "STATUS_DESINE_LEGE(contextus_desine)")
    textus = textus.replace("STATUS_DESINE_SCRIBE(tabula,", "STATUS_DESINE_SCRIBE(contextus_desine,")

    if "tabula[227]" in textus:
        raise SystemExit("ERRATUM: tabula[227] post migrationem adhuc adest")
    if textus.count("ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.") < 3:
        raise SystemExit("ERRATUM: contextus DESINE non plene propagatus est")
    if textus.count(NOVA_RECURSIO) < 1:
        raise SystemExit("ERRATUM: contextus DESINE recursionibus non propagatus est")

    FONS.write_text(textus, encoding="utf-8", newline="\n")

    lineae = BASIS.read_text(encoding="utf-8").splitlines()
    si_227 = [i for i, linea in enumerate(lineae) if linea.strip() == "227"]
    if len(si_227) == 1:
        del lineae[si_227[0]]
        BASIS.write_text("\n".join(lineae) + "\n", encoding="utf-8", newline="\n")
        mutatum = True
    elif len(si_227) > 1:
        raise SystemExit("ERRATUM: index 227 in basi plus semel adest")

    if mutatum:
        print("RECTE: status DESINE ex tabula in contextum explicitum migratus est.")
    else:
        print("RECTE: status DESINE iam extra tabulam est.")


if __name__ == "__main__":
    principale()
