# P16-VII — Capacitas Graphica Sylviae

## Finis

P16-VII renderer Fenestralis VINDEX facultatibus graphicis generalibus auget. Finis non est pictura simulata neque sola nova skin, sed fundamentum quo Sylvia imagines rasteras, alpha, gradientias, umbras et compositiones divitiores ipsa lingua VINDEX vere pingere potest.

## Primitiveae

Incrementum continet:

- interpolationem componentium coloris;
- gradientias horizontales et verticales;
- compositionem alpha software;
- umbras graduatas et halos;
- eandem familiam primitivarum pro framebuffer et superficiebus clientium;
- lectionem pixelorum ad probationes et compositionem.

Nullus backend graphicus externus post translationem UEFI introducitur.

## SIMG v1

Asseta rastera in memoria forma `SIMG v1` servantur.

Contractus:

- magia `SIMG`;
- versio I;
- pixel format RGBA8888;
- latitudo et altitudo 32-bit;
- stride explicitus;
- payload pixelorum RGBA.

Decoder generalis palette + RLE asseta compacta in SIMG expandit. Renderer formam picturae non novit: tantum pixela, alpha et recta fontis tractat.

## Blit partium et scala

P16-VII recta fontis et destinationis compacta adhibet, ne ABI per multitudinem argumentorum fragilis fiat. Blit nearest-neighbor eandem imaginem ad plures magnitudines pingere potest.

Hoc permittit eandem iconam applicationis:

- XLVIII×XLVIII in bureau;
- XXXII×XXXII in INITIUM;
- magnitudinibus minoribus futuris in taskbar;

sine triplici pictogrammate manuali.

## Iconographia

Atlas rasterus XCVI×XCVI quattuor tessellas XLVIII×XLVIII continet:

1. PROGRAMMATA;
2. TABULA;
3. TERMINALE;
4. OFFICINA.

Emblema Sylviae XXXII×XXXII asset SIMG separatum est.

Compositor finalis ordinem servat:

```text
fundum → bureau → rastera → fenestrae → INITIUM → taskbar → cursor
```

Ita iconae bureau fenestras numquam superpingunt.

## Probationes

Probatio nativa atlas, coordinatas tessellarum, recta compacta et lectionem pixelorum verificat. `tests/run_tests.sh` XXXV probationes rectas, nulla errata refert.

Custodia QEMU/OVMF dedicata framebuffer 1280×800 vere captat et separatim metitur:

```text
FORMA-VII: emblema_gemma=68 emblema_aes=68 colores_distincti=67
FORMA-VII: iconae_rasterae=936,907,984,822
```

Probatio nullam imaginem simulatam, generatam aut mock adhibet: captura framebuffer vera QEMU/OVMF sola auctoritas visualis est.

Via probata:

```text
OVMF → BOOTX64.EFI [VINDEX] → FENESTRALE II [VINDEX] → PS/2 [VINDEX] → FRAMEBUFFER
```

Nullum C in runtime Sylviae introducitur.

## Correctio instrumentorum VINDEX

Systema modernum P16-VII fontes coniunctos ultra vetus limen 212999 octetorum produxit. Compilator VINDEX 0.53 hunc limitem iam non habebat, sed `instrumenta/vindex_verifica.py` eum adhuc historice servabat. Custodia obsoleta remota est; verificator nunc systema integrum ultra illum limitem examinat sine limite artificiali resurrecto.

## Limites huius incrementi

P16-VII facultatem graphicam et primam iconographiam rasteram canonizat. Non mutat:

- hitbox applicationum;
- focus aut ordinem Z;
- semanticam fenestrarum;
- persistentiam fasciculorum;
- logicam TERMINALIS vel OFFICINAE.

Chrome compositus Frutiger-Aero × imperiale × Y2K est incrementum sequens super has primitiveas, non pars occultata huius contractus.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
