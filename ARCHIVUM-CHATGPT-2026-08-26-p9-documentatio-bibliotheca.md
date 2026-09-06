# Session ChatGPT — P9 : documentation canonique et bibliothèque standard

_Source : partage public ChatGPT `6a8f6eea-e288-83eb-bb01-8517defcac58`, récupéré et expurgé le 6 septembre 2026._
_Le partage expose surtout les réponses/actions ChatGPT ; aucun message utilisateur manquant n'est reconstruit._
_Raisonnement interne et sorties brutes d'outils omis._

---

## Documentation canonique

ChatGPT commence par réconcilier `CONSILIUM.md`, `ARCHITECTURA.md` et `LEGE-ME.md` avec l'état réel du dépôt, sans toucher au travail UEFI de Claude.

    [action] Vérifier les PR Officina/Fenestrale et l'architecture courante.
    [action] Corriger `CONSILIUM.md` pour refléter Fenestrale II Purus I fusionné, Officina canonique et les PR réellement ouvertes.
    [action] Ne pas modifier arbitrairement `VERSION` : documenter la divergence historique 0.51/0.53 au lieu d'inventer une release.
    [action] Ouvrir puis fusionner la PR documentaire #100.

`REFERENTIA.md` est ensuite identifié comme obsolète : références à GTK, `make systema`, BIOS/VGA, limite de 6 paramètres et limite source 212999 octets alors que ces points ne décrivent plus l'état canonique.

    [action] Transformer `REFERENTIA.md` en référence de langage actuelle : `TEXTUS`, 7 arguments SysV certifiés, PE/Win64, `PROIECTUM`, diagnostics structurés, buffers dynamiques et court-circuit.
    [action] Canoniser cette réconciliation documentaire par la PR #101.

## Premier incrément P9 sans toucher au compilateur

Pour éviter les conflits avec le chantier UEFI de Claude, la prochaine capacité est ajoutée entièrement en VINDEX standard : une collection dynamique de `NUMERUS`.

API minimale retenue : création, ajout, lecture, écriture, suppression, purge, comptage et libération.

    [action] Implémenter la collection chaînée dynamique en VINDEX pur.
    [action] Tester suppression tête/milieu/fin, valeur 0, index invalide, purge puis réutilisation, libération finale.
    [action] Ajouter le test au harnais canonique.

La suite atteint `24 probationes rectae; 0 errata` sans modification du compilateur. `RESERVA_OCTETA` + `LIBERA` suffisent donc déjà à construire une abstraction dynamique générale.

    [action] Ouvrir et fusionner la PR #102 ; la collection devient canonique.

## Enrichissement TEXTUS et échec utile

Le chantier suivant ajoute des opérations de texte (`VACUUS`, recherche/contenance, préfixe/suffixe). La première CI provoque un segfault dans le nouveau test.

Hypothèse initiale : `textus + 16` est interprété comme concaténation et non comme arithmétique d'adresse.

    [action] Inspecter l'ABI de `TEXTUS` et l'accès au descripteur interne.

Une première tentative avec `CONTENTUM(SEDES(textus))` ne suffit pas. Au lieu de continuer à deviner, décision de créer une petite sonde VINDEX isolée qui affiche les valeurs observables (`LONGITUDO`, `SEDES(textus)`, `CONTENTUM(SEDES(textus))`) sans déréférencement dangereux.

    [action] Créer une sonde ABI `TEXTUS` temporaire avant toute nouvelle primitive.

Le document historique confirme la représentation `{longueur, capacité, octets}`, mais la question restante est la manière dont la valeur brute est exposée par le langage quand le type statique est `TEXTUS`.

La session partagée s'arrête à cette sonde : aucun succès ultérieur n'est inventé ici.