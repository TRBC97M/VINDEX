"""
Assembleur x86-64 manu factus.
Instructiones directe in octeta machinalia codificat, sine ullo
instrumento externo (non nasm, non gcc).

Quaevis methodus instructioni processoris respondet et scit
quomodo eam in octeta transferre, secundum regulas codificationis
x86-64 (praefixum REX, ModRM, immediata...).
"""

RAX, RCX, RDX, RBX, RSP, RBP, RSI, RDI = range(8)
R8, R9, R10, R11, R12, R13, R14, R15 = range(8, 16)


class Assembleur:
    def __init__(self):
        self.code = bytearray()
        self.etiquettes = {}     # nom -> position dans self.code
        self.correctifs = []     # (position, nom_etiquette, taille, mode)

    # --- Instrumenta gradu infimo ---

    def etiquette(self, nom):
        self.etiquettes[nom] = len(self.code)

    def _rex(self, w=1, r=0, x=0, b=0):
        octet = 0x40 | (w << 3) | (r << 2) | (x << 1) | b
        self.code.append(octet)

    def _modrm(self, mod, reg, rm):
        self.code.append((mod << 6) | ((reg & 7) << 3) | (rm & 7))

    def _imm32(self, valeur):
        self.code += int(valeur).to_bytes(4, "little", signed=(valeur < 0))

    def _imm64(self, valeur):
        self.code += int(valeur).to_bytes(8, "little", signed=(valeur < 0))

    def _reserver_correctif(self, nom_etiquette, taille, mode):
        self.correctifs.append((len(self.code), nom_etiquette, taille, mode))
        self.code += bytes(taille)

    # --- Translatio datorum ---

    def mov_reg_imm64(self, dst, valeur):
        self._rex(1, 0, 0, dst >> 3)
        self.code.append(0xB8 + (dst & 7))
        self._imm64(valeur)

    def mov_reg_reg(self, dst, src):
        self._rex(1, src >> 3, 0, dst >> 3)
        self.code.append(0x89)
        self._modrm(3, src, dst)

    def mov_reg_pile(self, dst, decalage):
        """ex [rbp+decalage] ad dst onerat"""
        self._rex(1, dst >> 3, 0, 0)
        self.code.append(0x8B)
        self._modrm(2, dst, RBP)
        self._imm32(decalage)

    def mov_pile_reg(self, decalage, src):
        """src ad [rbp+decalage] servat"""
        self._rex(1, src >> 3, 0, 0)
        self.code.append(0x89)
        self._modrm(2, src, RBP)
        self._imm32(decalage)

    def lea_reg_etiquette(self, dst, nom_etiquette):
        """dst = adressa absoluta tesserulae (duobus gradibus corrigitur)"""
        self._rex(1, dst >> 3, 0, 0)
        self.code.append(0x8D)
        self._modrm(0, dst, 5)  # mod=00, rm=101 => adressatio relativa ad RIP
        self._reserver_correctif(nom_etiquette, 4, "rip32")

    def lea_reg_pile(self, dst, decalage):
        """dst = adressa [rbp+decalage] (non eius valor)"""
        self._rex(1, dst >> 3, 0, 0)
        self.code.append(0x8D)
        self._modrm(2, dst, RBP)
        self._imm32(decalage)

    def mov_reg_indirect(self, dst, base):
        """ex [base] ad dst onerat (base non debet esse RSP/RBP)"""
        self._rex(1, dst >> 3, 0, base >> 3)
        self.code.append(0x8B)
        self._modrm(0, dst, base)

    def movzx_reg_mem8(self, dst, base):
        """unum octetum ex [base] onerat, zeris extendit, ad dst"""
        self._rex(1, dst >> 3, 0, base >> 3)
        self.code += bytes([0x0F, 0xB6])
        self._modrm(0, dst, base)

    def mov_indirect_reg(self, base, src):
        """src ad [base] servat (base non debet esse RSP/RBP)"""
        self._rex(1, src >> 3, 0, base >> 3)
        self.code.append(0x89)
        self._modrm(0, src, base)

    # --- Arithmetica ---

    def add_reg_reg(self, dst, src):
        self._rex(1, src >> 3, 0, dst >> 3)
        self.code.append(0x01)
        self._modrm(3, src, dst)

    def sub_reg_reg(self, dst, src):
        self._rex(1, src >> 3, 0, dst >> 3)
        self.code.append(0x29)
        self._modrm(3, src, dst)

    def imul_reg_reg(self, dst, src):
        self._rex(1, dst >> 3, 0, src >> 3)
        self.code += bytes([0x0F, 0xAF])
        self._modrm(3, dst, src)

    def cqo(self):
        self._rex(1, 0, 0, 0)
        self.code.append(0x99)

    def idiv_reg(self, reg):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0xF7)
        self._modrm(3, 7, reg)

    def neg_reg(self, reg):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0xF7)
        self._modrm(3, 3, reg)

    def div_reg(self, reg):
        """divisio non signata RDX:RAX / reg -> quotiens RAX, residuum RDX"""
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0xF7)
        self._modrm(3, 6, reg)

    def dec_reg(self, reg):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0xFF)
        self._modrm(3, 1, reg)

    def inc_reg(self, reg):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0xFF)
        self._modrm(3, 0, reg)

    def add_reg_imm32(self, reg, valeur):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0x81)
        self._modrm(3, 0, reg)
        self._imm32(valeur)

    def sub_reg_imm32(self, reg, valeur):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0x81)
        self._modrm(3, 5, reg)
        self._imm32(valeur)

    def mov_mem_imm8(self, base_reg, valeur):
        """octetum immediatum ad adressam [base_reg] servat"""
        self.code.append(0xC6)
        self._modrm(0, 0, base_reg)
        self.code.append(valeur & 0xFF)

    def mov_mem_reg8(self, base_reg, src_reg):
        """octetum inferius src_reg ad adressam [base_reg] servat"""
        self.code.append(0x88)
        self._modrm(0, src_reg, base_reg)

    # --- Bit ad bit ---

    def and_reg_reg(self, dst, src):
        self._rex(1, src >> 3, 0, dst >> 3)
        self.code.append(0x21)
        self._modrm(3, src, dst)

    def or_reg_reg(self, dst, src):
        self._rex(1, src >> 3, 0, dst >> 3)
        self.code.append(0x09)
        self._modrm(3, src, dst)

    def xor_reg_reg(self, dst, src):
        self._rex(1, src >> 3, 0, dst >> 3)
        self.code.append(0x31)
        self._modrm(3, src, dst)

    def not_reg(self, reg):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0xF7)
        self._modrm(3, 2, reg)

    def shl_cl(self, dst):
        self._rex(1, 0, 0, dst >> 3)
        self.code.append(0xD3)
        self._modrm(3, 4, dst)

    def shr_cl(self, dst):
        self._rex(1, 0, 0, dst >> 3)
        self.code.append(0xD3)
        self._modrm(3, 5, dst)

    # --- Comparationes ---

    def cmp_reg_reg(self, a, b):
        """indicia pro (a - b) ponit"""
        self._rex(1, b >> 3, 0, a >> 3)
        self.code.append(0x39)
        self._modrm(3, b, a)

    def cmp_reg_imm32(self, reg, valeur):
        self._rex(1, 0, 0, reg >> 3)
        self.code.append(0x81)
        self._modrm(3, 7, reg)
        self._imm32(valeur)

    _CONDITIONS = {"==": 0x94, "!=": 0x95, ">": 0x9F, ">=": 0x9D, "<": 0x9C, "<=": 0x9E}

    def setcc_al(self, condition):
        self.code += bytes([0x0F, self._CONDITIONS[condition]])
        self._modrm(3, 0, RAX)

    def movzx_rax_al(self):
        self._rex(1, 0, 0, 0)
        self.code += bytes([0x0F, 0xB6])
        self._modrm(3, RAX, RAX)

    # --- Pila et gubernatio fluxus ---

    def push_reg(self, reg):
        if reg >= 8:
            self._rex(0, 0, 0, 1)
        self.code.append(0x50 + (reg & 7))

    def pop_reg(self, reg):
        if reg >= 8:
            self._rex(0, 0, 0, 1)
        self.code.append(0x58 + (reg & 7))

    def ret(self):
        self.code.append(0xC3)

    def syscall(self):
        self.code += bytes([0x0F, 0x05])

    def call_etiquette(self, nom_etiquette):
        self.code.append(0xE8)
        self._reserver_correctif(nom_etiquette, 4, "rel32")

    def jmp_etiquette(self, nom_etiquette):
        self.code.append(0xE9)
        self._reserver_correctif(nom_etiquette, 4, "rel32")

    def je_etiquette(self, nom_etiquette):
        self.code += bytes([0x0F, 0x84])
        self._reserver_correctif(nom_etiquette, 4, "rel32")

    def jne_etiquette(self, nom_etiquette):
        self.code += bytes([0x0F, 0x85])
        self._reserver_correctif(nom_etiquette, 4, "rel32")

    def jge_etiquette(self, nom_etiquette):
        self.code += bytes([0x0F, 0x8D])
        self._reserver_correctif(nom_etiquette, 4, "rel32")

    def jle_etiquette(self, nom_etiquette):
        self.code += bytes([0x0F, 0x8E])
        self._reserver_correctif(nom_etiquette, 4, "rel32")

    # --- Resolutio finalis (secundus gradus) ---

    def resoudre(self, adresse_base):
        """Omnes tesserulas per adressas/decalagia realia substituit."""
        for position, nom, taille, mode in self.correctifs:
            cible = self.etiquettes[nom]
            if mode == "rel32":
                relatif = cible - (position + taille)
                self.code[position:position + taille] = relatif.to_bytes(4, "little", signed=True)
            elif mode == "rip32":
                adresse_instr_suivante = adresse_base + position + taille
                relatif = (adresse_base + cible) - adresse_instr_suivante
                self.code[position:position + taille] = relatif.to_bytes(4, "little", signed=True)
        return bytes(self.code)
