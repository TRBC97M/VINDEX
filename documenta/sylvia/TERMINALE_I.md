# TERMINALE I — Primum terminale nativum Sylviae

## Finis

P17-I primam applicationem Sylviae quae claviaturam textualem vere consumit introducit. TERMINALE non est pictura decorativa neque ansa input separata: tertius cliens Fenestralis est, eodem catalogo applicationum, registro fenestrarum, foco et coda eventuum quibus PROGRAMMATA et TABULA utuntur.

Catena interactionis canonica est:

```text
clavis
→ UEFI Simple Text Input
→ IN_CLAVIS
→ GI_CLAVIS
→ coda eventuum Fenestralis
→ cliens focalis
→ TE_CLAVIS
→ superficies privata
→ compositor Fenestralis
→ framebuffer
```

## Registratio applicationis

TERMINALE in catalogo P16-IV ut applicatio tertia registratur:

- id applicationis: `3`;
- id clientis: `3`;
- genus clientis: `3`;
- nomen: `TERMINALE`;
- praesentia in bureau: vera.

Ita bureau, INITIUM, titulus fenestrae et taskbar nomen ex eodem registro communi accipiunt. Nullus ramus specialis navigationis TERMINALE cognoscere debet.

## Claviatura et focus

`GI_CLAVIS` claviaturam systematis adhuc pro contractibus Fenestralis tractat ubi necesse est:

- `ESC` — terminatio sessionis probationis;
- `TAB` — alternatio focus;
- claves directionales — motus fenestrae focalis.

Ceteri valores Unicode ad clientem fenestrae focalis per `EG_PONE` mittuntur. Eventus claviaturae genus `2` habet et scalaris Unicode in campo `datum` codatur.

`CI_EVENTA_AGE` eventum solum clienti visibili et focali tradit. Genus clientis `3` ad `TE_CLAVIS` dispatchatur; superficies deinde tantum si status mutatus est repingitur.

Hoc consilium significat claviaturam non habere ansam TERMINALIS privatam. Futuri clientes textuales eodem strato generali crescere possunt.

## Status TERMINALIS

`TE_CREA` structuram status creat:

```text
+0   descriptor lineae currentis
+8   responsum ultimi mandati
+16  numerus mandatorum actorum
```

Descriptor lineae contractum TEXTUS-compatible sequitur:

```text
+0   longitudo octetorum
+8   capacitas octetorum
+16  octeta UTF-8
```

Capacitas initialis LXIV octetorum est, sed `TE_LINEA_REDIMENSIONA` eam duplicat quoties opus est. Itaque linea terminalis non habet capacitatem parvam fixam.

## UTF-8

`TE_APPENDE_SCALARE` scalaria usque ad U+FFFF in UTF-8 codificat. Surrogata UTF-16 reiciuntur. P17-I consulto nondum omnem planitiem Unicode supra U+FFFF suscipit; hoc debitum apertum est et cum bibliotheca TEXTUS futura reconciliandum erit.

`TE_RETROCEDE` ultimum scalare UTF-8 integrum removet. Continuationes `10xxxxxx` retro percurruntur, ergo backspace in `é` duo octeta simul removet neque textum corruptum relinquit.

## Mandata interna primi gradus

P17-I quattuor mandata interna simplicia definit:

- `SALVE` → `SALVE EX SYLVIA.`;
- `VERSIO` → `SYLVIA / VINDEX 0.53`;
- `AUXILIUM` → indicem mandatorum;
- `PURGA` → responsum visibile purgat.

Mandatum ignotum → `MANDATUM NON INVENTUM.`

Haec mandata probant lineam input, submissionem per Enter, dispatchum et mutationem superficiei. Non simulant adhuc shell systematis, processuum creationem, filesystema neque exsecutionem programmatum externorum.

## Forma visualis

Superficies TERMINALIS est obscura et identitatem P16-V retinet:

- caput `SYLVIA TERMINALE`;
- titulus fenestrae e catalogo communi;
- corpus obscurum;
- responsum mandati;
- prompt `>`;
- cursor linearis;
- focus fenestrae per chrome P16-V.

Renderer TERMINALIS intra superficiem privatam pingit; ornamenta fenestrae a Fenestrale communi manent.

## Probationes

### Probatio nativa

`probationes/terminale_i.vindex` verificat:

- creationem status;
- scripturam et exsecutionem `SALVE`;
- UTF-8 `é` (`C3 A9`);
- backspace per scalare integrum;
- crescentiam lineae ultra capacitatem initialem usque ad CC characteres;
- `PURGA`;
- mandatum ignotum;
- numerum mandatorum actorum.

### Probatio QEMU/OVMF

`instrumenta/proba_terminale_sylviae_i.py` exercet viam realem:

1. Sylvia per OVMF bootat;
2. cursor PS/2 ad iconam TERMINALE movetur;
3. TERMINALE e bureau aperitur et focus accipit;
4. QEMU `sendkey` litteras `SALVE` mittit;
5. UEFI eas legit;
6. Fenestrale eas per codam clienti focali tradit;
7. textus in prompt vere apparet;
8. Enter mandatum exsequitur;
9. responsum in framebuffer vere mutatur;
10. prompt purgatur.

Probatio pixeles framebuffer reales comparat; nullam imaginem generatam pro testimonio adhibet.

## Limites conscii P17-I

P17-I nondum est shell plenus. Desunt adhuc:

- historia mandatorum;
- selectio/copia textus;
- scrollback;
- cursor editabilis intra lineam;
- Unicode supra U+FFFF;
- filesystema et directorium currente;
- processuum creatio et exsecutio programmatum VINDEX;
- pipes, redirectiones et variabiles;
- API communis callback clientium loco dispatchus per genus.

Hi limites non occultantur. Primus finis est contractum input textualem et applicationem TERMINALE veram stabilire.

## Via proxima

Post P17-I, TERMINALE paulatim ad shell Sylviae promovendum est. Sed proximum magnum applicativum destinatum manet Officina intra Sylviam: finis diuturnus est ut usor in ipsa Sylvia fontem VINDEX scribere, compilare et exsequi possit.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
