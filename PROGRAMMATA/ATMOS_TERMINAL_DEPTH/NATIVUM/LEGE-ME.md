# ATMOS // TERMINAL DEPTH — NATIVUM

**Status:** linea activa reconstructionis.  
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

`status ludi → compositor VINDEX → framebuffer BGRA VINDEX → una praesentatio Win32`

Textus, sonar, HUD, iconographia, overlays et effectus omnes in eodem framebuffer componuntur. `TextOutA` aut alia pictura directa super HDC post compositionem non adhibetur.

Haec regula directe removet genus defectus POC VI/VII ubi framebuffer et textus GDI geometria diversa post resize habebant.

## Ordo reconstructionis

1. fenestra Win32 vera et ansa eventuum;
2. canvas VINDEX unicus + typographia VINDEX in framebuffer;
3. sonar et coordinatae mundi;
4. navigatio continua per clic sonaris;
5. bathymetria et regiones;
6. minera continua et zonae depositi;
7. contactus/NPC/stationes;
8. dock/economia/cargo/upgrades;
9. contractus, factiones, pugna et bases;
10. save/load integrum et polish.

Nullus gradus contentum novum accipit antequam fundamentum eius sub Windows vero et test humano stabile sit.
