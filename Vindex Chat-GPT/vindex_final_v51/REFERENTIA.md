# Referentia linguae VINDEX

Haec referentia facultates **canonicas et re vera probatas** describit. Fines futuros vide in `ARCHITECTURA.md` et `CONSILIUM.md`.

VINDEX est lingua generalis in constructione. Compilator canonicus ipse VINDEX scriptus est, ELF64 x86-64, PE32+ Win64 et PE32+ UEFI generat atque punctum fixum auto-hospitii servat.

---

# I. Structura programmatis

Programma ordinarium functionem `PRINCIPALIS` habet:

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    PROCLAMA "Salve, mundus!".
    REDDE 0.
FIN-FUNCTIO.
```

Praecepta puncto terminantur. Bloci verbis propriis aperiuntur et `FIN-...` congruente clauduntur.

Commentaria `//` usque ad finem lineae etiam intra corpora functionum sustinentur.

---

# II. Compilatio

## ELF64 x86-64

```bash
./compilator_vindex programma.vindex programma
chmod +x programa
./programma
```

Forma publica commendata:

```bash
./vindexc programa.vindex -o programa
```

`vindexc` fontem verificat, in archivum temporarium compilat, ELF validum confirmat et productum atomice publicat.

## PE32+ Win64

```bash
./compilator_vindex programa.vindex programa.exe pe
```

Backend Win64 in CI sub Windows vero probatur, non solum per inspectionem structuram PE.

## PE32+ UEFI

```bash
./compilator_vindex programa.vindex programa.efi uefi
```

Target `uefi` per PR #109 canonicus est. Generat PE32+ subsystem EFI application sine importationibus Win32. Vocationes firmware UEFI et `SALI_AD(expressio)` ad opera basimi gradus praebentur.

Custodia dedicata non solum structuram EFI inspicit. Imaginem FAT construit et sub QEMU/OVMF probat catenam:

```text
OVMF → BOOTX64.EFI [VINDEX] → NUCLEUS [VINDEX] → FRAMEBUFFER → SYLVIA
```

Vetus ponticulus C non est pars huius contractus.

---

# III. Functiones

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
- Vocatio functionis posterius definitae sustinetur.
- Recursio sustinetur.
- `VACUUM` reditum sine valore significativo indicat.
- `TEXTUS` typus reditus canonice probatus est: functio litteralem, parametrum aut concatenationem dynamicam redire potest, et valor a vocante ut `TEXTUS` plene adhibetur.
- Probatio canonica R1 **septem argumenta SysV** exercet.

Exemplum reditus textus:

```vindex
FUNCTIO SALUTATIO REDDENS TEXTUS.
    REDDE "Salve".
FIN-FUNCTIO.
```

Win64 proprium ABI adhibet; eius correctiones per probationes Windows R4 muniuntur.

---

# IV. Typi canonici

| Typus | Natura |
| --- | --- |
| `NUMERUS` | integer signatus 64 bituum |
| `LITTERA` | littera / octetum in locis humilibus |
| `VERITAS` | valor logicus 0 aut 1 |
| `FLUITANS` | IEEE-754 duplicis praecisionis |
| `TEXTUS` | descriptor textus dynamici UTF-8 |
| `ACUS<T>` | acus ad genus `T` |
| `ORDO DE T CAPACITAS n` | ordo capacitate statica |
| `FORMA` / nomen formae | aggregatum camporum |
| `VACUUM` | reditus sine valore significativo |

---

# V. Variabilia et assignatio

```vindex
DECLARA x SICUT NUMERUS VALENS 42.
DECLARA y SICUT FLUITANS VALENS 3.5.
DECLARA nomen SICUT TEXTUS VALENS "Sylvia".
```

Assignatio:

```vindex
x = x + 1.
nomen = "VINDEX".
```

Frames functionum dynamice dimensionantur; probatio R1 frame plus quam unam paginam et centena localia exercet.

---

# VI. Ordines

```vindex
DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 10.
DECLARA litterae SICUT ORDO DE LITTERA CAPACITAS 64.
```

Accessus:

```vindex
tabula[3] = 99.
PROCLAMA tabula[3].
```

Capacitas ordinis statici tempore compilationis nota est.

`ORDO DE LITTERA` manet utilissimum ubi collocatio exacta et buffer fixus desiderantur; `TEXTUS` ad textum dynamicum commodior est.

---

# VII. Formae

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

Campus forma:

```vindex
campus DE variabile
```

Formae ordines internos et ordines formarum continere possunt. Acus ad formas quoque sustinentur.

---

# VIII. Acus et memoria directa

```vindex
DECLARA x SICUT NUMERUS VALENS 10.
DECLARA p SICUT ACUS<NUMERUS> VALENS SEDES(x).
CONTENTUM(p) = 99.
```

- `SEDES(valor)` sedem memoriae reddit.
- `CONTENTUM(acus)` valorem indicatum legit vel scribit.
- `p + 1` magnitudine generis indicati movetur.
- `p[index]` eadem scala utitur.
- `ACUS<Forma>` cum campis formae adhiberi potest.
- `OCTETUS_AB(sedes)` unum octetum legit.
- `SCRIBE_OCTETUM_AB(sedes, valor)` unum octetum scribit.

Memoria manualis:

```vindex
DECLARA p SICUT ACUS<NUMERUS> VALENS RESERVA(NUMERUS).
CONTENTUM(p) = 42.
LIBERA(p).
```

Acus invalida aut accessus extra memoriam mores indefinitos efficere potest. VINDEX hodiernus libertatem basimi gradus servat; systema memoriae tutius futurum hoc contractum humilem abolere non debet.

---

# IX. TEXTUS

`TEXTUS` est genus nativum textus dynamici. Repraesentatio canonica primae implementationis descriptor est:

```text
+0   longitudo octetorum : u64
+8   capacitas           : u64
+16  octeta UTF-8 ...
```

Exemplum:

```vindex
IMPORTA "bibliotheca/textus.vindex".

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA nomen SICUT TEXTUS VALENS "Sylvia".
    DECLARA titulus SICUT TEXTUS VALENS nomen + " OS".
    PROCLAMA titulus.
    PROCLAMA LONGITUDO(titulus).
    REDDE 0.
FIN-FUNCTIO.
```

Facultates probatae:

- litteralia textus;
- assignatio `TEXTUS`;
- concatenatio per `+`;
- comparatio contenti per `==` et `!=`;
- parametrum functionis;
- reditus `TEXTUS` a functionibus, etiam pro concatenatione dynamica;
- `PROCLAMA`;
- `LONGITUDO(textus)` — numerus octetorum UTF-8;
- `UTF8_VALIDUS(textus)` — validatio UTF-8 stricta;
- `LONGITUDO_SCALARUM(textus)` — numerus scalarum Unicode;
- `UTF8_SCALARE_CAPE(textus, index)` — valor scalaris Unicode;
- `SUBTEXTUS_SCALARUM(textus, initium, numerus)` — nova copia textus per limites scalarum Unicode.

`LONGITUDO` octeta UTF-8 numerat, non scalaria Unicode. Haec semantica humilis gradus deliberate servatur.

`SUBTEXTUS_SCALARUM` sequentiam UTF-8 numquam in medio incidit. Subtextum vacuum legitimum descriptor non-nullus longitudine zero est; input invalidum vel UTF-8 invalidum `TEXTUS` nullum reddit.

Scalae Unicode non idem sunt ac graphemata visibilia. Segmentatio graphematum, normalizatio NFC/NFD, proprietates Unicode et case folding adhuc futura sunt.

---

# X. Fluitantia

`FLUITANS` est IEEE-754 64 bituum.

```vindex
DECLARA x SICUT FLUITANS VALENS 3.14.
DECLARA y SICUT FLUITANS VALENS -1.25.
DECLARA z SICUT FLUITANS VALENS x + y.
PROCLAMA z.
```

Operationes probatae includunt arithmeticam et comparationes ordinarias. Valores negativi R1 quoque probantur.

---

# XI. Imperium fluxus

## Condicio

```vindex
SI x > 10 TUNC
    PROCLAMA x.
ALITER
    PROCLAMA 0.
FIN-SI.
```

## DUM

```vindex
DUM x < 10 PERFICE
    x = x + 1.
FIN-DUM.
```

## PER

```vindex
PER i AB 1 AD 10 PERFICE
    PROCLAMA i.
FIN-PER.
```

- `DESINE.` iterationem finit.
- `PERGE.` ad iterationem sequentem transit.

---

# XII. Operatores

## Arithmetici

```text
+  -  *  /  %
```

## Comparativi

```text
==  !=  <  >  <=  >=
```

## Logici

```text
!  &&  ||
```

`&&` et `||` **aestimationem brevem** habent.

```vindex
SI p != 0 && CONTENTUM(p) == 42 TUNC
    PROCLAMA 1.
FIN-SI.
```

Si `p == 0`, `CONTENTUM(p)` non aestimatur.

Prioritas logica canonica:

```text
comparatio → && → ||
```

## Bituales

```text
&  |  ^  <<  >>
```

`&` et `|` ab operatoribus logicis separati sunt et utramque partem ut valores bituales tractant.

---

# XIII. Importationes

```vindex
IMPORTA "bibliotheca/textus.vindex".
```

`IMPORTA` in gradu supremo ponitur. Viae fontium per systema projectuum et contextum compilationis resolvuntur.

Compilator hodiernus buffers fontium, functionum et codicis dynamice administrat. **Vetus limes publicus 212999 octetorum non amplius contractus canonicus est.** Probationes R1 multas functiones, frames magnas et codicem multo maiorem quam veteres casus ordinarios exercent.

Importationes invalidas compilator cum diagnosticis structis reicit.

---

# XIV. Argumenta lineae mandatorum

`PRINCIPALIS` potest argumenta processūs accipere:

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    ACCIPIT argc SICUT NUMERUS.
    ACCIPIT argv SICUT ACUS<NUMERUS>.
    PROCLAMA argc.
    REDDE 0.
FIN-FUNCTIO.
```

ELF et Win64 utrumque contractum argumentorum probationibus dedicatis muniuntur.

---

# XV. I/O et fasciculi

Praecepta / intrinseca probata includunt:

- `PROCLAMA valor.`;
- `SCRIBE ordo CAPACITAS n.`;
- `LEGE(descriptor, maximum)`;
- `OCTETUS(index)`;
- `MITTE(descriptor, ordo, longitudo)`;
- `APERI_LEGERE(via)`;
- `APERI_SCRIBERE(via)`;
- `APERI_ADICERE(via)`;
- `CLAUDE(descriptor)`.

Instrumenta processūs includunt, secundum target et ambitum:

- `EXSEQUERE(via)`;
- `EXSEQUERE_CAPTURA(...)`;
- `CURRE(...)`;
- `CAMBIA(via)`;
- `TUBUS(...)`.

---

# XVI. PROIECTUM

Projectum VINDEX potest manifesto describi. Contractus R3 vias relativas et destinationes ELF/PE probat.

Exempla canonica sunt sub:

```text
tests/proiecta/
```

Officina canonica eodem contractu projectuum utitur.

---

# XVII. Diagnostica

Compilator canonicus diagnostica structa generat:

```text
DIAGNOSTICUM VINDEX
FONS
<via>
LINEA
<numerus>
COLUMNA
<numerus>
NUNTIUS
<descriptio>
```

Origines importationum et errores compilationis probationibus R2 muniuntur. Officina haec diagnostica legit et ad fontem navigare potest.

---

# XVIII. Auto-hospitium

Fons compilatoris:

```text
src/compilator_vindex.vindex
```

Probatio:

```bash
make auto-hospitium
```

Contractus canonicus postulat:

```text
compilator versionatus = G2 = G3
```

Mutationes linguae non canonizentur si punctum fixum frangunt.

---

# XIX. Probationes

```bash
make probatio
```

Suite localis canonica post PR #108 **viginti novem probationes** exercet sine errore, inter quas:

- arithmeticam;
- fluitantia;
- importationes;
- formas et acus;
- recursionem;
- argumenta;
- diagnostica;
- collectiones, series et segmenta `NUMERUS`;
- `TEXTUS` UTF-8 et scalaria Unicode;
- reditum `TEXTUS` a functionibus;
- subtextum Unicode per scalaria;
- auto-hospitium;
- logicam brevem;
- PE32+;
- puritatem absolutam Sylviae;
- Fenestrale II Purus.

Workflow separati Win64 et Officina sub Windows vero probant. Workflow UEFI dedicatus QEMU/OVMF exsequitur, imaginem FAT inspicit et screendump Sylviae verificat.

---

# XX. Officina

Officina canonica hodierna in radice repositorii sub `officina/` est applicatio Windows nativa. Non est pons GTK historicus.

Ea projecta VINDEX aperit, fontes editat, syntaxin colorat, build/run exercet et diagnostica navigabilia exhibet.

Syntax linguae non dependet ab Officina; compilator lineae mandatorum auctoritas manet.

---

# XXI. Sylvia OS et lingua

Sylvia VINDEX adhibet sed non definit. Catena canonica Sylviae, **etiam initium UEFI**, VINDEX pura est.

Facultates Fenestralis, UEFI aut gubernatorum quae generaliter utiles sunt, ubi possibile est in linguam, ABI aut bibliothecam VINDEX generalem evolvantur potius quam exceptiones privatae fiant.

---

# XXII. Limites praesentis linguae

VINDEX nondum habet plenitudinem destinatam. Inter facultates futuras nondum in hac referentia canonicas sunt:

- integri multarum dimensionum ut typi publici pleni;
- enumerationes et uniones maturae;
- generica generalia;
- functiones/callback ut valores primi ordinis plene definiti;
- closures;
- modules et compilationes separatae maturae;
- ownership vel alius modus memoriae tutior;
- exceptiones aut mechanismus errorum alti gradus finalis;
- fila, atomica et async;
- SIMD publicum maturum;
- reflection / metaprogrammatio;
- graphemata, normalizatio et transformationes Unicode superiores;
- formatio ELF multi-`PT_LOAD` maturior et relocatio acervi;
- debugger et optimizer maturi;
- package manager;
- targeta ARM64 et WebAssembly canonica.

Haec absentia non mutat legem universalitatis: sunt agenda, non limites philosophici.

---

# XXIII. Exemplum integrum

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

Exitus:

```text
720
```

---

**VINDEX Latine cogitat. Sylvia Latine loquitur.**