#!/usr/bin/env python3
"""VINDEX 0.53: amorsam Python ad septem argumenta System V extendit."""

from pathlib import Path


VIA = Path("Vindex Chat-GPT/vindex_final_v51/bootstrap/python/generateur.py")

VETUS_PARAMETRA = '''        # Copie des arguments (reçus dans les registres) vers leurs emplacements sur la pile
        for i, param in enumerate(fonction.parametres):
            self.asm.mov_pile_reg(self.variables[param.nom], REGISTRES_ARGUMENTS[i])
'''

NOVA_PARAMETRA = '''        # Argumenta I-VI in registris System V veniunt; septimum in pila ad RBP+16.
        if len(fonction.parametres) > 7:
            raise ErreurGeneration("plus quam septem argumenta nondum sustentantur")
        for i, param in enumerate(fonction.parametres):
            if i < 6:
                self.asm.mov_pile_reg(self.variables[param.nom], REGISTRES_ARGUMENTS[i])
            else:
                self.asm.mov_reg_pile(R10, 16)
                self.asm.mov_pile_reg(self.variables[param.nom], R10)
'''

VETUS_APPELLATIO = '''            for arg in expr.arguments:
                if isinstance(arg, Identifiant) and self._est_tableau(arg.nom):
                    self._gen_adresse_base_tableau(arg.nom, RAX)
                else:
                    self._gen_expr(arg)
                self.asm.push_reg(RAX)
            for i in reversed(range(len(expr.arguments))):
                self.asm.pop_reg(REGISTRES_ARGUMENTS[i])
            self.asm.call_etiquette(f"fn_{expr.nom}")
'''

NOVA_APPELLATIO = '''            numerus_argumentorum = len(expr.arguments)
            if numerus_argumentorum > 7:
                raise ErreurGeneration("plus quam septem argumenta nondum sustentantur")
            for arg in expr.arguments:
                if isinstance(arg, Identifiant) and self._est_tableau(arg.nom):
                    self._gen_adresse_base_tableau(arg.nom, RAX)
                else:
                    self._gen_expr(arg)
                self.asm.push_reg(RAX)
            if numerus_argumentorum == 7:
                self.asm.pop_reg(R10)
            for i in reversed(range(min(numerus_argumentorum, 6))):
                self.asm.pop_reg(REGISTRES_ARGUMENTS[i])
            if numerus_argumentorum == 7:
                self.asm.mov_reg_imm64(R11, 0)
                self.asm.push_reg(R11)
                self.asm.push_reg(R10)
            self.asm.call_etiquette(f"fn_{expr.nom}")
            if numerus_argumentorum == 7:
                self.asm.pop_reg(R10)
                self.asm.pop_reg(R11)
'''


def muta_unum(textus: str, vetus: str, novum: str, nomen: str) -> tuple[str, bool]:
    nv = textus.count(vetus)
    nn = textus.count(novum)
    if nv == 1 and nn == 0:
        return textus.replace(vetus, novum, 1), True
    if nv == 0 and nn == 1:
        return textus, False
    raise SystemExit(f"ERRATUM: mutatio {nomen} ambigua est (vetus={nv}, nova={nn})")


def principale() -> None:
    textus = VIA.read_text(encoding="utf-8")
    mutatum = False
    textus, m = muta_unum(textus, VETUS_PARAMETRA, NOVA_PARAMETRA, "parametra")
    mutatum = mutatum or m
    textus, m = muta_unum(textus, VETUS_APPELLATIO, NOVA_APPELLATIO, "appellatio")
    mutatum = mutatum or m

    VIA.write_text(textus, encoding="utf-8", newline="\n")
    if mutatum:
        print("RECTE: amorsa Python septem argumenta secundum ABI System V sustinet.")
    else:
        print("RECTE: amorsa Python iam septem argumenta sustinet.")


if __name__ == "__main__":
    principale()
