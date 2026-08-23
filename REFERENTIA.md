# Referentia linguae VINDEX 0.53

Haec referentia nucleum linguae VINDEX describit. VINDEX fontes directe in exsecutabilia nativa x86-64 convertit: ELF Linux est modus praedefinitus, PE32+ AMD64 Windows tertio argumento `pe` eligi potest. Compilator ipse VINDEX scriptus est et punctum fixum stabile possidet.

## Compilatio

ELF Linux:

```bash
./compilator_vindex programma.vindex programma
chmod +x programma
./programma
```

PE32+ AMD64 Windows:

```bash
./compilator_vindex programma.vindex programma.exe pe
```

Proiectum:

```bash
./compilator_vindex PROIECTUM via/ad/proiectum.vindex
```

Forma canonica manifesti est:

```vindex
PROIECTUM VINDEX.
FONS "principalis.vindex".
PRODUCTUM "programma".
DESTINATIO ELF.
FIN-PROIECTUM.
```

`FONS` unitatem principalem, `PRODUCTUM` fasciculum generandum, `DESTINATIO` autem `ELF` aut `PE` eligit. Ordo sententiarum canonicus est. Viae relativae fontis, producti et importationum ex directorio manifesti resolvuntur, non ex directorio unde compilator vocatur. Modus directus prior integer manet.

Compilatio ordinaria GCC, NASM, libc, Python aut alium compilatorem non requirit.

## Structura programmatis

Omne programma functionem `PRINCIPALIS` habere debet:

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    PROCLAMA "Salve, mundus!".
    REDDE 0.
FIN-FUNCTIO.
```

Quodque praeceptum puncto terminatur. Bloci verbo suo aperiuntur et forma `FIN-...` congruente clauduntur.

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
- Usque ad septem parametra probata sunt; in ABI System V I–VI registris, VII pilae traditur.
- Vocatio functionis posterius definitae et recursio sustinentur.
- `VACUUM` reditum sine valore significativo indicat.

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
DECLARA numeri SICUT ORDO DE NUMERUS CAPACITAS 10.
DECLARA textus SICUT ORDO DE LITTERA CAPACITAS 20.
```

Elementa per `numeri[index]` leguntur et scribuntur. Capacitas ordinis in tempore compilationis nota esse debet.

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

Campus forma `campus DE variabile` acceditur. Formae ordines internos continere possunt et ordines formas continere possunt.

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
- `OCTETUS_AB(sedes)` unum octetum legit.
- `SCRIBE_OCTETUM_AB(sedes, valor)` unum octetum scribit.

## Numeri fluitantes

`FLUITANS` est numerus IEEE-754 64 bituum. Operationes `+`, `-`, `*`, `/` et comparationes `<`, `>`, `<=`, `>=`, `==`, `!=` sustinentur.

```vindex
DECLARA x SICUT FLUITANS VALENS 3.14.
DECLARA y SICUT FLUITANS VALENS 1.5.
DECLARA z SICUT FLUITANS VALENS x + y.
PROCLAMA z.
```

`PROCLAMA` fluitans sex cifras post punctum exhibet. Fluitantia in functionibus, formis et ordinibus adhiberi possunt.

## Fontes multiplices

```vindex
IMPORTA "bibliotheca.vindex".
```

`IMPORTA` tantum in gradu supremo poni potest. In compilatione directa via importationis a directorio praesenti resolvitur; in compilatione proiecti a directorio manifesti. Receptacula fontium dynamice crescunt; limes historicus summae fontium remotus est. Cyclus et importatio inclusa reiciuntur.

## Argumenta lineae mandatorum

Sub ELF, `PRINCIPALIS` potest `argc` et `argv` accipere:

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

In modo PE/Win64 linea mandatorum Windows in `argc` et `argv` convertitur. Spatia intra signa duplicia ad idem argumentum pertinent. Haec prima forma octetis paginae codicis Windows nititur; viae extra paginam activam nondum canonicae sunt.

## Lectio et scriptura

- `PROCLAMA valor.` valorem cum transitu lineae exhibet.
- `LEGE(descriptor, maximum)` ex descriptore legit.
- `OCTETUS(index)` octetum novissime lectum reddit.
- `MITTE(descriptor, ordo, longitudo)` octeta mittit.
- `APERI_LEGERE(via)` archivum ad legendum aperit.
- `APERI_SCRIBERE(via)` archivum ad scribendum aperit.
- `CLAUDE(descriptor)` descriptorem claudit.

Sub PE/Win64 `APERI_LEGERE`, `APERI_SCRIBERE`, `LEGE`, `MITTE` et `CLAUDE` per `CreateFileA`, `ReadFile`, `WriteFile` et `CloseHandle` probata sunt. `MITTE(1, ordo, longitudo)` descriptorium unum ad verum manubrium exitus ordinarii Windows convertit.

## Diagnostica fontis

Errores syntactici et semantici canonici structuram stabilem exhibent: `FONS`, `LINEA`, `COLUMNA` et `NUNTIUS`. Lineae et columnae ab uno numerantur; columna locum octeti in linea significat. Diagnostica vocationum ignotarum etiam ad fontem importatum verum referuntur, non ad unitatem post importationes conflatam.

Manifestum proiecti invalidum eadem structura reicitur atque locum vitii in ipso manifesto indicat.

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

`DESINE.` iterationem finit.

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

`RESERVA(typus)` memoriam pro uno valore generis dati petit. `RESERVA_OCTETA(quantitas)` numerum exactum octetorum petit; verificatores canonici ea forma utuntur. `LIBERA(acus)` memoriam reddit. Backend PE acervum per `VirtualAlloc` praeparat. Nulla collectio purgamentorum adest.

## Diagnostica

Compilator fontes absentes, importationes vitiosas, `PRINCIPALIS` absentem, instructiones ignotas et functiones vocatas non inventas reicit. Exsecutabile imperfectum non debet pro producto valido relinqui.

## Limites canonici 0.53

- architecturae probatae: ELF x86-64 Linux et PE32+ AMD64 Windows;
- codex machinalis, fontes et metadatae principales dynamice crescunt;
- longitudo identificatoris: 32 litterae;
- parametra functionis probata: 7;
- argumenta lineae mandatorum PE spatia intra signa duplicia servant;
- nulla collectio purgamentorum;
- nulla dependentia libc ad compilationem ordinariam.

## Auto-hospitium

`src/compilator_vindex.vindex` est fons canonicus compilatoris. Binarium `compilator_vindex` se ipsum ad punctum fixum byte pro byte reproducit. Sigillum distributum in `SIGILLA_SHA256.txt` servatur.

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

**VINDEX Latine cogitat.**
