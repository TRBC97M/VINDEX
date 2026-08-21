# VINDEX 0.51.0 — Bibliotheca duplex

VINDEX est lingua programmationis humilis, vocabulario Latino et forma
COBOL simili ornata. Fontes directe in exsecutabilia ELF x86-64 Linux
convertit, sine NASM, GCC vel libc.

Compilator hodiernus ipse VINDEX scriptus est atque se ipsum byte pro byte
reproducit. Sigillum puncti fixi SHA-256 est:

```text
153b57c82e32da4fb81ccf5de1dc0d3319418de5b7c02a5087fc8ba80ddb5f4e
```

## VINDEX Systema

VINDEX nunc nucleum x86-64 graphicum sine systemate hospite experimentalem
continet. Duae viae initii adsunt: BIOS/VGA ad machinas veteres et QEMU,
atque UEFI/GOP ad computatra recentia sine CSM. Utraque idem ELF a compilatore
VINDEX genitum exsequitur. Nucleus ambitum **VINDEX Fenestrale XCV** cum mensa
operaria, fascia operum, menu `INITIUM`, imaginibus, fenestris mobilibus et
cursore pingit. In via UEFI, pons firmware tenuis framebuffer, claviaturam et
murem vel tabulam tactus praebet; mensa, fenestrae, Scriptor II et Serpens ipsa
VINDEX manent. Tabula logica 320×200 in memoriam occultam pingitur, deinde
integra ad framebuffer linearem monitoris transfertur; margines nigri et
constructionis intermediae scintillatio sic tolluntur. Post initium nullus
actus graphicae firmware ad imagines praesentandas adhibetur.

Forma litterarum UEFI ex fonte IBM/VGA 8×8 publici dominii venit. Bullae muris
UEFI breviter stabiliuntur, ne tabulae tactiles menu `INITIUM` crebro aperiant
atque claudant.

In Fedora QEMU institue atque Systema incipe:

```bash
sudo dnf install qemu-system-x86-core
./vindex-systema
```

Imago BIOS `systema_vindex.img` et imago UEFI `systema_vindex_uefi.img` iam
paratae sunt. Ex fontibus byte pro byte restitui possunt:

```bash
make systema
```

Ad computatrum UEFI verum, `systema_vindex_uefi.img` in clavem USB vacuam
restitue, Secure Boot inhibe et clavem UEFI elige. Imago est discus GPT cum
partitione FAT32 ESP, partitione VINDEX separata et via normali
`/EFI/BOOT/BOOTX64.EFI`; CSM non requirit. Ad institutionem novam imago 0.51
integre restituenda est. Restitutio imaginis clavem destinatam totam delet.
Si clavis iam VINDEX 0.50 vel prior et documenta servata continet, solum fasciculum
`/EFI/BOOT/BOOTX64.EFI` substitue: partitio VINDEX et omnia documenta manent.
Volumen secundae vel tertiae formae ad quartam formam primo initio automatice
migratur. Programmata vetera in propriam partem transferuntur; `SALVE.VXNAT`
et `TABULA.VXNAT`, si desunt et locus vacat, automatice instituuntur.

`systema/nucleus.vindex` est logica nuclei et pictoris VINDEX.
`systema/boot.S` est parvus sector BIOS necessarius antequam ullum programma
x86-64 exsequi possit. `systema/uefi/firmamentum_uefi.c` est pons firmware
UEFI tenuis. Linux, libc, GTK et Python intra Systema non adsunt.
Haec versio volumen VINDEX permanens cum sex documentis et sex programmatis
separatis praebet. `FASCICULI`
documenta eligit, creat, nominat, renominat, delet atque in `SCRIPTOR` aperit.
Nomina usque ad octo litteras vel numeros accipiunt et suffixum `.TXT`
automatice accipiunt. `SCRIPTOR` documentum activum bullis `SERVA` et `APERI`
in volumine interno 32 KiB scribit atque legit. Scriptor II cursoris motum per
sagittas et murem, paginas verticales et documenta usque ad 4095 octeta
praebet. Nomen documenti activi in fenestra ostenditur et deletio ante actum
confirmationem petit.
`PROGRAMMATA` sex fasciculos `.VXNAT`, a documentis omnino separatos, creat,
nominat, in Scriptore II mutat, delet atque bulla `AGE` directe in nucleo
VINDEX exsequitur. Primo initio exempla `SALVE.VXNAT` et `TABULA.VXNAT`
adsunt. Exemplar novum `TABULA.VXNAT` mandata `PROGRAMMA`, `SCRIBE`, `COLOR`, `LOCUS`,
`RECTANGULUM`, `MARGO` et `FINIS` demonstrat. Programmata nunc textum
positionatum, areas coloratas et margines intra propriam fenestram pingunt.
Linux neque processus hospes huic exsecutioni intervenit. Vitium 0.49 quo
lineae `SCRIBE` ex memoria falsa legebantur correctum est; programmata 0.49
iam servata sine conversione recte agunt.
Pons UEFI partitionem binalem signo `VINDEXV0` invenit et volumen opacum per
Block I/O persistit; via FAT `VINDEX.FS` subsidium tantum manet. Post quamque
scripturam pons medium expurgat, 32 KiB relegit et signum octetorum comparat.
`SERVATUM` igitur non apparet nisi lectio comprobatoria exacte congruit.
Signum `VINDEXFS`, directorium duodecim ingressuum, nomina, longitudines et contenta
a nucleo VINDEX ordinantur. Documenta post initium novum computatri manent. Via BIOS editor
per sessionem operatur, sed persistentia disci adhuc viae UEFI propria est.

## Officina graphica

Fasciculo ZIP extracto, Officinam statim incipe:

```bash
./vindex-officina
```

**VINDEX Officina** est vera applicatio graphica declarativa. Structura eius in
`formae/officina.forma` describitur: fenestra, dispositiones, tituli, bullae,
editor, tabula exitus et reactiones. Logica ipsa VINDEX est: eventa accipit,
fontem compilat, ELF exsequitur et responsa reddit. `vindex_graphica` est pons
GTK generalis; neque structuram Officinae neque verba eius in C continet.
HTML, navigatrum, minister localis, terminale et Python in tempore executionis
omnino absunt. Fasciculi `.stilus` ad GTK pertinent, non ad interrete.

Fons iam exsistens aperiri potest:

```bash
./vindex-officina via/ad/programma.vindex
```

In Fedora Officinam sine `sudo` in indice applicationum installa:

```bash
./installa_officinam.sh
```

Index applicationum fenestram directe aperit. Imago, genus `.vindex` et
mandata `vindex-officina`/`vindexc` usori praesenti instituuntur. Versio prior
in renovatione servatur.

## Altera applicatio: Salutatio

Eadem Graphica applicationem omnino aliam pingit:

```bash
./vindex-salutatio
```

`VINDEX Salutatio` campum textus et bullam ex `salutatio.forma` creat. Nomen
ad processum VINDEX mittitur; `salutatio_vindex` responsum componit et forma
illud in fenestra ostendit. Hoc demonstrat pontem GTK Officinae non esse
alligatum.

## Linea mandatorum

```bash
./vindexc programma.vindex programma
./programma
```

Forma `-o` quoque accipitur:

```bash
./vindexc programma.vindex -o programma
```

`vindexc` fontem verificat, in archivum temporarium compilat, naturam ELF
probat atque exitum atomice publicat. Compilatio defecta exsecutabile
imperfectum non relinquit.

Verificatio separata:

```bash
./vindexc --verifica programma.vindex
```

## Exemplum minimum

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    PROCLAMA "Salve, mundus!".
    REDDE 0.
FIN-FUNCTIO.
```

## Probationes

```bash
./tests/run_tests.sh
# aut
make probatio
```

Inspectiones automaticae numeros, iterationes, functiones,
fluitantia, importationes, formas, acus, memoriam, recursionem, `argc`/`argv`,
diagnostica, auto-hospitium, duas applicationes VINDEX, pontem GTK declarativum
et installationem Fedora probant. Sector BIOS, PE32+ UEFI, GPT, FAT32, modus
VGA, GOP, forma litterarum, ELF nuclei, rectores PS/2, eventa firmware,
fenestrae, Scriptorem, Programmatum gestorem, exsecutionem `.VXNAT`, Serpentem
et reconstructiones identicas etiam probant;
probatio QEMU automatica perficitur si QEMU adest.

## Reconstructio integra

Compilator sine fiducia binario tradito restitui potest:

```bash
./bootstrap/reconstruit.sh
```

Catena integra:

```text
fontes Python → compilator amorsae → compilator VINDEX → punctum fixum
```

Python ad amorsam historicam et probationes tantum pertinet; Officina eo non
utitur. Exitus reconstructus cum binario distributo comparatur. Explicatio in
`bootstrap/AMORSA.md` invenitur.

## Ordinatio

- `src/compilator_vindex.vindex` — fons compilatoris auto-hospitis;
- `src/officina_vindex.vindex` — fons Officinae VINDEX;
- `src/salutatio_vindex.vindex` — altera applicatio Graphica VINDEX;
- `systema/nucleus.vindex` — nucleus VINDEX sine systemate hospite;
- `systema/boot.S` — sector BIOS et transitus ad modum x86-64;
- `systema/uefi/` — pons, forma litterarum et constructor imaginis UEFI;
- `systema_vindex.img` — imago BIOS statim initiabilis;
- `systema_vindex_uefi.img` — imago GPT UEFI cum ESP et volumine VINDEX;
- `BOOTX64.EFI` — applicatio UEFI removibilis;
- `nucleus_systema.elf` — ELF VINDEX a BIOS oneratum;
- `fenestrale_systema.bin` — inscriptiones Latinae ambitus Fenestralis;
- `rectores_systema.bin` — rectores PS/2 claviaturae et muris;
- `bibliotheca/graphica.vindex` — eventa bibliothecae graphicae Latina;
- `formae/` — formae declarativae et stili GTK applicationum;
- `runtime/vindex_graphica_gtk.c` — motor declarativus ad GTK systematis;
- `compilator_vindex` — compilator nativus paratus;
- `officina_vindex` — initiator VINDEX nativus;
- `salutatio_vindex` — programma Salutationis nativum;
- `vindex_graphica` — pons graphicus paratus;
- `vindexc` — interfacies publica compilationis;
- `vindex-officina` — initiator portabilis Officinae;
- `vindex-salutatio` — initiator portabilis Salutationis;
- `vindex-systema` — initiator QEMU Systematis;
- `installa_officinam.sh` — installatio usoris Fedora/Linux;
- `officina/` — imago et usus Officinae;
- `instrumenta/vindex_verifica.py` — diagnostica provecta facultativa;
- `tests/` — probationes regressionis;
- `examples/` — programmata maiora;
- `bootstrap/` — reconstructio ab Python;
- `testimonia/` — generationes nativae identicae;
- `archive/` — historia pristina;
- `REFERENTIA.md` — grammatica et facultates linguae;
- `COMMENTARIUM.md` — mutationes versionum.

## Integritas

Compilator fontes absentes, nimis magnos aut invalidos reicit. Importationes,
`FUNCTIO PRINCIPALIS`, functiones vocatas et scripturam exitus inspicit.
Officina fontem usque ad 1048576 octeta continet et
programmatum statum post executionem ostendit.

## Nomen

In iure Romano *vindex* erat qui alium defendebat vel libertati eius
interveniebat. Ideo nomen linguae libertatem, tutelam atque dominium proprii
instrumenti significat.
