# FENESTRALE II PVRVS — GRADVS D

## Propositum

Gradus D primam separationem veram inter ornamentum fenestrae et contentum clientis introducit. PROGRAMMATA iam non totum a gestore desktop directe pingitur: systema ornamentum fenestrae possidet, dum contentum PROGRAMMATA in superficie privata VINDEX propria pingitur.

Haec separatio fundamentum clientium Fenestralis II constituit sine runtime alienae linguae.

## Superficies privata

Bibliotheca nova:

- `bibliotheca/fenestrale_ii_superficies.vindex`

superficiem clientis in memoria VINDEX creat et administrat.

Caput superficiei LXIV octeta continet:

- latitudinem;
- altitudinem;
- numerum pixelorum per lineam;
- indicem memoriae pixelorum;
- rectangulum mutationis destinatum futuris regionibus laesis.

Pixela sunt XXXII bit et eadem forma coloris qua framebuffer nativus utitur.

## Primitivae

Bibliotheca Gradus D praebet:

- `FS_CREA` — superficiem et memoriam pixelorum reservat;
- `FS_PIXEL` — unum pixelum scribit;
- `FS_RECT` — rectangulum intra superficiem pingit;
- `FS_TEXTUM` — textum bitmap in superficie pingit;
- `FS_BLIT` — contentum superficiei in framebuffer transfert;
- `FS_PROGRAMMATA_RENDE` — primum clientem PROGRAMMATA in superficie sua pingit.

## PROGRAMMATA ut cliens

In `systema/fenestrale_ii_purus_d.vindex`, PROGRAMMATA superficiem privatam CCCCXCVI × CCLX px accipit.

Gestor Fenestralis:

1. fenestram et barram tituli per `FV_FENESTRA` pingit;
2. contentum PROGRAMMATA per `FS_BLIT` intra corpus fenestrae componit;
3. superficiem ad dimensionem visibilem fenestrae resecat;
4. focus, z-order, tractio et mutatio mensurae systemati manent.

Ita clientis contentum et ornamentum systematis iam sunt conceptus distincti.

TABULA in hoc gradu adhuc via directa veteris bibliothecae VINDEX pingitur. Hoc consulto fit ut transitus gradatim probari possit.

## Continuitas interactionis

Gradus D interactionem Gradus C servat:

- click-to-focus;
- z-order;
- tractio per barram tituli;
- minimizatio et restitutio;
- maximizatio et restitutio;
- clausura;
- mutatio mensurae per margines et angulos;
- `Tab`, sagittae et `Esc`.

Taskbar XXVIII px et fenestrae quadratae permanent.

## Regiones laesae

Caput superficiei iam locum rectanguli mutationis continet, sed Gradus D adhuc totam superficiem clientis componit. Structura data consulto parata est ut Gradus proximus regiones laesas vere adhibere possit.

Nulla affirmatio fit de compositione partiali nondum impleta.

## Puritas

Post bootstrap UEFI:

- memoria superficiei a VINDEX reservatur;
- clientis pictura est VINDEX;
- blit est VINDEX;
- ornamentum fenestrae est VINDEX;
- input et geometria sunt VINDEX;
- nullum `POLLE()` adhibetur;
- nullus runtime C, C++, Rust aut ASM introducitur.

## Limites Gradus D

Superficies PROGRAMMATA nunc mensuram fixam CCCCXCVI × CCLX px habet. Fenestra maior spatium reliquum systematis ostendere potest; fenestra minor superficiem resecat.

Gradus proximus potest:

- superficiem clientis cum mutatione mensurae recreare vel amplificare;
- regiones laesas vere componere;
- eventa focus et dimensionis clientibus tradere;
- TABULA ad eandem separationem clientis migrare.

## Dependentiae Git

Gradus D super Gradum C ponitur. Gradus C super Gradum B, Gradus B super Gradum A, et Gradus A super correctionem architectonicam VINDEX puram PR #30 nititur. Haec series stacked draft manet donec fundamenta canonica facta sunt.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
