# P16-V — Fenestrae modernae Sylviae

## Propositum

P16-V fenestras Fenestralis ab aspectu technico P16-I ad chrome systematis maturius promovet, sine semanticis interactionis iam probatis mutandis.

Geometria interactiva manet canonica:

- titulus: XXXVI px;
- regio clientis incipit ad LX px;
- bullae minimizationis, maximizatonis et clausurae easdem sedes servant;
- drag, resize, minimizatio, maximizatio, restitutio et clausura e registro Fenestralis manent;
- focus et ordo Z non a pictura, sed a registro fenestrarum reguntur.

P16-V ergo **chrome mutat, non contractum fenestrae**.

---

## Chrome novum

### Umbra duplex

Unaquaeque fenestra duas umbras post corpus habet:

1. umbram molliorem propiorem;
2. umbram profundam paulo longius positam.

Umbrae extra geometriam interactive pinguntur. Itaque hit-testing non crescit et fines resize non mutantur.

### Margo

Fenestra activa lineam superiorem bronzeam accipit. Fenestra inactiva eandem lineam argenteam accipit.

Latera duo gradus habent:

- ferrum externum;
- argentum internum.

Hoc fenestram a fundo separat sine vetere forma crassa et pseudo-3D.

### Titulus

Titulus duobus tonis pingitur.

Activus:

- pars superior `vitrum`;
- pars inferior `medium`;
- accentus aqua;
- margo superior bronzeus.

Inactivus:

- duo toni desaturati;
- accentus argentum;
- margo superior argentum.

Textus tituli manet forma bitmap VIII×VIII ad scalam II×, ut contractus P16-I non frangatur.

### Bullae

Bullae minimizationis et maximizatonis planae et clarae sunt. Bulla clausurae rubra manet in fenestra activa et mutior fit in fenestra inactiva.

Sedes historicae non mutantur, ergo probationes clic et hit-testing P16-II–IV valent.

### Status

Fascia status inferior colore leviore utitur et linea separatrice argentea. Corpus clientis non mutatur.

---

## Focus visualis

P16-V statum focus non ex colore deducit. Origo veritatis manet `FI_FOCUS_ID`.

Renderer accipit `activa`:

- `1` → chrome activum;
- `0` → chrome inactivum.

Cum TABULA focus accipit, PROGRAMMATA statim in chrome inactivum transit et TABULA accentum bronzeum recipit.

---

## Probatio QEMU

`instrumenta/proba_fenestras_sylviae_v.py` sub UEFI/QEMU:

1. bootat in bureau;
2. PROGRAMMATA per PS/2 aperit;
3. accentum bronzeum, titulum activum, umbram duplicem et bullas comprobat;
4. TABULA quoque aperit;
5. PROGRAMMATA in statum visualem inactivum transire comprobat;
6. TABULA accentum focus accipere comprobat;
7. umbram TABULAE comprobat.

Probatio screendump realem framebuffer legit; non est mock neque imago generata.

---

## Catena

```text
OVMF
  → BOOTX64.EFI [VINDEX]
  → FENESTRALE II [VINDEX]
  → REGISTRUM FENESTRARUM
  → CHROME P16-V
      ↘ focus activus
      ↘ focus inactivus
      ↘ umbrae
      ↘ bullae
      ↘ regio clientis
  → FRAMEBUFFER
  → screendump QEMU
```

Nullus runtime C introducitur.

---

## Quod sequitur

P16-V non debet in seriem infinitam emendationum cosmeticorum mutari. Post chrome fenestrarum canonizatum, prioritas Sylviae ad **applicationes reales** transit:

1. TERMINALE;
2. OFFICINA / editor VINDEX in ipsa Sylvia;
3. gestor fasciculorum.

Ita bureau et Fenestrale fiunt instrumenta laboris, non solum demonstratio graphica.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
