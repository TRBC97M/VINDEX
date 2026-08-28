# SIMG II — FORMATUM GRAPHICUM NATIVUM SYLVIAE

## I. Propositum

SIMG II est forma rastera nativa Sylviae OS. Non destinatur ad tollenda instrumenta artis communia. PNG, SVG, Krita, Photoshop aliave instrumenta manent fontes creationis; pipeline aedificationis ea in SIMG II convertet, dum Sylvia ipsa formatum nativum versionatum legit.

Principium est duplex:

**motor graphicus componit; asseta qualitatem visualem ferunt.**

SIMG II igitur non est solum receptaculum pixelorum. Metadata quae renderer revera indiget intra idem archivum servantur: genus asseti, scala, margines novem-partium, hotspot cursoris et integritas payload.

SIMG v1 manet legibile. Migratio non est ruptura.

---

## II. Contractus binarius

Header minimum est **LXXX octeta**. Integra multioctetalia sunt u32 little-endian.

| Offset | Mensura | Significatio |
| ---: | ---: | --- |
| 0 | 4 | magia `SIMG` |
| 4 | 1 | versio `2` |
| 5 | 1 | formatum pixelorum: `1 = RGBA8888` |
| 6 | 1 | compressio: `0 = RAW`, `1 = RLE32` |
| 7 | 1 | vexilla generalia, nunc reservata |
| 8 | 4 | mensura headeris |
| 12 | 4 | latitudo |
| 16 | 4 | altitudo |
| 20 | 4 | stride post expansionem |
| 24 | 4 | offset payload |
| 28 | 4 | mensura payload |
| 32 | 4 | mensura post expansionem |
| 36 | 4 | genus asseti |
| 40 | 4 | scala millesimalis |
| 44 | 4 | vexilla metadatae |
| 48 | 4 | margo sinister novem-partium |
| 52 | 4 | margo superior |
| 56 | 4 | margo dexter |
| 60 | 4 | margo inferior |
| 64 | 4 | hotspot X |
| 68 | 4 | hotspot Y |
| 72 | 4 | Adler-32 payload |
| 76 | 4 | reservatum |

Post header payload sequitur. `payload offset` non cogitur semper LXXX esse; hoc spatium extensionibus futuris relinquit.

---

## III. Genera assetorum

Prima taxonomia runtime:

| Valor | Genus |
| ---: | --- |
| 0 | genericum |
| 1 | wallpaper |
| 2 | icona |
| 3 | novem-partes |
| 4 | cursor |
| 5 | atlas fontis |
| 6 | testa / shell |

Taxonomia est indicium rendereris et gestor assetorum, non prohibitio. Versiones futurae genera addere possunt sine mutando RGBA fundamentale.

---

## IV. Scala

Scala est integer millesimalis:

- `1000` = 1×;
- `1500` = 1.5×;
- `2000` = 2×.

Gestor assetorum potest plures variantes eiusdem identitatis servare. Electio canonica est:

1. scala exacta, si adest;
2. aliter minima scala maior quam petita;
3. si nulla maior adest, maxima scala minor quam petita.

Hoc consilium qualitatem potius quam inutilem upscaling eligit. Resolutio canonica JL-UX erit 1920×1080, sed formatum ipsum nulli resolutioni ligatur.

---

## V. Compressio

### RAW

Payload est series RGBA8888 directa. Haec via simplicissima et velocissima est ad asseta iam cache parata et imagines quae celeriter ad superficiem transferendae sunt.

### RLE32

Cursus quilibet habet V octeta:

```text
[mensura u8 1..255][R][G][B][A]
```

RLE32 praecipue prodest iconis, chrome, cursoribus, panelis et aliis assetis UI ubi regiones eiusdem coloris communes sunt. Non destinatur ad photographicum wallpaper efficacissime comprimendum.

Compressiones block/lossless potentiores postea addi possunt novo numero compressionis sine ruptura versionis II.

---

## VI. Metadata

### Novem-partes

Bitum 0 in `vexilla metadatae` significat margines novem-partium valere. Margines u32 intra header servantur. Renderer ita non eget archivo `.meta` separato ad pannos, botones, chrome vel rail.

### Cursor

Bitum 1 significat hotspot X/Y valere. Cursor igitur imaginem et punctum actionis in uno asseto portat.

Metadatae futurae extensionibus headeris vel sectionibus additis introduci possunt.

---

## VII. Integritas

SIMG II a versione I differt etiam eo quod integritatem payload explicite servat. Adler-32 payload in offset LXXII scribitur et a `SII_VALIDUS` verificatur.

Hoc non est mechanismus cryptographicus. Propositum est corruptionem, truncationem et conversiones vitiosas mature deprehendere antequam renderer memoriae alienae credat.

---

## VIII. API VINDEX prima

`bibliotheca/simg_ii.vindex` praebet inter alia:

- `SII_CREA_RGBA` — ex pixelis RGBA formatum RAW vel RLE32 construit;
- `SII_VALIDUS` — structuram, metadata et checksum verificat;
- `SII_PIXEL_RGBA` — pixelum logicum legit;
- `SII_EXPANDE_RGBA` — payload ad RGBA directum expandit;
- `SII_META_NOVEM` — margines 9-slice inscribit;
- `SII_META_CURSOR` — hotspot cursoris inscribit;
- accessores latitudinis, altitudinis, compressionis, generis, scalae et metadatae.

`bibliotheca/simg_ii_compat_v1.vindex` formatum SIMG I legit et per `SII_EX_V1` in II convertit.

`bibliotheca/simg_ii_bridge_vii.vindex` per `SII_AD_V1` descriptor temporarium v1 generat. Hic pons permittit asseta II statim cum blitteribus Graphica VII/VIII adhiberi dum compositio nativa II construitur.

---

## IX. Gestor assetorum

`bibliotheca/simg_ii_assetum.vindex` est prima tabula runtime assetorum SIMG II. Id numericum unam familiam asseti repraesentat; eadem familia plures scalas continere potest.

Gestor servat:

- caput et caudam registri;
- numerum variantium;
- scalam UI petitam;
- generationem mutationum.

Nodus variantis servat:

- id asseti;
- genus;
- scalam;
- descriptor SIMG II;
- latitudinem et altitudinem;
- numerum usuum;
- cache temporarium SIMG I ad pipeline rasteram praesentem.

API principalis:

- `AII_CREA` — gestorem creat;
- `AII_ADDE` — variantem id+scala addit et duplicatum exactum recusat;
- `AII_VARIANS_EXACTA` — variantem exactam invenit;
- `AII_OPTIMUM` — optimam variantem secundum scalam petitam reddit;
- `AII_SCALA_PONE` — scalam UI mutat et generationem auget;
- `AII_V1_CACHE` — conversionem ad v1 semel facit et eundem descriptor postea reddit.

Cache v1 est pons migrationis, non finis architecturae. Cum Graphica directe SIMG II consumet, nodus eandem notionem cache servare poterit pro superficie decodificata vel textura GPU.

---

## X. Pipeline artis

Directio canonica:

```text
PNG / SVG / editor artis
        ↓
importator / convertor
        ↓
SIMG II + metadata intra unum assetum
        ↓
gestor assetorum VINDEX + selectio scalae + cache
        ↓
Graphica / superficies / futurus backend GPU
```

Runtime Sylviae non debet imagines artificis singulis redraw denuo decodere. Asseta semel validantur, expanduntur ubi opus est, deinde in cache manent.

---

## XI. Limites huius gradus

Fundamentum II nondum est finis pipeline:

- PNG decoder/importator nondum pars huius gradus est;
- atlas multiplex intra unum container nondum definitur;
- mipmaps et variantes multiplices intra unum archivum nondum adsunt; variantes nunc per gestorem eiusdem id ordinantur;
- compressio photographica non tentatur;
- cache nativa superficierum SIMG II adhuc sequitur;
- backend GPU futurus eodem formato uti poterit, sed SIMG II ab eo non dependet.

Hoc deliberate servat versionem II parvam, verificabilem et utilem statim.

---

## XII. Regula architectonica

SIMG II non creatur quia formatum proprium ornamentum est. Creatur quia Sylvia indiget contractu graphico nativo qui renderer, asseta JL-UX, scaling, 9-slice, cursores et cache eadem lingua coniungat.

**PNG est fons artis. SIMG II est lingua imaginum runtime Sylviae.**
