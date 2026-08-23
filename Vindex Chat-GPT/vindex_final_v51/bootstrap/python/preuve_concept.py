import struct

# Manu scribemus exsecutabile Linux x86-64 minimum.
# Hoc programma unam tantum rem facit: terminatur cum codice exitus 42.
# Nullus assembleur, nullus compilator: tantum octeta cruda.

# --- Codex machinalis (instructiones x86-64 hexadecimales) ---
# mov rax, 60      ; 60 = numerus vocationis systematis "exit" sub Linux
# mov rdi, 42      ; 42 = codex exitus quem reddere volumus
# syscall          ; nucleum Linux rogamus ut vocationem exsequatur

code_machine = bytes([
    0x48, 0xc7, 0xc0, 0x3c, 0x00, 0x00, 0x00,   # mov rax, 60
    0x48, 0xc7, 0xc7, 0x2a, 0x00, 0x00, 0x00,   # mov rdi, 42
    0x0f, 0x05                                    # syscall
])

# --- Forma ELF: involucrum quod Linux legere scit ut fasciculum exsequatur ---
base_addr = 0x400000
entete_taille = 64
prog_header_taille = 56
code_offset = entete_taille + prog_header_taille

entete_elf = struct.pack(
    "<4sBBBB8xHHIQQQIHHHHHH",
    b"\x7fELF", 2, 1, 1, 0,       # magia ELF, 64 bits, little-endian, versio, ABI
    2, 0x3e, 1,                   # typus=exsecutabile, machina=x86-64, versio
    base_addr + code_offset,      # punctum ingressus = ubi codex noster incipit
    entete_taille,                # offset program header
    0,                            # offset section header (nullum)
    0, entete_taille, prog_header_taille, 1, 0, 0, 0
)

program_header = struct.pack(
    "<IIQQQQQQ",
    1, 5,                         # typus=LOAD, indicia=R+X (lectio+exsecutio)
    0, base_addr, base_addr,      # offset, adressa virtualis, adressa physica
    code_offset + len(code_machine),  # mensura in fasciculo
    code_offset + len(code_machine),  # mensura in memoria
    0x1000                        # alignatio
)

with open("/tmp/preuve_concept", "wb") as f:
    f.write(entete_elf + program_header + code_machine)

import os
os.chmod("/tmp/preuve_concept", 0o755)
print("Exsecutabile creatum est sine instrumento externo.")
