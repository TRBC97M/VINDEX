# FENESTRALE II — GRADUS A
## Probatio framebuffer nativi Sylvia OS

**Status:** experimentum integrationis  
**Series:** Fenestrale II  
**Gradus:** A  
**Systema stabile intactum:** 0.51

---

## I. Propositum

Gradus A primam probationem exsecutabilem Fenestralis II constituit.
Non est mockup HTML neque imago conceptus: est applicatio UEFI x86-64 quae
**framebuffer physicum resolutione nativa directe scribit**.

Systema 0.51 hodiernum adhuc superficiem logicam `320×200` pingit et pons UEFI
eam ad monitoris mensuram amplificat. Gradus A hanc viam non delet, sed viam
novam separatam probat, ut migratio sine regressione fieri possit.

---

## II. Fasciculi

- `systema/uefi/fenestrale_native_a.c` — applicatio UEFI probationis;
- `systema/uefi/construe_fenestrale_native_a.sh` — constructio PE32+ EFI et imaginis bootabilis;
- exitus localis: `FENESTRALEA.EFI`;
- imago localis: `fenestrale_a_uefi.img`.

Nullus fasciculus nuclei 0.51 in hoc gradu mutatur.

---

## III. Quid iam probatur

Applicatio:

1. protocollo GOP UEFI utitur;
2. modum RGB/BGR idoneum invenit;
3. modum optimum saltem `1024×600` quaerit;
4. latitudinem, altitudinem et `PixelsPerScanLine` reales accipit;
5. framebuffer linearem XXXII-bit directe scribit;
6. wallpaper abstractum Sylvia pingit;
7. duas fenestras JL-UX quadratas pingit;
8. PROGRAMMATA et TABULA in eadem superficie simul ostendit;
9. barram operum **XXVIII px** altam pingit;
10. nullam superficiem `320×200` interponit.

Haec est prima probatio codicis qua Sylvia OS visualiter in spatio monitoris
reali constituitur.

---

## IV. Quid consulto nondum probatur

Gradus A nondum continet:

- compositorium verum;
- superficies separatas per fenestram;
- eventa muris;
- tractionem fenestrarum;
- z-order dynamicum;
- fontem JL-UX finalem;
- iconographiam finalem;
- integrationem cum nucleo VINDEX;
- persistentiam;
- executionem programmatum `.VXNAT`.

Textus huius probationis fonte bitmap minimo interno pingitur. Hic fons
**non est** futura familia typographica JL-UX.

---

## V. Ratio securitatis migrationis

Gradus A applicatio separata manet.

Hoc consilium tres utilitates habet:

- 0.51 semper bootare potest dum nova via construitur;
- framebuffer nativus probari potest sine filesystem aut nucleo tangendo;
- regressiones inter pontem UEFI veterem et Fenestrale II clare separantur.

Nulla mutatio in `BOOTX64.EFI` canonico fit antequam gradus nativus in QEMU et
in computatro vero confirmatus sit.

---

## VI. Constructio

Ex radice `vindex_final_v51`:

```bash
bash systema/uefi/construe_fenestrale_native_a.sh
```

Duo exitus fiunt:

```text
FENESTRALEA.EFI
fenestrale_a_uefi.img
```

Vel loca explicita:

```bash
bash systema/uefi/construe_fenestrale_native_a.sh \
    /tmp/FENESTRALEA.EFI \
    /tmp/fenestrale_a_uefi.img
```

Applicatio debet a `file` tamquam PE32+ EFI application agnosci, et
`objdump -p` subsystema `EFI application` monstrare.

Imago bootabilis eodem fabricatore GPT/FAT32 ac Sylvia 0.51 utitur, sed
`/EFI/BOOT/BOOTX64.EFI` probationem Gradus A continet, non systema stabile.

---

## VII. Probatio in firmware

Duae viae sunt.

### Applicatio sola

`FENESTRALEA.EFI` e partitione FAT EFI vel EFI Shell aperiri potest.

### Imago bootabilis

`fenestrale_a_uefi.img` directe in QEMU/OVMF aperiri aut in clavem USB
**experimentalem** restitui potest. Haec imago non est imago Sylvia OS stabilis.

Cum recte incipit:

- wallpaper caeruleum totam resolutionem realem implet;
- PROGRAMMATA et TABULA simul apparent;
- barra operum ima tenuis est;
- nomen `SYLVIA OS` discrete in demonstratione technica apparet;
- nulla vox `JL-UX` in desktop scribitur.

Clavis `Esc` ad firmware redit.

---

## VIII. Criterium ad Gradum B

Gradus A completus habetur cum eadem applicatio saltem in his condicionibus
recte ostensa est:

- QEMU + OVMF;
- unum monitor 1024×768 vel maius;
- unum monitor 16:9;
- hardware UEFI verum;
- pixel format RGB;
- pixel format BGR, si firmware illum offert.

Deinde Gradus B incipit: **superficies XXXII-bit separatae et compositorium
minimum**, primum cum duabus fenestris staticis, postea cum z-order et damage
rectangles.

---

## IX. Regula canonica confirmata

> Desktop Sylvia non est imago 320×200 dilatata.
> Desktop Sylvia est superficies resolutionis nativae.

Fenestrale II hanc regulam a Gradus A in codice, non tantum in documento,
incipit efficere.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
