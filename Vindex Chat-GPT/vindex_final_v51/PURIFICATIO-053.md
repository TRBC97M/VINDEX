# VINDEX 0.53 — Purificatio nuclei linguae

## Propositum

Finis huius rami est nucleum VINDEX ita ordinare ut **codex activus linguae et compilatoris, quantum fieri potest, ipso VINDEX scribatur**. Instrumenta historica migrationis, probationes ad tempus scriptae, applicatio graphica, Systema et prototypa PE non sunt pars minima linguae.

Status completus ante purificationem servatur in ramo:

```text
archive/vindex-053-avant-purificatio
9e70b09a8a258a76467b1045aca8337abbf1d4de
```

Ita nihil historicum amittitur, etiam si e nucleo activo removetur.

## I. Nucleus retinendus

Haec ad linguam VINDEX hodie directe necessaria sunt:

- `src/compilator_vindex.vindex` — fons compilatoris auto-hospitis, totus VINDEX;
- `compilator_vindex` — binarium seminale distributum, donec alia via initii tota VINDEX exstet;
- `tests/casus/*.vindex` quae semanticam linguae probant;
- exempla minima `.vindex` quae facultates linguae demonstrant;
- `REFERENTIA.md`, `LEGE-ME.md`, `COMMENTARIUM.md`, `VERSION`, sigilla et documenta architecturae necessaria;
- `.gitattributes` et `.gitignore`.

Binaria compilata non sunt codex alterius linguae; retineri possunt si ad initium auto-hospitii requiruntur.

## II. Reescribenda in VINDEX

Haec instrumenta utilia sunt, sed codex eorum hodie alia lingua utitur et functio eorum per VINDEX perfici potest:

1. **Probator structuram PE** — `tests/proba_pe_structuram_053.py`.
   VINDEX iam fasciculos binarios aperire, octeta legere et numeros componere potest; ergo verificator MZ/PE/IAT in VINDEX scribi potest.
2. **Cursor probationum linguae** — `tests/run_tests.sh`.
   VINDEX iam `CURRE`, `EXSEQUERE`, fasciculos, tubulos et codices exitus habet. Probationes igitur a programmate VINDEX regi possunt. Scriptum shell interim tantum infrastructura est.
3. **Orchestratio puncti fixi** — `bootstrap/reconstruit.sh`.
   Compilator distributus iam se ipsum compilat. Generatio I/II/III et comparatio binaria per instrumentum VINDEX fieri possunt.
4. **Interfacies `vindexc`**.
   Compilatio directa iam per `compilator_vindex fons exitus [pe]` fit. Functiones vere utiles `vindexc` aut in compilatorem ipsum aut in parvum instrumentum VINDEX transferendae sunt.
5. **Custodiae structurales** (`inventaria_tabula_053.py` et similia) si post purificationem adhuc valorem permanentem habent. Custodiae unius migrationis iam absolutae non reescribendae sunt: removendae sunt.

## III. Removenda, non reescribenda

Haec instrumenta historica mutationes iam canonicas applicaverunt. In nucleo finali nullum munus runtime habent:

- `instrumenta/applica_*.py`;
- `instrumenta/corrige_*.py` quae mutationes semel applicaverunt;
- `instrumenta/migra_*.py`;
- `instrumenta/diagnostica_*.py` et `.sh` ad investigationes clausas pertinentes;
- generatoria probationum temporaria Python;
- relationes intermediae quae relatione canonica recentiore supersessae sunt.

Historia eorum ramo archivistico et Git servatur.

## IV. Extra nucleum transferenda

Haec VINDEX demonstrare possunt, sed **linguae ipsi ad operandum non sunt necessaria**:

- `systema/` integrum, imagines BIOS/UEFI, `BOOTX64.EFI`, `nucleus_systema.elf` — ad Sylvia/Systema pertinent;
- `runtime/vindex_graphica_gtk.c`, `vindex_graphica`, `formae/`, `officina/`, `src/officina_vindex.vindex`, `src/salutatio_vindex.vindex`, `bibliotheca/graphica.vindex`, initiatores Officinae/Salutationis — ecosystema graphica separatum;
- `Vindex Claude Ai/` — prototypa et relationes historicae PE; backend probatus iam in compilatore canonico est;
- scripturae PowerShell radicis (`repo_guard*.ps1`, `install_repo_guard*.ps1` et similes) — custodia repositorii, non lingua;
- binaria et imagines derivatae ecosystematis quae ex fontibus externis vel Systemate nascuntur.

Haec non delenda ex historia sunt; e ramo activo purificationis removenda sunt post probationem nuclei.

## V. Infrastructura externa temporarie admissa

GitHub Actions ipsa VINDEX non est. Fasciculi `.github/workflows/*.yml` et pauca mandata `bash`/`pwsh` in runneribus **infrastructura CI externa** sunt, non implementatio linguae. Interim admittuntur dum faciunt unum tantum opus: compilatorem VINDEX aedificare, programmata VINDEX exsequi et eventum observare.

Regula: CI non debet logicam compilatoris, parseris, PE, ELF aut linguae in Python/C/Shell implere.

## VI. Python bootstrap

`bootstrap/python/` non requiritur ad usum cotidianum VINDEX neque ad auto-hospitium ex binario distributo. Solum catena fiduciae historica est.

Ordo purificationis:

1. probationem puncti fixi **sine Python** stabilire;
2. semanticam linguae **sine Python** stabilire;
3. verificatorem PE in VINDEX substituere;
4. tum `bootstrap/python/` e nucleo activo removere.

Ramus archivisticus versionem Python integram servat.

## VII. Limen acceptationis

Purificatio non potest in ramum dynamicum integrari nisi:

- compilator distributus se ipsum ad punctum fixum producit;
- probationes semanticae nuclei ELF transeunt;
- PE Win64 minimum et I/O realiter sub Windows transeunt;
- nullus Python/C/assembler/PowerShell ad **implementationem linguae** requiritur;
- omnis exceptio non-VINDEX remanens explicite infrastructura externa est;
- Systema, Officina, GTK et prototypa non amplius nucleum linguae contaminant;
- index codicis non-VINDEX activi in relatione finali enumeratur, cum ratione cuiusque exceptionis.

## VIII. Primus gradus

Primum additur workflow `VINDEX 0.53 — Nucleus purus` qui punctum fixum et casus linguae **sine Python, GTK, Systemate aut bootstrap externo** probat. Post illum viridem, deletiones fiunt per gradus parvos et probatos.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
