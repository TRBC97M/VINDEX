# ARCHIVUM — historique des échanges

Ce dossier conserve l'historique des sessions de travail entre Numi et les
agents contributeurs, sous une forme lisible par un humain **et par l'autre
agent**.

## Pourquoi

La coordination passe aujourd'hui par `CONSILIUM.md` (l'état), les PR (le
raisonnement d'un chantier) et les rapports (les investigations). Mais
beaucoup de choses se décident en conversation et n'apparaissent nulle
part : pourquoi une option a été écartée, quelle piste a déjà été essayée
sans succès, quel argument a tranché un choix de syntaxe.

Ces informations ont une valeur pratique directe. Un exemple réel : les
sections VIII et IX de `RELATIO-CASUUM-LIMITUM.md` ont évité de refaire
trois corrections déjà tentées et déjà invalidées. Sans elles, le même
travail aurait été repris de zéro.

L'archive rend ce type de contexte accessible aux deux côtés.

## Ce qui est conservé

- les messages de Numi ;
- les réponses textuelles de l'agent ;
- une ligne par action exécutée, avec sa description.

## Ce qui est écarté, et pourquoi

- **le raisonnement interne** : c'est du brouillon, non destiné à autrui, et
  il constitue la majeure partie du volume ;
- **les sorties brutes d'outils** : des milliers de lignes de journaux QEMU
  ou de compilation, dont la conclusion figure déjà dans la réponse.

Mesure : **39 Mo bruts → 1,9 Mo**, soit 5 %. La coordination ne perd rien ;
seul le bruit disparaît.

## Mise à jour

```
python3 archivum/extrahe_archivum.py
```

Le script relit les transcriptions de session et régénère les extraits.
À relancer après chaque session pour que l'archive reste à jour.

## Note aux deux agents

Cette archive est asymétrique par nature : elle contient les sessions de
Claude, pas celles de ChatGPT. Un terme comme « La Passe Génocidaire », par
exemple, n'y apparaît nulle part — il vient de l'autre versant du projet.

C'est précisément l'intérêt d'archiver des deux côtés : chacun détient des
morceaux que l'autre n'a pas.

Voir `INDEX.md` pour la liste des sessions.
