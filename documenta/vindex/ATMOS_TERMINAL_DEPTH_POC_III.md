# ATMOS Terminal Depth — Probatio III: Graphica Win64 nativa

## Status

**Gradus A, B1 et B2 probati sunt sub Windows vero.**

Probatio III transit a terminali ad applicationem graphicam Win64 nativam. Norma
manet: facultas utilis aliis programmatibus in VINDEX generale elevatur, non in
hack privatum ATMOS.

## Gradus A — FFI Win64

VINDEX nunc fundamentum generale habet:

- `WIN_DLL_APERI(nomen)` — bibliothecam DLL per `LoadLibraryA` aperit;
- `WIN_DLL_SYMBOLUM(modulus, nomen)` — symbolum per `GetProcAddress` invenit;
- `ABI_MSX64_VOCA16(functio, argumenta)` — punctatorem functionis secundum ABI
  Microsoft x64 vocat, usque ad XVI argumentis integer/pointer.

Backend PE duas importationes KERNEL32 novas tantum addit: `LoadLibraryA` et
`GetProcAddress`. USER32, GDI32 et bibliothecae futurae dynamice resolvi possunt.

Probatio Windows vera certificavit:

- `GetSystemMetrics` cum I argumento;
- `CreateWindowExA` cum XII argumentis et HWND vero;
- `CreateFontA` cum XIV argumentis;
- conversionem `TEXTUS` VINDEX ad LPCSTR;
- helperem `MSX64_ARGUMENTA_VACUA` cum arithmetica typata `ACUS<NUMERUS>`.

Per hanc probationem duo vitia generalia VINDEX inventa et correcta sunt:

1. litteralia `TEXTUS` PE sedem ELF `0x400000` adhuc adhibebant;
2. helper argumentorum indicem `ACUS<NUMERUS>` bis per VIII multiplicabat et
   memoriam extra tabulam scribebat.

## Gradus B1 — fenestra et framebuffer

`PROGRAMMATA/ATMOS_TERMINAL_DEPTH/POC_III/graphicum.vindex` iam:

1. `CreateWindowExA` dynamice resolvit;
2. fenestram top-level nativam creat;
3. framebuffer BGRA 320×180 in memoria VINDEX possidet;
4. aspectum CRT/sonar sine bibliotheca graphica externa rasterizat;
5. per GDI `StretchDIBits` illum in superficie clientis praesentat.

Certificatio Windows Server 2025 reddidit HWND positivum et `StretchDIBits = 180`,
id est omnes CLXXX lineas fontis praesentatas.

## Gradus B2 — eventa, clavis et mus

Versio interactiva addit:

- `PeekMessageA`, `TranslateMessage`, `DispatchMessageA`;
- `GetAsyncKeyState(VK_ESCAPE)`;
- `GetCursorPos`;
- `ScreenToClient`;
- `GetClientRect`;
- `IsWindow`;
- cyclum circiter LX tabularum per secundum cum `Sleep(16)`.

Mus in coordinatas framebuffer 320×180 convertitur et crucem viridem radarensem
movet. Escape vel clausura fenestrae cyclum terminat. Modus `smoke` easdem APIs
inputus/eventorum exercet; lectura cursoris vel conversio ad clientem si deficit,
probatio statim cum statu non-nullo desinit.

## Significatio

POC III non est adhuc ludus ATMOS plenus. Sed probat VINDEX iam posse unum `.exe`
Win64 nativum producere quod:

- fenestram possidet;
- graphica propria pingit;
- framebuffer praesentat;
- eventa Windows tractat;
- clavem legit;
- murem legit.

Proximus gradus logicus est statum et decisiones ludi ex POC I/II huic frontend
nativo coniungere, non novum backend graphicum denuo construere.
