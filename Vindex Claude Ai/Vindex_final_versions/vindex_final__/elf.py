"""
Construction du fichier exécutable ELF64 final, sans aucun outil externe.
"""

import struct

BASE_ADDR = 0x400000
TAILLE_ENTETE = 64
TAILLE_PROGRAM_HEADER = 56
DECALAGE_CODE = TAILLE_ENTETE + TAILLE_PROGRAM_HEADER


def construire_elf(code: bytes, decalage_point_entree: int) -> bytes:
    """
    code : les octets machine complets (fonctions + routines internes + données)
    decalage_point_entree : position, dans `code`, où l'exécution doit démarrer
                             (c'est-à-dire l'étiquette de la fonction PRINCIPALIS)
    """
    point_entree = BASE_ADDR + DECALAGE_CODE + decalage_point_entree

    entete_elf = struct.pack(
        "<4sBBBB8xHHIQQQIHHHHHH",
        b"\x7fELF", 2, 1, 1, 0,
        2, 0x3e, 1,
        point_entree,
        TAILLE_ENTETE,
        0,
        0, TAILLE_ENTETE, TAILLE_PROGRAM_HEADER, 1, 0, 0, 0
    )

    taille_totale = DECALAGE_CODE + len(code)
    program_header = struct.pack(
        "<IIQQQQQQ",
        1, 7,  # type=LOAD, flags=R+W+X (lecture+écriture+exécution)
        0, BASE_ADDR, BASE_ADDR,
        taille_totale, taille_totale,
        0x1000
    )

    return entete_elf + program_header + code
