# P16-VI — IDENTITAS VISVALIS SYLVIAE

## Propositum

P16-VI faciem Sylviae non ut ornamentum separatum, sed ut partem systematis Fenestralis definit. Renderer, bureau, INITIUM, taskbar, chrome fenestrarum et clientes canonici eadem grammatica visuali utuntur. Omnis pictura hic descripta a codice VINDEX nativo generatur et sub QEMU/OVMF in framebuffer vero probatur.

## Principia

1. **Nox graphitica** systema et ambitum significat. Fundum, taskbar, capita obscura et regiones systematis colore fere `RGB(28,31,32)` vel propinquis utuntur.
2. **Ebur et papyrus** sunt superficies operis. Documenta, tabulae, cardines et instrumenta clara non albo puro sed tonis calidis pinguntur.
3. **Bronzeum / aes** est accentus primarius. Focus fenestrae, limites selecti, prompta et lineae structurae eo distinguuntur.
4. **Viride temperatum** est accentus secundarius. Statum sanum, vias, cursorem et informationem systematis quietam indicat.
5. **Rubrum temperatum** solum errori, deletioni vel actioni periculosae reservatur.
6. Colores saturati caerulei P16-I–V non amplius identitatem principalem constituunt.
7. Decoratio numquam informationem aut interactionem fingit. Horologium, filesystema, status retis aut alia data non pinguntur nisi res vera subest.

## Palette canonica initialis

| Munus | RGB |
|---|---|
| Nox | `28,31,32` |
| Carbo TERMINALIS | `22,24,23` |
| Lapis | `49,55,55` |
| Chalybs | `92,99,96` |
| Ebur | `241,238,228` |
| Papyrus | `219,211,196` circiter |
| Charta | `249,247,240` vel `250,249,245` |
| Bronzeum | `185,138,82` |
| Aes obscurius | `128,87,53` |
| Viride | `71,118,111` |
| Rubrum temperatum | `143,64,58` vel `177,95,82` pro errore in campo obscuro |

Valores minores inter clientes permittuntur si munus semanticum idem manet.

## Bureau

- nomen `SYLVIA` in ebore cum accentu bronzeo;
- subtitulus `SYSTEMA VINDEX` viridis;
- quattuor applicationes canonicae pictogrammata diversa habent: PROGRAMMATA, TABULA, TERMINALE, OFFICINA;
- hitbox cuiusque tesserae manet `108×88` in P16-VI primo;
- hover papyraceus est mutatio visibilis, non mutatio geometriae;
- fundum est gradientia graphitica calida cum lineis architectonicis aeneis/viridibus tenuibus;
- nullum wallpaper externum aut imago aliena requiritur.

## INITIUM

- caput nocturnum cum titulo eburneo;
- corpus eburneum/papyraceum;
- applicationes pictogrammatibus eiusdem familiae ac bureau utuntur;
- hover papyraceus et focus fenestrae bronzeus distinguuntur;
- numerus columnarum et ordinum ex registro applicationum manet dynamicus.

## Taskbar

- altitudo canonica manet XL pixeli;
- corpus nocturnum, linea superior bronzea;
- INITIUM et regio systematis lapideae sunt;
- applicatio activa linea bronzea et tono calidiore distinguitur;
- nulla regio ficta fingit statum qui in runtime non exsistit.

## Fenestrae

- corpus eburneum;
- titulus activus nocturnus cum margine bronzeo;
- titulus inactivus lapideus/chalybeus;
- umbra neutra, non caerulea;
- bullae minimizationis/maximizationis lapideae;
- clausura rubra temperata;
- hitbox et geometria P16-V servantur, nisi incrementum futurum id expresse mutet et omnes probationes interactionis renovet.

## Clientes canonici

### PROGRAMMATA

Superficies eburnea/papyracea, cardines chartacei, accentus viridis et selectio/actiones bronzeae. Deletio sola rubra est.

### TABULA

Grid charta/papyrus, lineae calidae, selectio bronzea cum impletione viridi pallida. Formula regio viridem ut accentum secundarium adhibet.

### TERMINALE

Fundum carbonarium, caput lapideum, textus eburneus, promptum bronzeum, cursor et indicia systematis viridia, errores rubri. TERMINALE non debet videri sicut pannus cyanus separatus ab ambitu.

### OFFICINA

Charta clara, gutter papyraceus, linea activa calida, cursor viridis, caput nocturnum et status bronzeus/chalybeus. Stratum persistentiae P19-II eadem palette utitur: via et successus virides, errores rubri, `F2 SERVA` in papyro.

## Contractus interactionis

P16-VI non mutat sine causa:

- loca hit-test;
- magnitudines bullarum fenestrae;
- centrum iconarum bureau;
- cursum input PS/2/UEFI;
- focus bronzeum P16-V;
- semanticas TERMINALIS, OFFICINAE, PROGRAMMATUM aut TABULAE;
- persistentiam P19-I/P19-II.

Forma visualis non licet regressiones functionales occultare.

## Probatio canonica

Probationes visuales non simpliciter memoriam veterum colorum congelant. Quaerunt signa semantica:

- resolutio et pictura non trivialis;
- nox, ebur et bronzeum in framebuffer vero;
- focus activus/inactivus;
- hover, INITIUM et taskbar;
- launch, clausura et relaunch;
- TERMINALE cum claviatura et historia;
- OFFICINA cum editore, cursore et persistentia.

Capturae canonicae P16-VI ex `screendump` QEMU/OVMF veniunt. Maquette generata vel imago composita numquam probatio runtime habetur.

## Terminus

P16-VI identitatem visualem fundat, non artem graphicam semel ac semper claudit. Typographia, iconographia et compositio postea maturari possunt, sed mutationes futurae hunc contractum semanticum aut probationes reales violare non debent.
