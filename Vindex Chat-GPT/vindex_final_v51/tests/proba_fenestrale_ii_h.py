#!/usr/bin/env python3
"""Contractum Gradus H inter compositorium UEFI et clientem VINDEX verificat."""

from pathlib import Path
import re

RADIX = Path(__file__).resolve().parents[1]
C = RADIX / "systema" / "uefi" / "fenestrale_native_h.c"
SH = RADIX / "systema" / "uefi" / "construe_fenestrale_native_h.sh"
CLIENT = RADIX / "src" / "programmata_fenestrale_ii_h.vindex"
HEADER = RADIX / "systema" / "fenestrale_ii_compositor_abi.h"


def require(textus: str, fragmentum: str, nomen: str) -> None:
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: {nomen} deest: {fragmentum}")


def main() -> None:
    c = C.read_text(encoding="utf-8")
    sh = SH.read_text(encoding="utf-8")
    client = CLIENT.read_text(encoding="utf-8")
    header = HEADER.read_text(encoding="utf-8")

    for fragmentum in (
        'extern U8 _binary_programmata_g_elf_start[];',
        'FENESTRALE2_COMPOSITOR_MAILBOX',
        'FII_CAP_COMPOSITORIUM',
        'FII_CMP_OP_CREA',
        'FII_CMP_OP_PRAESENTA',
        'AllocatePool',
        'clientem_voca',
        'clientem_gradus_init',
        'mailbox_age',
        'd->taskbar_altitudo=28',
        'client_surface.formatum=0',
        'client_surface.visibilis=1;compone()',
    ):
        require(c, fragmentum, "compositorium H")

    for fragmentum in (
        'programmata_fenestrale_ii_h.vindex',
        'programmata_g.elf',
        'objcopy -I binary -O pe-x86-64',
        'fenestrale_native_h.c',
        'fac_imaginem_uefi.py',
        'FENESTRALEH.EFI',
        'fenestrale_h_uefi.img',
    ):
        require(sh, fragmentum, "constructio H")

    for fragmentum in (
        'CONTENTUM(50335264) = 1.',
        'CONTENTUM(50335256) = 1.',
        'CONTENTUM(50335264) = 3.',
        'H_RECT',
        'H_PINGE',
        'CONTENTUM(50334064)',
        'barra != 28',
    ):
        require(client, fragmentum, "client PROGRAMMATA H")

    require(header, '#define FENESTRALE2_COMPOSITOR_BASIS   0x03000E00ULL', 'ABI G')
    require(header, '#define FENESTRALE2_COMPOSITOR_MENSURA 256ULL', 'ABI G')

    if 'FENESTRALE_II_FRAMEBUFFER' in client:
        raise SystemExit("ERRATUM: client H framebuffer globalem directe petit")
    if re.search(r'JL-UX', client, re.IGNORECASE):
        raise SystemExit("ERRATUM: branding JL-UX in cliente H apparuit")

    # H manet experimentum separatum; nomina canonica non includuntur ut exitus scribendi.
    if 'BOOTX64.EFI"' in sh or 'systema_vindex_uefi.img"' in sh:
        raise SystemExit("ERRATUM: constructio H exitum canonicum petit")
    if re.search(r'firmamentum_uefi\.c', sh):
        raise SystemExit("ERRATUM: Gradus H firmamentum canonicum compilat")
    if re.search(r'systema/nucleus\.vindex', sh):
        raise SystemExit("ERRATUM: Gradus H nucleum canonicum tangit")

    print("RECTE: Gradus H compositorium separatum et clientem H coniungit.")


if __name__ == "__main__":
    main()
