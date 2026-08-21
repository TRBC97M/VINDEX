"""
Lexeur pour VINDEX
Découpe le code source en tokens reconnaissables.
"""

import re
from enum import Enum, auto

class TypeToken(Enum):
    # Mots-clés de structure (style COBOL)
    FUNCTIO = auto()
    FIN_FUNCTIO = auto()
    REDDENS = auto()
    DECLARA = auto()
    ACCIPIT = auto()
    SICUT = auto()
    VALENS = auto()
    SI = auto()
    TUNC = auto()
    ALITER = auto()
    FIN_SI = auto()
    DUM = auto()
    PERFICE = auto()
    FIN_DUM = auto()
    PER = auto()
    AB = auto()
    AD = auto()
    FIN_PER = auto()
    REDDE = auto()
    DESINE = auto()
    PERGE = auto()
    PROCLAMA = auto()
    SCRIBE = auto()
    PUNCTUM = auto()  # le point final "."

    # Structures et tableaux
    SERIES = auto()  # déjà présent comme type, mais aussi mot-clé structurel
    DE = auto()
    CAPACITAS = auto()
    FORMA = auto()
    FIN_FORMA = auto()
    CAMPUS = auto()
    CROCHET_OUVRANT = auto()
    CROCHET_FERMANT = auto()

    # Mémoire et constantes
    RESERVA = auto()
    LIBERA = auto()
    CONSTANS = auto()
    SEDES = auto()
    CONTENTUM = auto()

    # Fichiers
    APERI_LEGERE = auto()
    APERI_SCRIBERE = auto()
    LEGE = auto()
    OCTETUS = auto()
    SCRIBE_LECTUS = auto()
    MITTE = auto()
    CLAUDE = auto()

    # Bit à bit
    ET_BIT = auto()
    VEL_BIT = auto()
    XOR_BIT = auto()
    DECALAGE_GAUCHE = auto()
    DECALAGE_DROITE = auto()
    NON_BIT = auto()

    # Types
    TYPE_NUMERUS = auto()
    TYPE_NUMERUS64 = auto()
    TYPE_LITTERA = auto()
    TYPE_VERITAS = auto()
    TYPE_ACUS = auto()
    TYPE_SERIES = auto()
    TYPE_VACUUM = auto()

    # Littéraux
    NOMBRE = auto()
    CHAINE = auto()
    CARACTERE = auto()
    VERUM = auto()
    FALSUM = auto()
    NIHIL = auto()

    # Identifiant (nom de variable/fonction)
    IDENTIFIANT = auto()

    # Opérateurs
    PLUS = auto()
    MOINS = auto()
    FOIS = auto()
    DIVISE = auto()
    MODULO = auto()
    EGAL = auto()
    EGAL_EGAL = auto()
    DIFFERENT = auto()
    SUPERIEUR = auto()
    INFERIEUR = auto()
    SUPERIEUR_EGAL = auto()
    INFERIEUR_EGAL = auto()
    ET = auto()
    VEL = auto()
    NON = auto()

    # Symboles
    PARENTHESE_OUVRANTE = auto()
    PARENTHESE_FERMANTE = auto()
    ACCOLADE_OUVRANTE = auto()
    ACCOLADE_FERMANTE = auto()
    CHEVRON_OUVRANT = auto()
    CHEVRON_FERMANT = auto()
    DEUX_POINTS = auto()
    VIRGULE = auto()

    FIN_FICHIER = auto()


MOTS_CLES = {
    "functio": TypeToken.FUNCTIO,
    "fin-functio": TypeToken.FIN_FUNCTIO,
    "reddens": TypeToken.REDDENS,
    "declara": TypeToken.DECLARA,
    "accipit": TypeToken.ACCIPIT,
    "sicut": TypeToken.SICUT,
    "valens": TypeToken.VALENS,
    "si": TypeToken.SI,
    "tunc": TypeToken.TUNC,
    "aliter": TypeToken.ALITER,
    "fin-si": TypeToken.FIN_SI,
    "dum": TypeToken.DUM,
    "perfice": TypeToken.PERFICE,
    "fin-dum": TypeToken.FIN_DUM,
    "per": TypeToken.PER,
    "ab": TypeToken.AB,
    "ad": TypeToken.AD,
    "fin-per": TypeToken.FIN_PER,
    "redde": TypeToken.REDDE,
    "desine": TypeToken.DESINE,
    "perge": TypeToken.PERGE,
    "proclama": TypeToken.PROCLAMA,
    "scribe": TypeToken.SCRIBE,
    "de": TypeToken.DE,
    "capacitas": TypeToken.CAPACITAS,
    "forma": TypeToken.FORMA,
    "fin-forma": TypeToken.FIN_FORMA,
    "campus": TypeToken.CAMPUS,
    "reserva": TypeToken.RESERVA,
    "libera": TypeToken.LIBERA,
    "constans": TypeToken.CONSTANS,
    "sedes": TypeToken.SEDES,
    "contentum": TypeToken.CONTENTUM,
    "aperi_legere": TypeToken.APERI_LEGERE,
    "aperi_scribere": TypeToken.APERI_SCRIBERE,
    "lege": TypeToken.LEGE,
    "octetus": TypeToken.OCTETUS,
    "scribe_lectus": TypeToken.SCRIBE_LECTUS,
    "mitte": TypeToken.MITTE,
    "claude": TypeToken.CLAUDE,
    "numerus": TypeToken.TYPE_NUMERUS,
    "numerus64": TypeToken.TYPE_NUMERUS64,
    "littera": TypeToken.TYPE_LITTERA,
    "veritas": TypeToken.TYPE_VERITAS,
    "acus": TypeToken.TYPE_ACUS,
    "series": TypeToken.TYPE_SERIES,
    "vacuum": TypeToken.TYPE_VACUUM,
    "verum": TypeToken.VERUM,
    "falsum": TypeToken.FALSUM,
    "nihil": TypeToken.NIHIL,
    "et": TypeToken.ET,
    "vel": TypeToken.VEL,
    "non": TypeToken.NON,
}


class Token:
    def __init__(self, type_token, valeur, ligne, colonne):
        self.type = type_token
        self.valeur = valeur
        self.ligne = ligne
        self.colonne = colonne

    def __repr__(self):
        return f"Token({self.type.name}, {self.valeur!r}, L{self.ligne}:C{self.colonne})"


class ErreurLexicale(Exception):
    def __init__(self, message, ligne, colonne):
        super().__init__(f"Erreur lexicale L{ligne}:C{colonne} — {message}")


class Lexeur:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.ligne = 1
        self.colonne = 1
        self.tokens = []

    def _caractere_actuel(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]

    def _avancer(self):
        c = self._caractere_actuel()
        self.position += 1
        if c == "\n":
            self.ligne += 1
            self.colonne = 1
        else:
            self.colonne += 1
        return c

    def _ignorer_espaces_et_commentaires(self):
        while True:
            c = self._caractere_actuel()
            if c is None:
                return
            if c in " \t\r\n":
                self._avancer()
            elif c == "/" and self.position + 1 < len(self.source) and self.source[self.position + 1] == "/":
                # commentaire jusqu'à la fin de la ligne
                while self._caractere_actuel() not in (None, "\n"):
                    self._avancer()
            else:
                return

    def _lire_nombre(self):
        ligne, colonne = self.ligne, self.colonne
        debut = self.position
        while self._caractere_actuel() is not None and self._caractere_actuel().isdigit():
            self._avancer()
        # Un "." ne fait partie du nombre que s'il est suivi d'un chiffre
        # (partie décimale) — sinon c'est le point de fin d'instruction (style COBOL).
        if (self._caractere_actuel() == "."
                and self.position + 1 < len(self.source)
                and self.source[self.position + 1].isdigit()):
            self._avancer()
            while self._caractere_actuel() is not None and self._caractere_actuel().isdigit():
                self._avancer()
        valeur = self.source[debut:self.position]
        return Token(TypeToken.NOMBRE, valeur, ligne, colonne)

    def _lire_identifiant_ou_mot_cle(self):
        ligne, colonne = self.ligne, self.colonne
        debut = self.position
        while self._caractere_actuel() is not None and (self._caractere_actuel().isalnum() or self._caractere_actuel() == "_"):
            self._avancer()
        # Gère les mots composés type "FIN-DUM", "FIN-SI" : un tiret suivi
        # directement d'une lettre fait partie du mot-clé, pas de l'opérateur moins.
        while (self._caractere_actuel() == "-"
               and self.position + 1 < len(self.source)
               and self.source[self.position + 1].isalpha()):
            self._avancer()  # le tiret
            while self._caractere_actuel() is not None and (self._caractere_actuel().isalnum() or self._caractere_actuel() == "_"):
                self._avancer()
        valeur = self.source[debut:self.position]
        type_token = MOTS_CLES.get(valeur.lower(), TypeToken.IDENTIFIANT)
        return Token(type_token, valeur, ligne, colonne)

    def _lire_chaine(self):
        ligne, colonne = self.ligne, self.colonne
        self._avancer()  # on saute le guillemet ouvrant
        debut = self.position
        while self._caractere_actuel() is not None and self._caractere_actuel() != '"':
            self._avancer()
        if self._caractere_actuel() is None:
            raise ErreurLexicale("chaîne de caractères non terminée", ligne, colonne)
        valeur = self.source[debut:self.position]
        self._avancer()  # on saute le guillemet fermant
        return Token(TypeToken.CHAINE, valeur, ligne, colonne)

    _ECHAPPEMENTS = {"n": "\n", "t": "\t", "\\": "\\", "'": "'", '"': '"'}

    def _lire_caractere(self):
        ligne, colonne = self.ligne, self.colonne
        self._avancer()  # on saute le guillemet simple ouvrant
        c = self._caractere_actuel()
        if c is None:
            raise ErreurLexicale("caractère non terminé", ligne, colonne)
        if c == "\\":
            self._avancer()
            echappe = self._caractere_actuel()
            if echappe not in self._ECHAPPEMENTS:
                raise ErreurLexicale(f"séquence d'échappement inconnue '\\{echappe}'", ligne, colonne)
            valeur = self._ECHAPPEMENTS[echappe]
            self._avancer()
        else:
            valeur = c
            self._avancer()
        if self._caractere_actuel() != "'":
            raise ErreurLexicale("guillemet simple fermant attendu", ligne, colonne)
        self._avancer()
        return Token(TypeToken.CARACTERE, valeur, ligne, colonne)

    def tokeniser(self):
        while True:
            self._ignorer_espaces_et_commentaires()
            c = self._caractere_actuel()
            if c is None:
                self.tokens.append(Token(TypeToken.FIN_FICHIER, None, self.ligne, self.colonne))
                break

            ligne, colonne = self.ligne, self.colonne

            if c.isdigit():
                self.tokens.append(self._lire_nombre())
            elif c.isalpha() or c == "_":
                self.tokens.append(self._lire_identifiant_ou_mot_cle())
            elif c == '"':
                self.tokens.append(self._lire_chaine())
            elif c == "'":
                self.tokens.append(self._lire_caractere())
            elif c == "+":
                self._avancer(); self.tokens.append(Token(TypeToken.PLUS, "+", ligne, colonne))
            elif c == "-":
                self._avancer(); self.tokens.append(Token(TypeToken.MOINS, "-", ligne, colonne))
            elif c == "*":
                self._avancer(); self.tokens.append(Token(TypeToken.FOIS, "*", ligne, colonne))
            elif c == "/":
                self._avancer(); self.tokens.append(Token(TypeToken.DIVISE, "/", ligne, colonne))
            elif c == "%":
                self._avancer(); self.tokens.append(Token(TypeToken.MODULO, "%", ligne, colonne))
            elif c == "(":
                self._avancer(); self.tokens.append(Token(TypeToken.PARENTHESE_OUVRANTE, "(", ligne, colonne))
            elif c == ")":
                self._avancer(); self.tokens.append(Token(TypeToken.PARENTHESE_FERMANTE, ")", ligne, colonne))
            elif c == "{":
                self._avancer(); self.tokens.append(Token(TypeToken.ACCOLADE_OUVRANTE, "{", ligne, colonne))
            elif c == "}":
                self._avancer(); self.tokens.append(Token(TypeToken.ACCOLADE_FERMANTE, "}", ligne, colonne))
            elif c == "[":
                self._avancer(); self.tokens.append(Token(TypeToken.CROCHET_OUVRANT, "[", ligne, colonne))
            elif c == "]":
                self._avancer(); self.tokens.append(Token(TypeToken.CROCHET_FERMANT, "]", ligne, colonne))
            elif c == "^":
                self._avancer(); self.tokens.append(Token(TypeToken.XOR_BIT, "^", ligne, colonne))
            elif c == "~":
                self._avancer(); self.tokens.append(Token(TypeToken.NON_BIT, "~", ligne, colonne))
            elif c == ":":
                self._avancer(); self.tokens.append(Token(TypeToken.DEUX_POINTS, ":", ligne, colonne))
            elif c == ",":
                self._avancer(); self.tokens.append(Token(TypeToken.VIRGULE, ",", ligne, colonne))
            elif c == ".":
                self._avancer(); self.tokens.append(Token(TypeToken.PUNCTUM, ".", ligne, colonne))
            elif c == "&":
                self._avancer()
                if self._caractere_actuel() == "&":
                    self._avancer(); self.tokens.append(Token(TypeToken.ET, "&&", ligne, colonne))
                else:
                    self.tokens.append(Token(TypeToken.ET_BIT, "&", ligne, colonne))
            elif c == "|":
                self._avancer()
                if self._caractere_actuel() == "|":
                    self._avancer(); self.tokens.append(Token(TypeToken.VEL, "||", ligne, colonne))
                else:
                    self.tokens.append(Token(TypeToken.VEL_BIT, "|", ligne, colonne))
            elif c == "<":
                self._avancer()
                if self._caractere_actuel() == "=":
                    self._avancer(); self.tokens.append(Token(TypeToken.INFERIEUR_EGAL, "<=", ligne, colonne))
                elif self._caractere_actuel() == "<":
                    self._avancer(); self.tokens.append(Token(TypeToken.DECALAGE_GAUCHE, "<<", ligne, colonne))
                else:
                    self.tokens.append(Token(TypeToken.CHEVRON_OUVRANT, "<", ligne, colonne))
            elif c == ">":
                self._avancer()
                if self._caractere_actuel() == "=":
                    self._avancer(); self.tokens.append(Token(TypeToken.SUPERIEUR_EGAL, ">=", ligne, colonne))
                elif self._caractere_actuel() == ">":
                    self._avancer(); self.tokens.append(Token(TypeToken.DECALAGE_DROITE, ">>", ligne, colonne))
                else:
                    self.tokens.append(Token(TypeToken.CHEVRON_FERMANT, ">", ligne, colonne))
            elif c == "=":
                self._avancer()
                if self._caractere_actuel() == "=":
                    self._avancer(); self.tokens.append(Token(TypeToken.EGAL_EGAL, "==", ligne, colonne))
                else:
                    self.tokens.append(Token(TypeToken.EGAL, "=", ligne, colonne))
            elif c == "!":
                self._avancer()
                if self._caractere_actuel() == "=":
                    self._avancer(); self.tokens.append(Token(TypeToken.DIFFERENT, "!=", ligne, colonne))
                else:
                    self.tokens.append(Token(TypeToken.NON, "!", ligne, colonne))
            else:
                raise ErreurLexicale(f"caractère inattendu '{c}'", ligne, colonne)

        return self.tokens


if __name__ == "__main__":
    code_test = '''
FUNCTIO PRINCIPALIS REDDENS NUMERUS.

    DECLARA x SICUT NUMERUS VALENS 5.

    DUM x > 0 PERFICE
        PROCLAMA x.
        x = x - 1.
    FIN-DUM.

    REDDE 0.

FIN-FUNCTIO.
'''
    lexeur = Lexeur(code_test)
    tokens = lexeur.tokeniser()
    for t in tokens:
        print(t)
