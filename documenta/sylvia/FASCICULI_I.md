# FASCICULI SYLVIAE — Incrementum I

## Propositum

P19-I primum contractum fasciculorum persistentium Sylviae canonice definit. Finis non est filesystema fictum in memoria, sed ut applicationes VINDEX eundem contractum ad res vere in disco servatas uti possint.

Backend initialis `SimpleFileSystem` et `EFI_FILE_PROTOCOL` firmware UEFI adhibet. Sylvia ipsa protocolum vocat e `SystemTable` et `ImageHandle` quae ponticulus boot iam tradit; ponticulus igitur non fit servus fasciculorum residens.

## Separatio contractus et backend

`bibliotheca/fasciculi_sylviae_i.vindex` nomina publica `FS_*` a subsidiis UEFI `FU_*` separat. Hoc deliberatum est: OFFICINA, TERMINALE et futurus gestor fasciculorum contractum Sylviae videre debent, non internam originem bytes.

Backend UEFI incrementi I potest postea backend Block I/O vel filesystemate VINDEX nativo substitui sine mutatione semanticae applicationum.

## API incrementi I

- `FS_DISPONIBILIS()` — probat num volumen boot per protocolum UEFI aperiri possit;
- `FS_EXISTIT(via)` — existentiam fasciculi probat;
- `FS_LEGE_TEXTUM(via)` — totum fasciculum in novum `TEXTUS` dynamicum legit;
- `FS_SCRIBE_TEXTUM(via, textus)` — fasciculum scribit, flush facit, claudit, reaperit et contentum byte-per-byte verificat;
- `FS_DELE_SI_ADEST(via)` — fasciculum si adest delet;
- `FS_TEXTUS_AEQUALIS(a,b)` — auxiliare exactae comparationis octetorum.

`FS_LEGE_TEXTUM` magnitudinem fasciculi ex positione finis EFI obtinet, memoriam exactam dynamicam reservat et nullum limen parvum applicationis imponit.

## Viae et Unicode

Via publica est `TEXTUS` UTF-8. `FU_VIA_UTF16` eam ad catenam UTF-16LE firmware convertit:

- `/` ad `\\` UEFI vertitur;
- scalaria BMP directe servantur;
- scalaria supra `U+FFFF` in paria surrogate UTF-16 vertuntur;
- UTF-8 invalidum, surrogata input aut scalaria supra `U+10FFFF` reiciuntur.

Probatio pura inter alia viam `A/é/😀.VIX` exercet.

Propter modelum importationum praesentem VINDEX, fons qui hoc stratum utitur `bibliotheca/textus.vindex` ante `bibliotheca/fasciculi_sylviae_i.vindex` explicite importat. Hoc est contractus constructionis praesentis, non semanticum filesystematis.

## Scriptura

Scriptura P19-I sequitur ordinem:

1. vetus fasciculum, si adest, delet;
2. fasciculum novum cum `EFI_FILE_MODE_CREATE | READ | WRITE` creat;
3. omnes octetos scribit;
4. `Flush` vocat;
5. handle claudit;
6. e disco iterum aperit;
7. longitudinem et omnes octetos cum fonte comparat.

Ita successus API non solum codicem reditus firmware credit.

**Limitatio:** substitutio hodie atomica non est, quia vetus fasciculus ante creationem novi deletur. Scriptura per nomen temporarium et rename/commit separatum incrementum futurum est.

## Probatio persistentiae vera

Custodia `instrumenta/proba_fasciculos_persistentes_i.sh` unam imaginem discalem construit et eam duobus initii QEMU/OVMF sine reconstructione intermedia exercet.

Primum initium:

- `P19TEST.TXT` nondum adest;
- Sylvia 4 128 octeta creat et scribit;
- `Flush` fit;
- fasciculus clauditur et intra idem initium reaperitur;
- contentum exacte congruit;
- QEMU clauditur.

Secundum initium:

- **eadem imago** iterum bootat;
- fasciculus a primo initio iam adest;
- 4 128 octeta ex disco leguntur;
- contentum exacte congruit.

Exitus probatus:

```text
FASCICULI: status=1 mensura=4128 backend_uefi=1
RECTE: primum initium datum in disco reliquit.
FASCICULI: status=2 mensura=4128 backend_uefi=1
RECTE: secundum initium fasciculum a primo initio servatum legit.
=== P19-I PERSISTENTIA DUORUM INITIORUM PROBATA ===
OVMF -> Sylvia [VINDEX] -> SimpleFileSystem UEFI -> fasciculus -> restart -> relectio
Nulla copia memoriae inter initia transfertur.
```

Magnitudo 4 128 consulto vetus limen historicum 4 095 octetorum superat. P19-I igitur non reviviscit structuram veterem parvam.

## Cur backend UEFI nondum finis est

Historia VINDEX 0.44 rem magni momenti docuit: in quodam firmware ASUS E410M scriptura FAT successum rettulit sed post restart non mansit. Tum partitio GPT `VINDEXV0`, Block I/O, `FlushBlocks` et relectio exacta persistentiam hardware confirmaverunt.

Hodierna imago adhuc partitionem `VINDEXV0` continet, sed eius formatum vetus paucis slotis fixis **non** reviviscet. Mechanismus Block I/O selective in backend modernum dynamicum posterius portandus est.

P19-I ergo backend UEFI sub QEMU/OVMF canonice probat; persistentia in firmware physico specifico nondum ex hac probatione sola affirmatur.

## Nondum in P19-I

- enumeratio directoriorum;
- creatio directoriorum;
- rename;
- write atomica;
- metadata temporum/permissionum;
- montes multiplices;
- backend `VINDEXV0` modernus;
- apertio/servatio ab OFFICINA;
- mandata fasciculorum TERMINALIS;
- gestor fasciculorum graphicus.

## Gradus proximus

P19-II OFFICINAM ad hunc contractum coniungere debet, ita ut textus editus in fasciculum verum servetur et post restart iterum aperiatur. Nulla fictio save/build/run ante hoc stratum permissum est.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**