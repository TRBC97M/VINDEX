# P16-IV — Catalogus applicationum Sylviae

## Propositum

P16-IV fontem unicum metadatae applicationum introducit. INITIUM, bureau, tituli fenestrarum et taskbar non amplius duas applicationes ex ramis fixis cognoscunt; eundem registrum dynamicum VINDEX consulunt.

Hoc incrementum inter P16-III et futurum systema processuum sedet. P16-III launch graphicae sessionis probavit; P16-IV declarat **quid applicatio sessionis sit et quomodo facies systematis eam reperiat**.

---

## Registrum

Fasciculus canonicus:

`bibliotheca/applicationes_registrum_iv.vindex`

Caput registri tres campos continet:

1. numerum applicationum;
2. primum nodum;
3. ultimum nodum.

Unusquisque nodus continet:

- `id` applicationis;
- `cliens` Fenestralis;
- `genus` applicationis;
- `nomen` ut descriptor `TEXTUS`;
- indicium utrum in bureau appareat;
- nexum ad nodum proximum.

Nodi per `RESERVA_OCTETA` singillatim reservantur. Nulla capacitas parva fixa catalogo imponitur. Ordo insertionis servatur, ut idem ordo a pluribus partibus faciei systematis sumi possit.

Duplicatio eiusdem clientis in catalogo reicitur.

---

## Unus fons canonicus

Initio sessionis PROGRAMMATA et TABULA adhuc clientia systematis creantur, sed post P16-IV nomina earum et praesentia graphica per registrationes ordinarias fiunt:

```text
PROGRAMMATA → cliens 1 → genus 1 → in bureau
TABULA      → cliens 2 → genus 2 → in bureau
```

Haec non sunt duo sloti architectonici. Sunt tantum primae duae applicationes hodiernae registratae.

Ex eodem registro:

- bureau iconas enumerat;
- INITIUM applicationes enumerat;
- hit-testing applicationem ad clientem convertit;
- fenestra titulum accipit;
- taskbar nomen applicationis reperit.

Ita additio applicationis novae non postulat ramum novum `SI genus==...` in navigatione systematis.

---

## Dispositio bureau

Bureau applicationes quae indicium `in_bureau` habent per ordines et columnas disponit.

Primae duae registrationes servant metra P16-III:

- prima icona incipit ad `y = 72`;
- secunda ad `y = 176`;
- latitudo et altitudo iconarum canonicae manent.

Numerus ordinum ex altitudine reali framebuffer et taskbar computatur. Cum columna impletur, sequens applicatio in columnam proximam transit. Hoc veterem assumptionem duorum locorum fixorum tollit.

---

## Dispositio INITIUM

INITIUM eodem ordine catalogi utitur.

Ad duas applicationes metra P16-II servantur: pannus 320×260 et itema ad positiones veteres. Cum applicationes crescunt:

- altitudo menu secundum numerum itemorum crescit usque ad spatium verticale utile;
- deinde itema in columnas transeunt;
- latitudo panni secundum columnas crescit.

Hoc primum fundamentum catalogi generalis est; scrolling, quaestio, categoriae et alia instrumenta usabilitatis futura huic contractui superponi possunt.

---

## Launch sessionis

Clic in INITIUM vel bureau:

1. id applicationis e nodo catalogi capit;
2. clientem Fenestralis e metadata legit;
3. fenestram clientis in registro fenestrarum reperit;
4. statum fenestrae ad apertum restituit;
5. focus et ordo Z per registrum Fenestralis administrantur;
6. INITIUM clauditur.

Clausura fenestrae clientem aut applicationem e catalogo non delet. Ideo eadem applicatio ex bureau vel INITIUM iterum aperiri potest.

---

## Probatio regressiva

`probationes/applicationes_registrum_iv.vindex` **XCVI applicationes** in uno registro creat.

Probatio comprobat:

- ids crescere;
- numerum XCVI servari;
- primum et ultimum nodum recte teneri;
- totam catenam sine limite parvo percurri;
- quaestionem per id et clientem;
- genus et indicium bureau;
- descriptor `TEXTUS` nominis;
- duplicationem clientis reici;
- numerum registri post reiectionem immutatum manere.

Probatio in suite canonica `tests/run_tests.sh` includitur.

---

## Quod P16-IV non fingit

Catalogus non est processuum manager.

P16-IV nondum praebet:

- creationem novi processus VINDEX;
- isolationem memoriae inter applicationes;
- installationem vel remotionem persistentem;
- manifestum e disco lectum;
- permissiones;
- lifecycle processuum independentium.

Clientia hodierna in eadem sessione Fenestralis iam registrata sunt. P16-IV metadata et navigationem generalizat sine falso processuum subsystemate simulato.

---

## Catena

```text
OVMF
  → BOOTX64.EFI [VINDEX]
  → FENESTRALE II [VINDEX]
  → PS/2 [VINDEX]
  → REGISTRUM APPLICATIONUM
      ↘ INITIUM
      ↘ BUREAU
      ↘ FENESTRAE
      ↘ TASKBAR
  → FRAMEBUFFER
```

Nullus runtime C introducitur.

**VINDEX Latine cogitat. Sylvia Latine loquitur.**
