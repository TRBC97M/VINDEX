# ATMOS Terminal Depth — Probatio III: Graphica Win64 nativa

## Propositum

Probatio III transit a terminali ad applicationem graphicam Win64 nativam. Norma
manet: facultas utilis aliis programmatibus in VINDEX generale elevatur, non in
hack privatum Atmos.

## Gradus A — FFI Win64

Ante USER32/GDI32 directe in backend figere, VINDEX accipit fundamentum generale:

- `WIN_DLL_APERI(nomen)` — bibliothecam DLL per `LoadLibraryA` aperit;
- `WIN_DLL_SYMBOLUM(modulus, nomen)` — symbolum per `GetProcAddress` invenit;
- `ABI_MSX64_VOCA16(functio, argumenta)` — punctatorem functionis secundum ABI
  Microsoft x64 vocat, usque ad XVI argumentis integer/pointer.

Backend PE duas importationes KERNEL32 novas tantum addit: `LoadLibraryA` et
`GetProcAddress`. USER32, GDI32 et bibliothecae futurae dynamice resolvi possunt.
Ita eadem facultas ad graphica, audio, OpenGL, instrumenta et bibliothecas tertias
partes utilis erit.

Probatio `proba_win32_ffi.vindex` sub Windows vero `user32.dll` aperit,
`GetSystemMetrics` resolvit et `SM_CXSCREEN` legit. Hoc primum contractum FFI
certificat antequam fenestra Atmos construitur.

## Gradus B — fenestra et framebuffer

Post Gradum A viridem, POC III debet:

1. `CreateWindowExA` ex USER32 dynamice resolvere;
2. fenestram top-level nativam creare;
3. framebuffer BGRA in memoria VINDEX possidere;
4. per GDI `StretchDIBits` illum in fenestra praesentare;
5. eventa Windows sine callback privato tractare, classi systemica et
   `PeekMessageA` utendo;
6. clavem Escape et positionem muris legere;
7. modum `smoke` pro CI et modum visibilem pro usu humano praebere.

Hoc documentum facultates futuras non quasi iam probatas declarat. Gradus A et B
separatim certificantur.
