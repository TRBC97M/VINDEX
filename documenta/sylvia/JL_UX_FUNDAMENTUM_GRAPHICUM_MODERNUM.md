# JL-UX — FUNDAMENTUM GRAPHICUM MODERNUM

**Sylvia OS — P16-XII**  
Status: **P16-XII-A et P16-XII-B PERFECTA; P16-XII-C ACTIVUM, C1 PROBATUM / CANONIZANDUM**

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

Framebuffer GOP potest ordinem canalium mutare; conversio fit tantum in limite backendis. Memoria Graphica X manet canonica RGBA. Color iam per `FV_COLOR` ad ordinem GOP conversus **numquam** in superficiem `GX_*` ponendus est; hoc invarians P16-XII-B captura QEMU explicite confirmavit.

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

Blur et umbrae magnae non singulis frameis recreandae sunt. Lex productionis est:

- effectus staticus → cache;
- mutatio contenti → nova generatio fontis et invalidatio naturalis clavis cache;
- resize → recrea cache necessarium;
- compositio → damage tantum praesentat;
- blur late diffusum sine causa vitatur;
- radius blur secundum aream superficiei coerceri potest.

P16-XII-C1 hanc legem iam exsequitur per gestorem `XP_*` cum hit/miss, cache umbrarum et backdrop, blur adaptivo, maska alpha, clipping materializato et gloss reutilizabili.

Implementatio software est backend referentiae et veritatis semanticae, non finis accelerationis.

## VII. Via ad accelerationem GPU

P16-XII debet API compositoris ita definire ut backend CPU hodiernus postea a backend GPU substitui possit sine mutatione semantica shellis.

Ordo intentus:

1. backend software VINDEX purus sub QEMU ut referentia;
2. coda mandatorum Graphica VIII/Graphica X ad operationes compositionis extenditur;
3. superficies et effectus backend-neutri manent;
4. post fundamenta P12 BAR/MMIO/interruptiones, backend hardware acceleratus addi potest;
5. copia CPU↔GPU et cache texturarum minimantur.

**Acceleratio GPU non est condicio primae certificationis P16-XII; architectura quae eam impedit vetita est.**

## VIII. Gradus P16-XII

### P16-XII-A — Compositor RGBA

**Status: PERFECTUM per #146.**

- `GX_*` superficies;
- source-over;
- damage regionale;
- blur, umbra, vitrum;
- showroom QEMU/OVMF.

### P16-XII-B — Scena compositoris

**Status: PERFECTUM per #148; #147 historiam draft servat.**

- registrum dynamicum stratorum;
- Z ordinatum et mutabile runtime;
- x/y, visibilitas et opacitas per stratum;
- backbuffer GX plenum;
- recompositio tantum regionum laesarum;
- praesentia framebuffer tantum regionis laesae;
- prima forma double buffering: compositio off-screen completur ante praesentiam;
- canarii framebuffer probant regionem extra damage non repingi;
- locus vetus post motum ex fundo et Z ordine recte restituitur.

### P16-XII-C — Effectus productionis

**Status: ACTIVUM; C1 PROBATUM / CANONIZANDUM per #149.**

C1 iam instituit:

- cache umbrarum;
- backdrop cache cum generatione fontis in clave;
- blur adaptivum secundum aream;
- gloss/highlight reutilizabile;
- maskam alpha praemultiplicatam;
- clipping materializatum;
- hit/miss et capacitatem gestorii cache.

C2 proximum est:

- pontem rasterae premium Graphica IX/SIMG II → superficies GX;
- 9-slice materialem in superficie compositoris;
- contractum quo chrome JL-UX raster premium sine framebuffer directo reddi possit.

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

P16-XII-A sub QEMU/OVMF certificavit:

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

## XI. Probationes P16-XII-B

Scena compositoris separatim probat logicam in memoria et presentationem in framebuffer vero.

Probatio VINDEX nativa confirmat:

- compositionem Z `source-over`;
- mutationem Z runtime;
- motum cum unione loci veteris et novi;
- visibilitatem et opacitatem per stratum;
- backbuffer intactum extra damage;
- parvum motum qui tantum **LXXX pixela** recomponit, non totam scenam.

Showroom QEMU/OVMF 1280×800 rettulit:

```text
colores framebuffer: 699
canarius extra damage: (181,138,84) — servatus
locus vetus restitutus: (32,91,112)
stratum A: (14,115,136)
overlap/Z: (107,73,45)
stratum B: (107,69,41)
umbra, lumen locale: 170 / 235
XXXV probationes canonicae: 35 / 35
```

Captura inspecta est. Aqua et bronzeum ordinem colorum rectum servant; canarius extra damage post secundam praesentiam manet; canarius intra locum veterem deletur; umbra est stratum separatum infra panel; compositor regionem laesam tantum praesentat.

## XII. Probationes P16-XII-C1

Probatio VINDEX nativa confirmat:

- radius blur adaptivus `20 / 12 / 8` pro areis parva/media/magna;
- eandem umbram bis petitam eandem superficiem cacheatam reddere;
- backdrop eadem generatione cache hit dare;
- mutationem fontis generationem mutare et backdrop novum producere;
- maskam alpha canales praemultiplicatos simul minuere;
- clip mensuram et pixelum originis exactum servare;
- gloss partem superiorem illuminare sine parte inferiore mutata.

Showroom QEMU/OVMF 1280×800 capitis `512d470d…` rettulit:

```text
colores framebuffer: 1587
contrastus extra/intra backdrop: 11.20 / 0.60
masca, angulus/centrum: (6,14,23) / (18,123,147)
gloss, lumen supra/infra: 380 / 273
umbra cacheata, lumen: 37 / 46
cache showroom: duo hit / duo miss / duo nodi
XXXV probationes canonicae: 35 / 35
```

Captura framebuffer inspecta est. Backdrop strias vere mollit; anguli maskae ad fundum redeunt; highlight superior clarus sed localis est; clip intra limites suos manet; eadem umbra cacheata in pluribus stratis reutilizatur.

## XIII. Invarianta

- nulla regressio in `FS_*` clientium;
- nullum C in runtime Sylviae;
- nulla copia servilis Aero/Vista;
- canon JL-UX manet auctoritas artis;
- imago conceptus est scopus visualis, QEMU est auctoritas executionis;
- wallpaper non substituit motorem;
- effectus non iustificant input lentum;
- memoria GX semper RGBA canonica manet; conversio GOP tantum in limite framebufferis fit;
- effectus cacheatus non iterum calculatur nisi clavis vel generatio fontis mutatur.

## XIV. Sententia

**Non picturam pulchram supra motorem infirmum ponimus. Motorem facimus dignum Sylvia.**
