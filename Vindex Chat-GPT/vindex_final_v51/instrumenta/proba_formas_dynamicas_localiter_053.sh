#!/usr/bin/env bash
# VINDEX 0.53: formas et campos dynamicos localiter in WSL/Linux comprobat.
# Hic fluxus eandem probationem ac actio remota facit, sed eventum GitHub Actions non exspectat.

set -u

RAMUS='chatgpt/vindex-053-compilator-dynamicus'
RADIX='Vindex Chat-GPT/vindex_final_v51'
RELATIO="$RADIX/instrumenta/RELATIO-FORMAE-DYNAMICAE-053.md"
TEMPUS=/tmp/relatio_formae_053_localis
: > "$TEMPUS"
SUCCESSUS=0
RADIX_ABS=$(pwd)

integrum() {
  VIA="$1"
  [ -s "$VIA" ] || return 1
  A=$(stat -c '%s' "$VIA" 2>/dev/null)
  B=$(od -An -tu8 -j96 -N8 "$VIA" 2>/dev/null | tr -d '[:space:]')
  [ -n "$A" ] && [ "$A" = "$B" ]
}

refice() {
  git checkout -- \
    "$RADIX/src/compilator_vindex.vindex" \
    "$RADIX/compilator_vindex" \
    "$RADIX/officina_vindex" \
    "$RADIX/salutatio_vindex" \
    "$RADIX/nucleus_systema.elf" \
    "$RADIX/systema_vindex.img" \
    "$RADIX/BOOTX64.EFI" \
    "$RADIX/systema_vindex_uefi.img" 2>/dev/null || true
}

proba() {
  RAMUS_ACTUALIS=$(git branch --show-current)
  if [ "$RAMUS_ACTUALIS" != "$RAMUS" ]; then
    printf 'ERRATUM: ramus actualis est [%s], expectatur [%s].\n' "$RAMUS_ACTUALIS" "$RAMUS" >> "$TEMPUS"
    return 1
  fi

  if ! git diff --quiet || ! git diff --cached --quiet; then
    printf '%s\n' 'ERRATUM: arbor laboris munda non est.' >> "$TEMPUS"
    return 1
  fi

  chmod 755 "$RADIX/compilator_vindex"
  python3 "$RADIX/instrumenta/applica_formas_dynamicas_053.py" >> "$TEMPUS" 2>&1 || return 1

  if grep -q 'tabula\[950\|tabula\[1000\|tabula\[1050\|tabula\[1100\|tabula\[2500\|tabula\[2530\|tabula\[200 +' "$RADIX/src/compilator_vindex.vindex"; then
    printf '%s\n' 'ERRATUM: metadata formarum fixa adhuc manet.' >> "$TEMPUS"
    return 1
  fi
  grep -q 'FUNCTIO INITIA_FORMAS_DYNAMICA REDDENS NUMERUS' "$RADIX/src/compilator_vindex.vindex" || return 1
  printf '%s\n' 'RECTE: formae et campi descriptoribus crescentibus utuntur.' >> "$TEMPUS"

  "$RADIX/compilator_vindex" "$RADIX/src/compilator_vindex.vindex" /tmp/g1 >> "$TEMPUS" 2>&1
  S1=$?
  printf 'STATUS G1: %s.\n' "$S1" >> "$TEMPUS"
  [ "$S1" -eq 0 ] && integrum /tmp/g1 || return 1

  chmod 755 /tmp/g1
  /tmp/g1 "$RADIX/src/compilator_vindex.vindex" /tmp/g2 >> "$TEMPUS" 2>&1
  S2=$?
  printf 'STATUS G2: %s.\n' "$S2" >> "$TEMPUS"
  [ "$S2" -eq 0 ] && integrum /tmp/g2 || return 1

  chmod 755 /tmp/g2
  /tmp/g2 "$RADIX/src/compilator_vindex.vindex" /tmp/g3 >> "$TEMPUS" 2>&1
  S3=$?
  printf 'STATUS G3: %s.\n' "$S3" >> "$TEMPUS"
  [ "$S3" -eq 0 ] && integrum /tmp/g3 || return 1
  cmp -s /tmp/g2 /tmp/g3 || return 1
  printf '%s\n' 'RECTE: formae dynamicae punctum fixum compilatoris servant.' >> "$TEMPUS"

  cp /tmp/g3 "$RADIX/compilator_vindex"
  chmod 755 "$RADIX/compilator_vindex"

  python3 "$RADIX/instrumenta/genera_probationem_formarum_053.py" /tmp/formae_magnae_053.vindex >> "$TEMPUS" 2>&1 || return 1
  "$RADIX/compilator_vindex" /tmp/formae_magnae_053.vindex /tmp/formae_magnae_053 >> "$TEMPUS" 2>&1
  SF=$?
  printf 'COMPILATIO XL FORMARUM ET LXXX CAMPORUM: status=%s.\n' "$SF" >> "$TEMPUS"
  [ "$SF" -eq 0 ] && integrum /tmp/formae_magnae_053 || return 1

  chmod 755 /tmp/formae_magnae_053
  OF=$(/tmp/formae_magnae_053 2>>"$TEMPUS"); EF=$?
  printf 'EXECUTIO FORMARUM MAGNARUM: status=%s exitus=[%s].\n' "$EF" "$OF" >> "$TEMPUS"
  [ "$EF" -eq 0 ] || return 1
  EXPECTATUM=$(printf '39\n777')
  [ "$OF" = "$EXPECTATUM" ] || return 1
  printf '%s\n' 'RECTE: limites XV formarum et XXVI camporum remoti sunt.' >> "$TEMPUS"

  cd "$RADIX" || return 1
  ./compilator_vindex src/officina_vindex.vindex /tmp/officina_nova >> "$TEMPUS" 2>&1 || return 1
  ./compilator_vindex src/salutatio_vindex.vindex /tmp/salutatio_nova >> "$TEMPUS" 2>&1 || return 1
  cp /tmp/officina_nova ./officina_vindex
  cp /tmp/salutatio_nova ./salutatio_vindex

  find . -type f -name '*.sh' -exec chmod 755 {} +
  chmod 755 ./vindexc ./vindex_graphica ./officina_vindex ./salutatio_vindex ./compilator_vindex ./vindex-officina ./vindex-salutatio ./vindex-systema
  bash ./systema/construe_systema.sh >> "$TEMPUS" 2>&1 || return 1
  bash ./systema/uefi/construe_uefi.sh >> "$TEMPUS" 2>&1 || return 1
  printf '%s\n' 'RECTE: Systema BIOS et UEFI post migrationem formarum regenerata sunt.' >> "$TEMPUS"

  bash ./tests/run_tests.sh >> "$TEMPUS" 2>&1
  SR=$?
  printf 'PROBATIONES REGRESSIONALES: status=%s.\n' "$SR" >> "$TEMPUS"
  [ "$SR" -eq 0 ] || return 1

  cd "$RADIX_ABS" || return 1
  return 0
}

committe() {
  NUNTIUS="$1"
  git -c user.name='VINDEX Centurio' -c user.email='actions@users.noreply.github.com' commit -m "$NUNTIUS"
}

if proba; then
  SUCCESSUS=1
else
  STATUS=$?
  cd "$RADIX_ABS" 2>/dev/null || true
  printf 'ERRATUM: migratio formarum dynamicarum nondum canonica est; status=%s.\n' "$STATUS" >> "$TEMPUS"
fi

cd "$RADIX_ABS" || exit 1
{
  printf '%s\n\n' '# VINDEX 0.53 — Relatio formarum dynamicarum'
  printf '%s\n\n' 'Formae et campi crescibiles, punctum fixum, XL formae, LXXX campi et regressiones hic comprobantur.'
  printf '%s\n' '```text'
  cat "$TEMPUS"
  printf '%s\n' '```'
} > "$RELATIO"

if [ "$SUCCESSUS" -eq 1 ]; then
  git add \
    "$RADIX/src/compilator_vindex.vindex" \
    "$RADIX/compilator_vindex" \
    "$RADIX/officina_vindex" \
    "$RADIX/salutatio_vindex" \
    "$RADIX/nucleus_systema.elf" \
    "$RADIX/systema_vindex.img" \
    "$RADIX/BOOTX64.EFI" \
    "$RADIX/systema_vindex_uefi.img" \
    "$RELATIO"
  committe 'VINDEX 0.53: formas dynamicas comproba' || exit 1
  if git push origin "$RAMUS"; then
    printf '%s\n' 'RECTE: migratio formarum dynamicarum comprobata et missa est.'
    exit 0
  fi
  printf '%s\n' 'RECTE: migratio comprobata et commissa est; transmissio remota ex PowerShell facienda est.'
  exit 2
fi

refice
git add "$RELATIO"
committe 'VINDEX 0.53: formas dynamicas diagnostica' || exit 1
if git push origin "$RAMUS"; then
  printf '%s\n' 'ERRATUM: relatio diagnostica missa est.'
  exit 1
fi
printf '%s\n' 'ERRATUM: relatio diagnostica commissa est; transmissio remota ex PowerShell facienda est.'
exit 2
