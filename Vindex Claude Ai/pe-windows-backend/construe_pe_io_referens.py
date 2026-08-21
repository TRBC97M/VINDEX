#!/usr/bin/env python3
"""Exsecutabile PE64 quod catenam completam demonstrat: VirtualAlloc
(reservatio memoriae), scriptio directa in memoriam, CreateFileA +
WriteFile (memoria in fasciculum effusa), CreateFileA + ReadFile
(fasciculus relectus), CreateFileA + WriteFile iterum (secundus
fasciculus verificationis scriptus). Omnes quinque functiones — quas
RESERVA/APERI_SCRIBERE/MITTE/APERI_LEGERE/LEGE/CLAUDE sub Windows
requirent — hic simul in una catena probantur.

Nota: sequentia post has vocationes terminat per ExitProcess, quod in
hoc systemate probationis Wine defectum notum causat (vide
RELATIO-PE-WINDOWS.md, "GetStdHandle sequitur terminatio", quod idem
huic categoriae — quaevis vocatio quae HANDLE reddit, deinde
terminatio — pertinere videtur). Probatio hic non ex terminatione
ipsa pendet: fasciculi scripti post exsecutionem inspiciuntur."""
import struct

IMAGE_BASE = 0x140000000
FILE_ALIGN = 0x200
SECTION_ALIGN = 0x1000

def aligner(v, a):
    r = v % a
    return v if r == 0 else v + (a - r)

nomen_primus = b"proba_pe_io.txt\x00"
nomen_secundus = b"proba_pe_io_verificatio.txt\x00"
textus_initialis = b"ValAlloc PE!"

code = bytearray()
patches = []

def emettre(b):
    code.extend(b)

# sub rsp, 128 (spatium umbrae + multa loca scratch)
# NOTA: 128 non cadit in byte signato (-128..127 tantum), ergo forma
# brevis "83 /5 ib" male functionaret (fieret ADD, non SUB). Forma
# longa "81 /5 id" cum immediato 4 octetorum hic necessaria est.
emettre(bytes([0x48, 0x81, 0xEC]) + struct.pack('<I', 128))

# ================ 1. VirtualAlloc(NULL, 4096, MEM_COMMIT|MEM_RESERVE, PAGE_READWRITE) ================
emettre(bytes([0x48, 0x31, 0xC9]))                        # xor rcx, rcx
emettre(bytes([0xBA]) + struct.pack('<I', 4096))          # mov edx, 4096
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', 0x3000))  # mov r8d, MEM_COMMIT|MEM_RESERVE
emettre(bytes([0x41, 0xB9]) + struct.pack('<I', 0x04))    # mov r9d, PAGE_READWRITE
patches.append((len(code)+2, 'kernel32.dll', 'VirtualAlloc'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))
emettre(bytes([0x48, 0x89, 0x44, 0x24, 0x60]))            # mov [rsp+96], rax (locus memoriae)

# ================ 2. Scribe textus_initialis directe in memoriam reservatam ================
emettre(bytes([0x48, 0x8B, 0x5C, 0x24, 0x60]))            # mov rbx, [rsp+96]
for i, litt in enumerate(textus_initialis):
    emettre(bytes([0xC6, 0x43, i, litt]))                  # mov byte [rbx+i], litt

# ================ 3. CreateFileA(nomen_primus, GENERIC_WRITE, ..., CREATE_ALWAYS) ================
locus_lea_primus_w = len(code) + 3
emettre(bytes([0x48, 0x8D, 0x0D, 0, 0, 0, 0]))
emettre(bytes([0xBA]) + struct.pack('<I', 0x40000000))
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', 0))
emettre(bytes([0x4D, 0x31, 0xC9]))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x20]) + struct.pack('<i', 2))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x28]) + struct.pack('<i', 0x80))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x30]) + struct.pack('<i', 0))
patches.append((len(code)+2, 'kernel32.dll', 'CreateFileA'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))
emettre(bytes([0x48, 0x89, 0x44, 0x24, 0x68]))            # mov [rsp+104], rax (handle 1)

# ================ 4. WriteFile(handle1, memoria, longitudo, &scriptum, NULL) ================
emettre(bytes([0x48, 0x8B, 0x4C, 0x24, 0x68]))            # mov rcx, [rsp+104]
emettre(bytes([0x48, 0x8B, 0x54, 0x24, 0x60]))            # mov rdx, [rsp+96]
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', len(textus_initialis)))
emettre(bytes([0x4C, 0x8D, 0x4C, 0x24, 0x2C]))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x20, 0,0,0,0]))
patches.append((len(code)+2, 'kernel32.dll', 'WriteFile'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))

# ================ 5. CloseHandle(handle1) ================
emettre(bytes([0x48, 0x8B, 0x4C, 0x24, 0x68]))
patches.append((len(code)+2, 'kernel32.dll', 'CloseHandle'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))

# ================ 6. CreateFileA(nomen_primus, GENERIC_READ, ..., OPEN_EXISTING) ================
locus_lea_primus_r = len(code) + 3
emettre(bytes([0x48, 0x8D, 0x0D, 0, 0, 0, 0]))
emettre(bytes([0xBA]) + struct.pack('<I', 0x80000000))
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', 0))
emettre(bytes([0x4D, 0x31, 0xC9]))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x20]) + struct.pack('<i', 3))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x28]) + struct.pack('<i', 0x80))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x30]) + struct.pack('<i', 0))
patches.append((len(code)+2, 'kernel32.dll', 'CreateFileA'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))
emettre(bytes([0x48, 0x89, 0x44, 0x24, 0x68]))            # mov [rsp+104], rax (handle 2)

# ================ 7. ReadFile(handle2, buffer_lecti[rsp+112], longitudo, &lectum, NULL) ================
emettre(bytes([0x48, 0x8B, 0x4C, 0x24, 0x68]))
emettre(bytes([0x48, 0x8D, 0x54, 0x24, 0x70]))            # lea rdx, [rsp+112]
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', len(textus_initialis)))
emettre(bytes([0x4C, 0x8D, 0x4C, 0x24, 0x2C]))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x20, 0,0,0,0]))
patches.append((len(code)+2, 'kernel32.dll', 'ReadFile'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))

# ================ 8. CloseHandle(handle2) ================
emettre(bytes([0x48, 0x8B, 0x4C, 0x24, 0x68]))
patches.append((len(code)+2, 'kernel32.dll', 'CloseHandle'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))

# ================ 9. CreateFileA(nomen_secundus, GENERIC_WRITE, ..., CREATE_ALWAYS) ================
locus_lea_secundus = len(code) + 3
emettre(bytes([0x48, 0x8D, 0x0D, 0, 0, 0, 0]))
emettre(bytes([0xBA]) + struct.pack('<I', 0x40000000))
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', 0))
emettre(bytes([0x4D, 0x31, 0xC9]))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x20]) + struct.pack('<i', 2))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x28]) + struct.pack('<i', 0x80))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x30]) + struct.pack('<i', 0))
patches.append((len(code)+2, 'kernel32.dll', 'CreateFileA'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))
emettre(bytes([0x48, 0x89, 0x44, 0x24, 0x68]))            # mov [rsp+104], rax (handle 3)

# ================ 10. WriteFile(handle3, buffer_lecti, longitudo, &scriptum, NULL) ================
emettre(bytes([0x48, 0x8B, 0x4C, 0x24, 0x68]))
emettre(bytes([0x48, 0x8D, 0x54, 0x24, 0x70]))            # lea rdx, [rsp+112] (id quod lectum est)
emettre(bytes([0x41, 0xB8]) + struct.pack('<I', len(textus_initialis)))
emettre(bytes([0x4C, 0x8D, 0x4C, 0x24, 0x2C]))
emettre(bytes([0x48, 0xC7, 0x44, 0x24, 0x20, 0,0,0,0]))
patches.append((len(code)+2, 'kernel32.dll', 'WriteFile'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))

# ================ 11. CloseHandle(handle3) + ExitProcess(0) ================
emettre(bytes([0x48, 0x8B, 0x4C, 0x24, 0x68]))
patches.append((len(code)+2, 'kernel32.dll', 'CloseHandle'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))

emettre(bytes([0xB9]) + struct.pack('<i', 0))
patches.append((len(code)+2, 'kernel32.dll', 'ExitProcess'))
emettre(bytes([0xFF, 0x15, 0, 0, 0, 0]))
emettre(bytes([0xF4]))

offset_primus_in_textu = len(code)
code += nomen_primus
offset_secundus_in_textu = len(code)
code += nomen_secundus

mensura_codicis = len(code)

# ---------- Importationes ----------
dlls = [('kernel32.dll', ['VirtualAlloc', 'CreateFileA', 'ExitProcess', 'CloseHandle',
                           'WriteFile', 'ReadFile'])]

def construire_idata(dlls):
    nd = len(dlls)
    off_descriptorum = 0
    mensura_descriptorum = 20 * (nd + 1)
    cursor = mensura_descriptorum
    ilt_offsets, iat_offsets = {}, {}
    for nomen_dll, fns in dlls:
        ilt_offsets[nomen_dll] = cursor
        cursor += 8 * (len(fns) + 1)
    for nomen_dll, fns in dlls:
        iat_offsets[nomen_dll] = cursor
        cursor += 8 * (len(fns) + 1)
    hint_offsets = {}
    for nomen_dll, fns in dlls:
        for fn in fns:
            hint_offsets[(nomen_dll, fn)] = cursor
            elementum = struct.pack('<H', 0) + fn.encode() + b'\x00'
            if len(elementum) % 2 != 0:
                elementum += b'\x00'
            cursor += len(elementum)
    nomen_dll_offsets = {}
    for nomen_dll, fns in dlls:
        nomen_dll_offsets[nomen_dll] = cursor
        cursor += len(nomen_dll) + 1
    mensura_tota = aligner(cursor, 16)
    buf = bytearray(mensura_tota)
    return buf, off_descriptorum, mensura_descriptorum, ilt_offsets, iat_offsets, hint_offsets, nomen_dll_offsets, mensura_tota

(idata, off_descriptorum, mensura_descriptorum, ilt_offsets, iat_offsets,
 hint_offsets, nomen_dll_offsets, mensura_idata) = construire_idata(dlls)

capita_mensura_bruta = 0x40 + 24 + (112 + 16*8) + 40 + 40
capita_mensura_fasciculi = aligner(capita_mensura_bruta, FILE_ALIGN)
ptr_fasciculi_textus = capita_mensura_fasciculi
rva_textus = aligner(capita_mensura_fasciculi, SECTION_ALIGN)
mensura_textus_fasciculi = aligner(mensura_codicis, FILE_ALIGN)
mensura_textus_memoriae = aligner(mensura_codicis, SECTION_ALIGN)
ptr_fasciculi_idata = ptr_fasciculi_textus + mensura_textus_fasciculi
rva_idata = rva_textus + mensura_textus_memoriae
mensura_idata_fasciculi = aligner(mensura_idata, FILE_ALIGN)
mensura_idata_memoriae = aligner(mensura_idata, SECTION_ALIGN)
entry_rva = rva_textus
import_dir_rva = rva_idata + off_descriptorum
import_dir_mensura = mensura_descriptorum
premus_dll = dlls[0][0]
iat_rva = rva_idata + iat_offsets[premus_dll]
iat_mensura = 8 * (len(dlls[0][1]) + 1)
mensura_imaginis = aligner(rva_idata + mensura_idata_memoriae, SECTION_ALIGN)

struct.pack_into('<IIIII', idata, off_descriptorum,
                  rva_idata + ilt_offsets[premus_dll], 0, 0,
                  rva_idata + nomen_dll_offsets[premus_dll], rva_idata + iat_offsets[premus_dll])
struct.pack_into('<IIIII', idata, mensura_descriptorum - 20, 0, 0, 0, 0, 0)

for nomen_dll, fns in dlls:
    for j, fn in enumerate(fns):
        h = rva_idata + hint_offsets[(nomen_dll, fn)]
        struct.pack_into('<Q', idata, ilt_offsets[nomen_dll] + j*8, h)
        struct.pack_into('<Q', idata, iat_offsets[nomen_dll] + j*8, h)
    struct.pack_into('<Q', idata, ilt_offsets[nomen_dll] + len(fns)*8, 0)
    struct.pack_into('<Q', idata, iat_offsets[nomen_dll] + len(fns)*8, 0)

for (nomen_dll, fn), off in hint_offsets.items():
    struct.pack_into('<H', idata, off, 0)
    elementum = fn.encode() + b'\x00'
    idata[off+2:off+2+len(elementum)] = elementum

for nomen_dll, off in nomen_dll_offsets.items():
    nb = nomen_dll.encode() + b'\x00'
    idata[off:off+len(nb)] = nb

codex_finalis = bytearray(code)
locus_basis_textus = IMAGE_BASE + rva_textus
for offset_disp, nomen_dll, fn in patches:
    fns = dict(dlls)[nomen_dll]
    idx = fns.index(fn)
    locus_iat = IMAGE_BASE + rva_idata + iat_offsets[nomen_dll] + idx * 8
    locus_post_instr = locus_basis_textus + offset_disp + 4
    disp32 = locus_iat - locus_post_instr
    struct.pack_into('<i', codex_finalis, offset_disp, disp32)

for locus_lea, offset_in_textu in [(locus_lea_primus_w, offset_primus_in_textu),
                                     (locus_lea_primus_r, offset_primus_in_textu),
                                     (locus_lea_secundus, offset_secundus_in_textu)]:
    locus_nomen = locus_basis_textus + offset_in_textu
    disp32 = locus_nomen - (locus_basis_textus + locus_lea + 4)
    struct.pack_into('<i', codex_finalis, locus_lea, disp32)

def construire_capita():
    buf = bytearray()
    buf += struct.pack('<H', 0x5A4D)
    buf += b'\x00' * 58
    buf += struct.pack('<I', 0x40)
    buf += struct.pack('<I', 0x00004550)
    buf += struct.pack('<HH', 0x8664, 2)
    buf += struct.pack('<III', 0, 0, 0)
    mensura_optionalis = 112 + 16*8
    buf += struct.pack('<HH', mensura_optionalis, 0x0022)
    buf += struct.pack('<H', 0x020B)
    buf += bytes([0, 0])
    buf += struct.pack('<I', mensura_textus_memoriae)
    buf += struct.pack('<I', mensura_idata_memoriae)
    buf += struct.pack('<I', 0)
    buf += struct.pack('<I', entry_rva)
    buf += struct.pack('<I', rva_textus)
    buf += struct.pack('<Q', IMAGE_BASE)
    buf += struct.pack('<I', SECTION_ALIGN)
    buf += struct.pack('<I', FILE_ALIGN)
    buf += struct.pack('<HHHHHH', 6, 0, 0, 0, 6, 0)
    buf += struct.pack('<I', 0)
    buf += struct.pack('<I', mensura_imaginis)
    buf += struct.pack('<I', capita_mensura_fasciculi)
    buf += struct.pack('<I', 0)
    buf += struct.pack('<HH', 3, 0)
    buf += struct.pack('<QQQQ', 0x100000, 0x1000, 0x100000, 0x1000)
    buf += struct.pack('<I', 0)
    buf += struct.pack('<I', 16)
    elenchi = [(0,0)] * 16
    elenchi[1] = (import_dir_rva, import_dir_mensura)
    elenchi[12] = (iat_rva, iat_mensura)
    for r, s in elenchi:
        buf += struct.pack('<II', r, s)
    buf += b'.text\x00\x00\x00'
    buf += struct.pack('<IIIIIIHHI', mensura_textus_memoriae, rva_textus, mensura_textus_fasciculi,
                        ptr_fasciculi_textus, 0, 0, 0, 0, 0x60000020)
    buf += b'.idata\x00\x00'
    buf += struct.pack('<IIIIIIHHI', mensura_idata_memoriae, rva_idata, mensura_idata_fasciculi,
                        ptr_fasciculi_idata, 0, 0, 0, 0, 0xC0000040)
    return buf

capita = construire_capita()
fasciculus = bytearray()
fasciculus += capita
fasciculus += b'\x00' * (capita_mensura_fasciculi - len(capita))
fasciculus += codex_finalis
fasciculus += b'\x00' * (mensura_textus_fasciculi - len(codex_finalis))
fasciculus += idata
fasciculus += b'\x00' * (mensura_idata_fasciculi - len(idata))

with open('exemplum_io.exe', 'wb') as f:
    f.write(fasciculus)
print("Fasciculus scriptus:", len(fasciculus), "octeta")
