# PROBATIONES VINDEX CANONICAE

## Usus

Ex radice `Vindex Chat-GPT/vindex_final_v51`:

```bash
bash tests/run_tests.sh
```

aut:

```bash
make probatio
```

Haec est probatio localis canonica compilatoris VINDEX et fundamentorum Sylviae quae sub Linux sine firmware nec machina externa verificari possunt.

## Quid probatur

### Lingua et interfacies publica

Casus recti per `vindexc` et `compilator_vindex` compilantur atque vere exsequuntur:

- `SALVE` et exitus textus;
- arithmetica et comparationes;
- numeri fluitantes;
- `IMPORTA`;
- structurae et acus;
- recursio;
- `ARGV`;
- lectio partis ordinis `.VXNAT`.

Casus vitiosi confirmant fontem invalidum reici, diagnosticum rectum reddi et exsecutabile imperfectum non relinqui. Interfacies publica `vindexc` et compilator nativus separatim examinantur ubi contractus eorum differunt.

### Auto-hospitium

Compilator canonicus fontem suum iterum componit usque ad generationes `G2` et `G3`.

Probatio requirit:

- `G2 = G3` byte pro byte;
- binarium `compilator_vindex` in repositorio = `G3` byte pro byte.

Ita fons et compilator distributus unum idemque statum linguae repraesentant.

### Logica brevis

`probationes/logica_brevis.vindex` confirmat:

- `&&` dextram partem non aestimare si sinistra falsa est;
- `||` dextram partem non aestimare si sinistra vera est;
- accessum periculosum `CONTENTUM(48)` vere evitari;
- `&&` ante `||` aestimari;
- `&` et `|` operationes bitarias manere.

### PE32+

Compilator idem fontem simplicem in modum `pe` componit. Exitus signum `MZ` et structuram PE32+ x86-64 habere debet.

Executio sub Windows vero a custodia dedicata `VINDEX 0.53 — Win64 R4` probatur.

### Puritas Sylviae

`instrumenta/verifica_puritatem_sylviae.py` confirmat runtime Sylviae post pontem UEFI minimum VINDEX purum manere secundum contractum canonicum praesentem.

### Fenestrale II Purus I

Probatio localis:

- LXXX fenestras in registro dynamico creat atque runtime exsequitur;
- `systema/fenestrale_ii_purus_i.vindex` integrum in ELF64 componit.

Sic mutatio compilatoris non potest Fenestrale dynamicum tacite frangere.

## Probationes dedicatae

Quaedam proprietates machinam aut ambitum specialem requirunt et a GitHub Actions separatim custodiuntur:

- Win64 verum: `VINDEX 0.53 — Win64 R4`;
- Officina Windows nativa: `Officina VINDEX — canonica`;
- Fenestrale et puritas: custodiae Sylviae propriae;
- UEFI/QEMU: custodiae UEFI propriae cum firmware apto.

`make probatio` has custodias non fingit neque veteres pontes alienae linguae adhibet.

## Probationes historicae

`test_systema.py` et `test_officina.py` ad generationes anteriores pertinent. Illae BIOS/VGA, `rectores.S`, pontem UEFI C et veterem Officinam GTK/C examinant; hae viae post purificationem architecturae canonicae non amplius sunt auctoritas praesentis systematis.

Archiva historica manent ad evolutionem intellegendam, sed `run_tests.sh` ea consulto non exsequitur. Non licet probationem canonicam ad architecturam repudiatam redire tantum ut testis vetus virescat.

## Norma

Probatio canonica debet statum hodiernum VINDEX comprobare, non imaginem veterem repositorii conservare.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
