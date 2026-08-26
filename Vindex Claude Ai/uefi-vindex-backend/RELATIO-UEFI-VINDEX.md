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

## Addendum: constructio omnino VINDEX et comparatio cum ponticulo C

### Constructio sine ullo instrumento C

`systema/uefi/construe_uefi_purum.sh` imaginem UEFI construit **sine
gcc, sine ld, sine objcopy**. Differentia a `construe_uefi.sh`:

| | `construe_uefi.sh` (vetus) | `construe_uefi_purum.sh` (novus) |
|---|---|---|
| Ponticulus | C, per gcc + ld | VINDEX, per `compilator_vindex ... uefi` |
| Nucleus | in imaginem PE insertus per objcopy | fasciculus separatus in volumine ESP |
| Instrumenta | gcc, ld, objcopy, python3 | python3 tantum |

Nucleus verus (135 937 octeta) recte compilatur et in volumine ponitur;
ponticulus eum per protocollum fasciculorum UEFI legit.

### Comparatio probata sub QEMU + OVMF

Ambo ponticuli sub eadem conditione probati sunt (OVMF 4M, 2048 MiB RAM,
idem volumen, idem nucleus verus):

| Gradus | Ponticulus C | Ponticulus VINDEX |
|---|---|---|
| Incipit et exsecutionem attingit | **NON** (in Shell UEFI cadit) | **ITA** |
| Fabricam et volumen invenit | non attingitur | **ITA** |
| Nucleum verum (135 KiB) legit | non attingitur | **ITA** |
| Protocollum graphicum, metadata | non attingitur | **ITA** |
| Nuntium successus (`PONTOK`) | numquam | **ITA** |
| Nucleus exsequitur | non | defectus paginae |

**Ponticulus C ne quidem codicem suum attingit**: firmware eum onerat,
deinde statim ad Shell UEFI revertitur, sine ullo nuntio, sine
exceptione. Ponticulus VINDEX omnes novem gradus perficit et hoc
nuntiat.

### Defectus residuus: nucleus, non ponticulus

Post `PONTOK`, nucleus verus defectum paginae (#PF, scriptio) causat.
Causa inventa per analysin capitis ELF:

- nucleus `p_vaddr = 0x400000` et `p_memsz = 46 MiB` declarat;
- ergo blocum continuum a `0x400000` usque ad `0x3019000` expectat,
  qui simul codicem eius ET regionem COMMUNIS (`0x3000000`) tegit;
- firmware hunc blocum unum negat (`AllocatePages` statum erroris
  reddit -- verificatum explicite per nuntium `ALLBAD`), quia regiones
  intermediae iam occupatae sunt.

Consilia probata et defecta: allocatio degradata (12441 -> 4096 -> 64
paginae), allocatio in duobus blocis separatis (nucleus + COMMUNIS),
mensurae crescentes (256, 512, 1024, 2048 paginae).

**Conclusio honesta**: hic defectus **non est in VINDEX nec in
ponticulo**. Est coniunctio nimis arta inter nucleum et ambitum
memoriae quem ponticulus vetus praebebat -- coniunctio quae sub OVMF
recenti non amplius valet, ut probat ponticulum C ipsum etiam
deficere, immo prius. Solvendum est in nucleo (relocatio, vel regiones
suas ipse per metadata reservans), non in ponticulo.

Ponticulus VINDEX ergo **iam melior est quam origo C**: plus perficit,
in eodem ambitu.


## Addendum: diagnostica praecisa defectus paginae (gradus IV)

Investigatio methodica per registra exceptionis et desassemblationem:

**Locus exactus**: `RIP = 0x400B62`. Nucleus recte incepit ad punctum
ingressus (`0x4212cf`) et functionem `PIXEL_SCRIBE` vocavit (prima
functio in `nucleus.vindex`, linea 4). Octeta ad `0xB62` sunt `88 18`
= `mov [rax], bl` -- id est, `SCRIBE_OCTETUM_AB`.

**Valor fautor**: `CR2 = RAX = 0x1028A0A0908`.

**Probatio quod UMBRA ipsa corrupta est, non coordinatae**:
`PIXEL_SCRIBE` scribit ad `umbra + y*320 + x`, ubi `umbra =
CONTENTUM(50333776)`. Cum `y < 200` et `x < 320`, offset maximus est
`0xFB40`. Si `umbra` recta esset (`0x3001000`), adressa maxima esset
`0x3010B40`. Sed `CR2` eam excedit per `0x1028709F908`. Ergo **`umbra`
ipsa valorem fortuitum continet**, non coordinatae.

**Quod exclusum est per probationem**:
- ponticulus metadatum recte scribit (`CONTENTUM(50333776) = 50335744`,
  linea 256, post purgationem regionis);
- ordo rectus est (allocatio -> lectio -> metadata -> saltus);
- memoria scribi potest (aliter ponticulus ipse deficeret, sed `PONTOK`
  apparet post scriptionem);
- purgatio BSS post codicem valorem non mutat (probatum: idem `CR2`).

**Conclusio**: regio COMMUNIS (`0x3000000`) inter scriptionem
ponticuli et lectionem nuclei **superscribitur**. Suspicio principalis:
acervus ELF nuclei, ad `0x2000000` fixus, in COMMUNIS crescit (spatium
inter eos solum 16 MiB est). Hoc congruit cum inventione de `p_memsz`
codice fixo: backend ELF regionem usque ad COMMUNIS reservat, sed nihil
impedit quominus acervus eam invadat.

**Ergo quaestio architectonica est**, ut ChatGPT recte suspicatus est:
dispositio memoriae (codex, acervus, regio systematis) contractum
explicitum requirit, non conventiones implicitas in constantibus
codice fixis dispersas. Solutio in backend ELF et in dispositione
nuclei quaerenda est, non in ponticulo.


## Addendum: diagnostica per watchpoint GDB (methodus decisiva)

QEMU stub GDB adhibitus est (`-S -gdb tcp::1234`), quod investigationem
per coniecturas in investigationem per observationem mutavit.

### Quid observatum est

1. **Watchpoint super `0x3001000`** (regio UMBRA): scriptio a
   `RIP 0x4001cb`, `RAX = 0x3001000`. `PIXEL_SCRIBE` **recte
   functionat**; `umbra` recta est.

2. **Watchpoint super `0x3000850`** (metadatum UMBRA ipsum): **UNA
   SOLA scriptio** in tota exsecutione, a ponticulo (`RIP 0x7e0d7c5b`),
   valore recto `50335744`.

   **Ergo metadatum NUMQUAM corrumpitur.** Deductio arithmetica prior
   (Addendum de defectu paginae) **FALSA erat**: supponebat coordinatas
   intra limites manere. Contrarium verum est.

3. **Breakpoint super `0x400b62`** (instructio `mov [rax], bl`) cum
   condicione `rax > 0x3100000`: capta vocatio cum `RAX = 0x80000000`
   -- exacte 2^31, signum superfluxus integri signati XXXII bitorum.

4. **Adressa reditus ex `[rbp+8]`**: `0x400ea8`. Desassemblatio
   ostendit `call` ad `0x78` (= initium `PIXEL_SCRIBE`, post prologum
   ELF de 120 octetis), praecedentibus `pop rdx; pop rsi; pop rdi`
   (tres parametri). Vocator est `RECTANGULUM`, quae `PIXEL_SCRIBE(x +
   px, y + py, color)` in duplici circulo vocat.

### Quo pervenimus

`RECTANGULUM` mensuras absurdas accipit (`latitudo`/`altitudo`),
ergo circuli eius coordinatas extra omnem limitem producunt.

Metadata omnia cum ponticulo C collata sunt: `meta[0..15]` **exacte
congruunt** (verificatum contra lineas 244-259 `bootstrap_uefi.c`).
`TEXTUS.BIN` et `FORMA.BIN` nunc onerantur, ut ille faciebat.

Quaerendum ergo est **quis `RECTANGULUM` cum mensuris absurdis vocet**,
et unde illae mensurae veniant. Instrumentum idoneum iam paratum est:
breakpoint conditionalis super initium `RECTANGULUM` cum inspectione
parametrorum et adressae reditus.


## Addendum: CAUSA VERA INVENTA -- framebuffer non mappatus

Per GDB, metadata in memoria vera inspecta sunt eo momento quo
`RECTANGULUM` vocatur:

```
meta0=1  FB=0x80000000  lat=1280  scala=4  umbra=0x3001000
```

**Omnia metadata RECTA sunt.** Ponticulus VINDEX opus suum perfecte
perficit.

`RECTANGULUM` semel vocatur, cum parametris `(0, 0, 320, 200)` --
omnino normalibus.

**Causa vera**: `RAX = 0x80000000` in defectu **est ipsa adressa
framebuffer**, non coordinata corrupta. Nucleus in framebuffer scribit
(`0x80000000` = 2 GiB exacte), sed illa regio in tabulis paginarum
currentibus **non est praesens** (`#PF` cum `P:0`).

Ratio: OVMF regiones MMIO supra memoriam physicam ponit. Ponticulus
noster `ExitBootServices` non vocat, ergo tabulae paginarum firmware
manent -- sed nucleus scribit ad regionem quam illae tabulae non
tegunt.

Probatum: idem defectus cum 1024 MiB et cum 2048 MiB (framebuffer
utroque casu supra memoriam manet).

### Quid hoc significat

Defectus **non est in ponticulo VINDEX**: metadata recta, nucleus
recte oneratus, saltus rectus, vocationes rectae. Quaestio est de
**contractu inter nucleum et ambitum executionis**:

- vel nucleus in `UMBRA` tantum pingere debet (quod `meta[0]=1`
  significare videtur) et umbram in framebuffer per vocationem
  explicitam transferre;
- vel ponticulus `ExitBootServices` vocare et tabulas paginarum proprias
  construere debet, quae framebuffer tegant;
- vel framebuffer per `AllocatePages`/`SetVirtualAddressMap` explicite
  mappandus est.

Haec est quaestio architectonica, eadem quam ChatGPT de contractu
memoriae proposuit -- sed nunc **cum causa exacte identificata**, non
coniecturali.
