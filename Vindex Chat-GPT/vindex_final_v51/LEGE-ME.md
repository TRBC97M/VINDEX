# VINDEX 0.53 — Nucleus linguae

VINDEX est lingua programmationis Latina quae directe exsecutabilia nativa x86-64 generat. Hic ramus solum nucleum linguae servat: compilatorem auto-hospitem, fontem eius, specificationem et probationes canonicas VINDEX.

## Compilatio

ELF Linux:

```bash
./compilator_vindex programma.vindex programma
chmod +x programma
./programma
```

PE32+ AMD64 Windows:

```bash
./compilator_vindex programma.vindex programma.exe pe
```

Nulla bibliotheca C, GCC, NASM, Python, GTK aut alius compilator ad compilationem ordinariam requiritur.

## Auto-hospitium

Fons canonicus est:

```text
src/compilator_vindex.vindex
```

Binarium seminale est:

```text
compilator_vindex
```

Compilator seminale fontem suum compilat; generationes secunda et tertia byte pro byte congruunt, et generatio secunda cum binario distributo congruit. Sigillum SHA-256 est in `SIGILLA_SHA256.txt`.

## Probationes

`tests/casus/` continet casus semanticos VINDEX. `tests/proba_pe_structuram_053.vindex` structuram PE32+, sectiones, importationes et IAT ipso VINDEX verificat.

Infrastructura GitHub Actions non est pars nuclei; separatim servatur in ramo `infrastructura/vindex-053-ci-purificatio`.

## Ordinatio minima

- `src/compilator_vindex.vindex` — compilator auto-hospes;
- `compilator_vindex` — binarium seminale;
- `tests/` — probationes VINDEX;
- `REFERENTIA.md` — grammatica et semantica canonica;
- `PURIFICATIO-053.md` — relatio purificationis;
- `VERSION` — versio nuclei;
- `SIGILLA_SHA256.txt` — sigillum compilatoris.

Historia Systematis, Officinae, bootstrap Python, instrumentorum migrationis et ceterorum componentium ante purificationem servatur in ramo `archive/vindex-053-avant-purificatio`.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
