# FENESTRALE II — PVRVS I

## Propositum

Gradus I fenestras ipsas e locis fixis vectoris systematis removet. Geometria, status, focus et ordo Z non iam ex numero slotorum praedefinitorum pendent: registrum dynamicum VINDEX omnia administrat.

Hoc gradu Fenestrale structuram veterem, in qua paucae fenestrae in campis certis vivebant, definitive relinquit.

## Registrum fenestrarum

`bibliotheca/fenestrae_registrum_i.vindex` indicem dupliciter ligatum fenestrarum construit.

Caput registri continet:

1. numerum fenestrarum;
2. fenestram imam;
3. fenestram summam;
4. fenestram focus habentem;
5. identificatorem sequentem.

Quisque nodus fenestrae continet:

1. identificatorem fenestrae;
2. identificatorem clientis;
3. positionem x/y;
4. mensuram w/h;
5. statum;
6. statum maximizationis;
7. geometriam restitutionis;
8. nodum priorem;
9. nodum proximum.

Quisque nodus per `RESERVA_OCTETA` memoria VINDEX accipit. Nulla capacitas architectonica fenestrarum in registro definita est.

## Ordo Z et focus

`FI_FOCUS` fenestram electam ad summum ordinis Z movet. `FI_HIT` a summa ad imam quaerit, ut fenestra superior primum eventum muris accipiat.

`FI_RELEGE_FOCUS`, `FI_ALTERNA`, `FI_MINIMIZA` et `FI_CLAUDE` focum sine indice fixo servant vel ad alteram fenestram transferunt.

## Geometria

`FI_MOVE`, `FI_RESIZE`, `FI_MAX_TOGGLE` et `FI_GEOM_PONE` geometriam directe in nodo fenestrae mutant.

Vector systematis non iam campos x/y/w/h PROGRAMMATA aut TABULA possidet. In Gradus I statu globali tantum input, tractio, coda eventuum, registrum clientium et registrum fenestrarum manent.

## Gestor et input

`bibliotheca/fenestrale_input_i.vindex` sola protocolorum firmware lectione curat. Geometriam fenestrarum non possidet.

`bibliotheca/fenestrale_gestor_i.vindex` hit-test, focus, taskbar, tractionem, mutationem mensurae, minimizationem, maximizationem et clausuram per registrum fenestrarum exercet.

Gestor semanticam clientium non tractat. Click contenti in codam Gradus G ponitur.

## Clientes

`bibliotheca/clientes_eventa_i.vindex` clientem per registrum H et fenestram eius per registrum I quaerit. Eventum tantum clienti cui fenestra aperta est tradit.

Ita identitas clientis et identitas fenestrae separatae manent.

## Compositio

`systema/fenestrale_ii_purus_i.vindex` fenestras ab ima ad summam per indicem ligatum pingit. Taskbar numerum fenestrarum apertarum dynamice legit; latitudo bullarum ex numero praesenti nascitur.

PROGRAMMATA et TABULA sunt tantum duae fenestrae initiales demonstrationis. Architectura registri eas non limitat.

## Probatio octoginta fenestrarum

`probationes/fenestrale_purus_i_fenestrae.vindex` octoginta fenestras eodem registro creat. Probatio verificat:

- identificatores crescentes;
- numerum LXXX;
- focus et ordinem Z;
- minimizationem;
- maximizationem et restitutionem;
- clausuram;
- numerum fenestrarum apertarum.

Haec probatio non dicit LXXX esse capacitatem. Demonstrat tantum parvum limitem fixum non iam existere.

## Puritas

Post bootstrap UEFI minimum, registrum clientium, registrum fenestrarum, coda eventuum, input, gestor, compositor et clientes VINDEX sunt.

Nullum `POLLE()`. Nullum runtime alienae linguae.

**NON SVNT LOCI FIXI. SVNT FENESTRAE.**

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
