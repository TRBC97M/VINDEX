# FENESTRALE II — PVRVS H

## Propositum

Gradus H loca fixa clientium e vectore systematis removet. Superficies et status clientium non iam in `s[30]`, `s[31]`, `s[32]`, `s[33]` servantur: registrum dynamicum VINDEX eos administrat.

Hoc separat identitatem clientis a positione memoriae systematis et praeparat Fenestrale ad numerum applicationum qui non ex numero slotorum praedefinitorum nascitur.

## Registrum dynamicum

`bibliotheca/clientia_registrum_h.vindex` indicem ligatum construit. Caput registri tantum numerum nodorum et primum nodum continet. Quisque cliens nodum proprium memoria VINDEX reservatum habet.

Nodus quinque campos habet:

1. identificator clientis;
2. genus clientis;
3. superficies privata;
4. status clientis;
5. proximus nodus.

Novus cliens novum nodum accipit. Nulla capacitas architectonica XVI, XXXII, LXIV vel alia in registro definitur. Memoria praesens, non tabula slotorum fixa, terminus practicus est.

## API

- `CH_CREA` registrum vacuum creat;
- `CH_ADDE` clientem novum inserit et duplicatum id recusat;
- `CH_QUAERE` nodum per id invenit;
- `CH_NUMERUS` numerum clientium reddit;
- `CH_GENUS` genus reddit;
- `CH_SUPERFICIES` superficiem reddit;
- `CH_STATUS` statum reddit;
- `CH_STATUS_PONE` statum mutat.

## Dispatchus

`bibliotheca/clientes_eventa_h.vindex` eventum e coda Gradus G capit, nodum clientis in registro quaerit et deinde handler proprium generis clientis vocat.

Fenestrale ipsum neque superficiem PROGRAMMATA neque superficiem TABULA in locis fixis tenet. Renderer Fenestralis superficiem per `CH_SUPERFICIES` petit.

## Status systematis et status clientis

Distinctio nunc clara est:

- status fenestrae — aperta, minimizata, clausa, focus, geometria — ad Fenestrale pertinet;
- status clientis — selectio, actio, cella — in nodo registri clientis vivit;
- pixels clientis — in superficie privata nodo associata vivunt;
- eventa — per codam VINDEX ad identificatorem clientis feruntur.

## Duo clientes initiales

Gradus H ad demonstrationem PROGRAMMATA id `1`, genus `1`, et TABULA id `2`, genus `2` inserit. Haec duo non sunt capacitas registri; sunt tantum clientes initiales huius demonstrationis.

Gradus posterior potest tertium, decimum vel centesimum clientem eodem `CH_ADDE` inserere sine mutatione formae registri.

## Puritas

Post bootstrap UEFI minimum, registrum, nodi, superficies, eventa, dispatchus, compositor et input omnia VINDEX sunt.

Nullum `POLLE()`. Nullum runtime C, C++, Rust aut ASM.

**Non sunt sloti. Sunt clientes.**

**Sylvia cogitat, currit et vivit in VINDEX.**
