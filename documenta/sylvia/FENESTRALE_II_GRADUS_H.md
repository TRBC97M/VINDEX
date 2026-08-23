# FENESTRALE II — GRADUS H
## Compositorium exsecutabile cum cliente PROGRAMMATA VINDEX

**Status:** experimentalis, applicatio UEFI separata  
**Series:** Fenestrale II  
**Gradus:** H  
**Praerequisitum:** Gradus G

---

## I. Propositum

Gradus G pactum mailbox et superficiem privatam definivit. Gradus H primum
compositorium exsecutabile introducit quod hoc pactum **re vera administrat**.

Catena huius probationis est:

```text
PROGRAMMATA G (VINDEX)
        ↓ CREA
mailbox SYLCMP2
        ↓
compositor UEFI H
        ↓ memoria privata XXXII-bit
PROGRAMMATA G pingit
        ↓ PRAESENTA
compositor H
        ↓
framebuffer GOP nativus
```

Ita client VINDEX non amplius framebuffer physicum directe scribit.

---

## II. Separatio a Systemate canonico

Gradus H consulto applicatio UEFI propria est.

Non mutat:

- `systema/nucleus.vindex`;
- `systema/uefi/firmamentum_uefi.c`;
- `BOOTX64.EFI` canonicum;
- `systema_vindex_uefi.img` canonicam;
- volumen 0.51;
- exsecutionem `.VXNAT` Systematis principalis.

Exitus sunt:

```text
FENESTRALEH.EFI
fenestrale_h_uefi.img
```

Hoc consilium servat separationem inter opus visuale Fenestralis II et
progressionem nuclearem Sylvia OS.

---

## III. Client VINDEX verus

Scriptum constructionis `programmata_fenestrale_ii_g.vindex` compilat per
compilatorem VINDEX existentem. ELF resultans in applicationem UEFI H includitur.

Compositor memoriam clientis ad `0x00400000` ponit eodem principio quo pons
UEFI VINDEX hodiernus imaginem ELF nuclei tractat. Ingressus ELF ex campo
`e_entry` legitur et ante exsecutionem intra magnitudinem imaginis verificatur.

Client Gradus G est machina statuum parva:

1. prima vocatio `CREA` petit;
2. compositor memoriam privatam attribuit et `PERFECTUM` respondet;
3. secunda vocatio PROGRAMMATA in buffer datum pingit et `PRAESENTA` petit;
4. compositor superficiem componit;
5. tertia vocatio responsum consumit et mailbox vacuam relinquit.

Hic circuitus est prima probatio end-to-end clientis VINDEX per ABI compositorii.

---

## IV. Memoria communis

Gradus H paginam communem experimentalem circa `0x03000000` attribuit et ibi
contractus D/G collocat:

```text
0x03000900  descriptor Fenestralis II
0x03000E00  mailbox compositorii
0x03001000  locus UMBRAE hereditariae, hic a cliente H non adhibitus
```

Descriptor declarat:

- framebuffer nativum;
- formatum RGB/BGR;
- compositorium;
- resolutionem realem;
- `PixelsPerScanLine` realem;
- XXXII bits per pixel;
- taskbar `28 px`;
- scala `1000` per mille.

---

## V. Administratio superficiei

Ad `CREA`, compositor:

- latitudinem et altitudinem validat;
- memoriam per UEFI `AllocatePool` attribuit;
- superficiem id `1` dat;
- buffer, stride et formatum in mailbox reddit;
- fenestram intra spatium supra taskbar centrum collocat.

Superficies clientis ut formatum XXXII-bit cum alpha utitur. PROGRAMMATA G
pixels opacos alpha `255` scribit.

Ad `PRAESENTA`, compositor:

- buffer clientis legit;
- alpha componit;
- wallpaper abstractum Sylvia reddit;
- umbram brevem fenestrae addit;
- taskbar JL-UX XXVIII px super omnia componit;
- framebuffer GOP RGB vel BGR scribit.

---

## VI. Norma visualis servata

PROGRAMMATA ipsa adhuc contractum Gradus G pingit:

- anguli `0 px`;
- titulus `28 px`;
- menu `22 px`;
- instrumenta `34 px`;
- status `20 px`;
- vitrum caeruleum mineralis;
- superficies ebur et argentum;
- bronzeum rarum;
- clausura rubra;
- tres regiones collectionum/index/proprietatum;
- `TABULA.VXNAT` unicum programma initiale;
- nulla inscriptio `JL-UX` in desktop.

Taskbar a compositor H possidetur et semper `28 px` alta est.

---

## VII. Interactio probationis

Post compositionem:

- sagittae fenestram PROGRAMMATA movent;
- `Esc` ad firmware redit.

Motus hic compositoris probatio est, non API interactionis finalis. Mouse,
hit-testing clientis, resize et multiplex superficies ad gradus posteriores
reservantur.

---

## VIII. Constructio

Ex radice `vindex_final_v51`:

```bash
bash systema/uefi/construe_fenestrale_native_h.sh
```

Vel:

```bash
bash systema/uefi/construe_fenestrale_native_h.sh \
  /tmp/FENESTRALEH.EFI \
  /tmp/fenestrale_h_uefi.img
```

Scriptum:

1. clientem PROGRAMMATA G compilat;
2. ELF64 et ingressum eius verificat;
3. ELF ut sectionem binariam in PE32+ includit;
4. compositorium UEFI H compilat;
5. subsystema `EFI application` verificat;
6. imaginem GPT/FAT32 bootabilem facit.

---

## IX. Criterium probationis

Gradus H rite constructus est si CI confirmat:

- Gradus D ABI;
- regressionem PROGRAMMATA F;
- Gradus G contractum;
- contractum staticum H;
- compilationem realem PROGRAMMATA G;
- PE32+ EFI validum;
- imaginem bootabilem non vacuam.

Antequam aliquid ex H in viam canonicam transferatur, imago separata in
QEMU/OVMF et deinde hardware UEFI vero probanda est.

---

## X. Proximus gradus

Gradus I debet **multiplices superficies** et registrum dynamicae fenestrarum
introducere, adhuc in runtime experimentali separato. Inde PROGRAMMATA et
TABULA possunt simul clientes distincti fieri, sine limite sex locorum aut
unius fenestrae.

> Compositor videt scrinium; client videt superficiem suam.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
