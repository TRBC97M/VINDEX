# Bibliotheca VINDEX

Bibliotheca VINDEX codicem communem continet quem programmata per `IMPORTA` adhibere possunt.

## TEXTUS

`textus.vindex` operationes communes generis `TEXTUS` definit. In VINDEX 0.52 prima operatio est:

- `LONGITUDO(textus)` — numerum octetorum utilium descriptoris reddit.

Exemplum:

```vindex
IMPORTA "bibliotheca/textus.vindex".

DECLARA nomen SICUT TEXTUS VALENS "Sylvia".
PROCLAMA LONGITUDO(nomen).
```

## Graphica

`graphica.vindex` definit conventiones inter applicationes VINDEX et motorem Formarum GTK. Applicatio manet dominus eventuum: VINDEX eventum elementorum accipit, logicam suam perficit et responsum ad formam reddit.

Officina et Salutatio eodem ponte utuntur. Pons formam legit, elementa libere creat, dialogos systematis aperit, valores exportat atque eventa transmittit; neque Officinam novit neque programma VINDEX exsequitur.

Conventiones eventuum praesentium:

- `GRAPHICA_EVENTUM_NOVI()`;
- `GRAPHICA_EVENTUM_APERTIONIS()`;
- `GRAPHICA_EVENTUM_SERVATIONIS()`;
- `GRAPHICA_EVENTUM_COMPILATIONIS()`;
- `GRAPHICA_EVENTUM_EXECUTIONIS()`;
- `GRAPHICA_EVENTUM_CLAUSURAE()`;
- `GRAPHICA_EVENTUM_SALUTATIONIS()`;
- `GRAPHICA_COMPILATIO_INCEPTA()`;
- `GRAPHICA_EXECUTIO_INCEPTA()`;
- `GRAPHICA_RESPONSUM_RECTUM()`;
- `GRAPHICA_RESPONSUM_ERRATUM()`.

Numeri bullarum in archivo `.forma` etiam libere eligi possunt. Grammatica Formarum in `formae/LEGE-ME.md` describitur.
