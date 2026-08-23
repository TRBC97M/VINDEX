# FENESTRALE II — GRADUS I
## Duo clientes VINDEX et z-order dynamicus

**Status:** experimentalis, applicatio UEFI separata  
**Series:** Fenestrale II  
**Gradus:** I  
**Praerequisitum:** Gradus H

---

## I. Propositum

Gradus H probavit unum clientem VINDEX in superficie privata a compositor H
componi posse. Gradus I eandem viam ad **multiplices superficies** extendit.

Prima demonstratio continet duos clientes distinctos:

- `PROGRAMMATA H`, client `1`;
- `TABULA I`, client `2`.

Uterque `CREA` et `PRAESENTA` per mailbox `SYLCMP2` utitur. Uterque proprium
buffer XXXII-bit recipit. Framebuffer physicum solus compositor I scribit.

---

## II. Registrum fenestrarum

Compositor habet registrum initiale octo descriptorum superficiei et ordinem
separatum ad z-order. Capacitas octo est **capacitas implementationis
experimentalis**, non numerus locorum UI neque limitatio architecturae ad
programmas definitos. ABI clientis nullum numerum maximum exponit.

Ad novam superficiem:

1. locus liber registri invenitur;
2. memoria pixelorum per `AllocatePool` attribuitur;
3. id crescens datur;
4. index in summum z-order transfertur.

`FOCUS` eandem superficiem ad summum ordinem movet. `DELE` eam ex ordine et
memoria removet.

---

## III. PROGRAMMATA et TABULA

PROGRAMMATA contractum visualem Gradus H retinet.

TABULA I primum clientem alterum praebet. Aspectus eius:

- fenestra quadrata;
- titulus `28 px` vitreo-caeruleus;
- menu `22 px`;
- instrumenta `34 px`;
- area formulae;
- capita columnarum et ordinum;
- rete octo columnarum et duodecim ordinum;
- cellula activa ebur/aqua cum accentu bronzeo;
- status `20 px`.

Hoc nondum est editor tabularum plenus. Est prima superficies nativa TABULA
quae demonstrat duas applicationes simul sine fenestra unica hereditaria.

---

## IV. Taskbar et focus

Taskbar manet `28 px` alta. Compositor I duo botones applicationum ostendit et
buttonem clientis activi clariorem pingit.

In probatione:

- `Tab` focus inter fenestras mutat;
- sagittae fenestram activam movent;
- `Esc` ad firmware redit.

Mouse, resize et minimizatio multi-client postea addi possunt; Gradus I
principaliter possessionem separatarum superficierum et z-order probat.

---

## V. Exsecutio clientium

Compilator VINDEX 0.51 utrumque clientem compactum separatim in ELF64
convertit. Compositor spatium clientis ad `0x00400000` semel attribuit et
clientes **sequentialiter** initio onerat:

1. PROGRAMMATA initium facit et superficiem suam complet;
2. codex clientis e memoria removetur, superficies autem manet;
3. TABULA eodem spatio codicis oneratur et secundam superficiem creat.

Ita duae superficies simul manent, quamquam clientium initia eodem spatio ELF
temporario utuntur. Hoc vitat necessitatem relocatoris ELF in hoc gradu.

---

## VI. Separatio stricta

Gradus I non mutat:

- nucleum canonicum;
- `firmamentum_uefi.c`;
- `BOOTX64.EFI`;
- imaginem UEFI 0.51;
- volumen VINDEX;
- compilatorem VINDEX;
- logicam programmatum `.VXNAT`.

Exitus separati:

```text
FENESTRALEI.EFI
fenestrale_i_uefi.img
```

---

## VII. Probatio

```bash
python3 tests/proba_fenestrale_ii_i.py
bash systema/uefi/construe_fenestrale_native_i.sh
```

CI etiam regressiones D, G et H retinet, deinde ambos clientes compilat,
PE32+ EFI verificat atque imaginem GPT/FAT32 bootabilem construit.

---

## VIII. Proximus gradus

Gradus J potest interactionem multi-client ad murem transferre: hit-testing,
click-to-focus, tractio titlebar, minimizatio et restitutio per taskbar, semper
in runtime experimentali separato.

> Multae fenestrae sunt entitates; non loca fixa.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
