# VINDEX 0.53 — Contractus fasciculorum Win64

## Propositum

Hoc documentum limen inter analysatorem VINDEX et stratum API Win64 definit. Nulla mutatio semanticam VINDEX mutare debet: idem fons in modo ELF et PE eandem notionem descriptoris, lectionis, scripturae et clausurae servat.

## Conventio vocationis Win64

API Win64 non utitur conventione System V interna VINDEX. Ante vocationem API:

- argumenta I–IV ponuntur in `RCX`, `RDX`, `R8`, `R9`;
- XXXII octeta *shadow space* a vocatore reservantur;
- argumentum V incipit ad `[rsp+32]`, VI ad `[rsp+40]`, VII ad `[rsp+48]` ante instructionem `CALL`;
- `RSP` ad XVI octeta ordinatus manet ante `CALL`;
- `RAX` valorem reditum continet.

Ita emitter API separatus a vocationibus functionum VINDEX manere debet. Conventio System V septem argumentorum ad API Win64 directe adhiberi non potest.

## Importationes KERNEL32 necessariae

Stratum fasciculorum requirit:

```text
CreateFileA
ReadFile
CloseHandle
```

`WriteFile` a strato communi `PROCLAMA`/`MITTE` iam possidendo Claudii adhibebitur. `GetStdHandle`, `VirtualAlloc` et `ExitProcess` eodem descriptorio IAT communi servantur.

## APERI_LEGERE

Semantica VINDEX hodierna: nomen viae accipitur, descriptor redditur, valor negativus errorem significat.

Vocatio Win64 proposita:

```text
CreateFileA(
    via,
    GENERIC_READ,        // 0x80000000
    FILE_SHARE_READ,     // 1
    NULL,
    OPEN_EXISTING,       // 3
    FILE_ATTRIBUTE_NORMAL, // 0x80
    NULL
)
```

`CreateFileA` in errore `INVALID_HANDLE_VALUE` (`-1`) reddit; hoc cum probatione VINDEX `descriptor < 0` naturaliter congruit.

## APERI_SCRIBERE

Semantica ELF hodierna `O_WRONLY|O_CREAT|O_TRUNC` est. Vocatio Win64 correspondens:

```text
CreateFileA(
    via,
    GENERIC_WRITE,       // 0x40000000
    0,
    NULL,
    CREATE_ALWAYS,       // 2
    FILE_ATTRIBUTE_NORMAL,
    NULL
)
```

Valor reditus idem contractum descriptoris servat.

## LEGE

`LEGE(descriptor, numerus)` in VINDEX memoriam temporariam reservat, ex fonte legit, numerum octetorum redit et octeta per `OCTETUS(i)` postea praebet.

Win64:

```text
ReadFile(
    descriptor,
    buffer,
    numerus,
    &lecta,
    NULL
)
```

Dispositionis pilae exemplum ante `CALL`:

```text
[rsp+00 .. +31] shadow space
[rsp+32]         argumentum V = NULL
[rsp+40]         DWORD lecta + spatium
```

`R9` ad `[rsp+40]` demonstrat. XLVIII octeta reservata ordinationem XVI servant. Si `ReadFile` falsum reddit, VINDEX `-1` reddere debet; aliter `lecta` in `RAX` transferuntur.

## MITTE / WriteFile

Claude stratum commune `WriteFile` possidet, sed contractus fasciculorum hunc exitum exspectat:

```text
WriteFile(
    descriptor,
    buffer,
    numerus,
    &scripta,
    NULL
)
```

Eadem dispositio XLVIII octetorum ad `ReadFile` adhiberi potest. `MITTE` numerum octetorum scriptum reddere debet, vel `-1` in errore, quantum semantica Linux hodierna permittit.

## CLAUDE

```text
CloseHandle(descriptor)
```

`CloseHandle` BOOL reddit. Ad conventionem Unix/VINDEX servandam:

```text
successus -> 0
error     -> -1
```

Call-sites hodierni plerumque valorem negligunt, sed contractus explicitus regressiones futuras simpliciores facit.

## APERI_ADICERE

Haec primitiva extra primam partitionem manet. Semantica ELF hodierna `O_WRONLY|O_CREAT|O_APPEND` est; Win64 probabiliter `OPEN_ALWAYS` cum positione ad finem fasciculi requiret. Non debet tacite ad `APERI_SCRIBERE` reduci, quia truncatio semantica falsa esset.

## Contextus compilationis

Post stratum commune Claudii, contextus explicitus saltem targetum ELF/PE et accessum ad sedes IAT nominatas praebere debet. Primitivae fasciculorum non debent numeris absolutis vel offsetibus `.idata` propriis niti.

## Probationes destinatae

Post integrationem API:

1. PE minimum: `ExitProcess`, `VirtualAlloc` structuraliter recta;
2. PE lectio: IAT continet `CreateFileA`, `ReadFile`, `CloseHandle`;
3. PE scriptura: IAT continet `CreateFileA`, `WriteFile`, `CloseHandle`;
4. omnes vocationes `FF 15 disp32` ad sedes IAT reales ducunt;
5. modus ELF et XXV probationes canonicae immutatae manent;
6. auto-hospitium ELF punctum fixum servat;
7. executio realis sub Windows ante declarationem backend PE perfecti requiritur.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
