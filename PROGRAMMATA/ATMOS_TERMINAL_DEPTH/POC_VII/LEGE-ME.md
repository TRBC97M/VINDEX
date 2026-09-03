# ATMOS // TERMINAL DEPTH — POC VII / RESTITUTIO SONAR

Statut: **IN PROBATIONE**.

Ce jalon corrige une dérive de POC V/VI révélée par le test humain et par la comparaison avec le jeu HTML original.

## Contrat de gameplay

- la navigation principale n'est plus `DOWN/UP` ni un déplacement de secteur par flèches;
- le sonar est un espace de navigation continu;
- un clic dans le sonar devient une destination du monde;
- la position `(x,y)` évolue progressivement vers cette destination;
- la profondeur est dérivée de la bathymétrie déterministe du monde;
- le joueur reste au centre du sonar pendant le déplacement;
- la destination et la route sont affichées;
- cliquer un contact minéral l'approche puis lance l'extraction continue;
- `ESC` ou le bouton `X` Windows quittent le jeu.

## Fenêtre

Le framebuffer logique 640×440 est présenté à **la taille client réelle à chaque frame**. Le resize/maximize ne doit donc plus laisser d'anciennes copies ou des zones blanches comme Stabilitas I.

## Pureté

Le runtime reste entièrement VINDEX. Le fichier HTML original sert de spécification comportementale seulement; aucun HTML, CSS ou JavaScript n'est embarqué dans le jeu natif.
