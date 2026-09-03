# ATMOS // TERMINAL DEPTH

ATMOS est primum programma maius in `PROGRAMMATA/`: ludus terminalis qui VINDEX sub usu applicationis verae exercet.

## Fontes canonici

```text
PROGRAMMATA/ATMOS_TERMINAL_DEPTH/
├── POC_I/
│   ├── principalis.vindex
│   └── PROIECTUM.vindex
└── POC_II/
    ├── interactivum.vindex
    └── PROIECTUM.vindex
```

Ab P11-B hi fontes sunt fontes applicationis canonici. Exemplaria historica sub arbore interna compilatoris non amplius auctoritas programmatis sunt; probationes CI construunt fontes huius directorii.

## POC I

Probatio prima demonstrat sub Win64 nativo:

- compilationem PE32+;
- statum ludi in memoria;
- simulationem determinatam;
- argumenta programmatis;
- I/O fasciculorum;
- persistentiam `atmos.sav`.

**Status:** probatum sub Windows vero.

## POC II

Probatio secunda ludum e vocationibus separatis in **sessionem continuam interactivam** convertit:

```text
ATMOS LINK ONLINE
> descend
> mine
> ascend
> trade
> status
> quit
```

Probatio haec defectus generales VINDEX detexit et ad correctiones linguae duxit:

1. descriptor `0 = stdin` sub backend PE Win64 non ad `STD_INPUT_HANDLE` convertebatur — correctio P11-B facta et sub Windows vero probata est;
2. `ORDO DE LITTERA` accessum historicum octo-octetalem retinebat — P9 stride unius octeti dat, etiam per parametros, cum compilatore auto-hospite ad punctum fixum certificato;
3. `MITTE(fd, ordo, n)` stride VIII historicum cogebat — nunc magnitudinem elementi observat et `LITTERA` byte-addressatum exacte scribit.

Regressiones dedicatae confirmant `ORDO DE LITTERA` et `MITTE LITTERA` sub ELF, PE32+ et Windows vero. `MITTE` fasciculum quinque octetorum `ATD1` + versionem `1` exacte producit.

Ad migrationem tutam, spatium pilae ab ordinibus `LITTERA` reservatum adhuc historicam magnitudinem servat; hoc est solum inefficiens, non pars semanticae publicae. Contractus visibilis byte-addressatus est. Optimatio spatii separatim fieri potest sine mutando API programmatis.

**Status:** POC II probatum sub Windows vero: sessio stdin continua, simulationis status et persistentia `atmos.sav` certificata sunt.
