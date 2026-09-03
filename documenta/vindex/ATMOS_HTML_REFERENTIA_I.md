# ATMOS — REFERENTIA MORUM HTML I

## Propositum

Hoc documentum non JavaScript in VINDEX transferre iubet. Ludum HTML a domino
proiecti datum ut **specificationem morum** legit, ut clientes VINDEX ad ludum
verum redeant neque POC simplicior pro consilio originali habeatur.

Regula migrationis: mechanismus in VINDEX denuo scribitur; codex HTML/JS non
intrabit in runtime, in compilatorem aut in arborem canonicam ATMOS.

## I. Nucleus navigationis

Gameplay primarius non est `ascende/descende` per bullas. In versione HTML:

1. navis positionem continuam mundi `(x,y)` habet;
2. sonar spatium circa navem ostendit;
3. lusor punctum sonar mure eligit;
4. punctum screen ad coordinatas mundi convertitur;
5. destinatio ultra radium sonar ad marginem radii stringitur;
6. navis progressive ad destinationem movetur;
7. linea cursus, distantia et ETA ostenduntur;
8. oxygenium et energia motu consumuntur;
9. post adventum contactus, nodi, stationes et zona regenerantur/tractantur.

`COMMUNE/navigatio.vindex` hunc contractum VINDEX purum incipit.

## II. Profunditas

Profunditas non est axis manualis principalis. Post motum, regio mundi,
distantia a centro mundi et variatio localis bathymetriam determinant.
Ita navis per mundum 2D navigat et fundus maris profunditatem imponit.

Consequentia: actiones historicae POC `DOWN` et `UP` sunt scaffolding probationis,
non gameplay canonicus futurus.

## III. Camera et sonar

- camera navem sequi potest;
- zoom sonar mutabilis est;
- lusor cameram a nave separare et postea recentrare potest;
- entitates mundi ad screen per centrum camerae et scalam convertuntur;
- tantum contactus intra radium detectionis ostenduntur;
- stationes, bases, nodi, convoys et hostiles eodem spatio mundi coexistunt.

## IV. Tempora simulationis

Duae scalae distinctae sunt:

- motus visibilis interpolatur continue dum navis iter facit;
- mundus vivus circa quater per secundum (`~250 ms`) mutatur;
- drain longior oxygenii/energiae circa intervalla secundorum fit;
- systemata rara (radio, bella territorialia, eventa profunda) cadence propria habent.

VINDEX debet simulationem a presentatione separare; FPS non debet directe
mutationes oeconomiae aut mundi multiplicare.

## V. Pausa et overlays

Versio HTML simulationem sistit cum menu, settings, codex, map, profile,
factiones, quest log, dock, setup, tutorial aut game-over apertum est.
Pausa manualis quoque est.

Client VINDEX futurus eandem notionem `status simulationis` explicite habebit.

## VI. Contactus et actio

Contactus non sunt solum numerus sectoris. Sunt entitates spatii cum positione,
distantia, genere, factione/hostilitate et actionibus. Lusor potest:

- contactum eligere;
- ad eum appropinquare;
- stationem petere et dockare;
- nodum mineralem intrare et extractionem continuam incipere;
- hostiles eligere et pugnare;
- structures, convoys et bases in mundo invenire.

## VII. Mundus vivus

Referentia HTML iam continet fundamenta ad:

- factiones et reputationem;
- bellum territoriale off-screen;
- commercium et convoys mobiles;
- NPC traffic;
- stationes et docking;
- player outposts et drones;
- resource nodes et extractionem continuam;
- structures explorabiles;
- The Below;
- quests/contracts/bounties;
- real-time combat;
- weather, fatigue, corruption et economy.

Haec non omnia simul transferenda sunt. Ordo migrationis debet a nucleo
navigationis et interactionis incipere.

## VIII. Ordo migrationis post Stabilitas I

1. fenestra Win32 vera: move/minimize/maximize/resize/close;
2. navigatio continua sonar et destinatio mure;
3. navis + camera + transform mundus/screen;
4. bathymetria regionalis et costus itineris;
5. contactus spatiali positione;
6. stationes + docking;
7. resource nodes + mining continuum;
8. pause/menu/save UX;
9. deinde mundus vivus, factiones et combat.

## IX. Puritas

Haec referentia HTML est documentum specificationis tantum. Productum VINDEX:

- non includet HTML;
- non includet JavaScript;
- non utetur WebView/browser runtime;
- mechanismos hic descriptos VINDEX puro reimplementabit;
- manebit sub `La Passe Genocidaire`.
