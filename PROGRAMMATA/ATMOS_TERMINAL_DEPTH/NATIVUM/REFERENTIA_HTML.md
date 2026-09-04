# ATMOS NATIVUM — Referentia morum HTML

Hoc documentum non est translatio JavaScript. Est tabula contractuum observatorum in versione HTML auctoris, ad implementationem VINDEX dirigendam.

## Nucleus ludi

Status initialis HTML continet oxygenium, energiam, integritatem, profunditatem et credita; praeterea inventarium, upgrades, statistica, reputationes factionum, positionem navis et progressum mundi.

## Sonar et motus

- Sonar est spatium principale interactionis.
- Clic in sonar convertitur ad punctum mundi circa positionem navis.
- `travelToPoint` in fonte HTML movet navem progressive; destinationem non teletransportat.
- Scala sonaris mutat conversionem screen ↔ mundus.
- Player est centrum referentiae sonaris; entia mundi moventur visualiter relative ad eum.

## Resource nodes

- Nodum mineralem cliccare eligit punctum exactum intra zonam depositi.
- Si punctum cliccatum excedit radium depositi, destination est clampata intra zonam.
- Si navis nondum est in zona, APPROACH movet ad marginem/interiorem zonae.
- Adventus ad nodum incipit extractionem continuam.
- Extractio manet activa dum navis satis prope est et consumit resources ad intervalla.
- Mutatio destinationis potest extractionem interrumpere.

## Contactus et mundus

- Contactus/NPC habent coordinatas mundi proprias.
- Densitas traffic est proceduralis et potest crescere circa stationes.
- Stationes et bases sunt entia mundi; clic → course, deinde docking si intra radium.
- Mundus est streaming/proceduralis, non grille quattuor directionum.

## Profunditas

Profunditas sequitur regionem/positionem mundi et progressionem abyssalem. NATIVUM non exhibet `DOWN`/`UP` ut mechanicam navigationis principalem.

## Pause et cadentiae

HTML distinguit plures cadentias et sistit simulationem dum menus/overlays pertinents aperti sunt. NATIVUM idem principium servabit:

- input/render;
- motus et simulation mundi;
- drain oxygenii/energiae;
- extraction;
- autosave.

## Save

HTML servat multo plus quam POC ATD1/ATW1: status, inventarium, upgrades, rep factionum, positionem player, discovery, statistica, contracts, bases, dock, pilot/ship, weather/economia, quests/bounties et alia.

NATIVUM ideo formatum save proprium versionatum accipiet. Compatibilitas cum save POC non est obligatoria; POC sunt probationes historicae, non specificatio ludi.

## Regula migrationis

Quisque subsystema habet:

1. contractum ex HTML;
2. implementationem VINDEX propriam;
3. regressionem deterministicam ubi possibile;
4. probationem Windows realem;
5. test humanum antequam subsystema dependentia supra eum construantur.
