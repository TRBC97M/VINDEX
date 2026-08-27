# VINDEX — Lingua universalis in constructione

> **VINDEX Latine cogitat. Sylvia Latine loquitur.**

VINDEX est lingua programmationis generalis, vocabulario Latino, quae a basimo gradu usque ad applicationes magnas crescere destinatur.

Meta non est tantum C imitari aut C++ aequare. **Nullum genus programmatis extra fines VINDEX esse debet.** VINDEX tandem firmware, nucleos, gubernatores, applicationes graphicas, instrumenta evolutionis, ludos, servitores, rete, computationem scientificam et alia programmata exprimere debet.

Haec destinatio tamen a statu praesentis implementationis distinguitur. Hoc documentum quid **hodie canonicum et probatum** sit describit.

---

# I. Ubi codex canonicus est

Directorium principale huius lineae est:

```text
Vindex Chat-GPT/vindex_final_v51/
```

Nomen directorii est historicum. Non significat omnia quae ibi hodie canonica sunt ad facultates veteris 0.51 limitari.

Documenta totius repositorii:

- `ARCHITECTURA.md` — leges architectonicae VINDEX et Sylviae;
- `CONSILIUM.md` — status operum et prioritates;
- `documenta/vindex/` — contractus et relationes linguae;
- `documenta/sylvia/` — Fenestrale et Sylvia;
- `.github/workflows/` — certificationes canonicae.

---

# II. Compilator

Compilator canonicus est:

```text
compilator_vindex
```

Fons eius est:

```text
src/compilator_vindex.vindex
```

Compilator ipse VINDEX scriptus est et auto-hospitium ad punctum fixum exercetur.

## ELF64

```bash
./compilator_vindex programma.vindex programma
chmod +x programma
./programma
```

Aut per interfaciem publicam:

```bash
./vindexc programma.vindex -o programma
./programma
```

`vindexc` verificat fontem, exitum temporarium construit, formam ELF inspicit et productum atomice publicat.

## PE32+ Win64

```bash
./compilator_vindex programma.vindex programma.exe pe
```

Backend Win64 non solum structuram PE generat: probationes CI producta sub **Windows vero** exsequuntur.

## UEFI

```bash
./compilator_vindex programma.vindex programma.efi uefi
```

Target UEFI VINDEX purus est canonicus per PR #109. Compilator generat PE32+ EFI application sine importationibus Win32. Catena dedicata QEMU/OVMF probat non solum structuram fasciculi, sed boot realem usque ad framebuffer Sylviae.

Primitiva basimi gradus `SALI_AD(expressio)` imperium sine reditu ad sedem datam transfert. Vocationes firmware UEFI per contractum VINDEX proprium exercentur.

---

# III. Exemplum minimum

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    PROCLAMA "Salve, mundus!".
    REDDE 0.
FIN-FUNCTIO.
```

VINDEX iam exercet, inter alia:

- numeros integros et fluitantia;
- variabiles locales et globales;
- functiones, recursionem et reditum `TEXTUS`;
- argumenta functionum et ABI probata;
- acus et memoriam directam;
- `FORMA` et structuras memoriae;
- ordines, collectiones, series et segmenta;
- `TEXTUS` dynamicum UTF-8;
- validationem UTF-8 strictam et scalaria Unicode;
- subtextum Unicode per limites scalarum;
- importationes;
- I/O fundamentalem;
- `argc/argv`;
- projecta `PROIECTUM`;
- ELF64;
- PE32+ Win64;
- PE32+ UEFI;
- diagnostica cum fonte, linea, columna et nuntio;
- `&&` et `||` cum aestimatione brevi vera;
- `&` et `|` ut operationes bitariae separatae;
- commentaria `//` etiam intra corpora functionum.

Haec enumeratio non est promissio plenitudinis C aut C++; VINDEX adhuc lingua in constructione est.

---

# IV. Operatores logici

`&&` et `||` sunt operatoria logica cum **aestimatione brevi**.

```vindex
SI acus != 0 && CONTENTUM(acus + 48) == 7 TUNC
    PROCLAMA "RECTE".
FIN-SI.
```

Si `acus == 0`, pars dextra non aestimatur.

Prioritas canonica est:

```text
comparatio → && → ||
```

`&` et `|` operationes bitariae manent.

Contractus plenior est in `documenta/vindex/LOGICA_BREVIS.md`.

---

# V. Auto-hospitium

Probatio puncti fixi:

```bash
make auto-hospitium
```

Aut manualiter:

```bash
./compilator_vindex src/compilator_vindex.vindex /tmp/g2
chmod +x /tmp/g2
/tmp/g2 src/compilator_vindex.vindex /tmp/g3
cmp /tmp/g2 /tmp/g3
```

Catena canonica requirit:

```text
compilator versionatus = G2 = G3
```

Bootstrap Python vetus manet historia et testimonium originis; non est via ordinaria qua VINDEX hodiernus evolvitur.

---

# VI. Probationes

Suite localis canonica:

```bash
make probatio
```

Aut:

```bash
./tests/run_tests.sh
```

Status hodiernus:

```text
XXIX probationes rectae; nulla errata.
```

Suite exercet:

- `Salve`;
- calculum et fluitantia;
- importationes;
- formas et acus;
- recursionem;
- argumenta processūs;
- diagnostica reiectionis;
- auto-hospitium;
- logicam brevem;
- collectiones, series et segmenta `NUMERUS`;
- UTF-8, scalaria Unicode, reditum `TEXTUS` et subtextum Unicode;
- PE32+;
- puritatem absolutam Sylviae;
- LXXX fenestras Fenestralis;
- compilationem Fenestralis II Purus I.

Probationes quae vetus BIOS/VGA, `rectores.S`, pontes C/GTK aut Officinam GTK examinant sunt testimonia architecturae historicae, non contractus praesentis systematis nisi iterum expresse canonizentur.

Windows, Officina et UEFI habent probationes CI dedicatas ubi machina vel firmware speciale requiritur.

---

# VII. PROIECTUM

VINDEX potest projecta per manifestum `PROIECTUM` tractare. Viae relativae et destinationes ELF/PE sunt pars lineae reconciliatae et probationibus muniuntur.

Exempla projectuum probatorum sunt sub:

```text
tests/proiecta/
```

Officina eodem contractu utitur.

---

# VIII. Officina VINDEX

Officina canonica hodierna est applicatio **Windows nativa**, portata in `main` per PR #83.

Ea praebet:

- arborem projecti;
- tabulas editoris;
- colorationem syntaxeos;
- aperire et servare;
- build;
- run;
- tabulam output;
- diagnostica navigabilia;
- creationem novi projecti VINDEX.

Officina canonica non utitur HTML, CSS aut JavaScript. Workflow Windows aedificat Officinam, generat compilatorem Win64 VINDEX, projecta PE construit atque exsequitur et diagnostica realia probat.

Fons est in radice repositorii: `officina/`.

Officina GTK/C vetus servatur tantum ut historia in locis hereditatis; non est Officina canonica praesentis lineae.

---

# IX. Sylvia OS

Sylvia et VINDEX sunt duo projecta primi ordinis:

- VINDEX non dependet a Sylvia;
- Sylvia VINDEX ut linguam principalem adhibet;
- necessitates reales Sylviae saepe defectus generales VINDEX detegunt.

Regula absoluta est:

> **Catena canonica Sylviae, etiam initium UEFI, VINDEX pura esse debet.**

Custodia CI hanc regulam sine exceptione C tuetur.

## Fenestrale II Purus

Gradus A–I sunt iam canonice in `main` reconciliati.

Fenestrale hodiernum habet superficies clientium, codam eventuum, registra dynamica clientium et fenestrarum, focus, ordinem Z, motum, resize, minimizationem, maximizatio/restitutionem, clausuram, taskbar dynamicam et compositionem plurium fenestrarum.

Probatio runtime **LXXX fenestras** creat et administrat. Sylvia igitur non amplius architectonice ad paucos locos fixos clauditur.

## Forma visualis

Aspectus hodiernus est fundamentum technicum, non destinatio finalis. Consilia visualia futura in widgeta, thema, typographiam, iconographiam, scaling, menus et interactiones reales Fenestralis convertenda sunt.

---

# X. UEFI et boot Sylviae

PR #109 canonizat opus experimentale ex #82 selective supra `main` hodiernum. Catena probata est:

```text
OVMF → BOOTX64.EFI [VINDEX] → NUCLEUS [VINDEX] → FRAMEBUFFER → SYLVIA
```

Probatio automatica verificat:

- constructionem sine gcc, ld aut objcopy ad codicem UEFI;
- `NUCLEUS.BIN`, `TEXTUS.BIN` et `FORMA.BIN` in volumine FAT;
- mensuram nuclei per `GetInfo` sine limite II MiB;
- `PONTOK` post `SALI_AD`;
- absentiam exceptionis et defectus paginae;
- screendump 1280×800 non uniforme cum IX coloribus distinctis.

Vetus `bootstrap_uefi.c` et constructor C historicus e linea canonica remoti sunt.

ELF adhuc `p_memsz` magnum propter acervum fixum declarare potest. Ponticulus contractum hunc implementat; reformatio multi-`PT_LOAD` est debitum separatum.

---

# XI. PS/2

PR #71 est laboratorii probatio qua mus PS/2 VINDEX nativus sub QEMU/OVMF demonstratus est.

Ea PR vetere basi nititur et non directe in `main` fundenda est. Nunc P1 perfectum est, mechanismus selective in catenam P3 portandus et recertificandus est.

---

# XII. Quid nondum perfectum est

VINDEX iam lingua systemica vera incipiens est, sed nondum plenitudinem linguae universalis habet.

Inter futura fundamenta sunt:

- typi numerici pleniores;
- structurae, enumerationes et uniones maturiores;
- functiones ut valores et callback;
- compilationes separatae et moduli;
- generica;
- collectiones standardes generales;
- Unicode altius: graphemata et normalizatio;
- destructio determinata et disciplina memoriae;
- concurrentia et atomica;
- async;
- SIMD;
- optimizer;
- debugger;
- coniunctor/linker maturus;
- package manager;
- formatio ELF multi-`PT_LOAD` maturior;
- ARM64;
- WebAssembly.

Haec sunt **fines**, non facultates hodie falsas declarandae.

---

# XIII. Rete et Navigator

Destinatio Sylviae includit rete VINDEX nativum:

```text
gubernator → IPv4/IPv6 → UDP/TCP → DHCP/DNS → TLS → HTTP(S)
```

Postea navigator VINDEX proprius a fundamentis construi potest:

```text
HTTP(S) → HTML → CSS → layout → Fenestrale
```

JavaScript, multimedia et APIs moderniores post fundamenta addenda sunt. Chromium non est necessarius ut radix architectonica.

---

# XIV. Disciplina contributionis

Ante mutationem maiorem:

1. lege `ARCHITECTURA.md`;
2. lege `CONSILIUM.md`;
3. inspice recentissimum `main` et PR apertas;
4. noli opus `RESERVATUM` duplicare;
5. mutationem in ramo proprio fac;
6. adde probationem quae defectum vere deprehendit;
7. serva auto-hospitium ubi compilator mutatur;
8. per PR canoniza.

**Omnia documenta canonica repositorii Lingua Latina scribenda sunt.**

---

# XV. Versiones

Fasciculus `VERSION` et nonnulla nomina directoriorum historiam veteris distributionis adhuc servant. Facultates canonicae hodiernae iam ulterius progressae sunt per reconciliationes 0.52/0.53 et PR posteriores.

Numerus release non mutandus est fortuito tantum ad documenta recentiora imitanda. Versionatio publica separato actu deliberato reconcilianda est.

---

# XVI. Via hodierna

P1 non amplius reservatum est. Via principalis nunc bifurcatur sine contradictione:

- **P3:** boot UEFI purum cum Fenestrale II et input canonico coniungere, PS/2 ex #71 selective portando;
- **P9:** fundamenta universalia VINDEX per incrementa parva continuare;
- debitum ELF `PT_LOAD`/acervi fixi separatim solvere sine regressione targetorum.

Vide `CONSILIUM.md` pro statu exacto.

---

# XVII. Nomen

In iure Romano *vindex* erat qui alium defendebat vel libertati eius interveniebat. Nomen igitur libertatem, tutelam et dominium proprii instrumenti significat.

---

# XVIII. Sententia

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

**Nullum genus programmatis extra fines VINDEX esse debet.**
