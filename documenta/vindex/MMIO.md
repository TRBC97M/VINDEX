# MMIO typatum in VINDEX

## I. Finis

P12-V1 primam viam canonicam ad registra memoriae apparatuum instituit. Accessus
MMIO non est memoria ordinaria: latitudo instructionis, ordo et numerus
lectionum effectum hardware mutare possunt. Quattuor lectiones octeti ergo
lectionem atomicam XXXII bitorum substituere non possunt.

## II. Primitivae compilatoris

Compilator emittit:

- `MMIO_LEGE8`, `MMIO_LEGE16`, `MMIO_LEGE32`, `MMIO_LEGE64`;
- `MMIO_SCRIBE8`, `MMIO_SCRIBE16`, `MMIO_SCRIBE32`, `MMIO_SCRIBE64`;
- `MMIO_SEPES`, quae instructionem x86 `MFENCE` emittit.

Quaeque lectio una instructione memoriae latitudinis exactae efficitur.
Scriptio nihil (`0`) reddit. Compilator accessus non coalescit nec eliminat;
ordo fontis manet ordo instructionum. Primitivae humiles terminos non probant:
rectores per descriptor `MMIO_REGIO` eas vocare debent.

## III. Descriptor regionis

Descriptor LXIV octeta continet basim physicam et virtualem, mensuram,
paginam primam, longitudinem paginarum, permissiones, generationem et ultimum
erratum. `MMIO_ADRESSA` ante accessum probat:

- latitudinem esse 1, 2, 4 aut 8;
- intervallum et finem intra regionem manere;
- alignationem naturalem;
- permissionem lectionis aut scriptionis.

`MMIO_PCI_MAPPA` tantum BAR memoriae accipit. Adressa et mensura ex P12-IV
veniunt; BAR portuum reicitur.

## IV. Mappatio UEFI hodierna

OVMF regiones PCI in spatio UEFI identitate mappat. P12-V1 hanc rem non celat:
`basis_virtualis == basis_physica` et vexillum `MMIO_IDENTITAS` ponitur. Haec
est mappatio realis ambitus praesentis, sed nondum proprietas tabularum
paginarum Sylviae.

Incrementum sequens gestorem paginarum et attributa cache (UC/WC) possidebit.
Tum basis virtualis mutari poterit sine mutatione API rectorum.

## V. Probationes

`mmio_primitivae.vindex` omnes latitudines et octeta finitima probat.
`mmio_regiones.vindex` terminos, alignationem, permissiones et sepem probat.
`proba_pci_mmio_053.sh` sub QEMU/OVMF e1000e post pontem PCIe creat, BAR 0
mappat et registrum `STATUS` bis legit. Nulla scriptio in apparatum fit.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
