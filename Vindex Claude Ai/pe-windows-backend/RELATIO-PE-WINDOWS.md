# VINDEX — Fundamenta PE/Windows (RELATIO)

## Propositum

Explorare et probare mechanismum minimum necessarium ut VINDEX exsecutabilia
Windows nativa (formam PE64) generare possit, sine dependentia ab ELF, Wine
solum ad probationem adhibito (non ad exsecutionem finalem).

## Status honestus

Haec contributio praebet **mechanismum probatum et functionalem**, non
**integrationem completam in compilatorem**. Duae res distinguendae sunt:

1. **Quod functionat, verificatum sub Wine 9.0**: constructio manualis capitis
   PE64 (DOS, PE, Optional Header, tabulae sectionum), tabula importationis
   (`kernel32.dll`), vocatio indirecta per IAT (`FF 15` + `call [rip+X]`),
   terminatio per `ExitProcess`.
2. **Quod exploratum sed non inclusum est**: scriptio in consolam per
   `GetStdHandle` + `WriteFile` — textus ipse scribitur correcte, sed
   combinatio cum terminatione processus postea causavit defectum non
   plene explicatum sub Wine huius systematis probationis (vide sectio
   "Difficultates", n. 3). Ideo fasciculi hic inclusi solum `ExitProcess`
   adhibent, non `WriteFile`.
3. **Quod nondum factum est**: integratio huius mechanismi in
   `compilator_vindex` ipsum, ita ut `CONSTRUE_CAPUT_ELF` et
   `CONSTRUE_CAPUT_PE` simul adsint et lingua VINDEX utrumque scopum eligere
   possit.

## Fasciculi

- `construe_pe_reference.py` — prototypum Python, exemplar functionale primum.
  Aedificat exsecutabile PE64 minimum quod `ExitProcess(42)` tantum vocat,
  sine ELF, sine NASM. Generat `exemplum_referens.exe` cum exsecutus est.
- `exemplum_referens.exe` — exemplar generatum a `construe_pe_reference.py`,
  1536 octeta. Verificatum sub Wine 9.0, quinquies consecutive, semper
  deterministicum:
  ```text
  $ wine64 exemplum_referens.exe
  $ echo $?
  42
  ```
- `construe_pe_vindex.vindex` — idem mechanismus, sed **scriptus in VINDEX
  ipso**, compilatus per `compilator_vindex` (ELF), qui exsecutabile PE64
  scribit. Probat VINDEX iam nunc capacem esse formam binariam alienam
  generandi, etiam antequam compilator ipse PE emittat.
- `exemplum_salve.exe` — exemplar generatum, 1536 octeta, verificatum sub
  Wine 9.0. Cursus:
  ```text
  $ wine64 exemplum_salve.exe
  Salve, munde ex VINDEX!
  $ echo $?
  45
  ```

## Difficultates inventae et notatae (non solutae hic)

### 1. Fovea custodiae pilae (stack guard gap)

Reservatio pilae magna (~7 MiB) in una instructione `sub rsp, N` potest a
nucleo Linux reici, si pila non gradatim tacta est antea. Solutio empirice
verificata: circulus qui quamque paginam 4 KiB seriatim tangit ante `sub`
finalem. **Hoc problema in `compilator_vindex` hodierno huius repositorii
non repertum est** (probatum cum programmate minimo et cum 700 variabilibus
localibus, utroque sine defectu). Fortasse aderat solum in ramo
experimentali privato ubi haec inventio primum facta est. Notandum tamen ad
cautelam, si reservationes maiores in futurum adhibeantur.

### 2. Regio `tabula[2900..]`

Quaevis nova metadata compilatoris quae hanc regionem `tabula` adhibet
periculum corruptionis habet cum regione formarum extremarum
(`tabula[2530 + idx*26 + k]`, vide `TEXTUS-052.md`). Confirmatum in ramo
experimentali privato: corruptio huius regionis causat circulum infinitum in
resolutione vocationum pendentium. Consilium: quaevis nova metadata communis
inter agentes regionem explicite documentandam et vacuam eligat, non
adivinandam.

**Nota addita post collationem cum `chatgpt/vindex-053-compilator-dynamicus`**:
error observatus in hac contributione (`"functio vocata non inventa est"`,
circulus infinitus in resolutione) simillimus est errori hodierno relato in
`RELATIO-PENDENTES-DIAGNOSTICA-053.md` (`ERRATUM: functio vocata non inventa
est`, `COMPILATIO MCCL PENDENTIUM: status=65`). Utraque contributio, seorsum
et independenter, in eandem categoriam defectus incidit: resolutio nominum/
vocationum per tabulam veterem fragilis est. Hoc corroborat consilium migrationis
ad descriptorium dynamicum iam in cursu. Non est necessarium hic causam radicalem
ambarum invenire — sufficit notare eas eiusdem generis esse.

### 3. `GetStdHandle` sequitur terminatio processus (non explicatum)

In experimentis privatis, sequentia "`GetStdHandle` deinde `ExitProcess`
(vel `RtlExitUserProcess`)" causavit defectum deterministicum sub Wine 9.0
huius systematis probationis specifice — semper eodem loco memoriae,
independenter a fasciculo DLL vel functione terminandi electa. Sequentia
"`GetStdHandle` deinde alia functio non-terminans (`GetLastError`)" numquam
defecit. Causa radicalis non inventa est; suspicio est peculiaritatem huius
ambitus Wine specificam esse (nullum consolam veram habentis), non errorem
in ipsa constructione PE. **Non probatum sub Windows vero.** Propterea
fasciculi hic inclusi terminationem sine `GetStdHandle` praecedente
demonstrant tantum.

## Probationes exsecutae

Omnes hae probationes vere exsecutae sunt, non solum scriptae:

- `construe_pe_vindex.vindex` compilatum per `compilator_vindex` (ELF),
  exsecutum, `exemplum_salve.exe` scriptum: **RECTE**.
- `exemplum_salve.exe` sub Wine 9.0 exsecutum, output textus correctus,
  codex exitus 45 (valor programmate definitus): **RECTE**.
- Repetitio quinquies consecutiva, idem resultatum: **RECTE, deterministicum**.

## Proximi gradus proposti

**Nota (post collationem cum `chatgpt/vindex-053-compilator-dynamicus`, caput
`a00a388`)**: consilium mutatum est. Limes centum symbolorum localium iam
remotus est ibi — probatum a nobis independenter: programma CLXXX
variabilium localium recte compilatum et exsecutum est per compilatorem ibi
distributum, reservatione pilae parva et tuta (11456 octeta, non 7000000).
Migratio functionum/vocationum pendentium adhuc in cursu est, cum erroribus
visibilibus similibus illis supra notatis (§2). Consilium igitur:

1. Non integrare hunc mechanismum PE in `compilator_vindex.vindex` statim,
   dum migratio functionum/vocationum pendentium in ramo 053 non stabilita est.
2. Postquam illa migratio finita erit, `CONSTRUE_CAPUT_PE` intra novam
   architecturam dynamicam definire, non intra veterem `tabula` fixam.
3. Eligere modum quo lingua VINDEX scopum (ELF vel PE) designat — verbi
   gratia per argumentum lineae mandatorum, non per grammaticam mutandam.
4. Extendere tabulam importationis ad `ReadFile`, `CreateFileA`,
   `VirtualAlloc`, necessaria ad functiones basicas RESERVA/APERI/LEGE sub
   Windows. Investigare prius defectum `GetStdHandle` notatum supra, ideo
   sub Windows vero, non solum Wine.
5. Verificare sub Windows vero (non solum Wine) antequam quisquam gradus
   pro definitivo habeatur.
