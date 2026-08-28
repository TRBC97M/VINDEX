# JL-UX COMPONENTES I

**Sylvia OS — Regulae componentium communium**

Status: **NORMATIVUS**  
Gradus: **P16-X**

Hoc documentum definit quomodo elementa interactionis Sylviae se gerere et apparere debent. Finis est ut applicationes non singulae propriam dialectum visualem fingant.

## I. Status communes

Ubi sensum habent, componentes hos status distinguere debent:

1. normalis;
2. hover;
3. pressus;
4. focus;
5. selectus vel activus;
6. inactivus;
7. indisponibilis;
8. destructivus.

Mutatio status non debet unico pixel incerto niti. Saltem duo signa visualia praeferuntur.

## II. Bulla ordinaria

### Normalis

- Metallum Frigidum vel Gray-Blue;
- textus Ivory/Graphite secundum fundum;
- limes Silver;
- gradientia subtilis.

### Hover

- lumen Aqua Light;
- contrastus paulo maior;
- geometria invariata.

### Pressa

- gradientia inversa vel obscurata;
- contentum 0–1 px visive depressum si implementatione facile;
- nullus motus hitbox.

### Default/primaria

- focus Cyan/Aqua vel Bronze secundum contextum;
- non debet totum dialogum dominari colore saturato.

### Destructiva

- Imperial Crimson;
- textus clarus;
- usus tantum pro actione destructiva vera.

## III. Checkbox

- quadrum clarum et compactum;
- limes Silver/Gray-Blue;
- check Cyan Glow vel Laurel Green secundum semanticam;
- hover Aqua Light;
- disabled desaturatum.

Check non debet solum colore significari; glyphum visibile manet.

## IV. Radio button

- circulus metallicus;
- punctum activum Cyan/Aqua;
- label Graphite vel Ivory;
- hover per lumen subtile;
- selectio semper geometrice manifesta.

## V. Text field

### Normalis

- corpus Ivory;
- limes Silver;
- textus Graphite;
- placeholder Gray-Blue.

### Focus

- limes Cyan Glow vel Aqua Light;
- possibile signum Bronze parvum ubi shell contextus id postulat;
- caret clare visibilis.

### Error

- Imperial Crimson ad limitem vel iconam;
- textus utilis erroris, non rubor solus.

## VI. Dropdown

- eadem materia ac text field/button;
- sagitta clara;
- menu apertum in plano interactionis cum umbra externa;
- item hover Aqua/Bronze subtiliter;
- item selectus evidenter distinctus.

## VII. Tab

### Inactivus

- Metallum Frigidum/Gray-Blue;
- textus Silver/Graphite;
- nexus cum pane minus fortis.

### Activus

- corpus propius Ivory vel Vitrum Minerale;
- linea Bronze vel Cyan ad oram;
- continuum visuale cum pane contenti.

Tab activus debet videri pars pane, non bulla separata casu.

## VIII. Scrollbar

- track quietus Graphite/Silver secundum contextum;
- thumb Metallum Frigidum;
- hover Aqua Light;
- pressus Gray-Blue obscurior;
- magnitudo non nimis angusta ad usum desktop.

## IX. Progress bar

- track Graphite/Gray-Blue;
- progressus Cyan Glow cum Aqua highlight;
- Laurel Green admittitur si progressus completionem validam significat;
- numerus percentus optionalis sed legibilis.

Animationem infinitam tantum pro statu vere indeterminato adhibere licet.

## X. Toolbar

- materialis unitas cum fenestra;
- grupos actionum per spatia/separatora distinguere;
- icona + label ubi cognitio usoris prodest;
- hover et pressed communes;
- actio destructiva non inter normales abscondenda.

Toolbar non debet densitatem extremae applicationis alienae imitari. Sylvia spatio et hierarchia utitur.

## XI. Sidebar

- fundum Gray-Blue lucidum, Silver vel Ivory secundum applicationem;
- item selectus cum accentu Aqua/Bronze;
- iconographia constans;
- sectiones clare titulatae;
- separatora discreta.

## XII. List et table

- corpus Ivory;
- caput Silver/Gray-Blue;
- row hover Aqua Light tenuissimum;
- selectio evidens sed textum non mergens;
- zebra stripes tantum si densitas datae eas requirit;
- lineae grid non debent dominari.

## XIII. Status bar

- Metallum Frigidum vel Gray-Blue obscuratum;
- textus secundarius clare legibilis;
- informationes separatae per spatia vel limites;
- status Laurel Green/Crimson secundum semanticam.

## XIV. Dialog

- Vitrum/Metallum in chrome;
- corpus Ivory;
- una actio primaria clara;
- destructiva separata;
- focus initialis visibilis;
- umbra planum interactionis indicans.

## XV. Tooltip

- fundum Graphite;
- textus Ivory;
- limes Silver/Aqua subtilis;
- nulla mora nimis longa;
- non debet actionem ipsam occultare.

## XVI. Icona in componente

- iconographia canonica communis adhibenda;
- iconam non pingere in stylo singulari pro uno button;
- statum disabled per luminantiam/contrastum, non deformando glyphum;
- 16/24 px ad controles; 32/48 px ad tiles et launchers.

## XVII. Mensurae et spatium

JL-UX non canonizat hic unum systema pixelorum rigidum, sed has leges imponit:

- target click non debet esse absurdum parvum;
- margines inter textum et limites constanter apparent;
- textus non tangit iconam neque border;
- series componentium eandem altitudinem visualem servant;
- densitas ad desktop 1280×800 et maiores resolutiones utilis manet.

## XVIII. Geometria contra picturam

Gradus visuales primum picturam mutare debent, non semantica interactionis, nisi PR expresse aliter declarat.

Si hitbox mutatur:

- mutatio documentanda est;
- probatio interactionis renovanda est;
- regressio non celanda est.

## XIX. Responsivitas

Nullus componentis effectus est acceptabilis si redraw adeo tardat ut framebuffer medium inter statum captetur. Praeferuntur:

- gradientiae per lineas;
- alpha localis;
- umbrae ad oras;
- caches/rastera ubi utile.

## XX. Criterium adoptionis

Componens JL-UX communis adoptatus dicitur cum:

1. status eius principales distincti sunt;
2. palette canonica utitur;
3. materialem familiam declarat;
4. in duabus saltem applicationibus reutilis est vel ad talem reutilitatem paratus;
5. framebuffer verus effectum probare potest;
6. caret imitatione ad-hoc quae dialectum alienam introducat.
