# LOGICA BREVIS VINDEX

## Propositum

Operatores logici `&&` et `||` aestimationem brevem habent. Pars dextra non aestimatur cum valor partis sinistrae iam exitum logicum determinat.

Haec regula necessaria est non solum ad celeritatem, sed etiam ad salutem memoriae. Conditio quae acus ante dereferentiam examinat debet posse dereferentiam omnino vitare.

## Coniunctio `&&`

Expressio `a && b` primum `a` aestimat.

- Si `a` falsum est, `b` non aestimatur et exitus est `0`.
- Si `a` verum est, `b` aestimatur.
- Exitus finalis semper logicus est: `0` aut `1`.

Exemplum:

```vindex
SI acus != 0 && CONTENTUM(acus + 48) == 0 TUNC
    ...
FIN-SI.
```

Si `acus` est nulla, `CONTENTUM(acus + 48)` numquam legitur.

## Disiunctio `||`

Expressio `a || b` primum `a` aestimat.

- Si `a` verum est, `b` non aestimatur et exitus est `1`.
- Si `a` falsum est, `b` aestimatur.
- Exitus finalis semper logicus est: `0` aut `1`.

## Ordo operatorum

Coniunctio logica `&&` ante disiunctionem logicam `||` aestimatur.

Ita:

```vindex
A || B && C
```

idem ordinem logicum habet ac:

```vindex
A || (B && C)
```

Operatores `&` et `|` non mutantur. Illi operationes bitarias manent et utramque partem aestimant.

## Implementatio

Compilator comparationem simplicem a compositione logica separat:

- `ANALYSA_COMPARATIO_SIMPLEX` comparationes ordinarias componit;
- `ANALYSA_CONIUNCTIO_LOGICA` saltum brevem pro `&&` componit;
- `ANALYSA_COMPARATIO` disiunctionem `||` supra coniunctionem administrat.

Saltus futuri per mechanismum ordinarium codicis VINDEX componuntur et postea corriguntur. Nulla runtime externa requiritur.

## Probationes canonicae

Custodia `VINDEX — Logica brevis` haec semper probat:

1. compilator se ipsum recompilat usque ad punctum fixum `G2 = G3`;
2. binarium canonicum cum `G3` identicum est;
3. pars dextra periculosa cum `CONTENTUM(48)` sub `&&` falso et `||` vero non exsequitur;
4. prioritas `&&` ante `||` servatur;
5. `&` et `|` operationes bitariae manent;
6. probatio LXXX fenestrarum Fenestralis I transit;
7. Fenestrale II Purus I integrum cum compilatore novo compilatur.

## Norma

A die huius canonizationis, codex VINDEX potest condicionibus logicis uti ad accessum memoriae vere custoditum. Non licet compilatori futurorum graduum hanc proprietatem removere sine mutatione explicita specificationis linguae.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
