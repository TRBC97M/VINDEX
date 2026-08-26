# FENESTRALE II PVRVS — GRADVS C
## Mutatio mensurae canonica

**Status:** candidatus canonicus  
**Series:** Fenestrale II Purus  
**Gradus:** C  
**Fundamentum:** Gradus B in `main` canonicus

---

## I. Propositum

Gradus C interactionem Fenestralis II Puri extendit ut fenestrae non solum
trahi, minui, augeri et claudi possint, sed etiam per margines atque angulos
directe mutari mensura possint.

Omnis haec logica post initium UEFI in VINDEX manet. Gradus C faciem finalem
Sylviae non definit; contractum geometricum fenestrarum stabilit.

---

## II. Fundamentum

Gradus C super Gradum B canonicum struitur:

- `bibliotheca/fenestrale_ii_purus.vindex` primitivas graphicas communes praebet;
- `systema/fenestrale_ii_purus_c.vindex` gestorem B mutatione mensurae extendit;
- `probationes/fenestrale_purus_c_resize.vindex` logicam geometricam seorsum probat.

Input UEFI, focus, ordo Z, tractio, minimizatio, maximizatio, clausura et barra
operum ex Gradu B servantur.

---

## III. Status mutationis mensurae

Elementum `s[27]` vectoris status margines activos continet:

- `1` — sinister;
- `2` — dexter;
- `4` — superior;
- `8` — inferior.

Combinationes horum bituum angulos efficiunt. `s[14]` fenestram tractatam
servat, dum `s[15]` et `s[16]` positionem muris priorem vel offset tractionis
servant pro genere interactionis activo.

Cum bulla muris solvitur, et identificator tractionis et margines mutationis
ad nihilum restituuntur.

---

## IV. Detectio marginum

Margo sex pixelorum circa fenestram tractabilem agnoscitur. Ordo actionis
huiusmodi est:

1. bullae clausurae, minimizationis et maximizationis;
2. margines et anguli mutationis mensurae;
3. barra tituli ad tractionem;
4. corpus fenestrae ad focum.

Ita margo superior bullas tituli non usurpat. Fenestra maximizzata per
margines mutari non potest; ante mutationem mensurae restitui debet.

---

## V. Geometria

`FC_RESIZE` differentiam motus muris computat et geometriae fenestrae secundum
margines activos applicat.

PROGRAMMATA minimum servat:

- latitudinem DXX pixelorum;
- altitudinem CCCXL pixelorum.

TABULA minimum servat:

- latitudinem CDXX pixelorum;
- altitudinem CCC pixelorum.

Fenestrae intra latitudinem monitoris et supra barram operum XXVIII pixelorum
retinentur. Mutatio a margine sinistro vel superiore originem simul movet ut
latus oppositum stabile maneat.

---

## VI. Continuitas Gradus B

Gradus C non reponit gestorem B sed eum extendit. `FB_DRAG` si `s[27]` non est
nihil ad `FC_RESIZE` transit; aliter tractio ordinaria Gradus B manet.

Focus, ordo Z, taskbar, input claviaturae, murus UEFI et compositio graphica
communi bibliotheca uti pergunt.

---

## VII. Puritas

Gradus C:

- nullum `POLLE()` adhibet;
- nullum runtime C, C++, Rust aut ASM addit;
- `UEFI_VOCA6` intrinsecum VINDEX canonicum servat;
- hit-testing, mutatio mensurae, tractio, focus et compositio in VINDEX tenet;
- custodiam generalem `Sylvia VINDEX purum` non mutat.

---

## VIII. Relatio ad historiam

PR historica #59 probationem originalem Gradus C continebat, sed super veterem
pilam Gradus B posita erat. Haec reconciliatio directe ex `main` hodierno,
Gradu B iam canonico, nascitur et fontes VINDEX probatos selecte recipit sine
ascendentia veteris pilae.

Gradus D et posteriores eodem modo tantum post canonizationem huius gradus
reconciliabuntur.

---

## IX. Criterium canonizationis

CI requirit:

1. puritatem generalem Sylviae;
2. analysin staticam gestoris C et probationis resize;
3. praesentiam contractus marginum, minimorum et interactionis;
4. compilationem probationis resize in ELF64;
5. compilationem gestoris C integri in ELF64;
6. magnitudinem binarii intra limitem admissum;
7. absentiam `POLLE()`.

Si omnia transeunt, Gradus C fit fundamentum canonicum mutationis geometricae
Fenestralis II.

> VIA RECTA: geometria stabilis ante separationem clientium.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
