# ATMOS // TERMINAL DEPTH

ATMOS est primum programma maius in `PROGRAMMATA/`: ludus terminalis qui VINDEX sub usu applicationis verae exercet.

## POC I

Probatio prima demonstrat sub Win64 nativo:

- compilationem PE32+;
- statum ludi in memoria;
- simulationem determinatam;
- argumenta programmatis;
- I/O fasciculorum;
- persistentiam `atmos.sav`.

**Status:** probatum.

## POC II

Probatio secunda ludum e vocationibus separatis in **sessionem continuam interactive** convertit:

```text
ATMOS LINK ONLINE
> descend
> mine
> ascend
> trade
> status
> quit
```

Ea iam duos defectus generales VINDEX detexit:

1. descriptor `0 = stdin` sub backend PE Win64 non ad `STD_INPUT_HANDLE` convertebatur — correctio P11-B facta et sub Windows vero probata est;
2. `ORDO DE LITTERA` magnitudinem elementi VIII octetorum accipit, quamquam `LITTERA` elementum unius octeti esse debet — correctio compilatoris nunc agitur.

**Status:** activum in PR #175.

## Fontes

Dum POC II corrigitur et recertificatur, fontes experimentales adsunt in arbore canonica compilatoris sub:

`Vindex Chat-GPT/vindex_final_v51/exempla/atmos_terminal_depth/`

Post certificationem POC II, fontes programmatis in hoc directorium transferentur et probationes internae tantum regressiones contractuum VINDEX retinebunt.
