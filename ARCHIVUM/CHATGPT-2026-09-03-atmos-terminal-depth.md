# Session ChatGPT — ATMOS // TERMINAL DEPTH : POC I à V et Passe Génocidaire

_Reconstruction de coordination, non verbatim._
_La transcription intégrale de cette période n'est pas disponible dans les partages récupérables. Ce fichier conserve les décisions, abandons et résultats recoupés avec les PR/commits canoniques._
_Période couverte : 3–4 septembre 2026._
_Sources de contrôle : PR #174, #175, #176, #177, #178, #182 fermée et #183 draft._

---

## Pourquoi ATMOS

ATMOS a été choisi comme preuve de concept réelle de VINDEX hors Sylvia : au lieu d'ajouter des capacités abstraites, le jeu pousse le compilateur, la bibliothèque standard, Win64, le rendu et la persistance jusqu'à révéler les manques généraux du langage.

    [action] POC I/#174 : première application ludique PE Win64 VINDEX, état ATD1 persistant et chaîne `new -> descend -> mine -> ascend -> trade -> status` certifiée sous Windows réel.
    [action] POC II/#175 : STDIO Win64 réel, session interactive continue et `LITTERA` byte-addressée.
    [action] POC III/#176 : FFI Win64, fenêtre native, framebuffer BGRA VINDEX et input ; première application graphique interactive certifiée.
    [action] POC IV/#177 : noyau commun persistant, HUD/sonar, clavier/souris ; ajout général de conversion `NUMERUS -> TEXTUS`.
    [action] POC V/#178 : monde procédural déterministe, PRNG général, état monde ATW1 et HUD ; certification Windows réelle.

## « La Passe Génocidaire »

Ce nom interne désigne une vérification de pureté volontairement impitoyable : le runtime final du jeu ne doit dépendre d'aucun HTML, JavaScript, C, C++, C#, Rust, Python, assembleur externe, Electron, CRT, .NET ou runtime tiers.

Le compilateur VINDEX doit atteindre son point fixe, produire lui-même le binaire GUI, puis ce même binaire doit s'exécuter sous Windows réel.

Ce terme est un exemple direct de mémoire qui existait uniquement côté ChatGPT et qui manquait à l'archive Claude.

## Échec utile et abandon volontaire

Les essais humains Windows ont montré que la lignée expérimentale héritée des POC mélangeait des chemins graphiques incompatibles — framebuffer BGRA et GDI direct — avec ghosting/duplication et problèmes de resize. Le gameplay avait aussi trop divergé du HTML de référence.

    [action] PR #182 fermée sans fusion : la branche expérimentale est conservée comme laboratoire, pas comme base active du jeu.
    [action] PR #183 repart proprement de `main` : le HTML fourni par Numi devient une spécification comportementale ; aucun HTML/JS n'entre dans le runtime ; les systèmes sont réécrits en VINDEX.

## Décisions à ne pas perdre

- Les POC I–V sont des preuves historiques de capacités VINDEX, pas la base active du jeu final.
- `PROGRAMMATA/ATMOS_TERMINAL_DEPTH/NATIVUM/` devient la ligne active de reconstruction.
- La pureté VINDEX n'interdit pas Windows comme plateforme ; elle interdit que le runtime du jeu soit écrit ou soutenu par un autre langage/runtime.
- Une branche qui prouve beaucoup de choses peut quand même être abandonnée si les tests humains montrent que son architecture est mauvaise.