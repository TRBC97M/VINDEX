# Contributio ad VINDEX et Sylvia OS

## Principium

GitHub est fons communis et canonicus progressionis. Historia, rami et Pull Request statum operis definiunt. Directorium propter nomen agentis solum non habendum est vetitum vel historicum; ante iudicium inspicienda sunt `ARCHITECTURA.md`, `CONSILIUM.md`, ramus activus et contextus mutationis.

## Ordo cognitionis communis

Ante opus novum omnis collaborator, sive homo sive agens artificialis, hunc ordinem sequatur:

1. `ARCHITECTURA.md` legat — principia et limites canonicos;
2. `CONSILIUM.md` legat — prioritates, dependentias, curatores, statum et actiones proximas;
3. `main`, ramos pertinentes, Pull Request et probationes recentes inspiciat;
4. caveat ne opus `ACTIVUM` aut `RESERVATUM` ab alio collaboratore duplicetur;
5. nisi usor aliud expresse iubeat, opus maximae prioritatis eligat quod `PARATUM` est et non impeditur.

Si `CONSILIUM.md` et Git dissentiunt, status realis Git praevalet; deinde `CONSILIUM.md` corrigatur. Si `CONSILIUM.md` et `ARCHITECTURA.md` dissentiunt, `ARCHITECTURA.md` semper praevalet.

## Regulae generales

- `main` est linea stabilis communis.
- Omnis operatio nova in ramo separato fiat.
- Nulla mutatio directe in `main` facienda est.
- Pull Request ante coniunctionem ad `main` requiritur.
- Archivorum ZIP vel exempla veterum non sunt fundamentum canonica evolutionis.
- Directorii temporarii synchronizationis, inter quos `.tmp.driveupload/` et `.tmp.drivedownload/`, numquam in historiam Git mittantur.
- Mutatio quae prioritatem, statum, dependentiam, curatorem aut actionem proximam mutat etiam necessitatem renovationis `CONSILIUM.md` inducit.

## Rami collaboratorum

Praefixa agentium servant originem operis:

- `chatgpt/...` pro ChatGPT;
- `claude/...` pro Claude;
- `copilot/...` pro GitHub Copilot;
- `gemini/...` pro Gemini.

Rami humanitus creati alio nomine uti possunt, dummodo `main` directe non mutetur.

Ramus novus plerumque ex `main` creetur. Tamen ramus super alium ramum poni potest si mutatio posterior a priore realiter dependet. Talis dependentia in descriptione Pull Request explicanda est, et basis post coniunctionem mutationis prioris ad `main` transferri potest.

Ramus alienus non est territorium exclusivum, sed opus activum eius non duplicandum est sine inspectione. Si curator tempus, tokena aut instrumenta amittit, status relinquendus est ita ut successor intellegat quid probatum sit, quid desit et quid proximum sit.

## Separatio architecturica

Mutationes distinguendae sunt inter:

1. mutationem linguae VINDEX;
2. mutationem ecosystematis VINDEX;
3. mutationem Sylvia OS;
4. mutationem communem.

Si mutatio grammaticam, ABI, typum, compilatorem aut specificationem afficit, est mutatio VINDEX. Si sola instrumenta, bibliothecae aut Officina tanguntur, est mutatio ecosystematis. Si initium, memoria systematis, fasciculi, fenestrale aut operationes systematis mutantur, est mutatio Sylvia OS. In casu coniunctionis necessitatum, mutatio communis explicite justificetur.

## Regula linguae Sylviae

Post primam translationem imperii ex firmware, **omnis logica Sylvia OS in VINDEX scribenda est**.

Exceptio unica est ponticulus initialis UEFI strictissime minimus. Is framebuffer et metadata firmware obtinere, memoriam initialem reservare, imaginem VINDEX onerare et ad ingressum VINDEX salire potest. Non licet ponticulo postea munus runtime retinere.

Pull Request reicienda est si codex C, C++, Rust, assembly manualis aut alius sermo in Sylvia introducit aliquam ex his rebus:

- ansam eventuum residentem;
- compositionem graphicam aut picturam desktop;
- fenestras, superficies, focus, z-order, taskbar;
- polling clavieris aut muris;
- I/O fasciculorum vel disci runtime;
- allocationem vel administrationem runtime quae a VINDEX continuo revocatur;
- callback, mailbox aut functionem residentem quae VINDEX clientem intra runtime non-VINDEX facit.

Si VINDEX operationem requisitam nondum exprimere potest, mutatio recta est VINDEX ipsum extendere. Circumventio per C non admittitur.

Codex historicus qui hanc regulam violat est debitum migrationis, non praecedens approbandus. Nulla mutatio nova ab eo dependere debet nisi simul ad remotionem eius ducit.

## Disciplina Git

- Ante opus statum praesentem rami et mutationes aliorum inspice.
- Ante opus etiam `CONSILIUM.md` cum statu reali Git reconcilia.
- Mutationes parvae, singulares et retractabiles praeferantur.
- Ante `push`, status Git inspiciatur, ne mutationes alienae aut temporariae includantur.
- Si alius ramus opus pertinens iam continet, prius inspiciatur quam labor parallelus duplicetur.
- Experimentum probatum non integre in `main` miscendum est si structuram historicam vel debitum inutile secum fert; facultas probata in viam canonicam portetur.

## Probationes et qualitas

- Omnis mutatio ad VINDEX aut Sylvia probationem pertinentem aut saltem inspectionem demonstrabilem habeat.
- Compilator auto-hospes et punctum fixum servanda sunt.
- Mutationes regressivae evitandae sunt.
- Nullam probationem transisse affirmare licet nisi vere exsecuta et verificata sit.
- Mutationes Sylviae probare debent nullam novam logicam runtime non-VINDEX introductam esse.

## Pull Request

Pull Request contineat:

- titulum succinctum et descriptivum;
- obiectum et ambitum mutationis;
- genus mutationis: VINDEX, ecosystema, Sylvia OS aut communis;
- fasciculos principales mutatos;
- probationes vel inspectiones exsecutas;
- pericula, limites et eventus notabiles;
- dependentiam ab alio ramo, si adest;
- confirmationem explicitam puritatis VINDEX si Sylvia OS tangitur;
- mutationem status `CONSILIUM.md`, si opus huius tabulae promovetur, impeditur, reservatur aut perficitur.

## Successio operis

Si opus imperfectum relinquitur, successor invenire debet:

- ramum, PR et ultimum commit;
- quod vere probatum est;
- quod adhuc deest;
- pericula et decisiones iam factas;
- actionem proximam concretam.

Haec in `CONSILIUM.md`, descriptione PR, commit aut relatione pertinenti serventur; noli memoriam essentialem tantum in conversatione privata relinquere.

## Conclusio

Disciplina Git progressionem non impedire debet; debet efficere ut opus plurium collaboratorum componi, recognosci et retractari possit sine ambiguitate.

ARCHITECTURA est lex. CONSILIUM est via. Git historia est.

VINDEX Latine cogitat. Sylvia Latine loquitur.
