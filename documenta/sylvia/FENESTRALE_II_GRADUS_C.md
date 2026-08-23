# FENESTRALE II — GRADUS C
## Administrator fenestrarum minimus cum mure

**Status:** experimentum exsecutabile  
**Series:** Fenestrale II  
**Gradus:** C  
**Praerequisitum:** Gradus B

---

## I. Propositum

Gradus B superficiem propriam cuique fenestrae et compositorium minimum
introduxit. Gradus C primam interactionem desktop veram addit:
**murem, hit-testing, focus, tractionem, minimizationem, clausuram et cursorem
compositum.**

Haec via adhuc applicatio UEFI experimentalis separata est. Systema stabile
0.51 et `BOOTX64.EFI` canonicum non mutantur.

---

## II. Input muris

Gradus C duas vias firmware sustinet:

- `EFI_SIMPLE_POINTER_PROTOCOL` pro mure relativo;
- `EFI_ABSOLUTE_POINTER_PROTOCOL` pro tabulis tactilibus vel aliis indicibus
  absolutis.

Via absoluta coordinatas firmware ad totam resolutionem framebuffer vertit.
Via relativa motum secundum resolutionem indicis normalizat et deinde ad
mensuram desktop nativi adaptat.

Status bullae sinistrae breviter stabilitur, ut mutationes spuriae firmware
minus facile duplices clicus fingant.

---

## III. Cursor ut superficies

Cursor non pingitur directe super framebuffer.

Possidet propriam superficiem ARGB transparentem et semper in summo ordine
compositionis ponitur:

```text
fundum
→ fenestrae
→ barra operum
→ cursor
→ framebuffer
```

Cum cursor movetur, compositorium unionem regionis veteris et novae tantum
recomponit.

Haec separatio necessaria est ne pictura fenestrarum sub cursore destruatur.

---

## IV. Hit-testing et focus

Pressio bullae sinistrae primo a summo z-order deorsum examinatur.

Si punctum intra fenestram est:

1. fenestra in focus venit;
2. eius titulus fit activus;
3. z-order mutatur;
4. button taskbar respondens fit activus.

Ita focus iam non est status fictus picturae: ordinem compositionis vere regit.

---

## V. Tractio fenestrarum

Pressio in titlebar, extra controles dexteros, tractionem incipit.

Offset inter cursorem et originem fenestrae servatur. Dum bulla tenetur,
fenestra cursorem sequitur sine saltu initiali.

Fenestra intra aream utilem continetur et infra barram operum XXVIII px
trahi non potest.

Damage rectangle est unio:

```text
regio vetus + regio nova + regio cursoris
```

Ergo totum framebuffer in omni motu repingi non debet.

---

## VI. Minimizatio

Button sinistrissimus trium controlorum titlebar fenestram minimizat.

Status internus:

```text
STATUS_VISIBILIS
STATUS_MINIMUS
STATUS_CLAUSUS
```

Fenestra minima:

- non componitur in desktop;
- manet in barra operum;
- clicus in button taskbar eam restituit et in focus ponit.

Clicus in button taskbar fenestrae iam activae eam quoque minimizare potest.

---

## VII. Clausura

Button ruber dexter fenestram claudit.

Fenestra clausa:

- non componitur;
- e barra operum removetur;
- non iterum aperitur in hoc experimento.

Reapertio vera pertinebit ad shell/program manager post integrationem cum
nucleo.

---

## VIII. Taskbar

Barra operum manet **XXVIII px** alta ad scala C%.

In Gradus C:

- `INITIUM` manet locus visualis, nondum menu completum;
- PROGRAMMATA et TABULA buttones statum fenestrarum significant;
- minimizatio, restitutio et focus per hos buttones operantur;
- fenestra clausa buttonem suum amittit.

Nulla forma pillularis vel dock mobilis introducitur.

---

## IX. Interactiones probationis

| Input | Actio |
|---|---|
| clicus in fenestra | focus et z-order |
| clicus + tractio in titlebar | fenestram movet |
| clicus in `—` | minimizat |
| clicus in `×` | claudit |
| clicus in taskbar | focus / minimizatio / restitutio |
| `Tab` | focus inter fenestras visibiles mutat |
| sagittae | fenestram activam XII px movent |
| `Esc` | ad firmware redit |

Button medius (`□`) iam pingitur, sed **maximizatio nondum implementatur**.
Hoc consulto ad Gradum posteriorem relinquitur.

---

## X. Constructio

Ex radice `vindex_final_v51`:

```bash
bash systema/uefi/construe_fenestrale_native_c.sh
```

Exitus:

```text
FENESTRALEC.EFI
fenestrale_c_uefi.img
```

Imago `.img` directe in QEMU/OVMF bootari potest vel in clavem USB
experimentalem restitui potest.

---

## XI. Quid nondum est

Gradus C nondum administrator fenestrarum generalis est.

Desunt:

- resize interactive;
- maximizatio/restauratio;
- numerus arbitrarius fenestrarum;
- descriptor dynamicus fenestrarum;
- event queue inter applicationes et shell;
- INITIUM functionale;
- iconographia finalis;
- font JL-UX finalis;
- integratio cum nucleo VINDEX;
- accelerationes graphicae.

Duae fenestrae probationis adhuc structuris explicitis repraesentantur.

---

## XII. Limes ad Gradum D

Post Gradum C, demonstrata sunt quattuor fundamenta:

1. framebuffer nativus;
2. superficies separatae;
3. compositorium et z-order;
4. window manager interactive cum mure.

Gradus D non debet tertium mockup separatum crescere. Debet **limitem inter
nucleum VINDEX et Fenestrale II formaliter aperire**.

Scopus Gradus D:

- descriptor display communis;
- descriptor fenestrae dynamicus;
- eventa input in structuram communem;
- compositorium callable a nucleo;
- primum clientem nativum minimalem;
- iter migrationis PROGRAMMATA I.

Systema 0.51 manet via recuperationis donec haec nova catena in QEMU et
hardware vero probata sit.

---

## XIII. Regula architecturica

> Input non pingit. Applicatio non possidet framebuffer.
> Window manager ordinat; compositorium praesentat.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
