# CONSILIUM — Tabula Magistra Operum VINDEX et Sylviae

> **ARCHITECTURA est lex. CONSILIUM est via. Git historia est.**

## Munus

`CONSILIUM.md` statum operativum canonicum servat: quid perfectum sit, quid activum vel reservatum sit, quibus rebus opera dependeant et quid proximum faciendum sit. Historia minuta in Git et documentis incrementorum manet.

Omnis collaborator ante opus novum `ARCHITECTURA.md`, hoc documentum, `CONTRIBUTING.md` et statum Git recentem inspiciat. Si Git et haec tabula dissentiunt, Git praevalet et tabula corrigenda est.

## Status

- `IDEA` — finis receptus, nondum definitus;
- `LONGINQUUM` — finis canonicus diuturnus;
- `PARATUM` — opus satis definitum ut incipiatur;
- `ACTIVUM` — opus nunc exercetur;
- `RESERVATUM` — curator alius opus active tenet;
- `IMPEDITUM` — dependentia impedit;
- `PROBATUM` — demonstratum, nondum canonice integratum;
- `CANONIZANDUM` — probatum et in `main` portandum;
- `PERFECTUM` — in `main` integratum et probationibus munitum.

---

# I. Basis canonica hodierna

## P1 — UEFI VINDEX purum

**Status:** `PERFECTUM per #109`; contractus memoriae auxiliariae renovatus in #126.

Catena canonica:

```text
OVMF → BOOTX64.EFI [VINDEX] → NUCLEUS [VINDEX] → SYLVIA [VINDEX]
```

Canonice probatum:

- target UEFI PE32+ a compilatore VINDEX;
- ponticulus, nucleus et runtime Sylviae VINDEX puri;
- GOP, framebuffer et metadata firmware;
- `NUCLEUS.BIN`, `TEXTUS.BIN` et `FORMA.BIN` e volumine FAT leguntur;
- nullum gcc, ld, objcopy, C aut assembler externus in catena canonica requiritur;
- QEMU/OVMF totam catenam exercet.

### Contractus memoriae auxiliariae

P19-II defectum vetustum manifestavit: nucleus ad `0x400000` onerabatur, dum `TEXTUS.BIN` ad `0x430000` et `FORMA.BIN` ad `0x460000` sedibus historicis nimis propinquis ponebantur. Cum nucleus modernus 225092 octeta attigit, `TEXTUS.BIN` 28484 octeta codicis nuclei superposuit.

Correctio #126:

- nucleus magnitudine vera tractatur;
- `TEXTUS.BIN` sedem historicam tantum recipit si revera extra nucleum iacet;
- aliter paginae UEFI separatae sine concursu reservantur;
- `FORMA.BIN` quoque in memoria separata reservatur;
- sedes datae per metadata ad runtime traduntur;
- catena historica et Sylvia moderna sub QEMU/OVMF servantur.

**Debitum separatum:** ELF adhuc acervum ad sedem fixam collocat; multi-`PT_LOAD` vel relocatio acervi opus futurum P9 manet.

---

## P2 — Reconciliatio VINDEX 0.53

**Status:** `PERFECTUM R0–R6`.

Canonicum manet:

- allocationes dynamicae et frames amplae;
- diagnostica cum fonte, linea et columna;
- `PROIECTUM` et targeta;
- ELF, PE/Win64 et UEFI;
- auto-hospitium cum puncto fixo;
- semantica brevis `&&` / `||`;
- instrumenta regressionis et puritatis.

Monolitha historica non redeunt; facultates utiles selective portantur.

---

## P3 — Catena Sylviae pura

**Status:** `PERFECTUM per #111`.

Fenestrale II est payload canonicum eiusdem ponticuli UEFI. Post translationem imperii omnis logica runtime Sylviae in VINDEX manet.

---

## P4 — Fenestrale II Purus

**Status:** `PERFECTUM pro gradibus A–I`.

Facultates canonicae:

- superficies clientium;
- coda eventuum;
- registra dynamica clientium, fenestrarum et applicationum;
- focus et ordo Z;
- motus et resize;
- minimizatio, maximizatio, restitutio et clausura;
- taskbar dynamica;
- compositio ab ima ad summam;
- regressio LXXX fenestrarum.

---

## P5 — Mus PS/2 VINDEX nativus

**Status:** `PERFECTUM per #110 et #120`.

Rector 8042/PS2 totus VINDEX est et primitivas canonicas `PORTUS_LEGE` / `PORTUS_SCRIBE` adhibet. Nulla particula codicis machinalis manu scripta in catena canonica manet.

---

## P6 — Officina VINDEX pro Windows

**Status:** `PERFECTUM pro fundamento nativo per #83`.

Haec Officina ecosystematis VINDEX est, non eadem applicatio ac OFFICINA SYLVIAE. Projecta, arbor fasciculorum, editor, coloratio, save/build/run, output et diagnostica sub Windows vero iam existunt.

---

## P7 — Probationes canonicae

**Status:** `PERFECTUM et crescens`.

`tests/run_tests.sh` nunc **XXXV probationes rectas, nulla errata** refert.

Inter alia probantur:

- lingua, diagnostica et auto-hospitium `G2 = G3`;
- collectiones, series, segmenta et Unicode;
- PE32+ et puritas absoluta Sylviae;
- XCVI applicationes et LXXX fenestrae;
- TERMINALE P17-I/P17-II;
- OFFICINA SYLVIAE P18-I;
- P19-II: documentum 4200+ octetorum, Unicode, serializatio, restitutio et round-trip;
- P16-VII: atlas SIMG XCVI×XCVI, quattuor iconae XLVIII×XLVIII, recta fontis/destinationis compacta et lectio rastera;
- Fenestrale II integrum.

Custodiae separatae QEMU/OVMF exercent catenam historicam, PS/2, P16, TERMINALE, OFFICINAM, P19-I et P19-II. P16-VII custodiam QEMU graphicam dedicatam habet quae emblema et quattuor regiones iconarum in framebuffer vero separat et metitur. P19-II duobus initiis eiusdem imaginis persistentiam applicationis comprobat.

---

## P8 — Purificatio repositorii

**Status:** `PERFECTUM pro reconciliationibus maioribus; custodia continua`.

Historia servatur, sed `main`, `ARCHITECTURA.md` et haec tabula auctoritatem praesentem definiunt. Mechanismi historici tantum selective portantur.

---

# II. VINDEX ut lingua universalis

## P9 — Fundamenta typorum et structurae programmatis

**Status:** `ACTIVUM per incrementa`, sine curatore exclusivissimo.

Iam canonicum:

- collectiones dynamicae `NUMERUS` (#102);
- series contiguae (#104);
- segmenta mutuata zero-copy (#105);
- UTF-8 strictum et scalaria Unicode (#106);
- reditus `TEXTUS` (#107);
- `SUBTEXTUS_SCALARUM` (#108);
- structurae internae byte-addressatae separatae a semanticis `ACUS` (#111).

Candidata futura:

- typi numerici maturiores;
- structurae, uniones et enumerationes maturiores;
- functiones ut valores et callback;
- moduli et compilationes separatae;
- ABI explicitius;
- ELF multi-`PT_LOAD` / relocatio acervi;
- graphemata et normalizatio Unicode.

Quaelibet mutatio linguae punctum fixum, ELF, Win64 et UEFI ubi pertinent custodire debet.

---

## P10 — Abstractiones alti gradus

**Status:** `LONGINQUUM`.

Generica, interfaces vel mechanismus VINDEX proprius, errores/resultata, destructio determinata, ownership optativa, closures, concurrentia, atomica, async, SIMD et metaprogrammatio moderata post fundamenta P9 veniunt.

---

## P11 — Ecosystema universale

**Status:** `LONGINQUUM`, incrementis iam incohatum.

Destinatio continet compilatorem, linker, bibliothecam standardem, debugger, profiler, formatter/linter, systema projectuum/build, praepositum fasciculorum et Officinam, cum pluribus targetis.

**Criterium:** nullum genus programmatis rationabile extra fines VINDEX sit.

---

# III. Sylvia ut systema usus cotidiani

## P12 — Infrastructura gubernatorum

**Status:** `RESERVATUM CLAUDE`; incrementa I et II in `main`; incrementum III in #122 nondum canonicum.

**Curator:** Claude. ChatGPT hoc opus non duplicat dum reservatio valet.

### P12-I — portus I/O et PCI

**Status:** `PERFECTUM per #118`.

Primitivae canonicae `PORTUS_LEGE`, `PORTUS_LEGE32`, `PORTUS_SCRIBE`, `PORTUS_SCRIBE32`; rector PCI mechanismum configurationis #1 exercet.

### P12-II — PS/2 per primitivas nativas

**Status:** `PERFECTUM per #120`.

### P12-III — pontes PCI

**Status:** `RESERVATUM / ACTIVUM in #122`.

#122 manet aperta super basim veterem. Ante canonizationem adhuc requiruntur:

- synchronizatio cum `main` recente;
- profunditas vera topologiae, non index codae BFS;
- bus primarius/secondarius/subordinatus explicitus;
- custodiae allocationum canonicae `<=0`;
- recertificatio integra.

Post P12-III directio probabilis est BAR/MMIO et descriptio resourceorum, deinde interruptiones, ACPI, USB/HID et cetera hardware.

---

## P13 — Machina referentiae physica

**Status:** `LONGINQUUM`.

Machina referentiae requiret IDs hardware exacta et gradus boot → display → input → storage → USB → ACPI/battery → audio → rete → cetera.

---

## P14 — Rete Sylviae

**Status:** `LONGINQUUM`; dependet a P12.

NIC/Wi-Fi → Ethernet/802.11 → ARP/NDP → IPv4/IPv6 → ICMP → UDP → TCP → DHCP → DNS → TLS.

---

## P15 — Navigator Sylviae

**Status:** `LONGINQUUM`; dependet a Fenestrale, P9/P10 et P14.

Primum HTML/CSS/textus/nexus/scroll et HTTPS; postea imagines, formae, cookies, cache et layout maturior.

---

## P16 — Forma et ambitus Fenestralis modernus

**Status:** `PERFECTUM pro incrementis I–VI`; incrementum VII `CANONIZANDUM per #128`.

- P16-I / #113 — metra visualia moderna et taskbar;
- P16-II / #114 — INITIUM functionale;
- P16-III / #115 — bureau functionale;
- P16-IV / #116 — catalogus applicationum dynamicus;
- P16-V / #117 — chrome fenestrarum, focus/inertia et umbrae;
- P16-VI / #127 — identitas visualis nox-ebur-aes, pictogrammata distincta, chrome et clientes canonici.

### P16-VI — Identitas visualis Sylviae

**Status:** `PERFECTUM per #127`.

Canonicum:

- palette graphitica, eburnea, papyracea, bronzea et viridis;
- chrome fenestrarum et umbrae cohaerentes;
- pictogrammata distincta pro quattuor applicationibus;
- INITIUM, taskbar, PROGRAMMATA, TABULA, TERMINALE et OFFICINA eadem grammatica visuali utuntur;
- omnes interactiones P16–P19 sub QEMU/OVMF intactae probatae sunt;
- `documenta/sylvia/IDENTITAS_VISUALIS_VI.md` contractum visualem servat.

### P16-VII — Capacitas Graphica Sylviae

**Status:** `CANONIZANDUM per #128`; curator ChatGPT; ramus `chatgpt/capacitas-graphica-sylviae-vii`.

Finis est non mera nova skin, sed amplificatio renderer VINDEX ut Sylvia imagines et compositiones multo divitiores vere pingere possit.

In #128 probatum:

- interpolatio colorum et gradientiae horizontales/verticales;
- compositio alpha software super framebuffer et superficies clientium;
- umbrae graduatae, halos et primitiveae compositionis sine backend externo;
- contractus `SIMG v1` RGBA8888 et lectio pixelorum;
- decoder palette/RLE generalis qui asseta compacta in SIMG expandit;
- blit partium, recta source/destinationis compacta et scala nearest-neighbor;
- emblema Sylviae rasterum XXXII×XXXII;
- atlas XCVI×XCVI cum quattuor iconis rasteris XLVIII×XLVIII pro PROGRAMMATA, TABULA, TERMINALE et OFFICINA;
- compositor finalis cuius ordo est fundum → bureau → rastera → fenestrae → INITIUM → taskbar → cursor;
- custodia QEMU/OVMF dedicata quae in framebuffer vero emblema et quattuor iconae separat et metitur;
- `tests/run_tests.sh` ad XXXV probationes canonicas auctum;
- vetus limes staticus 212999 octetorum e verificatore VINDEX amotus; systema integrum ultra illum limitem verificatur et compilatur;
- nulla mutatio hitbox, focus, semantica applicationum aut puritatis VINDEX.

Probatio QEMU P16-VII mensuras iconarum rasterarum `936,907,984,822` rettulit et totam viam `OVMF → BOOTX64.EFI [VINDEX] → FENESTRALE II [VINDEX] → PS/2 [VINDEX] → FRAMEBUFFER` sine C servavit.

Post canonizationem #128, chrome compositus Frutiger-Aero × imperiale × Y2K super has primitiveas novas construatur; nullae picturae simulatae loco framebuffer veri pro probatione adhibeantur.

---

## P17 — TERMINALE Sylviae

**Status:** `PERFECTUM pro incrementis I et II`.

P17-I / #119: linea UTF-8 dynamica, backspace Unicode et mandata interna realia.

P17-II / #121: historia mandatorum, transcriptum/scrollback dynamicum, sagittae et PageUp/PageDown.

**Nondum shell plenus:** processus, executio externa, navigationes fasciculorum, pipes, redirectiones, environment et job control post strata systematis vera addenda sunt.

---

## P18 — OFFICINA SYLVIAE

**Status:** `P18-I PERFECTUM per #123`.

OFFICINA est editor VINDEX nativus intra Sylviam cum:

- documentis ex lineis dynamicis dupliciter vinculatis;
- UTF-8 et scalaribus Unicode usque ad `U+10FFFF`;
- insertione, backspace, divisione/coniunctione linearum;
- sagittis, PageUp/PageDown et viewport;
- statu mutationis.

P19-II persistentiam huic nucleo editoris superponit sine `OE_*` ad backend firmware directe ligando.

---

## P19 — Fasciculi et persistentia Sylviae

**Status:** P19-I `PERFECTUM`; P19-II `PERFECTUM`; curator ChatGPT.

### P19-I — contractus fasciculorum et backend UEFI

**Status:** `PERFECTUM per #125`.

Canonicum:

- API `FS_*` backend-neutra, tota VINDEX;
- viae UTF-8 cum conversione UTF-16 UEFI;
- existentia, apertura, lectio dynamica, scriptura, flush, clausura et deletio;
- scriptura re-aperta et byte-per-byte verificata;
- probatio 4128 octetorum, supra vetus limen 4095;
- duo initia QEMU/OVMF eiusdem imaginis sine copia memoriae inter initia.

Backend UEFI est primus backend; futura via Block I/O / `VINDEXV0` potest addi sine applicationibus mutandis. Vetus formatum slotorum fixorum non resurrectum est.

### P19-II — OFFICINA persistens

**Status:** `PERFECTUM per #126`.

Canonicum:

- `OE_*` manet editor memoriae independens;
- `OP_*` tenet persistentiam, viam `OFFICINA.VIX` et statum I/O;
- initium OFFICINAE fasciculum existentem automatice legit;
- F2 per Fenestrale ad conservationem realem routatur;
- `MODIFICATUM` tantum post scripturam, flush, re-aperturam et verificationem exactam felicem mundatur;
- LF canonice scribitur, CRLF recipitur;
- UTF-8 invalidum documentum bonum non corrumpit;
- regressio canonica 4200 octeta, Unicode et round-trip exercet;
- QEMU boot I scribit `ZEPHYR72941\nNOVAPERSISTET` (25 octeta);
- eadem imago iterum bootatur, documentum reaperitur, `X` additur et 26 octeta iterum servantur;
- nulla copia memoriae inter initia transfertur.

### P19-III — backend persistentiae robustior / hardware

**Status:** `PARATUM` post P16-VII vel cum necessitas hardware id poscit.

Finis probabilis est backend directior Block I/O / volumen VINDEX cum structura moderna dynamica, non resurrectio veterum slotorum fixorum.

---

# IV. Coordinatio agentium

- P12 manet reservatum Claude; ChatGPT non duplicat #122.
- P16-VII est `CANONIZANDUM` in #128 apud ChatGPT.
- P19-I et P19-II sunt canonica in `main` per #125 et #126.
- P9 potest paralleliter procedere si facultas linguae revera impedit opus systematis.
- mutationes maioris status per PR et probationes fiunt;
- omnis documentatio canonica repositorii Lingua Latina manet;
- Git praevalet si status scriptus obsolescit.

---

# V. Actio proxima

1. **#128 canonizare:** omnes custodias ultimi capitis virides obtinere, PR e draft educere et P16-VII in `main` integrare;
2. **chrome compositum:** gradientias, alpha, umbras, halos et stratos vitreos P16-VII ad fenestras, INITIUM et taskbar applicare;
3. **iconographiam propagare:** eadem asseta rastera in INITIUM et taskbar multiplicibus scalis sine duplicatione uti;
4. ergonomiam et densitatem typographicam cum identitate Frutiger-Aero × imperiali × Y2K maturare, semper sub framebuffer QEMU vero;
5. TERMINALE mandata fasciculorum realia accipiat;
6. gestorem fasciculorum Fenestralem realem construere;
7. processuum/executionis stratum verum construere, deinde compilationem et executionem VINDEX intra Sylviam cum OFFICINA conectere;
8. P19-III backend persistentiae robustior ad hardware quando opportunum;
9. P12 apud Claude paralleliter pergat post correctionem #122: pontes → BAR/MMIO → interruptiones → ACPI/USB/HID.

---

# VI. Sententia

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

**Nullum genus programmatis extra fines VINDEX esse debet.**
