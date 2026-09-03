#!/usr/bin/env python3
"""P11-C: canonizat FFI Win64 minimam VINDEX.

Patch temporarius rami laboris. Mutationes finales in compilatore et probationibus
manent; hoc instrumentum ante fusionem removendum est.
"""
from pathlib import Path
import re

RADIX = Path(__file__).resolve().parents[1]
COMP = RADIX / "Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex"
PE_TEST = RADIX / "Vindex Chat-GPT/vindex_final_v51/tests/proba_pe_structuram_053.vindex"

textus = COMP.read_text(encoding="utf-8")

if "FUNCTIO COMPONE_VOCA_MSX64_16" in textus and "WIN_DLL_SYMBOLUM" in textus:
    print("RECTE: FFI Win64 iam in compilatore adest.")
else:
    def muta(vetus: str, novus: str, titulus: str) -> None:
        global textus
        n = textus.count(vetus)
        if n != 1:
            raise SystemExit(f"ERRATUM: ancora {titulus} non unica est ({n})")
        textus = textus.replace(vetus, novus, 1)

    muta(
        "    DECLARA numerus_functionum_pe SICUT NUMERUS VALENS 8.\n",
        "    DECLARA numerus_functionum_pe SICUT NUMERUS VALENS 10.\n",
        "numerus functionum PE",
    )

    muta(
        "    DECLARA off_hint_gcl SICUT NUMERUS VALENS off_hint_ch + 14.\n"
        "    DECLARA off_nomen_dll SICUT NUMERUS VALENS off_hint_gcl + 18.\n",
        "    DECLARA off_hint_gcl SICUT NUMERUS VALENS off_hint_ch + 14.\n"
        "    DECLARA off_hint_ll SICUT NUMERUS VALENS off_hint_gcl + 18.\n"
        "    DECLARA off_hint_gpa SICUT NUMERUS VALENS off_hint_ll + 15.\n"
        "    DECLARA off_nomen_dll SICUT NUMERUS VALENS off_hint_gpa + 17.\n",
        "offseta LoadLibrary/GetProcAddress",
    )

    muta(
        "    DECLARA rva_hint_gcl SICUT NUMERUS VALENS rva_idata + off_hint_gcl.\n"
        "    DECLARA rva_nomen_dll SICUT NUMERUS VALENS rva_idata + off_nomen_dll.\n",
        "    DECLARA rva_hint_gcl SICUT NUMERUS VALENS rva_idata + off_hint_gcl.\n"
        "    DECLARA rva_hint_ll SICUT NUMERUS VALENS rva_idata + off_hint_ll.\n"
        "    DECLARA rva_hint_gpa SICUT NUMERUS VALENS rva_idata + off_hint_gpa.\n"
        "    DECLARA rva_nomen_dll SICUT NUMERUS VALENS rva_idata + off_nomen_dll.\n",
        "RVA LoadLibrary/GetProcAddress",
    )

    muta(
        "    DECLARA igp_gcl_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 56, rva_hint_gcl).\n"
        "    DECLARA igp15 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 64, 0).\n"
        "    DECLARA igp16 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat, rva_hint_ep).\n"
        "    DECLARA igp17 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 8, rva_hint_va).\n"
        "    DECLARA igp18 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 16, rva_hint_gsh).\n"
        "    DECLARA igp19 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 24, rva_hint_wf).\n"
        "    DECLARA igp_cf_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 32, rva_hint_cf).\n"
        "    DECLARA igp_rf_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 40, rva_hint_rf).\n"
        "    DECLARA igp_ch_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 48, rva_hint_ch).\n"
        "    DECLARA igp_gcl_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 56, rva_hint_gcl).\n"
        "    DECLARA igp20 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 64, 0).\n",
        "    DECLARA igp_gcl_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 56, rva_hint_gcl).\n"
        "    DECLARA igp_ll_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 64, rva_hint_ll).\n"
        "    DECLARA igp_gpa_ilt SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 72, rva_hint_gpa).\n"
        "    DECLARA igp15 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_ilt + 80, 0).\n"
        "    DECLARA igp16 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat, rva_hint_ep).\n"
        "    DECLARA igp17 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 8, rva_hint_va).\n"
        "    DECLARA igp18 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 16, rva_hint_gsh).\n"
        "    DECLARA igp19 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 24, rva_hint_wf).\n"
        "    DECLARA igp_cf_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 32, rva_hint_cf).\n"
        "    DECLARA igp_rf_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 40, rva_hint_rf).\n"
        "    DECLARA igp_ch_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 48, rva_hint_ch).\n"
        "    DECLARA igp_gcl_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 56, rva_hint_gcl).\n"
        "    DECLARA igp_ll_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 64, rva_hint_ll).\n"
        "    DECLARA igp_gpa_iat SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 72, rva_hint_gpa).\n"
        "    DECLARA igp20 SICUT NUMERUS VALENS SCRIBE_U64(codex, pos_idata + off_iat + 80, 0).\n",
        "ILT/IAT FFI",
    )

    ancora_nomina = (
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 16, 65).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 17, 0).\n\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_nomen_dll, 107).\n"
    )
    nomina_nova = (
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 16, 65).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gcl + 17, 0).\n\n"
        "    DECLARA igp_ll SICUT NUMERUS VALENS SCRIBE_U16(codex, pos_idata + off_hint_ll, 0).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 2, 76).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 3, 111).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 4, 97).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 5, 100).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 6, 76).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 7, 105).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 8, 98).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 9, 114).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 10, 97).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 11, 114).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 12, 121).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 13, 65).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_ll + 14, 0).\n\n"
        "    DECLARA igp_gpa SICUT NUMERUS VALENS SCRIBE_U16(codex, pos_idata + off_hint_gpa, 0).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 2, 71).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 3, 101).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 4, 116).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 5, 80).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 6, 114).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 7, 111).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 8, 99).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 9, 65).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 10, 100).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 11, 100).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 12, 114).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 13, 101).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 14, 115).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 15, 115).\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_hint_gpa + 16, 0).\n\n"
        "    CODEX_SCRIBE(codex, pos_idata + off_nomen_dll, 107).\n"
    )
    muta(ancora_nomina, nomina_nova, "nomina FFI PE")

    # Cadre Win64 commun pour vocationem per IAT, argumentis iam in RCX/RDX/R8/R9.
    pat_iat = re.compile(r"(FUNCTIO COMPONE_VOCA_IAT_DYNAMICA REDDENS NUMERUS\.\n.*?\nFIN-FUNCTIO\.\n)", re.S)
    m = pat_iat.search(textus)
    if not m:
        raise SystemExit("ERRATUM: COMPONE_VOCA_IAT_DYNAMICA non inventa")
    add_iat = r'''

FUNCTIO COMPONE_VOCA_IAT_MSX64 REDDENS NUMERUS.
    ACCIPIT codex SICUT NUMERUS.
    ACCIPIT indice SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT NUMERUS.
    ACCIPIT id_functionis SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.
    p = COMPONE_TRANSCRIBE(codex, p, 6, 4).
    CODEX_SCRIBE(codex, p, 72). CODEX_SCRIBE(codex, p + 1, 131). CODEX_SCRIBE(codex, p + 2, 228). CODEX_SCRIBE(codex, p + 3, 240). p = p + 4.
    CODEX_SCRIBE(codex, p, 72). CODEX_SCRIBE(codex, p + 1, 131). CODEX_SCRIBE(codex, p + 2, 236). CODEX_SCRIBE(codex, p + 3, 32). p = p + 4.
    p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, id_functionis).
    p = COMPONE_TRANSCRIBE(codex, p, 4, 6).
    REDDE p.
FIN-FUNCTIO.
'''
    textus = textus[:m.end()] + add_iat + textus[m.end():]

    # ABI Microsoft x64 generica: RAX = functio, R11 = tabula XVI argumentorum u64.
    pat_uefi = re.compile(r"(FUNCTIO COMPONE_VOCA_UEFI6 REDDENS NUMERUS\.\n.*?\nFIN-FUNCTIO\.\n)", re.S)
    m = pat_uefi.search(textus)
    if not m:
        raise SystemExit("ERRATUM: COMPONE_VOCA_UEFI6 non inventa")
    add_abi = r'''

// Vocatio ABI Microsoft x64 generalis usque ad XVI argumenta integer/pointer.
// RAX = punctator functionis; R11 = tabula XVI valorum u64 contiguorum.
// Argumenta I-IV -> RCX,RDX,R8,R9; V-XVI -> pila post shadow space XXXII.
FUNCTIO COMPONE_VOCA_MSX64_16 REDDENS NUMERUS.
    ACCIPIT codex SICUT NUMERUS.
    ACCIPIT indice SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.

    CODEX_SCRIBE(codex, p, 65). CODEX_SCRIBE(codex, p + 1, 84). p = p + 2.
    CODEX_SCRIBE(codex, p, 65). CODEX_SCRIBE(codex, p + 1, 85). p = p + 2.
    CODEX_SCRIBE(codex, p, 73). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 228). p = p + 3.
    CODEX_SCRIBE(codex, p, 77). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 221). p = p + 3.
    CODEX_SCRIBE(codex, p, 72). CODEX_SCRIBE(codex, p + 1, 131). CODEX_SCRIBE(codex, p + 2, 228). CODEX_SCRIBE(codex, p + 3, 240). p = p + 4.
    CODEX_SCRIBE(codex, p, 72). CODEX_SCRIBE(codex, p + 1, 129). CODEX_SCRIBE(codex, p + 2, 236). CODEX_SCRIBE(codex, p + 3, 128). CODEX_SCRIBE(codex, p + 4, 0). CODEX_SCRIBE(codex, p + 5, 0). CODEX_SCRIBE(codex, p + 6, 0). p = p + 7.

    CODEX_SCRIBE(codex, p, 73). CODEX_SCRIBE(codex, p + 1, 139). CODEX_SCRIBE(codex, p + 2, 77). CODEX_SCRIBE(codex, p + 3, 0). p = p + 4.
    CODEX_SCRIBE(codex, p, 73). CODEX_SCRIBE(codex, p + 1, 139). CODEX_SCRIBE(codex, p + 2, 85). CODEX_SCRIBE(codex, p + 3, 8). p = p + 4.
    CODEX_SCRIBE(codex, p, 77). CODEX_SCRIBE(codex, p + 1, 139). CODEX_SCRIBE(codex, p + 2, 69). CODEX_SCRIBE(codex, p + 3, 16). p = p + 4.
    CODEX_SCRIBE(codex, p, 77). CODEX_SCRIBE(codex, p + 1, 139). CODEX_SCRIBE(codex, p + 2, 77). CODEX_SCRIBE(codex, p + 3, 24). p = p + 4.

    DECLARA arg SICUT NUMERUS VALENS 4.
    DUM arg < 16 PERFICE
        DECLARA disp_fons SICUT NUMERUS VALENS arg * 8.
        DECLARA disp_dest SICUT NUMERUS VALENS 32 + (arg - 4) * 8.
        CODEX_SCRIBE(codex, p, 77). CODEX_SCRIBE(codex, p + 1, 139). CODEX_SCRIBE(codex, p + 2, 85). CODEX_SCRIBE(codex, p + 3, disp_fons). p = p + 4.
        CODEX_SCRIBE(codex, p, 76). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 84). CODEX_SCRIBE(codex, p + 3, 36). CODEX_SCRIBE(codex, p + 4, disp_dest). p = p + 5.
        arg = arg + 1.
    FIN-DUM.

    CODEX_SCRIBE(codex, p, 255). CODEX_SCRIBE(codex, p + 1, 208). p = p + 2.
    CODEX_SCRIBE(codex, p, 76). CODEX_SCRIBE(codex, p + 1, 137). CODEX_SCRIBE(codex, p + 2, 228). p = p + 3.
    CODEX_SCRIBE(codex, p, 65). CODEX_SCRIBE(codex, p + 1, 93). p = p + 2.
    CODEX_SCRIBE(codex, p, 65). CODEX_SCRIBE(codex, p + 1, 92). p = p + 2.
    REDDE p.
FIN-FUNCTIO.
'''
    textus = textus[:m.end()] + add_abi + textus[m.end():]

    def condicio(verbum: str) -> str:
        b = verbum.encode("ascii")
        partes = [f"fons[CONTENTUM(pos_fontis)] == {b[0]}"]
        for i, c in enumerate(b[1:], 1):
            partes.append(f"fons[CONTENTUM(pos_fontis)+{i}] == {c}")
        return " && ".join(partes)

    ramus = f'''    SI {condicio("ABI_MSX64_VOCA16(")} TUNC
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 17.
        DECLARA ig_msx64 SICUT NUMERUS VALENS ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
        ig_msx64 = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        ig_msx64 = IGNORA_SPATIA(fons, pos_fontis, n).
        ig_msx64 = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 11, 0).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 0).
        ig_msx64 = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        CONTENTUM(pos_codicis) = COMPONE_VOCA_MSX64_16(codex, CONTENTUM(pos_codicis)).
        REDDE 0.
    FIN-SI.

    SI {condicio("WIN_DLL_APERI(")} TUNC
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 14.
        DECLARA ig_dll SICUT NUMERUS VALENS ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        ig_dll = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 1, 0).
        CONTENTUM(pos_codicis) = COMPONE_VOCA_IAT_MSX64(codex, CONTENTUM(pos_codicis), contextus_parseris, 8).
        REDDE 0.
    FIN-SI.

    SI {condicio("WIN_DLL_SYMBOLUM(")} TUNC
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 17.
        DECLARA ig_sym SICUT NUMERUS VALENS ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
        ig_sym = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        ig_sym = IGNORA_SPATIA(fons, pos_fontis, n).
        ig_sym = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 0).
        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
        ig_sym = IGNORA_SPATIA(fons, pos_fontis, n).
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        CONTENTUM(pos_codicis) = COMPONE_VOCA_IAT_MSX64(codex, CONTENTUM(pos_codicis), contextus_parseris, 9).
        REDDE 0.
    FIN-SI.

'''
    ancora_parser = "    SI fons[CONTENTUM(pos_fontis)] == 85 && CONTENTUM(pos_fontis) + 10 < n && fons[CONTENTUM(pos_fontis)+1] == 69 && fons[CONTENTUM(pos_fontis)+2] == 70 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 95 && fons[CONTENTUM(pos_fontis)+5] == 86 && fons[CONTENTUM(pos_fontis)+6] == 79 && fons[CONTENTUM(pos_fontis)+7] == 67 && fons[CONTENTUM(pos_fontis)+8] == 65 && fons[CONTENTUM(pos_fontis)+9] == 54 && fons[CONTENTUM(pos_fontis)+10] == 40 TUNC\n"
    if textus.count(ancora_parser) != 1:
        raise SystemExit("ERRATUM: ancora UEFI_VOCA6 parser non unica")
    textus = textus.replace(ancora_parser, ramus + ancora_parser, 1)

    COMP.write_text(textus, encoding="utf-8")
    print("RECTE: compilator FFI Win64 patchatus est.")

# Verificator PE discit duas API novas KERNEL32.
pt = PE_TEST.read_text(encoding="utf-8")
if "LoadLibraryA" not in pt:
    ancora = "    SI id == 7 TUNC\n        SI pos + 15 > n TUNC REDDE 0. FIN-SI.\n        REDDE OCTETUS_AB(memoria+pos)==71 && OCTETUS_AB(memoria+pos+1)==101 && OCTETUS_AB(memoria+pos+2)==116 && OCTETUS_AB(memoria+pos+3)==67 && OCTETUS_AB(memoria+pos+4)==111 && OCTETUS_AB(memoria+pos+5)==109 && OCTETUS_AB(memoria+pos+6)==109 && OCTETUS_AB(memoria+pos+7)==97 && OCTETUS_AB(memoria+pos+8)==110 && OCTETUS_AB(memoria+pos+9)==100 && OCTETUS_AB(memoria+pos+10)==76 && OCTETUS_AB(memoria+pos+11)==105 && OCTETUS_AB(memoria+pos+12)==110 && OCTETUS_AB(memoria+pos+13)==101 && OCTETUS_AB(memoria+pos+14)==65.\n    FIN-SI.\n"
    if pt.count(ancora) != 1:
        raise SystemExit("ERRATUM: API 7 in verificatore PE non unica")
    nova = ancora + '''    // LoadLibraryA
    SI id == 8 TUNC
        SI pos + 12 > n TUNC REDDE 0. FIN-SI.
        REDDE OCTETUS_AB(memoria+pos)==76 && OCTETUS_AB(memoria+pos+1)==111 && OCTETUS_AB(memoria+pos+2)==97 && OCTETUS_AB(memoria+pos+3)==100 && OCTETUS_AB(memoria+pos+4)==76 && OCTETUS_AB(memoria+pos+5)==105 && OCTETUS_AB(memoria+pos+6)==98 && OCTETUS_AB(memoria+pos+7)==114 && OCTETUS_AB(memoria+pos+8)==97 && OCTETUS_AB(memoria+pos+9)==114 && OCTETUS_AB(memoria+pos+10)==121 && OCTETUS_AB(memoria+pos+11)==65.
    FIN-SI.
    // GetProcAddress
    SI id == 9 TUNC
        SI pos + 14 > n TUNC REDDE 0. FIN-SI.
        REDDE OCTETUS_AB(memoria+pos)==71 && OCTETUS_AB(memoria+pos+1)==101 && OCTETUS_AB(memoria+pos+2)==116 && OCTETUS_AB(memoria+pos+3)==80 && OCTETUS_AB(memoria+pos+4)==114 && OCTETUS_AB(memoria+pos+5)==111 && OCTETUS_AB(memoria+pos+6)==99 && OCTETUS_AB(memoria+pos+7)==65 && OCTETUS_AB(memoria+pos+8)==100 && OCTETUS_AB(memoria+pos+9)==100 && OCTETUS_AB(memoria+pos+10)==114 && OCTETUS_AB(memoria+pos+11)==101 && OCTETUS_AB(memoria+pos+12)==115 && OCTETUS_AB(memoria+pos+13)==115.
    FIN-SI.
'''
    pt = pt.replace(ancora, nova, 1)
    if pt.count("DUM i < 8 PERFICE") != 1:
        raise SystemExit("ERRATUM: numerus API verificatoris PE non inventus")
    pt = pt.replace("DUM i < 8 PERFICE", "DUM i < 10 PERFICE", 1)
    PE_TEST.write_text(pt, encoding="utf-8")
    print("RECTE: verificator PE ad X API KERNEL32 extensum est.")
else:
    print("RECTE: verificator PE FFI iam renovatus est.")
