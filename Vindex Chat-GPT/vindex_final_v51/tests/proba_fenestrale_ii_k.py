#!/usr/bin/env python3
"""Gradus K: resize, maximizatio, eventa clientium et damna verificat."""

from pathlib import Path
import re

R=Path(__file__).resolve().parents[1]
C=(R/'systema/uefi/fenestrale_native_k.c').read_text(encoding='utf-8')
SH=(R/'systema/uefi/construe_fenestrale_native_k.sh').read_text(encoding='utf-8')
ABI=(R/'systema/fenestrale_ii_compositor_k_abi.h').read_text(encoding='utf-8')
P=(R/'src/programmata_fenestrale_ii_k_runtime.vindex').read_text(encoding='utf-8')
T=(R/'src/tabula_fenestrale_ii_k_runtime.vindex').read_text(encoding='utf-8')
RT=(R/'tests/proba_fenestrale_ii_k_runtime.c').read_text(encoding='utf-8')

def req(textus,fragmentum,nomen):
    if fragmentum not in textus:
        raise SystemExit(f'ERRATUM: {nomen} deest: {fragmentum}')

def sine_commentariis_internis(textus,nomen):
    intra=False
    for linea in textus.splitlines():
        lota=linea.strip()
        if lota.startswith('FUNCTIO '): intra=True
        if intra and lota.startswith('//'):
            raise SystemExit(f'ERRATUM: commentarium internum compilatorem frangit: {nomen}')
        if lota=='FIN-FUNCTIO.': intra=False

def main():
    for fragmentum in (
        'FII_CMP_OP_EVENTUM',
        'FII_CMP_EVENTUM_FOCUS',
        'FII_CMP_EVENTUM_DIMENSIO',
        'FII_CMP_EVENTUM_ARG_TYPUS',
    ):
        req(ABI,fragmentum,'ABI K')
    for fragmentum in (
        'compone_region',
        'compone_duas',
        'cursor_redde',
        'TRACTIO_MENSURA',
        'mensuram_praevidere',
        'mensuram_confirma',
        'geometria_muta',
        'maxima_muta',
        'restitue_x',
        'clientem_eventum',
        'FII_CMP_EVENTUM_DIMENSIO',
        'q[i]==0xe8',
        'client_ingressus=target',
        'push %rbx',
        'ultimus_click_tituli',
        'opera->FreePool(info)',
        'mutatum||*bulla!=ante',
    ):
        req(C,fragmentum,'compositor K')
    if 'if(mota)compone()' in C:
        raise SystemExit('ERRATUM: motus cursoris totum framebuffer adhuc componit')
    for fragmentum in (
        'programmata_fenestrale_ii_k_runtime.vindex',
        'tabula_fenestrale_ii_k_runtime.vindex',
        'fenestrale_native_k.c',
        'FENESTRALEK.EFI',
        'fenestrale_k_uefi.img',
        'programmata_k',
        'tabula_k',
        '-Werror',
    ):
        req(SH,fragmentum,'constructio K')
    if 'Wno-error' in SH:
        raise SystemExit('ERRATUM: constructio K monita C tolerat')
    for nomen,textus,client in (('PROGRAMMATA K',P,'1'),('TABULA K',T,'2')):
        for fragmentum in (
            f'CONTENTUM(50335272) = {client}.',
            'status == 2 && operatio == 8',
            'CONTENTUM(50335408)',
            'SI eventum == 2',
            'REDDE 20.',
        ):
            req(textus,fragmentum,nomen)
        sine_commentariis_internis(textus,nomen)
    for fragmentum in ('MAP_FIXED_NOREPLACE','petitio CREA','eventum DIMENSIO','eventum FOCUS','clientem_voca','push %rbx'):
        req(RT,fragmentum,'probatio runtime K')
    if re.search(r'JL-UX',C,re.I):
        raise SystemExit('ERRATUM: branding JL-UX in compositorio K apparuit')
    for vetitum in ('firmamentum_uefi.c','systema/nucleus.vindex','BOOTX64.EFI"','systema_vindex_uefi.img"'):
        if vetitum in SH:
            raise SystemExit(f'ERRATUM: Gradus K viam canonicam tangit: {vetitum}')
    print('RECTE: Gradus K resize, maximizatio et eventa VINDEX vera definit.')

if __name__=='__main__':
    main()
