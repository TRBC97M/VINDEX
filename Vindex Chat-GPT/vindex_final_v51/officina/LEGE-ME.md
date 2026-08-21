# VINDEX Officina graphica

Officina est applicatio graphica VINDEX cum fenestra GTK nativa et forma
declarativa. Editor,
dialogi fasciculorum, compilatio, executio et relatio programmatis in eadem
fenestra apparent. Nullam paginam HTML, navigatrum, ministrum localem,
terminale aut Python in tempore executionis requirit.

Applicatio `officina_vindex` ex fonte VINDEX compilatur. Ipsa eventa accipit,
fontem compilat et ELF exsequitur. `formae/officina.forma` totam interfaciem
describit. Pons `vindex_graphica` eandem formam generalem in GTK 3 pingit;
nullam structuram Officinae in codice C habet.

## Initium

```bash
./vindex-officina
```

Fons iam exsistens statim aperiri potest:

```bash
./vindex-officina via/ad/programma.vindex
```

## Instrumenta fenestrae

- `NOVUM` — novum fontem VINDEX crea;
- `APERI` — fontem `.vindex` per dialogum systematis aperi;
- `SERVA` — fontem per dialogum systematis serva;
- `COMPILA` — ELF iuxta fontem crea;
- `EXSEQUERE` — fontem compila et programma exsequere;
- tabula inferior relationem compilationis et exitum programmatis ostendit.

## Necessaria

- Linux x86-64;
- GTK 3 in systemate;
- compilator VINDEX inclusus.

Fedora Workstation GTK iam praebet. Capita evolutionis GTK, GCC, Python et
navigatrum ad usum Officinae non requiruntur.

## Fedora

```bash
./installa_officinam.sh
```

Installatio `sudo` non requirit. Index applicationum fenestram directe aperit
et fasciculos `.vindex` cum ea coniungit.

Installatio etiam `VINDEX Salutatio` addit, alteram applicationem eodem motore
Formarum gubernatam.
