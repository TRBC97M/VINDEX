# ARCHIVUM — mémoire partagée des échanges

Toutes les archives de conversation sont regroupées dans **le dossier unique `ARCHIVUM/` à la racine de `main`**.

Ce choix évite d'encombrer la racine du dépôt tout en gardant la mémoire partagée accessible en un clic.

Convention interne :

- `CLAUDE-*.md` — sessions issues du versant Claude ;
- `CHATGPT-*.md` — sessions issues du versant ChatGPT ;
- `INDEX.md` — index commun ;
- `extrahe_archivum.py` — régénérateur des sessions Claude ;
- `verifica_secreta.py` — contrôle de secrets avant publication.

## Pourquoi

La coordination passe déjà par `CONSILIUM.md` pour l'état, les PR pour le raisonnement d'un chantier et les rapports pour les investigations. Mais beaucoup de choses se décident en conversation et n'apparaissent nulle part : pourquoi une option a été écartée, quelle piste a déjà été essayée sans succès, quel argument a tranché un choix de syntaxe ou d'architecture.

Ces informations ont une valeur pratique directe. Les sections VIII et IX de `RELATIO-CASUUM-LIMITUM.md`, par exemple, ont évité de refaire trois corrections déjà tentées et invalidées. De la même manière, côté ChatGPT, des décisions comme « La Passe Génocidaire », l'abandon de la base expérimentale ATMOS ou la contrainte VIRGL liée au RGBA prémultiplié peuvent maintenant être relues par Claude.

## Ce qui est conservé

- les messages de Numi lorsqu'ils sont disponibles dans la source ;
- les réponses textuelles de l'agent ;
- une ligne `[action]` par opération utile à la coordination ;
- les décisions, pistes invalidées, oracles et résultats qui évitent de recommencer un chantier.

## Ce qui est écarté

- **le raisonnement interne** : brouillon non destiné à autrui et inutile comme contrat de coordination ;
- **les sorties brutes d'outils** : milliers de lignes QEMU/compilation dont la conclusion utile est conservée ;
- **les URL temporaires signées et pièces jointes volumineuses** : leur rôle est résumé, pas leur octet brut.

Le premier versant Claude mesurait environ **39 Mo bruts -> 1,9 Mo**, soit 5 %. Le principe reste le même pour ChatGPT : garder le contexte qui change une décision, pas le bruit.

## Provenance ChatGPT

Deux types de fichiers sont distingués explicitement :

1. **Extrait de partage public** : le texte a été récupéré depuis un lien public ChatGPT, expurgé et nettoyé du chrome UI/outils. Si le partage ne contient qu'une partie de la session, le fichier le dit.
2. **Reconstruction de coordination, non verbatim** : la transcription complète n'est pas récupérable ; seules les décisions et actions recoupées avec les PR/commits canoniques sont conservées. Une reconstruction ne doit jamais être présentée comme une citation exacte de la conversation.

## Mise à jour du versant Claude

Depuis la racine du dépôt :

```bash
python3 ARCHIVUM/extrahe_archivum.py
python3 ARCHIVUM/verifica_secreta.py
```

Le générateur écrit les sessions Claude dans `ARCHIVUM/` sous `CLAUDE-*.md` et reconstruit `ARCHIVUM/INDEX.md` sans déplacer les entrées ChatGPT.

## Sécurité

Une archive de conversation peut contenir tout ce qui a été tapé. Les motifs de jetons GitHub/OpenAI/Slack/GitLab/HuggingFace, clés AWS et clés privées doivent être expurgés avant tout push.

Le contrôle automatique ne remplace pas le jugement humain : toute chaîne ressemblant à un secret ou credential doit être retirée même si elle ne correspond pas encore à un motif connu.

Voir `INDEX.md` pour la liste des sessions.
