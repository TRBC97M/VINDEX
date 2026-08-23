#!/usr/bin/env python3
"""Gradus I: duos clientes, registrum superficierum et z-order verificat."""

from pathlib import Path
import re

R=Path(__file__).resolve().parents[1]
C=(R/'systema/uefi/fenestrale_native_i.c').read_text(encoding='utf-8')
SH=(R/'systema/uefi/construe_fenestrale_native_i.sh').read_text(encoding='utf-8')
P=(R/'src/programmata_fenestrale_ii_h.vindex').read_text(encoding='utf-8')
T=(R/'src/tabula_fenestrale_ii_i.vindex').read_text(encoding='utf-8')
TR=(R/'src/tabula_fenestrale_ii_i_runtime.vindex').read_text(encoding='utf-8')

def req(t,s,n):
    if s not in t: raise SystemExit(f'ERRATUM: {n} deest: {s}')

def main():
    for s in ('SUPERFICIES_CAPACITAS 8U','superficies[SUPERFICIES_CAPACITAS]','ordo[SUPERFICIES_CAPACITAS]','ordinem_remove','focus(','alterna_focus','_binary_programmata_h_elf_start','_binary_tabula_i_elf_start','clientem_onera','mailbox_age','d->taskbar_altitudo=28'):
        req(C,s,'compositor I')
    for s in ('programmata_fenestrale_ii_h.vindex','tabula_fenestrale_ii_i_runtime.vindex','programmata_h','tabula_i','fenestrale_native_i.c','FENESTRALEI.EFI','fenestrale_i_uefi.img'):
        req(SH,s,'constructio I')
    for s in ('CONTENTUM(50335272) = 1.','H_PINGE','barra != 28'):
        req(P,s,'PROGRAMMATA H')
    for s in ('CONTENTUM(50335272) = 2.','T_PINGE','T_RECT','barra != 28','cellw SICUT NUMERUS','cellh SICUT NUMERUS','cellw * 8','cellh * 12'):
        req(T,s,'TABULA I plena')
    for s in ('CONTENTUM(50335272) = 2.','H_PINGE','H_RECT','H_COLOR','barra != 28'):
        req(TR,s,'TABULA I runtime')
    if 'DUM col' in T or 'DUM row' in T:
        raise SystemExit('ERRATUM: rete TABULA cyclis complexis iterum utitur')
    for nomen,textus in (('TABULA plena',T),('TABULA runtime',TR)):
        if 'FENESTRALE_II_FRAMEBUFFER' in textus:
            raise SystemExit(f'ERRATUM: {nomen} framebuffer globalem petit')
        if re.search(r'JL-UX',textus,re.I):
            raise SystemExit(f'ERRATUM: branding JL-UX in {nomen} apparuit')
    for vetitum in ('firmamentum_uefi.c','systema/nucleus.vindex','BOOTX64.EFI"','systema_vindex_uefi.img"'):
        if vetitum in SH: raise SystemExit(f'ERRATUM: Gradus I viam canonicam tangit: {vetitum}')
    print('RECTE: Gradus I duos clientes privatos et z-order dynamicum definit.')

if __name__=='__main__': main()
