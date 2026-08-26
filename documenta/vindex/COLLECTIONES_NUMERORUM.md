# VINDEX — Collectio dynamica numerorum

## Propositum

`bibliotheca/collectiones_numerorum.vindex` est primus gradus concretus bibliothecae collectionum generalium VINDEX.

Non nova syntaxis linguae est neque mutatio compilatoris. Facultatibus iam canonicis — memoria directa, `RESERVA_OCTETA`, `CONTENTUM`, `LIBERA`, functionibus et aestimatione brevi — utitur ut abstractio altiorem gradum praebeat.

Hoc principium magni momenti est: antequam generica linguae introducantur, VINDEX iam potest abstractiones reales super fundamenta humilis gradus construere.

## Contractus

```vindex
IMPORTA "bibliotheca/collectiones_numerorum.vindex".

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA c SICUT NUMERUS VALENS CN_CREA().
    CN_ADDE(c, 10).
    CN_ADDE(c, 20).
    CN_ADDE(c, 30).
    PROCLAMA CN_CAPE(c, 1).
    CN_LIBERA(c).
    REDDE 0.
FIN-FUNCTIO.
```

Exitus est `20`.

## API

### `CN_CREA()`

Collectionem vacuam creat. Sedem collectionis reddit; si memoria obtineri non potest, `0` reddit.

### `CN_NUMERUS(collectio)`

Numerum elementorum reddit. Collectio nulla `0` reddit.

### `CN_ADDE(collectio, valor)`

Valorem ad finem addit. Successus `1`, defectus `0`.

### `CN_CAPE(collectio, index)`

Valorem ad indicem legit. Indices a zero incipiunt. Index invalidus `0` reddit.

Quia `0` ipse valor legitimus est, programma quod validitatem distinguere debet primum `CN_NUMERUS` inspiciat.

### `CN_PONE(collectio, index, valor)`

Valorem existentem mutat. Successus `1`, index invalidus `0`.

### `CN_DELE(collectio, index)`

Elementum delet. Nodus deletus statim per `LIBERA` redditur. Primus, medius et ultimus nodus probantur.

### `CN_PURGA(collectio)`

Omnes nodos liberat atque collectionem vacuam relinquit, ita ut postea iterum adhiberi possit.

### `CN_LIBERA(collectio)`

Primum omnia elementa purgat, deinde caput collectionis liberat. Post hanc vocationem sedes antiqua iterum adhibenda non est.

## Repraesentatio

Caput collectionis XXIV octeta occupat:

```text
+0   numerus elementorum
+8   primus nodus
+16  ultimus nodus
```

Nodus XVI octeta occupat:

```text
+0   valor NUMERUS
+8   proximus nodus
```

Appendere est O(1), quia caput ultimum nodum servat. Accessus per indicem et deletio per indicem sunt O(n), quia structura lista simpliciter vinculata est.

Haec electio primae implementationis simplicem contractum memoriae et facilem probationem praebet. Vector dynamicus futurus potest accessum O(1) addere ubi reallocatio et generica maturiora sunt.

## Memoria

Collectio nullam runtime novam requirit. Nodi per `RESERVA_OCTETA` creantur et per `LIBERA` redduntur.

Probatio canonica confirmat:

- creationem;
- quattuor additiones;
- lectionem primi et ultimi;
- mutationem valoris;
- deletionem primi;
- deletionem medii;
- deletionem ultimi;
- valorem `0` legitimum;
- indices invalidos;
- purgationem;
- usum post purgationem;
- liberationem finalem.

## Limites

Prima collectio `NUMERUS` tantum continet. Hoc consultum est.

VINDEX nondum generica generalia canonica habet. Non fingitur `COLLECTIO<T>` antequam lingua ipsum `T` vere exprimere possit. Cum generica futura canonizabuntur, contractus huius bibliothecae potest fundamentum migrationis praebere.

## Probatio

Fons probationis:

```text
Vindex Chat-GPT/vindex_final_v51/tests/casus/collectiones_numerorum.vindex
```

Harnais canonicus:

```bash
make probatio
```

Cum hac collectione inclusa, series localis XXIV probationes rectas et nulla errata exspectat.

---

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
