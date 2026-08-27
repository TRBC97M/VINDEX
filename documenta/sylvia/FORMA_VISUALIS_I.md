# Forma Visualis Sylviae — Incrementum I

## Propositum

P16 formam Sylviae a demonstratione technica Fenestralis II ad systema visuale cotidianum paulatim ducit. Primum incrementum metra, textum et regiones fundamentales escritorio stabilit sine mutatione architecturae Fenestralis neque viae UEFI purae.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

## Metra canonica primi incrementi

Fenestrale nunc his metris utitur:

- taskbar: **XL px**;
- titulus fenestrae: **XXXVI px**;
- initium regionis clientis: **LX px** infra summum fenestrae;
- textus titulorum: scala **II×** formae VIII×VIII;
- bullae fenestrae: XXIV×XXIV px;
- margo tractabilis resize: VI px.

Haec metra non ornamentum solum sunt. Renderer, hit-testing, maximizatio, regio clientis et taskbar eandem geometriam sequi debent. Si pictura et input dissentiunt, contractus fractus est.

## Taskbar

Taskbar P16-I tres regiones manifestas habet:

1. **INITIUM** ad sinistram;
2. fenestrae apertae in regione media dynamica;
3. regio systematis **SYLVIA** ad dextram.

Fenestrae apertae spatium medium dividunt. Focus et minimizatio contractum Fenestralis II iam canonicum servant.

## Fenestrae

Fenestra activa marginem distinctum retinet et titulum ampliorem accipit. Bullae minimizationis, maximizatonis et clausurae maiores sunt; regiones hit-testing eadem metra sequuntur.

Regio clientis a titulo et ornamentis separata manet. Superficies privata clientis ad `y + LX` incipit, ita contentum PROGRAMMATA vel TABULA ornamentum fenestrae non pingit.

## Contractus TEXTUS graphici

P16-I vetus vitium in duobus rendereribus invenit et corrigit.

ABI canonicum `TEXTUS` est:

```text
+0   longitudo octetorum
+8   capacitas octetorum
+16  octeta UTF-8
```

Praeterea operator `+` cum valore generis `TEXTUS` concatenationem significat. Ergo forma talis non est arithmetica memoriae legitima:

```text
textus + 16 + i
```

Renderer ante offsetum descriptorem ad sedem numericam convertit; deinde octetum legit:

```text
DECLARA descriptor SICUT NUMERUS VALENS FV_TEXTUS_SEDES(textus).
DECLARA littera SICUT NUMERUS VALENS OCTETUS_AB(descriptor + 16 + i).
```

Eadem disciplina in superficiebus clientium servatur. Hoc facit ut tituli, taskbar et textus PROGRAMMATA/TABULA vera octeta descriptoris hodierni legant, non campum capacitatis neque concatenationem accidentalem.

## Textus scalaris

`FV_TEXTUM_SCALA` glyphum formae VIII×VIII per viam pixelorum iam probatam multiplicat. In P16-I scala II× ad titulos fenestrarum adhibetur.

Haec non est adhuc typographia vectorialis neque anti-aliasing. Propositum primi incrementi est mensura et legibilitas certa super fontem bitmap canonicum; systema fontium maturius incrementum separatum erit.

## Probatio

`instrumenta/proba_formam_sylviae_i.py` screendump realem QEMU/OVMF inspicit. Probatio requirit:

- resolutionem MCCLXXX×DCCC;
- taskbar XL px cum limite aqua per totam latitudinem;
- corpus taskbar colore profundo;
- regionem INITIUM ad sinistram;
- regionem systematis ad dextram;
- titulum fenestrae XXXVI px;
- regionem clientis infra titulum;
- quantitatem sufficientem pixelorum lucidorum quae titulum II× demonstrat.

In probatione canonizationis primi incrementi detecta sunt:

```text
resolutio = 1280x800
taskbar = 40
titulus = 36
linea_aqua = 1280
linea_profunda = 1280
lux_tituli = 1292
colores_distincti = 39
```

Eadem exsecutio XXIX/XXIX probationes canonicas et catenam Fenestralis II cum rectore PS/2 nativo sine regressione servat.

Catena probata manet:

```text
OVMF → BOOTX64.EFI [VINDEX] → FENESTRALE II [VINDEX] → PS/2 [VINDEX] → FRAMEBUFFER
```

Nullum C in tota via runtime adhibetur.

## Fines incrementi I

P16-I deliberate non conatur totam identitatem visualem uno passu absolvere. Incrementa sequentia tractare possunt:

- iconographiam canonicam;
- fontem et typographiam maturiorem;
- menu INITIUM functionale;
- widgeta et controles communes;
- statum hover/press/focus subtiliorem;
- compositionem, umbras et transitiones ubi ratio perficiendi permittit;
- thema et systema metrorum amplius centralizatum.

Regula manet: una mutatio visualis non canonizatur nisi pictura vera sub UEFI probatur et input eandem geometriam sequitur.
