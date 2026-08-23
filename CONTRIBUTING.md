# Contributio ad VINDEX et Sylvia OS

## Principium

GitHub est fons communis et canonicus progressionis. Historia, rami et Pull Request statum operis definiunt. Directorium propter nomen agentis solum non habendum est vetitum vel historicum; ante iudicium inspicienda sunt `ARCHITECTURA.md`, ramus activus et contextus mutationis.

## Regulae generales

- `main` est linea stabilis communis.
- Omnis operatio nova in ramo separato fiat.
- Nulla mutatio directe in `main` facienda est.
- Pull Request ante coniunctionem ad `main` requiritur.
- Archivorum ZIP vel exempla veterum non sunt fundamentum canonica evolutionis.
- Directorii temporarii synchronizationis, inter quos `.tmp.driveupload/` et `.tmp.drivedownload/`, numquam in historiam Git mittantur.

## Lingua

VINDEX Latine cogitat. Sylvia Latine loquitur. Haec non est solum
inscriptio decorativa, sed regula obligatoria pro omni parte activa et
canonica huius repositorii:

- Grammatica ipsa linguae VINDEX (verba clavia, structura syntactica)
  Latina est et manet.
- Codex compilatoris (`compilator_vindex.vindex`), instrumenta
  (`instrumenta/`), probationes (`tests/`), exempla (`examples/`), et
  relationes (`RELATIO-*.md`) — omnia haec, **commentaria, chordae
  litterales (nuntii erratorum, `PROCLAMA`, `print`), nomina
  functionum et variabilium, docstrings, et ipsi tituli fasciculorum
  ubi rationabiliter fieri potest** — Latine scribenda sunt.
- Hoc etiam ad instrumenta auxiliaria in aliis linguis scripta (Python,
  Bash, C) pertinet, non solum ad codicem VINDEX ipsum: catena bootstrap
  Python (`bootstrap/python/`) et scripta diagnostica quae eam invocant
  sequuntur eandem regulam.
- Nuntii commit (`git commit`) et descriptiones Pull Request Latine
  scribendae sunt, secundum morem iam observatum in historia hoc
  repositorii.
- Colloquium inter contributores humanos et agentes (extra Git ipsum,
  velut hoc CONTRIBUTING.md, vel colloquia in linguis vernaculis) non
  hac regula tenetur — sola pertinet ad id quod in repositorio ipso,
  tamquam parte canonica operis, manet.

**Exceptio explicita**: directoria archivalia continentia versiones
historicas antequam haec regula statuta est (exempli gratia
`Vindex Claude Ai/Vindex_final_versions/`) non retroactive corrigenda
sunt. Haec non sunt fundamentum canonica evolutionis (vide regulam
supra de archivis ZIP et exemplis veterum) et manent tantum ut memoria
historica, non ut codex activus.

Si agens (Claude, ChatGPT, aliusve) linguam non-Latinam in parte activa
et canonica repositorii invenit, id corrigere debet cum opportunitas
datur, praesertim si pars illa iam tangitur ob aliam causam. Non
necesse est omnem repositorium simul perscrutari; sufficit progressive
corrigere quod inventum est.

## Rami collaboratorum

Praefixa agentium servant originem operis:

- `chatgpt/...` pro ChatGPT;
- `claude/...` pro Claude;
- `copilot/...` pro GitHub Copilot;
- `gemini/...` pro Gemini.

Rami humanitus creati alio nomine uti possunt, dummodo `main` directe non mutetur.

Ramus novus plerumque ex `main` creetur. Tamen ramus super alium ramum poni potest si mutatio posterior a priore realiter dependet. Talis dependentia in descriptione Pull Request explicanda est, et basis post coniunctionem mutationis prioris ad `main` transferri potest.

## Separatio architecturica

Mutationes distinguendae sunt inter:

1. mutationem linguae VINDEX;
2. mutationem ecosystematis VINDEX;
3. mutationem Sylvia OS;
4. mutationem communem.

Si mutatio grammaticam, ABI, typum, compilatorem aut specificationem afficit, est mutatio VINDEX. Si sola instrumenta, bibliothecae aut Officina tanguntur, est mutatio ecosystematis. Si initium, memoria systematis, fasciculi, fenestrale aut operationes systematis mutantur, est mutatio Sylvia OS. In casu coniunctionis necessitatum, mutatio communis explicite justificetur.

## Disciplina Git

- Ante opus statum praesentem rami et mutationes aliorum inspice.
- Mutationes parvae, singulares et retractabiles praeferantur.
- Ante `push`, status Git inspiciatur, ne mutationes alienae aut temporariae includantur.
- Si alius ramus opus pertinens iam continet, prius inspiciatur quam labor parallelus duplicetur.

## Probationes et qualitas

- Omnis mutatio ad VINDEX aut Sylvia probationem pertinentem aut saltem inspectionem demonstrabilem habeat.
- Compilator auto-hospes et punctum fixum servanda sunt.
- Mutationes regressivae evitandae sunt.
- Nullam probationem transisse affirmare licet nisi vere exsecuta et verificata sit.

## Pull Request

Pull Request contineat:

- titulum succinctum et descriptivum;
- obiectum et ambitum mutationis;
- genus mutationis: VINDEX, ecosystema, Sylvia OS aut communis;
- fasciculos principales mutatos;
- probationes vel inspectiones exsecutas;
- pericula, limites et eventus notabiles;
- dependentiam ab alio ramo, si adest.

## Conclusio

Disciplina Git progressionem non impedire debet; debet efficere ut opus plurium collaboratorum componi, recognosci et retractari possit sine ambiguitate.

VINDEX Latine cogitat. Sylvia Latine loquitur.
