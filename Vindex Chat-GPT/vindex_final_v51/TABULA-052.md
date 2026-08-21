# VINDEX 0.52 — Mappa `tabulae`

Haec pagina fines interiores compilatoris enumerat, ne novae proprietates eadem loca memoriae casu occupent.

## Regiones confirmatae

| Regio | Usus |
|---|---|
| `0–99` | nomina variabilium localium |
| `100–199` | intervalla variabilium localium |
| `200–225` | nomina camporum temporaria |
| `226` | numerus acervi ad `RESERVA` |
| `227` | locus pendens `DESINE` |
| `228–327` | signa `ORDO` variabilium |
| `328–477` | nomina functionum auxiliarium |
| `478–627` | positiones functionum auxiliarium |
| `628` | numerus vocationum pendentium |
| `850–949` | magnitudines elementorum variabilium |
| `950–964` | nomina formarum registratarum |
| `1000–1014` | magnitudines formarum |
| `1050–1075` | magnitudines camporum temporariae |
| `1100–2269` | metadata camporum formarum: nomen, magnitudo, offset |
| `2300–2399` | index formae cui variabilis pertinet |
| `2400–2499` | signa `FLUITANS` variabilium |
| `2500–2525` | signa `FLUITANS` camporum temporaria |
| `2530–2919` | signa camporum formarum per formam et campum |
| `2920–2999` | regio nondum assignata in 0.51; non automatice libera habenda |
| `3000–3099` | regio reservata VINDEX 0.52 ad metadata nova, inter quae `TEXTUS` |
| `3100–3199` | regio reservata incrementis futuris 0.52 |

Capacitas `tabulae` in stabilitate 0.52 a `3000` ad `3200` augetur. Nullus novus usus infra `3000` sine renovatione huius tabulae admittendus est.

## Regula

Antequam regio nova in `tabula` sumitur, fines eius hic definiendi sunt. Formulae indices dynamicos habentes ad maximum theoreticum computandae sunt, non solum ad valores qui in probationibus fortuito apparuerunt.

Hoc principium directe ex collisione detecta circa `2900` nascitur: regio camporum formarum usque ad `2919` pervenire potest.
