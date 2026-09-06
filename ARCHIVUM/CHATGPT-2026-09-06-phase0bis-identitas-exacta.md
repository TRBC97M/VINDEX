# Session ChatGPT — Phase 0-bis : identité exacte des symboles

_Reconstruction de coordination, non verbatim, fondée sur Git et les sorties GitHub Actions du 6 septembre 2026._

## Contexte

Après relecture intégrale de l’ARCHIVUM, le chantier choisi avant `STRUCTURA I` a été la vérification du fondement d’identité des symboles. F9-II avait déjà corrigé les collisions de variables locales au moyen d’une identité compacte `[position:32 | longueur:32]`, mais il restait à vérifier si cette propriété avait été généralisée au compilateur.

`main` était alors à `3ee03c7d6280b0f154d544d9f50fe791ff52e3b2`. `CONSILIUM.md` était en retard sur Git concernant Graphica X : F9-III avait déjà été fusionné par #194 (`c6516c484fd9e31eab0f982bcfa097fbf776bf9c`) alors que la table annonçait encore F9-II comme prochain incrément.

Branche créée : `chatgpt/phase0bis-identitas-exacta`.
PR : #198 — `P9 Phase 0-bis — identitas exacta symbolorum`.

## Investigation : ce qui était réellement faux

Le compilateur utilisait encore le hash polynomial historique base 31 comme identité suffisante pour plusieurs catégories :

- fonctions via `CERCA_FUNCTIONEM_DYNAMICAM` ;
- formes via `INDEX_STRUCTURAE` ;
- champs via `INDEX_CAMPUS_ULTIMAE_FORMAE` et les recherches `CAMPUS_STRUCTURAE_*`.

Les variables locales, elles, utilisaient déjà l’identité exacte introduite pendant F9-II et ne devaient pas être régressées.

## Fausses pistes réfutées pendant la session

### 1. Mauvaise paire de collision

Une première paire `sx51d7` / `sgdzww` a été utilisée comme si elle produisait une collision dans le hash canonique. La CI a montré que les tests FORMA/champs passaient, ce qui a forcé une vérification du mécanisme de hash.

Conclusion corrigée : cette paire n’était pas l’oracle approprié pour le hash polynomial base 31 du compilateur actuel. La collision déjà documentée `vp` / `x2` donne bien le même hash `3770`.

### 2. Mauvais oracle pour la régression locale

Le test historique `probationes/identificatores_collisionis.vindex` ne produit volontairement aucune sortie : il encode ses assertions dans son code de sortie. Une première workflow attendait à tort du texte et l’a déclaré rouge.

Après lecture du test, l’oracle a été corrigé : sortie vide + code de sortie 0. F9-II a alors été reconfirmé comme correct, et non comme faux vert.

### 3. `vp` / `x2` n’était pas un bon test de fonction

Le chemin canonique des appels de fonction testé ici reconnaît les noms commençant en majuscule. `vp()` / `x2()` produisaient donc `0 / 0`, mais cela ne prouvait pas la collision fonctionnelle recherchée.

Une collision base 31 compatible a été choisie : `AP` et `B1`, car `65*31+80 = 66*31+49 = 2095`.

## Preuves avant correction

Workflow diagnostique : run GitHub Actions `34056694966`.

Résultats :

- locale `vp/x2` : code 0, oracle correct ;
- fonctions `AP/B1` : `222 / 222` au lieu de `111 / 222` ;
- formes `AP/B1` : la valeur `1.5` de la forme FLUITANS était traitée comme NUMERUS et imprimée `4609434218613702656` ;
- champs `vp/x2` : `222 / 222` au lieu de `111 / 222`.

Les trois familles fonctions/formes/champs étaient donc réellement collisionnables ; les locales étaient déjà saines.

## Correction architecturale

Le hash historique n’a pas été supprimé. Il reste un filtre rapide, mais il n’est plus une preuve d’identité.

Le mécanisme généralisé est :

```text
longueur -> hash base 31 -> comparaison des octets exacts
```

L’identité compacte déjà utilisée par les locales est réutilisée :

```text
[position source sur 32 bits | longueur sur 32 bits]
```

Le compilateur ajoute `SIGNUM_IDENTITATIS` et `NOMINA_IDENTITATUM_AEQUALIA`. Les descripteurs de fonctions et de formes conservent aussi le pointeur vers le source afin que la comparaison exacte soit possible. Les clés des tables de fonctions, formes et champs utilisent désormais l’identité compacte au lieu du hash seul.

Aucun ABI public du programme généré n’est modifié et aucune petite limite artificielle de longueur de nom n’est réintroduite.

## Auto-hébergement et preuves après correction

La migration déterministe a d’abord été exécutée dans la CI, puis le compilateur régénéré a été canonisé sur la branche uniquement après succès de toutes les preuves.

Run `34064482693` :

- migration appliquée ;
- `G2 = G3` ;
- locale : code 0 ;
- fonctions : `111 / 222` ;
- formes : `1.500000 / 7` ;
- champs : `111 / 222` ;
- `35 probationes rectae; 0 errata.` ;
- source et binaire compilateur régénéré commités automatiquement (`61c430b...`).

Une workflow permanente, sans migration ni écriture, a ensuite été installée. Run `34064541570` : succès depuis l’état déjà canonisé, avec vérification stricte `G1 = G2 = G3`, collisions exactes et 35/35.

Le migrateur Python temporaire a ensuite été retiré ; il n’appartient pas à la chaîne canonique.

## Conséquence pour STRUCTURA

La Phase 0-bis fournit désormais sur la branche #198 le fondement attendu avant `STRUCTURA I` : les identités de symboles utilisateur ne dépendent plus accidentellement d’une collision de hash pour les locales, fonctions, formes et champs couverts par les régressions.

La prochaine étape logique après fusion et resynchronisation documentaire est `STRUCTURA I`, conformément à `CONCEPTIO-STRUCTURA-REVISA.md`, sans revenir sur cette fondation.

## Canonisation finale

PR #198 a été fusionnée dans `main` par le merge commit `8e9b6a9b602a127b3c6e04a2a314c3361c5ed1bd`.

La preuve permanente a été réexécutée **après fusion sur ce commit de `main`** : GitHub Actions run `34064950925`, job `identitas`, succès. Les logs attestent explicitement :

- `RECTE: G1 = G2 = G3.` ;
- locale `vp/x2` : sortie vide, statut 0 ;
- fonctions `AP/B1` : `111`, puis `222` ;
- formes `AP/B1` : `1.500000`, puis `7` ;
- champs `vp/x2` : `111`, puis `222` ;
- `35 probationes rectae; 0 errata.`

Phase 0-bis est donc close selon la chaîne : implémentation -> preuve -> intégration -> documentation -> mémoire partagée. La prochaine étape canonique est `STRUCTURA I` selon `CONCEPTIO-STRUCTURA-REVISA.md`. F9-IV reste seulement `PARATUM` et ne doit pas être repris implicitement.
