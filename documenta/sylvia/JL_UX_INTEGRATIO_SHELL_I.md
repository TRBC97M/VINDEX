# JL-UX INTEGRATIO SHELL I

**Sylvia OS — P16-XI-B**  
Status: **ACTIVUM**

## I. Propositum

P16-XI-A demonstravit asseta altae resolutionis per catenam veram:

```text
PNG → SIMG II → FAT → VINDEX → Graphica IX → framebuffer QEMU/OVMF
```

reddi posse. P16-XI-B eandem familiam in testam veram Sylviae infert. Hic gradus non est showroom neque simulacrum: payload est `systema/fenestrale_ii_purus_i.vindex` ipsum.

## II. Ambitus

Hoc incremento mutantur tantum:

- iconae Bureau;
- iconae INITII;
- via constructionis quae XII SIMG in imaginem UEFI Fenestralis includit;
- compositor ad selectionem premium/fallback.

Non mutantur:

- hitbox Bureau 108×88;
- coordinatae INITII et itemorum;
- launch applicationum;
- focus et ordo Z;
- motus/resize/minimizatio/maximizatio fenestrarum;
- taskbar input contractus;
- clientes PROGRAMMATA, TABULA, TERMINALE, OFFICINA;
- persistentia OFFICINAE.

## III. Gestor runtime

Vector systematis locum `s[42]` accipit:

- `0` = familia premium non adest vel incompleta est;
- `!=0` = gestor SIMG II cum XII variantibus validis.

IDs assetorum sunt:

- 101 PROGRAMMATA;
- 102 TABULA;
- 103 TERMINALE;
- 104 OFFICINA.

Quodque ID habet scalas 1000, 1500 et 2000.

## IV. Fallback

Sylvia boot non recusat si assetum deest. `XIB_CREA()` familiam tantum accipit si omnes XII variantes validae sunt. Aliter `s[42]=0` et compositor atlas P16-VII canonicum adhibet.

Ita corruptio vel absentia artis non fit defectus semanticae shellis.

## V. Scala

Gestor eligit:

- 1000 infra 1600×1000;
- 1500 a 1600×1000;
- 2000 a 2400×1400.

Destinatio Bureau manet 48×48; INITIUM 32×32. Graphica IX interpolatione alpha praemultiplicata optimam variantem ad destinationem componit.

## VI. Constructio

`systema/uefi/construe_uefi_purum.sh` cum payload `fenestrale_ii_purus_i.vindex`:

1. fontem VINDEX compila;
2. imaginem GPT/FAT32 construe;
3. XII PNG per importatorem in SIMG II convertit;
4. fasciculos 8.3 in radicem ESP inserit;
5. imaginem finalem tradit.

Nomina runtime:

```text
PRG1.SMG  PRG15.SMG  PRG2.SMG
TAB1.SMG  TAB15.SMG  TAB2.SMG
TRM1.SMG  TRM15.SMG  TRM2.SMG
OFF1.SMG  OFF15.SMG  OFF2.SMG
```

Python hic instrumentum constructionis tantum est; BOOTX64.EFI, nucleus, shell, decoder, gestor et renderer runtime VINDEX puri manent.

## VII. Ordo picturae

Compositor:

```text
fundum
→ Bureau semanticum
→ emblema Sylviae
→ XIB premium vel atlas VII fallback
→ fenestrae
→ INITIUM
→ XIB premium vel atlas VII fallback
→ taskbar
→ cursor
```

INITIUM pictogramma vectoriale non pingit cum `s[42]!=0`, ne imago vetus sub alpha premium appareat.

## VIII. Probationes requisitae

Ante `CERTIFICATUM` requiruntur:

1. compilatio native VINDEX totius Fenestralis;
2. XXXV probationes canonicae sine regressione;
3. puritas Sylviae;
4. constructio imaginis cum XII SIMG realibus;
5. QEMU/OVMF Bureau cum quattuor iconis premium;
6. QEMU/OVMF INITIUM cum quattuor iconis premium;
7. click/hover/launch INITII intacta;
8. fenestrae, TERMINALE et OFFICINA integra;
9. captura framebuffer exacti capitis inspecta;
10. fallback sine assetis separatim compilabilis et bootabilis.

## IX. Lex visualis

Integratio non mutat familiam artis P16-XI-A. Iconae debent manere translucidae, anti-aliased, materialiter cognatae et sine halo RGB occulti. Background INITII debet per alpha iconis apparere, non quadratum opacum circum iconam.

## X. Post hunc gradum

Post P16-XI-B:

- **P16-XI-C** — chrome fenestrarum premium 9-slice;
- deinde cursores anti-aliased;
- materiae taskbar/INITIUM maturiores;
- wallpaper multi-resolutionis tantum postquam ipsa testa premium est.

**Asseta iam non in laboratorio vivunt; pars shellis realis fiunt.**
