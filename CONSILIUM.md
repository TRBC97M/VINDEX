# CONSILIUM — Tabula Magistra Operum VINDEX et Sylviae

> **ARCHITECTURA est lex. CONSILIUM est via. Git historia est.**

## Munus

`CONSILIUM.md` est tabula operativa canonica VINDEX et Sylvia OS. `ARCHITECTURA.md` fines et principia statuit; hoc documentum statum praesentem, dependentias, curatores, prioritates et actiones proximas declarat.

Omnis collaborator ante opus novum debet:

1. `ARCHITECTURA.md` legere;
2. `CONSILIUM.md` legere;
3. recentissimum `main`, ramos, Pull Request et probationes inspicere;
4. opus ab alio curatore activum non duplicare;
5. mutationes maiores in ramo proprio facere et per Pull Request canonizare;
6. post mutationem significantem hanc tabulam renovare.

Si documentum et Git dissentiunt, **Git praevalet**; documentum deinde corrigendum est.

## Status

- `IDEA` — finis receptus, nondum definitus.
- `LONGINQUUM` — finis canonicus diuturnus.
- `PARATUM` — opus definiri satis potest ut incipiatur.
- `ACTIVUM` — opus nunc exercetur.
- `RESERVATUM` — alius curator opus active tenet; ne duplicetur.
- `IMPEDITUM` — dependentia impedit.
- `PROBATUM` — demonstratum, nondum canonice integratum.
- `CANONIZANDUM` — probatum et in `main` portandum.
- `PERFECTUM` — in `main` integratum et probationibus munitum.

---

# I. Prioritates praesentes

## P1 — UEFI VINDEX purum

**Status:** `RESERVATUM / ACTIVUM / PROBATUM`  
**Curator:** Claude  
**Pull Request:** #82  
**Ramus:** `claude/uefi-vindex-purus`

### Iam demonstratum

- target UEFI a compilatore VINDEX generatus;
- PE32+ subsystem EFI sine importationibus Win32 in experimento;
- vocationes firmware ex VINDEX;
- GOP et framebuffer veri sub QEMU/OVMF;
- pictura directa in framebuffer;
- `SALI_AD` et translatio imperii;
- lectio nuclei ex disco;
- catena experimentalis `PONTOK` → `NUCLEUS VIVIT`;
- correctio commentariorum `//` in experimento;
- auto-hospitium experimentale servatum.

### Quod nondum declaratur perfectum

Nucleus Sylviae realis adhuc contractum memoriae proprium requirit. Probatio experimentalis indicat imaginem nuclei memoriam magnam continuatam postulare quam firmware non necessario concedit. Itaque ponticulus C canonicus nondum tollitur solum quia experimentum VINDEX ulterius processit.

### Regula coordinationis

**Nullum opus parallelum in P1 faciendum est donec usor dicat Claudium opus terminavisse aut relinquere.** Cum id acciderit, recentissimi commits et ipsa PR #82 denuo inspiciantur ante ullam integrationem.

### Criterium victoriae

Firmware UEFI → applicatio EFI a VINDEX canonico generata → nucleus Sylviae realis → metadata et memoria rite contracta → framebuffer et initium fundamentale, sine runtime C, sub CI QEMU/OVMF repetibili.

---

## P2 — Reconciliatio VINDEX 0.53 in lineam canonicam

**Status:** `PERFECTUM R0–R5`; `R6 RESERVATUM a P1`.

### Perfectum

- R0 — inventarium et matrix migrationis;
- R1 — allocationes dynamicae, functiones et frames amplae, septem argumenta SysV, punctum fixum;
- R2 — diagnostica `FONS / LINEA / COLUMNA / NUNTIUS`;
- R3 — `PROIECTUM`, viae relativae et targeta;
- R4 — PE/Win64, `argc/argv` et exsecutio sub Windows vero;
- R5 — instrumenta VINDEX ad PE et comparationem binariam;
- semantica `&&` / `||` cum aestimatione brevi postea canonizata per PR #98;
- suite regressionis hodierna canonizata per PR #99.

### R6

Harmonizatio UEFI manet pars P1. Non duplicetur.

### Criterium victoriae

Linea canonica retinet facultates probatas 0.53 sine monolitho historico et sine regressione ELF, Win64, auto-hospitii aut Sylviae.

---

## P3 — Catena Sylviae pura canonica

**Status:** `IMPEDITUM a P1`, sed fundamenta interna iam valida.

### Iam canonicum

- regula puritatis post initium firmware;
- custodia CI `Sylvia VINDEX purum`;
- nucleus et runtime novi in VINDEX;
- Fenestrale II Purus A–I in `main`;
- compositor, eventa, clientes et fenestrae VINDEX;
- probationes Fenestralis canonicae.

### Actio proxima

Post P1, una catena boot canonica a firmware usque ad Fenestrale componenda et sub QEMU/OVMF certificanda est.

### Criterium victoriae

Una imago Sylviae canonica bootat, initium, framebuffer, input fundamentale et Fenestrale VINDEX reale ostendit sine runtime C residente.

---

## P4 — Fenestrale II Purus

**Status:** `PERFECTUM` pro gradibus A–I.

### Canonizatio perfecta

Gradus reconciliati sunt per PR:

- A — #87;
- B — #88;
- C — #90;
- D — #92;
- E — #93;
- F — #94;
- G — #95;
- H — #96;
- I — #97.

### Facultates actuales

- superficies clientium;
- eventa per codam;
- registrum dynamicum clientium;
- registrum dynamicum fenestrarum;
- focus et ordo Z;
- motus et resize;
- minimizatio, maximizatio, restitutio et clausura;
- taskbar dynamica;
- compositio ab ima ad summam;
- probatio runtime **LXXX fenestrarum**.

Vetus pila PR #32, #33 et #59–#65 clausa est et auctoritatem praesentem non habet.

### Actio futura

Post catenae boot stabilitatem: thema, widgeta, typographia, iconographia, input maturior et intentio visualis canonica.

---

## P5 — Mus PS/2 VINDEX nativus

**Status:** `PROBATUM / CANONIZANDUM`  
**Pull Request laboratorii:** #71

PR #71 probat sub QEMU/OVMF desktop, textum et murem PS/2 VINDEX nativum. Basis eius historica est; **non wholesale mergeatur**.

### Actio proxima

Post P1/P3, mechanismus utilis selective in catena canonicam Fenestralis portetur et recertificetur.

### Criterium victoriae

Cursor et eventa muris in Sylvia canonica sub QEMU/OVMF moventur sine runtime C.

---

## P6 — Officina VINDEX

**Status:** `PERFECTUM` pro fundamento Windows nativo canonico.

PR #57 est historia. PR #83 Officinam selective in `main` portavit et sub Windows vero certificavit.

### Iam canonicum

- applicatio Windows nativa;
- nulla technologia HTML/CSS/JavaScript;
- projecta `PROIECTUM`;
- arbor fasciculorum;
- tabulae editoris;
- coloratio syntaxeos;
- save/build/run;
- output integratum;
- diagnostica navigabilia;
- creatio novi projecti;
- compilator VINDEX Win64 realiter adhibitus;
- probationes functionales Windows CI.

### Actio futura

Officina non est “finita”: amplianda est cum debugger, refactoring, exploratione symbolorum, package manager, build system maturiore et targetis pluribus.

---

## P7 — Probationes canonicae

**Status:** `PERFECTUM`.

PR #99 vetus harnais, qui BIOS/VGA/C/GTK historica requirebat, a contractu praesentis systematis separavit. PR #102 collectionem dynamicam `NUMERUS` ad eundem contractum regressionis addidit; PR #104 seriem dynamicam contiguam `NUMERUS` addidit; PR #105 segmenta mutuata zero-copy addit.

`make probatio` / `tests/run_tests.sh` nunc **XXVI probationes, nulla errata** exercet, inter quas:

- casus fundamentales linguae;
- diagnostica valida et invalida;
- auto-hospitium `G2 = G3`;
- identitas binarii canonici cum fonte;
- `&&` / `||` brevia;
- collectio dynamica `NUMERUS`;
- series dynamica contigua `NUMERUS`;
- segmenta mutuata `NUMERUS`;
- PE32+;
- puritas Sylviae;
- LXXX fenestrae;
- compilatio Fenestralis II Purus I.

Probationes Windows, Officina et UEFI proprias custodias CI habent.

---

## P8 — Purificatio repositorii

**Status:** `PERFECTUM` pro magnis ramis historicis iam reconciliatis; custodia continua manet.

### Regula

Historia non deletur ad speciem mundandam, sed PR apertae non debent vias mortuas quasi futuras repraesentare.

### PR apertae hodiernae relevantes

- **#82** — P1, UEFI VINDEX purum, reservata Claudio;
- **#71** — probatio laboratorii PS/2, fons selective canonizandus post P1/P3.

Ceterae veteres pilae Fenestrales et Officinae iam clausae sunt post canonizationem.

---

# II. VINDEX ut lingua universalis

## P9 — Fundamenta typorum et structurae programmatis

**Status:** `ACTIVUM per incrementa`, dum P1 alienum opus manet.

**Finis:** VINDEX non solum lingua nuclei esse debet. Prima strata universalitatis debent programmata magna facilius et tutius exprimere sine libertate basimi gradus minuenda.

### Iam canonicum

- PR #102 — prima collectio dynamica generalis `NUMERUS`, tota VINDEX scripta, cum creatione, additione, lectione, mutatione, deletione, purgatione et liberatione;
- PR #104 — series dynamica contigua `NUMERUS`, cum longitudine et capacitate separatis, relocatione automatica, insertione, deletione et basi contigua ad futuras series/slices praeparanda;
- PR #105 — segmenta mutuata `NUMERUS`, cum basi et longitudine, accessu mutabili zero-copy et subsegmentis sine copia; relationes vitae memoriae et invalidatio post relocationem explicite documentantur;
- regressiones collectionum et segmentorum inclusae in probationibus canonicis XXVI/XXVI;
- nulla generica ficta ante facultatem linguae: abstractiones concretae `NUMERUS` fundamentum migrationis futurae praebent.

### Facultates candidatae

- numeri dimensionibus et signis clare definitis;
- fluitantia maturiora;
- arrays, slices et acus divitiores;
- structurae / `FORMA` maturiores;
- uniones et enumerationes;
- functiones ut valores et callback;
- moduli et compilationes separatae;
- contractus ABI expliciti;
- textus et Unicode maturior.

### Disciplina

Una facultas parva simul. Quaelibet mutatio linguae debet auto-hospitium, punctum fixum, regressionem propriam, ELF et Win64 ubi pertinens custodire.

---

## P10 — Abstractiones alti gradus

**Status:** `LONGINQUUM`.

Post P9:

- generica;
- interfaces / traits vel mechanismus VINDEX proprius;
- collectiones standardes;
- errores/resultata;
- destructio determinata;
- ownership aut alia disciplina memoriae optativa;
- closures et lambda;
- concurrentia, atomica et async;
- SIMD;
- introspectio et metaprogrammatio moderata.

**Principium:** nulla facultas alti gradus runtime obligatoriam omnibus programmatibus imponat.

---

## P11 — Ecosystema universale

**Status:** `LONGINQUUM`.

Componentes destinati:

- compilator officialis `vindex`;
- coniunctor/linker;
- bibliotheca standardis;
- debugger;
- profiler;
- formatter et linter;
- systema projectuum/build;
- praepositus fasciculorum;
- Officina;
- targeta Sylvia, Windows, ELF-systemata, UEFI, ARM64, WebAssembly et alia ubi ratio permittit.

**Criterium diuturnum:** nullum genus programmatis rationabile extra fines VINDEX sit.

---

# III. Sylvia ut systema usus cotidiani

## P12 — Infrastructura gubernatorum

**Status:** `LONGINQUUM`, post P3.

Strata requisita:

- PCI/PCIe;
- ACPI;
- USB;
- HID;
- I2C;
- interruptiones;
- MMIO et portus;
- DMA;
- firmware loading;
- registrum apparatus;
- contractus gubernatorum.

---

## P13 — Machina referentiae physica

**Status:** `LONGINQUUM`.

Prima candidata: **CHUWI HeroBook Air**. Exacta identificatio Hardware IDs ante implementationem necessaria est.

Mappa desiderata:

boot → display → keyboard → mouse/touchpad → SSD → USB → ACPI/battery → audio → Wi-Fi → Bluetooth → webcam → HDMI → acceleratio graphica.

---

## P14 — Rete Sylviae

**Status:** `LONGINQUUM`, dependet a gubernatoribus.

Strata:

NIC/Wi-Fi → Ethernet/802.11 → ARP/NDP → IPv4/IPv6 → ICMP → UDP → TCP → DHCP → DNS → TLS.

Criterium initiale: programma VINDEX in Sylvia nomen interretiale resolvit et HTTPS verificatum aperit.

---

## P15 — Navigator Sylviae

**Status:** `LONGINQUUM`, dependet a Fenestrale, P9/P10 et P14.

Gradus:

1. URL + HTTP(S) + HTML + CSS fundamentalis + textus + nexus + scroll;
2. imagines, formae, cookies, historia, downloads, cache;
3. layout modernior, fontes, flexbox/tabulae;
4. JavaScript VINDEX proprius vel mechanismus nativus congruus.

Chromium non est fundamentum necessarium neque finis architectonicus.

---

## P16 — Forma visualis Sylviae

**Status:** `PARATUM post catenae boot stabilitatem`.

Consilia visualia sunt destinatio realis, non picturae decorativae. Fenestrale technicum debet paulatim accipere:

- widgeta;
- thema;
- typographiam;
- margines et proportionem;
- iconographiam;
- cursorem et status interactionis;
- taskbar et menus canonicos;
- scaling et resolutiones modernas.

**Sylvia hodierna est ossa constructionis, non facies finalis.**

---

# IV. Regula coordinationis agentium

- Opus P1 a Claudio reservatum manet donec usor aliter dicat.
- Alius agens potest interim P9, documenta, probationes aut alia opera vere independentia exercere.
- Ramus experimentalis prosperus non wholesale mergeatur si structuram veterem secum trahit.
- Mutationes in `main` fiant per PR parvas, probatas et reversibiles.
- Documenta repositorii tantum Lingua Latina utantur.
- Status realis Git semper ante opinionem veterem praevalet.

---

# V. Actio proxima dum P1 reservatum est

Dum Claude P1 exercet, via recta independentis progressionis est:

1. documenta canonica statui hodierno congruentia servare;
2. probationes 26/26 custodire;
3. **P9 per incrementa parva et generalia continuare**, non per magnam mutationem simul;
4. ubi Claude terminaverit, opus P1 denuo inspicere ante integrationem.

---

# VI. Sententia

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

**Nullum genus programmatis extra fines VINDEX esse debet.**