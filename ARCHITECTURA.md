# VINDEX et Sylvia OS — Architectura communis

## Principium

VINDEX et Sylvia OS sunt duo projecta primi ordinis.

**VINDEX** est lingua programmationis generalis et ecosystema instrumentorum. Non dependet a Sylvia OS et debet posse ad programmata, instrumenta, ludos, applicationes graphicas atque systemata alia scribenda adhiberi.

**Sylvia OS** est systema computatorium sui juris, destinatum ad usum verum et progressionem diuturnam. VINDEX est lingua principalis eius et Sylvia simul campus maximus in quo facultates VINDEX exercentur.

Sylvia non est programma demonstrativum abiciendum. VINDEX non est lingua privata Sylviae.

## Principium universalitatis VINDEX

**Nullum genus programmatis extra fines VINDEX esse debet.**

Haec est lex fundamentalis progressionis linguae. VINDEX non tantum C imitari, C++ aequare, aut linguam aliam substituere destinatur. Meta diuturna est ut VINDEX, secundum gradum abstractionis opportunum, ad omne genus operis computatorii adhiberi possit quod in machina moderna rationabiliter perfici potest.

Ita VINDEX paulatim capax esse debet ad scribenda, inter alia:

- firmware, pontes initiales, nucleos et gubernatores ferramentorum;
- systemata operativa et instrumenta basimi gradus;
- compilatores, coniunctores, debugatores et instrumenta evolutionis;
- applicationes graphicas, Officinam, ludos et machinamenta ludorum;
- servitores, protocolla retis, clientes et navigatores interretiales;
- programmata scientifica, mathematica, multimedia et computationis intensivae;
- programmata magni gradus abstractionis, ubi memoria et structurae complexae commode administrantur;
- codicem portabilem ad plura systemata et architecturas, ubi natura operis id permittit.

Universalitas non significat omnes proprietates C++, Rust, Python, JavaScript aut aliarum linguarum ad litteram imitandas esse. **Facultas, non imitatio, norma est.** Si genus quaestionis ab alia lingua solvi potest, VINDEX tandem viam nativam, coherentem et VINDEX propriam ad idem genus quaestionis solvendum praebere debet.

VINDEX igitur duos fines simul servet:

1. **Libertas basimi gradus** — memoria directa, ABI, hardware, codex machinalis, systemata sine runtime necessario et imperium exactum super machinam manere debent possibilia.
2. **Potentia alti gradus** — typi divites, abstractiones, collectiones, generica, concurrentia, instrumenta automatica memoriae et aliae commoditates addi possunt sine facultatibus basimi gradus tollendis.

Nulla futura commoditas magni gradus debet VINDEX ad runtime obligatoriam ligare. Nulla fidelitas basimo gradui debet impedire ne lingua ad applicationes magnas, modernas et commodas crescat.

**Non C est terminus VINDEX. Non C++ est terminus VINDEX. Terminus est ut nullum genus operis computatorii VINDEX alienum sit.**

## Relatio

VINDEX facultates praebet quibus Sylvia construitur. Sylvia necessitates reales detegit quae progressionem VINDEX dirigere possunt. Si Sylvia facultate caret quia VINDEX eam nondum exprimit, primum quaerendum est utrum facultas generalis in VINDEX vel eius bibliotheca standardi creanda sit, non utrum exceptio privata in Sylvia fingenda sit.

## Puritas VINDEX in Sylvia OS

**Sylvia OS post initium firmware tota lingua VINDEX scribenda est.** Haec regula architectonica absoluta est.

Alius sermo, ut C aut codex machinalis manualis, tantum in ponticulo UEFI initiali toleratur ubi firmware directe aliter vocari nondum potest. Ponticulus ille nihil ultra officium amorçandi faciat:

- modum graphicum et framebuffer a firmware obtineat;
- memoriam necessariam initialem reservet;
- imaginem primi programmatis VINDEX oneret;
- descriptorum minimorum initii valores VINDEX tradat, inter quos tabula systematis UEFI si opus est;
- imperium semel ad primum ingressum VINDEX transferat.

Post translationem imperii, ponticulus non debet manere minister runtime nec iterum vocari. Non licet ei:

- ansam eventuum tenere;
- clavierem aut murem pollere;
- framebuffer pingere vel componere;
- fenestras, focus, z-order, taskbar aut superficies administrare;
- systema fasciculorum interpretari vel I/O runtime praestare;
- applicationes VINDEX ut clientes intra runtime C regere;
- functionem residentem praebere quam VINDEX continuo revocet.

Si VINDEX facultate necessaria caret — exempli gratia vocatione indirecta UEFI, accessu memoriae-mappatae, input, disco, interruptione aut alio mechanismo — **lingua VINDEX, compilator eius, ABI aut bibliotheca standardis extendenda sunt.** Defectus facultatis VINDEX numquam causa valida est logicam Sylviae in C transferendi.

Codex non-VINDEX qui historice ultra hunc terminum processit habetur experimentum hereditatum, non exemplar architectonicum. Gradus novi eum non amplificent; migrandus est in VINDEX aut removendus.

## Tres columnae

### 1. VINDEX Lingua

- grammatica et semantica canonica;
- compilator auto-hospes;
- typi, memoria, functiones et moduli;
- ABI et formae binariae;
- diagnostica et probationes conformitatis;
- documentum specificationis versionatum;
- facultates basimi et alti gradus ita componendae ut nullum genus programmatis ex consilio excludatur.

### 2. Ecosystema VINDEX

- `vindexc` et instrumenta compilationis;
- bibliotheca standardis;
- Officina et instrumenta evolutionis;
- bibliotheca graphica;
- documentatio et exempla;
- forma programmatum nativorum Sylviae (`.vxnat`) ubi convenit.

### 3. Sylvia OS

- nucleus et initium;
- administratio memoriae et ferramentorum;
- systema fasciculorum;
- fenestrale et compositor;
- applicationes systematis;
- programmata VINDEX nativa;
- installatio, renovatio et persistentia;
- usabilitas cotidiana in monitoribus et computatris modernis.

## Regula evolutionis

Mutationes futurae distinguantur inter:

1. **mutationem linguae VINDEX** — mutat quid programma VINDEX exprimere potest;
2. **mutationem ecosystematis** — instrumenta vel bibliothecas addit sine grammatica mutanda;
3. **mutationem Sylvia OS** — systema ipsum evolvit;
4. **mutationem communem** — nova facultas VINDEX nascitur ex necessitate Sylviae et deinde a Sylvia adhibetur.

Versiones VINDEX et Sylvia separatim numerandae sunt. Nulla versio Sylviae implicat eandem versionem VINDEX.

## Status hereditatus

VINDEX 0.51 iam compilat directe in ELF x86-64, compilatorem auto-hospitem habet, memoriam, formas, acus, fluitantia, importationes, I/O et pontem graphicum declarativum. Systema experimentale praesens BIOS/UEFI, nucleum VINDEX et ambitum fenestralem continet.

Hoc opus historicum ad probationem et migrationem servari potest, sed nulla pars runtime non-VINDEX ex eo canonica habenda est si regulam puritatis supra violat.

## Directio Sylviae

Sylvia debet excedere limites prototypi praesentis: non mensa 320×200 cum paucis locis fixis, sed ambitus desktop amplitudinis modernae, resolutionibus dynamicis, numero fasciculorum non artificialiter parvo, applicationibus multiplicibus et spatio evolutionis futuro.

Intentio visualis est systema desktop distinctum, legibile et humanum: spiritus systematum classicorum maturorum servari potest, sed scala, ergonomia et facultates ad computatra moderna pertinent.

## Disciplina Git

`main` est linea stabilis communis. Opera majora fiant in ramis separatis, exempli gratia `chatgpt/...` et `claude/...`, deinde per pull request recognoscantur. Archivorum ZIP successio non amplius est ratio primaria versionum: historia Git ipsas versiones servat.

## Proximi gradus

1. Ponticulum UEFI ad initium strictum redigere et omnem logicam runtime ex eo expellere.
2. Facultates linguae VINDEX quae accessui firmware/hardware directo desunt definire et implementare.
3. Fenestrale, compositorium, input, focus, z-order et taskbar in VINDEX nativo migrare.
4. Systema fasciculorum et I/O runtime ex pontibus residentibus in VINDEX transferre.
5. Probationem CI instituere quae novam logicam runtime non-VINDEX in Sylvia prohibet.
