# VINDEX 0.52 — TEXTUS

`TEXTUS` est genus nativum VINDEX ad textum dynamicum tractandum. Propositum est usum manualem `ORDO DE LITTERA` et constructionem octetorum singillatim minuere, praesertim in Sylvia OS, Officina et instrumentis lineae mandatorum.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

## Contractus primae implementationis

Prima implementatio completa has proprietates praebere debet:

```vindex
IMPORTA "bibliotheca/textus.vindex".

DECLARA nomen SICUT TEXTUS VALENS "Sylvia".
DECLARA systema SICUT TEXTUS VALENS nomen + " OS".
PROCLAMA systema.
```

### Operationes

- litterale inter `"..."` ad `TEXTUS` assignari potest;
- `+` duos textus concatenat;
- `==` et `!=` contentum comparant, non sedes memoriae;
- `LONGITUDO(textus)` numerum octetorum utilium reddit;
- `PROCLAMA textus.` contentum exhibet;
- `TEXTUS` parametrum functionis esse potest;
- assignatio inter variabilia `TEXTUS` sustinetur.

## Repraesentatio 0.52

`TEXTUS` valor in ABI est acus ad descriptorem:

```text
+0   longitudo : u64
+8   capacitas : u64
+16  octeta UTF-8 ...
```

Longitudo terminatorem nullum non numerat. Octeta post contentum terminatore nullo clauduntur ut pons cum API C et viis fasciculorum facilior sit. Capacitas spatium contenti, non caput, significat.

Prima versio UTF-8 octeta conservat; `LONGITUDO` igitur octeta numerat. Numeratio scalarum Unicode potest postea separata operatione addi sine ABI frangendo.

## Signum typi internum

VINDEX 0.51 iam regionem `tabula[2400..2499]` ad proprietatem scalaris variabilis servabat. In 0.52 haec regio in signum typi simplex evolvitur:

```text
0 = genus ordinarium
1 = FLUITANS
2 = TEXTUS
```

Hoc consilium novam regionem centum locorum non requirit. Praesertim regio `2900..2918`, quae metadata formarum extremarum continere potest, intacta manet. Itaque TEXTUS metadata existentia non laedit et capacitas `tabula` augeri non debet.

## Bibliotheca

`LONGITUDO` in `bibliotheca/textus.vindex` definitur, non intra `ANALYSA_FACTOR`. Hoc consilium nucleum analysatoris simpliciorem servat et eandem syntaxin usoris retinet. Descriptore TEXTUS recepto, functio primum verbum descriptoris per `CONTENTUM` legit.

## Memoria

Litteralia in regione immutabili binarii vivere possunt. Resultata concatenationis memoriam dynamicam accipient. In 0.52 non introducitur garbage collector: vita valorum dynamicorum mechanismos memoriae VINDEX existentes sequetur. Designatio futura dominii vel relationum numeratarum separatim tractabitur; implementatio initialis auto-hospitium compilatoris frangere non debet.

## Compatibilitas

`ORDO DE LITTERA` manet validum. `TEXTUS` non eum substituit in codicibus humilibus, bufferibus magnitudine fixa, rectoribus aut locis ubi collocatio exacta memoriae necessaria est.

## Limes localium compilatoris

Tabula compilatoris 0.51 centum loca variabilibus localibus cuiusque functionis reservat. Hic limes magni momenti est in auto-hospitio: `ANALYSA_FACTOR` sex argumenta accipit et iam multas declarationes locales continet. Additio localium in analysatores maximos metadata sequentia corrumpere potest.

Errores experimentales priores, inter quos segmentatio et nuntius `exsecutabile imperfecte scriptum est`, cum mutationibus directis analysatorum magnorum congruebant. Propterea prima implementatio `ANALYSA_FACTOR` omnino intactam servat.

Duae functiones adiutrices parvae separantur: `COMPONE_LITTERALE_TEXTUS` descriptorem litteralis construit, et `COMPONE_IMPRIME_TEXTUS` contentum descriptoris scribit. `ANALYSA_BLOCUS` et analysis parametrorum variabilibus iam exsistentibus atque valoribus specialibus utuntur, ne nova loca localia consumantur.

## Gradus operis

Primus gradus exsecutionis in duas probationes minimas divisus est. `examples/textus_litterale_052.vindex` litterale TEXTUS et `PROCLAMA` probat; `examples/textus_longitudo_052.vindex` parametrum TEXTUS et `LONGITUDO` per bibliothecam probat. Ita vitium unius partis alteram non obscurat.

Concatenatio et comparatio secundum contentum postquam hic gradus stabilis est addendae sunt.

## Probatio canonica

`examples/textus_052.vindex` est programma acceptationis totius primae implementationis. TEXTUS non habetur completum donec illud a compilatore auto-hospite compilatur, exsecutio exitum rectum reddit, et probationes 0.51 regressiones non ostendunt.
