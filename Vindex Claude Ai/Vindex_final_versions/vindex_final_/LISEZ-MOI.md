# VINDEX

Un langage de programmation bas niveau à saveur latine/COBOL, compilant
directement vers des exécutables ELF x86-64 Linux, sans dépendance externe
(pas de nasm, pas de gcc, pas de libc).

## État du projet : auto-hébergement complet atteint

VINDEX est désormais **véritablement auto-hébergé**. Le compilateur,
`compilator_decalage.vindex`, est lui-même écrit en VINDEX, et peut se
compiler lui-même indéfiniment en produisant un résultat identique, octet
pour octet, à chaque génération.

Preuve : `compilator_gen3` et `compilator_gen4` (compilateurs de 3e et 4e
génération, chacun produit en compilant la génération précédente) ont un
hachage MD5 strictement identique. C'est un point fixe stable.

### Comment compiler du code VINDEX aujourd'hui

Python n'est plus nécessaire pour l'usage courant. Utilisez le script
`vindexc`, qui enveloppe le compilateur auto-hébergé `compilator_vindex` :

```bash
./vindexc mon_programme.vindex mon_executable
./mon_executable
```

Python (`compilateur.py` et les fichiers associés : `lexeur.py`,
`analyseur.py`, `assembleur.py`, `generateur.py`, `elf.py`) ne sert plus
qu'à l'amorçage historique — reconstruire un tout premier compilateur
VINDEX depuis rien, si `compilator_vindex` venait à être perdu. Pour tout
usage quotidien, `vindexc` suffit.

### Fichiers clés

- `compilator_decalage.vindex` — le code source du compilateur, en VINDEX.
- `compilator_vindex` — le binaire compilé, auto-hébergé, prêt à l'emploi.
- `vindexc` — script d'enveloppe pour compiler facilement un programme.
- `compilateur.py` et fichiers associés — l'amorce historique en Python.

## Bugs de fond résolus lors de la dernière session de débogage

Quatre bugs distincts empêchaient l'auto-hébergement complet, trouvés et
corrigés dans l'ordre suivant :

1. **Tampon de lecture limité à 65536 octets**, codé en dur dans
   `generateur.py` (le compilateur Python) — tronquait silencieusement
   toute lecture de fichier source dépassant cette taille.
2. **Dépilement du 6ᵉ argument manquant** dans la logique d'appel de
   fonction — le mappage des registres s'arrêtait à 5 arguments.
3. **Absence de gestion des références en avant** — le compilateur, en une
   seule passe, ne pouvait pas résoudre un appel vers une fonction définie
   plus loin dans le fichier. Corrigé par un mécanisme de correction
   différée des appels, sur le modèle du correctif de sauts déjà existant.
4. **Débordement du registre de variables locales** (26 → 100
   emplacements) et **zone `es_series` jamais réinitialisée entre
   fonctions** — une fonction ayant beaucoup de variables locales pouvait
   voir une variable héritée du drapeau "tableau/pointeur" d'une variable
   d'une fonction précédente, à cause d'une collision d'indice, causant
   une lecture par adresse (`lea`) au lieu d'une lecture par valeur
   (`mov`).

## Convention linguistique

Le code VINDEX (mots-clés, identifiants, commentaires, chaînes de
caractères affichées) est maintenu en latin. Un audit complet du projet a
été effectué : tout mot français ou anglais résiduel trouvé dans les
identifiants ou chaînes de caractères a été traduit
(`ERROR`→`ERRATUM`, `OK`→`RECTE`, `CARRE`→`QUADRATUM`,
`valeur`→`valor`, `somme`→`summa`, `compteur`→`numerator`, etc.).

Le code Python de l'amorce historique reste en français (choix
intentionnel du projet depuis l'origine) — Python lui-même impose des
mots-clés anglais incompressibles (`def`, `return`, `if`...), donc seule
la partie VINDEX porte l'identité latine du projet.
