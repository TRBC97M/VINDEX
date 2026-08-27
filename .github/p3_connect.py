#!/usr/bin/env python3
from pathlib import Path

RADIX = Path('Vindex Chat-GPT/vindex_final_v51')
PONS = RADIX / 'systema/uefi/ponticulus_uefi_purus.vindex'
NUCLEUS = RADIX / 'systema/nucleus.vindex'
PROBA = RADIX / 'instrumenta/proba_catenam_uefi_053.sh'
WORKFLOW = Path('.github/workflows/catena-uefi-vindex.yml')

# --- Ponticulus: moderatores firmware ante nucleum coniunguntur. ---
textus = PONS.read_text(encoding='utf-8')
vetus = """//   BootServices: AllocatePages=40, HandleProtocol=152, LocateProtocol=320,
//                 SetWatchdogTimer=256
"""
novus = """//   BootServices: AllocatePages=40, HandleProtocol=152, ConnectController=264,
//                 LocateHandleBuffer=312, LocateProtocol=320, SetWatchdogTimer=256
"""
if vetus not in textus:
    raise SystemExit('ERRATUM: tabula offsetorum BootServices non inventa')
textus = textus.replace(vetus, novus, 1)

ancora = """FUNCTIO SCRIBE_CATENAM REDDENS NUMERUS.
    ACCIPIT conout SICUT NUMERUS.
    ACCIPIT catena SICUT NUMERUS.
    DECLARA sc SICUT NUMERUS VALENS CONTENTUM(conout + 8).
    REDDE UEFI_VOCA6(sc, conout, catena, 0, 0, 0, 0).
FIN-FUNCTIO.

"""
functio = """FUNCTIO CONTROLLATORES_CONIUNGE REDDENS NUMERUS.
    ACCIPIT bs SICUT NUMERUS.
    SI bs == 0 TUNC REDDE 0. FIN-SI.
    DECLARA loca_handles SICUT NUMERUS VALENS CONTENTUM(bs + 312).
    DECLARA coniunge SICUT NUMERUS VALENS CONTENTUM(bs + 264).
    SI loca_handles == 0 || coniunge == 0 TUNC REDDE 0. FIN-SI.

    DECLARA numerus SICUT NUMERUS VALENS 0.
    DECLARA handles SICUT NUMERUS VALENS 0.
    DECLARA status SICUT NUMERUS VALENS UEFI_VOCA6(loca_handles, 0, 0, 0, SEDES(numerus), SEDES(handles), 0).
    SI status != 0 || handles == 0 || numerus <= 0 TUNC REDDE 0. FIN-SI.

    DECLARA i SICUT NUMERUS VALENS 0.
    DECLARA coniuncta SICUT NUMERUS VALENS 0.
    DUM i < numerus PERFICE
        DECLARA h SICUT NUMERUS VALENS CONTENTUM(handles + i * 8).
        SI h != 0 TUNC
            DECLARA s SICUT NUMERUS VALENS UEFI_VOCA6(coniunge, h, 0, 0, 1, 0, 0).
            SI s == 0 TUNC coniuncta = coniuncta + 1. FIN-SI.
        FIN-SI.
        i = i + 1.
    FIN-DUM.

    DECLARA libera SICUT NUMERUS VALENS CONTENTUM(bs + 72).
    SI libera != 0 TUNC
        DECLARA ig_l SICUT NUMERUS VALENS UEFI_VOCA6(libera, handles, 0, 0, 0, 0, 0).
    FIN-SI.
    REDDE coniuncta.
FIN-FUNCTIO.

"""
if ancora not in textus:
    raise SystemExit('ERRATUM: SCRIBE_CATENAM non inventa')
textus = textus.replace(ancora, ancora + functio, 1)

ancora_meta = """    // VII. Metadata pro nucleo.
    DECLARA ig_vac SICUT NUMERUS VALENS MEMORIA_VACUA(50331648, 4096).
"""
novum_meta = """    // VI-B. Moderatores firmware recursive coniunge. Hoc gradum laboratorii #71
    // e C in ponticulum VINDEX purum transfert.
    DECLARA moderatores_n SICUT NUMERUS VALENS CONTROLLATORES_CONIUNGE(bs).

    // VII. Metadata pro nucleo.
    DECLARA ig_vac SICUT NUMERUS VALENS MEMORIA_VACUA(50331648, 4096).
"""
if ancora_meta not in textus:
    raise SystemExit('ERRATUM: metadata nuclei non inventa')
textus = textus.replace(ancora_meta, novum_meta, 1)

ancora_imago = "    CONTENTUM(50334464) = imago.\n"
if ancora_imago not in textus:
    raise SystemExit('ERRATUM: metadata imaginis non inventa')
textus = textus.replace(ancora_imago, ancora_imago + "    CONTENTUM(50334504) = moderatores_n.\n", 1)
PONS.write_text(textus, encoding='utf-8')

# --- Nucleus: rector PS/2 nativus fit prima via muris, UEFI fallback manet. ---
nuc = NUCLEUS.read_text(encoding='utf-8')
caput = """// VINDEX Systema Fenestrale 0.51 — Bibliotheca duplex VXNAT.
// Omnis pictura et administratio fenestrarum ipsa VINDEX perficitur.

"""
caput_novum = caput + 'IMPORTA "systema/rectores/murus_ps2.vindex".\n\n'
if caput not in nuc:
    raise SystemExit('ERRATUM: caput nuclei non inventum')
nuc = nuc.replace(caput, caput_novum, 1)

polle_vetus = """FUNCTIO UEFI_POLLE REDDENS NUMERUS.
    DECLARA cl SICUT NUMERUS VALENS UEFI_CLAVES_POLLE().
    DECLARA ma SICUT NUMERUS VALENS UEFI_MURIS_ABS_POLLE().
    SI ma == 0 TUNC ma = UEFI_MURIS_REL_POLLE(). FIN-SI.
"""
polle_novum = """FUNCTIO UEFI_POLLE REDDENS NUMERUS.
    DECLARA cl SICUT NUMERUS VALENS UEFI_CLAVES_POLLE().
    DECLARA ma SICUT NUMERUS VALENS 0.
    SI PS2_PARATUS_EST() == 1 TUNC
        ma = PS2_POLLE().
    ALITER
        ma = UEFI_MURIS_ABS_POLLE().
        SI ma == 0 TUNC ma = UEFI_MURIS_REL_POLLE(). FIN-SI.
    FIN-SI.
"""
if polle_vetus not in nuc:
    raise SystemExit('ERRATUM: initium UEFI_POLLE non inventum')
nuc = nuc.replace(polle_vetus, polle_novum, 1)

init_vetus = """    DECLARA uefi_paratus SICUT NUMERUS VALENS UEFI_PARA().
    DECLARA volumen_lectum SICUT NUMERUS VALENS UEFI_VOLUMEN_RELEGE().
"""
init_novum = """    DECLARA uefi_paratus SICUT NUMERUS VALENS UEFI_PARA().
    // PS/2 8042 nativum post initium firmware paramus. Si apparatus non adest,
    // UEFI Simple/Absolute Pointer infra fallback manent.
    DECLARA ps2_paratus SICUT NUMERUS VALENS PS2_PARA().
    DECLARA volumen_lectum SICUT NUMERUS VALENS UEFI_VOLUMEN_RELEGE().
"""
if init_vetus not in nuc:
    raise SystemExit('ERRATUM: initium PRINCIPALIS UEFI non inventum')
nuc = nuc.replace(init_vetus, init_novum, 1)
NUCLEUS.write_text(nuc, encoding='utf-8')

# --- Probatio: eadem catena + QEMU q35 + PS/2 realis et framebuffer mutatus. ---
proba = PROBA.read_text(encoding='utf-8')
proba = proba.replace(
    "#   V.   Sylvia in schermo vere pingit (screendump inspectus).\n",
    "#   V.   Sylvia in schermo vere pingit (screendump inspectus).\n#   VI.  rector PS/2 VINDEX nativus murem vere movet.\n",
    1,
)
ancora_fin = """nuntia '   RECTE: Sylvia in schermo vere pingit.'
nuntia ''
nuntia '=== CATENA UEFI INTEGRA PROBATA ==='
nuntia 'OVMF -> BOOTX64.EFI [VINDEX] -> NUCLEUS [VINDEX] -> FRAMEBUFFER -> SYLVIA'
nuntia 'Nullum C in tota via.'
"""
novum_fin = """nuntia '   RECTE: Sylvia in schermo vere pingit.'

# --- VI. Murus PS/2 vere movetur ---
nuntia 'VI. Rector muris PS/2 VINDEX nativus...'
cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS3.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS3.fd"
MONITOR_MUS="$TEMPORARIUM/monitor-mus.sock"
QMP_MUS="$TEMPORARIUM/qmp-mus.sock"
qemu-system-x86_64 -machine q35 -m 256 -vga std \\
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \\
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS3.fd" \\
    -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \\
    -display none \\
    -monitor "unix:$MONITOR_MUS,server=on,wait=off" \\
    -qmp "unix:$QMP_MUS,server=on,wait=off" \\
    -net none >"$TEMPORARIUM/murus-qemu.log" 2>&1 &
PID_MUS=$!
if ! python3 "$RADIX/instrumenta/proba_murem_uefi_053.py" \\
        "$MONITOR_MUS" "$QMP_MUS" "$TEMPORARIUM" "$MORA_INITII"; then
    kill "$PID_MUS" 2>/dev/null || true
    wait "$PID_MUS" 2>/dev/null || true
    tail -50 "$TEMPORARIUM/murus-qemu.log" >&2 || true
    defecit 'rector PS/2 Sylviam non movit' 6
fi
wait "$PID_MUS" 2>/dev/null || true
nuntia '   RECTE: rector PS/2 VINDEX nativus in catena canonica movetur.'
nuntia ''
nuntia '=== CATENA UEFI INTEGRA PROBATA ==='
nuntia 'OVMF -> BOOTX64.EFI [VINDEX] -> NUCLEUS [VINDEX] -> FRAMEBUFFER -> PS/2 VINDEX -> SYLVIA'
nuntia 'Nullum C in tota via.'
"""
if ancora_fin not in proba:
    raise SystemExit('ERRATUM: finis probationis UEFI non inventus')
proba = proba.replace(ancora_fin, novum_fin, 1)
PROBA.write_text(proba, encoding='utf-8')

workflow = WORKFLOW.read_text(encoding='utf-8')
via = "      - 'Vindex Chat-GPT/vindex_final_v51/instrumenta/proba_catenam_uefi_053.sh'\n"
via_nova = via + "      - 'Vindex Chat-GPT/vindex_final_v51/instrumenta/proba_murem_uefi_053.py'\n      - 'Vindex Chat-GPT/vindex_final_v51/systema/rectores/murus_ps2.vindex'\n"
if workflow.count(via) != 2:
    raise SystemExit(f'ERRATUM: via probationis in workflow numero inexpectato: {workflow.count(via)}')
workflow = workflow.replace(via, via_nova)
WORKFLOW.write_text(workflow, encoding='utf-8')

print('RECTE: ConnectController, rector PS/2 nativus et probatio integra inserta sunt.')
