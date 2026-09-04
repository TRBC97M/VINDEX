# ATMOS // TERMINAL DEPTH

ATMOS est primum programma maius in `PROGRAMMATA/`: ludus qui VINDEX sub usu applicationis verae exercet et progressionem linguae dirigit.

## Linea activa — NATIVUM

A III Septembris MMXXVI, implementatio activa ludi est:

```text
PROGRAMMATA/ATMOS_TERMINAL_DEPTH/NATIVUM/
```

`NATIVUM` est reconstructio munda ex `main`, postquam experimenta humana POC VI/VII demonstraverunt frontem graphicam e framebuffer + textu GDI directo non esse fundamentum stabile ludi finalis.

Versio HTML auctoris est **referentia morum**: navigationem sonar, mundum, bathymetriam, extractionem, docking, economiam et ceteras mechanicas describit. Nullus HTML/JavaScript in runtime NATIVUM includitur; subsystemata propria VINDEX scribuntur.

Regula graphica NATIVUM est absoluta:

```text
status ludi
    ↓
compositor VINDEX
    ↓
unus framebuffer BGRA VINDEX
    ↓
una praesentatio Win32
```

Textus quoque in framebuffer a VINDEX rasterizatur. `TextOutA`/`WINAPP_TEXTUS` in fonte NATIVUM CI vetantur.

**Status:** in reconstructione et probatione humana; PR #183 draft. Non adhuc canonizatum in `main`.

## POC historici

POC I–V manent fontes canonici **probationum historicarum**. Demonstrant facultates reales VINDEX, sed non sunt fundamentum gameplay ludi activi.

```text
PROGRAMMATA/ATMOS_TERMINAL_DEPTH/
├── COMMUNE/                 # communia POC historica
├── POC_I/                   # persistentia terminalis
├── POC_II/                  # sessione interactiva
├── POC_III/                 # prima graphica Win64
├── POC_IV/                  # primus ludus graphicus persistentis
├── POC_V/                   # mundus proceduralis POC
└── NATIVUM/                 # IMPLEMENTATIO ACTIVA EX NOVO
```

## POC I — nucleus persistentis

Probatio prima demonstrat sub Win64 nativo compilationem PE32+, statum ludi in memoria, simulationem determinatam, argumenta programmatis, I/O fasciculorum et persistentiam `atmos.sav`.

**Status:** probatum sub Windows vero.

## POC II — terminale interactum

Probatio secunda ludum e vocationibus separatis in sessionem continuam interactiva convertit. Ea defectus generales VINDEX detexit et ad correctiones `stdin`, `ORDO DE LITTERA`, `MITTE` atque bibliothecam `stdio.vindex` duxit.

**Status:** probatum sub Windows vero.

## POC III — graphica Win64 nativa

Probatio tertia VINDEX e terminali ad applicationem graphicam nativam duxit: FFI Win64, ABI Microsoft x64, `CreateWindowExA`, framebuffer BGRA, `StretchDIBits`, eventa, Escape et murem.

**Status:** probatum sub Windows vero.

## POC IV — ludus graphicus persistentis

Probatio quarta coniunxit nucleum persistentem, HUD GDI, conversionem `NUMERUS -> TEXTUS`, actiones ludi, sonar et save ATD1.

**Status:** probatum sub Windows vero.

## POC V — mundus proceduralis persistentis

Probatio quinta addidit PRNG `aleatorium.vindex`, API `win32_app.vindex`, sectores determinatos, contactus sonar et persistentiam ATW1. Etiam defectus generales compilatoris detexit et correxit: identificatores longos, commentaria top-level/`FORMA`, atque deductionem generis post `=`.

**Status:** probatum sub Windows vero — III Septembris MMXXVI.

## Regula progressionis

ATMOS non debet collectionem workaround privatorum fieri. Si facultas ab hoc ludo postulata aliis programmatibus utilis est, primum in bibliothecam, ABI vel linguam VINDEX generalem elevanda est; ludus deinde illam facultatem consumit.

In NATIVUM nulla facultas gameplay maior supra fundamentum nondum probatum aedificatur: CI automatica et probatio humana ambae requiruntur ante gradum sequentem.
