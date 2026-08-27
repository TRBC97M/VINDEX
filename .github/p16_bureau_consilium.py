#!/usr/bin/env python3
from pathlib import Path

p = Path('CONSILIUM.md')
t = p.read_text(encoding='utf-8')

old = '**Status:** `PERFECTUM per PR #113 — incrementum I; ACTIVUM — incrementum II`.'
new = '**Status:** `PERFECTUM per PR #113 — incrementum I; PERFECTUM per PR #114 — incrementum II; PROBATUM / CANONIZANDUM — incrementum III`.'
if old not in t:
    raise SystemExit('status P16 vetus deest')
t = t.replace(old, new, 1)

old = '''### Incrementum II activum

P16-II menu **INITIUM** functionale construit: pannus systematis, applicationes PROGRAMMATA/TABULA, hover, apertio/clausura et focus/restauratio ex eodem contractu input. Incrementa posteriora iconographiam, fontem maturiorem, widgeta communia, status interactionis et thema paulatim tractabunt. Unaquaeque mutatio visualis pictura vera sub UEFI et geometria input congrua muniri debet.

**Sylvia hodierna est ossa constructionis quae iam faciem canonicam accipere incipit, non facies finalis.**'''
new = '''### Incrementum II perfectum per #114

- menu **INITIUM** vere aperitur et clauditur;
- pannus `SYLVIA / SYSTEMA VINDEX / APPLICATIONES`;
- PROGRAMMATA et TABULA in menu;
- hover verus;
- restitutio fenestrae minimizatae vel clausae;
- focus et ordo Z per registrum Fenestralis;
- cursor e framebuffer ipso repertus et per PS/2 nativum motus;
- probatio INITIUM permanens in custodia UEFI.

Contractus plenus in `documenta/sylvia/INITIUM_II.md` describitur.

### Incrementum III probatum / canonizandum

P16-III **bureau functionale** addit:

- boot sine fenestris applicationum visibilibus;
- taskbar initio applicationibus vacua;
- iconae PROGRAMMATA et TABULA in bureau;
- hover iconarum;
- clic iconae → fenestra aperitur et focus accipit;
- clausura → fenestra e taskbar removetur;
- relaunch post clausuram ex eadem icona;
- probatio PS/2 realis: PROGRAMMATA aperitur, clauditur, deinde TABULA aperitur.

Contractus plenus in `documenta/sylvia/BUREAU_III.md` describitur.

P16-IV debet a duobus clientibus fixis ad registrum/catalogum applicationum progredi, ut INITIUM et bureau applicationes ex uno fonte canonico cognoscant.

**Sylvia hodierna iam bureau et menu systematis functionalia possidet; nondum tamen processuum manager aut catalogum applicationum generalem.**'''
if old not in t:
    raise SystemExit('sectio P16-II vetus deest')
t = t.replace(old, new, 1)

old = '''1. P16-II menu INITIUM functionale sub QEMU/OVMF probare et canonizare;
2. P12 incipere per fundamenta gubernatorum quae hardware reale et input maturius aperiunt;
3. P9 per incrementa parva et generalia continuare;
4. debitum ELF `PT_LOAD`/acervi fixi separatim solvere sine regressione targetorum;
5. contractus applicationum, widgeta et input Fenestralis maturare.'''
new = '''1. P16-III bureau functionale canonizare;
2. P16-IV registrum/catalogum applicationum commune INITIUM et bureau construere;
3. P12 incipere per fundamenta gubernatorum quae hardware reale et input maturius aperiunt;
4. P9 per incrementa parva et generalia continuare;
5. debitum ELF `PT_LOAD`/acervi fixi separatim solvere sine regressione targetorum.'''
if old not in t:
    raise SystemExit('actio proxima vetus deest')
t = t.replace(old, new, 1)

p.write_text(t, encoding='utf-8')
print('RECTE: CONSILIUM P16-I/II/III reconciliatum est.')
