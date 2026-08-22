#!/usr/bin/env python3
"""VINDEX 0.53: recognitionem typorum sine falsis praefixis corrigit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")


def exige_unum(textus: str, vetus: str, nomen: str) -> str:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")
    return textus


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")

    vetus_fluitans = '''                        SI fons[CONTENTUM(pos_fontis)] == 70 TUNC
                            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 9.'''
    novum_fluitans = '''                        SI fons[CONTENTUM(pos_fontis)] == 70 && CONTENTUM(pos_fontis) + 7 < n && fons[CONTENTUM(pos_fontis)+1] == 76 && fons[CONTENTUM(pos_fontis)+2] == 85 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 84 && fons[CONTENTUM(pos_fontis)+5] == 65 && fons[CONTENTUM(pos_fontis)+6] == 78 && fons[CONTENTUM(pos_fontis)+7] == 83 && (CONTENTUM(pos_fontis)+8 >= n || fons[CONTENTUM(pos_fontis)+8] == 32 || fons[CONTENTUM(pos_fontis)+8] == 46 || fons[CONTENTUM(pos_fontis)+8] == 10 || fons[CONTENTUM(pos_fontis)+8] == 9) TUNC
                            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 9.'''
    exige_unum(textus, vetus_fluitans, "declaratio-fluitans")
    textus = textus.replace(vetus_fluitans, novum_fluitans, 1)

    vetus_simples = '''                            SI fons[CONTENTUM(pos_fontis)] == 78 || fons[CONTENTUM(pos_fontis)] == 65 || fons[CONTENTUM(pos_fontis)] == 86 || fons[CONTENTUM(pos_fontis)] == 84 TUNC'''
    novum_simples = '''                            SI (fons[CONTENTUM(pos_fontis)] == 78 && CONTENTUM(pos_fontis) + 6 < n && fons[CONTENTUM(pos_fontis)+1] == 85 && fons[CONTENTUM(pos_fontis)+2] == 77 && fons[CONTENTUM(pos_fontis)+3] == 69 && fons[CONTENTUM(pos_fontis)+4] == 82 && fons[CONTENTUM(pos_fontis)+5] == 85 && fons[CONTENTUM(pos_fontis)+6] == 83) || (fons[CONTENTUM(pos_fontis)] == 65 && CONTENTUM(pos_fontis) + 4 < n && fons[CONTENTUM(pos_fontis)+1] == 67 && fons[CONTENTUM(pos_fontis)+2] == 85 && fons[CONTENTUM(pos_fontis)+3] == 83 && fons[CONTENTUM(pos_fontis)+4] == 60) || (fons[CONTENTUM(pos_fontis)] == 86 && CONTENTUM(pos_fontis) + 6 < n && fons[CONTENTUM(pos_fontis)+1] == 69 && fons[CONTENTUM(pos_fontis)+2] == 82 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 84 && fons[CONTENTUM(pos_fontis)+5] == 65 && fons[CONTENTUM(pos_fontis)+6] == 83) || (fons[CONTENTUM(pos_fontis)] == 84 && CONTENTUM(pos_fontis) + 5 < n && fons[CONTENTUM(pos_fontis)+1] == 69 && fons[CONTENTUM(pos_fontis)+2] == 88 && fons[CONTENTUM(pos_fontis)+3] == 84 && fons[CONTENTUM(pos_fontis)+4] == 85 && fons[CONTENTUM(pos_fontis)+5] == 83) TUNC'''
    exige_unum(textus, vetus_simples, "declaratio-typorum-simplicium")
    textus = textus.replace(vetus_simples, novum_simples, 1)

    vetus_ordo_fluitans = '''                            SI fons[CONTENTUM(pos_fontis)] == 70 TUNC
                                es_arr_fluitans = 1.
                            FIN-SI.'''
    novum_ordo_fluitans = '''                            SI fons[CONTENTUM(pos_fontis)] == 70 && CONTENTUM(pos_fontis) + 7 < n && fons[CONTENTUM(pos_fontis)+1] == 76 && fons[CONTENTUM(pos_fontis)+2] == 85 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 84 && fons[CONTENTUM(pos_fontis)+5] == 65 && fons[CONTENTUM(pos_fontis)+6] == 78 && fons[CONTENTUM(pos_fontis)+7] == 83 TUNC
                                es_arr_fluitans = 1.
                            FIN-SI.'''
    exige_unum(textus, vetus_ordo_fluitans, "ordo-fluitans")
    textus = textus.replace(vetus_ordo_fluitans, novum_ordo_fluitans, 1)

    vetus_param_fluitans = '''                        SI fons[i] == 70 TUNC
                            es_flot_param = 1.
                        FIN-SI.'''
    novum_param_fluitans = '''                        SI fons[i] == 70 && i + 7 < n && fons[i+1] == 76 && fons[i+2] == 85 && fons[i+3] == 73 && fons[i+4] == 84 && fons[i+5] == 65 && fons[i+6] == 78 && fons[i+7] == 83 TUNC
                            es_flot_param = 1.
                        FIN-SI.'''
    exige_unum(textus, vetus_param_fluitans, "parametrum-fluitans")
    textus = textus.replace(vetus_param_fluitans, novum_param_fluitans, 1)

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: typi plene agnoscuntur; praefixa F/N/A/V/T formas non corrumpunt.")


if __name__ == "__main__":
    applica()
