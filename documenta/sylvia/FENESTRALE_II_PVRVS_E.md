# FENESTRALE II PVRVS — GRADVS E
## Eventa clientis PROGRAMMATA

**Status:** candidatus canonicus  
**Series:** Fenestrale II Purus  
**Gradus:** E  
**Fundamentum:** Gradus D in `main` canonicus

---

## I. Propositum

Gradus E superficiem privatam Gradus D in primum clientem interactivum convertit.
PROGRAMMATA eventa intra corpus suum accipit, statum proprium mutat et
superficiem suam iterum pingit; ornamentum, focus, geometria et compositio
Fenestrali manent.

---

## II. Clientis contractus

`bibliotheca/programmata_clientis_e.vindex` duas operationes principales
praebet:

- `PE_CLICK` — coordinatas locales clientis accipit et statum clientis reddit;
- `PE_RENDE` — superficiem PROGRAMMATA secundum statum clientis pingit.

Status demonstrativus:

- `0` — paratus;
- `1` — `TABULA.VXNAT` selectum;
- `2` — actio `NOVUM`;
- `3` — actio `EDITE`;
- `4` — actio `NOMEN`;
- `5` — actio `DELE`, confirmatione visuali indicata.

Operationes fasciculi reales hoc gradu nondum finguntur; status visualis tantum
contractum eventuum probat.

---

## III. Ordo eventuum

`FB_MOUSE_DOWN` eventum hoc ordine tractat:

1. barram operum;
2. bullas tituli;
3. margines et angulos mutationis mensurae;
4. barram tituli ad tractionem;
5. corpus clientis PROGRAMMATA;
6. focum ordinarium.

Cliens igitur ornamentum fenestrae numquam possidet.

Si click intra corpus PROGRAMMATA est, gestor coordinatas systematis in
coordinatas locales convertit per `lx - 10` et `ly - 52`, deinde `PE_CLICK`
vocat. Punctum `(0,0)` huius spatii localis est angulus superior sinister
superficiei clientis, non angulus fenestrae neque framebuffer. Si status
mutatur, `PE_RENDE` superficiem privatam iterum pingit.

---

## IV. Status systematis

Gradus E servat:

- `s[30]` — superficiem privatam PROGRAMMATA;
- `s[31]` — statum clientis PROGRAMMATA.

Initio `s[31] = 0`. Superficies CCCCXCVI × CCLX pixelorum per `FS_CREA`
creatur et per `PE_RENDE` pingitur.

---

## V. Separatio responsabilitatis

Clientis sunt:

- status contenti;
- hit-testing intra contentum;
- pictura contenti.

Fenestralis sunt:

- ornamentum;
- focus et ordo Z;
- drag et resize;
- minimizatio, maximizatio et clausura;
- translatio coordinatarum;
- compositio superficiei in framebuffer.

Haec divisio fundamentum eventuum applicationum futurorum constituit.

---

## VI. Puritas

Gradus E:

- nullum `POLLE()` adhibet;
- nullum runtime C, C++, Rust aut ASM addit;
- eventa, statum clientis, picturam et compositionem in VINDEX tenet;
- bibliothecas importatas folia servat, cum omnibus `IMPORTA` in fonte supremo;
- custodiam generalem `Sylvia VINDEX purum` non mutat.

---

## VII. Relatio ad historiam

PR historica #61 probationem originalem Gradus E continebat, sed super veterem
pilam Gradus D posita erat. Haec reconciliatio directe ex `main` hodierno,
Gradu D iam canonico, nascitur et fontes VINDEX probatos selecte recipit sine
ascendentia veteris pilae.

---

## VIII. Criterium canonizationis

CI requirit:

1. puritatem generalem Sylviae;
2. analysin staticam gestoris E et probationis clientis;
3. contractum `PE_CLICK`, `PE_RENDE`, `s[31]` et translationis coordinatarum;
4. compilationem probationis clientis in ELF64;
5. compilationem gestoris E integri in ELF64;
6. magnitudinem binarii intra limitem admissum;
7. absentiam `POLLE()`.

Si omnia transeunt, Gradus E fit primum fundamentum canonicum eventuum
clientis PROGRAMMATA.

> VIA RECTA: systema ornamentum regit; cliens contentum regit.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
