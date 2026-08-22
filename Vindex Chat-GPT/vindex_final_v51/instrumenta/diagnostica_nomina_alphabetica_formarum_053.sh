#!/usr/bin/env bash
# VINDEX 0.53: nomina formarum alphabetica et accessum camporum distinguit.

set -u

RADIX='Vindex Chat-GPT/vindex_final_v51'
FONS="$RADIX/src/compilator_vindex.vindex"
COMP="$RADIX/compilator_vindex"
RELATIO=/tmp/diagnosis_nomina_alphabetica_formarum_053
: > "$RELATIO"

refice() {
  git checkout -- "$FONS" "$COMP" 2>/dev/null || true
}
trap refice EXIT

printf '%s\n' '== PRAEPARATIO ==' | tee -a "$RELATIO"
python3 "$RADIX/instrumenta/applica_formas_dynamicas_053.py" | tee -a "$RELATIO" || exit 1
chmod 755 "$COMP"
"$COMP" "$FONS" /tmp/g1_nomina_alpha >>"$RELATIO" 2>&1 || exit 1
chmod 755 /tmp/g1_nomina_alpha
printf '%s\n' 'RECTE: G1 ad diagnosin paratum est.' | tee -a "$RELATIO"

proba_unam() {
  NOMEN="$1"
  VIA="/tmp/forma_nomen_${NOMEN}.vindex"
  EXE="/tmp/forma_nomen_${NOMEN}"
  cat > "$VIA" <<EOF
FORMA $NOMEN.
    CAMPUS valor SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA x SICUT $NOMEN.
    valor DE x = 7.
    PROCLAMA valor DE x.
    REDDE 0.
FIN-FUNCTIO.
EOF
  INIT=$(date +%s)
  timeout 5s /tmp/g1_nomina_alpha "$VIA" "$EXE" >/tmp/alpha_stdout 2>/tmp/alpha_stderr
  S=$?
  FIN=$(date +%s)
  printf 'nomen=%s: status=%s tempus=%ss\n' "$NOMEN" "$S" "$((FIN-INIT))" | tee -a "$RELATIO"
  if [ -s /tmp/alpha_stdout ]; then sed 's/^/  stdout: /' /tmp/alpha_stdout | tee -a "$RELATIO"; fi
  if [ -s /tmp/alpha_stderr ]; then sed 's/^/  stderr: /' /tmp/alpha_stderr | tee -a "$RELATIO"; fi
}

proba_multas() {
  MODUS="$1"
  VIA="/tmp/formae_multae_${MODUS}.vindex"
  EXE="/tmp/formae_multae_${MODUS}"
  python3 - "$MODUS" "$VIA" <<'PY'
from pathlib import Path
import sys
modus=sys.argv[1]
via=Path(sys.argv[2])

def suff(i: int, upper: bool) -> str:
    out=[]
    n=i+1
    while n:
        n,r=divmod(n-1,26)
        c=chr(ord('A' if upper else 'a')+r)
        out.append(c)
    return ''.join(reversed(out))

upper = modus == 'maiusculae'
L=[]
nomina=[]
for i in range(40):
    nomen='Forma'+suff(i, upper)
    nomina.append(nomen)
    L += [f'FORMA {nomen}.', '    CAMPUS valor SICUT NUMERUS.', 'FIN-FORMA.', '']
L += ['FUNCTIO PRINCIPALIS REDDENS NUMERUS.', f'    DECLARA x SICUT {nomina[-1]}.', '    valor DE x = 39.', '    PROCLAMA valor DE x.', '    REDDE 0.', 'FIN-FUNCTIO.', '']
via.write_text('\n'.join(L), encoding='utf-8')
PY
  INIT=$(date +%s)
  timeout 8s /tmp/g1_nomina_alpha "$VIA" "$EXE" >/tmp/alpha_stdout 2>/tmp/alpha_stderr
  S=$?
  FIN=$(date +%s)
  printf 'multae=%s: status=%s tempus=%ss\n' "$MODUS" "$S" "$((FIN-INIT))" | tee -a "$RELATIO"
  if [ -s /tmp/alpha_stdout ]; then sed 's/^/  stdout: /' /tmp/alpha_stdout | tee -a "$RELATIO"; fi
  if [ -s /tmp/alpha_stderr ]; then sed 's/^/  stderr: /' /tmp/alpha_stderr | tee -a "$RELATIO"; fi
}

printf '%s\n' '== NOMINA SINGULA ==' | tee -a "$RELATIO"
for NOMEN in Prima FormaA Formaa FormaZ Formaz FormaAA Formaaa FormaAN Formaan; do
  proba_unam "$NOMEN"
done

printf '%s\n' '== XL FORMAE ALPHABETICAE ==' | tee -a "$RELATIO"
proba_multas maiusculae
proba_multas minusculae

printf '%s\n' '== FINIS DIAGNOSIS ==' | tee -a "$RELATIO"
cat "$RELATIO"
