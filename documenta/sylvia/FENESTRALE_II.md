# SYLVIA OS — FENESTRALE II

## Fundamentum graphicae modernae

**Status:** propositum architecturale ad implementationem  
**Systema:** Sylvia OS  
**Lingua visualis:** JL-UX Core I.0  
**Genus mutationis:** Sylvia OS  
**Annus:** MMXXVI

---

## I. Propositum

Fenestrale II est ruptura deliberata a superficie logica veteri `320×200`.

Sylvia OS non amplius debet mensam operariam totam ut imaginem parvam pingere et postea ad magnitudinem monitoris extendere. Resolutionem veram monitoris accipit, in ea directe componit, et numerum fenestrarum dynamicum administrat.

Scopus est ut Sylvia OS ad usum cotidianum similem systematibus desktop plenis perveniat sine amissione identitatis JL-UX.

**Principium:**

> Resolutio monitoris est spatium reale operis, non textura quae ex `320×200` dilatatur.

---

## II. Regulae non negotiabiles

1. Nulla superficies desktop fixa `320×200` manet in via moderna.
2. Fenestrae multiplices simul adsunt et ordine profunditatis componuntur.
3. Fenestrae quadratae sunt; radius exterior est `0 px`.
4. Barra operum ad scala C% est `28 px` alta.
5. JL-UX non scribitur in imagine fundi neque in interface communi.
6. Sylvia OS est identitas primaria.
7. Applicatio non debet scire magnitudinem physicae memoriae video.
8. Numerus fenestrarum, programmatum et iconum non designatur per sex locos fixes.
9. Vetera programmata `320×200` possunt transitorie intra superficiem hereditariam currere, sed numquam totum desktop regunt.
10. UEFI/GOP est via moderna primaria; BIOS manere potest ad probationem historicam.

---

## III. Resolutiones

### Resolutio physica

Pons UEFI dimensiones veras framebuffer tradit:

- latitudinem;
- altitudinem;
- numerum octetorum per lineam;
- ordinem canalium RGB/BGR;
- basim memoriae.

Fenestrale II has dimensiones ut statum graphicum primarium servat.

### Resolutiones probationis canonicae

Minimum functionale:

- `1024×600`

Probationes principales:

- `1280×720`
- `1366×768`
- `1600×900`
- `1920×1080`
- `2560×1440`

Probatio scalae altae:

- `3840×2160`

Nulla ex his resolutionibus in codice ut unica magnitudo supponenda est.

---

## IV. Scala interface

JL-UX mensuras suas ad XCVI DPI et scala C% definit.

Fenestrale II factores sequentes sustinet:

| Scala | Factor | Barra operum |
|---|---:|---:|
| C% | `1.00` | `28 px` |
| CXXV% | `1.25` | `35 px` |
| CL% | `1.50` | `42 px` |
| CC% | `2.00` | `56 px` |

Mensurae semper ex tokenibus JL-UX derivantur; applicatio numeros arbitrarios proprios vitet.

---

## V. Contextus display

Fenestrale II unum descriptorem display praebet conceptu similem:

```text
DISPLAY
    basis_framebuffer
    latitudo
    altitudo
    linea_octeta
    formatum_pixelis
    scala_interface
    basis_compositoris
    basis_frontis
FINIS
```

Applicatio non scribit directe in framebuffer physicum. Omnis pictura transit per compositorium.

---

## VI. Superficies

Omnis fenestra habet superficiem propriam XXXII bit per pixel.

Formatum internum canonicum est RGBA vel BGRA praemultiplicatum, dummodo compositorium unum formatum constanter adhibeat.

Superficies continet:

- latitudinem;
- altitudinem;
- lineam;
- basim memoriae;
- regiones laesas;
- statum opacitatis.

Haec separatio concedit:

- vitrum;
- umbras;
- translucorem;
- compositionem fenestrarum;
- motum sine repictura totius desktop.

---

## VII. Fenestra

Descriptor fenestrae minimum continet:

```text
FENESTRA
    id
    x
    y
    latitudo
    altitudo
    minimum_latitudinis
    minimum_altitudinis
    status
    z
    titulus
    icon
    superficies
    proprietarius
FINIS
```

Status fundamentales:

- activa;
- inactiva;
- minima;
- maxima;
- clausa;
- movetur;
- mutatur mensura.

Nullus numerus sex fenestrarum in contractu publico exstat.

---

## VIII. Ordo profunditatis

Compositorium indicem dynamicum fenestrarum ordine `z` servat.

Clicus in fenestra:

1. fenestram activam facit;
2. eam supra alias ordinarias movet;
3. barram tituli activam pingit;
4. buttonem eius in barra operum activum facit.

Ordines speciales possunt postea addi:

- desktop;
- fenestra ordinaria;
- dialogus parentis;
- notificatio;
- menu;
- cursor.

Cursor semper ultimus componitur.

---

## IX. Motus et mutatio mensurae

Fenestra trahi potest per barram tituli.

Limites mutationis mensurae adsunt in quattuor marginibus et quattuor angulis, quamvis anguli graphice quadrati maneant.

Double clicus in barra tituli maximizationem vel restitutionem facit.

Maximizatio spatium usabile implet, barra operum excepta.

Fenestra minima in desktop non pingitur, sed in barra operum manet.

---

## X. Compositorium

Prima implementatio non requirit effectus graves. Ordo rectus est:

1. imago fundi;
2. icones desktop;
3. fenestrae a posteriore ad anteriorem;
4. umbrae et bordurae;
5. menu et notificationes;
6. barra operum;
7. cursor.

### Regiones laesae

Mutationes non totum scrinium sine causa repingunt.

Compositorium regiones mutatas colligit et solum eas restituit.

Primum stadium potest rectangula laesa simplicia habere; unio regionum subtilior postea additur.

---

## XI. Vitrum JL-UX

Vitrum non significat blur continuum totius systematis.

Prima via nativa:

- titulus caeruleus semiopacus;
- linea lucida superior;
- margo metallicus `1 px`;
- umbra exterior moderata;
- accentus aqua in fenestra activa;
- bronzeum rarum.

Blur background realis est proprietas posterior, non conditio ut Fenestrale II functionetur.

---

## XII. Barra operum

Barra operum est pars Fenestralis II, non applicatio separata fingens dock.

Ordo:

`INITIUM | ACCESSUS CELERES | FENESTRAE | SPATIUM | AREA SYSTEMATIS | TEMPUS`

Proprietates:

- fixa ad imum scrinii per default;
- `28 px` ad C%;
- buttones fenestrarum cum icone et textu;
- fenestra activa clare distincta;
- area systematis compacta;
- nullae icones centraliter coactae;
- nullae pillulae magnae.

---

## XIII. Menu INITIUM

Menu INITIUM retinet philosophiam desktop classicam.

Continet:

- programmata recentia;
- omnia programmata;
- documenta et loca principalia;
- quaesitionem;
- parametros systematis;
- claudere, restituere, dormire si sustentatur.

Menu non occupat totum scrinium.

---

## XIV. Desktop

Desktop non habet numerum fixum iconum.

Positiones iconum servantur in coordinatis logicis. Cum resolutio mutatur, positio intra limites novos coercetur, non deletur.

Icones possunt ordinari:

- libere;
- per reticulum;
- automatice secundum nomen, genus vel tempus.

Wallpaper default nullum textum habet.

---

## XV. Input

Cursor PS/2 aut UEFI ad coordinatas physicas display convertitur antequam eventus fenestris tradantur.

Eventa:

- motus;
- button deorsum;
- button sursum;
- rota;
- clavis deorsum;
- clavis sursum;
- textus.

Eventus ad fenestram activam vel ad obiectum sub cursore diriguntur.

Applicatio non legit directe memoriam globalem muris.

---

## XVI. Compatibilitas hereditatis

Programmata veteris Fenestralis XCV non statim delenda sunt.

Pons hereditarius potest superficiem `320×200` creare et illam intra fenestram modernam ostendere.

Regula:

> Hereditas est applicatio intra Fenestrale II; Fenestrale II non est hereditas ad totum monitor extendita.

Hoc concedit migrationem gradualem Scriptoris, Serpentis et aliorum sine regressione immediate.

---

## XVII. PROGRAMMATA

`PROGRAMMATA I` est prima applicatio quae Fenestrale II ut contractum targetat.

Requirit:

- fenestram mutabilem;
- indicem programmatum volubilem;
- quaesitionem;
- panel laterale;
- actiones `NOVUM`, `EDITE`, `NOMEN`, `DELE`, `AGE`;
- nullum numerum fixum sex locorum.

Cum Fenestrale II nativum paratum erit, prototype HTML non est finis; tantum referentia interactionis est.

---

## XVIII. Gradus implementationis

### Gradus A — framebuffer verus

- removere dependentiam desktop a `320×200` in via UEFI;
- servare dimensiones GOP veras;
- primitivas `PIXEL`, `RECTANGULUM`, `LINEA`, `TEXTUS` cum clipping resolutionis variae facere.

### Gradus B — compositorium

- superficiem RGBA per fenestram;
- compositionem z-order;
- regiones laesas;
- cursor separatam ultimam superficiem.

### Gradus C — fenestrae multiplices

- descriptor dynamicus;
- focus;
- move;
- resize;
- minimize;
- maximize;
- close;
- barra operum synchrona.

### Gradus D — shell Sylvia

- desktop;
- INITIUM;
- system tray;
- notificationes;
- PROGRAMMATA nativum.

### Gradus E — migratio applicationum

- TABULA;
- Scriptor;
- Fasciculi;
- Parametri;
- terminale;
- reliqua.

---

## XIX. Probationes requisitae

Fenestrale II non habetur paratum nisi:

- quinque resolutiones principales sine stretch `320×200` aperiuntur;
- duae fenestrae simul moveri possunt;
- tres fenestrae z-order recte mutant;
- minimizatio et restitutio cum barra operum concordant;
- resize minimum servat;
- focus claviaturae ad fenestram activam transit;
- cursor ad margines 4K recte manet;
- wallpaper sine textu JL-UX ostenditur;
- PROGRAMMATA indicem maiorem quam sex elementa visualiter tractare potest.

---

## XX. Definitio victoriae

Transitus completus est cum user Sylvia OS aperire potest et statim sentit se in desktop moderno pleno esse, non in demonstratione `320×200` amplificata.

Identitas tamen manet:

> **Structura desktop classica. Lux initii annorum MM. Disciplina Latina. Identitas Sylvia.**

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
