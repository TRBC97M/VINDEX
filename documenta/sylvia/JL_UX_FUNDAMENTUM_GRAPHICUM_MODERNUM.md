# JL-UX — FUNDAMENTUM GRAPHICUM MODERNUM

**Sylvia OS — P16-XII**  
Status: **P16-XII-A–D PERFECTA; P16-XII-E PROBATUM / CANONIZANDUM; P16-XII-F ACTIVUM**

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

Graphica IX rasteram SIMG II in RGBA recto bilineari reddit. P16-XII-C2 hoc RGBA in limite `GXX_*` semel praemultiplicat et deinde in GX componit. Ita rastera premium et compositor modernus eandem legem pixelorum participant sine conversione GOP intermedia.

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

P16-XII-C1 hanc legem exsequitur per gestorem `XP_*` cum hit/miss, cache umbrarum et backdrop, blur adaptivo, maska alpha, clipping materializato et gloss reutilizabili.

P16-XII-C2 addit pontem `GXX_*`: rastera premium SIMG II/Graphica IX directe in superficies GX redduntur, etiam per 9-slice, alpha recto in praemultiplicatum semel converso. Materia rastera igitur potest postea uti eodem Z, damage, cache, opacitate et backend-neutro compositore ac cetera strata.

Implementatio software est backend referentiae et veritatis semanticae, non finis accelerationis.

## VII. Tempus et motus

P16-XII-D separat **tempus logicum** a numero imaginum re vera praesentatarum.

Familia `TX_*` definit horologium backend-neutrum. Backend UEFI hodiernus utitur:

- `EFI_BOOT_SERVICES.CreateEvent` et `SetTimer` ad pacing atque telemetriam;
- `CheckEvent` tantum non-obstruenter, ideo ansa UI numquam eventum timeris exspectat;
- TSC x86-64 monotono ut fonte temporis animationis;
- calibratione semel facta per `BootServices.Stall(10 ms)` ante ansam UI.

Rutina TSC tredecim octetorum (`LFENCE; RDTSC; SHL RDX,32; OR RAX,RDX; RET`) a VINDEX ipso in memoria runtime scribitur et per vocatorem nativum existentem exercetur. Nullus assembler externus, nullum C et nulla mutatio compilatoris requiruntur.

**Lex temporis:** signum UEFI non est frame. Si renderer software periodum 16.67 ms superat, `TX_*` frame logicum ex tempore TSC elapso statim ad praesentem positionem promovet. Frames presentationis omitti possunt; tempus animationis non retardatur.

Familia `MX_*` motus stratorum regit:

- interpolatione fixed-point 16.16 ad proximum rotundata;
- curva lineari, ease-out cubica et smoothstep;
- x, y et alpha uno motu;
- duratione in frameis logicis temporalibus;
- retargetatione ex statu composito praesenti;
- nullo saltu cum meta inter motum mutatur;
- nullo opere si eadem frame bis pulsatur;
- mutationibus compositoris tantum ubi valor re vera mutatus est.

Hoc contractum backend-neutrum manet: futurus HPET/APIC, compositor GPU vel vsync alium fontem temporis praebere poterit sine mutatione semantica `MX_*`.

## VIII. Via ad accelerationem GPU

P16-XII debet API compositoris ita definire ut backend CPU hodiernus postea a backend GPU substitui possit sine mutatione semantica shellis.

Ordo intentus:

1. backend software VINDEX purus sub QEMU ut referentia;
2. coda mandatorum Graphica VIII/Graphica X ad operationes compositionis extenditur;
3. superficies, effectus et motus backend-neutri manent;
4. post fundamenta P12 BAR/MMIO/interruptiones, backend hardware acceleratus addi potest;
5. copia CPU↔GPU et cache texturarum minimantur.

**Acceleratio GPU non est condicio primae certificationis P16-XII; architectura quae eam impedit vetita est.**

## IX. Gradus P16-XII

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

**Status: PERFECTUM per C1/#150 et C2/#152.**

C1 instituit:

- cache umbrarum;
- backdrop cache cum generatione fontis in clave;
- blur adaptivum secundum aream;
- gloss/highlight reutilizabile;
- maskam alpha praemultiplicatam;
- clipping materializatum;
- hit/miss et capacitatem gestorii cache.

C2 instituit:

- pontem rasterae premium Graphica IX/SIMG II → superficies GX;
- conversionem RGBA recti in praemultiplicatum tantum in limite `GXX_*`;
- bilinearem alpha-correctam directe in GX;
- regionem, scaling linearem et 9-slice in superficie compositoris;
- constructorium superficiei materialis 9-slice paratae ad stratum Z;
- contractum quo chrome JL-UX raster premium sine framebuffer directo reddi potest.

### P16-XII-D — Tempus et motus

**Status: PROBATUM / CANONIZANDUM per #153.**

- `TX_*` horologium backend-neutrum;
- TSC monotonicum, semel per UEFI calibratum;
- eventus UEFI ut pacer/telemetria, non ut definitio temporis;
- catch-up ad frame logicum temporis realis sub onere;
- `MX_*` interpolationes fixed-point;
- linearis, ease-out cubica et smoothstep;
- x/y/alpha per stratum;
- retargetatio interruptibilis sine saltu;
- eadem frame iterata nullum opus compositorium creat;
- input non obstruitur ab horologio.

### P16-XII-E — Migratio shellis

**Status: PROBATUM / CANONIZANDUM per #155.**

- fenestrae in strata composita;
- chrome JL-UX;
- INITIUM;
- taskbar;
- cursor;
- Bureau;
- clientium migrationes ubi utile est.

### P16-XII-F — Backend accelerabilis

**Status: ACTIVUM; F1 contractum, F2 cache texturarum et F3 codam compositionis instituunt.**

- contractus backend explicatus;
- batching/coda communis Graphica VIII/X;
- fences et damnum post successum tantum purgatum;
- backend software ut referentia et target injectabile probationum;
- cache texturarum per generationem GX, cum residentia et LRU;
- copia, compositio source-over et 9-slice per codam BX;
- via GPU cum infrastructura hardware id sinit.

## X. Criterium Vista-class

P16-XII totum non dicitur perfectum quia unum panel translucet. Ante conclusionem, motor debet posse:

- plures fenestras RGBA simul componere;
- umbras molles cacheatas ostendere;
- backdrop blur regionalem sine halo praebere;
- translucidentiam et overlap recte miscere;
- resize/motus sine scintillatione gerere;
- effectus cum damage regionali non totum framebuffer frustra recreare;
- animationes UI stabili frame-clock regere;
- backend mutabilem sine mutatione theme/shell servare.

## XI. Probationes P16-XII-A

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

## XII. Probationes P16-XII-B

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

## XIII. Probationes P16-XII-C1

Probatio VINDEX nativa confirmat:

- radius blur adaptivus `20 / 12 / 8` pro areis parva/media/magna;
- eandem umbram bis petitam eandem superficiem cacheatam reddere;
- backdrop eadem generatione cache hit dare;
- mutationem fontis generationem mutare et backdrop novum producere;
- maskam alpha canales praemultiplicatos simul minuere;
- clip mensuram et pixelum originis exactum servare;
- gloss partem superiorem illuminare sine parte inferiore mutata.

Showroom QEMU/OVMF 1280×800 capitis C1 rettulit:

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

## XIV. Probationes P16-XII-C2

Probatio VINDEX nativa confirmat:

- conversionem RGBA recti Graphica IX in pixelum GX praemultiplicatum;
- alpha globalem sine mutatione coloris occulti;
- 9-slice SIMG II in destinatione GX;
- oram superiorem aqua et inferiorem bronzeam integram;
- flancum argentum semi-opacum;
- centrum vitrum alpha `170` cum canalibus praemultiplicatis;
- transparentiam extra destinationem;
- damage novem partium in unum rectum destinationis coalitum;
- constructorium directum superficiei materialis cum alpha globali.

Showroom QEMU/OVMF 1280×800 capitis `adf6b109…` ex **eadem rastera SIMG II 16×16** superficies `500×300` et `330×205` creavit:

```text
colores framebuffer: 323
ora magna aqua/centrum/bronze: (80,178,197) / (18,45,57) / (163,123,75)
ora parva aqua/centrum/bronze: (74,169,187) / (18,47,61) / (151,118,74)
colores centri: 3 / 3
halo magenta occultum: 0 / 0
flanc/centrum magna: (169,178,186) / (18,45,57)
flanc/centrum parva: (157,167,176) / (18,47,61)
XXXV probationes canonicae: 35 / 35
```

Captura framebuffer inspecta est. Margines quattuor pixelorum eandem crassitudinem servant in duabus magnitudinibus; centrum semi-transparens fascias fundi ostendit; flancum argentum a centro distinguitur; quattuor anguli fontis colorem magenta occultum sub alpha zero continent sed **nullum halo** in framebuffer apparet.

Hoc est primum contractum canonicum quo materia rastera premium redimensionabilis potest directe fieri stratum compositoris Graphica X.

## XV. Probationes P16-XII-D

Probatio VINDEX nativa confirmat:

- horologium manuale eandem API `TX_*` sine firmware exercere;
- fines interpolationis exactos;
- smoothstep medium `0.5` exactum;
- ease-out medium ultra linearem procedere;
- motum `(10,10,80) → (110,50,200)` ad medium exactum `(60,30,140)`;
- retargetationem ex hoc statu ipso, non ex meta veteri;
- primam frame post retargetationem continuam `(54,44,156)`;
- eandem frame bis pulsatam nullam mutationem creare;
- destinationem finalem exactam et motum deactivatum.

Showroom QEMU/OVMF 1280×800 capitis `30691241…` probavit TSC reale et catch-up sub renderer software lento:

```text
colores framebuffer: 329
status internus: (104,177,123) — viridis
ora ad metam secundam: (101,214,231)
centrum ad metam secundam: (18,110,131)
locus initialis restitutus: (8,18,28)
pixela bronzea trajectoriae: 147
saltus maximus temporalis: 27 frame
praesentationes logicae omissae: 75
XXXV probationes canonicae: 35 / 35
```

Captura framebuffer inspecta est. Tres loci intermedii bronzei et hiatus inter eos demonstrant renderer QEMU non posse omnes frame LX Hz praesentare; nihilominus panel ad metam secundam exactam pervenit et status viridis manet. Duae barrae framebuffer telemetriam `27 / 75` codificant et validator Python eas sine OCR legit.

Hoc probat differentiam essentialem XII-D: **sub onere praesentationes omittuntur, tempus non retardatur**. Retargetatio manet continua quia nova trajectoria semper a statu composito praesenti incipit.

Catena certificata:

```text
OVMF → VINDEX → EFI timer pacer → TSC calibratum → TX → MX → scena GX → damage-only → framebuffer
```

## XVI. Contractus P16-XII-F1

Prima pars XII-F limitem inter compositionem scenae et praesentiam physicam
explicat. `CX_SCENA_RENDE` backbuffer RGBA praemultiplicatum adhuc secundum
eandem semanticam software componit; `CX_PRAESENTA_FB` autem pixela GOP iam
non directe scribit.

Nova structura continet:

- nucleum `QVIII_*` in `fenestrale_coda_graphica.vindex`, communem executoribus
  Graphica VIII et Graphica X, sine mutatione opcodum historicorum `1..9`;
- descriptorem `BX_*` ABI versione `1`, genere, capacitatibus, statu framei,
  erroribus, numeris mandatorum et fences;
- electionem `BX_ELIGE` quae candidatum non paratum ad backend software
  referentiae reicit et fallback numerat;
- opcode `256` ad praesentiam regionalem superficiei GX;
- transactionem `FRAME_INCIPE → PRAESENTA_ADDE → FRAME_COMMITTE` quae plura
  recta in uno batch condere potest;
- target software injectabile ad probationes RGB/BGR sine firmware;
- backend software GOP ut referentiam semanticam productionis;
- sedes backendis et fence completa in descriptoribus scenae CX.

Genus GPU in ABI reservatur sed `BX_PARATUS` eum recusat donec executor verus
adsit. Ita P16-XII-F P12 non duplicat neque accelerationem fictam nuntiat.
Si submit vel praesentia deficit, damage scenae **non purgatur**: idem rectum
post backend validum restitutum iterum praesentari potest.

Probatio VINDEX nativa confirmat batch duo-mandatorum, ordinem canalium amborum
formatorum GOP, fences monotonas, overflow codae, electionem backendis scenae,
recusationem GPU ficti et conservationem damni post defectum.

## XVII. Contractus P16-XII-F2

Secunda pars XII-F vitam texturarum a memoria physica backendis separat.
Gestor `TXC_*` superficiem GX cum generatione contenti coniungit et recordum
residentiae LXXX-octetorum reddit. Recordum identitatem monotonicam,
generationem, pondus octetorum, tempus ultimi usus, fibulas et manubrium
backendis futurum continet.

Leges cache sunt:

- hit tantum si sedes superficiei **et** generatio GX conveniunt;
- mutatio GX vetus recordum invalidat et novam residentiam poscit;
- duo limites simul valent: numerus recordorum et summa octetorum logicorum;
- victima est recordum non fibulatum minime recens; aequalitas per identitatem
  minorem determinatur;
- recordum fibulatum numquam evincitur;
- invalidatio recordi fibulati differtur usque ad ultimam relaxationem;
- nodi evicti reutilizantur, ne acervus singulis generationibus crescat;
- res maior toto budget recusatur sine defectu compositionis software.

`BX_CACHE_INSTITUE` cache in offset `112` descriptoris backendis alligat.
`BX_CAP_TEXTURE` ante hanc institutionem non publicatur. Capacitas significat
contractum residentiae praesentem, non memoriam GPU fictam. Backend software
servat solum metadata et superficiem GX auctoritatem pixelorum; backend GPU
futurus eidem nodo manubrium reale in campo iam reservato alligare poterit.

Compositor cache tangit ubi texturae re vera consumuntur: fundum et unumquodque
stratum visibile quod damage secat. Petere et relaxare compositionem CPU non
mutat. Superficies immotae hits reddunt; renovatio clientis per generationem
miss et invalidationem reddit. Backbuffer semper post compositionem per
contractum F1 praesentatur et non pro textura statica falso cacheatur.

Probatio VINDEX nativa confirmat hit/miss, identitatem per generationem,
evictionem LRU, budget, saturitatem omnibus recordis fibulatis, invalidationem
dilatam, reusum nodorum, publicationem capacitatis BX et hits reales inter duas
recompositiones eiusdem scenae.

## XVIII. Contractus P16-XII-F3

Tertia pars XII-F compositionem ipsam, non solam praesentiam, per codam
backend-neutram transmittit. Opcode `256` praesentiae F1 servatur; nova mandata
sunt:

- `257 COPIA` — regio GX opaca in aliam superficiem;
- `258 COMPONE` — regio GX RGBA praemultiplicata source-over cum alpha globali;
- `259 NOVEM` — textura 9-slice intra rectum destinationis et clip damage.

Mandatum unum destinationem, fontem, recta fontis/destinationis et alpha
continet. Executor software easdem primitivas `GX_REGION_*` adhibet ac via
directa, ideo coda novam semanticam pixelorum non introducit. Residentia TXC
in executor tangitur ante operationem et postea relaxatur; cache plenum
compositionem software non impedit.

`CX_SCENA_RENDE` batch completum construit: fundum primum, strata visibilia
ordine Z postea. Commit compositionis fence propriam gignit; praesentia GOP in
transactione sequente fence alteram gignit. Damage scenae adhuc tantum post
praesentiam felicem purgatur.

Fallback est atomicus semanticis: si capacitas codae deficit, mandatum
reicitur aut executor compositionis deficit, frame abiicitur et eadem regio ab
initio per viam directam recomponitur. Ita effectus partialis batchis numquam
auctoritas finalis backbufferis fit.

Probatio F3 comparat codae exitum cum via directa pixel per pixel, generationem
cache inter tres frame, ordinem trium opcodum, fences, defectum in medio commit
cum coda statim purgata, et casum codae de industria nimis parvae qui sine
fence per fallback recte redditur.

## XIX. Invarianta

- nulla regressio in `FS_*` clientium;
- nullum C in runtime Sylviae;
- nulla copia servilis Aero/Vista;
- canon JL-UX manet auctoritas artis;
- imago conceptus est scopus visualis, QEMU est auctoritas executionis;
- wallpaper non substituit motorem;
- effectus non iustificant input lentum;
- memoria GX semper RGBA canonica manet; conversio GOP tantum in limite framebufferis fit;
- effectus cacheatus non iterum calculatur nisi clavis vel generatio fontis mutatur;
- textura fibulata non evincitur et capacitas texture sine cache non publicatur;
- residentia software metadata est, non affirmatio memoriae GPU;
- rastera Graphica IX in GX tantum per conversionem recti→praemultiplicati intrat;
- 9-slice margines materialis non cum dimensione destinationis extenduntur;
- eventus timeris non definit tempus animationis;
- frame logicum ex tempore monotono derivatur;
- frame presentationis omissa non debet durationem animationis extendere;
- retargetatio semper ex statu composito praesenti incipit;
- horologium UI non obstruit ansam input.

## XX. Sententia

**Non picturam pulchram supra motorem infirmum ponimus. Motorem facimus dignum Sylvia.**
