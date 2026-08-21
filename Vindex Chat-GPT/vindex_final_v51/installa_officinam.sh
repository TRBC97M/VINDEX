#!/usr/bin/env bash
# Officinam VINDEX graphicam usori praesenti sine iure administratoris installat.

set -eu

SOURCE_ROOT="$(cd "$(dirname "$0")" && pwd)"
DATA_HOME="${XDG_DATA_HOME:-$HOME/.local/share}"
BIN_HOME="${XDG_BIN_HOME:-$HOME/.local/bin}"
INSTALL_ROOT="${VINDEX_INSTALL_ROOT:-$DATA_HOME/vindex}"
PROJECTA="${VINDEX_PROJECTA_DIR:-$DATA_HOME/vindex-officina/projecta}"
APPLICATIONS_DIR="$DATA_HOME/applications"
ICONS_DIR="$DATA_HOME/icons/hicolor/scalable/apps"
MIME_DIR="$DATA_HOME/mime/packages"
DESKTOP_FILE="$APPLICATIONS_DIR/com.vindex.Officina.desktop"
SALUTATIO_DESKTOP_FILE="$APPLICATIONS_DIR/com.vindex.Salutatio.desktop"
SYSTEMA_DESKTOP_FILE="$APPLICATIONS_DIR/com.vindex.Systema.desktop"
MIME_FILE="$MIME_DIR/com.vindex.fons.xml"

if [ ! -x "$SOURCE_ROOT/vindex-officina" ] || \
   [ ! -x "$SOURCE_ROOT/vindex-salutatio" ] || \
   [ ! -x "$SOURCE_ROOT/vindex-systema" ] || \
   [ ! -x "$SOURCE_ROOT/officina_vindex" ] || \
   [ ! -x "$SOURCE_ROOT/salutatio_vindex" ] || \
   [ ! -x "$SOURCE_ROOT/vindex_graphica" ] || \
   [ ! -x "$SOURCE_ROOT/compilator_vindex" ] || \
   [ ! -f "$SOURCE_ROOT/systema_vindex.img" ] || \
   [ ! -f "$SOURCE_ROOT/nucleus_systema.elf" ] || \
   [ ! -f "$SOURCE_ROOT/fenestrale_systema.bin" ] || \
   [ ! -f "$SOURCE_ROOT/rectores_systema.bin" ]; then
    printf '%s\n' "Installatio impossibilis: fasciculus VINDEX imperfectus est." >&2
    exit 66
fi
if ! "$SOURCE_ROOT/vindex_graphica" --probatio >/dev/null 2>&1; then
    printf '%s\n' "Installatio impossibilis: GTK 3 in systemate deest." >&2
    exit 69
fi

mkdir -p "$DATA_HOME" "$BIN_HOME" "$APPLICATIONS_DIR" "$ICONS_DIR" "$MIME_DIR" "$PROJECTA"

if [ "$SOURCE_ROOT" != "$INSTALL_ROOT" ]; then
    STAGING="$(mktemp -d "$DATA_HOME/.vindex-install.XXXXXX")"
    purga_installationem() {
        if [ -n "${STAGING:-}" ] && [ -d "$STAGING" ]; then
            rm -rf -- "$STAGING"
        fi
    }
    trap purga_installationem EXIT HUP INT TERM
    cp -a "$SOURCE_ROOT/." "$STAGING/"

    if [ -e "$INSTALL_ROOT" ]; then
        STAMP="$(date +%Y%m%d-%H%M%S)"
        BACKUP="${INSTALL_ROOT}.reservatum-${STAMP}"
        INDEX=1
        while [ -e "$BACKUP" ]; do
            BACKUP="${INSTALL_ROOT}.reservatum-${STAMP}-${INDEX}"
            INDEX=$((INDEX + 1))
        done
        mv -- "$INSTALL_ROOT" "$BACKUP"
        printf 'Versio prior servata est in %s\n' "$BACKUP"
    fi

    mkdir -p "$(dirname "$INSTALL_ROOT")"
    mv -- "$STAGING" "$INSTALL_ROOT"
    STAGING=""
    trap - EXIT HUP INT TERM
fi

chmod 755 "$INSTALL_ROOT/vindex-officina" "$INSTALL_ROOT/vindexc" \
    "$INSTALL_ROOT/vindex-salutatio" "$INSTALL_ROOT/vindex-systema" \
    "$INSTALL_ROOT/systema/construe_systema.sh" "$INSTALL_ROOT/officina_vindex" \
    "$INSTALL_ROOT/salutatio_vindex" "$INSTALL_ROOT/vindex_graphica" \
    "$INSTALL_ROOT/compilator_vindex" \
    "$INSTALL_ROOT/installa_officinam.sh"
ln -sfn "$INSTALL_ROOT/vindex-officina" "$BIN_HOME/vindex-officina"
ln -sfn "$INSTALL_ROOT/vindex-salutatio" "$BIN_HOME/vindex-salutatio"
ln -sfn "$INSTALL_ROOT/vindex-systema" "$BIN_HOME/vindex-systema"
ln -sfn "$INSTALL_ROOT/vindexc" "$BIN_HOME/vindexc"
cp "$INSTALL_ROOT/officina/vindex.svg" "$ICONS_DIR/vindex-officina.svg"

cat >"$DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=VINDEX Officina
Comment=Programmata VINDEX in Officina graphica scribe, compila et exsequere
Exec="$INSTALL_ROOT/officina_vindex" "$INSTALL_ROOT/vindex_graphica" "$INSTALL_ROOT/compilator_vindex" "$INSTALL_ROOT/formae/officina.forma" %f
TryExec=$INSTALL_ROOT/officina_vindex
Path=$PROJECTA
Icon=vindex-officina
Terminal=false
StartupNotify=true
Categories=Development;IDE;
MimeType=text/x-vindex;
Keywords=VINDEX;programmatio;compilator;officina;
EOF
chmod 644 "$DESKTOP_FILE"

cat >"$SALUTATIO_DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=VINDEX Salutatio
Comment=Applicatio graphica declarativa a VINDEX gubernata
Exec="$INSTALL_ROOT/salutatio_vindex" "$INSTALL_ROOT/vindex_graphica" "$INSTALL_ROOT/formae/salutatio.forma"
TryExec=$INSTALL_ROOT/salutatio_vindex
Path=$PROJECTA
Icon=vindex-officina
Terminal=false
StartupNotify=true
Categories=Development;Utility;
Keywords=VINDEX;Graphica;Forma;Salutatio;
EOF
chmod 644 "$SALUTATIO_DESKTOP_FILE"

cat >"$SYSTEMA_DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=VINDEX Fenestrale
Comment=Ambitum VINDEX sine systemate hospite in QEMU inicia
Exec="$INSTALL_ROOT/vindex-systema"
TryExec=$INSTALL_ROOT/vindex-systema
Icon=vindex-officina
Terminal=false
StartupNotify=true
Categories=Development;Emulator;
Keywords=VINDEX;Systema;Nucleus;QEMU;
EOF
chmod 644 "$SYSTEMA_DESKTOP_FILE"

cat >"$MIME_FILE" <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="text/x-vindex">
    <comment>Fons VINDEX</comment>
    <glob pattern="*.vindex"/>
  </mime-type>
</mime-info>
EOF
chmod 644 "$MIME_FILE"

if command -v update-mime-database >/dev/null 2>&1; then
    update-mime-database "$DATA_HOME/mime" >/dev/null 2>&1 || true
fi
if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database "$APPLICATIONS_DIR" >/dev/null 2>&1 || true
fi
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -f -t "$DATA_HOME/icons/hicolor" >/dev/null 2>&1 || true
fi

printf '\n%s\n' "VINDEX Officina graphica installata est."
printf '%s\n' "Aperi « VINDEX Officina » ex indice applicationum."
printf '%s\n' "Aperi « VINDEX Salutatio » ut alteram Formarum applicationem probes."
printf '%s\n' "Aperi « VINDEX Fenestrale » ut nucleum sine hospite in QEMU probes."
printf 'In linea mandatorum: %s, %s aut %s\n' \
    "$BIN_HOME/vindex-officina" "$BIN_HOME/vindex-salutatio" "$BIN_HOME/vindex-systema"
case ":${PATH:-}:" in
    *":$BIN_HOME:"*) ;;
    *) printf 'Consilium: adde %s ad PATH ut mandata VINDEX recta via voces.\n' "$BIN_HOME" ;;
esac
