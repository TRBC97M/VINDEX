# JL-UX ASSETA PREMIUM I

**Sylvia OS — P16-XI-A**  
Status: **ACTIVUM**

## I. Propositum

Hic gradus est prima probatio artistica quae totam catenam modernam exercet:

```text
ars PNG → importator → SIMG II → gestor assetorum → Graphica IX → framebuffer QEMU/OVMF
```

Finis non est quattuor pictogrammata maiora tantum creare. Finis est demonstrare Sylviam asseta translucida, altae resolutionis et moderatim materialia sine aspectu pixelato reddere posse, dum semantica Fenestralis intacta manet.

## II. Canon impletus

Asseta sequuntur:

- `JL_UX_CANON_I.md` — Perspicuitas, Imperium, Continuitas;
- `JL_UX_PALETTA_I.md` — paletta canonica novem colorum;
- `JL_UX_MATERIAE_I.md` — Vitrum Minerale, Ebur Enamelatum, Metallum Frigidum, Lumen Molle;
- `JL_UX_COMPONENTES_I.md` — status visibiles non ex uno pixelo dubio dependentes;
- `GRAPHICA_IX.md` — bilinearis alpha praemultiplicata et cache RGBA;
- `SIMG_II.md` / `SIMG_II_IMPORTATIO.md` — formatum et pipeline artis.

`SYLVIA OS` est identitas primaria. Nomen `JL-UX` non in iconis, wallpaper aut testa principali gratuitum pingitur.

## III. Familia prima

Quattuor iconae principales fiunt:

1. `PROGRAMMATA` — ordo applicationum / fenestrae vel moduli;
2. `TABULA` — documentum/tabula ordinata;
3. `TERMINALE` — instrumentum textualis obscurum cum prompt claro;
4. `OFFICINA` — instrumentum creationis/editionis VINDEX.

Iconae debent esse inter se statim cognatae sed non confundendae.

## IV. Forma artistica

### Volumen

Iconae non sunt glyphi plani. Utuntur:

- silhouette clara;
- uno corpore principali;
- luce superiori/locali;
- umbra locali translucida;
- accentu Aqua/Cyan aut Bronze raro;
- Ebur/Metallum pro partibus structuralibus;
- Graphite pro profundo et contrastu.

### Moderatio

Vitanda sunt:

- cartoon nimis mollis;
- saturatio ubique;
- neon continuus;
- textus minutus intra iconam;
- radii magni generici qui faciem mobilem efficiunt;
- copia servilis iconographiae alterius OS.

### Alpha

Margines anti-aliased et umbrae translucidae deliberate servantur. Pixel alpha-zero potest RGB non-nigrum continere in probatione adversariali, ut demonstratur Graphica IX eum halo non creare.

## V. Scalae

Familia prima saltem tres variantes per identitatem habet:

- `1000` — 1×;
- `1500` — 1.5×;
- `2000` — 2×.

Basis hodierna iconis Fenestralis est XLVIII px. Prima familia igitur ad magnitudines circa XLVIII / LXXII / XCVI px producitur. Gestor SIMG II variantem optimam eligit; Graphica IX ad destinationem exactam componit.

Postea P16-XII familias XVI/XXIV/XXXII et alias scalas canonicas complet.

## VI. Nomina et dispositiones

Fons artis et output runtime separantur. Forma commendata:

```text
res/jlux/assetta/premium-i/png/<nomen>@1x.png
res/jlux/assetta/premium-i/png/<nomen>@1_5x.png
res/jlux/assetta/premium-i/png/<nomen>@2x.png
res/jlux/assetta/premium-i/simg/<nomen>@1x.simg
res/jlux/assetta/premium-i/simg/<nomen>@1_5x.simg
res/jlux/assetta/premium-i/simg/<nomen>@2x.simg
```

PNG est fons artis; `.simg` est res runtime. Asseta canonica non duplicantur in pluribus atlas sine causa.

## VII. Showroom

Ante integrationem in Bureau, showroom QEMU dedicatum debet:

- quattuor iconas ostendere;
- exemplar nearest historicum et Graphica IX premium iuxta se comparare;
- plures magnitudines exercere;
- alpha in framebuffer vero exercere;
- saltem unum assetum per variantem multi-scala eligere;
- output ex superficie privata quoque demonstrare.

Showroom non est mock: payload UEFI a compilatore VINDEX construitur et Graphica IX realis framebuffer pingit.

## VIII. Probationes host

Probationes sine QEMU verificent:

- PNG → SIMG II pro omnibus XII variantibus;
- `genus=icona`;
- `scala=1000/1500/2000`;
- integritatem Adler-32;
- geometriae expectatas;
- selectionem variantis gestor assetorum;
- cache RGBA stabilem;
- nullam corruptionem alpha.

## IX. Probationes framebuffer

Validator QEMU metitur saltem:

- praesentiam quattuor regionum iconarum;
- varietatem colorum premium maiorem quam nearest comparativum;
- absentiam halo e colore occulto alpha-zero;
- continuitatem silhouette et alpha;
- colores canonicos vel derivationes legitimas;
- output non vacuum in framebuffer et superficie privata.

Numerus magicus unus non fit auctoritas. Signatura regionis pluribus mensuris constat.

## X. Invarianta Fenestralis

Hoc gradu non mutantur:

- hitbox Bureau 108×88;
- launch semanticus;
- catalogus applicationum;
- focus et ordo Z;
- geometria fenestrarum;
- taskbar et INITIUM input contractus;
- persistentia OFFICINAE.

Qualitas rastera a geometria separatur.

## XI. Perfunctionis lex

- decode semel, compone saepe;
- cache RGBA nativa adhibetur;
- alpha magnae superficies vitantur;
- redraw PS/2 non occultatur mora maiore;
- si integra shell post integrationem p95 excedit limen Graphica VIII, causa corrigitur, non custodia laxatur.

## XII. Definition of Done

P16-XI-A non est `CERTIFICATUM` nisi:

1. XII PNG fontes et XII SIMG II runtime asseta structuram canonicam transeunt;
2. compilator VINDEX probationes pertinentes compila;
3. puritas Sylviae manet;
4. showroom QEMU/OVMF exacti capitis transiit;
5. captura framebuffer vera inspecta est;
6. premium contra nearest differentiam visibilem et mensurabilem ostendit;
7. nullus sleep auctus neque guard debilitatus successum fingit;
8. distantia relicta a conceptu JL-UX in PR aperte describitur.

## XIII. Post hunc gradum

Post certificationem:

- P16-XI-B eadem asseta in Bureau et INITIUM inserit;
- P16-XI-C chrome fenestrarum 9-slice premium construit;
- deinde cursores, materiae testae et wallpaper multi-resolutionis veniunt.

**Ars altae resolutionis intrat; Sylvia eam sine aspectu pixelato reddit.**
