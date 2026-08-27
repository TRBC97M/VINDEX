# INITIUM II — Menu Systematis Sylviae Functionale

## Finis

P16-II regionem `INITIUM`, quae in P16-I tantum forma taskbaris erat, in menu systematis vere interactive vertit.

Hoc incrementum non simulacrum graphice tantum addit. Apertio, hover, electio applicationis, restitutio fenestrae et focus per eandem catenam input nativam Fenestralis exercentur.

Catena probata manet:

```text
OVMF → BOOTX64.EFI [VINDEX] → FENESTRALE II [VINDEX] → PS/2 [VINDEX] → FRAMEBUFFER
```

Nullum C in hac via residet.

---

## Contractus visualis

Menu INITIUM supra taskbar P16-I pingitur.

Metra canonica:

- latitudo: `CCCXX` px;
- altitudo: `CCLX` px;
- caput: `LX` px;
- altitudo unius tesserae applicationis: `XLIV` px;
- taskbar manet `XL` px;
- pannus incipit ad `x = 6` et immediate supra taskbar terminatur.

Caput nomen `SYLVIA` et subtitulum `SYSTEMA VINDEX` ostendit. Corpus sectionem `APPLICATIONES` et saltem duas tesserae canonicas continet:

1. `PROGRAMMATA`;
2. `TABULA`.

Tessera sub cursore colorem `argentum` accipit; focus fenestrae electae per marginem `bronzeum` manifestatur.

---

## Contractus status

Status aperturae INITIUM in campo `s[38]` vectoris systematis servatur:

- `0` — menu clausum;
- `1` — menu apertum.

Clic in regione INITIUM taskbaris statum alternat.

Clic extra pannum menu claudit. Clic intra pannum sed extra tesseras applicationum pannum non frangit. Electio applicationis menu claudit post actionem.

---

## Contractus applicationum

P16-II nondum processum novum creat. INITIUM operatur super applicationes canonicas iam registratas in Fenestrale.

Cum tessera eligitur:

1. Fenestram ad clientem respondentem in registro quaerit;
2. si minimizata est, statum ad `0` restituit;
3. `FI_FOCUS` vocat;
4. fenestram ad summum ordinem Z transfert;
5. menu INITIUM claudit.

Hoc contractum facit ut P16-III postea creationem veram applicationum addere possit sine mutando semanticam menu iam probatam.

---

## Probatio input realis

`instrumenta/proba_initium_sylviae_ii.py` non coordinatas cursoris fingit. Cursor ex ipsa pictura framebuffer quaeritur per signaturam cursoris Sylviae, deinde per fasciculos PS/2 parvos ad scopum movetur.

Probatio QEMU/OVMF canonica observavit:

```text
cursor_init    = (640, 400)
cursor_INITIUM = (50, 770)
cursor_TABULA  = (150, 650)
```

Post clic INITIUM:

- pannus vere apparet;
- `85059` pixeli a pictura antecedente differunt;
- hover TABULA ad colorem `(185,196,207)` transit.

Post clic TABULA:

- menu clauditur;
- TABULA focus accipit;
- margo focus est `(185,138,82)`;
- `152712` pixeli inter statum apertum et statum post electionem differunt.

---

## Custodia regressionis

P16-II simul retinet:

- XXIX/XXIX probationes canonicas;
- P16-I: taskbar XL px, titulus XXXVI px, textus 2×;
- Fenestrale II sub UEFI;
- PS/2 nativum;
- puritatem runtime sine C.

Probatio `proba_initium_sylviae_ii.py` in `VINDEX — Catena UEFI pura` inseritur. Ergo regressio futura in apertione INITIUM, hover, PS/2 vel focus applicationis CI frangere debet.

---

## Finis huius incrementi

P16-II definit **menu systematis functionale minimum**.

Non adhuc definit:

- creationem applicationis quae nulla fenestra aperta habet;
- iconas escritorio interactivos;
- duplex clic;
- registrum applicationum generatum;
- quaestionem/search;
- sessiones aut potentiam systematis;
- animationes.

Haec sunt incrementa posteriora P16.

**INITIUM iam non est ornamentum. Est prima porta systematis Sylviae ad applicationes suas.**
