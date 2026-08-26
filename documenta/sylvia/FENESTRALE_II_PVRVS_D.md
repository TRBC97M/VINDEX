# FENESTRALE II PVRVS — GRADVS D
## Superficies privata clientis

**Status:** candidatus canonicus  
**Series:** Fenestrale II Purus  
**Gradus:** D  
**Fundamentum:** Gradus C in `main` canonicus

---

## I. Propositum

Gradus D primam separationem veram inter ornamentum fenestrae et contentum
clientis introducit. Gestor Fenestralis fenestram, focum, ordinem Z, geometriam
et compositionem possidet; cliens PROGRAMMATA contentum suum in superficie
privata VINDEX pingit.

Hoc gradus fundamentum est ad applicationes quae proprium spatium graphicum
habent sine dominio directo totius framebuffer.

---

## II. Bibliotheca superficierum

`bibliotheca/fenestrale_ii_superficies.vindex` superficies XXXII bit definit.
Caput superficiei latitudinem, altitudinem, stride, indicem pixelorum et
regionem laesam continet.

Primitivae principales sunt:

- `FS_CREA` — memoriam capitis et pixelorum per `RESERVA_OCTETA` reservat;
- `FS_PIXEL` — unum pixelum scribit;
- `FS_RECT` — rectangulum intra superficiem pingit;
- `FS_TEXTUM` — textum VIII×VIII in superficie pingit;
- `FS_BLIT` — superficiem clientis in framebuffer componit atque resecat;
- `FS_PROGRAMMATA_RENDE` — exemplum clientis PROGRAMMATA in superficie sua pingit.

Bibliotheca folium est et nullam aliam bibliothecam importat; fons principalis
dependentias graphicas communes ante eam importat.

---

## III. Separatio clientis et systematis

Gradus D statum `s[30]` ad superficiem privatam PROGRAMMATA reservat.
`PRINCIPALIS` superficiem CCCCXCVI × CCLX pixelorum creat et clientem semel
per `FS_PROGRAMMATA_RENDE` pingit.

`FD_PROGRAMMATA` ornamentum systematis per `FV_FENESTRA` pingit, deinde
`FS_BLIT` contentum clientis intra corpus fenestrae componit. Area composita
ad dimensiones visibiles fenestrae resecaretur.

TABULA hoc gradu adhuc via directa bibliothecae communis pingitur. Migratio
clientium deliberatim gradatim fit.

---

## IV. Continuitas geometriae

Gradus D contractum Gradus C servat:

- focus et ordo Z;
- tractio fenestrae;
- minimizatio et restitutio;
- maximizatio et restitutio;
- clausura;
- mutatio mensurae per margines et angulos;
- limites monitoris et barra operum XXVIII pixelorum.

Superficies privata hanc geometriam non possidet. Gestor decernit ubi et
quantum clientis visibile componatur.

---

## V. Memoria

`FS_CREA` structuram capitis LXIV octetorum et regionem pixelorum `w × h × IV`
octetorum separatam reservat. Haec prima memoria graphica privata clientis
Fenestralis II est.

Regio laesa in capite iam locum habet, quamvis hic gradus compositionem adhuc
simplicem et immediatam faciat. Gradus posteriores hunc contractum ad
redintegrationem partialem evolvere possunt.

---

## VI. Puritas

Gradus D:

- nullum `POLLE()` adhibet;
- nullum runtime C, C++, Rust aut ASM addit;
- allocationem superficiei per intrinseca VINDEX facit;
- picturam clientis et blit in VINDEX implet;
- input, geometriam, ornamentum et compositionem in VINDEX retinet;
- custodiam generalem `Sylvia VINDEX purum` non mutat.

---

## VII. Relatio ad historiam

PR historica #60 probationem originalem Gradus D continebat, sed super veterem
pilam Gradus C posita erat. Haec reconciliatio directe ex `main` hodierno,
Gradibus A, B et C iam canonicis, nascitur et fontes VINDEX probatos selecte
recipit sine ascendentia veteris pilae.

Intrinsecum `RESERVA_OCTETA` ante hunc gradum in verificatore R5 cum compilatore
canonico reconciliatum est; Gradus D nullam exceptionem verificatoris requirit.

---

## VIII. Criterium canonizationis

CI requirit:

1. puritatem generalem Sylviae;
2. analysin staticam gestoris D et probationis superficiei;
3. contractum `FS_CREA`, `FS_RECT`, `FS_TEXTUM`, `FS_BLIT` et clientis privatam;
4. compilationem probationis superficiei in ELF64;
5. compilationem gestoris D integri in ELF64;
6. magnitudinem binarii intra limitem admissum;
7. absentiam `POLLE()`.

Si omnia transeunt, Gradus D fit primum fundamentum canonicum separationis
clientis et gestoris Fenestralis II.

> VIA RECTA: cliens pingit; systema componit.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
