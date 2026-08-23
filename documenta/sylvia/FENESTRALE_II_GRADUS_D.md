# FENESTRALE II — GRADUS D
## Limes inter firmamentum, nucleum et clientes nativos

**Status:** contractus ABI implementatus  
**Series:** Fenestrale II  
**Gradus:** D  
**Praerequisitum:** Gradus C

---

## I. Mutatio philosophiae

Gradus A–C responderunt quaestioni: *potestne nova interface Sylvia exsistere?*

- A: framebuffer nativus;
- B: superficies et compositorium;
- C: window manager interactive.

Gradus D aliam quaestionem incipit:

> Quomodo nucleus VINDEX, firmamentum et applicationes eandem rem graphicam
> sine dependentia occulta intellegunt?

Responsum est **ABI Fenestralis II**.

Hic gradus consulto nullum novum mockup introducit.

---

## II. Memoria communis

ABI Gradus D spatium nondum adhibitum intra paginam communem 0.51 reservat,
sine umbram hereditariam `320×200` tangendo.

```text
0x03000000  communis hereditarius 0.51
0x03000800  META hereditarium
0x03000900  FENESTRALE2_DESCRIPTOR
0x03000980  FENESTRALE2_EVENTA_META
0x030009A0  FENESTRALE2_EVENTA[32]
0x03000DA0  finis circuli eventuum
0x03001000  UMBRA 320×200 hereditaria incipit
```

Ita nova ABI intra spatium iam reservatum sed vacuum continetur.

---

## III. Descriptor display

`systema/fenestrale_ii_abi.h` structuram `FENESTRALE2_DESCRIPTOR` definit.
Mensura canonica est **CXXVIII octeta**.

Campi:

| Offset | Campus | Significatio |
|---:|---|---|
| `00` | `magic` | signum `SYLFEN2` |
| `08` | `versio` | versio ABI |
| `10` | `mensura` | mensura descriptoris |
| `18` | `capacitates` | bitfield facultatum |
| `20` | `framebuffer` | basis framebuffer physici |
| `28` | `latitudo` | latitudo nativa |
| `30` | `altitudo` | altitudo nativa |
| `38` | `pixel_per_lineam` | stride GOP |
| `40` | `formatum_pixelorum` | RGB/BGR |
| `48` | `bits_per_pixel` | hodie XXXII |
| `50` | `murus_x` | coordinata nativa |
| `58` | `murus_y` | coordinata nativa |
| `60` | `bullae` | status bullarum |
| `68` | `numerus_eventuum` | numerus mutationum input |
| `70` | `taskbar_altitudo` | XXVIII ad scala C% |
| `78` | `scala_per_mille` | M = C% |

Magic in memoria little-endian est `SYLFEN2\0`.

---

## IV. Capacitatum bitfield

Descriptor non cogit clientem assumere quid firmamentum sustineat.

Vexilla initialia:

- `FII_CAP_FRAMEBUFFER_NATIVUS`;
- `FII_CAP_PIXEL_RGB_BGR`;
- `FII_CAP_MURUS_RELATIVUS`;
- `FII_CAP_MURUS_ABSOLUTUS`;
- `FII_CAP_EVENTA`;
- `FII_CAP_COMPOSITORIUM`.

Cliens semper capacitates legit antequam facultate utatur.

---

## V. Circulus eventuum

Post descriptorem est circulus **XXXII eventuum**.

Meta:

```text
caput_scripturae
caput_lectionis
capacitas = 32
reservatum
```

Singulum eventum XXXII octeta habet:

```text
typus
vexilla
a
b
```

Typi initiales:

1. murus movetur;
2. bulla muris mutatur;
3. clavis premitur;
4. clavis solvitur;
5. display mutatur;
6. eventum fenestrae.

Argumenta `a` et `b` secundum typum interpretantur. ABI futura novas species
addere potest sine structuram fundamentalem mutando.

---

## VI. Bibliotheca VINDEX

`bibliotheca/fenestrale_ii.vindex` est prima facies clientis linguae VINDEX.

Praebet functiones ad:

- praesentiam ABI cognoscendam;
- framebuffer et resolutionem legendam;
- formatum et stride legendum;
- murem nativum legendum;
- altitudinem taskbar et scalam legendam;
- eventa pendentia numeranda;
- eventum typum, vexilla et argumenta legenda;
- eventum consumendum.

Cliens qui sub via veteri currit `FENESTRALE_II_AD_EST() == 0` accipit et
fallback suum retinere potest.

---

## VII. Compatibilitas 0.51

Gradus D **non mutat adhuc** contractum hereditarium quem nucleus 0.51
requirit.

Hoc est consilium deliberatum:

```text
0.51 vetus  ───────────────► communis vetus + UMBRA 320×200
Fenestrale II futurum ─────► descriptor novus + eventa + framebuffer nativus
```

Per migrationem utraque via adesse potest.

Quando firmamentum novum descriptor Gradus D implebit, nucleus vetus eum
ignorabit. Nucleus novus eum agnoscet sine heuristica.

---

## VIII. Disciplina versionis

Cliens descriptor validum tantum habet si:

```text
magic == SYLFEN2
versio == 1
mensura >= 128
```

Campus novus in fine descriptoris addi potest cum `mensura` crescit.
Campus vetus neque reordinatur neque significationem mutat intra eandem
versionem maiorem.

---

## IX. Probatio automatica

`tests/proba_fenestrale_ii_abi_d.py` verificat:

- bases memoriae;
- magic et versionem;
- mensuras;
- addressa quae bibliotheca VINDEX legit;
- circulum XXXII eventuum ante `UMBRA` finire;
- concordantiam inter caput C et API VINDEX.

Header C quoque `_Static_assert` habet, ne compilator mutationem mensurae
silentiose admittat.

---

## X. Quid Gradus D nondum facit

Contractus iam exsistit, sed firmamentum stabile 0.51 nondum descriptor implet.
Hoc est proximus subgradus integrationis, non defectus contractus.

Nondum fiunt:

- eventa a firmware in circulum scribere;
- descriptor Gradus D in `firmamentum_uefi.c` stabile implere;
- clientem desktop VINDEX ad compositorium conectere;
- fenestras arbitrarias creare/destruere per ABI;
- processuum separatio.

---

## XI. Gradus E

Post ABI D, proximus gradus debet esse **transitio compatibilis firmamenti**:

1. `firmamentum_uefi.c` descriptor Gradus D implet;
2. coordinatae muris nativae simul cum coordinatis veteribus servantur;
3. eventa in circulum scribuntur;
4. 0.51 nihil horum uti debet et idem manet;
5. probatio regressionis confirmat boot veterem intactum;
6. client nativus minimalis descriptor legit et eventa consumit.

Tum demum compositorium Gradus C e probatione UEFI in structuram systematis
VINDEX migrare potest.

---

## XII. Regula architecturica

> ABI est pactum, non pictura.
> Firmamentum describit facultates; nucleus eas ordinat; clientes eas utuntur.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
