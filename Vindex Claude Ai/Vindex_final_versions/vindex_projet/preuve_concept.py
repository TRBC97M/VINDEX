import struct

# On va écrire, à la main, un exécutable Linux x86-64 minimal.
# Ce programme ne fait qu'une chose : il se termine avec le code de sortie 42.
# Aucun assembleur, aucun compilateur : juste des octets bruts.

# --- Le code machine (instructions x86-64 en hexadécimal) ---
# mov rax, 60      ; 60 = numéro de l'appel système "exit" sous Linux
# mov rdi, 42      ; 42 = le code de sortie qu'on veut renvoyer
# syscall          ; on demande au noyau Linux d'exécuter l'appel

code_machine = bytes([
    0x48, 0xc7, 0xc0, 0x3c, 0x00, 0x00, 0x00,   # mov rax, 60
    0x48, 0xc7, 0xc7, 0x2a, 0x00, 0x00, 0x00,   # mov rdi, 42
    0x0f, 0x05                                    # syscall
])

# --- Le format ELF : l'enveloppe que Linux sait lire pour exécuter un fichier ---
base_addr = 0x400000
entete_taille = 64
prog_header_taille = 56
code_offset = entete_taille + prog_header_taille

entete_elf = struct.pack(
    "<4sBBBB8xHHIQQQIHHHHHH",
    b"\x7fELF", 2, 1, 1, 0,       # magie ELF, 64 bits, little-endian, version, ABI
    2, 0x3e, 1,                   # type=exécutable, machine=x86-64, version
    base_addr + code_offset,      # point d'entrée = où commence notre code
    entete_taille,                # offset du program header
    0,                            # offset section header (aucune)
    0, entete_taille, prog_header_taille, 1, 0, 0, 0
)

program_header = struct.pack(
    "<IIQQQQQQ",
    1, 5,                         # type=LOAD, flags=R+X (lecture+exécution)
    0, base_addr, base_addr,      # offset, adresse virtuelle, adresse physique
    code_offset + len(code_machine),  # taille dans le fichier
    code_offset + len(code_machine),  # taille en mémoire
    0x1000                        # alignement
)

with open("/home/claude/langfr/preuve_concept", "wb") as f:
    f.write(entete_elf + program_header + code_machine)

import os
os.chmod("/home/claude/langfr/preuve_concept", 0o755)
print("Exécutable créé, sans aucun outil externe.")
