# FENESTRALE II — PVRVS B
## Interactio fenestrarum in VINDEX canonico

**Status:** candidatus canonicus  
**Series:** Fenestrale II Purus  
**Gradus:** B  
**Fundamentum:** Gradus A in `main` canonicus

---

## I. Propositum

Gradus B fundamentum graphicum Gradus A in primum gestorem fenestrarum
interactivum extendit. Omnis logica post initium UEFI in VINDEX manet.

Hic gradus non est facies finalis Sylviae. Propositum eius est contractus
interactionis: input, focus, ordo fenestrarum, motus et actiones fundamentales.

---

## II. Bibliotheca communis

`bibliotheca/fenestrale_ii_purus.vindex` primitivas communes continet:

- metadata framebuffer;
- conversionem coloris RGB/BGR;
- pixelum et rectangulum;
- textum VIII×VIII;
- globulos;
- ornamentum fenestrae;
- fundum desktop;
- barram operum;
- cursorem.

Bibliotheca eundem contractum metadatae UEFI quem Gradus A et ponticulus
canonicus hodiernus adhibet. Quia bibliotheca ipsa `FUNCTIO PRINCIPALIS` non
habet, per probationem `fenestrale_purus_b_graphica.vindex`, quae eam importat,
analysatur et compilatur.

---

## III. Gestor interactivus

`systema/fenestrale_ii_purus_b.vindex` super bibliothecam communem addit:

- statum duarum fenestrarum demonstrativarum;
- focum fenestrae;
- ordinem Z et elevationem ad summam;
- detectionem regionum activarum (`HIT`);
- tractionem et motum fenestrae;
- minimizationem;
- maximizationem et restitutionem;
- clausuram;
- restitutionem e barra operum;
- cursorem interactivum;
- recreationem desktop post mutationem status.

PROGRAMMATA et TABULA manent exempla huius gestoris, non limites futuri
systematis fenestrarum.

---

## IV. Input

Gradus B input UEFI nativum adhibet. `UEFI_VOCA6` conventionem Microsoft x64
pro ministeriis firmware servat.

Input claviaturae semper praesto est:

- sagittae cursorem movent;
- `ENTER` actionem cursoris excitat;
- `TAB` focum mutat;
- `SPACE` PROGRAMMATA minuit aut restituit;
- `ESC` TABULA claudit.

Pons metadatae muris, si adest, legi potest; absentia eius claviaturam non
impedit. Gradus posteriores hunc pontem input in subsystema plenius
transformabunt.

---

## V. Probationes separatae

Sex fontes probationis partes ante corpus integrum compilant:

- `fenestrale_purus_b_graphica.vindex` — bibliotheca graphica;
- `fenestrale_purus_b_gestor.vindex` — status et gestor;
- `fenestrale_purus_b_input.vindex` — input UEFI;
- `fenestrale_purus_b_interactio.vindex` — actiones et hit-testing;
- `fenestrale_purus_b_ansa.vindex` — ansa interactionis;
- `fenestrale_purus_b_principalis.vindex` — compositio principalis.

Haec divisio regressionem localem facilius detegit quam sola compilatio
systematis integri.

---

## VI. Puritas

Gradus B:

- nullum `POLLE()` utitur;
- nullum compositorium C, C++, Rust aut ASM invocat;
- compilatorem VINDEX canonicum e `main` directe utitur;
- bibliothecam et gestorem in VINDEX definit;
- custodiam generalem `Sylvia VINDEX purum` non mutat.

---

## VII. Relatio ad historiam

PR historica #33 probationem originalem Gradus B continebat, sed in pila
ramorum veterum fundata erat. Hic Gradus B ex `main` hodierno nascitur et
bloba VINDEX iam probata selecte reconciliat sine historia veteris pilae.

Gradus C et posteriores tantum post canonizationem huius Gradus B similiter
reconciliabuntur.

---

## VIII. Criterium canonizationis

CI requirit:

1. puritatem generalem Sylviae;
2. analysin staticam gestoris et probationum exsecutabilium, bibliotheca per probationem graphicam;
3. compilationem sex probationum separatarum;
4. compilationem gestoris integri;
5. ELF64 validum intra magnitudinem admissam;
6. praesentiam contractuum interactionis principalium;
7. absentiam `POLLE()`.

Si omnia transeunt, Gradus B fit fundamentum interactionis canonicum pro
Fenestrale II.

> VIA RECTA: singuli gradus, singula probatio, una veritas canonica.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
