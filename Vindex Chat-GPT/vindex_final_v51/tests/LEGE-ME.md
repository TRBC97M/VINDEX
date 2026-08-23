# Probationes nuclei VINDEX 0.53

Hoc directorium tantum fontes probationum VINDEX et data minima necessaria continet.

## Casus linguae

`casus/` grammatica, numeros, fluitantia, functiones, recursionem, importationes, acus, septem argumenta, `DESINE`, `LEGE/OCTETUS`, diagnostica et fasciculos probat. Fontes `erratum_*.vindex` consulto invalidi sunt.

Compilatio unius casus directe fit:

```text
./compilator_vindex tests/casus/salve.vindex /tmp/salve
chmod +x /tmp/salve
/tmp/salve
```

## Verificatio PE

`proba_pe_structuram_053.vindex` est verificator PE32+ AMD64 **in VINDEX scriptus**. Signaturas MZ/PE, sectiones `.text`/`.idata`, directorium importationum, IAT, septem API KERNEL32 requisitas atque vocationes RIP-relativas `FF 15` inspicit.

```text
./compilator_vindex tests/proba_pe_structuram_053.vindex /tmp/proba_pe
chmod +x /tmp/proba_pe
/tmp/proba_pe programma.exe
```

Python, C et Shell non sunt pars huius suite canonicae. Orchestratio GitHub Actions externa tantum est et codicem linguae non implementat.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
