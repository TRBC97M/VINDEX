#!/usr/bin/env python3
"""Exsecutabile PE minimum, octetum post octetum, cum ExitProcess(42).

Prototypum praeit ante translationem in VINDEX (CONSTRUE_CAPUT_PE)."""
import struct

IMAGE_BASE = 0x140000000
FILE_ALIGN = 0x200
SECTION_ALIGN = 0x1000

def aligner(valor, alignamentum):
    residuum = valor % alignamentum
    if residuum == 0:
        return valor
    return valor + (alignamentum - residuum)

# ---------- Codex sectionis .text ----------
# sub rsp, 40 ; mov ecx, 42 ; call [rip+X] -> IAT ExitProcess ; hlt
code = bytearray()
code += bytes([0x48, 0x83, 0xEC, 0x28])          # sub rsp, 40
code += bytes([0xB9, 42, 0, 0, 0])                # mov ecx, 42
# call qword [rip+disp32] -- FF 15 disp32, distantia postea computanda
call_patch_offset = len(code)
code += bytes([0xFF, 0x15, 0, 0, 0, 0])           # call [rip+???] (postea complenda)
code += bytes([0xF4])                              # hlt (numquam normaliter attingitur)

mensura_codicis = len(code)

# ---------- Data .idata (tabula importationis) ----------
# Dispositio (ordine scriptionis, spatia relativa ad idata_start):
#   0  : Descriptor Importationis (kernel32)     20 octeta
#   20 : Descriptor Importationis terminalis nullus 20 octeta
#   40 : ILT (Import Lookup Table)  1 elementum + terminator = 16 octeta
#   56 : IAT (Import Address Table) eadem forma  = 16 octeta
#   72 : Hint/Name pro ExitProcess
#   ?  : Nomen "kernel32.dll"

off_descriptorum = 0
off_descriptoris_nulli = 20
off_ilt = 40
off_iat = 56
off_hint = 72
nomen_functionis = b'ExitProcess\x00'
if len(nomen_functionis) % 2 != 0:
    nomen_functionis += b'\x00'
mensura_hint_elementi = 2 + len(nomen_functionis)
off_nom_dll = off_hint + mensura_hint_elementi
nomen_dll = b'kernel32.dll\x00'
mensura_idata = off_nom_dll + len(nomen_dll)
mensura_idata = aligner(mensura_idata, 16)

def rva(spatium_in_sectione, basis_rva_sectionis):
    return basis_rva_sectionis + spatium_in_sectione

# ---------- Calculus adressarum virtualium (RVA) et spatiorum fasciculi ----------
# Capita
mensura_dos_pe_opt_sectionum = 0  # postea calculanda per constructionem realem

# Prius capita in tabulario separato construimus ut magnitudinem exactam sciamus
def construe_capita(rva_text, mensura_textus_memoriae, ptr_fichier_text, mensura_textus_fasciculi,
                        rva_idata, mensura_idata_memoriae, ptr_fichier_idata, mensura_idata_fasciculi,
                        entry_rva, import_dir_rva, import_dir_size, iat_rva, iat_size,
                        mensura_imaginis, mensura_capitum_alignata):
    buf = bytearray()
    # Caput DOS (64 octeta)
    buf += struct.pack('<H', 0x5A4D)          # e_magic
    buf += b'\x00' * 58
    buf += struct.pack('<I', 0x40)             # e_lfanew (statim post, 0x40)
    assert len(buf) == 0x40

    # Caput PE
    buf += struct.pack('<I', 0x00004550)       # signature
    buf += struct.pack('<HH', 0x8664, 2)       # machine, nb sections
    buf += struct.pack('<III', 0, 0, 0)        # timestamp, symtable, nsyms
    mensura_optionalis = 112 + 16 * 8
    buf += struct.pack('<HH', mensura_optionalis, 0x0022)  # SizeOfOptionalHeader, Characteristics

    # Caput optionale (PE32+)
    buf += struct.pack('<H', 0x020B)           # Magic
    buf += bytes([0, 0])                        # linker version
    buf += struct.pack('<I', mensura_textus_memoriae)   # SizeOfCode
    buf += struct.pack('<I', mensura_idata_memoriae)  # SizeOfInitializedData
    buf += struct.pack('<I', 0)                  # SizeOfUninitializedData
    buf += struct.pack('<I', entry_rva)          # AddressOfEntryPoint
    buf += struct.pack('<I', rva_text)           # BaseOfCode
    buf += struct.pack('<Q', IMAGE_BASE)
    buf += struct.pack('<I', SECTION_ALIGN)
    buf += struct.pack('<I', FILE_ALIGN)
    buf += struct.pack('<HHHHHH', 6, 0, 0, 0, 6, 0)
    buf += struct.pack('<I', 0)                  # Win32VersionValue
    buf += struct.pack('<I', mensura_imaginis)       # SizeOfImage
    buf += struct.pack('<I', mensura_capitum_alignata) # SizeOfHeaders
    buf += struct.pack('<I', 0)                  # CheckSum
    buf += struct.pack('<HH', 3, 0)              # Subsystem CONSOLE, DllCharacteristics
    buf += struct.pack('<QQQQ', 0x100000, 0x1000, 0x100000, 0x1000)
    buf += struct.pack('<I', 0)                  # LoaderFlags
    buf += struct.pack('<I', 16)                 # NumberOfRvaAndSizes
    # 16 elenchi datorum
    dirs = [(0,0)] * 16
    dirs[1] = (import_dir_rva, import_dir_size)   # Import
    dirs[12] = (iat_rva, iat_size)                 # IAT
    for r, s in dirs:
        buf += struct.pack('<II', r, s)

    # Caput sectionis .text
    buf += b'.text\x00\x00\x00'
    buf += struct.pack('<IIIIIIHHI', mensura_textus_memoriae, rva_text, mensura_textus_fasciculi,
                        ptr_fichier_text, 0, 0, 0, 0, 0x60000020)
    # Caput sectionis .idata
    buf += b'.idata\x00\x00'
    buf += struct.pack('<IIIIIIHHI', mensura_idata_memoriae, rva_idata, mensura_idata_fasciculi,
                        ptr_fichier_idata, 0, 0, 0, 0, 0xC0000040)

    return buf

# Primus gradus: magnitudinem capitum aestimare (constans hic, iam nota)
capita_mensura_bruta = 0x40 + 24 + (112 + 16*8) + 40 + 40  # DOS+PE+Opt+2 sections
capita_mensura_fasciculi = aligner(capita_mensura_bruta, FILE_ALIGN)

ptr_fichier_text = capita_mensura_fasciculi
rva_text = aligner(capita_mensura_fasciculi, SECTION_ALIGN)  # 1er RVA de section alignee
mensura_textus_fasciculi = aligner(mensura_codicis, FILE_ALIGN)
mensura_textus_memoriae = aligner(mensura_codicis, SECTION_ALIGN)

ptr_fichier_idata = ptr_fichier_text + mensura_textus_fasciculi
rva_idata = rva_text + mensura_textus_memoriae
mensura_idata_fasciculi = aligner(mensura_idata, FILE_ALIGN)
mensura_idata_memoriae = aligner(mensura_idata, SECTION_ALIGN)

entry_rva = rva_text
import_dir_rva = rva_idata + off_descriptorum
import_dir_size = 40  # 2 descripteurs de 20 octets
iat_va_rva = rva_idata + off_iat
iat_size = 16

mensura_imaginis = aligner(rva_idata + mensura_idata_memoriae, SECTION_ALIGN)

capita = construe_capita(
    rva_text, mensura_textus_memoriae, ptr_fichier_text, mensura_textus_fasciculi,
    rva_idata, mensura_idata_memoriae, ptr_fichier_idata, mensura_idata_fasciculi,
    entry_rva, import_dir_rva, import_dir_size, iat_va_rva, iat_size,
    mensura_imaginis, capita_mensura_fasciculi
)
assert len(capita) == capita_mensura_bruta, (len(capita), capita_mensura_bruta)

# ---------- Vocationem indirectam complere, adressis iam notis ----------
locus_instr_post_vocationem = IMAGE_BASE + rva_text + call_patch_offset + 6  # RIP post instructionem call
locus_iat_elementi = IMAGE_BASE + iat_va_rva
disp32 = locus_iat_elementi - locus_instr_post_vocationem
code[call_patch_offset+2:call_patch_offset+6] = struct.pack('<i', disp32)

# ---------- Octeta .idata construere ----------
idata = bytearray(mensura_idata)
# Descriptor importationis (OriginalFirstThunk, TimeDateStamp, ForwarderChain, Name, FirstThunk)
struct.pack_into('<IIIII', idata, off_descriptorum,
                  rva_idata + off_ilt, 0, 0, rva_idata + off_nom_dll, rva_idata + off_iat)
struct.pack_into('<IIIII', idata, off_descriptoris_nulli, 0, 0, 0, 0, 0)
# ILT: unum elementum ad Hint/Name monstrans, deinde terminator nullus
struct.pack_into('<Q', idata, off_ilt, rva_idata + off_hint)
struct.pack_into('<Q', idata, off_ilt + 8, 0)
# IAT: identica ILT ante resolutionem ab initiatore
struct.pack_into('<Q', idata, off_iat, rva_idata + off_hint)
struct.pack_into('<Q', idata, off_iat + 8, 0)
# Hint/Name
struct.pack_into('<H', idata, off_hint, 0)
idata[off_hint+2:off_hint+2+len(nomen_functionis)] = nomen_functionis
# Nomen DLL
idata[off_nom_dll:off_nom_dll+len(nomen_dll)] = nomen_dll

# ---------- Fasciculum finalem componere ----------
fasciculus = bytearray()
fasciculus += capita
fasciculus += b'\x00' * (capita_mensura_fasciculi - len(capita))
fasciculus += code
fasciculus += b'\x00' * (mensura_textus_fasciculi - len(code))
fasciculus += idata
fasciculus += b'\x00' * (mensura_idata_fasciculi - len(idata))

with open('exemplum_referens.exe', 'wb') as f:
    f.write(fasciculus)

print("Fasciculus scriptus:", len(fasciculus), "octeta")
print("rva_text:", hex(rva_text), "rva_idata:", hex(rva_idata))
print("entry_rva:", hex(entry_rva))
print("iat_va_rva:", hex(iat_va_rva))
