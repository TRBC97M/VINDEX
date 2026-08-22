#!/usr/bin/env python3
"""VINDEX 0.53: limites fontium fixos adiutoribus dynamicis removet."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO LEGE_TOTUM_DYNAMICUM REDDENS NUMERUS."
PARAM_FONS_VETUS = "ACCIPIT fons SICUT ORDO DE LITTERA."
PARAM_FONS_NOVUS = "ACCIPIT fons SICUT ACUS<LITTERA>."


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    n = textus.count(exemplar)
    if n != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {n} vicibus inventa est")


def seca(textus: str, initium: str, finis: str, novum: str, nomen: str) -> str:
    exige_unum(textus, initium, nomen)
    a = textus.index(initium)
    b = textus.index(finis, a)
    return textus[:a] + novum + textus[b:]


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if (
        MARCA in textus
        and "CAPACITAS 213000" not in textus
        and "LEGE(fd, 213001)" not in textus
        and PARAM_FONS_VETUS not in textus
    ):
        print("RECTE: fontes dynamici iam applicati sunt.")
        return

    ancora = "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n"
    exige_unum(textus, ancora, "principalis")
    adiutores = '''FUNCTIO LEGE_TOTUM_DYNAMICUM REDDENS NUMERUS.
    ACCIPIT descriptor SICUT NUMERUS.
    ACCIPIT longitudo SICUT ACUS<NUMERUS>.
    DECLARA limen SICUT NUMERUS VALENS 65536.
    DECLARA basis SICUT NUMERUS VALENS RESERVA_OCTETA(limen).
    SI basis < 0 TUNC
        CONTENTUM(longitudo) = 0 - 1.
        REDDE basis.
    FIN-SI.
    DECLARA quantitas SICUT NUMERUS VALENS 0.
    DECLARA continua SICUT NUMERUS VALENS 1.
    DUM continua == 1 PERFICE
        DECLARA pars SICUT NUMERUS VALENS LEGE(descriptor, 65536).
        SI pars < 0 TUNC
            CONTENTUM(longitudo) = 0 - 1.
            REDDE pars.
        FIN-SI.
        SI pars == 0 TUNC
            continua = 0.
        ALITER
            SI quantitas + pars > limen TUNC
                DECLARA nova_capacitas SICUT NUMERUS VALENS limen * 2.
                DUM nova_capacitas < quantitas + pars PERFICE
                    nova_capacitas = nova_capacitas * 2.
                FIN-DUM.
                DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(nova_capacitas).
                SI nova_basis < 0 TUNC
                    CONTENTUM(longitudo) = 0 - 1.
                    REDDE nova_basis.
                FIN-SI.
                DECLARA i SICUT NUMERUS VALENS 0.
                DUM i < quantitas PERFICE
                    SCRIBE_OCTETUM_AB(nova_basis + i, OCTETUS_AB(basis + i)).
                    i = i + 1.
                FIN-DUM.
                basis = nova_basis.
                limen = nova_capacitas.
            FIN-SI.
            DECLARA j SICUT NUMERUS VALENS 0.
            DUM j < pars PERFICE
                SCRIBE_OCTETUM_AB(basis + quantitas + j, OCTETUS(j)).
                j = j + 1.
            FIN-DUM.
            quantitas = quantitas + pars.
        FIN-SI.
    FIN-DUM.
    CONTENTUM(longitudo) = quantitas.
    REDDE basis.
FIN-FUNCTIO.

FUNCTIO ASSECURA_BUFFERUM REDDENS NUMERUS.
    ACCIPIT basis SICUT NUMERUS.
    ACCIPIT longitudo SICUT NUMERUS.
    ACCIPIT necessaria SICUT NUMERUS.
    ACCIPIT limen SICUT ACUS<NUMERUS>.
    SI necessaria <= CONTENTUM(limen) TUNC
        REDDE basis.
    FIN-SI.
    DECLARA nova_capacitas SICUT NUMERUS VALENS CONTENTUM(limen) * 2.
    DUM nova_capacitas < necessaria PERFICE
        nova_capacitas = nova_capacitas * 2.
    FIN-DUM.
    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(nova_capacitas).
    SI nova_basis < 0 TUNC
        REDDE nova_basis.
    FIN-SI.
    DECLARA i SICUT NUMERUS VALENS 0.
    DUM i < longitudo PERFICE
        SCRIBE_OCTETUM_AB(nova_basis + i, OCTETUS_AB(basis + i)).
        i = i + 1.
    FIN-DUM.
    CONTENTUM(limen) = nova_capacitas.
    REDDE nova_basis.
FIN-FUNCTIO.

'''
    textus = textus.replace(ancora, adiutores + ancora, 1)

    # Fons dynamicus est acus ad memoriam, non iam tabula localis in pila.
    # Omnes adiutores analysatoris eundem indicem accipere debent; aliter ORDO
    # argumentum sedem tabulae localis fingit et primus FUNCTIO iam frangitur.
    numerus_parametrorum_fontis = textus.count(PARAM_FONS_VETUS)
    if numerus_parametrorum_fontis == 0:
        raise SystemExit("ERRATUM: parametri fontis veteres non inventi sunt")
    textus = textus.replace(PARAM_FONS_VETUS, PARAM_FONS_NOVUS)

    initium_lect = "    DECLARA fd SICUT NUMERUS VALENS APERI_LEGERE(argv[1]).\n"
    finis_lect = "    DECLARA pos_out_imp SICUT NUMERUS VALENS 0.\n"
    lectio = '''    DECLARA fd SICUT NUMERUS VALENS APERI_LEGERE(argv[1]).
    SI fd < 0 TUNC
        PROCLAMA "ERRATUM: fons aperiri non potest".
        REDDE 66.
    FIN-SI.
    DECLARA n SICUT NUMERUS VALENS 0.
    DECLARA basis_fons_brut SICUT NUMERUS VALENS LEGE_TOTUM_DYNAMICUM(fd, SEDES(n)).
    CLAUDE(fd).
    SI n < 0 || basis_fons_brut < 0 TUNC
        PROCLAMA "ERRATUM: fons legi non potest".
        REDDE 74.
    FIN-SI.
    DECLARA fons_brut SICUT ACUS<LITTERA> VALENS basis_fons_brut.
    DECLARA capacitas_fons SICUT NUMERUS VALENS 65536.
    DECLARA basis_fons SICUT NUMERUS VALENS RESERVA_OCTETA(capacitas_fons).
    SI basis_fons < 0 TUNC
        PROCLAMA "ERRATUM: memoria fontium reservata non est".
        REDDE 71.
    FIN-SI.
'''
    textus = seca(textus, initium_lect, finis_lect, lectio, "lectio-principalis")

    initium_imp = "            DECLARA fd_imp2 SICUT NUMERUS VALENS APERI_LEGERE(nomen_base_imp).\n"
    finis_imp = "        ALITER\n            i_imp = i_imp + 1.\n"
    importatio = '''            DECLARA fd_imp2 SICUT NUMERUS VALENS APERI_LEGERE(nomen_base_imp).
            SI fd_imp2 >= 0 TUNC
                DECLARA n_imp2 SICUT NUMERUS VALENS 0.
                DECLARA basis_imp SICUT NUMERUS VALENS LEGE_TOTUM_DYNAMICUM(fd_imp2, SEDES(n_imp2)).
                CLAUDE(fd_imp2).
                SI n_imp2 < 0 || basis_imp < 0 TUNC
                    PROCLAMA "ERRATUM: fons importatus legi non potest".
                    REDDE 74.
                FIN-SI.
                DECLARA basis_crescens SICUT NUMERUS VALENS ASSECURA_BUFFERUM(basis_fons, pos_out_imp, pos_out_imp + n_imp2 + 1, SEDES(capacitas_fons)).
                SI basis_crescens < 0 TUNC
                    PROCLAMA "ERRATUM: memoria fontium augeri non potest".
                    REDDE 71.
                FIN-SI.
                basis_fons = basis_crescens.
                DECLARA m_imp SICUT NUMERUS VALENS 0.
                DUM m_imp < n_imp2 PERFICE
                    SCRIBE_OCTETUM_AB(basis_fons + pos_out_imp, OCTETUS_AB(basis_imp + m_imp)).
                    pos_out_imp = pos_out_imp + 1.
                    m_imp = m_imp + 1.
                FIN-DUM.
                SCRIBE_OCTETUM_AB(basis_fons + pos_out_imp, 10).
                pos_out_imp = pos_out_imp + 1.
            ALITER
                PROCLAMA "ERRATUM: fons importatus aperiri non potest".
                REDDE 66.
            FIN-SI.
'''
    textus = seca(textus, initium_imp, finis_imp, importatio, "lectio-importi")

    initium_fin = "    DECLARA m2_imp SICUT NUMERUS VALENS 0.\n"
    finis_fin = "    DECLARA codex SICUT ORDO DE NUMERUS CAPACITAS 300000.\n"
    fin = '''    DECLARA basis_finalis SICUT NUMERUS VALENS ASSECURA_BUFFERUM(basis_fons, pos_out_imp, pos_out_imp + n, SEDES(capacitas_fons)).
    SI basis_finalis < 0 TUNC
        PROCLAMA "ERRATUM: memoria fontis finalis augeri non potest".
        REDDE 71.
    FIN-SI.
    basis_fons = basis_finalis.
    DECLARA m2_imp SICUT NUMERUS VALENS 0.
    DUM m2_imp < n PERFICE
        SCRIBE_OCTETUM_AB(basis_fons + pos_out_imp, OCTETUS_AB(basis_fons_brut + m2_imp)).
        pos_out_imp = pos_out_imp + 1.
        m2_imp = m2_imp + 1.
    FIN-DUM.
    n = pos_out_imp.
    DECLARA fons SICUT ACUS<LITTERA> VALENS basis_fons.

'''
    textus = seca(textus, initium_fin, finis_fin, fin, "appendix-fontis")

    vetita = [
        "CAPACITAS 213000",
        "LEGE(fd, 213001)",
        "LEGE(fd_imp2, 213001)",
        "212999 octeti",
        PARAM_FONS_VETUS,
    ]
    relicta = [x for x in vetita if x in textus]
    if relicta:
        raise SystemExit("ERRATUM: limites fontium adhuc manent: " + ", ".join(relicta))

    VIA.write_text(textus, encoding="utf-8")
    print(
        "RECTE: fontes dynamici adiutoribus separatis crescunt; "
        f"{numerus_parametrorum_fontis} parametri fontis acus utuntur."
    )


if __name__ == "__main__":
    applica()
