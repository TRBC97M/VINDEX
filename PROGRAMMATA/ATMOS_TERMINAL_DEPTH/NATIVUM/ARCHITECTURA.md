# ATMOS NATIVUM — Architectura

## I. Separatio ab experimentis

`NATIVUM/` nullum `IMPORTA` ad `POC_I`, `POC_II`, `POC_III`, `POC_IV`, `POC_V`, `POC_VI`, `POC_VII` nec ad módulos gameplay experimentales facit.

Scientia experimentorum portari potest; codex eorum non est fundamentum implicitum.

## II. HTML ut specificatio

Versio HTML ab auctore tradita describit mores ludi qui restituendi sunt. Transpositio fit subsystemate post subsystema, VINDEX proprio codice.

Contractus fundamentales observati:

- sonar est principale instrumentum navigationis;
- clic sonaris convertitur ad coordinatas mundi;
- navis progressive ad destinationem movetur;
- profunditas sequitur mundum/bathymetriam, non mandatum DOWN/UP;
- nodus resource est zona spatialis: APPROACH → ingressus in zonam → extractio continua;
- contactus, stationes et bases sunt entia in coordinatis mundi;
- mundus sistitur dum menu/overlay qui simulationem suspendit apertus est;
- resource drain, simulation mundi et rendering cadentias separatas habent.

## III. Renderer

### Una compositio

Omnia elementa visualia fiunt in superficie BGRA VINDEX:

- background;
- sonar;
- routes;
- entia;
- HUD;
- textus;
- menus/overlays;
- cursor/selectiones ludicas si necessarium.

Post compositionem fit **una** praesentatio `StretchDIBits` ad client rect actualem.

Nulla API GDI textus directe in fenestra scribit. HDC est solum destinatio finalis praesentandi.

### Resize

Canvas logicus manet coherens. Client rect Win32 singulis mutationibus mensuratur et praesentatio totam destinationem operit. Input muris e coordinatis clientis ad canvas logicum convertitur ante hit-test.

## IV. Platforma Win32

Fenestra vera classe propria Win32 utitur (`RegisterClassExA`, `DefWindowProcA`, `CreateWindowExA`). Non utitur classe `STATIC` ut fenestra principali.

Windows administrat non-client area: move, resize, minimize, maximize et close. Ludus pumpam nuntiorum exercet et exit si fenestra destructa est.

## V. Tempus et simulation

Loop visualis et simulationis distinguuntur. Cadentiae primae:

- render/input: frequens;
- motus/simulatio mundi: gradus fixus;
- drain resource: cadentia lenta;
- autosave: eventibus significantibus vel intervallo moderato.

Simulationem pause debet menu/overlay canonicus.

## VI. Puritas — Passe Génocidaire

CI debet probare:

1. omnes fontes runtime in `NATIVUM/` esse `.vindex` vel data non-exsecutoria;
2. nulla importatio ad HTML/JS/C/C++/C#/Rust/Python/ASM;
3. nulla importatio ad gameplay POC historicum;
4. compilator auto-hospes VINDEX NATIVUM compilare posse;
5. PE nullum CRT/.NET/runtime alienum importare;
6. executabile idem sub Windows vero currere.

YAML, shell et PowerShell CI instrumenta sunt, non runtime ludi, et in artefacto usuario non includuntur.
