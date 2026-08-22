#!/usr/bin/env python3
"""VINDEX 0.53: accessus 227 et 2999 sub accessoribus nominatis encapsulat."""

from pathlib import Path


VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO DESINE_LOCUS_LEGE REDDENS NUMERUS."
ANCORA = "FUNCTIO CERCA_VARIABILEM REDDENS NUMERUS.\n"

ADIUTORES = '''FUNCTIO DESINE_LOCUS_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    REDDE tabula[227].
FIN-FUNCTIO.

FUNCTIO DESINE_LOCUS_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT valor SICUT NUMERUS.
    tabula[227] = valor.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO LECTIO_INTERVALLUM_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    REDDE tabula[2999].
FIN-FUNCTIO.

FUNCTIO LECTIO_INTERVALLUM_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT valor SICUT NUMERUS.
    tabula[2999] = valor.
    REDDE 0.
FIN-FUNCTIO.

'''


def principale() -> None:
    textus = VIA.read_text(encoding="utf-8")
    mutatum = False

    mutationes_227 = (
        ("tabula[227] = loci_desine.", "DESINE_LOCUS_SCRIBE(tabula, loci_desine).", "desine-scribe"),
        (
            "DECLARA tabula79_ante SICUT NUMERUS VALENS tabula[227].",
            "DECLARA tabula79_ante SICUT NUMERUS VALENS DESINE_LOCUS_LEGE(tabula).",
            "desine-serva",
        ),
        ("tabula[227] = 0.", "DESINE_LOCUS_SCRIBE(tabula, 0).", "desine-purga"),
        ("SI tabula[227] != 0 TUNC", "SI DESINE_LOCUS_LEGE(tabula) != 0 TUNC", "desine-proba"),
        (
            "CORRIGE_SALTUM(codex, tabula[227], pos_fin_dum)",
            "CORRIGE_SALTUM(codex, DESINE_LOCUS_LEGE(tabula), pos_fin_dum)",
            "desine-corrige",
        ),
        ("tabula[227] = tabula79_ante.", "DESINE_LOCUS_SCRIBE(tabula, tabula79_ante).", "desine-restitue"),
    )

    adiutores_adsunt = MARCA in textus

    for vetus, novum, nomen in mutationes_227:
        n_vetus = textus.count(vetus)
        n_novus = textus.count(novum)
        if n_vetus == 1 and n_novus == 0:
            textus = textus.replace(vetus, novum, 1)
            mutatum = True
        elif n_vetus == 0 and n_novus == 1:
            pass
        else:
            raise SystemExit(
                f"ERRATUM: status mutationis {nomen} ambiguus est "
                f"(vetus={n_vetus}, novus={n_novus})"
            )

    vetus_scriptio_2999 = "tabula[2999] = tabula[51]."
    nova_scriptio_2999 = "LECTIO_INTERVALLUM_SCRIBE(tabula, tabula[51])."
    if textus.count(vetus_scriptio_2999) == 1 and textus.count(nova_scriptio_2999) == 0:
        textus = textus.replace(vetus_scriptio_2999, nova_scriptio_2999, 1)
        mutatum = True
    elif not (
        textus.count(vetus_scriptio_2999) == 0
        and textus.count(nova_scriptio_2999) == 1
    ):
        raise SystemExit("ERRATUM: status scripturae 2999 ambiguus est")

    # Ante insertionem adiutorum quattuor lectiones directae restant. Post
    # encapsulationem soli duo accessus in ipsis adiutoribus manent.
    si_directae_2999 = textus.count("tabula[2999]")
    if not adiutores_adsunt:
        if si_directae_2999 != 4:
            raise SystemExit(
                f"ERRATUM: quattuor lectiones 2999 exspectabantur; inventae={si_directae_2999}"
            )
        textus = textus.replace("tabula[2999]", "LECTIO_INTERVALLUM_LEGE(tabula)")
        mutatum = True
    elif si_directae_2999 != 2:
        raise SystemExit(
            f"ERRATUM: soli duo accessus 2999 in adiutoribus exspectantur; inventi={si_directae_2999}"
        )

    if not adiutores_adsunt:
        if textus.count(ANCORA) != 1:
            raise SystemExit("ERRATUM: ancora adiutorum tabulae non unica est")
        if textus.count("tabula[227]") != 0:
            raise SystemExit("ERRATUM: accessus 227 directus ante adiutores mansit")
        textus = textus.replace(ANCORA, ADIUTORES + ANCORA, 1)
        mutatum = True

    if textus.count("tabula[227]") != 2:
        raise SystemExit("ERRATUM: 227 post encapsulationem bis tantum apparere debet")
    if textus.count("tabula[2999]") != 2:
        raise SystemExit("ERRATUM: 2999 post encapsulationem bis tantum apparere debet")

    VIA.write_text(textus, encoding="utf-8", newline="\n")
    if mutatum:
        print("RECTE: DESINE et status lectionis sub accessoribus nominatis encapsulata sunt.")
    else:
        print("RECTE: DESINE et status lectionis iam encapsulata sunt.")


if __name__ == "__main__":
    principale()
