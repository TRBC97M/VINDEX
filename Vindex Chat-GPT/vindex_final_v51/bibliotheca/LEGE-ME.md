# Bibliotheca VINDEX

`bibliotheca/` codicem VINDEX communem continet qui per `IMPORTA` adhiberi potest.

Haec bibliotheca nunc tria genera rerum continet:

1. facultates generales linguae, ut `textus.vindex`;
2. collectiones generales, ut `collectiones_numerorum.vindex` et `series_numerorum.vindex`;
3. bibliothecas Fenestralis II Purus, quae pars Sylviae canonicae hodiernae sunt.

Nonnulli fasciculi veteres, praesertim `graphica.vindex`, ad architecturam GTK historicam pertinent et non sunt fundamentum Officinae canonicae Windows hodiernae.

---

# I. TEXTUS

`textus.vindex` operationes generales generis `TEXTUS` continet.

Hodie definit:

- `LONGITUDO(textus)` — numerum octetorum UTF-8 descriptoris reddit.

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

`TEXTUS` ipse genus nativum est; bibliotheca auxilia generalia supra genus praebet.

---

# II. Collectio numerorum

`collectiones_numerorum.vindex` est prima collectio dynamica generalis bibliothecae standardis nasciturae. Nulla mutatio compilatoris requiritur: tantum facultatibus memoriae VINDEX canonicis utitur.

Importatio:

```vindex
IMPORTA "bibliotheca/collectiones_numerorum.vindex".
```

API:

- `CN_CREA()` — collectionem vacuam creat;
- `CN_NUMERUS(c)` — numerum elementorum reddit;
- `CN_ADDE(c, valor)` — valorem in fine addit;
- `CN_CAPE(c, index)` — valorem indice legit;
- `CN_PONE(c, index, valor)` — valorem indice mutat;
- `CN_DELE(c, index)` — elementum delet et memoriam nodi liberat;
- `CN_PURGA(c)` — omnia elementa delet, collectionem ipsam servans;
- `CN_LIBERA(c)` — omnia elementa et collectionem ipsam liberat.

Indices a zero incipiunt. Mutationes quae succedunt `1` reddunt; index invalidus aut collectio nulla `0` reddit. `CN_CAPE` quoque `0` pro indice invalido reddit, itaque si valor zero legitime continetur, validitas indicis per `CN_NUMERUS` separatim cognoscenda est.

Repraesentatio interna est lista simpliciter vinculata:

```text
collectio:
+0   numerus elementorum
+8   primus nodus
+16  ultimus nodus

nodus:
+0   valor NUMERUS
+8   proximus nodus
```

Prima implementatio consulto `NUMERUS` tantum tractat. Generica futura debent hanc necessitatem generalizare, non API fictam genericam ante facultatem linguae simulare.

---

# III. Series numerorum

`series_numerorum.vindex` seriem dynamicam **contiguam** praebet. Ea collectionem ligatam non substituit: contractus alius est. Series accessum indicis directum et memoriam contiguam praebet, dum collectio vinculata additiones et deletiones nodorum sine relocatione totius memoriae sustinet.

Importatio:

```vindex
IMPORTA "bibliotheca/series_numerorum.vindex".
```

API:

- `SN_CREA()` — seriem vacuam cum capacitate initiali creat;
- `SN_NUMERUS(s)` — longitudinem logicam reddit;
- `SN_CAPACITAS(s)` — capacitatem memoriae praesentem reddit;
- `SN_BASIS(s)` — basim contiguam elementorum reddit;
- `SN_RESERVA(s, capacitas)` — capacitatem minimam postulat;
- `SN_CAPE(s, index)` — elementum indice legit;
- `SN_PONE(s, index, valor)` — elementum exsistens mutat;
- `SN_ADDE(s, valor)` — elementum in fine addit;
- `SN_INSERE(s, index, valor)` — elementum inserit, posteriora movens;
- `SN_DELE(s, index)` — elementum delet, posteriora contrahens;
- `SN_PURGA(s)` — longitudinem ad zero reducit sed capacitatem retinet;
- `SN_LIBERA(s)` — basim et descriptorem liberat.

Repraesentatio:

```text
series:
+0   numerus elementorum
+8   capacitas elementorum
+16  basis memoriae contiguae

basis:
+0   elementum 0
+8   elementum 1
+16  elementum 2
...
```

Cum capacitas deficit, nova regio maior reservatur, elementa servantur et vetus regio liberatur. Ideo valor a `SN_BASIS` redditus **post operationem quae seriem augere potest invalidari potest**; ne acus veterem post `SN_ADDE`, `SN_INSERE` aut `SN_RESERVA` quae relocationem efficit servaveris.

Haec implementatio consulto `NUMERUS` tantum tractat. Ea fundamentum practicum praebet ad futuras series/slices et generica linguae sine semantica nondum canonica fingenda.

---

# IV. Fenestrale II Purus

Bibliothecae hodiernae Fenestralis includunt:

- `fenestrale_ii_superficies.vindex` — superficies clientium et compositio;
- `fenestrale_eventa_g.vindex` — coda eventuum;
- `clientia_registrum_h.vindex` — registrum dynamicum clientium;
- `fenestrae_registrum_i.vindex` — registrum dynamicum fenestrarum;
- `fenestrale_input_i.vindex` — separatio input a geometria fenestrarum;
- `fenestrale_gestor_i.vindex` — focus, ordo Z, motus, resize et status fenestrarum;
- `clientes_eventa_i.vindex` — distributio eventuum ad clientes;
- `programmata_clientis_e.vindex` — cliens PROGRAMMATA;
- `tabula_clientis_f.vindex` — cliens TABULA.

Fasciculi suffixis gradus `g`, `h`, `i` historiam canonizationis servant. Auctoritas praesentis systematis est catena Gradus I et probationes eius in `main`.

---

# V. Graphica historica

`graphica.vindex` eventa veteris motoris declarativi GTK describit. Servatur ad historiam et compatibilitatem experimentorum pristinorum.

**Officina canonica hodierna non eo ponte nititur.** Officina actualis est applicatio Windows nativa in radice repositorii sub `officina/`, sine HTML/CSS/JavaScript et sine motore GTK canonico.

Ne novam bibliothecam generalem super contractum GTK historicum construas nisi expresse ad migrationem vel archivum pertinet.

---

# VI. Regula evolutionis bibliothecae

Bibliotheca generalis VINDEX paulatim crescere debet ad:

- textum et Unicode;
- collectiones;
- fasciculos;
- projecta;
- rete;
- cryptographiam;
- mathematicam;
- concurrentiam;
- utilitates systematis;
- abstractiones portabiles inter targeta.

Sed bibliotheca standardis futura non debet facultates humilis gradus auferre neque runtime obligatoriam omnibus programmatibus imponere.

---

# VII. Importatio

Forma ordinaria:

```vindex
IMPORTA "bibliotheca/textus.vindex".
```

Viae in projectis maioribus per contractum `PROIECTUM` et contextum compilationis administrari possunt.

---

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
