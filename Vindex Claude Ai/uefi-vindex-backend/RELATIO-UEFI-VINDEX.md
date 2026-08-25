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

## Gradus II probatus: VINDEX purus firmware UEFI vocat

Post modum `uefi` compilatori additum (commit `7797906`), probatio
sequens facta est: programma **in VINDEX puro scriptum**, per
`compilator_vindex ... uefi` compilatum, quod firmware ipsum vocat.

Vide `exempla/salve_uefi.vindex` (fons) et `exempla/salve_uefi.efi`
(exsecutabile generatum).

Mechanismus:
1. Prologus modi `uefi` `SystemTable` (RDX a firmware acceptam) ad
   `0x1000008` servat;
2. programma eam legit per `CONTENTUM(16777224)`;
3. `SystemTable->ConOut` ad offset 64, `ConOut->OutputString` ad offset 8;
4. `UEFI_VOCA6(scribe_catenam, conout, SEDES(nuntius), 0, 0, 0, 0)`.

**Resultatum sub QEMU + OVMF: `VINDEX` in schermo vere apparuit.**

Hoc probat catenam completam: fons VINDEX -> `compilator_vindex` ->
exsecutabile EFI -> firmware verum -> vocatio servitii firmware ->
exitus in schermo. **Nullus C in tota via.**

### Duo impedimenta vera inventa (documentanda pro opere sequenti)

1. **`ORDO DE LITTERA` octeta compacta non praebet.** Elementa per octo
   octeta disponuntur, non per unum (verificatum: `SEDES(t[1]) -
   SEDES(t[0])` non unum reddit; `CONTENTUM(SEDES(t[0]))` valorem
   integrum reddit). Ergo catenae CHAR16 (UTF-16, duo octeta per
   litteram) directe construi non possunt hoc modo. **Consilium
   adhibitum**: quattuor litteras CHAR16 in uno verbo LXIV-bit componere
   (`littera + littera*65536 + littera*2^32 + littera*2^48`), quod
   dispositionem memoriae rectam producit. **Solutio vera pro futuro**:
   primitivam VINDEX addere quae octeta singula in memoriam scribat
   (velut `SCRIBE_OCTETUM(adressa, valor)`), quae etiam pro ponticulo
   completo necessaria erit.

2. **Litterales numerici magni compilatorem exhauriunt.** Constans
   `281474976710656` (2^48) scripta directe compilationem occidit
   (status 137, memoria exhausta). **Consilium adhibitum**: valores per
   multiplicationes successivas computare (`k16 = 65536; k32 = k16 *
   k16; k48 = k32 * k16`). Causa radicalis non investigata; defectus
   verisimiliter in analysi litteralium magnorum latet, seorsum ab opere
   UEFI, sed notandus.

### Gradus proximi

Cum catena probata sit, opus sequens est migratio ipsius ponticuli:
protocollum graphicum invenire (`LocateProtocol`, quod `nucleus.vindex`
iam facit), modum eligere, nucleum copiare, metadata implere, salire.
Primitiva `SCRIBE_OCTETUM` (vel similis) prius addenda videtur, quia
copia memoriae octetim necessaria est.

VINDEX Latine cogitat. Sylvia Latine loquitur.
