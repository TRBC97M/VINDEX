# ATMOS Terminal Depth — Certificatio Probationis I

## Status

**PROBATUM — III Septembris MMXXVI.**

Haec relatio eventum exsecutionis verae conservat. Non est intentio futura nec
inspectio statica formae PE tantum.

## Catena certificata

GitHub Actions cursus `33713788910`, ex Pull Request #174, duas partes
exsecutus est.

### I. Compilator Win64

In Ubuntu compilator canonicus VINDEX fons `src/compilator_vindex.vindex` ad
`compilator_vindex.exe` PE32+ Win64 generatus est. Gradus sine errore
perfectus est et productum inter jobs artifactum transmissum est.

### II. ATMOS sub Windows vero

Secundum job in **Microsoft Windows Server 2025** (`windows-2025-vs2026`)
`compilator_vindex.exe` vere exsecutus est. Is fontem
`exempla/atmos_terminal_depth/principalis.vindex` ad `atmos.exe` compilavit.
Signatura MZ verificata est; deinde `atmos.exe` ipse exsecutus est.

Catena ludi:

```text
new -> descend -> mine -> ascend -> trade -> status
```

## Valores observati

### Post `new`

```text
CYCLE 0
DEPTH_M 120
OXYGEN 100
ENERGY 100
HULL 100
CREDITS 250
ORE 0
WORLD_SEED 7319
```

### Post `descend`

```text
CYCLE 1
DEPTH_M 270
OXYGEN 94
ENERGY 92
```

### Post `mine`

```text
ORE EXTRACTED
5
CYCLE 2
OXYGEN 90
ENERGY 80
ORE 5
```

### Post `ascend`

```text
CYCLE 3
DEPTH_M 120
OXYGEN 87
ENERGY 75
```

### Post `trade`

```text
TRADE COMPLETE
PRICE_PER_ORE 10
CYCLE 4
DEPTH_M 120
OXYGEN 87
ENERGY 75
HULL 100
CREDITS 300
ORE 0
WORLD_SEED 7319
```

Invocatio `status` separata eosdem valores post novam exsecutionem processus
reddidit. Ergo status inter processus vere persistit, non tantum in memoria unius
processus manet.

## Fasciculus persistentiae

`atmos.sav` post singulas mutationes inspectus est. Probatio postulavit:

- mensuram exactam XLVIII octetorum;
- magiam ASCII `ATD1`;
- versionem I;
- decem campos `u32` little-endian in offsetis documentatis;
- mutationes exactas cycli, profunditatis, oxygenii, energiae, creditorum et
  mineralium post actiones.

## Exitus auctorativus

Workflow scripsit:

```text
RECTE: ATMOS VINDEX PE Win64 et persistentia sub Windows probata sunt.
```

Artifactum `atmos-terminal-depth-vindex-poc-i` quoque a workflow servatum est.

## Assertio nunc demonstrata

> **VINDEX potest ludum persistentem nativum Win64 ex fonte VINDEX producere et
> sub Windows vero exsequi.**

Hoc adhuc non significat VINDEX machinam ludorum completam habere. Significat
vero fundamenta applicationum ordinariarum extra Sylvia OS iam satis realia esse
ut ludus eas exerceat et progressionem linguae dirigat.

## Debita generalia a probatione detecta

Probatio I simul quinque directiones utilitatis generalis confirmat:

1. input terminale/`stdin` canonicum, ut una sessio interactiva fieri possit;
2. bibliotheca serializationis versionatae, ne formatos binarios omnis
   applicatio manu componat;
3. PRNG deterministicum bibliothecae standardis pro simulationibus et
   probationibus reproducibilibus;
4. API consolam/TTY portabilem pro colore, cursore, dimensionibus et input;
5. bibliothecam graphicae applicationum VINDEX extra partes Sylviae privatas.

Atmos his facultatibus clientis realis fieri potest. Norma est ut solutio, si
aliis programmatibus utilis est, in VINDEX generale elevetur potius quam hack
privatus ludi maneat.
