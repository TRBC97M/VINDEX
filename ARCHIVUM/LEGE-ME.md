# ARCHIVUM — memoria communis colloquiorum

Omnia colloquiorum archiva in **uno directorio `ARCHIVUM/` ad radicem `main`** congregantur.

Haec dispositio radicem repositorii non onerat, memoriam tamen communem uno accessu praebet.

## De dispositione decreta

Prima tentatio singula archiva directe in radice `main` posuerat, ut statim conspicerentur. Haec dispositio nimis onerosa visa est atque expresse relicta est.

Conventio canonica hodierna igitur est:

- **unum tantum directorium `ARCHIVUM/` in radice**;
- omnia archiva Claude et ChatGPT in hoc directorio manent;
- `INDEX.md`, `LEGE-ME.md` atque instrumenta sustentationis in eodem directorio manent;
- dispositio transitoria, qua multi fasciculi `ARCHIVUM-*` directe in radice iacebant, **non restituenda est** nisi auctor principalis, sub nominibus Numi, TRBC97M vel Morgan agnitus, novam directivam explicitam det.

Haec nota eo ipso scripta est, ne futurus agens gradum historicum cum conventione finali confundat.

Conventio interna:

- `CLAUDE-*.md` — sessiones ex parte Claude;
- `CHATGPT-*.md` — sessiones ex parte ChatGPT;
- `INDEX.md` — index communis;
- `extrahe_archivum.py` — regenerator sessionum Claude;
- `verifica_secreta.py` — inspectio secretorum ante publicationem.

## Cur

Coordinatio iam utitur `CONSILIUM.md` ad statum, PR ad rationem operis, relationibus ad investigationes. Multa tamen in colloquiis decernuntur quae nusquam alibi apparent: cur via aliqua relicta sit, quae tentatio iam facta et irrita fuerit, quod argumentum electionem syntacticam vel architectonicam direxerit.

Haec indicia utilitatem practicam directam habent. Sectiones VIII et IX `RELATIO-CASUUM-LIMITUM.md`, exempli gratia, prohibuerunt ne tres correctiones iam temptatae atque reiectae iterum fierent. Similiter ex parte ChatGPT, decreta sicut « La Passe Génocidaire », reiectio basis experimentalis ATMOS, vel restrictio VIRGL ex RGBA praemultiplicato orta nunc a Claude relegi possunt.

## Quae servantur

- nuntii auctoris principalis, sub nominibus Numi, TRBC97M vel Morgan, cum in fonte praesto sint;
- responsa textualia agentis;
- una linea `[action]` pro unaquaque operatione coordinationi utili;
- decreta, viae reiectae, oracula atque eventus qui impediunt ne idem opus denuo incipiatur.

## Quae excluduntur

- **ratiocinatio interna**: rudimentum aliis non destinatum neque ut pactum coordinationis utile;
- **exitus instrumentorum integri**: milia linearum QEMU vel compilationis, quarum conclusio utilis servatur;
- **URL temporaria subscripta atque adiuncta magna**: munus eorum summatim describitur, non octeta integra servantur.

Prima pars Claude circiter **39 Mo rudia -> 1,9 Mo** continebat, id est 5 %. Eadem ratio pro ChatGPT valet: servandus est contextus qui decisionem mutat, non strepitus.

## Origo ChatGPT

Duo genera fasciculorum expresse distinguuntur:

1. **Excerptum communicationis publicae**: textus ex ligamine publico ChatGPT receptus, purgatus atque ab ornamentis interfaciei et instrumentorum mundatus est. Si communicatio tantum partem sessionis continet, fasciculus hoc dicit.
2. **Reconstructio coordinationis, non ad verbum**: transcriptio integra recuperari non potest; servantur tantum decreta et actiones cum PR atque commissis canonicis collatae. Reconstructio numquam tamquam citatio exacta colloquii exhibenda est.

## Renovatio partis Claude

Ex radice repositorii:

```bash
python3 ARCHIVUM/extrahe_archivum.py
python3 ARCHIVUM/verifica_secreta.py
```

Generator sessiones Claude in `ARCHIVUM/` sub nominibus `CLAUDE-*.md` scribit atque `ARCHIVUM/INDEX.md` reficit, inscriptionibus ChatGPT non motis.

## Securitas

Archivum colloquii continere potest quidquid umquam scriptum est. Formae indiciorum GitHub/OpenAI/Slack/GitLab/HuggingFace, claves AWS atque claves privatae ante omnem push expurgandae sunt.

Inspectio automatica iudicium humanum non substituit: omnis catena quae secreto vel credentiali similis est removenda est, etiam si nondum formae notae respondeat.

Vide `INDEX.md` ad indicem sessionum.
