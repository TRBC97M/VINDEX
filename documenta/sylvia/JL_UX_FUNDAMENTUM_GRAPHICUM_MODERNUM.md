# JL-UX — FUNDAMENTUM GRAPHICUM MODERNUM

**Sylvia OS — P16-XII**  
Status: **P16-XII-A PROBATUM / CANONIZANDUM**

## I. Propositum

P16-XII non est thema, wallpaper neque mutatio iconarum. Propositum est ipsum substratum graphicum Sylviae ad facultatem systematis desktop moderni elevare, ordine capacitatis comparabili cum aevo Windows Vista/Aero, sine imitatione identitatis alienae.

Identitas manet Sylvia et canon JL-UX. Comparatio cum Vista significat **vim technicam**: compositio alpha, umbrae molles, vitrum, blur locale, strata, animationes, caches et backend graphicum accelerabile.

## II. Diagnosis

Graphica VIII et IX iam canonice dederunt clipping, anti-aliasing, scaling, 9-slice, typographiam atlas, damage tracking, superficies privatas, cache RGBA et interpolationem bilinearem alpha praemultiplicatam.

Sed superficies clientium `FS_*` historice RGB opacae manent. Quartum octetum pixelorum non est alpha semanticum, et praesentatio plerumque blit/copia est. Hoc satis est applicationibus hodiernis, non compositori vitreo pleno.

P16-XII igitur **novam familiam `GX_*` addit**; `FS_*` non frangitur. Migratio shellis et clientium fit gradatim.

## III. Lex pixelorum

Superficies Graphica X servant:

```text
RGBA8888 canonicum
alpha verum 0..255
RGB praemultiplicatum per alpha
```

Compositio utitur regula `source-over` praemultiplicata. Pixel alpha=0 nullum colorem occultum in framebuffer emittere potest.

Framebuffer GOP potest ordinem canalium mutare; conversio fit tantum in limite backendis. Memoria Graphica X manet canonica RGBA.

## IV. Descriptor superficiei

`GX_CREA(w,h)` creat superficiem XCVI-octetorum cum:

- mensura et stride;
- basi pixelorum RGBA;
- recto damage regionali;
- vexillo damage;
- generatione mutationum;
- spatio vexillorum futurorum.

Superficies initio vere translucida est. Damage non statim totam superficiem contaminat: mutationes rectangulares uniuntur.

## V. Capacitas incrementi A

Prima tranche P16-XII instituit:

1. superficies RGBA praemultiplicatas;
2. compositionem surface → surface;
3. compositionem surface → framebuffer;
4. global alpha per stratum;
5. capturam framebuffer → RGBA;
6. damage regionale;
7. blur separabile RGBA;
8. umbram mollem ex alpha;
9. vitrum locale per backdrop blur + tincturam;
10. strata translucentia se mutuo componentia.

Haec non sunt ornamenta hard-coded shellis; sunt primitive compositoris reutilizabiles.

## VI. Effectus et cache

Blur et umbrae magnae non singulis frameis recreandae sunt. Lex productionis erit:

- effectus staticus → cache;
- mutatio contenti → invalida tantum regionem affectam;
- resize → recrea cache necessarium;
- compositio → damage tantum praesentat;
- blur late diffusum sine causa vitatur.

Implementatio software est backend referentiae et veritatis semanticae, non finis accelerationis.

## VII. Via ad accelerationem GPU

P16-XII debet API compositoris ita definire ut backend CPU hodiernus postea a backend GPU substitui possit sine mutatione semantica shellis.

Ordo intentus:

1. backend software VINDEX purus sub QEMU ut referentia;
2. coda mandatorum Graphica VIII/Graphica X ad operationes compositionis extenditur;
3. superficies et effectus backend-neutri manent;
4. post fundamenta P12 BAR/MMIO/interruptiones, backend hardware acceleratus addi potest;
5. copia CPU↔GPU et cache texturarum minimantur.

**Acceleratio GPU non est condicio primae certificationis P16-XII-A; architectura quae eam impedit vetita est.**

## VIII. Gradus P16-XII

### P16-XII-A — Compositor RGBA

**Status: PROBATUM / CANONIZANDUM.**

- `GX_*` superficies;
- source-over;
- damage regionale;
- blur, umbra, vitrum;
- showroom QEMU/OVMF.

### P16-XII-B — Scena compositoris

- registrum stratorum;
- Z ordinatum;
- opacitas et transformata per stratum;
- compositio tantum regionum laesarum;
- double buffering/presentatio stabilis.

### P16-XII-C — Effectus productionis

- cache umbrarum;
- backdrop cache;
- blur adaptivus;
- gloss/highlight;
- maskae et clipping per stratum;
- 9-slice materialis super Graphica IX.

### P16-XII-D — Tempus et motus

- horologium frame;
- interpolationes;
- apertura/clausura/focus/hover;
- transitus breves et interruptibiles;
- nulla animatio input tardat.

### P16-XII-E — Migratio shellis

- fenestrae in strata composita;
- chrome JL-UX;
- INITIUM;
- taskbar;
- cursor;
- Bureau;
- clientium migrationes ubi utile est.

### P16-XII-F — Backend accelerabilis

- contractus backend explicatus;
- batching/coda;
- texturarum cache;
- via GPU cum infrastructura hardware id sinit.

## IX. Criterium Vista-class

P16-XII totum non dicitur perfectum quia unum panel translucet. Ante conclusionem, motor debet posse:

- plures fenestras RGBA simul componere;
- umbras molles cacheatas ostendere;
- backdrop blur regionalem sine halo praebere;
- translucidentiam et overlap recte miscere;
- resize/motus sine scintillatione gerere;
- effectus cum damage regionali non totum framebuffer frustra recreare;
- animationes UI stabili frame-clock regere;
- backend mutabilem sine mutatione theme/shell servare.

## X. Probationes P16-XII-A

Prima tranche requirit:

1. compilationem per compilatorem VINDEX nativum;
2. probationes matheseos RGBA/source-over;
3. probationem damage regionalis;
4. probationem blur et umbrae in memoria;
5. XXXV regressiones canonicas;
6. puritatem Sylviae;
7. showroom QEMU/OVMF verum;
8. metrum quod blur contrastum texturae minuit et colores intermedios creat;
9. metrum umbrae mollis;
10. metrum overlap duorum stratorum translucentium;
11. capturam framebuffer inspectam.

Omnia haec in capite `1e09e737…` probata sunt. Showroom verus 1280×800 rettulit:

```text
colores framebuffer: 881
vitrum: 2 → 5 tonos
contrastus texturae: 104 → 2
umbra, lumen locale: 216 / 251
overlap: aqua (15,113,135)
         mixtum (116,111,84)
         bronzeum (117,86,55)
XXXV probationes canonicae: 35 / 35
```

Captura framebuffer inspecta est: striae post vitrum localiter molliuntur, umbra externa gradatim evanescit et regio duorum stratorum tertium colorem compositum ostendit. Showroom est probatio motoris, non propositum artis finalis Sylviae.

## XI. Invarianta

- nulla regressio in `FS_*` clientium;
- nullum C in runtime Sylviae;
- nulla copia servilis Aero/Vista;
- canon JL-UX manet auctoritas artis;
- imago conceptus est scopus visualis, QEMU est auctoritas executionis;
- wallpaper non substituit motorem;
- effectus non iustificant input lentum.

## XII. Sententia

**Non picturam pulchram supra motorem infirmum ponimus. Motorem facimus dignum Sylvia.**
