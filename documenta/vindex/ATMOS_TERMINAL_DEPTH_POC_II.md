# ATMOS Terminal Depth — Probatio applicationis VINDEX II

## Propositum

Probatio II primam probationem Win64 persistentem in **sessionem terminalem
continuam** convertit. Usor non amplius unum processum per actionem vocare debet;
`atmos_interactivum.exe` stdin legit, promptum ostendit, mandata exercet et idem
`atmos.sav` versionatum servat.

Hoc incrementum simul exemplum practicum regulae P11 est: ubi ludus facultatem
aliis programmatibus utilem desiderat, facultas generalis VINDEX praeferenda est
hack privato ATMOS.

## Primum beneficium generale inventum: stdin Win64

Probatio initio demonstravit defectum verum backend PE32+ Win64.

Contractus VINDEX historicus erat:

```text
0 = stdin
1 = stdout
```

`MITTE(1, ...)` sub Win64 iam descriptor 1 ad verum `STD_OUTPUT_HANDLE`
transducebat. `LEGE(0, ...)` autem numerum 0 directe ad `ReadFile` mittebat;
propterea pipe Windows verum reddebat:

```text
ERRATUM: stdin breve aut vacuum est
```

Correctio P11-B backend PE generaliter mutavit:

- prologus Win64 `GetStdHandle(-11)` pro stdout servat;
- prologus nunc etiam `GetStdHandle(-10)` pro stdin servat;
- `MITTE(1, ...)` ad handle stdout transfertur;
- `LEGE(0, ...)` ad handle stdin transfertur;
- descriptor fasciculi ordinarius alius quam 0/1 immutatus manet.

Compilator auto-hospes post mutationem ad punctum fixum regeneratus est:

```text
G2 = G3 = compilator canonicus
```

Probatio dedicata `tests/proba_stdio_win64.vindex` post correctionem pipe verum
Windows legit et stdout scribit. Hoc est beneficium linguae/ecosystematis
universale, non facultas ATMOS privata.

## Bibliotheca generalis `stdio.vindex`

Nova bibliotheca:

```text
bibliotheca/stdio.vindex
```

primum stratum portabile praebet:

- `STDIO_SCRIBE`;
- `STDIO_PROMPTUM`;
- `STDIO_LEGE_LINEAM`;
- `STDIO_AEQUA`.

`STDIO_LEGE_LINEAM` CR/LF tractat, NUL terminationem praebet et EOF ab linea
vacua distinguit. Implementatio prima consulto `LEGE(0, 1)` utitur: simplex et
correcta ante optimizationem buffering futuram.

Haec bibliotheca futuris CLI, instrumentis, debuggeribus et programmatibus
terminalibus VINDEX utilis est.

## ATMOS interactum

Fons:

```text
exempla/atmos_terminal_depth/interactivum.vindex
```

Productum:

```text
atmos_interactivum.exe
```

Mandata huius incrementi:

```text
status
scan
descend
ascend
mine
trade
repair
new
help
quit
```

Status ATD1 v1 cum Probatione I compatitur. Eadem expeditione cycle,
profunditas, oxygenium, energia, integritas, credita, minera et semen servantur.

Forma usus destinata:

```text
ATMOS LINK ONLINE — INTERACTIVE VINDEX SESSION
...
> descend
DESCENT COMPLETE
...
> mine
ORE EXTRACTED
...
> quit
SESSION CLOSED
```

## Secunda inventio: `PERGE` documentatum sed non receptum

Prima compilatio sessionis interactive lineam `PERGE.` reiecit cum diagnostico
structo `instructio ignota est`, quamquam `REFERENTIA.md` illud verbum adhuc ut
canonicum describit.

ATMOS POC II non dilatat hunc defectum in eadem mutatione: ansa interactive sine
`PERGE` scripta est. Discordantia inter referentiam et compilatorem tamen nunc
explicite nota est et ad P9 linguae reconcilianda manet. Aut `PERGE` rite
implementandum et regressionibus muniendum est, aut referentia corrigenda est.

Hoc est exemplum alterius utilitatis applicationis realis: usus concretus
facultates documentatas sed non vere exercitas detegit.

## Certificatio proposita

Workflow `.github/workflows/vindex-atmos-poc-ii.yml` sub Windows vero debet:

1. compilatorem VINDEX Win64 generare;
2. `interactivum.vindex` ad `atmos_interactivum.exe` compilare;
3. unam sessionem cum pluribus lineis stdin exercere;
4. actiones `descend -> mine -> ascend -> trade -> status -> quit` in eodem
   processu confirmare;
5. `atmos.sav` post sessionem byte per byte inspicere;
6. productum `.exe` ut artifactum servare.

Status huius documenti ante eventum workflow finale **IN PROBATIO** est. Relatio
certificationis tantum post exsecutionem viridem scribenda est.

## Directio post Probationem II

Si Probatio II transit, proximum incrementum utile est POC III:

- serializationem ATD1 ex ludo in bibliothecam versionatam generalem extrahere;
- PRNG determinatum generale creare;
- nucleum simulationis ATMOS a front-end terminali separare;
- deinde primum backend fenestrae applicationum VINDEX extra Sylvia OS
  investigare.

Norma manet: **ATMOS est ludus, sed etiam clientis probatio VINDEX.**
