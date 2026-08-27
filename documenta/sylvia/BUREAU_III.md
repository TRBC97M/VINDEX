# BUREAU III — Bureau Sylviae Functionale

## Finis

P16-III Sylviam ab statu demonstrationis, in quo fenestrae PROGRAMMATA et TABULA statim post boot ostendebantur, ad bureau systematis transit.

Post hoc incrementum:

- nulla fenestra applicationis initio visibilis est;
- taskbar initio applicationibus vacua est;
- PROGRAMMATA et TABULA ut iconae bureau pinguntur;
- clic in icona fenestram respondentem aperit et focalizat;
- clausura fenestrae eam e taskbar removet;
- eadem applicatio post clausuram ex bureau iterum aperiri potest.

Hoc est **launch graphicae sessionis**, non adhuc creatio novi processus VINDEX.

---

## Catena canonica

```text
OVMF → BOOTX64.EFI [VINDEX] → FENESTRALE II [VINDEX] → PS/2 [VINDEX] → BUREAU → FENESTRAE → FRAMEBUFFER
```

Nullum C in runtime residet.

---

## Metra bureau

Metra iconarum in `fenestrale_ii_purus.vindex` canonice definiuntur:

- basis horizontalis: `XVIII` px;
- latitudo tesserae: `CVIII` px;
- altitudo tesserae: `LXXXVIII` px;
- PROGRAMMATA: `y = LXXII`;
- TABULA: `y = CLXXVI`.

Marca `SYLVIA` in summo sinistro per textum 2× pingitur et `SYSTEMA VINDEX` subtitulum servat.

Hover tesserae ad colorem `argentum` transit. Iconographia ipsa primitivis VINDEX (`FV_RECT`, `FV_TEXTUM`, `FV_TEXTUM_SCALA`) pingitur.

---

## Initium sessionis

Clientia et superficies PROGRAMMATA/TABULA adhuc in initio sessionis creantur, quia processus applicativus separatus nondum exsistit.

Fenestrae tamen statim post `FI_ADDE` ad statum `2` ponuntur. Ergo:

- nodi fenestrarum in registro manent;
- nullae fenestrae pinguntur;
- `FI_APERTA_NUM` eas non numerat;
- taskbar applicationum vacua est;
- launcher eas postea ad statum `0` restituere potest.

Haec divisio P16-III permittit experientiam bureau veram sine simulatione falsi processus.

---

## Hit-testing

`GI_MOUSE_DOWN` prius fenestras apertas per `FI_HIT` examinat.

Si nulla fenestra sub coordinata est, `GI_BUREAU` iconas bureau examinat. Hoc impedit clic per fenestram ad iconam subiectam.

Electio iconis eundem contractum applicationis iam a P16-II probatum adhibet:

1. nodus applicationis in registro quaeritur;
2. status ad `0` ponitur;
3. `FI_FOCUS` applicatur;
4. ordo Z renovatur;
5. redraw completum fit.

---

## Probatio realis QEMU/OVMF

`instrumenta/proba_bureau_sylviae_iii.py` cursorem ex framebuffer ipso invenit et per fasciculos PS/2 parvos movet.

Trajectoria probationis:

```text
cursor initialis      = (640, 400)
PROGRAMMATA icona     = (70, 110)
PROGRAMMATA clausura  = (798, 74)
TABULA icona          = (70, 214)
```

Eventa probata:

1. boot cum taskbar applicationibus vacua;
2. hover PROGRAMMATA;
3. clic PROGRAMMATA;
4. fenestra PROGRAMMATA cum margine focus `bronzeum`;
5. PROGRAMMATA in taskbar apparet;
6. clic bullae clausurae;
7. PROGRAMMATA e taskbar removetur;
8. clic TABULA ex bureau;
9. TABULA cum focus `bronzeum` apparet;
10. TABULA in taskbar apparet.

Differentiae framebuffer observatae:

```text
launch PROGRAMMATA = 389605 pixeli
clausura           = 389637 pixeli
launch TABULA      = 232027 pixeli
```

---

## Regressionis custodia

P16-III retinet:

- XXIX/XXIX probationes canonicas;
- P16-I: taskbar XL px et textum 2×;
- P16-II: INITIUM functionale;
- PS/2 nativum;
- Fenestrale II sub UEFI;
- runtime sine C.

`proba_bureau_sylviae_iii.py` in `VINDEX — Catena UEFI pura` inseritur.

---

## Quod nondum est

P16-III consulto nondum fingit facultates quae systema non possidet:

- non creat processum novum;
- non legit catalogum applicationum e disco;
- non habet associationes fasciculorum;
- non habet duplex clic temporis sensibile;
- non habet selectionem/motionem iconarum persistens;
- non habet sessiones multiplices.

P16-IV debet e duobus clientibus fixis ad **registrum/catalgum applicationum** progredi. P10/P11 deinde contractum processus et IPC maturabunt.

**Sylvia nunc bureau habet; proximum opus est ut bureau non solum fenestras, sed applicationes ipsas cognoscat.**
