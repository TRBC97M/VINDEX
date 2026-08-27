# CONSILIUM — Tabula Magistra Operum VINDEX et Sylviae

> **ARCHITECTURA est lex. CONSILIUM est via. Git historia est.**

## Munus

`CONSILIUM.md` est tabula operativa canonica VINDEX et Sylvia OS. Non est commentarium omnium mutationum: historia exacta in Git et documentis singulorum incrementorum manet. Hic tantum status praesens, dependentiae, curatores, limites et actiones proximae servantur.

Omnis collaborator ante opus novum debet:

1. `ARCHITECTURA.md` legere;
2. hoc `CONSILIUM.md` legere;
3. recentissimum `main`, ramos, Pull Request et probationes inspicere;
4. opus ab alio curatore activum non duplicare;
5. mutationes maiores in ramo proprio facere et per Pull Request canonizare;
6. post mutationem significantem hanc tabulam renovare.

Si documentum et Git dissentiunt, **Git praevalet**; documentum deinde corrigendum est.

## Status

- `IDEA` — finis receptus, nondum definitus;
- `LONGINQUUM` — finis canonicus diuturnus;
- `PARATUM` — opus satis definitum ut incipiatur;
- `ACTIVUM` — opus nunc exercetur;
- `RESERVATUM` — curator alius opus active tenet; ne duplicetur;
- `IMPEDITUM` — dependentia impedit;
- `PROBATUM` — demonstratum, nondum canonice integratum;
- `CANONIZANDUM` — probatum et in `main` portandum;
- `PERFECTUM` — in `main` integratum et probationibus munitum.

---

# I. Basis canonica hodierna

## P1 — UEFI VINDEX purum

**Status:** `PERFECTUM per PR #109`.

Canonice probatum:

- target UEFI PE32+ a compilatore VINDEX;
- `BOOTX64.EFI` VINDEX purus;
- `NUCLEUS.BIN`, `TEXTUS.BIN` et `FORMA.BIN` e volumine FAT per protocolla UEFI leguntur;
- metadata firmware ad nucleum traduntur;
- GOP et framebuffer reales;
- saltus ad nucleum sine runtime C residente;
- auto-hospitium et punctum fixum servantur;
- catena QEMU/OVMF repetibilis.

Catena canonica:

```text
OVMF → BOOTX64.EFI [VINDEX] → NUCLEUS [VINDEX] → SYLVIA [VINDEX]
```

**Debitum separatum:** ELF adhuc acervum ad sedem fixam collocat; multi-`PT_LOAD` vel relocatio acervi opus futurum P9 manet.

---

## P2 — Reconciliatio VINDEX 0.53

**Status:** `PERFECTUM R0–R6`.

Canonicum manet:

- allocationes dynamicae et frames amplae;
- diagnostica cum fonte, linea et columna;
- `PROIECTUM` et targeta;
- ELF, PE/Win64 et UEFI;
- auto-hospitium;
- semantica brevis `&&` / `||`;
- instrumenta regressionis et puritatis.

Monolitha historica non redeunt in lineam canonicam; facultates utiles selective portantur.

---

## P3 — Catena Sylviae pura

**Status:** `PERFECTUM per PR #111`.

Fenestrale II est payload canonicum eiusdem ponticuli UEFI. Post translationem imperii omnis logica runtime Sylviae in VINDEX manet. PS/2, framebuffer et eventa Fenestralia sub QEMU/OVMF probantur sine C residente.

---

## P4 — Fenestrale II Purus

**Status:** `PERFECTUM` pro gradibus A–I.

Facultates canonicae:

- superficies clientium;
- coda eventuum;
- registra dynamica clientium, fenestrarum et applicationum;
- focus et ordo Z;
- motus et resize;
- minimizatio, maximizatio, restitutio et clausura;
- taskbar dynamica;
- compositio ab ima ad summam;
- regressio **LXXX fenestrarum**.

---

## P5 — Mus PS/2 VINDEX nativus

**Status:** `PERFECTUM per PR #110 et #120`.

Rector 8042/PS2 totus VINDEX est. `PS2_IN` et `PS2_OUT` primitivas canonicas `PORTUS_LEGE` et `PORTUS_SCRIBE` adhibent; nullae particulae codicis machinalis manu scriptae in catena canonica manent.

---

## P6 — Officina VINDEX pro Windows

**Status:** `PERFECTUM` pro fundamento nativo canonico per #83.

Haec Officina ecosystematis VINDEX est, non eadem applicatio ac OFFICINA SYLVIAE. Projecta, arbor fasciculorum, tabulae editoris, coloratio syntaxeos, save/build/run, output et diagnostica sub Windows vero iam existunt.

---

## P7 — Probationes canonicae

**Status:** `PERFECTUM et crescens`.

`tests/run_tests.sh` nunc **XXXIII probationes rectas, nulla errata** refert.

Inter alia probantur:

- lingua et diagnostica;
- auto-hospitium `G2 = G3`;
- collectiones, series et segmenta dynamica;
- `TEXTUS` et Unicode strictum;
- PE32+;
- puritas absoluta Sylviae;
- XCVI applicationes;
- LXXX fenestrae;
- TERMINALE P17-I/P17-II;
- OFFICINA SYLVIAE P18-I;
- Fenestrale II integrum.

Custodia UEFI separata exercet boot historicum, PS/2, P16, TERMINALE et OFFICINAM sub QEMU/OVMF. Capturae QEMU OFFICINAE ut artifacta CI temporaria servari possunt.

---

## P8 — Purificatio repositorii

**Status:** `PERFECTUM` pro reconciliationibus maioribus; custodia continua manet.

Regula: historia non deletur, sed nullus ramus historicus vel exemplar vetus auctoritatem super `main` habet. Mechanismi historice probati selective portari possunt si architectura hodierna eos recipit.

---

# II. VINDEX ut lingua universalis

## P9 — Fundamenta typorum et structurae programmatis

**Status:** `ACTIVUM per incrementa`, sine curatore exclusivissimo.

Iam canonicum:

- collectio dynamica `NUMERUS` (#102);
- series dynamica contigua `NUMERUS` (#104);
- segmenta mutuata zero-copy (#105);
- UTF-8 strictum et scalaria Unicode (#106);
- reditus `TEXTUS` e functionibus (#107);
- `SUBTEXTUS_SCALARUM` (#108);
- structurae internae byte-addressatae separatae a semanticis `ACUS` (#111).

Candidata futura:

- numeri dimensionibus et signis clarioribus;
- fluitantia maturiora;
- structurae, uniones et enumerationes maturiores;
- functiones ut valores et callback;
- moduli et compilationes separatae;
- contractus ABI expliciti;
- ELF multi-`PT_LOAD` / relocatio acervi;
- graphemata, normalizatio et transformationes Unicode superiores.

Quaelibet mutatio linguae punctum fixum, ELF, Win64 et UEFI ubi pertinent custodire debet.

---

## P10 — Abstractiones alti gradus

**Status:** `LONGINQUUM`.

Generica, interfaces vel mechanismus VINDEX proprius, errores/resultata, destructio determinata, ownership optativa, closures, concurrentia, atomica, async, SIMD et metaprogrammatio moderata post fundamenta P9 veniunt.

---

## P11 — Ecosystema universale

**Status:** `LONGINQUUM`, incrementis iam incohatum.

Destinatio continet compilatorem, linker, bibliothecam standardem, debugger, profiler, formatter/linter, systema projectuum/build, praepositum fasciculorum et Officinam, cum targetis Sylvia, Windows, ELF-systematum, UEFI et aliis ubi ratio permittit.

**Criterium diuturnum:** nullum genus programmatis rationabile extra fines VINDEX sit.

---

# III. Sylvia ut systema usus cotidiani

## P12 — Infrastructura gubernatorum

**Status:** `RESERVATUM CLAUDE`; incrementa I et II in `main`, incrementum III in PR #122 nondum canonicum.

**Curator:** Claude. ChatGPT hoc opus non duplicat dum reservatio valet.

### Incrementum I — portus I/O et PCI (`PERFECTUM per #118`)

Primitivae canonicae:

- `PORTUS_LEGE`;
- `PORTUS_LEGE32`;
- `PORTUS_SCRIBE`;
- `PORTUS_SCRIBE32`.

`systema/rectores/pci.vindex` configurationem PCI mechanismi #1 per `0xCF8/0xCFC` legit et apparatus enumerat.

### Incrementum II — PS/2 per primitivas nativas (`PERFECTUM per #120`)

`murus_ps2.vindex` nunc solas primitivas portuum canonicas adhibet. Correctio verificatoris statici pro `PORTUS_*` etiam in `main` est.

### Incrementum III — pontes PCI (`ACTIVUM in #122`)

Claude iam demonstravit sub QEMU q35 pontes PCIe et apparatus in bus secundariis. Ante canonizationem #122 adhuc recensenda sunt:

- profunditas vera topologiae, non index codae BFS;
- contractus bus primarii/secondarii/subordinati;
- custodiae allocationum canonicae;
- synchronizatio cum `main` recente et recertificatio integra.

Post P12-III, directio probabilis est **P12-IV — BAR, MMIO et descriptio resourceorum**, deinde interruptiones, ACPI, USB/HID et cetera strata hardware.

---

## P13 — Machina referentiae physica

**Status:** `LONGINQUUM`.

Prima candidata est CHUWI HeroBook Air. Hardware IDs exacta ante implementationem gubernatorum specificorum requiruntur.

Mappa destinata:

boot → display → keyboard → mouse/touchpad → SSD → USB → ACPI/battery → audio → Wi-Fi → Bluetooth → webcam → HDMI → acceleratio graphica.

---

## P14 — Rete Sylviae

**Status:** `LONGINQUUM`, dependet a P12.

NIC/Wi-Fi → Ethernet/802.11 → ARP/NDP → IPv4/IPv6 → ICMP → UDP → TCP → DHCP → DNS → TLS.

---

## P15 — Navigator Sylviae

**Status:** `LONGINQUUM`, dependet a Fenestrale, P9/P10 et P14.

Primum HTML/CSS/textus/nexus/scroll et HTTPS; deinde imagines, formae, cookies, cache et layout maturior. Chromium non est fundamentum necessarium.

---

## P16 — Forma et ambitus Fenestralis modernus

**Status:** `PERFECTUM pro incrementis I–V`.

- P16-I / #113 — metra visualia moderna et taskbar;
- P16-II / #114 — INITIUM functionale;
- P16-III / #115 — bureau functionale;
- P16-IV / #116 — catalogus applicationum dynamicus;
- P16-V / #117 — chrome fenestrarum, focus/inertia et umbrae probatae sub QEMU.

P16 non significat finem evolutionis visualis. Refectio aesthetica maior futura est legitima, sed forma non amplius impedit constructionem applicationum et stratorum systematis.

---

## P17 — TERMINALE Sylviae

**Status:** `PERFECTUM pro incrementis I et II`.

### P17-I / #119

TERMINALE est cliens Fenestralis nativus cum linea UTF-8 dynamica, backspace Unicode et mandatis internis realibus (`SALVE`, `VERSIO`, `AUXILIUM`, `PURGA`). QEMU claves per UEFI → Fenestrale → clientem vere mittit.

### P17-II / #121

Historia mandatorum et transcriptum/scrollback dynamicum addita sunt. Sagittae et PageUp/PageDown ad TERMINALE focalem mittuntur. Probatio QEMU revocationem et re-exsecutionem mandatorum realiter comprobat.

**Nondum shell plenus:** processus, executio externa, navigationes fasciculorum, pipes, redirectiones, environment et job control post strata systematis vera addenda sunt.

---

## P18 — OFFICINA SYLVIAE

**Status:** `P18-I PERFECTUM per #123`.

OFFICINA est quarta applicatio Fenestralis et editor VINDEX nativus intra Sylviam:

- documentum ut lineae dynamicae dupliciter vinculatae;
- lineae UTF-8 dynamicis capacitatibus;
- scalaria Unicode canonica usque ad `U+10FFFF`;
- insertio ad cursorem;
- backspace Unicode;
- divisio et coniunctio linearum;
- sagittae quattuor;
- PageUp/PageDown;
- viewport verticalis;
- status `MODIFICATUM`.

Probatio nativa CCC octeta in una linea et LXXXII lineas exercet. QEMU aperit OFFICINAM e bureau, scribit `VINDEX`, novam lineam creat, scribit `SYLVIA` et sagittas ad cursorem editoris mittit.

**Terminus honestus:** P18-I adhuc in memoria volatili operatur. Apertio/servatio fasciculorum, build/run, coloratio syntaxeos et debugger nondum simulantur.

---

## P19 — Fasciculi et persistentia Sylviae

**Status:** `ACTIVUM`; curator ChatGPT; ramus `chatgpt/p19-fasciculi-i`.

**Finis immediatus:** OFFICINA et TERMINALE debent uti fasciculis vere persistentibus, non copia memoriae ficta.

### Incrementum I — contractus fasciculorum + backend UEFI

Intentio:

- API fasciculorum Sylviae backend-neutra, tota VINDEX;
- viae UTF-8 canonicae cum conversione ad UTF-16 UEFI;
- apertura, lectio, scriptura, flush et clausura;
- scriptura postea re-aperta et byte-per-byte verificata;
- probatio QEMU/OVMF **per duos boots eiusdem imaginis**, ut persistentia post restart comprobetur;
- ponticulus UEFI non fit servus fasciculorum residens: Sylvia ipsa per `SystemTable` iam traditam protocolla firmware directe vocat, sicut input Fenestralis hodie facit.

### Fundamentum historicum utile, non canonicum

Series 0.43–0.51 olim persistentiam realem demonstravit. Praesertim 0.44 in computatro ASUS E410M invenit firmware quod scripturam FAT prosperam simulabat sine persistentia; secunda partitio GPT `VINDEXV0`, Block I/O, `FlushBlocks` et relectio exacta hoc solvebant.

Imago hodierna adhuc partitionem `VINDEXV0` et fasciculum praeparatum `VINDEX.FS` continet. **Formatum vetus cum paucis slotis fixis non reviviscet.** Mechanismus robustus Block I/O selective in incrementum posterius portari potest ut backend nativior vel fallback hardware, cum structura dynamica moderna.

### Incrementa probabilia post I

- P19-II — OFFICINA: aperire et servare fasciculum realem;
- P19-III — backend robustus voluminis VINDEX / Block I/O et probatio hardware;
- deinde TERMINALE cum mandatis fasciculorum realibus et gestor fasciculorum Fenestralis.

---

# IV. Coordinatio agentium

- P12 est reservatum Claude; ChatGPT non duplicat #122.
- P19 est activum apud ChatGPT et a P12 independenter procedere potest.
- P9 potest paralleliter procedere si facultas linguae revera impedit P12, P18 aut P19.
- Rami experimentales prosperi non wholesale merguntur; mechanismus utilis selective in architecturam praesentem portatur.
- Mutationes in `main` fiunt per PR parvas, probatas et reversibiles.
- Omnis documentatio canonica repositorii Lingua Latina manet.
- Git semper praevalet si status scriptus obsolescit.

---

# V. Actio proxima

Ordo operis praesentis:

1. **P19-I** — contractum fasciculorum persistentium et backend UEFI VINDEX purum construere atque duobus bootibus QEMU probare;
2. **P19-II** — OFFICINAM ad aperturam et conservationem fasciculi veri coniungere;
3. TERMINALE mandata fasciculorum realia accipiat;
4. gestorem fasciculorum Fenestralem realem construere;
5. compilationem et executionem VINDEX intra Sylviam super filesystema et processuum stratum verum conectere;
6. P12 apud Claude paralleliter pergat: pontes → BAR/MMIO → interruptiones → ACPI/USB/HID.

Refactio visualis maior Sylviae manet desiderata, sed non impedit P19; post fundamenta functionalia iterum tractari potest.

---

# VI. Sententia

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

**Nullum genus programmatis extra fines VINDEX esse debet.**