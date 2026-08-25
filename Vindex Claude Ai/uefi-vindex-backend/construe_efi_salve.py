#!/usr/bin/env python3
"""Prototypum II: exsecutabile UEFI quod vere nuntium per firmware scribit.

Adhibet SystemTable->ConOut->OutputString, ABI Microsoft x64.
Probat non solum onerationem, sed vocationem firmware realem ex codice nostro.
"""
import struct

# Ingressus: RCX = ImageHandle, RDX = SystemTable
# SystemTable->ConOut est ad offset 64 (0x40)
# ConOut->OutputString est ad offset 8 intra structuram SIMPLE_TEXT_OUTPUT
#
# sub rsp, 40           ; spatium umbrae (32) + alignatio
# mov rax, [rdx+0x40]   ; RAX = ConOut
# mov rcx, rax          ; arg1 = ConOut (this)
# lea rdx, [rip+msg]    ; arg2 = catena UTF-16
# call [rax+0x08]       ; ConOut->OutputString(ConOut, msg)
# xor eax, eax          ; redde EFI_SUCCESS
# add rsp, 40
# ret

nuntius = "VINDEX UEFI\r\n".encode('utf-16-le') + b'\x00\x00'

codex = bytearray()
codex += bytes([0x48, 0x83, 0xEC, 0x28])              # sub rsp, 40
codex += bytes([0x48, 0x8B, 0x42, 0x40])              # mov rax, [rdx+0x40]  (ConOut)
codex += bytes([0x48, 0x89, 0xC1])                    # mov rcx, rax
# lea rdx, [rip + disp32] -- disp calcule apres
lea_pos = len(codex)
codex += bytes([0x48, 0x8D, 0x15, 0, 0, 0, 0])        # lea rdx, [rip+disp32]
codex += bytes([0xFF, 0x50, 0x08])                    # call [rax+8]  (OutputString)
codex += bytes([0x31, 0xC0])                          # xor eax, eax
codex += bytes([0x48, 0x83, 0xC4, 0x28])              # add rsp, 40
codex += bytes([0xC3])                                # ret

# nuntius immediate post codicem
off_nuntius = len(codex)
disp = off_nuntius - (lea_pos + 7)   # RIP-relatif: apres l'instruction complete
struct.pack_into('<i', codex, lea_pos + 3, disp)
codex += nuntius

codex = bytes(codex)

ALIGN_FASC, ALIGN_SECT, CAPITA, BASIS = 512, 4096, 512, 0x140000000
mensura_text_fasc = ((len(codex) + ALIGN_FASC - 1) // ALIGN_FASC) * ALIGN_FASC
mensura_text_mem = ((len(codex) + ALIGN_SECT - 1) // ALIGN_SECT) * ALIGN_SECT
rva_text = ALIGN_SECT
mensura_imaginis = ((rva_text + mensura_text_mem + ALIGN_SECT - 1) // ALIGN_SECT) * ALIGN_SECT

buf = bytearray(CAPITA + mensura_text_fasc)
struct.pack_into('<H', buf, 0, 0x5A4D)
struct.pack_into('<I', buf, 60, 64)
struct.pack_into('<I', buf, 64, 0x00004550)
struct.pack_into('<H', buf, 68, 0x8664)
struct.pack_into('<H', buf, 70, 1)
struct.pack_into('<H', buf, 84, 240)
struct.pack_into('<H', buf, 86, 0x0022)
struct.pack_into('<H', buf, 88, 0x20B)
struct.pack_into('<I', buf, 92, mensura_text_mem)
struct.pack_into('<I', buf, 104, rva_text)
struct.pack_into('<I', buf, 108, rva_text)
struct.pack_into('<Q', buf, 112, BASIS)
struct.pack_into('<I', buf, 120, ALIGN_SECT)
struct.pack_into('<I', buf, 124, ALIGN_FASC)
struct.pack_into('<H', buf, 128, 6)
struct.pack_into('<H', buf, 136, 6)
struct.pack_into('<I', buf, 144, mensura_imaginis)
struct.pack_into('<I', buf, 148, CAPITA)
struct.pack_into('<H', buf, 156, 10)          # SUBSYSTEM = EFI APPLICATION
struct.pack_into('<Q', buf, 160, 0x100000)
struct.pack_into('<Q', buf, 168, 0x1000)
struct.pack_into('<Q', buf, 176, 0x100000)
struct.pack_into('<Q', buf, 184, 0x1000)
struct.pack_into('<I', buf, 196, 16)
buf[328:336] = b'.text\0\0\0'
struct.pack_into('<I', buf, 336, mensura_text_mem)
struct.pack_into('<I', buf, 340, rva_text)
struct.pack_into('<I', buf, 344, mensura_text_fasc)
struct.pack_into('<I', buf, 348, CAPITA)
struct.pack_into('<I', buf, 364, 0x60000020)
buf[CAPITA:CAPITA + len(codex)] = codex

with open('esp/EFI/BOOT/BOOTX64.EFI', 'wb') as f:
    f.write(bytes(buf))
print(f"creatum: {len(buf)} octeta, codex={len(codex)}, disp_lea={disp}")
