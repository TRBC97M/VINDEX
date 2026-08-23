# Referentia linguae VINDEX

Haec referentia facultates re vera probatas describit. VINDEX fontes directe in
exsecutabilia nativa x86-64 convertit: ELF Linux est modus praedefinitus, PE32+
AMD64 Windows tertio argumento `pe` eligi potest. Compilator ipse VINDEX
scriptus est et punctum fixum stabile possidet.

## Structura programmatis

Omne programma functionem `PRINCIPALIS` habere debet:

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    PROCLAMA "Salve, mundus!".
    REDDE 0.
FIN-FUNCTIO.
```

Quodque praeceptum puncto terminatur. Bloci verbo suo aperiuntur et forma
`FIN-...` congruente clauduntur.

## Officina, compilatio et diagnostica

Officina graphica nativa:

```bash
./vindex-officina
```

Fenestra editoris bullas `NOVUM`, `APERI`, `SERVA`, `COMPILA` et `EXSEQUERE`,
dialogos fasciculorum atque relationem compilationis et executionis praebet.
Forma `formae/officina.forma` structuram declarat. Applicatio VINDEX eventa e
`bibliotheca/graphica.vindex` tractat; pons GTK generalis formas pingit, valores
exportat et eventa transmittit. Altera applicatio `vindex-salutatio` eodem
motore utitur. HTML, navigatrum, minister localis, terminale et Python ad
executionem non requiruntur.

Linea mandatorum commendata pro ELF Linux:

```bash
./vindexc programma.vindex -o programma
./programma
```

Verificatio sine compilatione:

```bash
./vindexc --verifica programma.vindex
```

Diagnostica provecta formam `archivum:linea:columna: erratum: nuntius`
habent. Compilator nativus directe quoque vocari potest:

```bash
./compilator_vindex programma.vindex programma
chmod +x programma
```

PE32+ AMD64 Windows generatur:

```bash
./compilator_vindex programma.vindex programma.exe pe
```

Backend PE non utitur GCC, NASM aut libc. Importationes Win64 necessariae per
IAT a compilatore ipso construuntur.

## Nucleus sine systemate hospite

Fons `systema/nucleus.vindex` ab eodem `compilator_vindex` in ELF x86-64
convertitur. Quia nucleus nullum servitium Linux vocat et memoriam VGA directe
scribit, sector `systema/boot.S` eum sine systemate hospite exsequi potest.

```bash
make systema
./vindex-systema
```

In hac prima versione memoria infra primum GiB identice mappatur, ELF ad
`0x400000`, pila ad 16 MiB et allocator VINDEX ad 32 MiB ponuntur. Nucleus
minimum 64 MiB memoriae postulat; initiator QEMU 128 MiB praebet.

## Functiones

```vindex
FUNCTIO ADDE REDDENS NUMERUS.
    ACCIPIT a SICUT NUMERUS.
    ACCIPIT b SICUT NUMERUS.
    REDDE a + b.
FIN-FUNCTIO.
```

- `ACCIPIT nomen SICUT typus.` parametrum declarat.
- `REDDENS typus` typum reditus declarat.
- `REDDE expressio.` valorem reddit atque functionem finit.
- Usque ad septem parametra per functionem probata sunt; in conventione System V
  I–VI registris, VII pilae traditur.
- Vocatio functionis posterius definitae et recursio sustinentur.
- `VACUUM` reditum sine valore significativo indicat; ex consuetudine tamen
  `REDDE 0.` adhiberi potest.

## Typi

| Typus | Natura |
| --- | --- |
| `NUMERUS` | integer signatus 64 bituum |
| `LITTERA` | littera vel octetum |
| `VERITAS` | valor Booleanus, 0 aut 1 |
| `FLUITANS` | numerus IEEE-754 duplicis praecisionis |
| `ACUS<T>` | acus ad valorem generis `T` |
| `ORDO DE T CAPACITAS n` | ordo `n` elementorum |
| `FORMA` | structura camporum |
| `VACUUM` | reditus sine valore significativo |

### Variabilia et ordines

```vindex
DECLARA x SICUT NUMERUS VALENS 42.
DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 10.
DECLARA textus SICUT ORDO DE LITTERA CAPACITAS 20.
```

Elementa per `tabula[index]` leguntur et scribuntur. Hic `tabula` nomen
variabilis usoris est; tabula historica interna compilatoris VINDEX 0.53 omnino
deleta est. Capacitas ordinis in tempore compilationis nota esse debet.

### Formae

```vindex
FORMA Punctum.
    CAMPUS x SICUT NUMERUS.
    CAMPUS y SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA p SICUT Punctum.
    x DE p = 3.
    y DE p = 7.
    PROCLAMA x DE p + y DE p.
    REDDE 0.
FIN-FUNCTIO.
```

Campus forma `campus DE variabile` acceditur. Forma ordines internos et ordo
formas continere possunt.

### Acus

```vindex
DECLARA x SICUT NUMERUS VALENS 10.
DECLARA p SICUT ACUS<NUMERUS> VALENS SEDES(x).
CONTENTUM(p) = 99.
```

- `SEDES(valor)` sedem memoriae reddit.
- `CONTENTUM(acus)` valorem indicatum legit vel scribit.
- `p + 1` magnitudine generis indicati movetur.
- `p[index]` eadem scala utitur.
- `ACUS<Forma>` campum per `campus DE CONTENTUM(p)` accedere potest.
- `OCTETUS_AB(sedes)` unum octetum legit.
- `SCRIBE_OCTETUM_AB(sedes, valor)` unum octetum scribit.

## Numeri fluitantes

`FLUITANS` est numerus IEEE-754 64 bituum. Operationes `+`, `-`, `*`, `/` et
comparationes `<`, `>`, `<=`, `>=`, `==`, `!=` sustinentur.

```vindex
DECLARA x SICUT FLUITANS VALENS 3.14.
DECLARA y SICUT FLUITANS VALENS 1.5.
DECLARA z SICUT FLUITANS VALENS x + y.
PROCLAMA z.
```

`PROCLAMA` sex cifras post punctum exhibet. Fluitantia positiva et negativa sub
ELF et PE/Win64 probata sunt. Fluitantia in functionibus, formis et ordinibus
adhiberi possunt.

## Fontes multiplices

```vindex
IMPORTA "bibliotheca.vindex".
```

`IMPORTA` tantum in gradu supremo poni potest. Via importationis nunc a
directorio praesenti resolvitur. Limes historicus summae fontium `212999`
octetorum remotus est; receptacula fontium dynamice crescunt. Cyclus et
importatio inclusa reiciuntur.

## Argumenta lineae mandatorum

Sub modo ELF, `PRINCIPALIS` potest `argc` et `argv` accipere:

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    ACCIPIT argc SICUT NUMERUS.
    ACCIPIT argv SICUT ACUS<NUMERUS>.
    PROCLAMA argc.
    SI argc > 1 TUNC
        PROCLAMA OCTETUS_AB(CONTENTUM(argv + 1)).
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.
```

Ingressus PE/Win64 iam conventionem pilae Linux non adhibet. Argumenta lineae
mandatorum Windows nondum convertuntur: interim `PRINCIPALIS` in modo PE
`argc=0` et `argv=0` accipit. Haec limitatio explicita est et separata a
backend I/O Win64.

## Lectio et scriptura

- `PROCLAMA valor.` valorem cum transitu lineae exhibet; catenae, integri et
  fluitantes sub ELF et PE probati sunt.
- `SCRIBE ordo CAPACITAS n.` litteras ordinis exhibet.
- `LEGE(descriptor, maximum)` ex descriptore legit.
- `OCTETUS(index)` octetum novissime lectum reddit.
- `MITTE(descriptor, ordo, longitudo)` octeta mittit.
- `APERI_LEGERE(via)` archivum ad legendum aperit.
- `APERI_SCRIBERE(via)` archivum ad scribendum aperit.
- `APERI_ADICERE(via)` archivum adiciendum aperit.
- `CLAUDE(descriptor)` descriptorem claudit.

Sub PE/Win64 `APERI_LEGERE`, `APERI_SCRIBERE`, `LEGE`, `MITTE` et `CLAUDE`
per `CreateFileA`, `ReadFile`, `WriteFile` et `CloseHandle` probata sunt.
`APERI_ADICERE` nondum in backend Win64 canonice probatum est et pro nunc ad
ambitum ELF referendum est.

## Executio aliorum programmatum

- `EXSEQUERE(via)` programma exsequitur.
- `EXSEQUERE_CAPTURA(via, receptaculum, capacitas)` exitum capit.
- `CURRE(argumenta, ambitus, descriptor)` programma cum argumentis exsequitur.
- `CAMBIA(via)` directorium praesens mutat.
- `TUBUS(receptaculum)` tubum systematis creat.

Haec familia servitiorum systematis historice Linux innititur nisi contrarium
in backend Win64 expresse probatum est.

## Imperium fluxus

### Condicio

```vindex
SI x > 10 TUNC
    PROCLAMA x.
ALITER
    PROCLAMA 0.
FIN-SI.
```

### Iteratio conditionalis

```vindex
DUM x < 10 PERFICE
    x = x + 1.
FIN-DUM.
```

### Iteratio finita

```vindex
PER i AB 1 AD 10 PERFICE
    PROCLAMA i.
FIN-PER.
```

`DESINE.` iterationem finit; `PERGE.` ad iterationem sequentem transit.

## Operatores

- arithmetici: `+`, `-`, `*`, `/`, `%`;
- comparativi: `==`, `!=`, `<`, `>`, `<=`, `>=`;
- logici: `&&`, `||`, `!`;
- bituales: `&`, `|`, `^`, `<<`, `>>`;
- assignatio: `=`.

Praecedentia ordinaria servatur; parenthesibus mutari potest.

## Memoria

```vindex
DECLARA p SICUT ACUS<NUMERUS> VALENS RESERVA(NUMERUS).
CONTENTUM(p) = 42.
PROCLAMA CONTENTUM(p).
LIBERA(p).
```

`RESERVA(typus)` memoriam petit; `LIBERA(acus)` eam reddit. Allocator internus
simplex est. Backend PE reservat memoriam Win64 per `VirtualAlloc`; primum
acervum quoque in ingressu PE constituit. Acus invalida vel memoria extra fines
mores indefinitos efficere potest; verificator staticus haec omnia demonstrare
non potest.

## Limites generales

- architecturae probatae: ELF x86-64 Linux; PE32+ AMD64 Windows;
- limes historicus summae fontium `212999` octetorum: remotus;
- codex machinalis et receptacula metadatae: dynamice crescunt;
- longitudo identificatoris: 32 litterae;
- parametra functionis probata: 7;
- fons in Officina: 1048576 octeta;
- pons graphicus: GTK 3;
- nucleus Systematis: BIOS x86-64, imago 1 MiB, nucleus maximus 16384 octeta;
- nulla collectio purgamentorum;
- nulla bibliotheca libc.

## Exemplum integrum

```vindex
FUNCTIO FACTORIA REDDENS NUMERUS.
    ACCIPIT n SICUT NUMERUS.
    SI n <= 1 TUNC
        REDDE 1.
    FIN-SI.
    REDDE n * FACTORIA(n - 1).
FIN-FUNCTIO.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA responsum SICUT NUMERUS VALENS FACTORIA(6).
    PROCLAMA responsum.
    REDDE 0.
FIN-FUNCTIO.
```

Exitus est `720`.
