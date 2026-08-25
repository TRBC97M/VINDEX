#!/usr/bin/env python3
"""Migrationem mechanicam ad runtime Sylviae VINDEX purum applicat."""
from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
COMPILATOR = RADIX / "Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex"
NUCLEUS = RADIX / "Vindex Chat-GPT/vindex_final_v51/systema/nucleus.vindex"


def substitue_unum(textus: str, vetus: str, novus: str, nomen: str) -> str:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: {nomen}: expectabatur 1 inventum, inventa sunt {numerus}")
    return textus.replace(vetus, novus, 1)


# --- Compilator: POLLE residentem removet et vocationem UEFI indirectam nativam addit. ---
comp = COMPILATOR.read_text(encoding="utf-8")

ancora = '''FUNCTIO COMPONE_VOCA_NUCLEUM REDDENS NUMERUS.\n    ACCIPIT codex SICUT ORDO DE NUMERUS.\n    ACCIPIT indice SICUT NUMERUS.\n    codex[indice] = 15.\n    codex[indice + 1] = 5.\n    REDDE indice + 2.\nFIN-FUNCTIO.\n'''

adiunctum = ancora + '''\n// Vocat functionem UEFI per ABI Microsoft x64.\n// RAX = functio; RCX,RDX,R8,R9 = argumenta I-IV; R10,R11 = argumenta V-VI.\n// R12 servat pilam originalem quia callee-saved est in ABI UEFI.\nFUNCTIO COMPONE_VOCA_UEFI6 REDDENS NUMERUS.\n    ACCIPIT codex SICUT ORDO DE NUMERUS.\n    ACCIPIT indice SICUT NUMERUS.\n    DECLARA p SICUT NUMERUS VALENS indice.\n\n    // push r12\n    codex[p] = 65. codex[p + 1] = 84. p = p + 2.\n    // mov r12, rsp\n    codex[p] = 73. codex[p + 1] = 137. codex[p + 2] = 228. p = p + 3.\n    // and rsp, -16\n    codex[p] = 72. codex[p + 1] = 131. codex[p + 2] = 228. codex[p + 3] = 240. p = p + 4.\n    // sub rsp, 48 : 32 octeti shadow space + duo argumenta in pila\n    codex[p] = 72. codex[p + 1] = 131. codex[p + 2] = 236. codex[p + 3] = 48. p = p + 4.\n    // mov [rsp+32], r10\n    codex[p] = 76. codex[p + 1] = 137. codex[p + 2] = 84. codex[p + 3] = 36. codex[p + 4] = 32. p = p + 5.\n    // mov [rsp+40], r11\n    codex[p] = 76. codex[p + 1] = 137. codex[p + 2] = 92. codex[p + 3] = 36. codex[p + 4] = 40. p = p + 5.\n    // call rax\n    codex[p] = 255. codex[p + 1] = 208. p = p + 2.\n    // mov rsp, r12\n    codex[p] = 76. codex[p + 1] = 137. codex[p + 2] = 228. p = p + 3.\n    // pop r12\n    codex[p] = 65. codex[p + 1] = 92. p = p + 2.\n    REDDE p.\nFIN-FUNCTIO.\n'''
comp = substitue_unum(comp, ancora, adiunctum, "ancora COMPONE_VOCA_NUCLEUM")

polle = '''    SI fons[CONTENTUM(pos_fontis)] == 80 && CONTENTUM(pos_fontis) + 4 < n && fons[CONTENTUM(pos_fontis)+1] == 79 && fons[CONTENTUM(pos_fontis)+2] == 76 && fons[CONTENTUM(pos_fontis)+3] == 76 && fons[CONTENTUM(pos_fontis)+4] == 69 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 5.\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 50333704).\n        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 0).\n        codex[CONTENTUM(pos_codicis)] = 255.\n        codex[CONTENTUM(pos_codicis) + 1] = 208.\n        CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 2.\n        REDDE 0.\n    FIN-SI.\n'''

uefi = '''    SI fons[CONTENTUM(pos_fontis)] == 85 && CONTENTUM(pos_fontis) + 10 < n && fons[CONTENTUM(pos_fontis)+1] == 69 && fons[CONTENTUM(pos_fontis)+2] == 70 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 95 && fons[CONTENTUM(pos_fontis)+5] == 86 && fons[CONTENTUM(pos_fontis)+6] == 79 && fons[CONTENTUM(pos_fontis)+7] == 67 && fons[CONTENTUM(pos_fontis)+8] == 65 && fons[CONTENTUM(pos_fontis)+9] == 54 && fons[CONTENTUM(pos_fontis)+10] == 40 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 11.\n        DECLARA ig_uefi SICUT NUMERUS VALENS 0.\n\n        // functio + sex argumenta; omnia primum in pila servantur.\n        ig_uefi = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).\n        DECLARA arg_uefi SICUT NUMERUS VALENS 0.\n        DUM arg_uefi < 6 PERFICE\n            ig_uefi = IGNORA_SPATIA(fons, pos_fontis, n).\n            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n            ig_uefi = IGNORA_SPATIA(fons, pos_fontis, n).\n            ig_uefi = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).\n            arg_uefi = arg_uefi + 1.\n        FIN-DUM.\n        ig_uefi = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n\n        // Ordo inversus e pila: VI->r11, V->r10, IV->r9, III->r8, II->rdx, I->rcx, functio->rax.\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 11).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 9).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 8).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).\n        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 0).\n        CONTENTUM(pos_codicis) = COMPONE_VOCA_UEFI6(codex, CONTENTUM(pos_codicis)).\n        REDDE 0.\n    FIN-SI.\n'''
comp = substitue_unum(comp, polle, uefi, "intrinsecum POLLE")
COMPILATOR.write_text(comp, encoding="utf-8")


# --- Nucleus: runtime C callback removetur; input et volumen firmware a VINDEX vocantur. ---
nuc = NUCLEUS.read_text(encoding="utf-8")

uefi_runtime = r'''// --- UEFI runtime VINDEX purum -------------------------------------------------
// META + 8 continet EFI_SYSTEM_TABLE*; META + 56 EFI image handle.
// Nulla functio C post ingressum nuclei revocatur.

FUNCTIO UEFI_I32 REDDENS NUMERUS.
    ACCIPIT locus SICUT NUMERUS.
    DECLARA valor SICUT NUMERUS VALENS OCTETUS_AB(locus) | (OCTETUS_AB(locus + 1) << 8) | (OCTETUS_AB(locus + 2) << 16) | (OCTETUS_AB(locus + 3) << 24).
    SI valor >= 2147483648 TUNC valor = valor - 4294967296. FIN-SI.
    REDDE valor.
FIN-FUNCTIO.

FUNCTIO UEFI_CLAVIS_IMPONE REDDENS NUMERUS.
    ACCIPIT clavis SICUT NUMERUS.
    DECLARA caput SICUT NUMERUS VALENS CONTENTUM(50331712).
    SCRIBE_OCTETUM_AB(50332416 + (caput & 63), clavis).
    CONTENTUM(50331712) = caput + 1.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_LITTERA_CLAVIS REDDENS NUMERUS.
    ACCIPIT c SICUT NUMERUS.
    SI c == 97 TUNC REDDE 16. FIN-SI. SI c == 122 TUNC REDDE 17. FIN-SI.
    SI c == 101 TUNC REDDE 18. FIN-SI. SI c == 114 TUNC REDDE 19. FIN-SI.
    SI c == 116 TUNC REDDE 20. FIN-SI. SI c == 121 TUNC REDDE 21. FIN-SI.
    SI c == 117 TUNC REDDE 22. FIN-SI. SI c == 105 TUNC REDDE 23. FIN-SI.
    SI c == 111 TUNC REDDE 24. FIN-SI. SI c == 112 TUNC REDDE 25. FIN-SI.
    SI c == 113 TUNC REDDE 30. FIN-SI. SI c == 115 TUNC REDDE 31. FIN-SI.
    SI c == 100 TUNC REDDE 32. FIN-SI. SI c == 102 TUNC REDDE 33. FIN-SI.
    SI c == 103 TUNC REDDE 34. FIN-SI. SI c == 104 TUNC REDDE 35. FIN-SI.
    SI c == 106 TUNC REDDE 36. FIN-SI. SI c == 107 TUNC REDDE 37. FIN-SI.
    SI c == 108 TUNC REDDE 38. FIN-SI. SI c == 109 TUNC REDDE 39. FIN-SI.
    SI c == 119 TUNC REDDE 44. FIN-SI. SI c == 120 TUNC REDDE 45. FIN-SI.
    SI c == 99 TUNC REDDE 46. FIN-SI. SI c == 118 TUNC REDDE 47. FIN-SI.
    SI c == 98 TUNC REDDE 48. FIN-SI. SI c == 110 TUNC REDDE 49. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_UNICODE_INPONE REDDENS NUMERUS.
    ACCIPIT c SICUT NUMERUS.
    DECLARA maius SICUT NUMERUS VALENS 0.
    SI c >= 65 && c <= 90 TUNC maius = 1. c = c + 32. FIN-SI.
    DECLARA clavis SICUT NUMERUS VALENS UEFI_LITTERA_CLAVIS(c).
    SI clavis != 0 TUNC
        SI maius == 1 TUNC DECLARA a SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(42). FIN-SI.
        DECLARA b SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(clavis).
        SI maius == 1 TUNC DECLARA d SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(170). FIN-SI.
        REDDE 1.
    FIN-SI.
    SI c >= 49 && c <= 57 TUNC clavis = 2 + c - 49. FIN-SI.
    SI c == 48 TUNC clavis = 11. FIN-SI.
    SI c == 32 TUNC clavis = 57. FIN-SI.
    SI c == 8 TUNC clavis = 14. FIN-SI.
    SI c == 13 || c == 10 TUNC clavis = 28. FIN-SI.
    SI c == 44 TUNC clavis = 50. FIN-SI.
    SI c == 59 TUNC clavis = 51. FIN-SI.
    SI c == 58 TUNC clavis = 52. FIN-SI.
    SI c == 33 TUNC clavis = 53. FIN-SI.
    SI clavis != 0 TUNC DECLARA e SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(clavis). REDDE 1. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_CLAVES_POLLE REDDENS NUMERUS.
    DECLARA systema SICUT NUMERUS VALENS CONTENTUM(50333704).
    SI systema == 0 TUNC REDDE 0. FIN-SI.
    DECLARA conin SICUT NUMERUS VALENS CONTENTUM(systema + 48).
    SI conin == 0 TUNC REDDE 0. FIN-SI.
    DECLARA lege SICUT NUMERUS VALENS CONTENTUM(conin + 8).
    SI lege == 0 TUNC REDDE 0. FIN-SI.
    DECLARA data_clavis SICUT NUMERUS VALENS 0.
    DECLARA numerus SICUT NUMERUS VALENS 0.
    DECLARA status SICUT NUMERUS VALENS 0.
    DUM numerus < 8 PERFICE
        data_clavis = 0.
        status = UEFI_VOCA6(lege, conin, SEDES(data_clavis), 0, 0, 0, 0).
        SI status != 0 TUNC REDDE numerus. FIN-SI.
        DECLARA scan SICUT NUMERUS VALENS OCTETUS_AB(SEDES(data_clavis)) | (OCTETUS_AB(SEDES(data_clavis) + 1) << 8).
        DECLARA unicode SICUT NUMERUS VALENS OCTETUS_AB(SEDES(data_clavis) + 2) | (OCTETUS_AB(SEDES(data_clavis) + 3) << 8).
        SI unicode != 0 TUNC DECLARA u SICUT NUMERUS VALENS UEFI_UNICODE_INPONE(unicode). FIN-SI.
        SI scan == 1 TUNC DECLARA s1 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(72). FIN-SI.
        SI scan == 2 TUNC DECLARA s2 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(80). FIN-SI.
        SI scan == 3 TUNC DECLARA s3 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(77). FIN-SI.
        SI scan == 4 TUNC DECLARA s4 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(75). FIN-SI.
        SI scan == 9 TUNC DECLARA s9 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(73). FIN-SI.
        SI scan == 10 TUNC DECLARA s10 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(81). FIN-SI.
        SI scan == 23 TUNC DECLARA s23 SICUT NUMERUS VALENS UEFI_CLAVIS_IMPONE(1). FIN-SI.
        numerus = numerus + 1.
    FIN-DUM.
    REDDE numerus.
FIN-FUNCTIO.

FUNCTIO UEFI_MURIS_PUBLICA REDDENS NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    ACCIPIT y SICUT NUMERUS.
    ACCIPIT bullae SICUT NUMERUS.
    SI x < 0 TUNC x = 0. FIN-SI. SI x > 306 TUNC x = 306. FIN-SI.
    SI y < 0 TUNC y = 0. FIN-SI. SI y > 186 TUNC y = 186. FIN-SI.
    SI CONTENTUM(50331648) != x || CONTENTUM(50331656) != y || CONTENTUM(50331664) != bullae TUNC
        CONTENTUM(50331648) = x.
        CONTENTUM(50331656) = y.
        CONTENTUM(50331664) = bullae.
        CONTENTUM(50331672) = CONTENTUM(50331672) + 1.
        REDDE 1.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_MURIS_ABS_POLLE REDDENS NUMERUS.
    DECLARA murus SICUT NUMERUS VALENS CONTENTUM(50333800).
    SI murus == 0 TUNC REDDE 0. FIN-SI.
    DECLARA lege SICUT NUMERUS VALENS CONTENTUM(murus + 8).
    DECLARA modus SICUT NUMERUS VALENS CONTENTUM(murus + 24).
    SI lege == 0 || modus == 0 TUNC REDDE 0. FIN-SI.
    DECLARA status_muris SICUT ORDO DE NUMERUS CAPACITAS 4.
    DECLARA status SICUT NUMERUS VALENS UEFI_VOCA6(lege, murus, SEDES(status_muris), 0, 0, 0, 0).
    SI status != 0 TUNC REDDE 0. FIN-SI.
    DECLARA minx SICUT NUMERUS VALENS CONTENTUM(modus).
    DECLARA miny SICUT NUMERUS VALENS CONTENTUM(modus + 8).
    DECLARA maxx SICUT NUMERUS VALENS CONTENTUM(modus + 24).
    DECLARA maxy SICUT NUMERUS VALENS CONTENTUM(modus + 32).
    DECLARA dx SICUT NUMERUS VALENS maxx - minx.
    DECLARA dy SICUT NUMERUS VALENS maxy - miny.
    SI dx <= 0 || dy <= 0 TUNC REDDE 0. FIN-SI.
    DECLARA x SICUT NUMERUS VALENS (status_muris[0] - minx) * 306 / dx.
    DECLARA y SICUT NUMERUS VALENS (status_muris[1] - miny) * 186 / dy.
    DECLARA bullae SICUT NUMERUS VALENS status_muris[3] & 3.
    REDDE UEFI_MURIS_PUBLICA(x, y, bullae).
FIN-FUNCTIO.

FUNCTIO UEFI_MURIS_REL_POLLE REDDENS NUMERUS.
    DECLARA murus SICUT NUMERUS VALENS CONTENTUM(50333792).
    SI murus == 0 TUNC REDDE 0. FIN-SI.
    DECLARA lege SICUT NUMERUS VALENS CONTENTUM(murus + 8).
    DECLARA modus SICUT NUMERUS VALENS CONTENTUM(murus + 24).
    SI lege == 0 TUNC REDDE 0. FIN-SI.
    DECLARA status_muris SICUT ORDO DE NUMERUS CAPACITAS 2.
    DECLARA status SICUT NUMERUS VALENS UEFI_VOCA6(lege, murus, SEDES(status_muris), 0, 0, 0, 0).
    SI status != 0 TUNC REDDE 0. FIN-SI.
    DECLARA mx SICUT NUMERUS VALENS UEFI_I32(SEDES(status_muris)).
    DECLARA my SICUT NUMERUS VALENS UEFI_I32(SEDES(status_muris) + 4).
    DECLARA rx SICUT NUMERUS VALENS 0.
    DECLARA ry SICUT NUMERUS VALENS 0.
    SI modus != 0 TUNC rx = CONTENTUM(modus). ry = CONTENTUM(modus + 8). FIN-SI.
    SI rx > 0 TUNC mx = mx * 6 / rx. FIN-SI. SI ry > 0 TUNC my = my * 6 / ry. FIN-SI.
    SI mx == 0 && UEFI_I32(SEDES(status_muris)) != 0 TUNC SI UEFI_I32(SEDES(status_muris)) < 0 TUNC mx = 0 - 1. ALITER mx = 1. FIN-SI. FIN-SI.
    SI my == 0 && UEFI_I32(SEDES(status_muris) + 4) != 0 TUNC SI UEFI_I32(SEDES(status_muris) + 4) < 0 TUNC my = 0 - 1. ALITER my = 1. FIN-SI. FIN-SI.
    DECLARA bullae SICUT NUMERUS VALENS 0.
    SI OCTETUS_AB(SEDES(status_muris) + 12) != 0 TUNC bullae = bullae | 1. FIN-SI.
    SI OCTETUS_AB(SEDES(status_muris) + 13) != 0 TUNC bullae = bullae | 2. FIN-SI.
    REDDE UEFI_MURIS_PUBLICA(CONTENTUM(50331648) + mx, CONTENTUM(50331656) + my, bullae).
FIN-FUNCTIO.

FUNCTIO UEFI_GUID_PONE REDDENS NUMERUS.
    ACCIPIT guid SICUT ACUS<LITTERA>.
    ACCIPIT genus SICUT NUMERUS.
    DECLARA i SICUT NUMERUS VALENS 0.
    DUM i < 16 PERFICE guid[i] = 0. i = i + 1. FIN-DUM.
    SI genus == 1 TUNC
        guid[0]=135. guid[1]=140. guid[2]=135. guid[3]=49. guid[4]=117. guid[5]=11. guid[6]=213. guid[7]=17.
        guid[8]=154. guid[9]=79. guid[10]=0. guid[11]=144. guid[12]=39. guid[13]=63. guid[14]=193. guid[15]=77.
    FIN-SI.
    SI genus == 2 TUNC
        guid[0]=43. guid[1]=211. guid[2]=89. guid[3]=141. guid[4]=85. guid[5]=198. guid[6]=233. guid[7]=74.
        guid[8]=155. guid[9]=21. guid[10]=242. guid[11]=89. guid[12]=4. guid[13]=153. guid[14]=42. guid[15]=67.
    FIN-SI.
    SI genus == 3 TUNC
        guid[0]=161. guid[1]=49. guid[2]=27. guid[3]=91. guid[4]=98. guid[5]=149. guid[6]=210. guid[7]=17.
        guid[8]=142. guid[9]=63. guid[10]=0. guid[11]=160. guid[12]=201. guid[13]=105. guid[14]=114. guid[15]=59.
    FIN-SI.
    SI genus == 4 TUNC
        guid[0]=34. guid[1]=91. guid[2]=78. guid[3]=150. guid[4]=89. guid[5]=100. guid[6]=210. guid[7]=17.
        guid[8]=142. guid[9]=57. guid[10]=0. guid[11]=160. guid[12]=201. guid[13]=105. guid[14]=114. guid[15]=59.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_VOLUMEN_APERI REDDENS NUMERUS.
    DECLARA systema SICUT NUMERUS VALENS CONTENTUM(50333704).
    DECLARA imago SICUT NUMERUS VALENS CONTENTUM(50333752).
    SI systema == 0 || imago == 0 TUNC REDDE 0. FIN-SI.
    DECLARA boot SICUT NUMERUS VALENS CONTENTUM(systema + 96).
    SI boot == 0 TUNC REDDE 0. FIN-SI.
    DECLARA handle SICUT NUMERUS VALENS CONTENTUM(boot + 152).
    SI handle == 0 TUNC REDDE 0. FIN-SI.
    DECLARA guid SICUT ORDO DE LITTERA CAPACITAS 16.
    DECLARA factum SICUT NUMERUS VALENS UEFI_GUID_PONE(guid, 3).
    DECLARA onusta SICUT NUMERUS VALENS 0.
    DECLARA status SICUT NUMERUS VALENS UEFI_VOCA6(handle, imago, SEDES(guid), SEDES(onusta), 0, 0, 0).
    SI status != 0 || onusta == 0 TUNC REDDE 0. FIN-SI.
    DECLARA fabrica SICUT NUMERUS VALENS CONTENTUM(onusta + 24).
    factum = UEFI_GUID_PONE(guid, 4).
    DECLARA fs SICUT NUMERUS VALENS 0.
    status = UEFI_VOCA6(handle, fabrica, SEDES(guid), SEDES(fs), 0, 0, 0).
    SI status != 0 || fs == 0 TUNC REDDE 0. FIN-SI.
    DECLARA radix SICUT NUMERUS VALENS 0.
    DECLARA aperi_volumen SICUT NUMERUS VALENS CONTENTUM(fs + 8).
    status = UEFI_VOCA6(aperi_volumen, fs, SEDES(radix), 0, 0, 0, 0).
    SI status != 0 || radix == 0 TUNC REDDE 0. FIN-SI.
    DECLARA nomen SICUT ORDO DE LITTERA CAPACITAS 20.
    DECLARA k SICUT NUMERUS VALENS 0. DUM k < 20 PERFICE nomen[k]=0. k=k+1. FIN-DUM.
    nomen[0]=86. nomen[2]=73. nomen[4]=78. nomen[6]=68. nomen[8]=69. nomen[10]=88. nomen[12]=46. nomen[14]=70. nomen[16]=83.
    DECLARA fasciculus SICUT NUMERUS VALENS 0.
    DECLARA aperi SICUT NUMERUS VALENS CONTENTUM(radix + 8).
    DECLARA crea SICUT NUMERUS VALENS (4611686018427387904 << 1) | 3.
    status = UEFI_VOCA6(aperi, radix, SEDES(fasciculus), SEDES(nomen), crea, 0, 0).
    SI status == 0 && fasciculus != 0 TUNC
        CONTENTUM(50333760) = fasciculus. CONTENTUM(50333768) = 1.
    ALITER
        fasciculus = 0.
        status = UEFI_VOCA6(aperi, radix, SEDES(fasciculus), SEDES(nomen), 1, 0, 0).
        SI status == 0 && fasciculus != 0 TUNC CONTENTUM(50333760)=fasciculus. CONTENTUM(50333768)=0. FIN-SI.
    FIN-SI.
    DECLARA claude_radix SICUT NUMERUS VALENS CONTENTUM(radix + 16).
    SI claude_radix != 0 TUNC DECLARA cr SICUT NUMERUS VALENS UEFI_VOCA6(claude_radix, radix, 0, 0, 0, 0, 0). FIN-SI.
    SI CONTENTUM(50333760) != 0 TUNC REDDE 1. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_VOLUMEN_RELEGE REDDENS NUMERUS.
    DECLARA fasciculus SICUT NUMERUS VALENS CONTENTUM(50333760).
    SI fasciculus == 0 TUNC REDDE 0. FIN-SI.
    DECLARA pone SICUT NUMERUS VALENS CONTENTUM(fasciculus + 56).
    DECLARA lege SICUT NUMERUS VALENS CONTENTUM(fasciculus + 32).
    SI pone == 0 || lege == 0 TUNC REDDE 0. FIN-SI.
    DECLARA status SICUT NUMERUS VALENS UEFI_VOCA6(pone, fasciculus, 0, 0, 0, 0, 0).
    SI status != 0 TUNC REDDE 0. FIN-SI.
    DECLARA mensura SICUT NUMERUS VALENS 32768.
    status = UEFI_VOCA6(lege, fasciculus, SEDES(mensura), 50401280, 0, 0, 0).
    SI status == 0 TUNC REDDE 1. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_VOLUMEN_SERVA REDDENS NUMERUS.
    DECLARA fasciculus SICUT NUMERUS VALENS CONTENTUM(50333760).
    SI fasciculus == 0 || CONTENTUM(50333768) == 0 TUNC REDDE 0. FIN-SI.
    DECLARA pone SICUT NUMERUS VALENS CONTENTUM(fasciculus + 56).
    DECLARA scribe SICUT NUMERUS VALENS CONTENTUM(fasciculus + 40).
    DECLARA flush SICUT NUMERUS VALENS CONTENTUM(fasciculus + 80).
    SI pone == 0 || scribe == 0 TUNC REDDE 0. FIN-SI.
    DECLARA status SICUT NUMERUS VALENS UEFI_VOCA6(pone, fasciculus, 0, 0, 0, 0, 0).
    SI status != 0 TUNC REDDE 0. FIN-SI.
    DECLARA mensura SICUT NUMERUS VALENS 32768.
    status = UEFI_VOCA6(scribe, fasciculus, SEDES(mensura), 50401280, 0, 0, 0).
    SI status != 0 || mensura != 32768 TUNC REDDE 0. FIN-SI.
    SI flush != 0 TUNC status = UEFI_VOCA6(flush, fasciculus, 0, 0, 0, 0, 0). FIN-SI.
    SI status == 0 TUNC REDDE 1. FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO UEFI_PARA REDDENS NUMERUS.
    DECLARA systema SICUT NUMERUS VALENS CONTENTUM(50333704).
    SI systema == 0 TUNC REDDE 0. FIN-SI.
    DECLARA boot SICUT NUMERUS VALENS CONTENTUM(systema + 96).
    SI boot == 0 TUNC REDDE 0. FIN-SI.
    DECLARA locate SICUT NUMERUS VALENS CONTENTUM(boot + 320).
    SI locate != 0 TUNC
        DECLARA guid SICUT ORDO DE LITTERA CAPACITAS 16.
        DECLARA rel SICUT NUMERUS VALENS 0.
        DECLARA abs SICUT NUMERUS VALENS 0.
        DECLARA f SICUT NUMERUS VALENS UEFI_GUID_PONE(guid, 1).
        DECLARA s SICUT NUMERUS VALENS UEFI_VOCA6(locate, SEDES(guid), 0, SEDES(rel), 0, 0, 0).
        SI s == 0 TUNC CONTENTUM(50333792) = rel. FIN-SI.
        f = UEFI_GUID_PONE(guid, 2).
        s = UEFI_VOCA6(locate, SEDES(guid), 0, SEDES(abs), 0, 0, 0).
        SI s == 0 TUNC CONTENTUM(50333800) = abs. FIN-SI.
        SI rel != 0 TUNC DECLARA rr SICUT NUMERUS VALENS UEFI_VOCA6(CONTENTUM(rel), rel, 0, 0, 0, 0, 0). FIN-SI.
        SI abs != 0 TUNC DECLARA ra SICUT NUMERUS VALENS UEFI_VOCA6(CONTENTUM(abs), abs, 0, 0, 0, 0, 0). FIN-SI.
    FIN-SI.
    DECLARA vol SICUT NUMERUS VALENS UEFI_VOLUMEN_APERI().
    REDDE 1.
FIN-FUNCTIO.

FUNCTIO UEFI_POLLE REDDENS NUMERUS.
    DECLARA cl SICUT NUMERUS VALENS UEFI_CLAVES_POLLE().
    DECLARA ma SICUT NUMERUS VALENS UEFI_MURIS_ABS_POLLE().
    SI ma == 0 TUNC ma = UEFI_MURIS_REL_POLLE(). FIN-SI.
    DECLARA systema SICUT NUMERUS VALENS CONTENTUM(50333704).
    SI systema != 0 TUNC
        DECLARA boot SICUT NUMERUS VALENS CONTENTUM(systema + 96).
        SI boot != 0 TUNC
            DECLARA stall SICUT NUMERUS VALENS CONTENTUM(boot + 248).
            SI stall != 0 TUNC DECLARA st SICUT NUMERUS VALENS UEFI_VOCA6(stall, 10000, 0, 0, 0, 0, 0). FIN-SI.
        FIN-SI.
    FIN-SI.
    CONTENTUM(50331728) = CONTENTUM(50331728) + 1.
    REDDE cl + ma.
FIN-FUNCTIO.

'''

marker = "FUNCTIO VOLUMEN_PARA REDDENS NUMERUS.\n"
nuc = substitue_unum(nuc, marker, uefi_runtime + marker, "ante VOLUMEN_PARA")

vetus_serva = '''FUNCTIO VOLUMEN_SERVA REDDENS NUMERUS.\n    SI CONTENTUM(50333696) == 1 && CONTENTUM(50333792) == 1 TUNC\n        CONTENTUM(50333808) = 0.\n        CONTENTUM(50333800) = 1.\n        DECLARA factum SICUT NUMERUS VALENS POLLE().\n        SI CONTENTUM(50333808) == 1 TUNC REDDE 1. FIN-SI.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO VOLUMEN_RELEGE REDDENS NUMERUS.\n    SI CONTENTUM(50333696) == 1 && CONTENTUM(50333792) > 0 TUNC\n        CONTENTUM(50333808) = 0.\n        CONTENTUM(50333800) = 2.\n        DECLARA factum SICUT NUMERUS VALENS POLLE().\n        SI CONTENTUM(50333808) == 1 && VOLUMEN_PARA() < 2 TUNC REDDE 1. FIN-SI.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n'''
novum_serva = '''FUNCTIO VOLUMEN_SERVA REDDENS NUMERUS.\n    REDDE UEFI_VOLUMEN_SERVA().\nFIN-FUNCTIO.\n\nFUNCTIO VOLUMEN_RELEGE REDDENS NUMERUS.\n    SI UEFI_VOLUMEN_RELEGE() == 1 && VOLUMEN_PARA() < 2 TUNC REDDE 1. FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n'''
nuc = substitue_unum(nuc, vetus_serva, novum_serva, "VOLUMEN_SERVA/RELEGE")

init_vetus = '''    DECLARA factum SICUT NUMERUS VALENS 0.\n    DECLARA migratio SICUT NUMERUS VALENS VOLUMEN_PARA().\n'''
init_novum = '''    DECLARA factum SICUT NUMERUS VALENS 0.\n    DECLARA uefi_paratus SICUT NUMERUS VALENS UEFI_PARA().\n    DECLARA volumen_lectum SICUT NUMERUS VALENS UEFI_VOLUMEN_RELEGE().\n    DECLARA migratio SICUT NUMERUS VALENS VOLUMEN_PARA().\n'''
nuc = substitue_unum(nuc, init_vetus, init_novum, "initium UEFI")
nuc = substitue_unum(nuc, "            factum = POLLE().\n", "            factum = UEFI_POLLE().\n", "ansa principalis POLLE")

# SALVE non amplius automatice in PROGRAMMATA recreatur.
functio_exempla_vetus = '''FUNCTIO PROGRAMMATA_EXEMPLA_PARA REDDENS NUMERUS.\n    DECLARA salve SICUT NUMERUS VALENS 0.\n    DECLARA tabula SICUT NUMERUS VALENS 0.\n    DECLARA i SICUT NUMERUS VALENS 6.\n    DUM i < 12 PERFICE\n        SI PROGRAMMA_NOMEN_EST(i, 0) == 1 TUNC salve = 1. FIN-SI.\n        SI PROGRAMMA_NOMEN_EST(i, 1) == 1 TUNC tabula = 1. FIN-SI.\n        i = i + 1.\n    FIN-DUM.\n    DECLARA addita SICUT NUMERUS VALENS 0.\n    SI salve == 0 TUNC\n        i = 6.\n        DUM i < 12 && CONTENTUM(50401344 + i * 32) == 1 PERFICE i = i + 1. FIN-DUM.\n        SI i < 12 TUNC addita = addita + PROGRAMMA_EXEMPLUM_PONE(i, 0). FIN-SI.\n    FIN-SI.\n    SI tabula == 0 TUNC\n        i = 6.\n        DUM i < 12 && CONTENTUM(50401344 + i * 32) == 1 PERFICE i = i + 1. FIN-DUM.\n        SI i < 12 TUNC addita = addita + PROGRAMMA_EXEMPLUM_PONE(i, 1). FIN-SI.\n    FIN-SI.\n    REDDE addita.\nFIN-FUNCTIO.\n'''
functio_exempla_novum = '''FUNCTIO PROGRAMMATA_EXEMPLA_PARA REDDENS NUMERUS.\n    DECLARA tabula SICUT NUMERUS VALENS 0.\n    DECLARA i SICUT NUMERUS VALENS 6.\n    DUM i < 12 PERFICE\n        SI PROGRAMMA_NOMEN_EST(i, 1) == 1 TUNC tabula = 1. FIN-SI.\n        i = i + 1.\n    FIN-DUM.\n    DECLARA addita SICUT NUMERUS VALENS 0.\n    SI tabula == 0 TUNC\n        i = 6.\n        DUM i < 12 && CONTENTUM(50401344 + i * 32) == 1 PERFICE i = i + 1. FIN-DUM.\n        SI i < 12 TUNC addita = addita + PROGRAMMA_EXEMPLUM_PONE(i, 1). FIN-SI.\n    FIN-SI.\n    REDDE addita.\nFIN-FUNCTIO.\n'''
nuc = substitue_unum(nuc, functio_exempla_vetus, functio_exempla_novum, "PROGRAMMATA_EXEMPLA_PARA")

if "POLLE()" in nuc:
    raise SystemExit("ERRATUM: POLLE() adhuc in nucleo manet")
NUCLEUS.write_text(nuc, encoding="utf-8")

print("RECTE: compilator et nucleus ad runtime VINDEX purum migrati sunt.")
