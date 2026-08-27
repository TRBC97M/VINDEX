# TERMINALE II — Historia et transcriptum dynamicum

## Status

**P17 — incrementum II.**  
**Praerequisitum:** `TERMINALE_I.md`, Fenestrale II Purus, catalogus applicationum P16-IV.  
**Finis:** TERMINALE a campo unius responsi ad sessionem textualem persistentem intra vitam clientis provehere, sine simulando processuum aut fasciculorum facultates nondum canonicas.

---

## I. Principium

P17-I probavit catenam realem:

```text
clavis UEFI → focus Fenestralis → coda eventuum → cliens TERMINALE → framebuffer
```

P17-II eandem catenam retinet et duas res addit:

1. **historiam mandatorum dynamicam**, navigabilem sagittis `↑` et `↓`;
2. **transcriptum dynamicum**, navigabilem `PageUp` et `PageDown`.

Nulla capacitas parva fixa historiae vel transcripti in contractu ponitur. Singula mandata et ingressus transcripti nodos memoriae VINDEX accipiunt.

---

## II. Status clientis

Status TERMINALIS nunc continet:

```text
+0   descriptor lineae praesentis
+8   responsum novissimum
+16  numerus mandatorum actorum
+24  caput historiae
+32  cursor historiae
+40  caput transcripti
+48  finis transcripti
+56  numerus ingressuum transcripti
+64  distantia scrollback a fine
```

Haec structura capacitatem historiae non definit. Incrementum memoriae fit per nodos `RESERVA_OCTETA`.

### Nodus historiae

```text
+0   descriptor TEXTUS mandati
+8   nodus antiquior
+16  nodus recentior
```

### Nodus transcripti

```text
+0   genus: 1 = mandatum, 2 = responsum
+8   datum: descriptor mandati vel numerus responsi
+16  nodus antiquior
+24  nodus recentior
```

---

## III. Historia mandatorum

Mandatum non vacuum ante purgationem lineae in historia inseritur.

- `↑` a linea praesentis temporis ad mandatum recentissimum transit;
- `↑` iteratum ad mandata antiquiora procedit;
- `↓` ad recentiora redit;
- post mandatum recentissimum `↓` lineam vacuam restituit;
- editio manualis lineae cursorem historiae dimittit;
- historia post `PURGA` manet.

Historia non est series magnitudine XXXII, LXIV vel alio numero parvo definita. Probatio canonica plura mandata addit et nodos sequitur.

---

## IV. Transcriptum et scrollback

Mandatum exsecutum et responsum eius transcriptum crescunt. Renderer solum tot ingressus pingit quot superficies visibiles recipere potest; **numerus visibilis non est capacitas datorum**.

`PageUp` distantiam a fine transcripti auget. `PageDown` eam minuit. Distantia semper ad fines reales transcripti coercetur.

Cum novum mandatum exsequitur, visus ad finem recentissimum redit.

`PURGA`:

- transcriptum visibile et indices eius evacuat;
- offset scrollback ad nullum reddit;
- historiam mandatorum **non** delet.

Hoc discrimen intentionaliter mores terminalium ordinariorum sequitur.

---

## V. Distributio scan-codicum

P17-I tantum `UnicodeChar` ad clientem mittebat. P17-II eventum claviaturae utrumque portat:

- `scan` UEFI;
- `unicode` UEFI.

Fenestrale clientem fenestrae focalis ex registro clientium cognoscit.

Si genus clientis est `3` (`TERMINALE`), hi scan-codices ad clientem mittuntur:

- `1` — sursum / historia antiquior;
- `2` — deorsum / historia recentior;
- `9` — PageUp / scrollback sursum;
- `10` — PageDown / scrollback deorsum.

Textus Unicode ad eundem clientem per codam eventuum transit.

PROGRAMMATA et TABULA mores Fenestralis anteriores servant; sagittae eorum fenestram movere possunt. Itaque P17-II navigationem TERMINALIS addit sine contractum ceterorum clientium abrumpendo.

---

## VI. Mandata interna

Mandata P17-I manent:

- `SALVE`;
- `VERSIO`;
- `AUXILIUM`;
- `PURGA`.

Mandatum ignotum responsum `MANDATUM NON INVENTUM.` reddit.

P17-II consulto **non** introducit mandatum fictum ad processum externum exsequendum. Sylvia nondum contractum processuum, filesystematis et loaderis applicationum satis maturum habet ut shell externum honeste promittatur.

Cum illa strata canonica erunt, TERMINALE eis coniungetur potius quam simulationem localem creare.

---

## VII. Probationes

### Probatio nativa

`probationes/terminale_ii.vindex` verificat:

- `SALVE` et `VERSIO` in historia;
- navigationem `↑ ↑ ↓ ↓`;
- XL mandata addita sine capacitate parva fixa;
- LXXXIV ingressus transcripti;
- PageUp usque ad finem realem et PageDown;
- `PURGA` transcriptum delere;
- historiam post `PURGA` servari;
- numerum mandatorum P17-I congruum manere.

P17-I separatim manet in suite, ut regressiones lineae UTF-8 dynamicae et backspace scalaris non occultentur.

### Probatio QEMU/OVMF

`proba_terminale_sylviae_i.py` nunc:

1. TERMINALE e bureau aperit;
2. `SALVE` per `sendkey` scribit et exsequitur;
3. `VERSIO` scribit et exsequitur;
4. bis `↑` mittit;
5. mutationem lineae prompti in framebuffer comprobans `SALVE` revocatum esse demonstrat;
6. verificat fenestram ipsam sagittis non motam esse;
7. `Enter` mittit et responsum revocati mandati in framebuffer probat.

Ita historia non solum in structura interna, sed per catenam realem UEFI → Fenestrale → TERMINALE probatur.

---

## VIII. Terminus honestus

P17-II non est shell plenus. Nondum praebet:

- creationem processuum;
- exsecutionem programmatum externorum;
- filesystema navigabile;
- pipes vel redirectiones;
- variabiles ambitus;
- job control;
- completionem tabulatoriam;
- cursorem intra lineam et editionem lateralem.

Haec facultates incrementis futuris accedent cum fundamenta systematis vera eas sustinebunt.

---

## IX. Sententia

**Historia crescit sicut usus, non sicut tabula fixa.**

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
