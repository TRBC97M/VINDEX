#!/usr/bin/env bash
# VINDEX 0.53: consumptionem temporis et memoriae in auto-hospitio nativo metitur.

set -u

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
FONS="$RADIX/src/compilator_vindex.vindex"
TEMPORARIUM="$(mktemp -d)" || exit 1
trap 'rm -rf -- "$TEMPORARIUM"' EXIT HUP INT TERM

AMORSA="$TEMPORARIUM/compilator_amorsa"

printf '%s\n' '=== AMORSA PYTHON ==='
python3 "$RADIX/bootstrap/python/compilateur_053.py" "$FONS" "$AMORSA" || exit 1
chmod 755 "$AMORSA" || exit 1
chmod 755 "$RADIX/compilator_vindex" 2>/dev/null || true

lege_kib() {
    CLAVIS="$1"
    VIA="$2"
    awk -v k="$CLAVIS" '$1 == k ":" { print $2; exit }' "$VIA" 2>/dev/null
}

proba() {
    NOMEN="$1"
    COMPILATOR="$2"
    EXITUS="$TEMPORARIUM/exitus_${NOMEN}"
    LOG="$TEMPORARIUM/log_${NOMEN}"

    printf '\n=== %s ===\n' "$NOMEN"
    printf '%s\n' 'secundae rss_kib vmsize_kib vmdata_kib vmstk_kib rssanon_kib mappae cpu_percent'

    "$COMPILATOR" "$FONS" "$EXITUS" >"$LOG" 2>&1 &
    PID=$!

    PRIMUM_RSS=''
    PRIMUM_MAPPAE=''
    ULTIMUM_RSS=''
    ULTIMUM_MAPPAE=''
    SECUNDA=0

    while [ "$SECUNDA" -le 20 ]; do
        if ! kill -0 "$PID" 2>/dev/null; then
            break
        fi

        STATUS_VIA="/proc/$PID/status"
        RSS="$(lege_kib VmRSS "$STATUS_VIA")"
        VSZ="$(lege_kib VmSize "$STATUS_VIA")"
        DATA="$(lege_kib VmData "$STATUS_VIA")"
        STK="$(lege_kib VmStk "$STATUS_VIA")"
        ANON="$(lege_kib RssAnon "$STATUS_VIA")"
        MAPPAE="$(wc -l < "/proc/$PID/maps" 2>/dev/null || printf '0')"
        CPU="$(ps -p "$PID" -o pcpu= 2>/dev/null | tr -d '[:space:]')"

        RSS="${RSS:-0}"
        VSZ="${VSZ:-0}"
        DATA="${DATA:-0}"
        STK="${STK:-0}"
        ANON="${ANON:-0}"
        MAPPAE="${MAPPAE:-0}"
        CPU="${CPU:-0}"

        if [ -z "$PRIMUM_RSS" ]; then
            PRIMUM_RSS="$RSS"
            PRIMUM_MAPPAE="$MAPPAE"
        fi
        ULTIMUM_RSS="$RSS"
        ULTIMUM_MAPPAE="$MAPPAE"

        printf '%s %s %s %s %s %s %s %s\n' \
            "$SECUNDA" "$RSS" "$VSZ" "$DATA" "$STK" "$ANON" "$MAPPAE" "$CPU"

        SECUNDA=$((SECUNDA + 1))
        sleep 1
    done

    SI_VIVIT=0
    if kill -0 "$PID" 2>/dev/null; then
        SI_VIVIT=1
        kill -TERM "$PID" 2>/dev/null || true
        sleep 1
        kill -KILL "$PID" 2>/dev/null || true
    fi

    wait "$PID" 2>/dev/null
    STATUS=$?

    if [ "$SI_VIVIT" -eq 1 ]; then
        printf 'STATUS: intermissus post XXI secundas; status=%s.\n' "$STATUS"
    else
        printf 'STATUS: finitus ante terminum; status=%s.\n' "$STATUS"
    fi

    if [ -n "$PRIMUM_RSS" ] && [ -n "$ULTIMUM_RSS" ]; then
        printf 'CRESCENTIA RSS: %s KiB.\n' "$((ULTIMUM_RSS - PRIMUM_RSS))"
    fi
    if [ -n "$PRIMUM_MAPPAE" ] && [ -n "$ULTIMUM_MAPPAE" ]; then
        printf 'CRESCENTIA MAPPARUM: %s.\n' "$((ULTIMUM_MAPPAE - PRIMUM_MAPPAE))"
    fi

    if [ -s "$EXITUS" ]; then
        printf 'MENSURA EXITUS: %s octeta.\n' "$(stat -c '%s' "$EXITUS")"
    else
        printf '%s\n' 'MENSURA EXITUS: nondum scripta.'
    fi

    if [ -s "$LOG" ]; then
        printf '%s\n' '--- EXSCRIPTA COMPILATORIS ---'
        tail -20 "$LOG"
    fi
}

proba 'COMPILATOR_TRADITUS' "$RADIX/compilator_vindex"
proba 'COMPILATOR_AB_AMORSA' "$AMORSA"

printf '\n%s\n' '=== DIAGNOSTICA AUTO-HOSPITII FINITA ==='
