# ATMOS // TERMINAL DEPTH

ATMOS est primum programma maius in `PROGRAMMATA/`: ludus qui VINDEX sub usu applicationis verae exercet et progressionem linguae dirigit.

## Fontes canonici

```text
PROGRAMMATA/ATMOS_TERMINAL_DEPTH/
├── COMMUNE/
│   └── nucleus.vindex
├── POC_I/
│   ├── principalis.vindex
│   └── PROIECTUM.vindex
├── POC_II/
│   ├── interactivum.vindex
│   └── PROIECTUM.vindex
├── POC_III/
│   ├── graphicum.vindex
│   └── PROIECTUM.vindex
└── POC_IV/
    ├── ludus.vindex
    └── PROIECTUM.vindex
```

Hi fontes sub `PROGRAMMATA/` sunt fontes applicationis canonici. Probationes CI
construunt directe hanc arborem radicis repositorii.

## POC I — nucleus persistentis

Probatio prima demonstrat sub Win64 nativo:

- compilationem PE32+;
- statum ludi in memoria;
- simulationem determinatam;
- argumenta programmatis;
- I/O fasciculorum;
- persistentiam `atmos.sav`.

**Status:** probatum sub Windows vero.

## POC II — terminale interactum

Probatio secunda ludum e vocationibus separatis in sessionem continuam
interactivam convertit. Ea defectus generales VINDEX detexit et ad correctiones
`stdin`, `ORDO DE LITTERA`, `MITTE` atque bibliothecam `stdio.vindex` duxit.

**Status:** probatum sub Windows vero.

## POC III — graphica Win64 nativa

Probatio tertia VINDEX e terminali ad applicationem graphicam nativam ducit:

- FFI Win64 generalis per `LoadLibraryA` / `GetProcAddress`;
- ABI Microsoft x64 usque ad XVI argumenta;
- fenestra `CreateWindowExA`;
- framebuffer BGRA VINDEX;
- `StretchDIBits`;
- eventa Win32;
- clavem Escape et murem.

**Status:** probatum sub Windows vero, HWND verum et CLXXX lineae framebufferis certificatae.

## POC IV — ludus graphicus persistentis

Probatio quarta tres lineas anteriores coniungit in unum `.exe`:

- nucleus ludicus communis in `COMMUNE/nucleus.vindex`;
- formatum ATD1 v1 compatibile cum POC I/II;
- HUD GDI cum valoribus realibus status;
- conversio generalis `NUMERUS -> TEXTUS`;
- actiones `S/D/A/M/T/R/N`;
- eaedem actiones mure cliccabiles;
- sonar et eventa in visu;
- save post actiones.

Certificatio Windows seriem `descend -> mine -> ascend -> trade` exercet et
confirmat statum finalem `cycle=4`, `depth=120`, `oxygen=87`, `energy=75`,
`hull=100`, `credits=300`, `ore=0` tam in memoria/output quam in `atmos.sav`.

**Status:** probatum sub Windows vero.

## Regula progressionis

ATMOS non debet collectionem workaround privatorum fieri. Si facultas ab hoc
ludo postulata aliis programmatibus utilis est, primum in bibliothecam, ABI vel
linguam VINDEX generalem elevanda est; ludus deinde illam facultatem consumit.
