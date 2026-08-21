# VINDEX 0.52 — TEXTUS

`TEXTUS` est genus nativum VINDEX ad textum dynamicum tractandum. Propositum est usum manualem `ORDO DE LITTERA` et constructionem octetorum singillatim minuere, praesertim in Sylvia OS, Officina et instrumentis lineae mandatorum.

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

`TEXTUS` valor in ABI est acus ad structuram memoriae administratam:

```text
+0   longitudo : u64
+8   capacitas : u64
+16  octeta UTF-8 ...
```

Longitudo terminatorem nullum non numerat. Octeta post contentum terminatore nullo clauduntur ut pons cum API C et viis fasciculorum facilior sit. Capacitas spatium contenti, non caput, significat.

Prima versio UTF-8 octeta conservat; `LONGITUDO` igitur octeta numerat. Numeratio scalarum Unicode potest postea separata operatione addi sine ABI frangendo.

## Bibliotheca

`LONGITUDO` in `bibliotheca/textus.vindex` definitur, non intra analysatorem expressionum. Hoc consilium nucleum compilatoris simpliciorem servat et eandem syntaxin usoris retinet. Descriptore TEXTUS recepto, functio primum verbum descriptoris legit.

## Memoria

Litteralia possunt in regione immutabili binarii vivere. Resultata concatenationis memoriam dynamicam accipiunt. In 0.52 non introducitur garbage collector: vita valorum dynamicorum sequitur mechanismos memoriae VINDEX existentes. Designatio futura dominii vel relationum numeratarum separatim tractabitur; implementatio initialis non debet auto-hospitium compilatoris frangere.

## Compatibilitas

`ORDO DE LITTERA` manet validum. `TEXTUS` non eum substituit in codicibus humilibus, bufferibus magnitudine fixa, rectoribus aut locis ubi collocatio exacta memoriae necessaria est.

## Limes localium compilatoris

Tabula compilatoris 0.51 centum loca variabilibus localibus cuiusque functionis reservat. Hic limes magni momenti est in auto-hospitio: `ANALYSA_FACTOR` sex argumenta accipit et iam circiter nonaginta tres declarationes locales continet. Additio etiam unius localis novae igitur tabulam ad limitem ducere potest et metadata sequentia corrumpere.

Errores priores, inter quos segmentatio et nuntius `exsecutabile imperfecte scriptum est`, cum mutationibus quae nova localia in analysatores maximos addebant congruebant. Suspicio prior de regione temporaria `MITTE` ideo reiecta est; instrumentum quod eam movebat remotum est.

Implementatio nova functiones adiutrices parvas (`EST_TEXTUS_VARIABILIS`, `COMPONE_LITTERALE_TEXTUS`, `COMPONE_IMPRIME_TEXTUS`) separat. In `ANALYSA_BLOCUS` et in analysa parametrorum variabiles iam exsistentes atque valores speciales adhibentur, ne nova loca localia consumantur. Hoc principium etiam mutationibus futuris compilatoris servandum est, donec tabula localium ipsa amplietur.

## Gradus operis

Primus gradus exsecutionis in duas probationes minimas divisus est. `examples/textus_litterale_052.vindex` litterale TEXTUS et `PROCLAMA` probat; `examples/textus_longitudo_052.vindex` parametrum TEXTUS et `LONGITUDO` per bibliothecam probat. Ita vitium unius partis alteram non obscurat.

Concatenatio et comparatio secundum contentum postquam hic gradus stabilis est addendae sunt.

## Probatio canonica

`examples/textus_052.vindex` est programma acceptationis totius primae implementationis. TEXTUS non habetur completum donec illud a compilatore auto-hospite compilatur, exsecutio exitum rectum reddit, et probationes 0.51 regressiones non ostendunt.
