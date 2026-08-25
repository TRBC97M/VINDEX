# Ponticulus UEFI in VINDEX puro — primus gradus probatus

## Propositum

`ARCHITECTURA.md` post PR #30 puritatem VINDEX absolutam statuit, cum una
exceptione: `bootstrap_uefi.c` (264 lineae C). Quaestio proposita est:
**estne haec exceptio vere necessaria, an potest etiam ponticulus ipse in
VINDEX scribi?**

Haec relatio primum gradum probationis continet. Responsum breve: **exceptio
non est necessaria; via aperta est.**

## Quid iam habemus (nihil novum requirens)

| Facultas necessaria | Status |
|---|---|
| Generare PE32+ validum | **IAM FACTUM** — `CONSTRUE_CAPUT_PE`, opus sessionis Win64 |
| Vocare firmware per ABI Microsoft x64 | **IAM FACTUM** — `UEFI_VOCA6`, adhibitum XIX vicibus in `nucleus.vindex` |
| Accessus memoriae crudus, scriptio ad adressam fixam | **IAM FACTUM** — `CONTENTUM`, `SEDES` |
| Invenire protocollum graphicum, legere clavem/murem per UEFI | **IAM FACTUM in VINDEX** intra `nucleus.vindex` |

Nucleus VINDEX iam vocat `LocateProtocol`, iam legit clavem et murem
nativa. Quod ponticulus C facit, VINDEX alibi iam facit.

## Quid deest (et quantum)

### 1. Modus `pe-uefi` in compilatore

Tres differentiae a modo `pe` currenti:

- **Subsystem**: linea 386 `src/compilator_vindex.vindex` scribit
  `SCRIBE_U16(codex, 156, 3)` (console Windows). Pro UEFI requiritur **10**.
  *Una cifra.*
- **Nulla tabula importationis**: UEFI `kernel32.dll` non praebet; omnia per
  tabulam systematis in parametro accepta transeunt. Ergo sectio `.idata`
  omnino omittenda est — simplificatio, non complicatio.
- **Ingressus cum parametris**: punctum ingressus accipit
  `(ImageHandle in RCX, SystemTable in RDX)`, non prologum Windows currentem.

### 2. Ponticulus ipse in VINDEX

`bootstrap_uefi.c` habet 264 lineas, sed ex his **circiter 108 sunt merae
declarationes generum UEFI** (structurae firmware), non logica. Codex vere
exsecutabilis circiter 150 lineas habet, ex quibus duae functiones triviales
sunt (`memoria_vacua`, `memoria_copia`).

Logica realis: protocollum graphicum invenire, modum eligere, nucleum in
memoriam copiare, sedecim metadata implere, salire.

### 3. Saltus finalis

Nunc quinque instructiones assembler inline (`mov rsp`, `and`, `call`,
`hlt`, `jmp`). Solvi potest per primitivam VINDEX propriam, vel per
emissionem octetorum directam (quam VINDEX iam facit).

## Probationes vere exsecutae

Duo prototypa Python (eadem methodo qua `construe_pe_reference.py` pro
backend Win64: mechanismum probare ante integrationem).

### Prototypum I — `construe_efi_reference.py`

Exsecutabile UEFI minimum: `xor rax,rax ; ret` (reddit `EFI_SUCCESS`).

- `file` confirmat: `PE32+ executable (EFI application) x86-64` ✓
- Subsystem in capite = **10** ✓
- Sub QEMU + OVMF (firmware UEFI verum): firmware onerat et exsequitur
  (`BdsDxe: starting Boot0001`), deinde ad menu redit — comportamentum
  exspectatum cum applicatio EFI `EFI_SUCCESS` reddit ✓

### Prototypum II — `construe_efi_salve.py`

Exsecutabile quod **vere firmware vocat** ut nuntium scribat:

```
sub rsp, 40                ; spatium umbrae Win64
mov rax, [rdx+0x40]        ; RAX = SystemTable->ConOut
mov rcx, rax               ; arg1 = ConOut (this)
lea rdx, [rip+nuntius]     ; arg2 = catena UTF-16
call [rax+0x08]            ; ConOut->OutputString
xor eax, eax               ; EFI_SUCCESS
add rsp, 40
ret
```

**Resultatum sub QEMU + OVMF: `VINDEX UEFI` in schermo vere apparuit.** ✓

Hoc probat non solum onerationem, sed vocationem firmware realem ex codice
nostro, cum ABI Microsoft x64 correcta — id est, exacte quod `UEFI_VOCA6`
in VINDEX iam facit.

## Conclusio et gradus proximi

Mechanismus omnino probatus est. Nihil in hac via requirit C.

Gradus proximi suasi, ordine:

1. Addere modum `pe-uefi` compilatori (subsystem 10, sine `.idata`,
   ingressus cum parametris) — mutatio parva, super infrastructuram
   `CONSTRUE_CAPUT_PE` iam existentem.
2. Scribere `bootstrap.vindex` minimum qui idem facit quam prototypum II,
   sed compilatus per `compilator_vindex ... pe-uefi`.
3. Gradatim logicam `bootstrap_uefi.c` migrare: protocollum graphicum,
   electio modi, copia nuclei, metadata.
4. Saltum finalem solvere (primitiva nova vel octeta directa).
5. Cum versio VINDEX probata est sub QEMU, `bootstrap_uefi.c` removere et
   `verifica_puritatem_sylviae.py` stringere ut nullum omnino fasciculum C
   admittat.

**Cautio**: ponticulus fractus = machina quae omnino non incipit, sine ullo
nuntio erroris. `bootstrap_uefi.c` servandus est functionalis donec versio
VINDEX plene probata sit; deinde substitutio fiat.

VINDEX Latine cogitat. Sylvia Latine loquitur.
