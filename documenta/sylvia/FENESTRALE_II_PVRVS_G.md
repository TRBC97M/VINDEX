# FENESTRALE II — PVRVS G

## Propositum

Gradus G nexum directum inter gestorem fenestrarum et clientes removet. Gestor iam click clientis non interpretatur neque `PE_CLICK` aut `TF_CLICK` vocat. Eventum locale in codam circularem VINDEX ponit; stratum clientium codam consumit et clientem destinatarium tractat.

Hoc est primum gradum ad clientes Fenestralis re vera independentes et ad numerum applicationum non fixum.

## Coda eventuum

`bibliotheca/fenestrale_eventa_g.vindex` codam circularem in memoria VINDEX definit.

Caput codarum quattuor numeros LXIV-bituum continet:

1. capacitas;
2. index lectionis;
3. index scriptionis;
4. numerus eventuum praesentium.

Quodque eventum quinque numeros continet:

1. genus;
2. cliens destinatus;
3. x locale;
4. y locale;
5. datum auxiliarium.

Gradus G capacitatem XXXII eventuum adhibet. Coda plena eventum novum non delet neque vetus superinscribit: `EG_PONE` zero reddit et gestor numerum eventuum perditorum in statu suo auget.

## Genus eventus

Gradus G genus `1` definit ut **click clientis**. Structura quinque camporum deliberatim generalis est, ut gradus posteriores clavem, focus, resize, activationem, timer et alia eventa eodem itinere tradere possint.

## Separatio responsabilitatum

`bibliotheca/fenestrale_gestor_g.vindex` possidet:

- input UEFI a VINDEX vocatum;
- hit-testing ornamentorum;
- focus et z-order;
- minimizationem, maximizationem et clausuram;
- tractionem et mutationem mensurae;
- conversionem coordinatarum screen in coordinatas locales;
- eventum clientis in codam ponendum.

Gestor nullam functionem PROGRAMMATA aut TABULA vocat.

`bibliotheca/clientes_eventa_g.vindex` est stratum dispatchus. `CG_AGE` eventa e coda capit, clientem destinatarium eligit, statum clientis mutat et superficiem eius renovat.

Ita Fenestrale ornamenta et ordinem desktop possidet; clientes contentum et semanticam propriam possident.

## Ordo ansae

Ansa principalis:

1. clavem legit et actiones systematis tractat;
2. murum legit;
3. click ornamentorum statim tractat vel click contenti in codam ponit;
4. `CG_AGE` codam clientium consumit;
5. si geometria vel clientis superficies mutata est, desktop iterum componit;
6. breviter quiescit.

Click contenti igitur non amplius synchrona vocatio gestoris ad clientem est.

## Clientia praesentia

PROGRAMMATA et TABULA duas superficies privatas servant. Gradus G identificatores `1` et `2` adhibet, sed coda ipsa numerum clientium non claudit: campus `cliens` numerus generalis est.

Gradus posterior registrum clientium vel mailbox generaliorem super hanc structuram aedificare potest, sine reditu ad limites sex programmatum vel ad runtime alienae linguae.

## Puritas

Post bootstrap UEFI minimum:

- coda eventuum est VINDEX;
- input est VINDEX;
- gestor fenestrarum est VINDEX;
- dispatchus clientium est VINDEX;
- superficies et compositio sunt VINDEX;
- PROGRAMMATA et TABULA sunt VINDEX.

Nullum `POLLE()`. Nullum runtime C, C++, Rust aut ASM.

**Sylvia cogitat, currit et vivit in VINDEX.**
