# Session ChatGPT — P0/P9 : diagnostics stricts du compilateur

_Reconstruction de coordination, non verbatim._
_La transcription intégrale de cette période n'est pas disponible dans les partages récupérables. Ce fichier conserve les causes, pistes déjà tentées et corrections recoupées avec les PR canoniques._
_Période couverte : 4 septembre 2026._
_Sources de contrôle : PR #186/#187, tests de régression et rapport de cas limites._

---

## Défaut P0 : le niveau supérieur avalait l'inconnu

Cas déclencheur : `STRUCTURA` n'existait pas encore dans VINDEX mais pouvait être placé au niveau supérieur sans diagnostic. À l'intérieur d'une fonction, un mot inconnu était déjà rejeté. Le danger était donc une fausse croyance sur les capacités du langage.

Une première piste avait déjà été tentée ailleurs : ajouter une garde dans le `ALITER` final du grand balayage top-level. Cette piste ne devait pas être répétée telle quelle, car cet `ALITER` servait aussi de béquille implicite à des constructions valides mal consommées.

L'instrumentation a établi trois causes distinctes :

1. `IMPORTA` cherchait le premier `.` après le mot-clé, y compris les points contenus dans le chemin importé ;
2. le chemin `FUNCTIO PRINCIPALIS` terminait par `i = n` et cachait tout texte top-level placé après la fonction ;
3. `FORMA` ne consommait pas le `.` de `FIN-FORMA.` ; l'ancien fourre-tout avalait donc à la fois des erreurs et ce terminateur valide.

    [action] PR #186 : `IMPORTA` consomme la chaîne puis son vrai terminateur, `PRINCIPALIS` rend la main au top-level, `FORMA` consomme son point, et tout octet top-level non reconnu produit `ERRATUM: clavis ignota ad gradum supremum est`, exit 65.

Le drapeau `inter_definitiones` envisagé n'a finalement pas été nécessaire : chaque construction reconnue doit simplement rendre le parseur top-level dans un état propre.

## P9 : terminaison stricte des fonctions

Après la fermeture des autres trous du parseur, deux cas restaient : `PRINCIPALIS` dupliquée et `FIN-FUNCTIO` absent.

    [action] PR #187 : diagnostics XI (`FUNCTIO PRINCIPALIS bis definita est`) et XII (`FIN-FUNCTIO deest`), reconnaissance stricte par `EST_FIN_FUNCTIO`, arrêt d'`ANALYSA_BLOCUS` lorsqu'une nouvelle déclaration top-level `FUNCTIO` apparaît dans un corps non fermé.

## Oracles non négociables

- exit 65 et aucun binaire publié pour les sources invalides ;
- fichier/ligne/colonne exacts, y compris à travers `IMPORTA` ;
- point fixe auto-hébergé `G2 = G3` ;
- suite canonique complète ;
- ATMOS/POC non modifiés ne doivent pas changer de code généré à cause d'une correction de diagnostic.

## Leçon de coordination

Avant de corriger un « trou » du parser, vérifier si l'octet avalé n'est pas la conséquence d'une construction précédente mal terminée. Transformer le fourre-tout en erreur sans nettoyer les sorties des constructions reconnues peut casser des sources valides tout en masquant la vraie cause.