# Praecepta GitHub Copilot pro VINDEX et Sylvia OS

Haec praecepta toti repositorio valent.

## Principia canonica

- `ARCHITECTURA.md` ante omnem mutationem lege et eius principia tamquam canonica considera.
- `CONSILIUM.md` statim post `ARCHITECTURA.md` lege: est tabula operativa canonica quae prioritates, dependentias, curatores, statum et actionem proximam definit.
- Si usor opus novum non expresse delegat, primum opus maximae prioritatis in `CONSILIUM.md` quod `PARATUM` est et non ab alio agente reservatur elige.
- GitHub est fons veritatis huius operis. Si `CONSILIUM.md` a statu reali Git dissentit, Git praevalet et tabula postea corrigenda est.
- Ne utere archivis ZIP aut exemplaribus veteribus tamquam fundamento canonico.
- `CONTRIBUTING.md` et `.github/pull_request_template.md`, ubi adsunt, sunt documenta operativa contributionum et Pull Request.
- Nomina directoriorum agentium historiam originis indicare possunt, sed non sufficiunt ad statuendum fasciculum esse non canonicum. Statum praesentem ramorum et operis inspice antequam directorium historicum vel vetitum iudices.
- VINDEX et Sylvia OS sunt duo opera principalia et distincta: VINDEX est lingua programmandi generalis; Sylvia OS est systema operationale verum et diuturnum quod VINDEX late exercet.
- Mutationes ad VINDEX non tantum propter Sylvia fiant, nisi emendatio generaliter utilis sit; pontes infimi gradus extra VINDEX tantum ubi necessarii sunt admittantur.

## Lingua colloquii et documentatio

- Cum usuario colloqueris, eadem lingua utere qua usor te alloquitur, nisi ipse aliam linguam petit.
- Lingua Latina ad documenta canonica et textus qui in repositorium intrant reservatur; noli responsiones ordinarias usuario Latine reddere nisi id petitum est.
- Omnis documentatio canonica in repositorio tantum Lingua Latina scribatur.
- Commentarii technici, nomina canonica, specificationes, relationes probationum, documenta README et textus projectus Latine scribantur.
- Ne introducas documenta canonica Francogallice, Anglice vel alia lingua.
- Serva identitatem linguisticam VINDEX; ne linguam in syntaxim alterius linguae cum vocabulis Latinis superficialibus redigas.

## Disciplina Git

- Numquam directe in `main` operare.
- Utere ramo proprio ad mutationes, deinde Pull Request crea ante coniunctionem.
- Rami a Copilot creati praefixum `copilot/` habeant.
- Rami aliorum collaboratorum possunt praefixa propria habere, inter quae `chatgpt/`, `claude/` et `gemini/`; noli eos propter praefixum alienum reicere.
- Ramus novus plerumque ex `main` nascatur; ramus super alium ramum poni potest cum dependentia intentionalis est et in Pull Request clare declaratur.
- Postquam usor mutationem vere applicari iussit et fasciculi mutati sunt, mutationes in ramo `copilot/...` committe et ramum ad GitHub mitte, ut aliis collaboratoribus statim visibiles sint.
- Si usor tantum analysim, consilium, recensionem, propositionem aut diff non applicatum petit, nihil committe nec mitte.
- Ante `push`, statum Git inspice et cave ne mutationes alienas, locales aut extra opus praesens forte includas.
- Directorii temporarii synchronizationis, praesertim `.tmp.driveupload/` et `.tmp.drivedownload/`, numquam committantur.
- Si probationes ad mutationem pertinentes exsequi possunt, eas ante `push` exsequere; si non possunt aut deficiunt, hoc clare indica et noli exitum falsum affirmare.
- Post `push`, usuario ramum et SHA commit ultimi indica.
- Noli coniungere mutationes in `main` sine recognitione humana aut probationibus congruentibus.
- Noli delere fundamenta historica VINDEX 0.51 sine causa architecturali probata.

## Compilator et auto-hospitium

- `Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex` compilator auto-hospes criticus est; mutationes ibi minimae, explicabiles et probationibus munitissimae esse debent.
- Auto-hospitium et punctum fixum compilatoris servanda sunt.
- Numquam afirma probationem transisse nisi vere exsecuta est et exitus verificatus est.
- Si probatio deficit, causam distingue antequam plures mutationes coniecturales facias.
- Mutationes diagnosticae temporariae a codice canonico separandae sunt.
- Ne augeas complexitatem compilatoris sine necessitate manifesta.

## Modus operandi

- Ante mutationem amplam, statum praesentem codicis inspice.
- Ante novum opus, statum operis in `CONSILIUM.md` inspice et cum Git reconcilia.
- Praefer mutationes parvas, singulares et facile retractabiles.
- Si opus incertum est, primum analysim fac; noli statim structuram totam reficere.
- Si alius ramus `chatgpt/...`, `claude/...`, `copilot/...` aut `gemini/...` mutationes pertinentes continet, inspice eas ante opus parallelum duplicandum.
- Opus `ACTIVUM` vel `RESERVATUM` ab alio agente non duplica sine recognitione explicita status.
- Post mutationem quae ordinem, statum, dependentiam aut actionem proximam mutat, `CONSILIUM.md` renovandum considera.
- In conflictu inter hoc fasciculum et `ARCHITECTURA.md`, `ARCHITECTURA.md` praevalet. In quaestionibus ordinis operativi, `CONSILIUM.md` praevalet nisi status Git recentior sit.

## Norma qualitatis

- Codex novus formam et syntaxim VINDEX iam exstantem sequatur.
- Nomina significativa et Latina praeferantur ubi pars canonica VINDEX vel Sylvia sunt.
- Mutationes regressiones vitent et compatibilitatem cum codice existente servent, nisi ruptura explicite deliberata est.
- Omnis nova facultas linguistica, si fieri potest, exemplo parvo et probatione acceptationis muniatur.

ARCHITECTURA est lex. CONSILIUM est via. Git historia est.

VINDEX Latine cogitat. Sylvia Latine loquitur.
