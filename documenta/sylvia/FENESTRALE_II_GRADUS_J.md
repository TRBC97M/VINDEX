# FENESTRALE II — GRADUS J
## Muris interactio super superficiebus multiplicibus

**Status:** experimentalis, applicatio UEFI separata  
**Series:** Fenestrale II  
**Gradus:** J  
**Praerequisitum:** Gradus I

---

## I. Propositum

Gradus I duas superficies privatas clientium VINDEX simul composuit atque
z-order dynamicum introduxit. Gradus J interactionem huius scrinii a sola
claviatura ad **murem verum UEFI** transfert.

PROGRAMMATA et TABULA manent clientes VINDEX distincti. Compositor solus
framebuffer physicum scribit et nunc etiam:

- cursorem pingit;
- fenestram summam sub cursore invenit;
- click ad focus convertit;
- titulum trahendo fenestram movet;
- taskbar ad minimizationem et restitutionem adhibet;
- bullam clausurae tractat.

---

## II. Fontes muris

Gradus J duas protocollorum UEFI vias sustinet:

1. `EFI_ABSOLUTE_POINTER_PROTOCOL`, utile praesertim tabulis tactilibus et
   quibusdam machinis UEFI;
2. `EFI_SIMPLE_POINTER_PROTOCOL`, pro mure relativo.

Si protocollo absoluto eventus utilis non datur, compositor protocollo
relativo uti potest. Motus relativus ad resolutionem realem monitoris
normalizatur.

Bulla sinistra breviter stabilitur, ne click simplex ob firmware instabile
multiplicetur.

---

## III. Cursor

Cursor pars compositorii est, non clientis. Post fenestras et taskbar pingitur.

Forma Gradus J retinet principium cursorem JL-UX iam definitum sine inscriptione
branding in superficie usoris:

- corpus ebur;
- margo graphites;
- parva forma classica et clara;
- nulla geometria mobilis magna.

Descriptor Fenestralis II campos `murus_x`, `murus_y` et `bullae` in tempore
executionis renovat.

---

## IV. Hit-testing et focus

`hit_fenestra` z-order a summo ad imum percurrit. Prima superficies visibilis
quae punctum muris continet eligitur.

Click in fenestra eam ad summum ordinem transfert. Ita focus non amplius est
sola alternatio artificialis per clavem `Tab`; ordo visualis sequitur actionem
usoris.

Clavis `Tab` tamen manet via subsidiaria.

---

## V. Tractio fenestrae

Click in area tituli `28 px`, extra botones systematis, tractionem incipit.
Compositor distantiam inter cursorem et originem fenestrae memorat.

Dum bulla sinistra tenetur:

- locus fenestrae cursorem sequitur;
- x et y intra scrinium coercentur;
- fenestra infra taskbar XXVIII px descendere non potest;
- z-order manet activus.

Sagittae claviaturae adhuc fenestram activam movent ut regressio et via
subsidii.

---

## VI. Minimizatio, restitutio et clausura

Taskbar manet `28 px` alta et non fluit.

PROGRAMMATA et TABULA proprios botones habent. Click:

- in fenestra activa eam minuit;
- in fenestra minuta eam restituit et focus dat;
- in fenestra visibili sed non activa focus dat.

Bulla minima in titulo idem statum `MINIMUS` ponit. Bulla rubra clausurae
statum `CLAUSUS` ponit et fenestram ex z-order removet.

In hoc gradu clausura runtime clientem denuo non exsequitur; tantum superficiem
ab scrinio removet. Launch/relaunch ad gradum posteriorem pertinet.

---

## VII. Registrum superficierum

Capacitas experimentalis registri manet octo descriptorum. Hoc **non** est
numerus programmatum Sylvia OS neque numerus locorum desktop. ABI nullum talem
limitem exponit.

Status cuiusque superficiei nunc distinguit:

```text
VISIBILIS
MINIMUS
CLAUSUS
```

Focus et hit-testing solas superficies `VISIBILIS` considerant.

---

## VIII. Clientium separatio

Gradus J eosdem clientes runtime iam probatos utitur:

- PROGRAMMATA H, client `1`;
- TABULA I runtime, client `2`.

Forma plena TABULA I separatim manet contractus visualis. Gradus J compilatorem
VINDEX 0.51 non mutat.

---

## IX. Constructio

Ex radice `vindex_final_v51`:

```bash
python3 tests/proba_fenestrale_ii_j.py
bash systema/uefi/construe_fenestrale_native_j.sh
```

Exitus separati sunt:

```text
FENESTRALEJ.EFI
fenestrale_j_uefi.img
```

CI regressiones D, G, H et I ante Gradum J verificat.

---

## X. Separatio stricta

Gradus J non mutat:

- `systema/nucleus.vindex`;
- `systema/uefi/firmamentum_uefi.c`;
- `BOOTX64.EFI` canonicum;
- imaginem UEFI 0.51;
- volumen VINDEX;
- compilatorem VINDEX;
- logicam `.VXNAT` Systematis principalis.

Ita labor Fenestralis II manet experimentum separatum donec series satis
matura sit ad integrationem deliberatam.

---

## XI. Proximus gradus

Gradus K potest resize fenestrarum, maximizationem/restaurationem et eventa
focus/magnitudinis ad clientes introducere. Inde fenestrae non solum moveri et
ordinari, sed etiam ad spatium desktop adaptive respondere poterunt.

> Compositor ordinat. Client pingit. Usor movet.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
