# VINDEX 0.53 — Nucleus purus

VINDEX est lingua programmationis nativa vocabulario Latino et forma syntactica COBOL simili. Compilator eius principalis **ipse VINDEX scriptus est** et se ipsum byte pro byte reproducit.

Hic ramus consulto **nucleum linguae tantum** continet. Systema, Sylvia OS, Officina, GTK, prototypa historica, bootstrap Python et instrumenta migrationis ex codice activo remota sunt. Status integer prior in ramo `archive/vindex-053-avant-purificatio` servatur.

## Compilator

Fons canonicus:

```text
src/compilator_vindex.vindex
```

Binarium seminale distributum:

```text
compilator_vindex
```

Punctum fixum SHA-256:

```text
166a0e666deb83f759f90d1b721474ede01bb3519ec5231b2fe0e9b23158c969
```

Compilator non indiget GCC, NASM, libc aut Python ad compilationem ordinariam vel ad auto-hospitium.

## Compilatio ELF Linux

```text
./compilator_vindex programma.vindex programma
chmod +x programma
./programma
```

## Compilatio PE32+ AMD64 Windows

```text
./compilator_vindex programma.vindex programma.exe pe
```

Backend Win64 iam continet `ExitProcess`, `VirtualAlloc`, `GetStdHandle`, `WriteFile`, `CreateFileA`, `ReadFile` et `CloseHandle`. `PROCLAMA`, allocationes atque operationes fundamentales fasciculorum sub Windows vero probatae sunt.

Limitatio hodierna: punctum ingressus PE nondum argumenta lineae mandatorum Windows in `argc/argv` convertit; programma PE `PRINCIPALIS` interim cum `argc=0`, `argv=0` incipit.

## Exemplum

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    PROCLAMA "Salve, mundus!".
    REDDE 0.
FIN-FUNCTIO.
```

## Structura nuclei

```text
src/compilator_vindex.vindex        fons compilatoris auto-hospitis
compilator_vindex                   binarium seminale
REFERENTIA.md                       grammatica et facultates linguae
COMPILATOR-DYNAMICUS-053.md         architectura compilatoris 0.53
PURIFICATIO-053.md                  disciplina nuclei puri
tests/casus/                        casus conformitatis VINDEX
tests/proba_pe_structuram_053.vindex verificator PE ipso VINDEX scriptus
SIGILLA_SHA256.txt                  sigillum compilatoris
VERSION                             versio
```

## Probationes

Nucleus se ipsum sine Python recompilat usque ad punctum fixum. Casus linguae et verificator PE sunt VINDEX. GitHub Actions tantum ut infrastructura externa temporaria manet: duo fasciculi YAML compilatorem VINDEX incipiunt et exitus in Linux atque Windows observant; logicam compilatoris non implent.

Status purificationis comprobatus:

```text
punctum fixum nativum       RECTE
casus semantici ELF         RECTE
CRLF                        RECTE
PE32+ / IAT per VINDEX      RECTE
executio Windows vera       RECTE
fasciculus VINX             RECTE
```

In codice fonte activo nuclei nullus Python, C, assembler, Shell aut PowerShell manet. Solum VINDEX est codex linguae; Markdown et configurationes Git non sunt implementatio linguae.

## Nomen

In iure Romano *vindex* erat qui alium defendebat vel libertati eius interveniebat. Nomen igitur libertatem, tutelam atque dominium propriorum instrumentorum significat.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
