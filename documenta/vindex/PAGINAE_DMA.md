# Paginae DMA in VINDEX

## I. Finis

P12-V2 primum contractum canonicum memoriae DMA instituit. Buffer DMA non est
acervus communis novo nomine: rector paginas physicas per UEFI `AllocatePages`
vere possidet, basim physicam et virtualem separatim publicat, mensuram ad
paginas IV Kio rotundat et easdem paginas per `FreePages` liberat.

Hoc incrementum nondum gubernator e1000e aut VirtIO-GPU est. Fundamentum
memoriae praebet quo tales gubernatores postea codas, descriptora et buffers
apparatui sine adressis fictis tradere possint.

## II. Descriptor

`paginae_dma.vindex` descriptor CXX octetorum servat:

- basim physicam et virtualem;
- mensuram a rectore postulatam et mensuram integram attributam;
- numerum paginarum;
- proprietatem, identitatem, purgationem et permissiones apparatus;
- generationem et statum activum;
- tabulam systematis UEFI et limitem physicum postulationis;
- numerum atque directionem synchronizationum;
- attributa cache e tabula memoriae UEFI observata;
- ultimum erratum.

`DMA_REGIO_ADOPTA` memoriam ab alio gestore possidendum non facit. Haec via
probationibus et futuris allocatoribus prodest. `DMA_UEFI_ALLOCA` contra
vexillum `DMA_PROPRIETAS_UEFI` ponit; sola talis regio per
`DMA_UEFI_LIBERA` dimitti potest. Usus post liberationem et duplex liberatio
reiciuntur.

Ante liberationem gubernator apparatum sistere et dominium bufferis ad CPU
reduxisse debet. `FreePages` ordinem transactionum hardware per se nescit;
rector igitur liberationem paginae adhuc a fabrica usurpatae tutam fingere non
potest.

## III. Adressa physica et limites

Paginae semper ad IV Kio alignantur. Si `maxima` nulla est, UEFI locum eligit.
Si `maxima` positiva est, `AllocateMaxAddress` adhibetur. Sic gubernator
apparatus XXXII bitorum potest postulare ut ultimum octetum regionis infra
`0xFFFFFFFF` maneat.

`DMA_PHYSICA` adressam apparatui tradendam reddit solum post probationem
terminorum. `DMA_ADRESSA` accessus CPU ad latitudines 8/16/32/64 bitorum,
terminos et alignationem naturalem coercet. Basis virtualis hodie identitati
physicae aequatur; vexillum `DMA_IDENTITAS` hanc condicionem explicite notat.

Sylvia hodie Boot Services activos retinet. Paginae generis `EfiLoaderData`
ideo a firmware possidentur et liberantur. Cum futurum `ExitBootServices`
introducetur, gestor paginarum Sylviae eandem proprietatem recipere et has
regiones a reutilizatione excludere debebit; descriptor iam omnes paginas et
generationem ad hanc translationem necessarias servat.

## IV. Cache et cohaerentia

Post allocationem rector `GetMemoryMap` vocat et attributa regionis verae
quaerit. Campus `cache_status = DMA_CACHE_OBSERVATA` significat attributum a
firmware lectum esse; **non** significat `DMA_CACHE_IMPOSITA`. Constantes
`DMA_CACHE_UC/WC/WT/WB/UCE` bits UEFI canonicos nominant. Probatio OVMF
requirit `DMA_CACHE_WB`, id est memoriam ordinariam write-back aptam DMA
cohaerenti in x86.

`DMA_SYNCHRONIZA` permissionem directionis probat et `MFENCE` emittit:

- `DMA_AD_APPARATUM`: CPU scripsit, apparatus lecturus est;
- `DMA_AB_APPARATU`: apparatus scripsit, CPU lecturus est;
- `DMA_BIDIRECTA`: utraque permissio necessaria est.

Haec sepes ordinem praestat in x86; cache non purgat nec invalidat in machina
non cohaerenti. Futurum stratum architecturae tale opus explicite addere
debet. Similiter cache UC/WC BAR MMIO nondum a P12-V2 imponitur: V2 paginarum
DMA WB curat, non tabulas paginarum regionum apparatus.

## V. Probationes

`probationes/paginae_dma.vindex` descriptor adoptatum nativa via exercet:
terminos, alignationem, latitudines, conversionem physicam, permissiones
directionis et reiectionem liberationis non possessae.

`instrumenta/proba_paginae_dma_053.sh` sub QEMU/OVMF:

1. 8193 octeta infra IV Gio postulat et tres paginas accipit;
2. basim physicam et ultimum octetum contra limitem probat;
3. purgationem totius regionis probat;
4. attributum cache WB e tabula memoriae observat;
5. valores in tribus paginis scribit et legit;
6. duas synchronizationes directionales exercet;
7. paginas per `FreePages` liberat, usum post liberationem et duplicem
   liberationem reicit.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
