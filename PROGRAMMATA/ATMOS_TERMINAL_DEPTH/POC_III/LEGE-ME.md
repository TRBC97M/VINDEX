# ATMOS // TERMINAL DEPTH — POC III

Probatio III primum backend applicationis graphicae Win64 nativae VINDEX exercet.

## Gradus B1

`graphicum.vindex`:

- `user32.dll`, `gdi32.dll` et `kernel32.dll` per FFI VINDEX aperit;
- `CreateWindowExA` ad fenestram Win32 systemicam nativam adhibet;
- framebuffer BGRA 320×180 in memoria VINDEX pingit;
- `StretchDIBits` ad 800×500 praesentat;
- modum sine argumento visibilem et modum `smoke` CI occultum praebet.

Nulla HTML, JavaScript, Electron, SDL, C aut C++ runtime ludi adhibetur.

### Usus

```text
atmos_graphicum.exe
```

CI:

```text
atmos_graphicum.exe smoke
```

Status huius documenti mutandus est in **probatum** tantum post exsecutionem
Windows veram workflow POC III.
