# VINDEX 0.53 — Migratio tabulae historicae

## Propositum

`tabula` olim simul symbola, statum parseris, cursorem pilae, functiones, vocationes pendentes et formas continebat. Collectiones maiores iam ad memoriam crescentem migratae sunt, sed radix historica adhuc exstat:

```text
DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 3000.
```

Finis migrationis est statum compilationis nominatum et explicitum obtinere, non numeros magicos alio loco abscondere.

## Inventarium

`instrumenta/inventaria_tabula_053.py` omnes accessus litterales `tabula[n]` numerat. `instrumenta/TABULA-LITTERALIA-053.txt` basim admittendam figit et GitHub Actions index novus tacitus frangit.

Initio purificationis:

```text
INDICES LITTERALES DISTINCTI: 12
ACCESSUS LITTERALES TOTALES: 106
```

Post migrationem `227`: XI indices, XCVII accessus.
Post migrationem `2999`: X indices, XCV accessus.
Post migrationem cursoris `51`: IX indices, XLV accessus.
Post migrationem descriptorum functionum et vocationum pendentium: VII indices, XLI accessus.

Indices adhuc praesentes:

```text
2970
2971
2972
2990
2991
2992
2993
```

## Custodia semantica

Suite canonica XXV probationes continet. Inter probationes structuram migrationis directe custodientes sunt:

- `vocationes_nullae.vindex`: MXXIV vocationes sine argumentis, exitus `7168`;
- `desine_imbrique.vindex`: `DESINE` intra ansas `DUM` imbriquatas, exitus `48`;
- `argumenta_septem.vindex`: conventio System V cum septem argumentis, exitus `28`;
- `lectio_contextus.vindex`: status `LEGE/OCTETUS` per contextum explicitum transit.

Septem argumenta tam compilatore nativo quam amorsa Python probantur.

## I. Status `DESINE` — absolutus

`tabula[227]` omnino remota est. `STATUS_DESINE_LEGE` et `STATUS_DESINE_SCRIBE` contextum explicitum accipiunt.

## II. Status lectionis `2999` — absolutus

`tabula[2999]` omnino remota est. Status temporarius lectionis in secundo campo contextus servatur.

## III. Cursor pilae `51` — absolutus

`tabula[51]` omnino remota est. `CURSOR_PILAE_LEGE` et `CURSOR_PILAE_SCRIBE` tertium campum contextus regunt. Haec migratio L accessus litterales una mutatione delevit.

## IV. Functiones et vocationes pendentes — absolutae

`tabula[2982]` et `tabula[2985]` omnino remotae sunt. Descriptores functionum et vocationum pendentium nunc memoria propria utuntur, cuius structura est:

```text
+0  basis collectionis
+8  capacitas
+16 quantitas
```

`PARES_LEGE`, `PARES_SCRIBE`, `PARES_QUANTITAS` et `ASSECURA_PARES_DYNAMICA` descriptoris acum accipiunt; indices historici `2980..2985` in call-sites iam non sunt.

Contextus communis nunc XL octeta continet:

```text
+0  status DESINE
+8  intervallum temporarium lectionis
+16 cursor pilae functionis
+24 acus descriptoris functionum
+32 acus descriptoris vocationum pendentium
```

## V. Descriptor localium `2970..2972` — proximus gradus

Localia ipsa iam collectione crescente servantur; tantum descriptor historice in `tabula` manet:

```text
2970: basis — V accessus
2971: capacitas — III accessus
2972: quantitas — XIII accessus
```

Proximus gradus est descriptor localium in memoriam explicitam transferre et `INITIA_LOCA_DYNAMICA`, `ASSECURA_LOCA_DYNAMICA`, `LOCALE_LEGE`, `LOCALE_SCRIBE`, `RESTITUE_LOCA_DYNAMICA` atque `PROXIMUS_LOCUS_LIBER` ab `tabula` separare. Hoc XXI accessus litterales removebit.

## VI. Descriptor formarum `2990..2993`

Post localia tantum formae manebunt:

```text
2990: basis — V accessus
2991: capacitas — III accessus
2992: quantitas — VIII accessus
2993: index ultimae formae — IV accessus
```

His remotis ipsa `CAPACITAS 3000` deleri poterit.

## Disciplina migrationis

Post quemque gradum:

1. numerus accessuum literalium `tabula[n]` minuatur;
2. basis `TABULA-LITTERALIA-053.txt` renovetur;
3. nullus index magicus novus introducatur;
4. auto-hospitium punctum fixum servet;
5. amorsa Python transeat;
6. regressiones canonicae omnes transeant;
7. CRLF et pila > I MiB separatim transeant.

## Ordo operis

```text
227 remove — FACTUM
2999 remove — FACTUM
51 remove — FACTUM
2982/2985 remove — FACTUM
descriptor localium 2970..2972 remove
descriptor formarum 2990..2993 remove
CAPACITAS 3000 remove
PE/Windows integra
```

## Status comprobatus

```text
25 probationes rectae; 0 errata.
PUNCTUM FIXUM SHA-256: 405162aeb6d06302c388d7384723917a6a0e138887a7f6beffa755a700efff1b
INDICES TABULAE: 7
ACCESSUS TABULAE: 41
227: 0
2999: 0
51: 0
2982: 0
2985: 0
ARGUMENTA SEPTEM: 28
PILA MAGNA: 1048592,16
```

**VINDEX Latine cogitat. Sylvia Latine loquitur.**