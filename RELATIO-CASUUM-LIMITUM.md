# Relatio casuum limitum — compilator VINDEX

**Auctor:** Claude. **Genus:** relatio tantum; nullus codex mutatus.

Probatio systematica compilatoris contra casus limites et fontes vitiosos.
Finis non est omnia statim corrigere, sed **inventa scripto tradere** ut
quisquis ea postea tractet sciat quid inveniendum sit.

---

## I. Quae recte se habent

| Casus | Resultatum |
|---|---|
| Chorda MM litterarum | recta |
| L `SI` imbricati | rectus |
| CCC functiones in uno fonte | rectae |
| `9223372036854775807` et eius negativum | recta |
| Functio inexistens vocata | diagnosticum (65) |
| Fons vacuus | diagnosticum (65) |
| `FUNCTIO PRINCIPALIS` deest | diagnosticum (65) |
| `REDDE` sine valore | diagnosticum (65) |
| Divisio per nihilum | SIGFPE in exsecutione (more ferri) |

Diagnostica haec cum linea et columna redduntur — bene.

---

## II. Vitium primum: signa clausurae orphana → **binarium cadens**

Quattuor claves clausurae, si sine initio suo apparent, compilationem
transeunt sed **binarium cadens** producunt (SIGSEGV, exitus 139):

```text
FIN-SI orphanum    -> compilatio 0, exsecutio 139
FIN-DUM orphanum   -> compilatio 0, exsecutio 139
FIN-PER orphanum   -> compilatio 0, exsecutio 139
ALITER orphanum    -> compilatio 0, exsecutio 139
```

Reproductio minima:

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    FIN-SI.
    REDDE 7.
FIN-FUNCTIO.
```

**Causa probabilis.** `ANALYSA_BLOCUS` circulum suum terminat cum `FIN-`
vel `ALITER` videt (lineae 4806, 4809): id enim exspectatur, quia vocans
clavem clausurae ipse consumere debet. Si autem clavis orphana est,
nemo eam consumit; reliquum corpus functionis numquam analysatur, ergo
epilogus rectus numquam emittitur.

**Gravitas.** Maior quam species prima fert: non est simplex acceptatio
taciturna, sed **codex machinae invalidus**. Scriptor credit se recte
compilasse.

**Correctio suggesta.** `ANALYSA_BLOCUS` scire debet an in corpore
functionis an in blocco interno vocetur. In corpore, clavis `FIN-`
praeter `FIN-FUNCTIO` erratum est. Hoc parametrum novum poscit vel
statum in contextu parseris — ideo **opus separatum**, non minimum.

---

## III. Vitium secundum: parenthesis non clausa taciturna

```vindex
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    REDDE (1 + 2.
FIN-FUNCTIO.
```

Compilatur; exitus 3 redditur — **valor rectus**. Binarium ergo non
cadit, sed error scriptoris tacetur. Minus grave quam I, sed diagnosticum
merebatur.

---

## IV. Vitium tertium: `FUNCTIO PRINCIPALIS` bis definita

Duae definitiones eiusdem nominis sine ullo monito acceptantur; **prima
vincit** (probatum: exitus 1, non 2). Redefinitio silens fons errorum
subtilium est, praesertim cum `IMPORTA` adhibetur.

---

## V. Vitium quartum: `FIN-FUNCTIO` deficiens taciturnum

Fons sine `FIN-FUNCTIO` finali compilatur sine monito.

---

## VI. Quid iam correctum est

- **Chorda litteralis non clausa** compilatorem ipsum occidebat (SIGSEGV,
  exitus 139): septem circuli lectionis sine limite super `n`. Correctum
  in PR #170; genus diagnostici VII (`chorda litteralis non clauditur`)
  additum, sed propagatio erroris ex functionibus profundis adhuc deest,
  ergo casus nunc **taciturne acceptatur** loco diagnostici — melius quam
  casus, nondum optimum.

- **Identificatores ultra XXXII litteras** aream tamponis excedebant
  (SIGSEGV) et nomina post XXXII litteram differentia idem signum
  accipiebant. Correctum in PR #168 tampone omnino sublato.

---

## VII. Ratio communis

Quattuor vitia superstitia unam radicem communem habent: **propagatio
erroris ex functionibus analyseos profundis ad `PRINCIPALIS` non exsistit**.
`DIAGNOSTICUM_FONTIS` ex `PRINCIPALIS` sola vocatur et ad `via_fons` et
`n_fons_principalis` accessum habet, quae `ANALYSA_FACTOR` vel
`ANALYSA_BLOCUS` non habent.

Ergo directio probabilis non est quattuor correctiones separatae sed
**una**: campus erroris in contextu parseris, quem functiones profundae
ponere possint et `PRINCIPALIS` post analysim legat. Genus VII iam paratum
est ad hunc usum.

Opus id non parvum est et compilatorem tangit; ideo hic **describitur
tantum**, non fit. Quisquis id suscipiet hanc relationem pro fundamento
habere poterit.
