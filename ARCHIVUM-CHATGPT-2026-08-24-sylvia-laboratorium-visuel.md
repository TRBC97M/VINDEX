# Session ChatGPT — Sylvia Laboratorium : bureau, texte et souris UEFI

_Source : partage public ChatGPT `6a8ccb26-10d0-83eb-a297-0cd01c6aaf44`, récupéré et expurgé le 6 septembre 2026._
_Les nombreuses images générées et captures sont réduites à leur rôle de coordination ; les URL temporaires signées ne sont pas conservées._
_Raisonnement interne et sorties brutes d'outils omis._

---

## Contexte visuel

La session contient de nombreuses itérations de guides de style JL-UX/Sylvia et de captures du bureau. Leur valeur pour la coordination est la direction retenue : un shell Sylvia visuellement moderne, distinct, avec guides de fenêtres, contrôles et icônes, puis certification dans le Laboratorium réel.

    [action] Générer et comparer plusieurs guides de style JL-UX, fenêtres/contrôles, icônes et bureaux Sylvia.

## Numi

« alors, cool, mais là ya rien qui charge, je ne peux pas vraiment cliquer dessus, ça ne fais rien »

Puis :

« alors, oui, je vois le bureau, plus ou moins, ya rien, je ne peux pas bouger la souris, mais c'est déjà bien je présume »

Puis encore :

« toujours pareil, et la souris ne bouge pas, bref »

Numi signale également voir « un truc tiano core ».

## ChatGPT

Le diagnostic QEMU/OVMF finit par prouver :

```text
QEMU: RESOLUTIO 1280x800
QEMU: GLYPHI_TITULI 336
QEMU: DESKTOP RECTE
QEMU: TEXTUS RECTE
```

Le bureau et les textes fonctionnent donc réellement. Le rendu de texte du Laboratorium a été remplacé par un rendu ASCII 8x8 natif VINDEX alimenté par une ressource préparée au bootstrap.

Le point restant est `QEMU: MURUS DEFECIT` : la souris n'est pas encore certifiée.

    [action] Remplacer l'ancien test HMP par un canal QMP séparé utilisant `input-send-event` et des coordonnées absolues pour `usb-tablet`.

État stable annoncé : bureau OK, texte OK, souris encore en cours de certification.

## Numi

« continue »

## ChatGPT

L'isolation progresse : les deux protocoles souris UEFI sont trouvés — Simple Pointer et Absolute Pointer — et le blocage se produit au premier appel `GetState` depuis VINDEX.

Le problème n'est donc plus VNC, `LocateProtocol`, `Reset` ou l'absence de `usb-tablet`. Le suspect devient l'adresse du buffer passée à `GetState`, notamment `SEDES(data)` pour un `ORDO`.

État à préserver : desktop OK, texte OK, protocoles souris détectés, premier `GetState` encore à corriger.

## Numi

« continue »

## Actions de poursuite visibles dans le partage

    [action] Inspecter le compilateur, les tests UEFI et les exécutions CI afférentes.
    [action] Comparer les artefacts visuels extraits des captures.
    [action] Mettre à jour le test UEFI et vérifier le workflow GitHub.
    [action] Analyser l'ELF embarqué et désassembler les appels UEFI.
    [action] Analyser le blocage USB UEFI et inspecter les marqueurs de pixels.
    [action] Modifier la sélection du pointeur et réexaminer les exécutions QEMU.

La session partagée s'arrête pendant cette investigation ; elle ne prétend pas que la souris est déjà résolue.