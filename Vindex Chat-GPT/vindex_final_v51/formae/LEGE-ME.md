# Formae Graphicae VINDEX

Forma est descriptio tabulis divisa quam `vindex_graphica` in elementa GTK
convertit. Quodque mandatum unam lineam occupat; campi signo tabulationis
separantur. Lineae `#` incipientes commentaria sunt.

## Elementa

- `FENESTRA` — fenestra cum titulo et magnitudine;
- `VERTICALIS`, `HORIZONTALIS` — dispositiones elementorum;
- `TITULUS` — inscriptio;
- `BULLA` — bulla cum numero eventus unius octeti;
- `EDITOR` — editor fontis volubilis;
- `EXITUS` — textus immutabilis volubilis;
- `CAMPUS_TEXTUS` — campus unius lineae;
- `DIVISOR` — duo spatia mobilia;
- `SEPARATOR` — linea divisoria;
- `STILUS` — stilus GTK externus;
- `ICONA` — imago fenestrae.

Omne elementum identificatorem accipit. Parens ante filium describendus est.
`INITIUM` et `FINIS` locum in dispositione statuunt; in divisore `PRIMUM` et
`SECUNDUM` adhibentur.

## Eventa et responsa

Numerus bullae ad processum VINDEX mittitur. Ante eventum, motor valores
mutabiles in haec archiva exportat:

```text
.vindex-graphica-valor-<identificator>
```

`CLAVIS`, `MUS` et `MUTATIO` eventa claviaturae, muris et mutationis textus
elemento sociant. Singula clavis vel muris indicia in
`.vindex-graphica-eventum-<identificator>` scribuntur; clavis numerum GTK,
mus bullam et coordinata continet.

Programma VINDEX unum octetum respondet. Directivae `RESPONSUM` eius effectus
declarant: `TEXTUS`, `TEXTUS_ARCHIVO`, `SENSIBILIS`, `NOVUM`, `APERI`, `SERVA`,
`TITULUS_FENESTRAE` aut `CLAUDE`. Plures actiones eidem numero sociari possunt.

Forma sine sessione graphica verificari potest:

```bash
./vindex_graphica --verifica-formam formae/officina.forma
```

`officina.forma` et `salutatio.forma` duae formae integrae eiusdem motoris
sunt. Fasciculi `.stilus` stilum GTK continent; HTML vel navigatrum non sunt.
