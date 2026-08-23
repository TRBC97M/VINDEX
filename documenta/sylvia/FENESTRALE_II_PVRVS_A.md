# FENESTRALE II — PVRVS A
## Prima superficies desktop nativa omnino VINDEX

**Status:** experimentalis, pendet a correctione architectonica PR #30  
**Series:** Fenestrale II Purus  
**Gradus:** A  
**Lingua runtime:** VINDEX sola

---

## I. Ruptura cum via repudiata

Gradus veteres qui `fenestrale_native_*.c` ad compositorium, input aut
fenestras utebantur non sunt fundamentum huius seriei. Historia Git manet,
sed architectura illa repudiata est.

Regula huius seriei est absoluta:

> post saltum bootstrap UEFI, nulla logica runtime extra VINDEX exsistit.

Bootstrap alienae linguae solum initium firmware aperit, metadata minima
scribit, nucleum VINDEX onerat atque imperium semel tradit. Non pingit
fenestras, non legit murem, non componit superficies et non revocatur.

---

## II. Propositum Gradus A

`systema/fenestrale_ii_purus_a.vindex` probat ipsum VINDEX posse ex metadata
bootstrap:

- framebuffer physicum legere;
- resolutionem et `PixelsPerScanLine` reales uti;
- RGB/BGR discernere;
- pixela et rectangula XXXII-bit scribere;
- fontem firmware iam traditum legere;
- textum in resolutione nativa pingere;
- desktop JL-UX sine superficie 320×200 construere.

Nullum `fenestrale_native_*.c`, nullum callback `POLLE()` et nullum ministerium
runtime alienae linguae introducitur.

---

## III. Metadata initii

Gradus A legit pactum minimum quod bootstrap correctivus iam tradit in
`0x03000800`:

| Locus | Res |
|---|---|
| `0x03000800` | modus UEFI |
| `0x03000810` | basis framebuffer |
| `0x03000818` | pixela per lineam |
| `0x03000820` | latitudo physica |
| `0x03000828` | altitudo physica |
| `0x03000830` | formatum RGB/BGR |
| `0x03000858` | forma glyphorum VIII×VIII |

Haec sunt data initii, non servitium runtime.

---

## IV. Primitivae graphicae VINDEX

Gradus A ipse definit:

- `P_PIXEL` — unum pixelum physicum;
- `P_RECT` — rectangulum cum clipping ad limites monitoris;
- `P_TEXTUM` — textum per fontem VIII×VIII;
- `P_COLOR` — ordinem byte RGB/BGR;
- `P_FUNDUM` — wallpaper nativum caeruleum;
- `P_FENESTRA` — fenestram quadratam JL-UX;
- `P_TASKBAR` — barram operum XXVIII px;
- `P_CURSOR` — cursorem ebur/graphites.

Nulla harum functionum vocat C, ASM, Rust, C++ aut runtime externum.

---

## V. Imago visualis

Prima demonstratio continet duas fenestras simul:

### PROGRAMMATA

- fenestra activa;
- titulus XXVIII px;
- menu XXII px;
- instrumenta XXXIV px;
- columna collectionum;
- `TABULA.VXNAT` ut programma initiale;
- accentus bronzeus minimus.

### TABULA

- fenestra secundaria;
- barra formulae;
- capita columnarum et ordinum;
- rete octo columnarum et duodecim ordinum;
- cellula activa cum accentu bronzeo.

Desktop utitur resolutione physica vera. Barra operum manet **XXVIII px** ad
scala C%. Nulla inscriptio `JL-UX` in superficie usoris apparet.

---

## VI. Quid Gradus A nondum facit

Gradus A est primum fundamentum graphicum purum. Nondum implementat:

- compositorium superficierum separatarum;
- z-order dynamicum;
- hit-testing;
- tractionem;
- resize;
- maximizationem;
- loop eventuum desktop novum.

Haec omnia sequentur **in VINDEX**. Si facultas linguae deest, VINDEX prius
extendendus est; nulla via runtime aliena adhibebitur.

---

## VII. Relatio ad correctionem PR #30

Hic ramus directe ex `chatgpt/custos-vindex-purus` nascitur. Pull Request huius
Gradus ad illum ramum destinatur et **non ad `main` mergeatur antequam PR #30
perfecta et canonica sit**.

Ita progressio visualis potest procedere sine fundamentum correctivum
praeterire.

---

## VIII. Probatio

CI verificat:

1. custodem puritatis Sylviae;
2. syntaxim fontis VINDEX;
3. compilationem `fenestrale_ii_purus_a.vindex` in ELF64;
4. magnitudinem sub limite nuclei bootstrap hodierni.

Successus Gradus A significat primam picturam desktop resolutionis nativae ex
**VINDEX ipso**, non ex simulatione C.

> VINDEX est ratio. Sylvia est forma viva eius.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
