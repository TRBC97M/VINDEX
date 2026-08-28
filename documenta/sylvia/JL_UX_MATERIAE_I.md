# JL-UX MATERIAE I

**Sylvia OS — Materiae visuales normativae**

Status: **NORMATIVUS**  
Gradus: **P16-X**

JL-UX superficiem non ut campum coloris tantum, sed ut materiam perceptibilem tractat. Quattuor materiae canonicae sunt.

## I. Vitrum Minerale

### Intentio

Vitrum Minerale significat technologiam lucidam, profunditatem et precisionem.

### Ubi adhibetur

- tituli fenestrarum;
- capita INITII;
- panes selecti;
- highlight toolbar;
- regiones preview obscuriores;
- superficies activae ubi translucida species utilis est.

### Signa visualia

- gradientia frigida;
- linea luminis Aqua Light;
- reflectio alba/ivorea parva;
- margo Silver vel Bronze secundum focus;
- umbra moderata;
- alpha parvus et localis.

### Prohibetur

- alpha per totam fenestram magnam sine causa;
- blur fictus qui perfunctionem destruit;
- translucida superficies sub textu quae legibilitatem minuit;
- lumen cyanum ubique.

## II. Ebur Enamelatum

### Intentio

Ebur Enamelatum est materia contenti: clara, calma, nitida sed non sterilis.

### Ubi adhibetur

- corpora applicationum;
- panes documentorum;
- lists et tables;
- regiones editorum;
- dialogs lucidi;
- contentum exploratoris fasciculorum.

### Signa visualia

- basis Ivory;
- gradientia subtilissima;
- separatora Silver;
- umbra interior minima ubi hierarchia requiritur;
- textus Graphite;
- selectio per Gray-Blue/Aqua/Bronze, non per saturatam superficiem magnam.

### Prohibetur

- album purum maximum sine variatione;
- textura fortis quae textum turbat;
- contrastus nimis parvus inter contentum et separatora.

## III. Metallum Frigidum

### Intentio

Metallum Frigidum significat structuram, firmitatem et instrumentum.

### Ubi adhibetur

- margines fenestrarum;
- toolbar;
- scrollbar;
- separatora;
- bullae systematis;
- regiones status;
- controles compacti.

### Signa visualia

- Silver + Cool Gray-Blue;
- gradientia verticalis vel horizontalis parva;
- linea superior clarior;
- linea inferior obscurior;
- focus distinctus Bronze/Aqua.

### Prohibetur

- specularitas nimis fortis;
- chrome griseum sine identitate;
- margines nimis crassi ad imitandum vetus skeuomorphismus.

## IV. Lumen Molle

### Intentio

Lumen Molle non est materia physica sed effectus communis qui alias materias coniungit.

### Ubi adhibetur

- focus;
- hover;
- progressus;
- wallpaper;
- logo;
- reflexus;
- transitus inter regiones.

### Signa visualia

- Aqua Light ad highlight;
- Cyan Glow ad punctum energicum;
- Ivory ad reflexum calidum;
- opacity moderata;
- gradientia longa et lenis in wallpaper, brevis et subtilis in UI.

### Prohibetur

- glow magnus circa omnem rem;
- textus cyanus lucens per paginas integras;
- effectus qui cursor vel iconas occultant.

## V. Compositio materialis per elementum

### Fenestra activa

- umbra externa Graphite;
- margo Metallum Frigidum;
- titulus Vitrum Minerale;
- linea focus Subtle Bronze;
- reflexus Aqua Light;
- corpus Ebur Enamelatum vel materia applicationis propria.

### Fenestra inactiva

- eadem structura;
- minus Bronze;
- minus Aqua;
- Gray-Blue/Silver desaturatum;
- contrastus adhuc sufficiens.

### INITIUM

- caput Vitrum Minerale;
- corpus Ebur Enamelatum;
- separatora Metallum Frigidum;
- hover cum Luminis Mollis signo et linea Bronze.

### Taskbar

- basis Graphite + Cool Gray-Blue;
- metallum obscurum;
- focus Bronze;
- lumen Aqua;
- fenestra activa plus vitrea, inactiva plus metallica.

### TERMINALE

- Graphite dominans;
- textus Ivory/Silver;
- prompt vel status Aqua/Cyan/Laurel secundum semanticam;
- chrome externum JL-UX commune.

### OFFICINA

- contentum Ebur Enamelatum vel variante frigida;
- toolbar Metallum Frigidum;
- focus/editor cursor Cyan/Aqua;
- status Bronze/Laurel ubi semantice utile.

## VI. Profunditas

JL-UX utitur profunditate tribus gradibus:

1. **planum basis** — wallpaper/bureau;
2. **planum operis** — fenestrae, menus, panes;
3. **planum interactionis** — dropdown, dialog, tooltip, drag object.

Umbra debet hanc hierarchiam explicare, non ornamentum esse.

## VII. Ordo umbrarum

- umbrae ad oras externae praeferuntur;
- thickness modica;
- opacity gradatim minuitur;
- alpha compositio per regiones enormes vitatur;
- shadow non mutat hitbox.

Experientia P16-VIII est lex perfunctionis: effectus visualis qui redraw sub QEMU nimis tardum facit reiciendus est etiam si pulchrior videtur.

## VIII. Reflexus et highlight

Highlight debet unam causam habere:

- directionem luminis;
- focus;
- materialem separationem.

Duplex vel triplex highlight sine causa evitatur.

## IX. Scala

Materia ad magnitudinem elementi adaptatur.

- In iconis 16 px, signa materiae simplicissima sunt.
- In bullis 24–40 px, gradientia subtilis sufficit.
- In titulis fenestrarum, vitrum et reflexus clarius apparere possunt.
- In wallpaper, lumen et profunditas amplissime exprimi possunt.

## X. Probatio runtime

Quotiens nova materia implementatur, probator framebuffer debet saltem comprobare:

- gradientiam realem;
- distinctionem status;
- umbram vel highlight ubi norma id postulat;
- invarianta geometriae;
- responsivitatem sine mora artificiose aucta.
