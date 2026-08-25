#!/usr/bin/env python3
"""Prototypum: exsecutabile UEFI (PE32+ subsystem 10) minimum sine C.

Nihil facit nisi statim redire ad firmware cum EFI_SUCCESS (0).
Si firmware hoc onerat et exsequitur sine defectu, mechanismus probatus est.
"""
import struct

# --- codex machinalis: xor eax,eax ; ret ---
# Ingressus UEFI accipit (RCX=ImageHandle, RDX=SystemTable), reddit EFI_STATUS in RAX.
codex = bytes([0x48, 0x31, 0xC0, 0xC3])  # xor rax,rax ; ret

ALIGN_FASC = 512
ALIGN_SECT = 4096
CAPITA = 512
BASIS = 0x140000000

mensura_text_fasc = ((len(codex) + ALIGN_FASC - 1) // ALIGN_FASC) * ALIGN_FASC
mensura_text_mem = ((len(codex) + ALIGN_SECT - 1) // ALIGN_SECT) * ALIGN_SECT
rva_text = ALIGN_SECT
mensura_imaginis = ((rva_text + mensura_text_mem + ALIGN_SECT - 1) // ALIGN_SECT) * ALIGN_SECT

buf = bytearray(CAPITA + mensura_text_fasc)

# DOS header
struct.pack_into('<H', buf, 0, 0x5A4D)          # MZ
struct.pack_into('<I', buf, 60, 64)             # e_lfanew -> PE header a 64

# PE signature
struct.pack_into('<I', buf, 64, 0x00004550)     # "PE\0\0"
# COFF header
struct.pack_into('<H', buf, 68, 0x8664)         # machina AMD64
struct.pack_into('<H', buf, 70, 1)              # numerus sectionum
struct.pack_into('<I', buf, 72, 0)              # TimeDateStamp
struct.pack_into('<I', buf, 76, 0)              # PointerToSymbolTable
struct.pack_into('<I', buf, 80, 0)              # NumberOfSymbols
struct.pack_into('<H', buf, 84, 240)            # SizeOfOptionalHeader
struct.pack_into('<H', buf, 86, 0x0022)         # Characteristics: EXECUTABLE | LARGE_ADDRESS_AWARE

# Optional header (PE32+)
struct.pack_into('<H', buf, 88, 0x20B)          # magia PE32+
struct.pack_into('<I', buf, 92, mensura_text_mem)   # SizeOfCode
struct.pack_into('<I', buf, 104, rva_text)      # AddressOfEntryPoint
struct.pack_into('<I', buf, 108, rva_text)      # BaseOfCode
struct.pack_into('<Q', buf, 112, BASIS)         # ImageBase
struct.pack_into('<I', buf, 120, ALIGN_SECT)    # SectionAlignment
struct.pack_into('<I', buf, 124, ALIGN_FASC)    # FileAlignment
struct.pack_into('<H', buf, 128, 6)             # MajorOSVersion
struct.pack_into('<H', buf, 136, 6)             # MajorSubsystemVersion
struct.pack_into('<I', buf, 144, mensura_imaginis)  # SizeOfImage
struct.pack_into('<I', buf, 148, CAPITA)        # SizeOfHeaders
struct.pack_into('<H', buf, 156, 10)            # *** SUBSYSTEM = 10 (EFI APPLICATION) ***
struct.pack_into('<Q', buf, 160, 0x100000)      # SizeOfStackReserve
struct.pack_into('<Q', buf, 168, 0x1000)        # SizeOfStackCommit
struct.pack_into('<Q', buf, 176, 0x100000)      # SizeOfHeapReserve
struct.pack_into('<Q', buf, 184, 0x1000)        # SizeOfHeapCommit
struct.pack_into('<I', buf, 196, 16)            # NumberOfRvaAndSizes

# Section header .text (a 328 = 88 + 240)
buf[328:336] = b'.text\0\0\0'
struct.pack_into('<I', buf, 336, mensura_text_mem)  # VirtualSize
struct.pack_into('<I', buf, 340, rva_text)          # VirtualAddress
struct.pack_into('<I', buf, 344, mensura_text_fasc) # SizeOfRawData
struct.pack_into('<I', buf, 348, CAPITA)            # PointerToRawData
struct.pack_into('<I', buf, 364, 0x60000020)        # CODE | EXECUTE | READ

buf[CAPITA:CAPITA + len(codex)] = codex

with open('BOOTX64.EFI', 'wb') as f:
    f.write(bytes(buf))
print(f"BOOTX64.EFI creatum: {len(buf)} octeta, subsystem=10 (UEFI)")
