#!/usr/bin/env bash
# VINDEX 0.53: distinguit vitium nominum a vitio formae non ultimae.

set -u

RADIX='Vindex Chat-GPT/vindex_final_v51'
FONS="$RADIX/src/compilator_vindex.vindex"
COMP="$RADIX/compilator_vindex"
RELATIO=/tmp/diagnosis_nomina_formarum_053
: > "$RELATIO"

refice() {
  git checkout -- "$FONS" "$COMP" 2>/dev/null || true
}
trap refice EXIT

printf '%s\n' '== PRAEPARATIO ==' | tee -a "$RELATIO"
python3 "$RADIX/instrumenta/applica_formas_dynamicas_053.py" | tee -a "$RELATIO" || exit 1
chmod 755 "$COMP"
"$COMP" "$FONS" /tmp/g1_nomina_formarum >>"$RELATIO" 2>&1 || { cat "$RELATIO"; exit 1; }
chmod 755 /tmp/g1_nomina_formarum
printf '%s\n' 'RECTE: G1 ad diagnosin paratum est.' | tee -a "$RELATIO"

proba() {
  NOMEN="$1"
  FONS_CASUS="$2"
  VIA="/tmp/${NOMEN}.vindex"
  EXE="/tmp/${NOMEN}"
  printf '%s\n' "$FONS_CASUS" > "$VIA"
  INIT=$(date +%s)
  timeout 5s /tmp/g1_nomina_formarum "$VIA" "$EXE" >/tmp/nomina_stdout 2>/tmp/nomina_stderr
  S=$?
  FIN=$(date +%s)
  SEC=$((FIN-INIT))
  printf '%s: status=%s tempus=%ss\n' "$NOMEN" "$S" "$SEC" | tee -a "$RELATIO"
  if [ -s /tmp/nomina_stdout ]; then sed 's/^/  stdout: /' /tmp/nomina_stdout | tee -a "$RELATIO"; fi
  if [ -s /tmp/nomina_stderr ]; then sed 's/^/  stderr: /' /tmp/nomina_stderr | tee -a "$RELATIO"; fi
}

proba 'prima_sola' 'FORMA Prima.
    CAMPUS valor SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA x SICUT Prima.
    valor DE x = 39.
    PROCLAMA valor DE x.
    REDDE 0.
FIN-FUNCTIO.'

proba 'forma0_sola' 'FORMA Forma0.
    CAMPUS valor SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA x SICUT Forma0.
    valor DE x = 39.
    PROCLAMA valor DE x.
    REDDE 0.
FIN-FUNCTIO.'

proba 'prima_non_ultima' 'FORMA Prima.
    CAMPUS valor SICUT NUMERUS.
FIN-FORMA.

FORMA Magna.
    CAMPUS c0 SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA x SICUT Prima.
    valor DE x = 39.
    PROCLAMA valor DE x.
    REDDE 0.
FIN-FUNCTIO.'

proba 'forma0_non_ultima' 'FORMA Forma0.
    CAMPUS valor SICUT NUMERUS.
FIN-FORMA.

FORMA Magna.
    CAMPUS c0 SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA x SICUT Forma0.
    valor DE x = 39.
    PROCLAMA valor DE x.
    REDDE 0.
FIN-FUNCTIO.'

proba 'prima_ante_secundam' 'FORMA Prima.
    CAMPUS valor SICUT NUMERUS.
FIN-FORMA.

FORMA Secunda.
    CAMPUS aliud SICUT NUMERUS.
FIN-FORMA.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA x SICUT Prima.
    valor DE x = 39.
    PROCLAMA valor DE x.
    REDDE 0.
FIN-FUNCTIO.'

printf '%s\n' '== FINIS DIAGNOSIS ==' | tee -a "$RELATIO"
cat "$RELATIO"
