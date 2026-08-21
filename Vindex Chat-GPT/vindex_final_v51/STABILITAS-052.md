# VINDEX 0.52 — Stabilitas Compilatoris

Hoc opus ante `TEXTUS` ponitur. Propositum non est novas proprietates celeriter accumulare, sed compilatorem 0.51 ita firmare ut mutationes posteriores causas occultas non introducant.

## Principia

1. Nulla regio `tabulae` adhibetur antequam fines eius in `TABULA-052.md` descripti sunt.
2. Mutationes magnae in `ANALYSA_FACTOR` et `PRINCIPALIS` vitantur; nova logica, ubi fieri potest, in functiones auxiliares separatur.
3. Commentaria linearia `//` in instrumento publico praeparantur sine mutatione positionum octetorum. Characteres commentarii spatiis substituuntur; finis lineae servatur.
4. `//` intra chordas vel litteras non est commentarium.
5. Probationes huius rami manu tantum fiunt. Nulla GitHub Actio automatica huic labori necessaria est.

## Commentaria

`instrumenta/vindex_praepara.py` fontem ante verificationem et compilationem praeparat. Longitudo fontis ante et post praeparationem eadem manet. Hoc consilium electum est quia compilator 0.51 effectus positioni fontis sensibiles ostendit; lineas vel octetos removere igitur periculosum esset.

Interfacies `vindexc` praeparatorem adhibet, deinde tutelam defectuum notorum, deinde verificatorem, postremo compilatorem. Si Python 3 abest, praeparatio et tutela omittuntur more compatibili cum 0.51.

## Identificatores maiusculi

Usus variabilium omnino maiuscularum est defectus confirmatus 0.51. Analysis factorum eas cum vocationibus functionum confundere potest, quia via identificatorum maiusculorum vocationem cum parenthesi exspectat.

`instrumenta/vindex_tutela_052.py` hunc casum nunc ante invocationem compilatoris interceptat. Sic defectus nativus non iam debet in ruinam obscuram mutari: usor diagnosticum Latinum cum archivo, linea, columna et nomine identificatoris accipit. Haec tutela correctio linguae definitiva non est; removebitur cum analysis nativa variabiles maiusculas recte distinguet a vocationibus functionum.

## TEXTUS

`TEXTUS` non deletur nec postponitur sine fine. Reintroducetur postquam saltem commentaria et identificatores maiusculi casibus minimis reproductibilibus stabiliuntur. Regio destinata metadatae novae est `3000–3099`, non regio circa `2900` quae cum metadata formarum colliditur.

## Devise

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
