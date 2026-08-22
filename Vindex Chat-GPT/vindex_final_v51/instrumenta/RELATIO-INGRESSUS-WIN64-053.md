# VINDEX 0.53 — Relatio ingressus Win64

## Propositum

Haec relatio defectum executionis PE minimum distinguit a defectibus structuralibus `.idata`/IAT et a Wine. Probatio facta est sine mutatione rami implementationis PE Claudii: instrumentum in PR #9 fontem temporarium tantum mutat.

## Fundamentum probatum

Caput PR #8 ad initium experimenti erat:

```text
f054fe2da8d72ddec177341d25b7e882b6fa14d5
```

PE minimum structuram rectam habebat:

- `MZ` et `PE\0\0` recta;
- PE32+ AMD64;
- sectiones `.text` et `.idata` praesentes;
- Import Directory et IAT congruentes;
- `KERNEL32.dll!ExitProcess` et `KERNEL32.dll!VirtualAlloc` inventa;
- vocationes RIP-relativae `FF 15 disp32` ad sedes IAT reales ducebant.

## Executio pristina sub Windows vero

Idem PE minimum in GitHub Actions `windows-latest`, Microsoft Windows Server 2025, exsecutum est.

Exspectatum:

```text
42
```

Receptum:

```text
-1073741819
0xC0000005
STATUS_ACCESS_VIOLATION
```

Ita defectus non est solum vitium machinae SEH Wine: programma etiam sub Windows vero cadebat.

## Causa

Wrapper ingressus PE adhuc conventionem ingressus processus Linux adhibebat ante ramum PE:

```text
POP RAX
MOV RSI,RSP
MOV RDI,RAX
```

In ELF haec ratio `argc` et `argv` ex pila initiali Linux colligit. In PE/Win64 autem punctum ingressus processui talem pilam Linux non accipit.

Consequentiae:

1. `POP` aufert valorem e pila quem wrapper PE pro `argc` falso habet;
2. status pilae ante vocationes Win64 mutatur;
3. deinde `sub rsp,0x28` fit super pilam iam mutatam;
4. ABI Win64 et shadow space non iam ex fundamento certo servantur;
5. accessus violatio in executione reali oritur.

## Experimentum correctivum

Instrumentum `proba_ingressum_win64_053.py` fontem temporarium ita mutat:

- ramus PE nullum `POP` Linux facit;
- `sub rsp,0x28` directe ab ingressu Win64 fit;
- `RDI=0` et `RSI=0` ponuntur ad vocationem internam `PRINCIPALIS`, donec argumenta Win32 proprie introducantur;
- `VirtualAlloc` et `ExitProcess` per IAT manent;
- ramus ELF solus pristinam extractionem `argc/argv` retinet.

Compilator diagnosticus inde reconstructus est.

## Resultata

Workflow:

```text
VINDEX 0.53 — Experimentum ingressus Win64
run 32574788513
```

Resultata:

```text
Compilatorem diagnosticum construe   RECTE
Modum ELF servatum proba              RECTE (exitus 42)
PE correctum para                      RECTE
Structuram PE/IAT verifica             RECTE
PE correctum sub Windows vero          RECTE (exitus 42)
```

Uterque job, `construe` et `windows`, feliciter transiit.

## Conclusio

Causa defectus minimum PE confirmata est: **wrapper ingressus PE conventionem pilae initialis Linux ante ramum Win64 perperam adhibebat.** Correctio quae extractionem Linux ad ramum ELF tantum restringit accessum violationis tollit et minimum VINDEX sub Windows vero exitum `42` reddit.

Hoc experimentum non substituit implementationem finalem argumentorum processus Windows. `argc/argv` PE postea ex `GetCommandLineW`/`CommandLineToArgvW` vel alia strategia definita constitui poterunt. Interim `0,0` contractum minimum stabilit.

## Impetus sequens

1. correctio ingressus in PR #8 incorporanda est;
2. target ELF/PE et sedes IAT in contextu compilationis explicito ponendae sunt;
3. `GetStdHandle`/`WriteFile` ad `PROCLAMA`/`MITTE`;
4. `CreateFileA`/`ReadFile`/`CloseHandle` ad primitivas fasciculorum;
5. probationes PE reales sub Windows permanent.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
