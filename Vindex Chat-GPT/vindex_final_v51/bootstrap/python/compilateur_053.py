"""Amorsa Python VINDEX 0.53 cum primitivis memoriae dynamicis."""

import os
import sys

from analyseur import AccesIndice, Analyseur, AppelFonction
from assembleur import RAX, RBX, RCX, RDI, RSI, RDX, R8, R9, R10
from generateur import ErreurGeneration, Generateur as GenerateurPrior
from lexeur import Lexeur


class Generateur053(GenerateurPrior):
    """Generator prior servatur; primitivae necessariae VINDEX 0.53 adduntur."""

    def _gen_adresse_indice(self, nom, expr_indice):
        """ACUS<LITTERA> per octeta, cetera receptacula per verba VIII octetorum indicat."""
        self._gen_expr(expr_indice)
        self.asm.push_reg(RAX)
        self._gen_adresse_base_tableau(nom, RBX)
        self.asm.pop_reg(RAX)

        genus = self.types_variables.get(nom, "")
        if genus != "ACUS<LITTERA>":
            self.asm.mov_reg_imm64(RCX, 8)
            self.asm.imul_reg_reg(RAX, RCX)

        if self._est_pointeur(nom):
            self.asm.add_reg_reg(RBX, RAX)
        else:
            self.asm.sub_reg_reg(RBX, RAX)

    def _gen_expr(self, expr):
        if isinstance(expr, AccesIndice) and self.types_variables.get(expr.nom, "") == "ACUS<LITTERA>":
            self._gen_adresse_indice(expr.nom, expr.indice)
            self.asm.movzx_reg_mem8(RAX, RBX)
            return

        if isinstance(expr, AppelFonction) and expr.nom == "RESERVA_OCTETA":
            if len(expr.arguments) != 1:
                raise ErreurGeneration("RESERVA_OCTETA unum argumentum exspectat")

            # Linux x86-64: mmap(NULL, mensura, PROT_READ|PROT_WRITE,
            # MAP_PRIVATE|MAP_ANONYMOUS, 0, 0).
            self._gen_expr(expr.arguments[0])
            self.asm.mov_reg_reg(RSI, RAX)
            self.asm.mov_reg_imm64(RDI, 0)
            self.asm.mov_reg_imm64(RDX, 3)
            self.asm.mov_reg_imm64(R10, 34)
            self.asm.mov_reg_imm64(R8, 0)
            self.asm.mov_reg_imm64(R9, 0)
            self.asm.mov_reg_imm64(RAX, 9)
            self.asm.syscall()
            return

        if isinstance(expr, AppelFonction) and expr.nom == "OCTETUS_AB":
            if len(expr.arguments) != 1:
                raise ErreurGeneration("OCTETUS_AB unum argumentum exspectat")
            self._gen_expr(expr.arguments[0])
            self.asm.mov_reg_reg(RBX, RAX)
            self.asm.movzx_reg_mem8(RAX, RBX)
            return

        return super()._gen_expr(expr)


def compila(codex_fontis: str, via_exitus: str):
    signa = Lexeur(codex_fontis).tokeniser()
    arbor = Analyseur(signa).analyser()
    binarium = Generateur053().generer(arbor)
    with open(via_exitus, "wb") as fasciculus:
        fasciculus.write(binarium)
    os.chmod(via_exitus, 0o755)


if __name__ == "__main__":
    via_fontis = sys.argv[1]
    via_exitus = sys.argv[2] if len(sys.argv) > 2 else "a.out"
    with open(via_fontis, encoding="utf-8") as fasciculus:
        compila(fasciculus.read(), via_exitus)
    print(f"Compilatum: {via_exitus}")
