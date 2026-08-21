#!/bin/bash
cd "$(dirname "$0")"
clear

echo "============================================================"
echo "  TerminalVindex"
echo "============================================================"
echo ""

if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then
    echo "Lancement via Docker (le binaire est compile pour Linux)..."
    echo ""
    docker run --rm -it -v "$(pwd)":/app -w /app alpine:latest sh -c "chmod +x ./TerminalVindex; ./TerminalVindex"
else
    echo "TerminalVindex est un programme Linux natif. Sur Mac, il"
    echo "faut un moyen de faire tourner du code Linux — deux options :"
    echo ""
    echo "  OPTION 1 (recommandee) — Installer Docker Desktop :"
    echo "    1. https://www.docker.com/products/docker-desktop/"
    echo "    2. Une fois installe et lance, redemarre ce fichier"
    echo "       (double-clic sur Lancer-TerminalVindex.command)"
    echo ""
    echo "  OPTION 2 — Utiliser une machine virtuelle Linux"
    echo "    (UTM, VirtualBox, ou Parallels)"
    echo ""
    read -p "Appuie sur Entree pour fermer..."
fi
