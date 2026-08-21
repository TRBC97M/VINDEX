# VINDEX 0.52 — TEXTUS

`TEXTUS` est genus nativum VINDEX ad textum dynamicum tractandum. Propositum est usum manualem `ORDO DE LITTERA` et constructionem octetorum singillatim minuere, praesertim in Sylvia OS, Officina et instrumentis lineae mandatorum.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**

## Contractus primae implementationis

Prima implementatio has proprietates praebet:

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

`LONGITUDO` in `bibliotheca/textus.vindex` definitur, non intra `ANALYSA_FACTOR`. Descriptore TEXTUS recepto, functio primum verbum descriptoris per `CONTENTUM` legit.

## Memoria

Litteralia in regione immutabili binarii vivunt. Resultata concatenationis in TAS dynamice collocantur, eadem dispositione descriptoris utentes. Concatenatio summam longitudinum et capacitatem novam scribit, contenta ordine transfert et terminatorem nullum addit.

In 0.52 non introducitur garbage collector: vita valorum dynamicorum mechanismos memoriae VINDEX existentes sequitur. Designatio futura dominii vel relationum numeratarum separatim tractabitur.

## Comparatio

Comparatio `TEXTUS` secundum octeta contenti fit, non secundum sedes descriptorum. `==` et `!=` igitur etiam textus in regionibus memoriae diversis recte comparant. Adiutor internus comparationem lexicographicam parat, ut vexilla comparationis x86 cum operatoribus VINDEX congruant.

## Compatibilitas

`ORDO DE LITTERA` manet validum. `TEXTUS` non eum substituit in codicibus humilibus, bufferibus magnitudine fixa, rectoribus aut locis ubi collocatio exacta memoriae necessaria est.

## Limes localium compilatoris

Tabula compilatoris 0.51 centum loca variabilibus localibus cuiusque functionis reservat. `ANALYSA_FACTOR` nunc nonaginta novem loca utitur; gradus IV nullum novum locum localem ei addit.

Operatio gravis in adiutoribus separatis `COMPONE_CONCATENA_TEXTUS` et `COMPONE_COMPARA_TEXTUS` manet. `COMPONE_LITTERALE_TEXTUS` et `COMPONE_IMPRIME_TEXTUS` descriptorem litteralis et exhibitionem contenti curant. Fons compilatoris 209259 octeta ex limite 212999 occupat; 103 functiones auxiliares ex limite 150 adhibentur.

## Probationes

Probationes canonicae sunt:

- `examples/textus_litterale_052.vindex` — litterale et `PROCLAMA`;
- `examples/textus_longitudo_052.vindex` — parametrum et `LONGITUDO`;
- `examples/textus_concatena_052.vindex` — concatenatio catenata;
- `examples/textus_comparatio_052.vindex` — `==` et `!=` secundum contentum;
- `examples/textus_assignatio_052.vindex` — assignatio inter variabilia `TEXTUS`;
- `examples/textus_limites_052.vindex` — textus vacuus, concatenatio cum vacuo et catena plurium partium;
- `examples/textus_052.vindex` — acceptatio totius contractus.

Omnes hae probationes statum 0 reddunt. Auto-hospitium per G1, G2 et G3 statum 0 reddit, G2 et G3 sunt identica, et series regressionum VINDEX 0.51 viginti unam probationem rectam sine errore refert.

Ita contractus primae implementationis `TEXTUS` pro VINDEX 0.52 completus et probatus habetur.
