# FENESTRALE II — GRADUS E
## Firmamentum compatibile descriptoris nativi

**Status:** integratio experimentalis cum nucleo 0.51  
**Series:** Fenestrale II  
**Gradus:** E  
**Praerequisitum:** ABI Gradus D

---

## I. Propositum

Gradus D pactum memoriae inter firmamentum et VINDEX definivit. Gradus E
primum pactum illud in **vera catena boot Sylvia 0.51** implet, sed sine fontem
`firmamentum_uefi.c` canonicum adhuc mutando.

Instrumentum transformationis deterministicae ex fonte firmamenti 0.51
variantem temporalem generat. Varians:

- eundem nucleum VINDEX onerat;
- eandem umbram 320×200 veterem servat;
- eandem persistentiam et input veterem servat;
- simul `FENESTRALE2_DESCRIPTOR` implet;
- coordinatas muris nativas servat;
- eventa Gradus D in circulum scribit.

Ita via nova primum iuxta viam veterem vivit.

---

## II. Cur fons canonicus nondum mutatur

Gradus E est mutatio fundamentalis, sed recuperatio systematis magni momenti
est.

Ergo:

```text
firmamentum_uefi.c             → 0.51 stabile
        │
        └─ generator Gradus E  → firmamentum temporarium + ABI II
```

Si Gradus E in firmware aliquo deficit, `BOOTX64.EFI` stabile nihil mutatum
habet.

Post probationes QEMU et hardware, patch Gradus E potest in firmamentum
canonicum transferri.

---

## III. Descriptor impletus

Variant Gradus E in initio scribit:

- magic `SYLFEN2`;
- versio `1`;
- mensura `128`;
- basis framebuffer GOP;
- latitudo et altitudo nativae;
- `PixelsPerScanLine`;
- RGB/BGR pixel format;
- XXXII bits per pixel;
- coordinatae muris nativae;
- bullae;
- altitudo taskbar XXVIII;
- scala M per mille.

Capacitates declarantur tantum si re vera adsunt.

`FII_CAP_COMPOSITORIUM` consulto nondum ponitur, quia compositorium Gradus C
adhuc in probatione separata manet.

---

## IV. Duplex coordinatarum via

Nucleus 0.51 adhuc murem in spatio logico circiter `320×200` exspectat.
Fenestrale II coordinatas monitoris reales requirit.

Gradus E utrumque servat:

```text
input firmware
   ├─► coordinatae veteres → communis 0.51
   └─► coordinatae nativae → FENESTRALE2_DESCRIPTOR
```

Via absoluta directe ad resolutionem monitoris convertitur.
Via relativa motum veterem normalizat et deinde proportionaliter ad
resolutionem nativam transfert.

Nihil in codice nuclei veteris mutandum est.

---

## V. Eventa

Gradus E circulum Gradus D incipit re vera implere.

Eventa initialia:

- `FII_EVENTUM_DISPLAY_MUTATUR` semel in initio;
- `FII_EVENTUM_MURUS_MOVETUR` cum positio nativa mutatur;
- `FII_EVENTUM_MURUS_BULLA` cum bulla stabilis mutatur;
- `FII_EVENTUM_CLAVIS_PREMITUR` pro input UEFI.

UEFI Simple Text Input eventum release clavium non praebet; ideo
`FII_EVENTUM_CLAVIS_SOLVITUR` in hoc gradu nondum generatur.

Si circulus plenus est, eventum vetustissimum relinquitur ut systema novum
recipere possit sine stallo firmware.

---

## VI. Generator deterministus

`systema/uefi/genera_firmamentum_fenestrale_e.py` non patch obscurum facit.
Singula mutatio anchoram exactam requirit.

Si fons 0.51 mutatur et ancora non iam unica est, constructio **statim
ERRATUM** reddit potius quam codicem incertum generare.

Hoc facit Gradum E auditabilem et facile removendum.

---

## VII. Constructio

Primum Systema BIOS construe, sicut in via UEFI ordinaria:

```bash
./systema/construe_systema.sh
```

Deinde:

```bash
bash systema/uefi/construe_fenestrale_e.sh
```

Exitus:

```text
BOOTX64-FENESTRALE-E.EFI
systema_vindex_uefi_fenestrale_e.img
```

Haec **non substituunt** automatice `BOOTX64.EFI` neque
`systema_vindex_uefi.img` stabiles.

---

## VIII. Criterium regressionis

Gradus E acceptandus est tantum si:

1. nucleus 0.51 ante et post constructionem idem est;
2. fons `firmamentum_uefi.c` canonicus idem est;
3. varians E est PE32+ EFI valida;
4. imago GPT/FAT32 bootabilis construitur;
5. compilatio fit cum `-Wall -Wextra -Werror`;
6. ABI D automatice transit;
7. 0.51 in QEMU eadem interactione veteri uti potest.

Hardware reale post QEMU sequitur.

---

## IX. Quid mutatur pro VINDEX

Primum, bibliotheca:

```text
bibliotheca/fenestrale_ii.vindex
```

potest in vera imagine VINDEX descriptor validum invenire.

Hoc significat Gradus E primum punctum esse ubi client VINDEX potest dicere:

```text
SI FENESTRALE_II_AD_EST() == 1
```

et responsum `1` accipere in systemate realiter bootato.

Nucleus veteris desktop tamen descriptor adhuc ignorat; hoc est intentionalis
status transitionis.

---

## X. Gradus F

Post probationem Gradus E, proximus gradus est primus **client nativus VINDEX**
qui ABI utitur sine framebuffer vetere tamquam fonte veritatis.

Gradus F debet:

- descriptor legere;
- eventa consumere;
- superficiem clientis describere;
- primam fenestram nativam creare;
- compositorium Gradus C cum clientibus conectere;
- PROGRAMMATA minimalem in nova via ostendere.

Via 320×200 nondum deletur; fit fallback donec Gradus F/G maturi sunt.

---

## XI. Regula migrationis

> Nova via intrat sine veterem frangendo.
> Compatibilitas est pons, non destinatio finalis.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
