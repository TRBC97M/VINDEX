#!/usr/bin/env python3
"""Gradus J: murem, hit-testing, tractionem et taskbar multi-client verificat."""

from pathlib import Path
import re

R=Path(__file__).resolve().parents[1]
C=(R/'systema/uefi/fenestrale_native_j.c').read_text(encoding='utf-8')
SH=(R/'systema/uefi/construe_fenestrale_native_j.sh').read_text(encoding='utf-8')
P=(R/'src/programmata_fenestrale_ii_h.vindex').read_text(encoding='utf-8')
T=(R/'src/tabula_fenestrale_ii_i_runtime.vindex').read_text(encoding='utf-8')

def req(textus, fragmentum, nomen):
    if fragmentum not in textus:
        raise SystemExit(f'ERRATUM: {nomen} deest: {fragmentum}')

def main():
    for s in (
        'EFI_SIMPLE_POINTER_PROTOCOL', 'EFI_ABSOLUTE_POINTER_PROTOCOL',
        'guid_muris=', 'guid_muris_absoluti=', 'murem_lege', 'bullam_confirma',
        'hit_fenestra', 'mouse_down', 'drag_move', 'taskbar_click',
        'STATUS_MINIMUS', 'STATUS_CLAUSUS', 'cursor_pixel',
        'top_visibilis_index', 'focus(', 'ordinem_remove',
        'SUPERFICIES_CAPACITAS 8U', 'd->taskbar_altitudo=28',
        'd->murus_x=', 'd->murus_y=', 'd->bullae=',
    ):
        req(C,s,'compositor J')
    for s in (
        'programmata_fenestrale_ii_h.vindex',
        'tabula_fenestrale_ii_i_runtime.vindex',
        'fenestrale_native_j.c', 'FENESTRALEJ.EFI', 'fenestrale_j_uefi.img',
    ):
        req(SH,s,'constructio J')
    req(P,'CONTENTUM(50335272) = 1.','PROGRAMMATA H')
    req(T,'CONTENTUM(50335272) = 2.','TABULA runtime')
    if re.search(r'JL-UX', C, re.I):
        raise SystemExit('ERRATUM: branding JL-UX in compositorio J apparuit')
    for vetitum in ('firmamentum_uefi.c','systema/nucleus.vindex','BOOTX64.EFI"','systema_vindex_uefi.img"'):
        if vetitum in SH:
            raise SystemExit(f'ERRATUM: Gradus J viam canonicam tangit: {vetitum}')
    print('RECTE: Gradus J murem et interactionem multi-client separatam definit.')

if __name__=='__main__':
    main()
