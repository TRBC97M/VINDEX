# Probationes VINDEX

Omnes probationes e radice incipe:

```bash
./tests/run_tests.sh
# aut
make probatio
```

Casus recti exitum et statum exsecutabilium probant. Casus vitiosi confirmant
`vindexc` et compilatorem nativum fontem invalidum reicere neque ELF
imperfectum relinquere. Denique compilator ab Python restituitur et punctum
fixum nativum verificatur.
Casus `vxnat-partem` quinque litteras a positione septima ordinis legit et
valores `SALVE` confirmat; hic regressio acuminis vitiosi versionis 0.49 est.

Octo probationes Graphicae confirmant:

- fontem VINDEX idem ELF initiatoris distributi reproducere;
- pontem GTK declarativum omnia symbola necessaria invenire;
- duas formas applicationum rectas esse;
- bibliothecam graphicam eventa Latina praebere;
- logicam VINDEX eventum graphicum accipere, compilare et exsequi;
- alteram applicationem nomen accipere et salutationem in VINDEX componere;
- installationem Fedora fenestram sine terminali declarare;
- interfaciem interretialem et terminalem omnino abesse.

Sola Officina:

```bash
make probatio-officina
```

Duodeviginti probationes Systematis confirmant:

- fontem nuclei idem ELF distributum reproducere;
- ELF unum segmentum ad basim `0x400000` habere;
- nucleum memoriam VGA `0xA0000` et formam BIOS `0x8000` directe attingere;
- sectorem BIOS 512 octeta et signum `55aa` habere;
- modum VGA 320×200, paginationem et modum longum contineri;
- rectores IRQ0, IRQ1, IRQ12, PIT, circulum claviaturae et PS/2 continere;
- omnes inscriptiones Fenestrales Latinas esse;
- `SERVA`, `APERI`, `NOVUM`, `NOMEN`, `DELE`, `FASCICULI` et formatum internum
  sex documentorum atque sex programmatum VINDEX in nucleo adesse;
- nullam functionem nuclei conventionem sex argumentorum excedere;
- `APERI` in Fasciculis ingressum electum sine lectione disci supervacua
  directe ad Scriptorem transferre;
- Scriptorem II documenta 4095 octetorum, cursorem mobilem, volutationem verticalem,
  nomen activum, migrationem voluminis et confirmationem deletionis continere;
- `PROGRAMMATA` fasciculos `.VXNAT` in regione separata creare, nominare, in
  Scriptore mutare atque exempla `SALVE.VXNAT` et `TABULA.VXNAT` instituere;
- programmata
  mandata `SCRIBE`, `COLOR`, `LOCUS`, `RECTANGULUM` et `MARGO` directe exsequi;
- pontem UEFI volumen opacum 32 KiB legere, scribere atque expurgare;
- imaginem UEFI fasciculum praeparatum `VINDEX.FS` in FAT32 continere;
- secundam partitionem GPT signo `VINDEXV0` et volumine vacuo contineri;
- rectorem binalem scribere, expurgare, relegere, initium novum simulare atque
  corruptionem pro successu numquam accipere;
- imaginem sectorem, nucleum, textus et rectores recto loco servare;
- reconstructionem imaginem byte pro byte identicam creare.

Si QEMU adest, probatio addita confirmat nucleum currere neque triplici errato
statim terminari.

Fontes `casus/erratum_*.vindex` consulto invalidi sunt.
