#!/bin/bash
DOSSIER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DOSSIER"
chmod +x ./TerminalVindex
./TerminalVindex
echo ""
read -p "Appuie sur Entree pour fermer..."
