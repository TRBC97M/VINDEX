# Transportus VirtIO PCI in VINDEX

## I. Finis

P12-V4 primum transportum VirtIO modernum a VINDEX puro instituit. Rector
capacitatum venditoris PCI non ad structuras fictas confugit: BAR, intervalla,
mensurae et multiplicator notificationis e configuratione apparatus ipsius
leguntur, contra limites BAR probantur, deinde per regiones MMIO typatas
adhibentur.

Probatio canonica apparatum `virtio-gpu-pci` `1AF4:1050` post pontem PCIe
invenit, `VIRTIO_F_VERSION_1` tractat, codam DMA constituit et mandatum
`VIRTIO_GPU_CMD_GET_DISPLAY_INFO` per apparatum verum consumi requirit. Hoc
incrementum transportum et responsum scanout certificat; nondum superficiem
Graphica X ad scanout VirtIO nectit nec accelerationem 3D fingit.

Norma secuta est
[Virtual I/O Device (VIRTIO) Version 1.3](https://docs.oasis-open.org/virtio/virtio/v1.3/virtio-v1.3.html),
praesertim capitula 2.7, 3.1, 4.1 et 5.7.

## II. Facultates PCI modernae

`VP_CREA` indicem capacitatum PCI terminis et XLVIII visitationibus munitum
percurrit. Solas capacitates venditoris `0x09` interpretatur et primas formas
quas rector sustinet eligit:

- `COMMON_CFG` ad statum, facultates et configurationem codae;
- `NOTIFY_CFG` cum `notify_off_multiplier`;
- `ISR_CFG` ad causam legendo simul agnoscendam;
- `DEVICE_CFG` ad configurationem propriam GPU.

Quisque campus `bar`, `offset` et `length` ante mappationem probatur. BAR
portuum reicitur. Mensura explorata, overflow arithmetica et minima structurae
coercentur. Regio notificationis scribi tantum potest; ISR legi tantum potest;
regio communis utraque permissione indiget.

Intervallum zero est validum: regio communis QEMU eo modo in initio BAR LXIV
ponitur. Custodia overflow solum regressum addressae recusat, non aequalitatem
legitimam inter basim BAR et primum octetum facultatis.

Forma `VP_CREA_EX` eundem contractum praebet et descriptorem diagnosticum
optionalem implet: codicem creationis, genera facultatum visa et mappata,
statum PCI atque caput facultatis cuius mappatio recusata est. Haec probatio
firmware defectum ante negotiationem sine telemetria privata rectoris
distinguere potest; `VP_CREA` manet involucrum ABI simplex.

Ante explorationem mensurae BAR, `VP_CREA` decodificationem I/O, memoriam et
bus mastering cohibet. Postquam regio communis inventa est, solam memoriam
aperit, apparatum ad status zero resetat, deinde commandum PCI pristinum
reddit. Sic firmware vel rector prior DMA veterem non resumere potest dum BAR
omnibus unitatibus exploratur.

In BAR LXIV bitorum, pars superior originalis per indicem BAR proximum
legitur et ante partem inferiorem restituitur. Sic regio supra IV Gio neque
truncatur neque per explorationem magnitudinis corrumpitur.

## III. Nominatio et status apparatus

`VP_INITIALIZA` ordinem normae servat:

1. commandum PCI pristinum servat, deinde memoriam et bus mastering aperit;
2. zero ad `device_status` scribit et resetum completum exspectat;
3. `ACKNOWLEDGE` et `DRIVER` ponit;
4. duas partes facultatum legit;
5. solum subset a rectore intellectum reddit;
6. `VIRTIO_F_VERSION_1` obligatoriam requirit;
7. `FEATURES_OK` ponit atque iterum legit;
8. post codam instructam `DRIVER_OK` ponit.

Rector hoc gradu nullas facultates optionales accipit. Coda ergo forma divisa
est, notificationis data et event-index non adhibentur. Negotium novum post
`FEATURES_OK` numquam additur.

## IV. Coda divisa et memoria DMA

Descriptor `VQ_*` tres areas normativas continet:

| Pars | Conformatio | Mensura |
|---|---:|---:|
| descriptoria | XVI octeta | `16 * q` |
| annulus praebitus | II octeta | `6 + 2 * q` |
| annulus adhibitus | IV octeta | `6 + 8 * q` |

Magnitudo codae positiva, potentia duorum et non maior quam `32768` esse
debet. P12-V4 sub probatione octo ingressus in una pagina DMA possessa ponit.
Adressae `queue_desc`, `queue_driver` et `queue_device` physicae sunt, non
acus acervi communes.

Quamquam hae tres adressae LXIV bitorum sunt, regio communis PCI accessus
XXXII bitorum postulat. `VP_COMMUNE_SCRIBE64` partem inferiorem primum et
partem superiorem deinde duabus scriptionibus XXXII bitorum naturaliter
conformatis ponit; transactio MMIO LXIV bitorum consulto non adhibetur.

`VQ_DESCRIPTOR_SCRIBE` longitudinem XXXII bitorum, indicem, vexilla `NEXT` et
`WRITE`, atque nexum non circularem coercet. `VQ_PRAEBE` descriptoria et
annulum ante incrementum `idx` per `DMA_SYNCHRONIZA` publicat; index naturaliter
ad XVI bitos volvitur. Numerus catenarum expositarum magnitudinem codae
excedere non potest.

`VQ_COMPLETUM` dominium per sepem ad CPU reducit, ingressum annuli adhibiti
legit, id et longitudinem servat, atque unam catenam liberam reddit. Rector
simplex P12-V4 unam catenam synchronam exercet; allocator generalis
descriptorum plurium postea addetur.

## V. Prima mandati GPU probatio

`virtio_gpu.vindex` caput XXIV octetorum et responsum CCCCVIII octetorum
`GET_DISPLAY_INFO` format. Duo descriptoria ligantur:

1. caput a fabrica legendum;
2. responsum a fabrica scribendum.

Annulus praebitus `NO_INTERRUPT` petit, quia hic incrementum completionem in
annulo adhibito exspectat. Post `DRIVER_OK`, scriptio XVI bitorum ad adressam
`notify_base + queue_notify_off * notify_off_multiplier` fabricam excitat.
Responsum `VIRTIO_GPU_RESP_OK_DISPLAY_INFO` (`0x1101`), id catenae zero,
index adhibitus unus et saltem unus scanout activus dimensionibus positivis
requiruntur.

## VI. Vita et restauratio

Ante paginam DMA liberandam `VP_RESTITUE` totum apparatum resetat et zero
relectum exspectat. Sic fabrica annulos iam non attingere potest. Deinde pagina
per `FreePages` liberatur et commandum PCI XVI bitorum exactum pristinum
redditur. Status PCI superior numquam rescribitur.

Defectus post initium non debet paginam vivam relinquere; probator omnes vias
post codam creatam per `VP_RESTITUE` claudit. Mappationes descriptorum MMIO
acervum logicum hodiernum sequuntur et paginae apparatus non possidentur.

## VII. Limites honesti et iter sequens

P12-V4 consulto haec nondum facit:

- MSI-X VirtIO non instituit; `NO_INTERRUPT` et annulus `used` probationem
  synchronous perficiunt;
- plures catenas simul nec allocator descriptorum generalis sustinet;
- coda cursoris GPU non constituitur;
- resource 2D, backing, transfer, flush et scanout non mittuntur;
- Graphica X framebuffer auctoritas visualis manet;
- 3D, virgl, rutabaga et host blobs extra hunc contractum sunt.

Proximum incrementum hardware est MSI-X transactionale vel, si integra
catena graphica ad probationem prius componitur, executor Graphica X qui
transportum P12-V4 accipit sed backend software oraculum semanticum servat.
Nulla coda GPU `parata` declarabitur antequam interruptio, vita resource et
fallback post errorem realiter probata sint.

## VIII. Probationes

`probationes/virtio_pci.vindex` native probat:

- mensuras et conformationes trium arearum;
- terminos capacitatis et notificationis;
- descriptoria legibilia bit pro bit;
- ordinem annuli praebiti et reditum annuli adhibiti;
- conversionem `65535 -> 0`;
- overflow codae, nexum circularem et regionem DMA nimis parvam.

`instrumenta/proba_virtio_gpu_053.sh` sub QEMU/OVMF q35:

1. `virtio-gpu-pci` modernum post pontem PCIe ponit;
2. payload UEFI VINDEX purum compilat;
3. facultates et BAR ex apparatu legit;
4. codam octo ingressuum in pagina DMA possessa constituit;
5. `GET_DISPLAY_INFO` notificat et responsum in annulo `used` exspectat;
6. genus `0x1101`, dimensiones et scanout activum probat;
7. resetum, liberationem paginae et commandum PCI restitutum requirit.

Nuntii huius probationis per UART COM1 directe exeunt. `ConOut` consulto non
adhibetur postquam VINDEX apparatum GPU resetat, quia protocollum GOP firmware
eodem apparatu uti potest et post translationem proprietatis iam auctoritas
telemetriae esse non debet.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
