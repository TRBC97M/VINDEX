# ATMOS Terminal Depth — Probatio IV: ludus graphicus persistentis

## Propositum

Probatio IV primum punctum est in quo tres probationes anteriores non iam iuxta
se demonstrantur, sed in **unam applicationem ludicam Win64** coalescunt.

Catena est:

```text
POC I     nucleus simulationis + ATD1 persistentia
   +
POC II    actio continua + contractus I/O maturiores
   +
POC III   fenestra + framebuffer + FFI + clavatura + mus
   ↓
POC IV    ludus graphicus persistentis
```

Applicatio canonica:

```text
PROGRAMMATA/ATMOS_TERMINAL_DEPTH/POC_IV/ludus.vindex
```

## Nucleus communis

Logica quae frontendibus non propria est in:

```text
PROGRAMMATA/ATMOS_TERMINAL_DEPTH/COMMUNE/nucleus.vindex
```

separatur.

Nucleus continet:

- initium et onerationem status;
- formatum `ATD1` versionis I;
- scan sonar;
- descensum et ascensum;
- extractionem mineralium;
- mercaturam;
- reparationem;
- eventa determinata;
- condicionem missionis perdita;
- `ATMOS_ACTIO` ut contractum unicum frontendium.

Formatum save manet XLVIII octetorum et cum POC I/II compatibile. Duo campi iam
olim reservati nunc ultimum contactum sonar et ultimum eventum servant; lectores
historici eos ignorare possunt.

## Facultas generalis nova: NUMERUS ad TEXTUS

HUD ludicus numeros reales ostendere debet. Bibliotheca `textus.vindex` iam UTF-8
mature tractabat, sed conversionem integeris ad textum decimalem non praebebat.

Propter regulam architectonicam PROGRAMMATA, solutio non in Atmos privata
scripta est. Addita est bibliotheca generalis:

```text
Vindex Chat-GPT/vindex_final_v51/bibliotheca/conversio.vindex
```

Contractus:

```text
TEXTUS_EX_NUMERO_DECIMALI(valor)
```

Probat:

- zerum;
- valores positivos;
- valores negativos;
- `INT64_MAX`;
- `INT64_MIN`;
- TEXTUS UTF-8 validum et NUL-terminatum.

Workflow `VINDEX — Conversio NUMERUS TEXTUS` eam tam sub ELF quam sub Windows
PE32+ vero exsequitur.

## HUD Win64

Frontend POC IV USER32/GDI32 per FFI generalem P11-C utitur.

Framebuffer VINDEX repraesentat:

- oxygenium;
- energiam;
- integritatem;
- profunditatem;
- radar sonar;
- ultimum contactum;
- ultimum eventum;
- septem regiones actionum.

Super framebuffer, `GDI32!TextOutA` pingit valores actuales:

- `DEPTH`;
- `OXYGEN`;
- `ENERGY`;
- `HULL`;
- `CREDITS`;
- `ORE`;
- `CYCLE`;
- statum sonar/eventi;
- actiones disponibles.

Ita POC IV simul rasterizationem VINDEX et textum nativum GDI exercet.

## Inputum

Claves:

| Clavis | Actio |
| --- | --- |
| `S` | scan sonar |
| `D` | descende |
| `A` | ascende |
| `M` | minera extrahe |
| `T` | mercaturam fac |
| `R` | repara |
| `N` | expeditionem novam crea |
| `Escape` | exi |

Fascia inferior eadem septem actiones mure offert. Positio muris per
`GetCursorPos` et `ScreenToClient` in coordinatas framebuffer convertitur.

## Certificatio Windows

GitHub Actions cursus `33754602955`:

1. `ludus.vindex` ad `atmos_poc_iv.exe` PE32+ compilavit;
2. executable sub Microsoft Windows Server 2025 vere exsecutus est;
3. statum novum creavit;
4. `descend -> mine -> ascend -> trade` per `ATMOS_ACTIO` exsecutus est;
5. framebuffer et HUD `TextOutA` praesentavit;
6. APIs muris, clavis et eventorum exercuit;
7. `atmos.sav` byte per byte verificavit.

Status finalis:

```text
CYCLE   4
DEPTH   120
OXYGEN  87
ENERGY  75
HULL    100
CREDITS 300
ORE     0
```

CI eosdem valores in save ATD1 confirmavit et conclusit:

```text
RECTE: POC IV HUD + nucleus + ATD1 sub Windows probata sunt.
```

## Quid iam demonstratur

Post Probationem IV assertio fortior quam antea demonstrata est:

> **VINDEX potest ludum Win64 nativum, graphicum, interactum et persistentem ex
> fonte VINDEX producere, sine HTML aut runtime ludi externo.**

Hoc nondum significat Atmos originalis perfecte portatus esse. Significat autem
fundamenta necessaria iam in una applicatione vera convenire.

## Gradus posteriores

Probationes sequentes plus ad ludum ipsum quam ad minimum backend spectare
possunt:

1. topologiam sectorum et mundum proceduralem;
2. contactus sonar cum positione et tempore vitae;
3. stationes, structuras et convoy;
4. UI richer et typographiam Atmos;
5. audio nativum per eandem FFI;
6. migrationem ulterioris logicae ex prototypo HTML originali.

Regula manet: quoties nova necessitas Atmos generalis est, facultas VINDEX
generalis ante workaround privatum praeferenda est.
