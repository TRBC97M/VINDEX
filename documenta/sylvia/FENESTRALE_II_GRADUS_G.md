# FENESTRALE II — GRADUS G
## Superficies privatae et mailbox compositorii

**Status:** experimentalis, extra viam Sylvia OS stabilem  
**Series:** Fenestrale II  
**Gradus:** G  
**Praerequisitum:** Gradus F

---

## I. Propositum

Gradus F primum clientem VINDEX nativum ad framebuffer physicum directe
scribentem demonstravit. Id ad probationem utile erat, sed client graphicus
finalis framebuffer globalem possidere non debet.

Gradus G igitur primum contractum **superficiei privatae** introducit:

- client superficiem petit;
- compositor memoriam pixelorum attribuit;
- client intra suam superficiem pingit;
- client regionem mutatam per `PRAESENTA` nuntiat;
- compositor solus framebuffer physicum componere debet.

Hoc gradus contractum definit et clientem PROGRAMMATA ad illum transfert.
Firmamentum canonicum 0.51 et nucleus canonicus **non mutantur**.

---

## II. Mailbox

Extensio experimentalis in spatio vacuo inter circulum eventuum Gradus D et
`UMBRA` hereditariam ponitur:

```text
0x03000DA0  finis eventuum Gradus D
0x03000E00  FENESTRALE2_COMPOSITOR_MAILBOX
0x03000F00  finis mailbox (256 octeta)
0x03001000  UMBRA 320×200 hereditaria
```

Mailbox est serialis. Hoc **non** significat unam tantum fenestram aut quattuor
loca fixa; solum una petitio controlis simul transit. Superficies ipsae memoria
dynamica compositorii sunt et numero huius structurae non definiuntur.

Magic:

```text
SYLCMP2\0
```

Versio initialis est `1`, mensura `256` octeta.

---

## III. Status

Quattuor status sunt:

- `VACUUM` — nulla petitio pendet;
- `PETITUM` — client structuram complevit et compositor eam legere potest;
- `PERFECTUM` — responsum validum paratum est;
- `ERRATUM` — petitio recusata vel exsecutio defecit.

Client campos petitionis **ante** statum `PETITUM` scribit. Compositor statum
`PERFECTUM` vel `ERRATUM` ultimum scribit. Ita mutatio status munus sigilli
simplicis agit.

---

## IV. Operationes

Gradus G definit:

1. `CREA` — superficiem privatam crea;
2. `DELE` — superficiem libera;
3. `PRAESENTA` — regionem mutatam compositorii nuntia;
4. `MOVE` — positionem fenestrae muta;
5. `OSTENDE` — superficiem visibilem fac;
6. `CELA` — superficiem absconde;
7. `FOCUS` — superficiem activam pete.

Non omnes operationes hoc gradu ab aliquo firmamento impletae sunt. ABI eas
nunc stabilit ne client PROGRAMMATA rursus mutandus sit cum compositor runtime
postea conectitur.

---

## V. Superficies

Responsum `CREA` continet saltem:

- `superficies_id`;
- `basis_pixelorum`;
- `pixel_per_lineam`;
- `formatum_pixelorum`;
- latitudinem et altitudinem petitionis acceptae.

Pixels sunt XXXII-bit. Gradus G alpha `255` pro coloribus opacis scribit.
RGB et BGR eodem contractu sustinentur.

Client non scribit in `FENESTRALE_II_FRAMEBUFFER()`.

---

## VI. PROGRAMMATA G

`src/programmata_fenestrale_ii_g.vindex` prioris Gradus F structuram visualem
retinet, sed omnes rectangulos in superficiem privatam scribit.

Normae servatae:

- fenestra quadrata, radius nullus;
- titulus `28 px`;
- menu `22 px`;
- instrumenta `34 px`;
- status `20 px`;
- taskbar systematis `28 px`;
- vitrum caeruleum moderatum;
- ebur et argentum ut superficies functionales;
- bronzeum raro;
- rubrum solum pro actione clausurae;
- nulla inscriptio `JL-UX` in superficie usoris;
- `TABULA.VXNAT` manet unicum programma initiale conceptus.

Glyphi finalis familiae typographicae nondum includuntur. Rectangula tenuia
vestigia textus tantum sunt; futura typographia propria ea substituet.

---

## VII. Cur Gradus G sessionem principalem non tangit

Hic gradus:

- `systema/nucleus.vindex` non mutat;
- `systema/uefi/firmamentum_uefi.c` non mutat;
- `BOOTX64.EFI` canonicum non mutat;
- volumen 0.51 non mutat;
- logicam exsecutionis `.VXNAT` non mutat.

Solum extensio ABI, bibliotheca clientis, client visualis experimentalis,
probationes et documenta adduntur.

Ita opus JL-UX/Fenestrale II pergere potest sine ramo laboris principalis
Sylvia OS invadendo.

---

## VIII. Probatio

```bash
python3 tests/proba_fenestrale_ii_abi_d.py
python3 tests/proba_programmata_fenestrale_f.py
python3 tests/proba_fenestrale_ii_compositor_g.py
```

Probatio Gradus G confirmat:

- header C mensuram mailbox servare;
- mailbox eventa D neque UMBRAM 0.51 attingere;
- bibliothecam VINDEX easdem inscriptiones uti;
- clientem framebuffer globalem directe non scribere;
- alpha opacum in superficie privata scribi;
- mensuras JL-UX canonicas servari;
- fontes VINDEX verificatore syntactice probari.

---

## IX. Proximus gradus

Gradus H potest compositorium **experimentale separatum** facere quod mailbox G
re vera administrat et superficies clientium in framebuffer nativum componit.
Id faciendum est eadem disciplina ac Gradus A–C: extra firmware canonicum, cum
imagine bootabili propria et CI separata.

Postea tantum, probatione QEMU et hardware completa, deliberari potest de
integratione in viam principalem Sylvia OS.

> Client non amplius scrinium possidet; superficiem suam possidet.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
