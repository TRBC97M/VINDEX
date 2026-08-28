# GRAPHICA IX — RASTERA PREMIUM SYLVIAE

## I. Propositum

Graphica IX est gradus quo asseta SIMG II desinunt videri sicut imagines simpliciter dilatatae. Intentio est clara: iconographia, chrome, cursores et alia ornamenta JL-UX debent scalari molliter, alpha recte servare et in framebuffer sive superficiem privatam eodem modo componi.

Graphica VIII manet fundamentum geometricum: recta compacta, 9-slice, superficies, damage et typographia. Graphica IX super hoc fundamentum addit rasteram imaginum qualitatem altiorem.

---

## II. Interpolatio alpha praemultiplicata

SIMG II RGBA rectum servat. Interpolatio autem non debet canales RGB pixelorum transparentium simpliciter miscere, quia hoc halos nigros, caeruleos vel alios circa margines iconarum creat.

Graphica IX igitur interpolationem bilinearem in spatio alpha praemultiplicato facit:

1. quattuor pixela vicina leguntur;
2. RGB cuiusque pixeli per alpha ponderatur;
3. alpha et canales praemultiplicati bilineari modo interpolantur;
4. RGB in fine per alpha resultatum denuo normalizatur;
5. compositio in destinatum per alpha finalem fit.

Exemplum canonicum probationis est pixel ruber opacus iuxta pixel caeruleum omnino transparentem. Medium debet manere rubrum semitransparens, non purpureum.

---

## III. Cache RGBA nativa

Gestor SIMG II nunc in nodo variantis etiam cache RGBA decodificatam servat. `AII_RGBA_CACHE` payload RAW vel RLE semel expandit et eandem sedem in vocationibus sequentibus reddit.

Hoc principium magni momenti est:

**decode semel, compone saepe.**

Pons SIMG I adhuc manet ad compatibilitatem, sed Graphica IX iam eo uti non debet ad rasteram premium.

---

## IV. Viae destinationis

Duae viae eandem mathematicam interpolationis utuntur.

### Framebuffer

- `GIX_RGBA_REGION_FB`
- `GIX_ASSET_REGION_FB`
- `GIX_ASSET_LINEAR_FB`
- `GIX_ASSET_NOVEM_FB`

Haec directe in framebuffer Sylviae componunt.

### Superficies privata

- `GIX_RGBA_REGION_S`
- `GIX_ASSET_REGION_S`
- `GIX_ASSET_LINEAR_S`
- `GIX_ASSET_NOVEM_S`

Haec in superficies privatas clientium componunt. Sic fenestra, widget vel compositor offscreen eadem qualitate uti potest ac bureau.

---

## V. Novem partes

Metadata novem-partium SIMG II directe a Graphica IX legitur. Anguli servantur, latera et centrum ad spatium destinatum bilineari modo adaptantur.

Hoc est fundamentum futurorum:

- chrome fenestrarum;
- panelium vitreo-metallicorum;
- rail et taskbar;
- buttonum et camporum;
- cardarum JL-UX.

Metadata non duplicatur in codice rendereris.

---

## VI. Multi-scala

Graphica IX assetum non eligit sola. Gestor `AII_OPTIMUM_NODUS` variantem 1×, 1.5×, 2× vel aliam scalam optimam eligit, deinde Graphica IX eam ad mensuram exactam destinationis interpolat.

Haec separatio deliberata est:

- gestor decernit **quod assetum**;
- Graphica IX decernit **quomodo pixela componantur**.

Futurus backend GPU idem contractum servare potest.

---

## VII. Probatio canonica

Probatio in duos gradus dividitur, quia `FV_COLOR` et compositio framebufferis statum UEFI Sylviae requirunt.

`probationes/capacitas_graphica_ix.vindex` sub ELF nativo exercet partes puras:

- cache RGBA nativam;
- identitatem cache inter vocationes;
- interpolationem in margine transparente sine halo;
- alpha resultatum;
- clamping coordinatarum fixed-point.

Deinde `systema/showroom_graphica_ix_uefi.vindex` sub QEMU/OVMF exercet partes quae framebuffer verum requirunt:

- eundem assetum per nearest veterem et Graphica IX premium;
- compositionem bilinearem alpha praemultiplicatam in framebuffer;
- 9-slice ex metadata SIMG II;
- compositionem in superficie privata atque blit ad framebuffer.

Validator framebuffer exactum metitur. In certificatione initiali specimen nearest **III colores** habuit, specimen premium **CDXXII colores**, color caeruleus occultus in alpha-zero **nullum halo** creavit, et orae 9-slice aqua/bronze utrumque **M-VIII pixela** continua servaverunt.

---

## VIII. Directio pro JL-UX

Post certificationem huius gradus, primi beneficiarii debent esse asseta quae differentiam visualem statim ostendunt:

1. iconographia bureau et INITIUM altae resolutionis;
2. chrome fenestrarum 9-slice;
3. cursores anti-aliased;
4. taskbar et INITIUM materiae;
5. wallpaper premium multi-resolutionis.

Graphica IX non est ornamentum separatum. Est pontus inter pipeline artis modernae et compositor VINDEX.

**Ars altae resolutionis intrat; Sylvia eam sine aspectu pixelato reddit.**
