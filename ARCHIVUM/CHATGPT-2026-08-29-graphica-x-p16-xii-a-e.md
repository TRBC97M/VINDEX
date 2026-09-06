# Session ChatGPT — Graphica X : P16-XII A à E

_Reconstruction de coordination, non verbatim._
_La transcription intégrale de cette période n'est pas disponible dans les partages récupérables. Ce fichier conserve les décisions, essais, abandons et résultats recoupés avec les PR/commits canoniques ; il ne prétend pas reproduire mot pour mot la conversation._
_Période couverte : 29 août – 5 septembre 2026._
_Sources de contrôle : PR #146, #148, #150, #152, #154 et #155, certifications QEMU/OVMF associées._

---

## Direction retenue

Le but n'est pas de repeindre l'ancien shell mais de donner à Sylvia une vraie pile graphique moderne dont le résultat reste vérifiable. La sémantique doit rester explicite : surfaces RGBA prémultipliées, source-over, dommages régionaux, scènes ordonnées en Z, effets réutilisables, puis migration du shell réel.

    [action] P16-XII-A/#146 : surfaces `GX_*`, alpha prémultiplié, source-over, blur, ombre molle et verre local ; certification réelle puis fusion canonique.
    [action] P16-XII-B/#148 : scène de compositeur, registre de couches, Z-order, backbuffer et présentation damage-only.
    [action] P16-XII-C1/#150 : cache d'effets, masques, blur adaptatif et gloss.
    [action] P16-XII-C2/#152 : pont des assets SIMG/Graphica IX vers les surfaces GX et 9-slice matériel.
    [action] P16-XII-D/#154 : horloge frame, TSC monotone calibré, pacing UEFI et mouvements interruptibles/retargetables.
    [action] P16-XII-E/#155 : migration du shell utilisable (INITIUM, Bureau, fenêtres, Terminal, OFFICINA) sur une vraie scène Graphica X.

## Choix importants

- Le framebuffer et les tests QEMU servent d'oracle : une évolution d'architecture ne doit pas modifier silencieusement les pixels attendus.
- Le temps d'animation vient d'un TSC calibré ; l'UEFI sert de pacer/télémétrie, pas de définition de la durée.
- Les effets graphiques sont des primitives réutilisables, pas des hacks propres à une seule fenêtre.
- La migration du shell ne doit pas casser la persistance d'OFFICINA : deux boots UEFI distincts servent de preuve.

## Ce qui a été écarté

- Considérer une capture jolie comme preuve suffisante : couleurs, damage, canaris et sorties exactes doivent être vérifiés automatiquement.
- Réécrire le shell en parallèle de la nouvelle pile sans fondation/pont : XII-E attend la fondation GX puis migre le shell dessus.
- Faire du firmware/UEFI la sémantique graphique finale : Graphica X reste l'autorité du rendu.