# FENESTRALE II PVRVS — GRADVS F
## Duo clientes privati: PROGRAMMATA et TABULA

**Status:** candidatus canonicus  
**Series:** Fenestrale II Purus  
**Gradus:** F  
**Fundamentum:** Gradus E in `main` canonicus

---

## I. Propositum

Gradus F separationem inter Fenestrale et clientes ulterius perficit. PROGRAMMATA iam clientis privatus Gradus E est; TABULA nunc quoque superficiem, statum, picturam et eventa propria accipit.

Fenestrale ornamentum, focus, ordinem Z, tractionem, mutationem mensurae, minimizationem, maximizationem, clausuram et compositionem possidet. Clientes contentum suum tantum possident.

---

## II. TABULA clientis

`bibliotheca/tabula_clientis_f.vindex` duas operationes principales praebet:

- `TF_CLICK` — coordinatas locales TABULAE interpretatur et statum clientis reddit;
- `TF_RENDE` — superficiem privatam TABULAE secundum statum suum pingit.

TABULA craticulam VIII × XII demonstrat. Status `1..96` cellam selectam indicat; status `101` actionem `NOVUM`, status `102` actionem `SERVA` indicat.

Operationes reales fasciculi hoc gradu nondum finguntur; hic contractus separationem clientis probat.

---

## III. Superficies et status

Status systematis servat:

- `s[30]` — superficiem PROGRAMMATA;
- `s[31]` — statum PROGRAMMATA;
- `s[32]` — superficiem TABULA;
- `s[33]` — statum TABULA.

PROGRAMMATA superficiem CCCCXCVI × CCLX pixelorum possidet. TABULA superficiem CCCXCVI × CCXXVI pixelorum possidet.

Utraque superficies per `FS_BLIT` intra corpus ornamentatum componitur.

---

## IV. Eventa

Click Fenestralis prius ornamenta systematis tractat. Si click in corpore clientis incidit, gestor coordinatas fenestrae in spatium locale clientis convertit et ad clientem rectum tradit.

PROGRAMMATA `PE_CLICK` et `PE_RENDE` adhibet. TABULA `TF_CLICK` et `TF_RENDE` adhibet.

Nullus cliens bullas tituli, resize, drag aut focus systematis possidet.

---

## V. Separatio responsabilitatis

Fenestralis sunt:

- ornamentum;
- focus et ordo Z;
- geometria;
- input systematis;
- translatio coordinatarum;
- compositio superficierum.

Clientium sunt:

- status contenti;
- hit-testing intra contentum;
- pictura contenti;
- actiones locales demonstrativae.

TABULA hoc gradu non iam per `FV_TABULA` directe a gestore pingitur.

---

## VI. Puritas

Gradus F:

- nullum `POLLE()` adhibet;
- nullum runtime C, C++, Rust aut ASM addit;
- superficies, status, eventa et compositionem in VINDEX tenet;
- bibliothecas clientes folia sine `IMPORTA` servat;
- custodiam generalem `Sylvia VINDEX purum` non mutat.

---

## VII. Relatio ad historiam

PR historica #62 Gradum F primum probavit, sed super veterem pilam A–E posita erat. Haec reconciliatio directe ex `main` hodierno, Gradu E iam canonico, nascitur et fontes VINDEX probatos selecte recipit sine ascendentia veteris pilae.

---

## VIII. Criterium canonizationis

CI requirit:

1. puritatem generalem Sylviae;
2. analysin staticam gestoris F et probationis duorum clientium;
3. praesentiam `TF_CLICK`, `TF_RENDE`, `s[32]`, `s[33]` et `FS_BLIT`;
4. absentiam picturae directae `FV_TABULA` in gestore F;
5. compilationem probationis duorum clientium in ELF64;
6. compilationem gestoris F integri in ELF64;
7. magnitudinem binarii intra limitem admissum;
8. absentiam `POLLE()`.

Si omnia transeunt, Gradus F fit primum fundamentum canonicum in quo duo clientes graphici distincti simul superficies privatas possident.

> VIA RECTA: Fenestrale fenestras regit; clientes contentum suum regunt.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
