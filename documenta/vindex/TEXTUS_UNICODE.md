# TEXTUS Unicode — Contractus Canonicus

## Propositum

`TEXTUS` UTF-8 octeta iam a VINDEX 0.52 servat. Hoc documentum facultates Unicode bibliothecae canonicas definit sine mutatione ABI `TEXTUS`.

Repraesentatio manet:

```text
+0   longitudo octetorum
+8   capacitas octetorum
+16  octeta UTF-8
```

`LONGITUDO(textus)` numerum **octetorum** reddit. Non mutatur, quia haec proprietas pars ABI et utilitas humilis gradus est.

## Facultates

`bibliotheca/textus.vindex` praebet:

- `UTF8_VALIDUS(textus)` — `1` si omnis catena UTF-8 canonice valida est, aliter `0`;
- `LONGITUDO_SCALARUM(textus)` — numerum scalarum Unicode reddit; `-1` si catena invalida est;
- `UTF8_SCALARE_CAPE(textus, index)` — valorem scalaris Unicode indice a zero reddit; `-1` si index invalidus aut catena UTF-8 invalida est;
- `UTF8_POSITIO_SCALARIS(textus, index)` — positionem octeti ad limitem scalaris reddit, fine textus ut indice legitimo admisso;
- `SUBTEXTUS_SCALARUM(textus, initium, numerus)` — novum `TEXTUS` ex intervallo scalarum Unicode creat sine sequentiam UTF-8 incidere.

Textus vacuus UTF-8 validus est et zero scalaria continet.

`SUBTEXTUS_SCALARUM` inter vacuum et errorem distinguit:

- subtextum vacuum legitimum descriptor `TEXTUS` non-nullus longitudine zero est;
- input invalidum, UTF-8 invalidum vel defectus memoriae `TEXTUS` nullum (`0`) reddit.

## Functiones et reditus TEXTUS

PR #107 contractum iam implicitum canonice probavit: functio VINDEX `TEXTUS` redire potest, sive litteralem, sive parametrum, sive concatenationem dynamicam. Valor redditus a vocante comparari, mensurari et operationibus Unicode tradi potest.

Hoc fundamentum permittit ut `SUBTEXTUS_SCALARUM` et futurae operationes textuales nova obiecta `TEXTUS` naturaliter reddant sine syntaxeos vel ABI mutatione.

## Validatio stricta

Validator non solum formam continuationum inspicit. Reicit etiam formas quas Unicode vetat:

- octeta continuationis sine capite;
- sequentias truncatas;
- formas superlongas;
- capita `C0` et `C1`;
- surrogata `U+D800`–`U+DFFF`;
- scalaria supra `U+10FFFF`;
- capita quinque aut plurium octetorum obsoleta.

Intervalla canonica igitur sunt:

- `00`–`7F`;
- `C2`–`DF` + una continuatio;
- `E0`–`EF` + duae continuationes, cum custodiis contra formas superlongas et surrogata;
- `F0`–`F4` + tres continuationes, cum custodiis contra formas superlongas et valores supra maximum Unicode.

## Scalae, non graphemata

`LONGITUDO_SCALARUM`, `UTF8_SCALARE_CAPE` et `SUBTEXTUS_SCALARUM` scalaria Unicode tractant, non graphemata quae usor visu pro uno charactere habet.

Exempli gratia littera cum signo combinanti duas scalaria continere potest. Segmentatio graphematum, normalizatio NFC/NFD, proprietates Unicode et case folding sunt gradus futuri separati.

Haec distinctio deliberata est: primum fundamentum UTF-8 exactum et parvum canonizatur; deinde abstractiones textus superiores super eo aedificari possunt.

## Memoria et copia

`SUBTEXTUS_SCALARUM` novum descriptorem `TEXTUS` et nova octeta reservat. Itaque subtextus fontem non mutuat et post creationem sedem propriam habet.

Adiutor `TEXTUS_COPIA_OCTETORUM` copiam humilis gradus facit et terminatorem nullum post contentum servat. `TEXTUS_EX_SEDE` conversionem explicitam a sede numerica ad genus `TEXTUS` praebet.

## Compatibilitas

Nulla mutatio compilatoris aut ABI fit. Programmata quae `LONGITUDO` ut numerum octetorum ad fasciculos, protocolla aut API externas utuntur eandem semanticam servant.

`ORDO DE LITTERA` et accessus memoriae humilis gradus manent validi.

## Probatio canonica

Casus `tests/casus/textus_unicode.vindex` probat:

- ASCII;
- scalare duorum octetorum `U+00E9`;
- scalare trium octetorum `U+20AC`;
- scalare quattuor octetorum `U+1F600`;
- textum vacuum;
- formam superlongam;
- sequentiam truncatam;
- surrogatum;
- valorem supra `U+10FFFF`;
- continuationem solitariam.

Casus `tests/casus/textus_reditus.vindex` reditum `TEXTUS` a functionibus probat.

Casus `tests/casus/subtextus_unicode.vindex` probat:

- extractionem centralem ex `Aé€😀Z`;
- limites primum et ultimum;
- subtextum vacuum in medio et fine;
- copiam totius fontis cum descriptore distincto;
- indices negativos et ultra fines;
- rejectionem fontis UTF-8 corrupti.

Post PR #108 suite canonica **XXIX probationes rectas, nulla errata** refert.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
