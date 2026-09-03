# ATMOS // TERMINAL DEPTH — POC III

**Status: probatum sub Windows vero.**

Probatio III demonstrat VINDEX iam applicationem graphicam Win64 nativam, sine
HTML vel runtime alieno, generare posse.

## Gradus B1 — fenestra et framebuffer

`graphicum.vindex`:

- `user32.dll`, `gdi32.dll` et `kernel32.dll` per FFI VINDEX aperit;
- `CreateWindowExA` ad fenestram Win32 systemicam nativam adhibet;
- framebuffer BGRA 320×180 in memoria VINDEX pingit;
- `StretchDIBits` ad superficiem clientis praesentat;
- aspectum CRT/sonar ATMOS a VINDEX ipso rasterizat.

Certificatio Windows Server 2025 probavit HWND verum et omnes CLXXX lineas
framebufferis a `StretchDIBits` praesentatas.

## Gradus B2 — interactio

Eadem applicatio nunc:

- `PeekMessageA`, `TranslateMessage` et `DispatchMessageA` exercet;
- `GetAsyncKeyState` ad clavem Escape legit;
- `GetCursorPos` et `ScreenToClient` ad murem in coordinatas fenestrae convertit;
- `GetClientRect` ad framebuffer secundum spatium clientis adaptat;
- cursorem radarensem in framebuffer VINDEX pingit;
- in modo visibili usque ad Escape vel clausuram fenestrae currit.

Modus `smoke` easdem APIs inputus/eventorum sub CI exercet sine fenestra visibili.

Nulla HTML, JavaScript, Electron, SDL, C aut C++ runtime ludi adhibetur.

## Usus

```text
atmos_graphicum.exe
```

CI:

```text
atmos_graphicum.exe smoke
```

Hoc POC non est adhuc ludus ATMOS plenus: est fundamentum graphicae et
interactionis native quo logica POC I/II deinde coniungi potest.
