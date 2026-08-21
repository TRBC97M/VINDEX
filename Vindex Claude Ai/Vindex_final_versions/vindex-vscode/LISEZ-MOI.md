# Extension VS Code pour VINDEX

Coloration syntaxique et intégration de base pour écrire du VINDEX
directement dans VS Code — mots-clés, types, chaînes, commentaires,
définitions et appels de fonctions sont tous reconnus et colorés.

## Installation (extension non empaquetée, en local)

1. Copiez tout le dossier `vindex-vscode` dans le dossier d'extensions de
   VS Code :
   - Linux/macOS : `~/.vscode/extensions/vindex-lang/`
   - Windows : `%USERPROFILE%\.vscode\extensions\vindex-lang\`

   ```bash
   cp -r vindex-vscode ~/.vscode/extensions/vindex-lang
   ```

2. Redémarrez VS Code (ou `Développeur : Recharger la fenêtre` depuis la
   palette de commandes, `Ctrl+Shift+P`).

3. Ouvrez n'importe quel fichier `.vindex` — la coloration syntaxique
   s'active automatiquement.

Alternative : depuis la palette de commandes, `Développeur : Installer
l'extension depuis un emplacement...`, puis sélectionnez ce dossier
`vindex-vscode`. Fonctionne sans redémarrage manuel.

## Compiler et exécuter depuis VS Code

Le dossier `exemple-espace-travail/` est un espace de travail VS Code
prêt à l'emploi : ouvrez-le directement (`Fichier > Ouvrir le dossier`).
Il contient :

- `vindexc` et `compilator_vindex` — le compilateur auto-hébergé et son
  enveloppe (aucune dépendance à Python).
- `salve.vindex` — un premier programme d'exemple.
- `.vscode/tasks.json` — deux tâches prêtes à l'emploi :
  - **VINDEX: Compilare** (`Ctrl+Shift+B`) — compile le fichier ouvert.
  - **VINDEX: Compilare et Exsequi** (palette de commandes → `Exécuter
    la tâche de test`) — compile *et* exécute, résultat affiché dans le
    terminal intégré.

Pour utiliser ceci dans votre propre projet, copiez simplement
`vindexc`, `compilator_vindex` et le dossier `.vscode/` à la racine de
votre espace de travail.

## Ce que ça ne fait pas (encore)

Pas de coloration sémantique (résolution de types), pas de complétion
automatique, pas de détection d'erreurs en temps réel, pas de
"aller à la définition". C'est une extension de coloration syntaxique
et d'intégration de tâches — l'équivalent d'un tout premier support
d'éditeur, pas un serveur de langage complet (`language server`).
