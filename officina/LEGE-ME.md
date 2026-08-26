# VINDEX Officina — Gradus B

Officina est ambitus programmationis nativus Windows pro proiectis VINDEX. Gradus B proiectum novum creare potest, manifestum `proiectum.vindex` aperit, arborem fasciculorum ostendit, fontes colorat, mutationes servat, proiectum construit, productum exsequitur atque diagnostica ad lineam et columnam fontis revocat.

Nulla pagina HTML, CSS, JavaScript, navigatrum aut minister interretialis adhibetur. Fenestra per WinForms nativa est; forma et stilus eius in fasciculis Latinis `formae/officina.forma` et `formae/officina.stilus` declarantur.

## Novum proiectum

Actio `NOVUM PROIECTUM` directorium eligit vel creat. Officina ibi sine rescriptione fasciculos canonicos parat:

- `principalis.vindex` — fons initialis VINDEX;
- `proiectum.vindex` — manifestum canonicum R3;
- `programma.exe` — productum PE quod prima constructione generatur.

Si fasciculus canonicus iam exstat, Officina nihil rescribit. Novum proiectum in nova fenestra statim aperitur, ut plura proiecta simul aperta manere possint.

## Usus

Pone `officina_vindex.exe`, `compilator_vindex.exe` et directorium `formae` in eodem directorio. Deinde Officinam aperi aut manifestum argumentum trade:

```text
officina_vindex.exe via\ad\proiectum.vindex
```

Compendia:

- `Ctrl+N` — novum proiectum creat;
- `Ctrl+O` — proiectum aperit;
- `Ctrl+S` — fontes mutatos servat;
- `F7` — proiectum construit;
- `F5` — proiectum construit et exsequitur.

## Architectura

Nucleus linguae VINDEX immutatus manet. Omnis compilatio per contractum canonicum `compilator_vindex PROIECTUM <manifestum>` fit; diagnostica ipsa a compilatore VINDEX oriuntur. Fabrica Gradus B eundem contractum R3 scribit quem compilator et Officina iam legunt.

Contextus applicationis plures fenestras Officinae sustinet; creatio novi proiecti igitur documenta iam aperta non destruit neque claudit.

Gradus posterior orchestrationem processuum in VINDEX transferet postquam ea facultas sub Linux et Win64 canonice definita erit. Sic instrumentum hodie utile est, sine falsa mixtura Officinae, compilatoris et Sylvia-OS.
