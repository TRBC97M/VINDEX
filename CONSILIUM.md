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

**Status:** `PERFECTUM per PR #109`  
**Origo experimentalis:** PR #82, ramus `claude/uefi-vindex-purus`  
**Canonizatio:** portus selectivus super `main` hodiernum

### Canonice probatum

- target `uefi` a compilatore VINDEX generatus;
- PE32+ subsystem EFI sine importationibus Win32;
- vocationes firmware UEFI directe ex VINDEX;
- commentaria `//` intra functiones canonice tractata;
- `SALI_AD` et translatio imperii;
- lectio nuclei ex disco per `GetInfo`, sine limite II MiB;
- `NUCLEUS.BIN`, `TEXTUS.BIN` et `FORMA.BIN` vere in volumine FAT;
- contractus memoriae nuclei explicitus et a ponticulo impletus;
- GOP et framebuffer veri sub QEMU/OVMF;
- `PixelsPerScanLine` ex offset canonico +32;
- nulla exceptio, nullus defectus paginae post saltum;
- screendump 1280×800 cum IX coloribus distinctis;
- Sylvia vere in framebuffer pingit;
- auto-hospitium `compilator canonicus = G2 = G3`;
- XXIX/XXIX probationes canonicae cum mutationibus UEFI integratis;
- catena repetibilis:

```text
OVMF → BOOTX64.EFI [VINDEX] → NUCLEUS [VINDEX] → FRAMEBUFFER → SYLVIA
```

Vetus `bootstrap_uefi.c` et constructor C e linea canonica removentur. Custos puritatis nullam exceptionem C amplius admittit.

### Debitum separatum

ELF adhuc acervum ad sedem fixam collocat; id `p_memsz` circiter XLVI MiB etiam pro binariis parvis efficere potest. Ponticulus UEFI hunc contractum recte implet per reservationes frustatim, ergo P1 non impeditur. Reformatio multi-`PT_LOAD` vel relocatio acervi opus architectonicum separatum est.

### Criterium victoriae

**Perfectum:** firmware UEFI → applicatio EFI VINDEX → nucleus Sylviae realis → metadata et memoria rite contracta → framebuffer → pictura Sylviae, sine C, sub CI QEMU/OVMF repetibili.

---

## P2 — Reconciliatio VINDEX 0.53 in lineam canonicam

**Status:** `PERFECTUM R0–R6`.

### Perfectum

- R0 — inventarium et matrix migrationis;
- R1 — allocationes dynamicae, functiones et frames amplae, septem argumenta SysV, punctum fixum;
- R2 — diagnostica `FONS / LINEA / COLUMNA / NUNTIUS`;
- R3 — `PROIECTUM`, viae relativae et targeta;
- R4 — PE/Win64, `argc/argv` et exsecutio sub Windows vero;
- R5 — instrumenta VINDEX ad PE et comparationem binariam;
- R6 — target UEFI purus, vocationes firmware, `SALI_AD` et catena QEMU/OVMF canonizata per P1/#109;
- semantica `&&` / `||` cum aestimatione brevi per PR #98;
- suite regressionis praesentis per PR #99 et incrementa posteriora.

### Criterium victoriae

Linea canonica retinet facultates probatas 0.53 sine monolitho historico et sine regressione ELF, Win64, UEFI, auto-hospitii aut Sylviae.

---

## P3 — Catena Sylviae pura canonica

**Status:** `PERFECTUM per PR #111`.

### Canonice probatum per #111

- boot UEFI VINDEX purus usque ad Fenestrale II Purus;
- `NUCLEUS_FONS` sinit Fenestrale II ut payload canonicum eiusdem ponticuli construi;
- Fenestrale II rectorem PS/2 VINDEX nativum directe consumit;
- input PS/2 ante claviaturam firmware pollitur, protocollis UEFI ut fallback retentis;
- initium PS/2 `09 FA FA` sub QEMU/OVMF confirmatum;
- VI fasciculi muris in Fenestrale recepti;
- framebuffer Fenestralis post motum muris re-pingitur;
- resolutio 1280×800 et signa colorum Fenestralis realia probantur;
- XXXIX colores significativi in captura Fenestralis;
- CXII pixeli post motum PS/2 mutati;
- catena historica nuclei simul sine regressione custoditur;
- nulla exceptio CPU, nullus defectus paginae, nullum C in runtime;
- custodia UEFI permanens utramque catenam exercet.

Catena P3 canonica:

```text
OVMF → BOOTX64.EFI [VINDEX] → FENESTRALE II [VINDEX] → PS/2 [VINDEX] → FRAMEBUFFER
```

### Correctio compilatoris inventa per P3

Structurae internae quibus campi in octetis definiuntur (`codex`, `contextus_parseris`, `descriptor*`) olim `ACUS<NUMERUS>` erant. Cum arithmetica acus typata recte per magnitudinem elementi multiplicet, offset `+8` in +64 octeta vertebatur. Allocationes `mmap` separatae vitium occultaverant.

#111 addressa harum structurarum ad `NUMERUS` cruda convertit, semanticam verarum `ACUS<NUMERUS>` intactam servat, ac `RESERVA_OCTETA` ELF ad acervum VINDEX nativum transfert. Auto-hospitium ad punctum fixum `G3 = G4` et XXIX/XXIX probationes hoc contractum muniunt.

### Criterium victoriae

**Perfectum:** una imago Sylviae canonica bootat, Fenestrale VINDEX reale ostendit et input fundamentale exercet sine runtime non-VINDEX residente. #111 in `main` canonizatum est.

---

## P4 — Fenestrale II Purus

**Status:** `PERFECTUM` pro gradibus A–I.

### Canonizatio perfecta

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

Post P3: thema, widgeta, typographia, iconographia, input maturior et intentio visualis canonica.

---

## P5 — Mus PS/2 VINDEX nativus

**Status:** `PERFECTUM per PR #110`  
**Origo laboratorii:** PR #71, nunc historia clausa

### Canonice probatum

- rector 8042 / PS/2 totus in VINDEX;
- mandata F6 et F4 cum ACK `FA`;
- fasciculi trium octetorum;
- AUX ante claviaturam firmware hauritur;
- cursor in catena UEFI canonica vere movetur;
- probatio QEMU: VI fasciculi, cursor `(160,100) → (274,140)`;
- MMMCLII pixeli mutati;
- nulla exceptio C in runtime.

#71 non mergitur wholesale; mechanismus utilis selective per #110 canonizatus est et per #111 Fenestrali II coniungitur.

### Criterium victoriae

**Perfectum:** cursor et eventa muris in imagine Sylviae canonica sub QEMU/OVMF moventur sine runtime C.

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

Officina amplianda est cum debugger, refactoring, exploratione symbolorum, package manager, build system maturiore et targetis pluribus.

---

## P7 — Probationes canonicae

**Status:** `PERFECTUM`.

PR #99 vetus harnais a contractu praesentis systematis separavit. Incrementa #102, #104, #105, #106, #107 et #108 collectiones, series, segmenta et `TEXTUS` maturaverunt. PR #109 addidit custodiam UEFI completam; #110 addidit probationem PS/2 nativam; #111 custodiam duplicem nuclei historici et Fenestralis II addidit.

`make probatio` / `tests/run_tests.sh` nunc **XXIX probationes, nulla errata** exercet, inter quas:

- casus fundamentales linguae;
- diagnostica valida et invalida;
- auto-hospitium `G2 = G3`;
- identitas binarii canonici cum fonte;
- `&&` / `||` brevia;
- collectio dynamica `NUMERUS`;
- series dynamica contigua `NUMERUS`;
- segmenta mutuata `NUMERUS`;
- `TEXTUS` cum validatione stricta UTF-8 et scalaribus Unicode;
- reditus `TEXTUS` a functionibus;
- subtextus Unicode per limites scalarum;
- PE32+;
- puritas absoluta Sylviae;
- LXXX fenestrae;
- compilatio Fenestralis II Purus I.

Custodia UEFI separata exsequitur QEMU/OVMF, screendump, PS/2 nuclei historici et Fenestrale II cum PS/2 nativo. Probationes Win64 et Officina sub Windows vero manent separatae.

---

## P8 — Purificatio repositorii

**Status:** `PERFECTUM` pro magnis ramis historicis reconciliatis; custodia continua manet.

### Regula

Historia non deletur ad speciem mundandam, sed PR apertae non debent vias mortuas quasi futuras repraesentare.

### PR pertinentes

- **#109** — canonizatio P1 ex opere #82, ad `main` hodiernum portata;
- **#82** — origo experimentalis UEFI, post #109 historia/supersessa;
- **#110** — canonizatio selectiva rectoris PS/2 nativi;
- **#71** — laboratorium PS/2, post #110 historia/supersessum et clausum;
- **#111** — coniunctio canonica Fenestralis II cum catena UEFI et PS/2.

Ceterae veteres pilae Fenestrales et Officinae iam clausae sunt post canonizationem.

---

# II. VINDEX ut lingua universalis

## P9 — Fundamenta typorum et structurae programmatis

**Status:** `ACTIVUM per incrementa`.

**Finis:** VINDEX non solum lingua nuclei esse debet. Prima strata universalitatis debent programmata magna facilius et tutius exprimere sine libertate basimi gradus minuenda.

### Iam canonicum

- PR #102 — collectio dynamica `NUMERUS`;
- PR #104 — series dynamica contigua `NUMERUS`;
- PR #105 — segmenta mutuata `NUMERUS` zero-copy;
- PR #106 — validatione UTF-8 stricta, numeratione scalarum Unicode et accessu ad scalare;
- PR #107 — functiones `TEXTUS` redire possunt, etiam post concatenationem dynamicam;
- PR #108 — `SUBTEXTUS_SCALARUM` cum vacuo legitimo ab errore distincto;
- regressiones collectionum, segmentorum et Unicode inclusae in XXIX/XXIX;
- #111 — structurae internae byte-addressatae a semanticis `ACUS` separatae et acervus ELF VINDEX nativus adhibitus;
- nulla generica ficta ante facultatem linguae.

### Facultates candidatae

- numeri dimensionibus et signis clare definitis;
- fluitantia maturiora;
- arrays, slices et acus divitiores;
- structurae / `FORMA` maturiores;
- uniones et enumerationes;
- functiones ut valores et callback;
- moduli et compilationes separatae;
- contractus ABI expliciti;
- formatio ELF multi-`PT_LOAD` / relocatio acervi;
- textus et Unicode maturior: quaestio, graphemata, normalizatio et transformationes superiores.

### Disciplina

Una facultas parva simul. Quaelibet mutatio linguae debet auto-hospitium, punctum fixum, regressionem propriam, ELF, Win64 et UEFI ubi pertinent custodire.

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

**Status:** `PARATUM ad primum fundamentum`.

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

**Status:** `PARATUM`.

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

- P1 non amplius reservatum est; eius origo #82 post #109 historia experimentalis est.
- P3 per #111 perfectum est; P5 per #110 perfectum est; #71 historia tantum est.
- Opera independentia P9, P12 et P16 procedere possunt, sed mutationes compilatoris eundem punctum fixum et targeta canonica custodire debent.
- Ramus experimentalis prosperus non wholesale mergeatur si structuram veterem secum trahit.
- Mutationes in `main` fiant per PR parvas, probatas et reversibiles.
- Documenta repositorii tantum Lingua Latina utantur.
- Status realis Git semper ante opinionem veterem praevalet.

---

# V. Actio proxima

Via recta progressionis nunc est:

1. P16 incipere: Fenestrale technicum ad formam visualem Sylviae modernam paulatim movere;
2. P12 incipere per fundamenta gubernatorum quae hardware reale et input maturius aperiunt;
3. P9 per incrementa parva et generalia continuare;
4. debitum ELF `PT_LOAD`/acervi fixi separatim solvere sine regressione targetorum;
5. contractus applicationum, widgeta et input Fenestralis maturare.

---

# VI. Sententia

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

**Nullum genus programmatis extra fines VINDEX esse debet.**