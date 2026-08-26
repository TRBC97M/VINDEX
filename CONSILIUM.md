# CONSILIUM — Tabula Magistra Operum VINDEX et Sylviae

> **ARCHITECTURA est lex. CONSILIUM est via. Git historia est.**

## Munus huius documenti

`CONSILIUM.md` est tabula operativa canonica totius operis VINDEX et Sylvia OS. Non substituit `ARCHITECTURA.md`: illa principia fundamentalia et limites architectonicos statuit; hoc documentum ordinem operum, dependentias, curatores, statum praesentem, actionem proximam et criteria victoriae declarat.

Omnis collaborator — homo, ChatGPT, Claude, Copilot, Gemini aut alius agens — ante opus novum debet:

1. `ARCHITECTURA.md` legere;
2. `CONSILIUM.md` legere;
3. statum recentem `main`, ramorum, Pull Request et probationum inspicere;
4. cavere ne opus iam ab alio agente activum duplicetur;
5. primum opus maximae prioritatis eligere quod `PARATUM` est et dependentiis non impeditur, nisi usor aliud expresse iubeat;
6. post mutationem significantem statum huius tabulae renovare.

Si res in hoc documento et status realis Git dissentiunt, **status realis Git praevalet**, deinde `CONSILIUM.md` quam primum corrigendum est.

## Status operum

- `IDEA` — destinatio recepta est, sed nondum ad operandum parata.
- `LONGINQUUM` — propositum canonicum diuturnum est; nondum prioritas praesentis temporis.
- `PARATUM` — opus clare definitum est et incipi potest.
- `ACTIVUM` — opus nunc a collaboratore exercetur.
- `RESERVATUM` — alius collaborator hoc opus active tenet; ne duplicetur sine recognitione status.
- `IMPEDITUM` — dependentia aut defectus impedit progressionem.
- `PROBATUM` — functio demonstrata est, sed nondum canonica aut plene integrata.
- `CANONIZANDUM` — experimentum probatum est et in lineam canonicam portandum.
- `PERFECTUM` — criterium victoriae impletum et in linea canonica verificatum est.

## Regula coordinationis agentium

- Ramus alienus non est territorium hostium sed memoria operis communis.
- Si alius agens opus `ACTIVUM` vel `RESERVATUM` facit, primum eius ramum et recentissimos commits inspice; noli idem opus ex nihilo duplicare.
- Experimenta prospera non statim in `main` fundantur. Portentur in structuram canonicam per mutationes parvas et probatas.
- Cum opus relinquitur propter tempus, tokena, errorem instrumentorum aut aliam causam, curator statum, ramum, ultimum commit, quod probatum est, quod incertum est et actionem proximam in hoc documento relinquat.
- Usor potest ordinem quolibet momento mutare. Eius mandatum expressum prioritatem tabulae superat; postea tabula ad novam decisionem accommodetur.

---

# I. PRIORITATES PRAESENTES

## P1 — UEFI in VINDEX puro; ponticulus C tollendus

**Status:** `RESERVATUM / PROBATUM`  
**Curator praesens:** Claude  
**Ramus notus:** `claude/uefi-vindex-purus`  
**Ultima probatio nota:** ponticulus VINDEX purus `NUCLEUS.BIN` onerat, metadata tradit et ad nucleum probationis salit sub QEMU + OVMF; `PONTOK` et `NUCLEUS VIVIT` observata sunt.  
**Causa:** Sylviae puritas postulabit ut etiam exceptio ultima C in initio UEFI tandem evanescat.  
**Actio proxima:** postquam curator opus resumit vel terminat, recentissimos commits inspicere et statum denuo aestimare ante quam quidquam parallelum fiat.

**Canonizatio post probationem:**  
- modum `uefi` in compilatore canonico separare a PE/Win64;
- importationes Windows (`kernel32`, `.idata`) a target UEFI removere;
- memoriam operariam, metadata et acervum per contractum UEFI rite allocare vel reservare, sine regionibus fortuitis non possessis;
- magnitudinem `NUCLEUS.BIN` vere interrogare et paginas exactas allocare, sine limite arbitrario 2 MiB;
- `SALI_AD` ad acervum legitime reservatum accommodare;
- nucleum Sylviae realem, non tantum nucleum probationis, onerare;
- probationem CI QEMU/OVMF instituere.

**Criterium victoriae:** firmware UEFI → applicatio EFI a VINDEX generata → nucleus Sylviae VINDEX realis, sine C et sine assembler externo in catena runtime, cum probatione repetibili.

## P2 — Reconciliatio VINDEX 0.53 cum linea canonica

**Status:** `PARATUM`, sed P1 ante mutationes magnas recensendum est.  
**Fontes principales:** ramus historicus VINDEX 0.53 et rami reconciliationis.  
**Causa:** 0.53 multas facultates maturas continet — fontes et buffers dynamicos, functiones et locales dynamicos, contextum compilationis explicitum, Win64 PE32+, argumenta plura ABI, PROIECTUM, diagnostica, ARGV et alia — sed ramus historicus non est directe miscendus cum `main`.

**Actio proxima:** facultates 0.53 inventariare contra `main`, deinde eas parvis commitibus portare, auto-hospitio et regressionibus ELF/PE/UEFI post singulos gradus verificatis.

**Criterium victoriae:** compilator canonicus modernus omnes facultates probatas 0.53 retinet, structuram praesentem observat, auto-hospitium punctum fixum servat et targeta ELF, PE/Win64 atque UEFI non regreditur.

## P3 — Catena Sylviae pura canonica

**Status:** `IMPEDITUM` a P1/P2.  
**Finis:** unum iter boot canonicum et comprehensibile, non collectionem prototyporum historicorum.

**Debet continere:**
- boot UEFI VINDEX;
- nucleus VINDEX;
- memoria et initium hardware;
- framebuffer et output textus;
- input fundamentale;
- Fenestrale II Purus;
- launch programmatum VINDEX.

**Criterium victoriae:** imago Sylvia canonica in QEMU/OVMF bootat et desktop realem VINDEX ostendit sine runtime C.

## P4 — Fenestrale II Purus canonizandum

**Status:** `CANONIZANDUM`.  
**Fontes:** gradus Purus A–I in ramis/PR separatis.  
**Causa:** fundamentum desktop moderni Sylviae est compositor, registrum fenestrarum dynamicum, focus, z-order, eventa, resize et clientes multiplices, omnia in VINDEX.

**Actio proxima:** post stabilitatem catenae boot, gradus Purus ordine dependentiarum in lineam canonicam portare et probationes renovare.

**Criterium victoriae:** fenestrae dynamicae sine limite artificiali parvo; creare, movere, redimensionare, focalizare, componere et claudere; eventa recte tradere; multitudo fenestrarum probata.

## P5 — Mus PS/2 VINDEX nativus

**Status:** `PROBATUM / CANONIZANDUM`.  
**Fons probationis:** laboratorium PS/2 sub QEMU/OVMF; desktop, textus et mus iam demonstrati sunt.  
**Actio proxima:** mechanismum experimenti in catena P3/P4 portare, non ramum laboratorii integre miscere.

**Criterium victoriae:** cursor et eventa muris in Fenestrale II canonico sub QEMU/OVMF probantur, sine C runtime.

## P6 — Officina VINDEX

**Status:** `IMPEDITUM / CANONIZANDUM`.  
**Finis:** IDE nativum VINDEX, simile instrumento moderno evolutionis sed identitate Sylviae/VINDEX propria.

**Iam demonstratum:** applicatio Windows nativa cum arbore projectus, tabulis, coloratione syntaxeos, save/build/run, output et navigatione diagnosticorum.  
**Defectus notus:** probatio functionalis non est adhuc certificata.

**Actio proxima:** defectus probationum corrigere, deinde Officinam ad compilatorem canonicum 0.53+ conectere.

**Criterium victoriae:** projectum VINDEX a creatione usque ad compilationem, executionem et diagnosticum in Officina tractari potest sine processu manuali disperso.

## P7 — Purificatio repositorii

**Status:** `PARATUM`, sed mutationes activas aliorum agentium non turbet.  
**Finis:** ramos experimentales veteres, duplicata, PR obsoletas et artefacta non canonica post verificationem ordinare vel claudere.

**Criterium victoriae:** `main` et rami activi rationem praesentis architecturae clare repraesentant; historia servatur, sed via canonica non obscuratur.

---

# II. VINDEX UT LINGUA UNIVERSALIS

## P8 — Fundamenta alti gradus VINDEX

**Status:** `LONGINQUUM / PARATUM per incrementa`.  
**Lex:** facultas, non imitatio, norma est.

VINDEX paulatim accipiat facultates quae programmata magna et moderna simpliciter scribi sinunt, sine libertate basimi gradus tollenda:

- typi numerici pleni et conversiones bene definitae;
- structurae, uniones, enumerationes et typi usoris;
- moduli et compilationes separatae;
- functiones ut valores, callback, closures et lambda ubi utiles;
- generica nativa simplicia et potentia;
- collectiones standardes;
- textus et Unicode maturus;
- errores et mechanismus tractationis eorum congruus;
- ownership vel alia disciplina memoriae optativa;
- destructio determinata / RAII similis ubi utilis;
- concurrentia, atomica, fila et async;
- SIMD, fluitantia et computationes vectoriales;
- introspectio vel metaprogrammatio moderata;
- FFI ad bibliothecas externas;
- optimizator, debugger et instrumenta analysi.

**Principium absolutum:** commoditates alti gradus runtime obligatoriam omnibus programmatibus imponere non debent.

## P9 — Ecosystema universale

**Status:** `LONGINQUUM`.  
**Componentes destinati:**
- compilator `vindex`;
- coniunctor/linker;
- debugger;
- bibliotheca standardis;
- praepositus fasciculorum/package manager;
- systema projectuum et constructionis;
- Officina;
- formatter, linter et instrumenta analysi;
- targeta multiplicia: Sylvia, Windows, ELF-systemata, UEFI, ARM64, WebAssembly et alia ubi ratio permittit.

**Criterium victoriae diuturnum:** idem projectum VINDEX, ubi API dependentes separantur, ad plura targeta a toolchain officiali construi potest.

---

# III. SYLVIA UT SYSTEMA USUS COTIDIANI

## P10 — Apparatus et infrastructura gubernatorum

**Status:** `LONGINQUUM`, post stabilitatem nuclei.  
**Finis:** vera architectura driver VINDEX.

**Strata requisita:** PCI/PCIe, ACPI, USB, HID, I2C, interruptiones, MMIO/portus, DMA, firmware loading, registrum apparatus et contractus gubernatorum.

**Criterium victoriae:** gubernator VINDEX potest apparatum detegere, initiare, eventa accipere et servitium systemati praebere sine logica privata in nucleo sparsa.

## P11 — Machina referentiae physica: CHUWI HeroBook Air

**Status:** `LONGINQUUM`.  
**Propositum:** una machina realis eligatur ut prima tabula certificationis hardware Sylviae.

**Mappa desiderata:** boot → display → keyboard → mouse/touchpad → SSD → USB → ACPI/battery → audio → Wi-Fi → Bluetooth → webcam → HDMI → acceleratio graphica ubi possibilis.

**Nota:** exacta identificatio componentium hardware ante gubernatores reales facienda est; variantes eiusdem exemplaris non praesumantur identicae.

**Criterium victoriae:** Sylvia in machina referentiae nativa quotidie adhiberi potest cum omnibus componentibus essentialibus functionantibus.

## P12 — Rete Sylviae

**Status:** `LONGINQUUM`, dependet a P10/P11.  
**Strata:** driver NIC/Wi-Fi → Ethernet/802.11 ubi opus → ARP/NDP → IPv4/IPv6 → ICMP → UDP → TCP → DHCP → DNS → TLS.

**Criterium victoriae:** programma VINDEX in Sylvia potest nomen interretiale resolvere et connexionem HTTPS verificatam aperire.

## P13 — Navigator interretialis VINDEX

**Status:** `LONGINQUUM`, dependet a P4, P8 et P12.  
**Gradus I:** URL, HTTP(S), HTML, CSS fundamentalis, textus, nexus, scroll, input et Fenestrale.  
**Gradus II:** imagines, formae, cookies, historia, downloads, cache.  
**Gradus III:** layout modernior, fontes, flexbox/tabulae et CSS latius.  
**Gradus IV:** engine JavaScript VINDEX proprius vel alius mechanismus VINDEX nativus, sine Chromium ut fundamento necessario.

**Criterium victoriae initiale:** paginae HTML/CSS simplices per HTTPS in Sylvia native redduntur et navigari possunt.

## P14 — Forma visualis Sylviae canonica

**Status:** `LONGINQUUM / dependet a P4`.  
**Finis:** implementationem realem ad consilia visualia canonica adducere; status rudis praesentis non est destinatio finalis.

**Requisita:** typographia, proportiones, margines, icones, widgets, menu, taskbar, cursor, status hover/pressed/focus, scaling dynamicum, resolutiones modernae, compositiones et identitas visualis constans.

**Regula:** designa approbata sunt referentia; Fenestrale debet ad ea convergere, non ea ad limitationes prototypi reducere.

**Criterium victoriae:** screenshot systematis realis cum referentia canonica comparari potest et differentiae maiores non manent.

## P15 — Programmata systematis Sylviae

**Status:** `LONGINQUUM`, dependet a P4/P8.  
**Minimum destinatum:** terminale, gestor fasciculorum, editor textus, Officina, configurationes systematis, monitor systematis, installer/updater, navigator et instrumenta retis.

**Criterium victoriae:** usor potest Sylvia uti, configurare, programmare et conservare sine altero OS ad opera ordinaria.

---

# IV. PRINCIPIA PRIORITATIS

Ordinem operum sic iudicamus:

1. **Puritas et fundamenta ante ornamenta.**
2. **Probatio realis ante canonizationem.**
3. **Canonizatio ante novum experimentum eiusdem rei.**
4. **Dependentiae communes ante applicationes quae eis egent.**
5. **Nullus terminus artificialis propter commoditatem prototypi permanentem fiat.**
6. **Quod hodie experimentum est, cras aut probetur et canonizetur, aut clare archivetur.**
7. **Idea nova in tabula recipi potest sine eo quod statim prioritatem supremam accipiat.**

## Ordo praesens summarius

`P1 UEFI purus` → `P2 VINDEX 0.53 canonicus` → `P3 catena Sylvia pura` → `P4 Fenestrale II` + `P5 mus` → `P6 Officina` → deinde infrastructura linguae/systematis secundum dependentias.

P7 purificatio repositorii inter hos gradus fieri potest cum non perturbat opus activum.

---

# V. FORMA NOVI OPERIS

Cum novum propositum additur, hac forma describatur:

```text
## PX — Nomen operis

Status: IDEA | LONGINQUUM | PARATUM | ACTIVUM | RESERVATUM | IMPEDITUM | PROBATUM | CANONIZANDUM | PERFECTUM
Curator: liber | homo | ChatGPT | Claude | Copilot | Gemini | alius
Ramus/PR: ...
Causa: cur hoc opus necessarium est
Finis: quid construendum est
Dependentiae: quid antea existere debet
Actio proxima: unus gradus concretus
Criterium victoriae: probatio observabilis quae finem demonstrat
Notae: decisiones, pericula, res incertae
```

---

# VI. MODUS SUCCESSIONIS INTER SESSIONES ET AGENTES

Antequam sessio aut curator opus relinquat, si mutationes adhuc imperfectae sunt, haec quinque relinquantur:

1. **ubi sumus** — ramus, PR et commit;
2. **quid vere probatum est** — non quod speratur;
3. **quid adhuc deest**;
4. **quid cavendum est** — regressiones, decisiones, rami alieni;
5. **quid proximum faciendum est**.

Agens novus hoc documentum et Git legat antequam ab usuario repetat quae iam hic certa sunt. Quaestiones tantum fiant ubi electio humana vera est aut intentio mutata esse potest.

---

# VII. SENTENTIA MAGISTRA

**VINDEX Latine cogitat. Sylvia Latine loquitur.**  
**Nullum genus programmatis extra fines VINDEX esse debet.**  
**ARCHITECTURA est lex. CONSILIUM est via. Git historia est.**
