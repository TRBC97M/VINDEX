import sys
from lexeur import Lexeur
from analyseur import Analyseur
from generateur import Generateur


def compiler(code_source: str, chemin_sortie: str):
    tokens = Lexeur(code_source).tokeniser()
    arbre = Analyseur(tokens).analyser()
    binaire = Generateur().generer(arbre)
    with open(chemin_sortie, "wb") as f:
        f.write(binaire)
    import os
    os.chmod(chemin_sortie, 0o755)


if __name__ == "__main__":
    chemin_source = sys.argv[1]
    chemin_sortie = sys.argv[2] if len(sys.argv) > 2 else "a.out"
    with open(chemin_source, encoding="utf-8") as f:
        compiler(f.read(), chemin_sortie)
    print(f"Compilatum: {chemin_sortie}")
