# Interruptiones MSI in VINDEX

## I. Finis

P12-V3 primam viam canonicam ab apparatu PCI ad tractatorem VINDEX instituit.
Probatio non statum registri iterum iterumque legit ut interruptionem simulet:
apparatus QEMU EDU MSI ad APIC mittit, porta IDT ad codicem VINDEX ducit,
tractator causam legit atque agnoscit, EOI scribit et per `IRETQ` redit.

Hoc incrementum infrastructura est, nondum gubernator generalis. Portae IDT,
capacitas MSI et commandum PCI post probationem ad valores exactos pristinos
restituuntur.

## II. ABI tractatoris

Nova declaratio linguae est:

```vindex
INTERRUPTIO TRACTATOR.
    // corpus sine SIMD/FPU
    REDDE 0.
FIN-INTERRUPTIO.
```

Compilator:

- quindecim registra generalia servat, `RSP` excepto;
- `RBP` ad pilam servatam ponit atque `RSP` ad XVI octeta coaequat;
- corpus ordinarium VINDEX cum vocationibus functionum componit;
- registra ordine inverso restituit et `IRETQ` emittit.

`REDDE` intra `INTERRUPTIO` epilogum interruptionis emittit. Finis implicitus
eundem epilogum habet. `SEDES_FUNCTIONIS(nomen)` adressam relocabilem
RIP-relativam reddit; relocatio differenda tractatorem post vocantem declarari
sinit.

Hic ABI tantum **interruptiones externas sine codice erroris** accipit.
Exceptiones x86 quae codicem erroris in pilam imponunt alium prologum
requirebunt. Compilator VINDEX hodie SIMD/FPU non emittit; status XMM/FPU ideo
nondum servatur. Antequam SIMD in lingua admittatur, ABI interruptionum
extendendus est.

## III. Primitivae privilegiatae

Compilator has primitivas x86-64 praebet:

- `IDTR_LEGE(adressa)` — `SIDT` ad descriptorem decem octetorum;
- `INTERRUPTIONES_STATUS()` — `PUSHFQ` et valor `RFLAGS`;
- `INTERRUPTIONES_CLAUDE()` — `CLI`;
- `INTERRUPTIONES_APERI()` — `STI`;
- `CODICIS_SELECTOR()` — selector `CS`;
- `SEDES_FUNCTIONIS(nomen)` — adressa codicis RIP-relativa.

`interruptiones.vindex` mutationes IDT/MSI reicit si `IF=1`. Vocator statum
pristinum servat, interruptiones claudit, transactionem perficit et statum
per `IN_STATUS_RESTITUE` reddit.

## IV. IDT et contextus

Rector unam paginam in regione communi Sylviae ad `0x03002000` per
UEFI `AllocateAddress` possidet. Contextus continet basim MMIO, numerum atque
causam IRQ, portam IDT pristinam, descriptorem IDTR, `RFLAGS`, selectorem `CS`
et statum transactionum.

`IN_IDT_INSTALLE` limitem IDTR probat, portam XVI octetorum servat et portam
interrupti praesentem generis `0x8E` construit. `IN_IDT_RESTITUE` duas partes
LIV bitorum exactas restituit. Pagina liberari non potest dum porta IDT aut
descriptor MSI activus est.

## V. Capacitas MSI

`PCI_CAPACITAS_INVENI` indicem capacitatum PCI terminis et numero visitationum
munitum percurrit. `IN_MSI_ACTIVA`:

1. MSI et numerum nuntiorum interim inhibet;
2. formas XXXII et LXIV bitorum distinguit;
3. adressam APIC `0xFEE00000` et vectorem ponit;
4. si larva per-vector adest, solum nuntium primum aperit;
5. MSI activat et statum lectum confirmat.

`IN_MSI_RESTITUE` MSI primum inhibet, larvam, datum, partes adressae et caput
ordine tuto restituit. Primus contractus ad unum CPU QEMU limitatur et APIC ID
zero petit. Iter ad SMP postea destinationem ex APIC ID CPU currentis derivabit;
P12-V3 hanc facultatem nondum fingit.

## VI. Probationes

`proba_interruptiones_abi_053.sh` calculos portae/MSI native exercet et in PE
genito prologum, `SIDT`, `RFLAGS`, `CS`, sedem RIP-relativam atque `IRETQ`
quaerit.

`proba_interruptiones_msi_053.sh` sub QEMU/OVMF q35, uno CPU et apparatu EDU:

1. EDU `1234:11E8` post pontem PCIe invenit et BAR0 mappat;
2. portam `0xF1` instituit et capacitatem MSI vere programmat;
3. valorem `0x40` ad registrum `IRQ raise` scribit;
4. solum incrementum a tractatore factum ut probationem receptionis accipit;
5. causam `0x40` agnoscit et pendens zero requirit;
6. IDT, MSI, commandum PCI atque statum `IF` restituit.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
