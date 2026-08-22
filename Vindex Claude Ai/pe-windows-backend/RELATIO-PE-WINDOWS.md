# VINDEX — Fundamenta PE/Windows (RELATIO)

## Propositum

Explorare et probare mechanismum minimum necessarium ut VINDEX exsecutabilia
Windows nativa (formam PE64) generare possit, sine dependentia ab ELF, Wine
solum ad probationem adhibito (non ad exsecutionem finalem).

## Status honestus

Haec contributio praebet **mechanismum probatum et functionalem**, non
**integrationem completam in compilatorem**. Res distinguendae sunt:

1. **Quod functionat, verificatum sub Wine 9.0**: constructio manualis capitis
   PE64 (DOS, PE, Optional Header, tabulae sectionum), tabula importationis
   multi-functionis (`kernel32.dll`), vocatio indirecta per IAT (`FF 15` +
   `call [rip+X]`), terminatio per `ExitProcess`. Praeterea, functiones I/O
   basicae — `VirtualAlloc`, `CreateFileA`, `WriteFile`, `ReadFile`,
   `CloseHandle` — omnes simul in una catena probatae (vide
   `construe_pe_io_referens.py`): memoria reservata, scripta directe, in
   fasciculum effusa, relecta, in secundum fasciculum rescripta — utrumque
   fasciculum idem contentum byte-pro-byte habet.
2. **Quod exploratum sed pendet a terminatione processus**: scriptio in
   consolam per `GetStdHandle` + `WriteFile`, et similiter tota catena I/O
   supra descripta — omnes operationes ipsae **recte** functionant (fasciculi
   scripti et relecti correcte), sed sequentia terminationis (`ExitProcess`)
   post quamvis vocationem quae HANDLE reddit causat defectum non plene
   explicatum sub Wine huius systematis probationis specifice (vide sectio
   "Difficultates", n. 3). Probatio horum fasciculorum igitur non ex
   terminatione ipsa pendet: rectitudo per contentum fasciculorum scriptorum
   post exsecutionem verificatur, non per codicem exitus.
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
- `construe_pe_io_referens.py` — extensio: catena completa I/O — `VirtualAlloc`
  (reservatio 4 KiB), scriptio directa in memoriam, `CreateFileA` + `WriteFile`
  (memoria in fasciculum effusa), `CreateFileA` + `ReadFile` (fasciculus
  relectus), `CreateFileA` + `WriteFile` iterum (secundus fasciculus
  verificationis). Generat `exemplum_io.exe` cum exsecutus est.
- `exemplum_io.exe` — exemplar generatum, 1536 octeta. Verificatum sub Wine
  9.0: ambo fasciculi scripti (`proba_pe_io.txt`,
  `proba_pe_io_verificatio.txt`) idem contentum "ValAlloc PE!" (12 octeta)
  habent post exsecutionem, confirmante catenam integram recte functionare
  independenter a defectu terminationis notato supra.

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

**Nota correcta (post collationem cum capite `a00a388`, novissimo tunc
`chatgpt/vindex-053-compilator-dynamicus`)**: error notatus supra
(`"functio vocata non inventa est"`) proveniebat ex relatione diagnostica
intermedia (`RELATIO-PENDENTES-DIAGNOSTICA-053.md`, commit `65cbd5d`), non
ex statu finali. Caput `a00a388` ipsum — verificatum a nobis independenter,
non solum lectum — jam MCCL (1250) vocationes pendentes recte solvit: nostrum
proprium exemplum (1250 functiones definitione posteriore vocatae) recte
compilatum et exsecutum est, sine defectu, sine circulo infinito, codice
exitus recte reddito. Relatio officialis eiusdem capitis confirmat: 21/21
probationes rectae, punctum fixum G1=G2=G3 servatum, exitus programmate
definitus (777) recte redditus. Difficultas huius sectionis igitur **non
amplius manet in ramo 053**; relinquitur hic tantum ut exemplum genericum
categoriae defectuum quam mechanismus dynamicus removere debuit.

### 3. `GetStdHandle` sequitur terminatio processus (characterizatum, non solutum)

In experimentis privatis, sequentia "`GetStdHandle` (vel `CreateFileA`, vel
quaevis functio quae HANDLE reddit) deinde `ExitProcess` (vel
`RtlExitUserProcess`)" causavit defectum deterministicum sub Wine 9.0 huius
systematis probationis specifice — semper eodem loco memoriae,
independenter a fasciculo DLL vel functione terminandi electa. Sequentia
"`GetStdHandle` deinde alia functio non-terminans (`GetLastError`)" numquam
defecit.

**Diagnosticum praecisius (per `WINEDEBUG=+relay`)**: filum quod
`ExitProcess` vocat correcte perficit **omnes tres** vocationes
`DllMain(PROCESS_DETACH)` exspectatas — pro `kernel32.dll`, `kernelbase.dll`,
et `ntdll.dll`, singulis recte redditis (`retval=1`) — deinde **nihil amplius
a filo illo in relatione relais apparet**: nulla ulterior vocatio API
tracta, tantum defectus memoriae. Hoc indicat defectum non esse in codice
DllMain ipso (qui recte perficitur), sed in codice Wine interno et **non
tracto** post has tres vocationes.

**Diagnosticum ulterius praecisum (per `strace -f` in ipso systemate Linux
subiacenti)**: signum verum non est `SIGSEGV` communis (`SEGV_MAPERR` vel
`SEGV_ACCERR` cum adresse fallente reali), sed `si_code=SI_KERNEL` cum
`si_addr=NULL`. Documentatio nuclei Linux confirmat: haec combinatio
praecise indicat **General Protection Fault** (#GP), non defectum paginae
(#PF) — categoria omnino differens, typice ex instructione **privilegiata**
vel **violatione alignationis stricti** exsecuta in modo utente (ring 3).

**Instructio praecisa identificata (per GDB directe in processu Wine)**:
`movdqa %xmm6, 0x60(%rcx)` — instructio SSE quae **alignationem 16 octetorum
strictam** requirit pro destinatione memoriae. Valor realis `RCX` erat
`0x11fd18`; `(RCX + 0x60) mod 16 = 8`, non `0` — destinatio male alignata
octo octetis, causa directa et mathematicae confirmata #GP. Codex circa
hanc instructionem (`movdqa %xmm6..%xmm15` in serie, offsets `0x60`
usque `0xf0`) est classicum exemplar routinae quae registra XMM in
structuram CONTEXT servat — verisimiliter pars routinae internae quae
statum CPU servat circa transitiones PE-ad-Unix.

**Fons routinae identificatus**: adresse quae hanc instructionem vocat
(secundus gradus stack-tracei) cadit tantum `0x1696` octeta post
`__wine_unix_call` — mechanismum centralem quo Wine omnes vocationes API
(PE-side) ad implementationem realem Unix-side transfert. Hoc perfecte
congruit cum natura defectus: quaevis vocatio realis Win32 (`CreateFileA`,
`GetStdHandle`, `WriteFile`...) hoc pontem transit, qui statum CPU servare
debet pro transitione.

**AMPLIFICATIO MAGNA (per probationem `CreateProcessA`)**: probatio
additionalis — `CreateProcessA(NULL, "cmd.exe /c exit 42", ...)` — causavit
**eundem defectum** (`movdqa %xmm6, 0x60(%rcx)`), sed haec vice Wine ipse
(aedificatio habens symbola debug pro `kernelbase.dll` specifice, non pro
`ntdll.dll`) praebuit **nomina functionum et locos fontis exactos**:

```text
0  0x...4f464b in kernelbase (+0x8464b)
1  FindClose+0x45(handle=0x0) [dlls/kernelbase/file.c:1580] in kernelbase
2  GetLongPathNameW+0x2f0(shortpath=L"C:\windows\system32\cmd.exe",
   longpath=0x0, longlen=0x11fb00) [dlls/kernelbase/file.c:2122]
3  create_process_params+0x27(...) [dlls/kernelbase/process.c:150]
4  CreateProcessInternalW+0x176(...) [dlls/kernelbase/process.c:564]
5  CreateProcessInternalA+0x195(...) [dlls/kernelbase/process.c:496]
6  CreateProcessA+0x5c(...) [dlls/kernelbase/process.c:693]
```

`cmd.exe` **existit** realiter in hoc praefixo Wine (verificatum:
`/root/.wine/drive_c/windows/system32/cmd.exe`, 1762230 octeta) — defectus
igitur non pendet a fasciculo desiderato absente. `FindClose` vocatur cum
`handle=0x0` intra `GetLongPathNameW`, quae internum `FindFirstFileW`/
`FindNextFileW` adhibet ad nomen longum resolvendum — et haec, sicut
`CreateFileA`/`GetStdHandle`, per `__wine_unix_call` pontem transit.

**Conclusio ampliata**: defectus non est proprius sequentiae specificae
"HANDLE deinde terminatio", sed generalior — quaevis **pluralitas
vocationum sequentialium** per `__wine_unix_call` (sive `CreateFileA` +
`ExitProcess`, sive `FindFirstFileW`-interna + `FindClose`-interna intra
`CreateProcessA`) potest hunc defectum eodem mechanismo (context-save
male alignatum) provocare, in hac aedificatione Wine 9.0 sub hoc ambitu
specifico. Habemus nunc non tantum instructionem exactam, sed **nomina
functionum Wine et locos fontis exactos** (`dlls/kernelbase/file.c:1580`,
`:2122`) — sufficiens ut quisquis fontem Wine correspondentem habet
possit radicem ultimam persequi.

**Hypothesis prima reiecta (documentata ad memoriam methodi)**: codicem
post `HLT` proprium (rete securitatis) forte attingi, et ipsum HLT
(instructio etiam privilegiata) causam esse — **directe probata et
reiecta**: `HLT` in fasciculo compilato per `EB FE` (`jmp $`, non
privilegiata) substitutum est, defectus idem mansit. Confirmat: defectus
totus intra Wine ipsum accidit, antequam ullum control ad nostrum codicem
redeat.

**RADIX ULTIMA INVENTA (per fontem Wine 9.0 realem, `dlls/kernelbase/file.c:1580`
et `include/wine/exception.h`)**: linea 1580 est `__EXCEPT_PAGE_FAULT` —
**verum blocum SEH x86-64** (`__except`), definitum in fonte Wine ipso ut:

```c
#define __EXCEPT_PAGE_FAULT __EXCEPT_HANDLER(__wine_exception_handler_page_fault)
```

`FindClose` continet blocum `__TRY { ... si (handle malus) info->magic
accedit ... } __EXCEPT_PAGE_FAULT { WARN(...); return FALSE; } __ENDTRY` —
consilium est: si accessus ad structuram interna per handle malum **veram**
faultam paginae (#PF) causat, hoc SEH blocum eam **gratiose** capere et
`FALSE` reddere debet. Sed capere hanc faultam requirit machinam completam
SEH x86-64 (tabulas unwind, `RtlUnwind`, dispatch exceptionis, **captura et
restitutio contextus CPU completi, registris XMM inclusis**) — **exactam
routinam ubi defectus noster latet**.

**Conclusio definitiva**: hic non est defectus in constructione PE nostra,
neque proprius uni functioni. Est **defectus in machina propria SEH x86-64
Wine 9.0** huius aedificationis (`9.0~repack-4build3`, Ubuntu) sub hoc
ambitu Linux/continentis specifico: quotienscumque codex internus Wine
vere **capere** debet exceptionem/faultam paginae per `__except` (sicut
`FindClose` erga handle malum, vel verisimiliter codex terminationis
processus erga cleanup), **ipsa machina captationis** (context-save per
`movdqa` in registra XMM) accedit ad buffer male alignatum octo octetis,
causans #GP **secundariam et non captam** — pro #PF **primaria et
captanda** quam codex expectabat. Investigatio nunc **finita** est: causa
radicalis identificata usque ad mechanismum architecturalem exactum
(SEH dispatch context-save), verificata per fontem Wine realem, non
tantum suspicata. **Non probatum sub Windows vero** — defectus
verisimiliter Wine/continenti-specificus est, non error in ipsa
constructione PE nostra (quae, per omnes probationes hic relatas,
correcte functionat). Propterea fasciculi hic inclusi terminationem sine
tali functione praecedente demonstrant tantum, vel — pro catena I/O —
rectitudinem per contentum fasciculorum post exsecutionem verificant,
non per exitum limpidum processus.

## Probationes exsecutae

Omnes hae probationes vere exsecutae sunt, non solum scriptae:

- `construe_pe_vindex.vindex` compilatum per `compilator_vindex` (ELF),
  exsecutum, `exemplum_salve.exe` scriptum: **RECTE**.
- `exemplum_salve.exe` sub Wine 9.0 exsecutum, output textus correctus,
  codex exitus 45 (valor programmate definitus): **RECTE**.
- Repetitio quinquies consecutiva, idem resultatum: **RECTE, deterministicum**.

## Proximi gradus proposti

**Nota (post collationem cum `chatgpt/vindex-053-compilator-dynamicus`, caput
`a00a388`)**: limes centum symbolorum localium iam remotus est ibi — probatum
a nobis independenter: programma CLXXX variabilium localium recte compilatum
et exsecutum est per compilatorem ibi distributum, reservatione pilae parva
et tuta (11456 octeta, non 7000000). Migratio functionum/vocationum
pendentium **etiam finita est** in eodem capite — probatum a nobis
independenter: 1250 vocationes pendentes recte compilatae et exsecutae, sine
defectu. Relatio officialis confirmat praeterea 21/21 probationes rectas et
punctum fixum servatum. Consilium igitur manet idem quantum ad tempus
integrationis (adhuc melius exspectare aliquam stabilitatem post tot
mutationes recentes simul), sed causa specifica mutata est:

1. Non integrare hunc mechanismum PE in `compilator_vindex.vindex` statim.
   Ratio praecisa mutata est: tabula locorum et tabula functionum/vocationum
   pendentium jam dynamicae et stabiles sunt (probatum a nobis). Restat
   tamen in cursu ordinis diei 053 — expresse notatum ibi — quaestio magnitudinis
   fixae fasciculorum pilae (stack frame) per functionem; haec quaestio
   distincta est ab illis duabus jam solutis, et directe pertinet ad
   fovea custodiae pilae hic in §1 notata. Melius igitur exspectare illam
   quoque, ut integratio PE super fundamentum vere completum aedificetur.
2. Postquam illa quoque stabilita erit, `CONSTRUE_CAPUT_PE` intra novam
   architecturam dynamicam definire, non intra veterem `tabula` fixam.
3. Eligere modum quo lingua VINDEX scopum (ELF vel PE) designat — verbi
   gratia per argumentum lineae mandatorum, non per grammaticam mutandam.
4. Extendere tabulam importationis ad `ReadFile`, `CreateFileA`,
   `VirtualAlloc`, necessaria ad functiones basicas RESERVA/APERI/LEGE sub
   Windows. Investigare prius defectum `GetStdHandle` notatum supra, ideo
   sub Windows vero, non solum Wine.
5. Verificare sub Windows vero (non solum Wine) antequam quisquam gradus
   pro definitivo habeatur.
