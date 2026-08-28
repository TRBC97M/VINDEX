# GRAPHICA VIII — FUNDAMENTUM JL-UX

**Status:** ACTIVUM  
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

Hoc stratum viam aperit fontibus rasteris multi-magnitudinis sine amplificatione quadratorum 8×8.

## III. Responsivitas

Graphica VIII separat duas vias:

1. **via frequens** — copia opaca, superficies cached, dirty regions, primitiveae localiter alpha;
2. **via qualitatis** — bilinear, alpha raster et 9-slice ubi asset/componens id requirit.

Effectus pretiosus non debet per totum framebuffer ad omnem motum PS/2 iterari.

## IV. Backend acceleratus

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

## V. Invarianta

- omnia runtime Sylviae in VINDEX manent;
- nulla bibliotheca C/C++ externa in catena canonica;
- QEMU/OVMF framebuffer verus manet auctoritas visualis;
- P16-VIII/P16-IX non mutantur donec Graphica VIII satis probata est;
- hitbox et semantica non mutantur sub nomine graphicae;
- probationes non solvuntur mora artificialiter aucta.

## VI. Portae adoptionis

Graphica VIII in `main` non mergitur nisi:

1. probationes puras clipping/damage/typographiae transeunt;
2. primitiveae superficierum vere exercentur;
3. regressiones Graphica VII manent virides;
4. compositor demo vel facies Sylviae sub QEMU ostendit rectangula rotunda, raster scaling et 9-slice in framebuffer vero;
5. mensura redraw demonstrat nullam regressionem PS/2 intolerabilem;
6. documentatio et custodia architectonica concordant.

## VII. Non finis

Graphica VIII non declarat JL-UX perfectum. Post fundamentum sequuntur asseta iconographica maiora, font atlas realis, componentes communes, compositor dirty-region, deinde renovatio Bureau/INITIUM/taskbar/fenestrarum.

**Sententia:** prius instrumenta digna construimus; deinde Sylvia eis pingitur.
