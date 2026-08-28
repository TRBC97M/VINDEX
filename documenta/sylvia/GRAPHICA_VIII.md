# GRAPHICA VIII — FUNDAMENTUM JL-UX

**Status:** ACTIVUM — SHOWROOM QEMU ET BASELINE PS/2 PROBATA  
**Ramus:** `chatgpt/capacitas-graphica-viii`

## I. Finis

Capacitas Graphica VIII non est skin neque wallpaper. Finis est motorem 2D Sylviae ita amplificare ut canon JL-UX sine pictura ad-hoc ex solis rectangulis exprimi possit.

Graphica VIII stratum inter applicationes/compositorem et backend graphicum constituit. Backend software framebuffer primus manet; contractus tamen ita ordinantur ut backend acceleratus postea addi possit sine grammatica UI iterum scribenda.

## II. Facultates huius incrementi

### Primitivae geometricae

- clipping rectangulorum;
- clamp/min/max communes;
- rectangula rotunda anti-aliased in framebuffer et superficies;
- umbra rotunda localis pro componentibus parvis;
- scaling nearest-neighbour;
- scaling bilinearis integer pro resampling qualitatis.

### Rastera

- scaling regionis SIMG RGBA8888 cum alpha globali;
- scaling in framebuffer et superficies privatas;
- compositio **novem partium / 9-slice** ad pannos, bullas, chrome et dialogos sine deformandis angulis;
- copia opaca inter superficies duobus pixelis per qword ubi licet.

### Damnum / redraw

`fenestrale_damage_viii.vindex` tenet plures regiones invalidas, regiones tangentia coalescit et solum ad bounding rect fallback facit cum capacitas saturatur. Hoc fundamentum est ut cursor, hover, drag et fenestrae non semper totum framebuffer redpingant.

### Typographia

`fenestrale_typographia_viii.vindex` introducit glyph atlas RGBA anti-aliased:

- font 8×8 historicus manet fallback;
- glyphi ex atlas cellulari sumi possunt;
- alpha atlas larvam glyphi definit;
- color glyphi runtime mutari potest;
- magnitudo destinationis libera est;
- idem renderer framebuffer et superficies clientium sustinet.

`fons_ui_viii.vindex` primum atlas UI compactum praebet. Glyphi 5×7 in `NUMERUS` conduntur et a VINDEX ipso in cellas 16×20 RGBA rasterizantur cum alpha interpolato. Hoc blob fontis externum vel concatenationem textus ingentem vitat. ASCII XXXII cellam omnino transparentem habet et hoc pixelatim probatione custoditur.

Hoc stratum viam aperit fontibus rasteris multi-magnitudinis et atlasibus subtilioribus sine amplificatione quadratorum 8×8.

### Coda commandorum

`fenestrale_commandos_viii.vindex` mandata graphica compacta a backend separat. Showroom easdem operationes per codam backend-neutram transmittit et hodie backend software framebuffer exsequitur. Hic contractus postea backend VirtIO-GPU recipere poterit sine grammatica componentium iterum scribenda.

## III. Responsivitas

Graphica VIII separat duas vias:

1. **via frequens** — copia opaca, superficies cached, dirty regions, primitiveae localiter alpha;
2. **via qualitatis** — bilinear, alpha raster et 9-slice ubi asset/componens id requirit.

Effectus pretiosus non debet per totum framebuffer ad omnem motum PS/2 iterari.

### Baseline PS/2 ante integrationem shell

`metire_murem_graphica_viii.py` QEMU/OVMF accendit sine mora initiali fixa, statum rectoris PS/2 `IX` exspectat, unum eventum calefactionis mittit, deinde XVI motus relativos per QMP injicit. Pro singulo motu tempus usque ad mutationem seriei eventuum in telemetria nuclei metitur.

Tres cursus in runneribus GitHub distinctis ante limen statuendum dederunt:

- cursus I: mediana telemetriae **29.641 ms**, p95 **29.696 ms**, maximum **29.696 ms**;
- cursus II: mediana telemetriae **28.882 ms**, p95 **31.217 ms**, maximum **31.217 ms**;
- cursus III: mediana telemetriae **28.827 ms**, p95 **32.380 ms**, maximum **32.380 ms**.

Tempus QMP fuit circa I–I.4 ms. Custodia definitiva nunc tempus **totale QMP → telemetria nuclei** probat cum liminibus deliberate laxioribus quam baseline:

- p95 ≤ **50 ms**;
- nullum specimen > **75 ms**.

Ita varietas runneris CI toleratur, sed regressio perceptibilis post integrationem Graphica VIII fit defectus testis, non impressio subjectiva.

## IV. Showroom QEMU/OVMF

Showroom dedicatum `showroom_graphica_viii.vindex` non est facies finalis Sylviae; facultates motoris isolatim demonstrat. Catena probata est:

`OVMF -> BOOTX64.EFI [VINDEX] -> SHOWROOM [VINDEX] -> GRAPHICA VIII -> FRAMEBUFFER`

In captura 1280×800 vera probantur inter alia:

- gradient framebuffer;
- pannos 9-slice cum accentibus aqua/aeneis;
- rectangula rotunda et umbrae;
- nearest scaling contra bilinear scaling;
- emblema SIMG RGBA scalarum;
- typographia atlas alpha-gradua;
- damage tracker et command queue.

Probatio automatica mensuravit nearest ad VI colores et bilinear ad circiter MCDXCVII colores, quo demonstratur interpolationem non esse alias nearest occultum.

## V. Backend acceleratus

VINDEX iam enumerationem PCI puram et primitivas portuum habet. Tamen BAR/MMIO, resource descriptors et interruptiones sunt pars P12 reservata et nondum canonica.

Graphica VIII **non fingit GPU accelerationem quae nondum exsistit**. Architectura tamen backend-neutra ordinatur, ut post canonizationem BAR/MMIO primus backend acceleratus probabilis sit **VirtIO-GPU sub QEMU/OVMF**.

Ordo intentus:

1. renderer software maturus et probatus;
2. damage tracking et caches in compositore;
3. contractus commandorum/superficierum stabilis;
4. BAR/MMIO P12 canonicum;
5. VirtIO-GPU 2D/resource scanout;
6. postea investigatio hardware physici secundum machinam referentiae P13.

Driver NVIDIA/AMD plenus non est conditio ad JL-UX: compositor 2D acceleratus et renderer software maturus primum valorem realem praebent.

## VI. Invarianta

- omnia runtime Sylviae in VINDEX manent;
- nulla bibliotheca C/C++ externa in catena canonica;
- QEMU/OVMF framebuffer verus manet auctoritas visualis;
- P16-VIII/P16-IX non mutantur donec Graphica VIII satis probata est;
- hitbox et semantica non mutantur sub nomine graphicae;
- probationes non solvuntur mora artificialiter aucta;
- responsivitas PS/2 post integrationem contra baseline mensuratum custoditur.

## VII. Portae adoptionis

Graphica VIII in `main` non mergitur nisi:

1. probationes puras clipping/damage/typographiae transeunt;
2. primitiveae superficierum vere exercentur;
3. regressiones Graphica VII manent virides;
4. showroom sub QEMU ostendit rectangula rotunda, raster scaling et 9-slice in framebuffer vero;
5. p95/max PS/2 intra limina 50/75 ms manent;
6. documentatio et custodia architectonica concordant.

## VIII. Non finis

Graphica VIII non declarat JL-UX perfectum. Post fundamentum sequuntur asseta iconographica maiora, fontes UI subtiliores/multi-magnitudinis, componentes communes, compositor dirty-region, deinde renovatio Bureau/INITIUM/taskbar/fenestrarum.

**Sententia:** prius instrumenta digna construimus; deinde Sylvia eis pingitur.
