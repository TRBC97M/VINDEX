# ATMOS // TERMINAL DEPTH — NATIVUM

**Status:** fundamentum novum GUI/DIB technice probatum; probationem humanam expectat ante progressionem gameplay.  
**Basis:** `main` post POC V (`e0bff270…`).

`NATIVUM/` est transpositio activa ludi ATMOS in VINDEX purum.

POC I–V manent in repositorio ut probationes historicae facultatum linguae. Experimenta Stabilitas/POC VI/POC VII in PR #182 scientiam utilem dederunt sed **non sunt fundamentum huius implementationis**.

## Lex principalis

Ludus runtime 100% VINDEX est.

Permittuntur:

- bibliothecae VINDEX canonicae;
- API systematis Win32 vocatae per FFI VINDEX;
- asseta data a VINDEX lecta/composita;
- instrumenta CI extra runtime.

Non permittuntur in runtime:

- HTML / JavaScript / WebView / Electron;
- C / C++ / C# / Rust;
- Python;
- assembler externus;
- SDL aut alius runtime alienus;
- importatio codicis gameplay ex POC I–VII.

Fasciculus HTML originalis est **referentia morum**, non pars runtime nec fons qui includitur.

## Regula graphica absoluta

Una frame habet unum fontem veritatis:

`status ludi → compositor VINDEX → pixels DIB BGRA scripti a VINDEX → una praesentatio Win32`

Textus, sonar, HUD, iconographia, overlays et effectus omnes in eadem memoria bitmap componuntur. `TextOutA` aut alia pictura directa super HDC post compositionem non adhibetur.

Haec regula directe removet genus defectus POC VI/VII ubi framebuffer et textus GDI geometria diversa post resize habebant.

## Applicatio Windows vera

VINDEX nunc targetum `gui` possidet. NATIVUM eo compilatur:

```text
compilator_vindex ludus.vindex ATMOS_NATIVUM.exe gui
```

Productum est PE32+ `Windows GUI`, non `Windows CUI`. Runtime Win64 idem ac target `pe` manet (`VirtualAlloc`, ABI Microsoft x64, `ExitProcess`), sed Windows nullam consolam CMD creat.

CI separat et verificat:

- `pe` → Windows CUI;
- `gui` → Windows GUI;
- `uefi` → EFI application.

Minimum GUI VINDEX et ATMOS GUI ambo sub Windows vero cum exitus 0 probati sunt.

## Renderer DIB

Canvas VINDEX involvit bits realis DIB Section Win32. VINDEX scribit ipsa pixela; Windows bitmap finalem tantum praesentat. Smoke Windows etiam pixelum e fenestra post presentationem legit, ne superficies alba/vacua falso pro successu habeatur.

## Ordo reconstructionis

1. **fenestra GUI vera + canvas DIB VINDEX unicus + typographia VINDEX** — technice probatum, test humanum pendet;
2. sonar et coordinatae mundi;
3. navigatio continua per clic sonaris;
4. bathymetria et regiones;
5. minera continua et zonae depositi;
6. contactus/NPC/stationes;
7. dock/economia/cargo/upgrades;
8. contractus, factiones, pugna et bases;
9. save/load integrum et polish.

Nullus gradus contentum novum accipit antequam fundamentum eius sub Windows vero et test humano stabile sit.
