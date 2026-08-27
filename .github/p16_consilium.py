#!/usr/bin/env python3
from pathlib import Path

p = Path('CONSILIUM.md')
t = p.read_text(encoding='utf-8')

vetus = '''## P16 — Forma visualis Sylviae

**Status:** `PARATUM`.

Consilia visualia sunt destinatio realis, non picturae decorativae. Fenestrale technicum debet paulatim accipere:

- widgeta;
- thema;
- typographiam;
- margines et proportionem;
- iconographiam;
- cursorem et status interactionis;
- taskbar et menus canonicos;
- scaling et resolutiones modernas.

**Sylvia hodierna est ossa constructionis, non facies finalis.**
'''

novum = '''## P16 — Forma visualis Sylviae

**Status:** `PROBATUM / CANONIZANDUM — incrementum I`.

Consilia visualia sunt destinatio realis, non picturae decorativae. Fenestrale technicum debet paulatim accipere widgeta, thema, typographiam, margines et proportionem, iconographiam, cursorem et status interactionis, taskbar et menus canonicos, scaling et resolutiones modernas.

### Incrementum I probatum

- taskbar a XXVIII ad **XL px** modernizata;
- titulus fenestrae ad **XXXVI px**;
- regio clientis ad offset **LX px**;
- bullae minimizationis, maximizatonis et clausurae maiores cum hit-testing congruo;
- regiones **INITIUM** et **SYLVIA** in taskbar;
- tituli fenestrarum per formam VIII×VIII ad scalam II× pinguntur;
- renderer Fenestralis et superficies clientium ad ABI canonicum `TEXTUS` (`+16` octeta UTF-8) corriguntur;
- descriptor `TEXTUS` ante arithmeticam memoriae ad `NUMERUS` convertitur, ne operator `+` concatenationem accidentalem efficiat;
- probatio screendump realis QEMU/OVMF metra et textum comprobat;
- XXIX/XXIX probationes, Fenestrale II et PS/2 sine regressione manent.

Contractus plenus in `documenta/sylvia/FORMA_VISUALIS_I.md` describitur.

### Incrementa sequentia

P16-II et posteriora iconographiam, fontem maturiorem, menu INITIUM functionale, widgeta communia, status interactionis et thema paulatim tractabunt. Unaquaeque mutatio visualis pictura vera sub UEFI et geometria input congrua muniri debet.

**Sylvia hodierna est ossa constructionis quae iam faciem canonicam accipere incipit, non facies finalis.**
'''

if vetus not in t:
    raise SystemExit('DEFECIT: sectio P16 vetus non inventa est')
t = t.replace(vetus, novum, 1)

t = t.replace(
    'Custodia UEFI separata exsequitur QEMU/OVMF, screendump, PS/2 nuclei historici et Fenestrale II cum PS/2 nativo. Probationes Win64 et Officina sub Windows vero manent separatae.',
    'Custodia UEFI separata exsequitur QEMU/OVMF, screendump, PS/2 nuclei historici, Fenestrale II cum PS/2 nativo et contractum formae visualis P16-I. Probationes Win64 et Officina sub Windows vero manent separatae.',
    1,
)

t = t.replace(
    '1. P16 incipere: Fenestrale technicum ad formam visualem Sylviae modernam paulatim movere;',
    '1. P16-I canonizare et P16-II per iconographiam, fontem vel menu INITIUM parvum continuare;',
    1,
)

p.write_text(t, encoding='utf-8')
print('RECTE: CONSILIUM P16-I statum probatum refert.')
