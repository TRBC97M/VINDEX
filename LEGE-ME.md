# VINDEX 0.53 — Nucleus linguae

VINDEX est lingua programmationis Latina quae directe exsecutabilia nativa x86-64 generat. Hic ramus solum nucleum linguae servat: compilatorem auto-hospitem, fontem eius, referentiam et probationes canonicas VINDEX.

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

Fons canonicus est `src/compilator_vindex.vindex`; binarium seminale est `compilator_vindex`. Compilator seminale fontem suum compilat, generationes secunda et tertia byte pro byte congruunt, atque generatio secunda cum binario distributo congruit. Sigillum SHA-256 est in `SIGILLA_SHA256.txt`.

## Probationes

`tests/casus/` continet contractum semanticum minimum. `tests/compara_fasciculos_053.vindex` comparationem byte pro byte ipso VINDEX facit. `tests/proba_pe_structuram_053.vindex` structuram PE32+, sectiones, importationes et IAT ipso VINDEX verificat.

Infrastructura GitHub Actions non est pars nuclei; separatim servatur in ramo `infrastructura/vindex-053-ci-purificatio`.

## Ordinatio minima

- `src/compilator_vindex.vindex` — compilator auto-hospes;
- `compilator_vindex` — binarium seminale;
- `tests/` — contractus et verificatores VINDEX;
- `REFERENTIA.md` — grammatica, semantica et limites canonici;
- `VERSION` — versio nuclei;
- `SIGILLA_SHA256.txt` — sigillum compilatoris.

Historia ante purificationem servatur in ramo `archive/vindex-053-avant-purificatio`.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
