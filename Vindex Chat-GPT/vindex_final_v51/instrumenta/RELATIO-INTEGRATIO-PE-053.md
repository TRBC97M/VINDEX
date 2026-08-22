# VINDEX 0.53 — Integratio PE/Windows in compilatorem (RELATIO, v2)

## Propositum

Idem propositum quam relatio prior (integrare mechanismum PE64 in
`compilator_vindex.vindex`), sed haec versio **rebasata** est super
statum currentem `chatgpt/vindex-053-compilator-dynamicus` **post**
dissolutionem completam `tabula` (commits `8860585`, `a3d5368`, et
alii — 132 commits inter caput antiquum et hoc novum).

Prima versio huius integrationis (in ramo separato, jam PR aperta) facta
erat super statum **ante** hanc dissolutionem. Cum `tabula` omnino e
compilatore remota est, mutationes antiquae rebasari debuerunt, non
simpliciter fundi — hoc fecimus manualiter, applicando easdem mutationes
super novum fontem, ne quid corrumperetur.

## Status honestus

Idem consilium conservativum quam antea: modus PE (tertium argumentum
`pe`) additur iuxta modum ELF, numquam eum mutans. Ambitus idem
limitatus: programmata solum `REDDE` utentia PE64 realiter generant;
functiones I/O adhuc solum ELF/Linux.

## Probationes exsecutae (super statum novum, post dissolutionem tabula)

Omnes hae probationes vere exsecutae sunt, super codicem qui `tabula`
non amplius continet:

- **Verificatio independens dissolutionis `tabula`**: numerus occurrentiam
  verbi `tabula` in compilatore recepto: **0**. Summa SHA-256 fasciculi
  binarii recepti: `0a4e4247c800c05da7734d1255bd6e54dd46a099214b081d65e03af577169d49`
  — identica relationi ChatGPT, verificata hic independenter per
  `sha256sum` directe in fasciculo dempto ex ramo.
- **Auto-hospitium punctum fixum, ante ullam mutationem nostram**:
  compilator receptus compilavit se ipsum, eadem summa. **RECTE**.
- **Auto-hospitium punctum fixum, post integrationem PE**: compilator
  mutatus (cum PE) compilavit se ipsum per modum ELF; binaria resultantia
  identica (SHA-256 `4374276776540d55d5a3caf067f9afd20734c7006f1ee15e208768e1944603ea`).
  **RECTE**: punctum fixum servatum etiam super novum fundamentum sine
  `tabula`.
- **Programma minimum per ELF**: exitus 42. **RECTE**.
- **Idem per PE**: fasciculus PE32+ validus generatus (`file`, Wine).
  **RECTE, structuraliter**.
- **VirtualAlloc + scriptio acervi**: verificata per GDB directe —
  `0x2000000` continet exacte `0x2000010` post exsecutionem. **RECTE**.

## Difficultas nota (eadem quam antea, non nostra)

Terminatio completa sub hoc systemate Wine adhuc causat idem defectum
exhaustive documentatum in `pe-windows-backend/RELATIO-PE-WINDOWS.md`
(§3, machina SEH interna Wine). Non mutata ab hac rebasatione — defectus
in Wine ipso latet, non in nostro codice, ut multipliciter hic et alibi
demonstratum est.

## Relatio ad ramum prioris integrationis

Ramus prior (`claude/pe-integration-053`, PR #7) super statum antiquum
(cum `tabula`) factus est et probabiliter non amplius directe fundi
potest sine conflictibus, data magnitudo mutationum interpositarum
(132 commits). Hic ramus (`claude/pe-integration-053-v2`) illum
substituit, super statum currentem factus. Consulendum est PR #7
claudere in favorem huius, vel eam actualizare cum his fasciculis.

VINDEX Latine cogitat. Sylvia Latine loquitur.

## Addendum — PROCLAMA/MITTE sub PE (secunda pars huius contributionis)

Post rebasationem super statum sine `tabula`, contributio extensa est ad
implementandam catenam I/O consolae PE completam:

### Mutationes structurales

1. **`contextus_parseris` extensus** (56 → 72 octeta): duo nova campa,
   `modus_pe` (valor simplex) et `descriptor_iat_pe` (punctum ad
   descriptorem parium dynamicum, per `INITIA_PARES_DYNAMICA` initiatum).
2. **`COMPONE_VOCA_IAT_DYNAMICA`**: substituit variabiles individuales
   `loci_iat_exitprocess`/`loci_iat_virtualalloc` prioris versionis.
   Quaevis vocatio IAT registrat par `(id_functionis, locus_patch)` in
   lista dynamica parium contextus, reutens infrastructuram `PARES_*`
   iam existentem pro vocationibus pendentibus.
3. **`CONSTRUE_CAPUT_PE` extensa ad IV functiones**: `ExitProcess`(0),
   `VirtualAlloc`(1), `GetStdHandle`(2), `WriteFile`(3). Circulus super
   omnia paria registrata patchat quamque vocationem ad IAT slot
   correctum, secundum `id_functionis`.
4. **`COMPONE_SCRIBE_STDOUT_DYNAMICA`**: functio auxiliaris nova, generat
   sequentiam `GetStdHandle(STD_OUTPUT_HANDLE)` + `WriteFile` (modo PE)
   vel `write` syscall (modo ELF), secundum `MODUS_PE_LEGE`. Substituit
   sex loca in codice ubi antea syscall directus scribebatur:
   `COMPONE_IMPRIME_NUMERUS` (signum et cifrae), `COMPONE_IMPRIME_CHAR`,
   `COMPONE_IMPRIME_PADEADO`, et ambo rami `PROCLAMA` (catena litteralis
   et numerus/fluitans).

### Ambitus explicite non tactus

`MITTE` **non** mutata est. Haec functio generalior est quam `PROCLAMA`
(scribit ad quemvis descriptorem fasciculi, non solum stdout, per
circulum elementum-post-elementum) et intrinsece dependet ab abstractione
"handle fasciculi" quae adhuc functiones `APERI_LEGERE`/`APERI_SCRIBERE`/
`CLAUDE` requirit — has, ut convenit, ChatGPT tractabit. Similiter,
`SCRIBE_LECTUS` (functio quae ultimam litteram lectam rescribit, pars
familiae `LEGE`) intacta relicta est, quamvis ad stdout scribat, quia
conceptualiter parti I/O fasciculorum pertinet.

### Duo defectus proprii inventi et correcti in hac secunda parte

1. **Adresses catenarum litteralium**: codex qui adressem catenae in
   registrum onerat utebatur constanti `4194304` (0x400000, fundamentum
   ELF) incondicionaliter. Correctum: calculus conditionalis secundum
   `MODUS_PE_LEGE`, adhibens fundamentum PE (`5368709120 + 4096 - 512 +
   sedes_chorda`) in modo PE.
2. **Defectus resolutionis variabilium ad magnam profunditatem
   nidificationis**: variabiles simplices `modus_pe` et
   `capita_reservata` (declaratae ad summum `PRINCIPALIS`) redderunt
   valores corruptos (verisimiliter adresses pilae) cum lectae intra
   codicem valde nidificatum rami `PROCLAMA` catenae litteralis (circiter
   decem gradus nidificationis SI/DUM). **Non plene explicatum** — nota
   ad investigationem futuram de systemate variabilium localium
   dynamicarum. Consilium adhibitum: pro `modus_pe`, uti
   `MODUS_PE_LEGE(contextus_parseris)` (per punctum, non variabilem
   simplicem); pro `capita_reservata`, valorem constantem 512 directe
   inserere, quia in hoc contextu (intra `SI modus_pe==1`) semper illud
   valorem habet.

### Probationes exsecutae (omnes vere currunt, non solum scriptae)

Vide `instrumenta/proba_proclama_pe_localiter_053.sh` (probatio nova,
exsecuta et confirmata RECTE quinquies):
- ELF catena: `"Salve ex PE!"`, exitus 33 — RECTE.
- PE catena: `"Salve ex PE!"` scriptum correcte sub Wine (verificatum
  per octeta exitus directa, non per codicem terminationis, propter
  defectum notum SEH Wine) — RECTE.
- ELF multi (catena+numerus+catena sequentialia): `"Premier\n999\n
  Dernier"`, exitus 7 — RECTE.
- PE multi: omnes tres partes praesentes in exitu — RECTE.
- Auto-hospitium punctum fixum post has mutationes: G2=G3 (SHA-256
  identica) — RECTE.

Exempla nova: `examples/proclama_catena_pe_053.vindex`,
`examples/proclama_multi_pe_053.vindex`.

