# VINDEX Fenestrale XCV

Hoc directorium nucleum graphicum et interactivum VINDEX sine systemate
hospite continet.

## Initium in QEMU BIOS

In Fedora:

```bash
sudo dnf install qemu-system-x86-core
./vindex-systema
```

QEMU imaginem `systema_vindex.img` tamquam discum IDE BIOS incipit. Linux non
est nucleus hospes: post BIOS nullum systema inter VINDEX et machinam manet.

## Initium in computatro UEFI

`systema_vindex_uefi.img` est imago disci 64 MiB cum GPT, partitione FAT32 ESP,
partitione VINDEX separata et fasciculo canonico `/EFI/BOOT/BOOTX64.EFI`.
In instrumento graphico Disci
Fedora/GNOME actionem imaginis restituendae elige, imaginem hanc et clavem USB
vacuam indica, deinde computatrum e clave in modo UEFI incipe. CSM vel modus
Legacy non requiritur. Secure Boot inhibendus est, quia applicatio nondum
subscriptionem cryptographicam habet.

**Cave:** restitutio imaginis omnia in clave USB destinata delet. Imago non
est fasciculus Ventoy; in clavem ipsam restituenda est.
Ad institutionem novam versio 0.51 integre restituenda est. Si clavis iam
VINDEX 0.50 vel prior continet et documenta servanda sunt, partitionem ESP monta et
solum `/EFI/BOOT/BOOTX64.EFI` novo fasciculo substitue. Sic partitio VINDEX
intacta manet. Volumen secundae vel tertiae formae primo initio ad quartam
sine amissione documentorum migratur. Programmata vetera in propriam partem
transferuntur, deinde exempla absentia instituuntur. Restitutio totius imaginis
volumen delet.

## Mensa operaria

- intra superficiem QEMU clica ut murem capiat;
- `SCRIPTOR`, `SERPENS`, `FASCICULI` aut `PROGRAMMATA` bis clicare non necesse est: unus clicus aperit;
- fasciam caeruleam fenestrae tene et trahe ut fenestram moveas;
- quadratum dextrum tituli fenestram claudit;
- `INITIUM` menu programmatum supra fasciam operum aperit;
- clavis `1` Scriptorem, clavis `2` Serpentem, clavis `3` Fasciculos et clavis
  `4` Programmata sine mure aperit;
- `Esc` ad mensam operariam redit;
- `Ctrl` + `Alt` + `G` murem a QEMU liberat.

## Scriptor

`SCRIPTOR II` editor textus multarum linearum est. Dispositio clavium AZERTY
adhibetur. Litterae, maiores, numeri, spatium, clavis ingressus, clavis
deletionis et nonnullae notae scribi possunt. Bulla `SERVA` documentum activum
in volumen VINDEX scribit; `APERI` ultimam formam persistentem
restituit. Status `SERVATUM`, `APERTUM` aut `ERRATUM` in ima fenestra apparet.
Sagittae cursorem movent; clicus intra textum cursorem ponit; `Pagina sursum`
et `Pagina deorsum` novem lineas movent. Fenestram visibilem cursor automatice
sequitur. Nomen fasciculi activi in capite et ima fenestra apparet. Singulum
documentum usque ad 4095 octeta continet.
In via BIOS textus per sessionem manet, sed bullae disci `ERRATUM` respondent.

## Fasciculi

`FASCICULI` volumen internum inspicit et sex documenta continere potest.
Ordinem clica ut documentum eligas, deinde `APERI` ut in Scriptore aperias.
`NOVUM` nomen petit et documentum vacuum creat; `NOMEN` electum renominat;
`DELE` dialogum confirmationis aperit et electum tantum post `CONFIRMA` delet.
Nomen maximum octo litteras vel numeros continet, dum
`.TXT` automatice additur. `Intra` nomen confirmat et `Esc` recusat. Ante
primam conservationem `VACUUM` apparet. Volumen 32 KiB in partitione
VINDEX separata continetur; `VINDEX.FS` in ESP via subsidii manet. Firmware
integrum volumen tantum legit vel scribit; forma, signum `VINDEXFS`,
directorium et contentum ipsa VINDEX administrat. Post scripturam pons medium
expurgat et omnia octeta relegit. `SERVATUM` tantum post hanc probationem
apparet. `PARTITIO` in ima fenestra viam binalem activam indicat;
`SUBSIDIUM` viam FAT alternativam indicat.

## Programmata

`PROGRAMMATA` fasciculos nativos suffixi `.VXNAT` in propria parte voluminis ostendit.
`NOVUM` exemplar `TABULA.VXNAT` creat; `EDITE` illud in Scriptore II aperit;
`NOMEN` renominat; `DELE` confirmationem petit; `AGE` programma electum
directe in nucleo exsequitur. Nomen basis maximum sex litteras vel numeros
continet, quia suffixum `.VXNAT` automatice additur. Sex loca documentorum et
sex loca programmatum separata sunt: creatio documenti programma delere neque
occultare potest. Singulum programma usque ad 1279 octeta continet.

Primo initio `SALVE.VXNAT` et `TABULA.VXNAT` automatice instituuntur. Si volumen
0.50 iam `TABULA.VXNAT` continet, migratio illud servat et solum
`SALVE.VXNAT` addit. Deletio voluntaria exemplaris post migrationem observatur;
VINDEX illud in omni initio denuo non creat.

Exemplar graphicum est:

```text
PROGRAMMA TABULA
RECTANGULUM 16 14 220 58 1
MARGO 12 10 228 66 0
LOCUS 32 28
COLOR 15
SCRIBE VINDEX GRAPHICA
LOCUS 32 42
COLOR 11
SCRIBE PROGRAMMA VXNAT
FINIS
```

`PROGRAMMA` titulum declarat; `SCRIBE` reliquam lineam ostendit; `COLOR`
colorem sequentium linearum inter 0 et 15 eligit; `LOCUS x y` locum sequentis
scripturae ponit; `RECTANGULUM x y latitudo altitudo color` aream implet;
`MARGO` iisdem quinque numeris solum limitem pingit; `FINIS` exsecutionem
finit. Coordinatae ad superficiem internam 254×100 pertinent. Mandatum ignotum,
numerus extra superficiem vel color invalidus `PROGRAMMA ERRATUM` ostendit.
Clavis `Esc` aut quadratum tituli ad gestorem Programmatum redit.

Versio 0.49 lineas `SCRIBE` per acumen iam translatum iterum transferre
conabatur, unde glyphi falsi in computatro vero apparebant. Versio 0.50
ordinem pristinum cum indice separato legit; `SALVE.VXNAT` iam servatum sine
ulla mutatione recte ostenditur.

## Serpens

`SERPENS` sagittis gubernatur. Cibus ruber corpus auget et punctum addit.
Margo vel corpus ipsum ludum finit; spatium novum ludum incipit. Motus ab
interruptione PIT centies in secundo mensurata pendet, non ab ansa ficta.

## Reconstructio

```bash
make systema
```

Reconstructio octo exitus creat:

- `boot_systema.bin` — sector BIOS 512 octetorum;
- `nucleus_systema.elf` — nucleus a compilatore VINDEX genitus;
- `fenestrale_systema.bin` — inscriptiones Latinae ambitus;
- `rectores_systema.bin` — rectores PS/2, PIC, PIT et interruptiones;
- `systema_vindex.img` — imago BIOS 1 MiB parata;
- `BOOTX64.EFI` — applicatio UEFI x86-64;
- `systema_vindex_uefi.img` — imago GPT UEFI 64 MiB cum ESP et volumine VINDEX.

Instrumenta GNU `as`, `gcc`, `ld` et `objcopy` sectores ac pontes necessarios
construunt. Mensa, fenestrae, tractio, editor et ludus ipsa VINDEX sunt.

## Ordo initii BIOS

1. BIOS sectorem `boot_systema.bin` ad `0x7C00` legit.
2. Sarcina 128 KiB quattuor lectionibus tutis ad `0x10000` legitur.
3. Forma litterarum BIOS 8×8 ad `0x8000` conservatur.
4. Modus VGA 320×200 cum 256 coloribus aperitur.
5. A20, modus protectus et paginae memoriae constituuntur.
6. Sarcina ad basim physicam `0x400000` transfertur.
7. Modus longus x86-64 aperitur.
8. Rectores ad `0x41F000` IDT, PIC, PIT, IRQ0, IRQ1, IRQ12 et PS/2 constituunt.
9. Nucleus VINDEX paginam communem ad `0x03000000` et memoriam VGA ad
   `0xA0000` directe gubernat.

## Ordo initii UEFI

1. Firmware `/EFI/BOOT/BOOTX64.EFI` e partitione ESP aperit.
2. Pons UEFI protocollo GOP framebuffer RGB vel BGR invenit.
3. ELF nuclei ad basim `0x400000`, textus ad `0x41E000` et formam litterarum
   internam praeparat.
4. Pons partitionem signo `VINDEXV0` per UEFI Block I/O invenit et volumen
   opacum 32 KiB in tabulam legit; `VINDEX.FS` subsidium alternativum manet.
5. Eventa claviaturae, muris relativi vel tabulae absolutae in pagina communi
   VINDEX ponuntur; bullae per duas vicissitudines stabiliuntur contra motus
   falsos tabularum tactilium.
6. Nucleus VINDEX mensam 320×200 in tabulam occultam pingit; pons mutationem
   detegit et imaginem completam ad latitudinem atque altitudinem exactam
   monitoris expandit.
7. Imago perfecta directe in framebuffer linearem transcribitur. Nullus actus
   GOP BLT post initium vocatur, ut VINDEX a vitiis firmware non pendeat.

## Limites 0.51

- x86-64 tantum;
- superficies logica 320×200 est, quamvis UEFI eam ad totum framebuffer
  amplificet; proportio in monitoribus 16:9 paululum dilatatur;
- initium UEFI adhuc officiis firmware ad claviaturam et murem utitur;
- non omne firmware tabulam tactus ut murem UEFI exponit;
- una fenestra activa simul;
- Scriptor maximum 4095 octetorum in singulo documento continet;
- volumen sex documenta `.TXT` et sex programmata `.VXNAT` separat;
- singulum programma `.VXNAT` maximum 1279 octeta continet;
- exsecutor `.VXNAT` septem mandata textus et graphicae habet; computationes generales
  linguae VINDEX nondum ex volumine compilantur;
- persistentia disci UEFI tantum adest; via BIOS memoriam sessionis servat;
- nulla exsecutio multiplex.

Proxima progressio naturalis est exsecutorem `.VXNAT` condicionibus,
variabilibus et interactione claviaturae augere.
