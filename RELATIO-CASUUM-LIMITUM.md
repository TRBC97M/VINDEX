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

---

## VIII. Renovatio — quid factum sit, quid restet

### Facta

| Vitium | Status | Ubi |
|---|---|---|
| Chorda non clausa → compilator cadens | **solutum** | circuli iam limitati in `main` |
| Claves clausurae orphanae → binarium cadens | **solutum** | #180 |
| Parenthesis non clausa taciturna | **solutum** | #181, per campum erroris |
| Operator `^` omissus (calculus falsus) | **solutum** | #184 |
| Operator `~` absens (calculus falsus) | **solutum** | #185 |

Campus erroris in contextu parseris (#181) mechanismum communem praebet:
offset LXXX genus, offset LXXXVIII positio, `ERRATUM_PONE` primum erratum
servans. Functiones profundae eo uti possunt sine accessu ad `via_fons`.

### Restat: claves ignotae ad gradum supremum

**Vitium.** Intra corpus functionis, verbum ignotum recte deprehenditur
(exitus 65). Ad gradum supremum, nihil: quidquid non agnoscitur silenter
transitur. Ideo hoc compilatur sine ullo monito:

```vindex
STRUCTURA P
    x SICUT NUMERUS.
FIN-STRUCTURA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    REDDE 0.
FIN-FUNCTIO.
```

Gravitas: scriptor credit `STRUCTURA` exsistere. Me ipsum fefellit cum
facultates linguae inspicerem — quod exemplum est vitii periculosissimi:
non falsum resultatum sed **falsa persuasio de lingua ipsa**.

**Causa, quam bis tentando inveni.** Fons vitii est ultimum `ALITER` circuli
principalis (linea 6651-6652):

```vindex
ALITER
    i = i + 1.
FIN-SI.
```

Custodiam ibi ponere **non licet**, quamvis primo aspectu locus rectus
videatur. Ratio: circulus principalis (linea 6277) gradum supremum NON
fideliter repraesentat. Post `ANALYSA_BLOCUS`, linea 6646 hoc facit:

```vindex
DUM i < n && fons[i] != 46 PERFICE
    i = i + 1.
FIN-DUM.
i = i + 1.
```

id est: **saltat ad punctum proximum et circulum principalem resumit**. Si
`ANALYSA_BLOCUS` in medio corpore desiit — quod in constructionibus
quibusdam fit — circulus principalis intra corpus resumitur, non inter
definitiones.

Probatio empirica: custodia ibi posita ATMOS POC III, IV, V frangit.
`graphicum.vindex` linea 253 (`CONTENTUM(args + 8) = point.`) ut clavis
ignota reicitur, cum codex perfecte validus sit.

**Directio recta.** Custodia vexillo indiget:

1. vexillum `inter_definitiones` in contextu parseris (offset XCVI liber);
2. ad verum ponitur cum `FIN-FUNCTIO` revera consumitur;
3. ad falsum cum corpus intratur;
4. custodia clavium ignotarum tantum si vexillum verum est.

**Probatio canonica mutanda.** `tests/run_tests.sh` linea 299 exspectat ut
`erratum_principalis.vindex` (`HOC NON EST PROGRAMMA VINDEX.`) nuntium
`FUNCTIO PRINCIPALIS deest` reddat. Custodia recta nuntium praecisiorem
dabit (`clavis ignota ad gradum supremum`, linea I columna I). Probatio
renovanda est, non custodia mollienda.

**Quod probatum est et quod non.** Custodia inconditionalis scripta est,
punctum fixum servavit, XXXV/XXXV transiit post probationem renovatam — sed
ATMOS fregit. Ramus deletus est, nihil propositum. Sine vexillo, custodia
recta esse non potest.
