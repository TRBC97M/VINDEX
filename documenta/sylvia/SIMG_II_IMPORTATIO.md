# SIMG II — IMPORTATIO ARTIS

## I. Finis

SIMG II est formatum runtime Sylviae; PNG manet unus e fontibus artis. Instrumentum `instrumenta/simg_ii_importa_png.py` pontem a fonte artis ad assetum nativum facit.

Haec divisio deliberata est:

- editor artis generat PNG;
- build convertit PNG in `.simg`;
- Sylvia runtime non decodificat PNG;
- lector, validator, metadata et gestor assetorum SIMG II manent VINDEX.

Python igitur non est dependentia runtime Sylviae. Tantum instrumentum officinae/build est.

---

## II. PNG recepta

Importator sine bibliotheca externa operatur et validat:

- signaturam PNG;
- CRC omnium chunkorum;
- IHDR;
- IDAT per zlib;
- quinque filtra PNG `0..4`;
- imagines VIII bituum non interlaced.

Color types recepti:

- grayscale;
- RGB;
- palette cum `PLTE` et `tRNS`;
- grayscale + alpha;
- RGBA.

Omnia ante emissionem in RGBA8888 convertuntur.

PNG interlaced Adam7 et canales XVI bituum hoc gradu consulto non sustinentur. Pipeline artis canonica exportare debet PNG VIII bituum non interlaced.

---

## III. Usus

Forma minima:

```text
python3 instrumenta/simg_ii_importa_png.py fons.png exitus.simg
```

Icona 2×:

```text
python3 instrumenta/simg_ii_importa_png.py icon.png icon@2x.simg --genus icona --scala 2000
```

Pannus novem-partium:

```text
python3 instrumenta/simg_ii_importa_png.py button.png button.simg --genus novem --novem 12,12,12,12
```

Cursor:

```text
python3 instrumenta/simg_ii_importa_png.py cursor.png cursor.simg --genus cursor --hotspot 3,2
```

Wallpaper:

```text
python3 instrumenta/simg_ii_importa_png.py sylvia-1920x1080.png sylvia-1920x1080.simg --genus wallpaper --scala 1000 --compressio auto
```

---

## IV. Compressio

`--compressio` accipit:

- `raw` — RGBA8888 directe;
- `rle` — RLE32 SIMG II;
- `auto` — RLE32 tantum si payload minor quam RAW est, aliter RAW.

Hoc magni momenti est: wallpaper photographicum non cogitur in RLE32, quod in imagine valde varia maius esse potest. Iconae, cursor, chrome et paneles saepe RLE32 utiliter minuuntur.

Compressio futura ad wallpaper altae qualitatis addi poterit numero novo compressionis sine ruptura SIMG II.

---

## V. Metadata

### Genus

`--genus`:

- `genericum`;
- `wallpaper`;
- `icona`;
- `novem`;
- `cursor`;
- `fons`;
- `testa`.

### Scala

`--scala` est millesimalis:

- `1000 = 1×`;
- `1500 = 1.5×`;
- `2000 = 2×`.

Gestor assetorum VINDEX plures variantes eiusdem identitatis retinere et optimam ad densitatem UI eligere potest.

### Novem-partes

`--novem L,T,R,B` metadata intra ipsum `.simg` scribit. Nullum `.meta` separatum requiritur.

### Cursor

`--hotspot X,Y` punctum actionis cursoris intra ipsum `.simg` scribit.

---

## VI. Probatio transversa

`instrumenta/proba_importatorem_simg_ii.py` non solum header Python inspectat.

Catena probationis est:

```text
PNG fabricatum
  → decoder/importator Python
  → fasciculus .simg
  → bytes in probationem VINDEX inserta
  → compilator_vindex
  → SII_VALIDUS / SII_PIXEL_RGBA
```

Ita incompatibilitas inter emitter Python et lectorem VINDEX non potest latere post duas probationes separatas.

Probator etiam exercet:

- quinque filtra PNG;
- palette et transparentiam `tRNS`;
- electionem automaticam RAW/RLE32;
- metadata novem-partium;
- exactam geometriae, generis et scalae lectionem in VINDEX.

---

## VII. Directio assetorum JL-UX

Post hunc pontem, asseta premium possunt extra codicem VINDEX creari et sine perdita qualitate in runtime adduci.

Ordo productionis:

1. typographia et atlases;
2. iconographia systematis;
3. shell kit: INITIUM, rail, status, divisores;
4. wallpaper canonica 1920×1080 et variantes;
5. chrome fenestrarum;
6. componentes universales.

SIMG II non substituit artem. SIMG II facit ut ars bona **nativa Sylviae** fiat.

*PNG est fons artis. SIMG II est lingua imaginum runtime Sylviae.*
