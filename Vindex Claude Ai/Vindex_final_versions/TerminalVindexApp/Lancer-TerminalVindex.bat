@echo off
title TerminalVindex

wsl.exe -e sh -c "chmod +x ./TerminalVindex 2>/dev/null; ./TerminalVindex" 2>nul

if errorlevel 1 (
    echo.
    echo ============================================================
    echo   TerminalVindex a besoin de WSL pour tourner sur Windows.
    echo.
    echo   Pour l'installer :
    echo     1. Ouvre PowerShell EN ADMINISTRATEUR
    echo        (clic droit sur PowerShell dans le menu Demarrer
    echo         puis "Executer en tant qu'administrateur")
    echo     2. Tape :  wsl --install
    echo     3. Redemarre l'ordinateur si demande
    echo     4. Relance ce fichier (Lancer-TerminalVindex.bat)
    echo ============================================================
    echo.
    pause
)
