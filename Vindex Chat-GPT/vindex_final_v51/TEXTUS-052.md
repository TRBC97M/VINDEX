# VINDEX 0.52 — TEXTUS

`TEXTUS` est genus nativum VINDEX ad textum dynamicum tractandum. Propositum est usum manualem `ORDO DE LITTERA` et constructionem octetorum singillatim minuere, praesertim in Sylvia OS, Officina et instrumentis lineae mandatorum.

## Contractus primae implementationis

Prima implementatio completa has proprietates praebere debet:

```vindex
DECLARA nomen SICUT TEXTUS VALENS "Sylvia".
DECLARA systema SICUT TEXTUS VALENS nomen + " OS".
PROCLAMA systema.
```

### Operationes

- litterale inter `"..."` ad `TEXTUS` assignari potest;
- `+` duos textus concatenat;
- `==` et `!=` contentum comparant, non sedes memoriae;
- `LONGITUDO(textus)` numerum octetorum utilium reddit;
- `PROCLAMA textus.` contentum exhibet;
- `TEXTUS` parametrum functionis esse potest;
- assignatio inter variabilia `TEXTUS` sustinetur.

## Repraesentatio 0.52

`TEXTUS` valor in ABI est acus ad structuram memoriae administratam:

```text
+0   longitudo : u64
+8   capacitas : u64
+16  octeta UTF-8 ...
```

Longitudo terminatorem nullum non numerat. Octeta post contentum terminatore nullo clauduntur ut pons cum API C et viis fasciculorum facilior sit. Capacitas spatium contenti, non caput, significat.

Prima versio UTF-8 octeta conservat; `LONGITUDO` igitur octeta numerat. Numeratio scalarum Unicode potest postea separata operatione addi sine ABI frangendo.

## Memoria

Litteralia possunt in regione immutabili binarii vivere. Resultata concatenationis memoriam dynamicam accipiunt. In 0.52 non introducitur garbage collector: vita valorum dynamicorum sequitur mechanismos memoriae VINDEX existentes. Designatio futura ownership/refcounting separatim tractabitur; implementatio initialis non debet auto-hospitium compilatoris frangere.

## Compatibilitas

`ORDO DE LITTERA` manet validum. `TEXTUS` non eum substituit in codicibus humilibus, bufferibus magnitudine fixa, rectoribus aut locis ubi collocatio exacta memoriae necessaria est.

## Probatio canonica

`examples/textus_052.vindex` est programma acceptationis. TEXTUS non habetur completum donec illud a compilatore auto-hospite compilatur, exsecutio exitum rectum reddit, et probationes 0.51 regressiones non ostendunt.
