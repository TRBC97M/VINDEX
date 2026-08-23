# FENESTRALE II — GRADUS B
## Compositorium minimum Sylvia OS

**Status:** experimentum exsecutabile  
**Series:** Fenestrale II  
**Gradus:** B  
**Praerequisitum:** Gradus A

---

## I. Propositum

Gradus A demonstravit Sylvia OS framebuffer monitoris resolutione nativa
directe pingere posse. Gradus B demonstrat secundam partem fundamenti:
**fenestrae non iam directe in desktop pinguntur; proprias superficies habent,
quas compositorium in framebuffer componit.**

Hoc experimentum adhuc UEFI separatum est et systema stabile 0.51 non mutat.

---

## II. Novae structurae

`fenestrale_native_b.c` introducit structuram `SUPERFICIES`:

```text
pix     — memoria ARGB XXXII-bit
w, h    — mensura propria
x, y    — positio in desktop
```

Tres superficies creantur:

- PROGRAMMATA;
- TABULA;
- barra operum.

PROGRAMMATA et TABULA non sunt regiones framebuffer. Sunt buffers memoriae
independentes, postea a compositore secundum ordinem profunditatis lecti.

---

## III. Alpha compositing

Pixel internus forma canonica experimentali utitur:

```text
AARRGGBB
```

Compositorium formulam alpha ordinariam adhibet et deinde colorem ad formam
GOP RGB vel BGR convertit.

Hoc permittit:

- umbras translucidas;
- titulos vitrei leviter translucidos;
- futuros effectus JL-UX sine framebuffer directe contaminando.

---

## IV. Z-order

Duae fenestrae ordinem dynamicum habent.

Clavis `Tab`:

1. fenestram activam mutat;
2. stilum tituli activi/inactivi mutat;
3. ordinem compositionis mutat;
4. buttonem correspondentem in barra operum illustrat.

Ita fenestra activa vere super alteram componitur.

---

## V. Regiones laesae

Sagittae fenestram activam movent.

Compositorium non totum desktop necessario repingit. Ante motum servatur regio
vetus; post motum regio nova computatur; unio earum tantum componitur.

Hoc est primum fundamentum systematis **damage rectangles** Fenestralis II.

Gradus posteriores possunt plures regiones et clipping subtilius addere.

---

## VI. Interactiones probationis

| Clavis | Actio |
|---|---|
| `Tab` | focus et z-order inter PROGRAMMATA/TABULA mutat |
| `← ↑ → ↓` | fenestram activam XII px movet |
| `Esc` | ad firmware redit |

Taskbar XXVIII px manet et compositorium eam tamquam superficiem supremam
tractat.

---

## VII. Constructio

Ex radice `vindex_final_v51`:

```bash
bash systema/uefi/construe_fenestrale_native_b.sh
```

Exitus:

```text
FENESTRALEB.EFI
fenestrale_b_uefi.img
```

Imago `.img` directe cum QEMU/OVMF bootari potest vel in clavem USB
experimentalem restitui potest.

---

## VIII. Quid nondum est

Gradus B nondum est window manager completus.

Desunt adhuc:

- muris hit-testing;
- tractio mouse;
- resize interactive;
- minimizatio/claudere vera;
- event queue generica;
- compositorium intra nucleum VINDEX;
- dynamicus numerus fenestrarum;
- font JL-UX finalis;
- acceleratio graphica.

Sed divisio fundamentalis iam probatur:

```text
APP → SUPERFICIES → COMPOSITORIUM → FRAMEBUFFER
```

non iam:

```text
APP → FRAMEBUFFER
```

---

## IX. Gradus C

Gradus C debet compositorium cum **input muris et window manager minimo**
coniungere:

- hit-testing a summo z-order deorsum;
- click-to-focus;
- tractio per titlebar;
- minimizatio;
- clausura;
- cursor propriam superficiem habens;
- eventa separata a pictura.

Post Gradum C, fundamentum satis maturum erit ut PROGRAMMATA I ab HTML
prototypo ad implementationem Sylvia nativam migrari incipiat.

---

## X. Regula architecturica

> Fenestra non est regio framebuffer.
> Fenestra possidet superficiem; compositorium possidet scrinium.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
