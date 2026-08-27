# UEFI VINDEX Purum — Contractus Canonicus

## Propositum

PR #109 canonizat facultates UEFI primum in PR experimentali #82 demonstratas. Facultates utiles selective supra `main` hodiernum portatae sunt; ramus experimentalis ipse propter magnam divergentiam non wholesale mergitur.

Catena canonica non continet C neque assembler externum residentem:

```text
OVMF
  ↓
BOOTX64.EFI [VINDEX]
  ↓
NUCLEUS.BIN [VINDEX]
  ↓
FRAMEBUFFER
  ↓
SYLVIA
```

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

---

## Target compilatoris

Compilator canonicus tertium modum x86-64 praebet:

```bash
./compilator_vindex fons.vindex productum.efi uefi
```

Productum est PE32+ subsystem **EFI application**. Target UEFI importationes Win32 non continet.

Targeta manent distincta:

- default — ELF64 x86-64;
- `pe` — PE32+ Win64;
- `uefi` — PE32+ EFI application.

Mutationes UEFI non licet semanticam PE/Win64 per accidens mutare.

---

## Primitiva basimi gradus

### Vocationes firmware

Ponticulus VINDEX functiones firmware per contractum vocationis UEFI adhibet. `UEFI_VOCA6` vocationem indirectam cum conventionibus necessariis praebet.

### `SALI_AD`

```vindex
SALI_AD(adressa).
```

Imperium ad sedem datam transfert et non redit. In catena Sylviae ad punctum ingressus nuclei realis adhibetur.

---

## Ponticulus canonicus

Fons:

```text
Vindex Chat-GPT/vindex_final_v51/systema/uefi/ponticulus_uefi_purus.vindex
```

Officia eius sunt stricta:

1. watchdog firmware exstinguere;
2. LoadedImage et SimpleFileSystem invenire;
3. `NUCLEUS.BIN` aperire;
4. magnitudinem veram per `GetInfo` legere;
5. memoriam nuclei secundum contractum praesentem reservare;
6. `NUCLEUS.BIN`, `TEXTUS.BIN` et `FORMA.BIN` legere;
7. GOP, framebuffer, resolutionem et `PixelsPerScanLine` obtinere;
8. metadata nuclei implere;
9. `PONTOK` scribere;
10. per `SALI_AD` ad nucleum transire.

Ponticulus ansam eventuum, fenestras, input continuum aut runtime applicationum non administrat.

---

## GOP

Structura `EFI_GRAPHICS_OUTPUT_MODE_INFORMATION` hoc contractu adhibetur:

```text
HorizontalResolution   +4
VerticalResolution     +8
PixelFormat           +12
PixelInformation      +16 ... +31
PixelsPerScanLine     +32
```

Error experimentalis qui `PixelsPerScanLine` ad +36 legebat lineam absurdam generabat. Correctio canonica est **+32**.

---

## Volumen FAT

Constructor:

```text
systema/uefi/construe_uefi_purum.sh
```

Creator imaginis:

```text
systema/uefi/fac_imaginem_uefi.py
```

Imago FAT canonica continet saltem:

```text
EFI/BOOT/BOOTX64.EFI
NUCLEUS.BIN
TEXTUS.BIN
FORMA.BIN
```

Probatio dedicata ipsa imaginem inspicit; non sufficit ut fasciculi tantum in directorio constructionis existant.

---

## Contractus memoriae praesentis

Nucleus ELF hodiernus acervum ad sedem fixam disponit. Propter hanc dispositionem `p_memsz` circiter XLVI MiB declarari potest etiam si fasciculus nucleus ipse multo minor est.

Firmware non necessario unum blocum continuum huius magnitudinis concedit. Ponticulus canonicus regionem requisitam **frustatim** reservat et sic contractum nuclei praesentis implet.

Hoc efficit ut catena hodierna rite bootet; non significat dispositionem ELF optimam esse.

### Debitum separatum

Futurum opus potest:

- plura segmenta `PT_LOAD` recte generare;
- acervum a segmento ELF statice extenso separare;
- relocationem memoriae maturiorem introducere.

Haec est emendatio formae/ABI, non conditio residua certificationis P1.

---

## Puritas absoluta

Post PR #109:

- `bootstrap_uefi.c` e linea canonica removetur;
- constructor C historicus removetur;
- `instrumenta/verifica_puritatem_sylviae.py` nullam exceptionem C admittit;
- codex canonicus sub `systema/` extensionem C/C++/assembler/Rust habere non potest.

Instrumenta host ut Python, Bash et QEMU ad constructionem vel probationem adhiberi possunt. Regula puritatis ad **codicem systematis et runtime** pertinet, non ad prohibendum instrumenta testium.

---

## Probatio canonica

Scriptum:

```text
instrumenta/proba_catenam_uefi_053.sh
```

Workflow:

```text
.github/workflows/catena-uefi-vindex.yml
```

Custodia requirit:

- auto-hospitium `compilator canonicus = G2 = G3`;
- XXIX/XXIX probationes canonicas;
- PE32+ EFI application validam;
- puritatem absolutam;
- QEMU + OVMF;
- `PONTOK`;
- nullam exceptionem CPU;
- nullum defectum paginae;
- screendump 1280×800;
- imaginem non uniformem;
- plures colores distinctos.

In certificatione integrationis P1 screendump **IX colores distinctos** exhibuit et Sylvia vere pingere probata est.

---

## Historia diagnosticorum

In investigatione experimentali tres hypotheses falsae — UMBRA corrupta, coordinatae absurdae aliunde ortae, framebuffer non mappatus — per GDB reiectae sunt. Historia harum investigationum servanda est quia demonstrat differentiam inter hypothesin et causam verificatam.

Causa finalis visibilis GOP erat offset falsum `PixelsPerScanLine`; contractus memoriae separatim per reservationes frustatim stabilitus est.

---

## Finis P1

P1 perfectum declaratur quia vera catena repetibilis ex firmware usque ad picturam Sylviae sine C probata est.

Proximum opus non est iterum bootstrapping solvere. Proximum est P3: eandem catenam cum Fenestrale II Purus et input canonico componere.

**Nullum genus programmatis extra fines VINDEX esse debet.**
