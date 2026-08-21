"""
Analyseur syntaxique pour VINDEX.
Transforme la liste plate de tokens en un arbre représentant
la vraie structure grammaticale du programme.
"""

from lexeur import Lexeur, TypeToken, Token


# --- Les nœuds de l'arbre (AST : Abstract Syntax Tree) ---

class Noeud:
    pass


class Programme(Noeud):
    def __init__(self, fonctions, formes):
        self.fonctions = fonctions
        self.formes = formes

    def __repr__(self):
        return f"Programme({self.fonctions}, {self.formes})"


class DefinitionForma(Noeud):
    def __init__(self, nom, champs):
        self.nom = nom
        self.champs = champs  # liste de (nom_champ, type_champ)

    def __repr__(self):
        return f"Forma({self.nom}, {self.champs})"


class AccesChamp(Noeud):
    def __init__(self, champ, structure):
        self.champ = champ
        self.structure = structure

    def __repr__(self):
        return f"AccesChamp({self.champ} DE {self.structure})"


class AffectationChamp(Noeud):
    def __init__(self, champ, structure, valeur):
        self.champ = champ
        self.structure = structure
        self.valeur = valeur

    def __repr__(self):
        return f"AffectationChamp({self.champ} DE {self.structure} = {self.valeur})"


class DeclarationSeries(Noeud):
    def __init__(self, nom, type_element, capacite):
        self.nom = nom
        self.type_element = type_element
        self.capacite = capacite

    def __repr__(self):
        return f"DeclarationSeries({self.nom}: SERIES DE {self.type_element} CAPACITAS {self.capacite})"


class AccesIndice(Noeud):
    def __init__(self, nom, indice):
        self.nom = nom
        self.indice = indice

    def __repr__(self):
        return f"AccesIndice({self.nom}[{self.indice}])"


class AffectationIndice(Noeud):
    def __init__(self, nom, indice, valeur):
        self.nom = nom
        self.indice = indice
        self.valeur = valeur

    def __repr__(self):
        return f"AffectationIndice({self.nom}[{self.indice}] = {self.valeur})"


class ReservaExpr(Noeud):
    def __init__(self, type_):
        self.type = type_

    def __repr__(self):
        return f"Reserva({self.type})"


class LiberaInstr(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"Libera({self.valeur})"


class EcritureSeries(Noeud):
    def __init__(self, nom, longueur):
        self.nom = nom
        self.longueur = longueur

    def __repr__(self):
        return f"Scribe({self.nom} CAPACITAS {self.longueur})"


class AperiExpr(Noeud):
    def __init__(self, mode, chemin):
        self.mode = mode  # "legere" ou "scribere"
        self.chemin = chemin

    def __repr__(self):
        return f"Aperi({self.mode}, {self.chemin})"


class ClaudeInstr(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"Claude({self.valeur})"


class LegeExpr(Noeud):
    def __init__(self, fd, capacite):
        self.fd = fd
        self.capacite = capacite

    def __repr__(self):
        return f"Lege({self.fd}, {self.capacite})"


class OctetusExpr(Noeud):
    def __init__(self, indice):
        self.indice = indice

    def __repr__(self):
        return f"Octetus({self.indice})"


class ScribeLectusInstr(Noeud):
    def __init__(self, longueur):
        self.longueur = longueur

    def __repr__(self):
        return f"ScribeLectus({self.longueur})"


class MitteExpr(Noeud):
    def __init__(self, fd, nom_tampon, longueur):
        self.fd = fd
        self.nom_tampon = nom_tampon
        self.longueur = longueur

    def __repr__(self):
        return f"Mitte({self.fd}, {self.nom_tampon}, {self.longueur})"


class InstructionExpr(Noeud):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"InstructionExpr({self.expr})"


class SedesExpr(Noeud):
    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return f"Sedes({self.nom})"


class ContentumExpr(Noeud):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Contentum({self.expr})"


class AffectationContentum(Noeud):
    def __init__(self, expr_pointeur, valeur):
        self.expr_pointeur = expr_pointeur
        self.valeur = valeur

    def __repr__(self):
        return f"AffectationContentum({self.expr_pointeur} = {self.valeur})"


class Parametre(Noeud):
    def __init__(self, nom, type_):
        self.nom = nom
        self.type = type_

    def __repr__(self):
        return f"Parametre({self.nom}: {self.type})"


class Fonction(Noeud):
    def __init__(self, nom, parametres, type_retour, corps):
        self.nom = nom
        self.parametres = parametres
        self.type_retour = type_retour
        self.corps = corps

    def __repr__(self):
        return f"Fonction({self.nom}, params={self.parametres}, retour={self.type_retour}, corps={self.corps})"


class Declaration(Noeud):
    def __init__(self, nom, type_, valeur):
        self.nom = nom
        self.type = type_
        self.valeur = valeur

    def __repr__(self):
        return f"Declaration({self.nom}: {self.type} = {self.valeur})"


class Affectation(Noeud):
    def __init__(self, nom, valeur):
        self.nom = nom
        self.valeur = valeur

    def __repr__(self):
        return f"Affectation({self.nom} = {self.valeur})"


class Si(Noeud):
    def __init__(self, condition, bloc_tunc, bloc_aliter):
        self.condition = condition
        self.bloc_tunc = bloc_tunc
        self.bloc_aliter = bloc_aliter  # peut être None

    def __repr__(self):
        return f"Si({self.condition}, tunc={self.bloc_tunc}, aliter={self.bloc_aliter})"


class Dum(Noeud):
    def __init__(self, condition, corps):
        self.condition = condition
        self.corps = corps

    def __repr__(self):
        return f"Dum({self.condition}, {self.corps})"


class Per(Noeud):
    def __init__(self, variable, debut, fin, corps):
        self.variable = variable
        self.debut = debut
        self.fin = fin
        self.corps = corps

    def __repr__(self):
        return f"Per({self.variable}, {self.debut}->{self.fin}, {self.corps})"


class Redde(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"Redde({self.valeur})"


class Proclama(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"Proclama({self.valeur})"


class Desine(Noeud):
    def __repr__(self):
        return "Desine()"


class Perge(Noeud):
    def __repr__(self):
        return "Perge()"


class AppelFonction(Noeud):
    def __init__(self, nom, arguments):
        self.nom = nom
        self.arguments = arguments

    def __repr__(self):
        return f"AppelFonction({self.nom}, {self.arguments})"


class OperationBinaire(Noeud):
    def __init__(self, gauche, operateur, droite):
        self.gauche = gauche
        self.operateur = operateur
        self.droite = droite

    def __repr__(self):
        return f"({self.gauche} {self.operateur} {self.droite})"


class Identifiant(Noeud):
    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return f"Id({self.nom})"


class Nombre(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"Nombre({self.valeur})"


class Chaine(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"Chaine({self.valeur!r})"


# --- Types reconnus par le langage ---
TOKENS_DE_TYPE = {
    TypeToken.TYPE_NUMERUS, TypeToken.TYPE_NUMERUS64, TypeToken.TYPE_LITTERA,
    TypeToken.TYPE_VERITAS, TypeToken.TYPE_ACUS,
    TypeToken.TYPE_SERIES, TypeToken.TYPE_VACUUM,
}

# Précédence des opérateurs binaires (plus haut = évalué en premier)
PRECEDENCE = {
    TypeToken.VEL: 1, TypeToken.VEL_BIT: 1,
    TypeToken.ET: 2, TypeToken.ET_BIT: 2,
    TypeToken.XOR_BIT: 2,
    TypeToken.EGAL_EGAL: 3, TypeToken.DIFFERENT: 3,
    TypeToken.CHEVRON_FERMANT: 4, TypeToken.CHEVRON_OUVRANT: 4,
    TypeToken.SUPERIEUR_EGAL: 4, TypeToken.INFERIEUR_EGAL: 4,
    TypeToken.DECALAGE_GAUCHE: 4, TypeToken.DECALAGE_DROITE: 4,
    TypeToken.PLUS: 5, TypeToken.MOINS: 5,
    TypeToken.FOIS: 6, TypeToken.DIVISE: 6, TypeToken.MODULO: 6,
}


class ErreurSyntaxique(Exception):
    def __init__(self, message, token):
        pos = f"L{token.ligne}:C{token.colonne}" if token else "finis archivi"
        super().__init__(f"Erratum syntacticum {pos} — {message} (acceptum: {token})")


class Analyseur:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def _actuel(self):
        return self.tokens[self.position]

    def _verifier(self, type_token):
        return self._actuel().type == type_token

    def _avancer(self):
        t = self._actuel()
        if t.type != TypeToken.FIN_FICHIER:
            self.position += 1
        return t

    def _attendre(self, type_token, message=None):
        if not self._verifier(type_token):
            raise ErreurSyntaxique(message or f"{type_token.name} exspectatur", self._actuel())
        return self._avancer()

    # --- Programme ---

    def analyser(self):
        fonctions = []
        formes = []
        while not self._verifier(TypeToken.FIN_FICHIER):
            if self._verifier(TypeToken.FORMA):
                formes.append(self._analyser_forma())
            else:
                fonctions.append(self._analyser_fonction())
        return Programme(fonctions, formes)

    def _analyser_forma(self):
        self._attendre(TypeToken.FORMA)
        nom = self._attendre(TypeToken.IDENTIFIANT).valeur
        self._attendre(TypeToken.PUNCTUM)
        champs = []
        while self._verifier(TypeToken.CAMPUS):
            self._avancer()
            nom_champ = self._attendre(TypeToken.IDENTIFIANT).valeur
            self._attendre(TypeToken.SICUT)
            type_champ = self._analyser_type()
            self._attendre(TypeToken.PUNCTUM)
            champs.append((nom_champ, type_champ))
        self._attendre(TypeToken.FIN_FORMA)
        self._attendre(TypeToken.PUNCTUM)
        return DefinitionForma(nom, champs)

    def _analyser_fonction(self):
        self._attendre(TypeToken.FUNCTIO)
        nom = self._attendre(TypeToken.IDENTIFIANT).valeur
        self._attendre(TypeToken.REDDENS)
        type_retour = self._analyser_type()
        self._attendre(TypeToken.PUNCTUM)

        parametres = []
        while self._verifier(TypeToken.ACCIPIT):
            self._avancer()
            nom_param = self._attendre(TypeToken.IDENTIFIANT).valeur
            self._attendre(TypeToken.SICUT)
            if self._verifier(TypeToken.TYPE_SERIES):
                self._avancer()
                self._attendre(TypeToken.DE)
                type_element = self._analyser_type()
                type_param = f"SERIES_REF:{type_element}"
            else:
                type_param = self._analyser_type()
            self._attendre(TypeToken.PUNCTUM)
            parametres.append(Parametre(nom_param, type_param))

        corps = self._analyser_bloc_jusqua(TypeToken.FIN_FUNCTIO)
        self._attendre(TypeToken.FIN_FUNCTIO)
        self._attendre(TypeToken.PUNCTUM)
        return Fonction(nom, parametres, type_retour, corps)

    def _analyser_type(self):
        if self._verifier(TypeToken.IDENTIFIANT):
            return self._avancer().valeur
        if self._actuel().type not in TOKENS_DE_TYPE:
            raise ErreurSyntaxique("typus exspectatur", self._actuel())
        type_ = self._avancer().valeur
        if self._verifier(TypeToken.CHEVRON_OUVRANT):
            self._avancer()
            type_interne = self._analyser_type()
            self._attendre(TypeToken.CHEVRON_FERMANT)
            type_ = f"{type_}<{type_interne}>"
        return type_

    # --- Blocs et instructions ---

    def _analyser_bloc_jusqua(self, *types_fin):
        instructions = []
        while self._actuel().type not in types_fin:
            instructions.append(self._analyser_instruction())
        return instructions

    def _analyser_instruction(self):
        t = self._actuel().type

        if t == TypeToken.DECLARA:
            return self._analyser_declaration()
        if t == TypeToken.SI:
            return self._analyser_si()
        if t == TypeToken.DUM:
            return self._analyser_dum()
        if t == TypeToken.PER:
            return self._analyser_per()
        if t == TypeToken.REDDE:
            self._avancer()
            valeur = self._analyser_expression()
            self._attendre(TypeToken.PUNCTUM)
            return Redde(valeur)
        if t == TypeToken.PROCLAMA:
            self._avancer()
            valeur = self._analyser_expression()
            self._attendre(TypeToken.PUNCTUM)
            return Proclama(valeur)
        if t == TypeToken.DESINE:
            self._avancer()
            self._attendre(TypeToken.PUNCTUM)
            return Desine()
        if t == TypeToken.PERGE:
            self._avancer()
            self._attendre(TypeToken.PUNCTUM)
            return Perge()
        if t == TypeToken.CONTENTUM:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            expr_pointeur = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            self._attendre(TypeToken.EGAL)
            valeur = self._analyser_expression()
            self._attendre(TypeToken.PUNCTUM)
            return AffectationContentum(expr_pointeur, valeur)
        if t == TypeToken.CLAUDE:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            valeur = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            self._attendre(TypeToken.PUNCTUM)
            return ClaudeInstr(valeur)
        if t == TypeToken.SCRIBE_LECTUS:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            longueur = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            self._attendre(TypeToken.PUNCTUM)
            return ScribeLectusInstr(longueur)
        if t in (TypeToken.APERI_LEGERE, TypeToken.APERI_SCRIBERE, TypeToken.LEGE,
                 TypeToken.OCTETUS, TypeToken.MITTE):
            expr = self._analyser_primaire()
            self._attendre(TypeToken.PUNCTUM)
            return InstructionExpr(expr)
        if t == TypeToken.SCRIBE:
            self._avancer()
            nom = self._attendre(TypeToken.IDENTIFIANT).valeur
            self._attendre(TypeToken.CAPACITAS)
            longueur = self._analyser_expression()
            self._attendre(TypeToken.PUNCTUM)
            return EcritureSeries(nom, longueur)
        if t == TypeToken.LIBERA:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            valeur = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            self._attendre(TypeToken.PUNCTUM)
            return LiberaInstr(valeur)
        if t == TypeToken.IDENTIFIANT:
            nom = self._avancer().valeur
            if self._verifier(TypeToken.DE):
                self._avancer()
                structure = self._analyser_primaire()
                if self._verifier(TypeToken.EGAL):
                    self._avancer()
                    valeur = self._analyser_expression()
                    self._attendre(TypeToken.PUNCTUM)
                    return AffectationChamp(nom, structure, valeur)
                return AccesChamp(nom, structure)
            if self._verifier(TypeToken.CROCHET_OUVRANT):
                self._avancer()
                indice = self._analyser_expression()
                self._attendre(TypeToken.CROCHET_FERMANT)
                self._attendre(TypeToken.EGAL)
                valeur = self._analyser_expression()
                self._attendre(TypeToken.PUNCTUM)
                return AffectationIndice(nom, indice, valeur)
            if self._verifier(TypeToken.PARENTHESE_OUVRANTE):
                self._avancer()
                arguments = []
                if not self._verifier(TypeToken.PARENTHESE_FERMANTE):
                    arguments.append(self._analyser_expression())
                    while self._verifier(TypeToken.VIRGULE):
                        self._avancer()
                        arguments.append(self._analyser_expression())
                self._attendre(TypeToken.PARENTHESE_FERMANTE)
                self._attendre(TypeToken.PUNCTUM)
                return InstructionExpr(AppelFonction(nom, arguments))
            return self._analyser_affectation_avec_nom(nom)

        raise ErreurSyntaxique("praeceptum exspectatur", self._actuel())

    def _analyser_declaration(self):
        self._attendre(TypeToken.DECLARA)
        nom = self._attendre(TypeToken.IDENTIFIANT).valeur
        self._attendre(TypeToken.SICUT)

        if self._verifier(TypeToken.TYPE_SERIES):
            self._avancer()
            self._attendre(TypeToken.DE)
            type_element = self._analyser_type()
            self._attendre(TypeToken.CAPACITAS)
            capacite = int(self._attendre(TypeToken.NOMBRE).valeur)
            self._attendre(TypeToken.PUNCTUM)
            return DeclarationSeries(nom, type_element, capacite)

        type_ = self._analyser_type()
        valeur = None
        if self._verifier(TypeToken.VALENS):
            self._avancer()
            valeur = self._analyser_expression()
        self._attendre(TypeToken.PUNCTUM)
        return Declaration(nom, type_, valeur)

    def _analyser_affectation_avec_nom(self, nom):
        self._attendre(TypeToken.EGAL)
        valeur = self._analyser_expression()
        self._attendre(TypeToken.PUNCTUM)
        return Affectation(nom, valeur)

    def _analyser_si(self):
        self._attendre(TypeToken.SI)
        condition = self._analyser_expression()
        self._attendre(TypeToken.TUNC)
        bloc_tunc = self._analyser_bloc_jusqua(TypeToken.ALITER, TypeToken.FIN_SI)
        bloc_aliter = None
        if self._verifier(TypeToken.ALITER):
            self._avancer()
            bloc_aliter = self._analyser_bloc_jusqua(TypeToken.FIN_SI)
        self._attendre(TypeToken.FIN_SI)
        self._attendre(TypeToken.PUNCTUM)
        return Si(condition, bloc_tunc, bloc_aliter)

    def _analyser_dum(self):
        self._attendre(TypeToken.DUM)
        condition = self._analyser_expression()
        self._attendre(TypeToken.PERFICE)
        corps = self._analyser_bloc_jusqua(TypeToken.FIN_DUM)
        self._attendre(TypeToken.FIN_DUM)
        self._attendre(TypeToken.PUNCTUM)
        return Dum(condition, corps)

    def _analyser_per(self):
        self._attendre(TypeToken.PER)
        variable = self._attendre(TypeToken.IDENTIFIANT).valeur
        self._attendre(TypeToken.AB)
        debut = self._analyser_expression()
        self._attendre(TypeToken.AD)
        fin = self._analyser_expression()
        self._attendre(TypeToken.PERFICE)
        corps = self._analyser_bloc_jusqua(TypeToken.FIN_PER)
        self._attendre(TypeToken.FIN_PER)
        self._attendre(TypeToken.PUNCTUM)
        return Per(variable, debut, fin, corps)

    # --- Expressions (avec gestion de la précédence des opérateurs) ---

    def _analyser_expression(self, precedence_min=0):
        gauche = self._analyser_primaire()

        while True:
            t = self._actuel().type
            precedence = PRECEDENCE.get(t)
            if precedence is None or precedence < precedence_min:
                break
            operateur = self._avancer().valeur
            droite = self._analyser_expression(precedence + 1)
            gauche = OperationBinaire(gauche, operateur, droite)

        return gauche

    def _analyser_primaire(self):
        t = self._actuel()

        if t.type == TypeToken.NOMBRE:
            self._avancer()
            return Nombre(t.valeur)
        if t.type == TypeToken.CHAINE:
            self._avancer()
            return Chaine(t.valeur)
        if t.type == TypeToken.CARACTERE:
            self._avancer()
            return Nombre(str(ord(t.valeur)))
        if t.type == TypeToken.VERUM:
            self._avancer()
            return Nombre("1")
        if t.type == TypeToken.FALSUM:
            self._avancer()
            return Nombre("0")
        if t.type == TypeToken.PARENTHESE_OUVRANTE:
            self._avancer()
            expr = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return expr
        if t.type == TypeToken.NON:
            self._avancer()
            operande = self._analyser_primaire()
            return OperationBinaire(Nombre("0"), "==", operande)
        if t.type == TypeToken.SEDES:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            nom = self._attendre(TypeToken.IDENTIFIANT).valeur
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return SedesExpr(nom)
        if t.type == TypeToken.CONTENTUM:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            expr_interne = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return ContentumExpr(expr_interne)
        if t.type == TypeToken.RESERVA:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            type_ = self._analyser_type()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return ReservaExpr(type_)
        if t.type == TypeToken.APERI_LEGERE:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            chemin = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return AperiExpr("legere", chemin)
        if t.type == TypeToken.APERI_SCRIBERE:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            chemin = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return AperiExpr("scribere", chemin)
        if t.type == TypeToken.LEGE:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            fd = self._analyser_expression()
            self._attendre(TypeToken.VIRGULE)
            capacite = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return LegeExpr(fd, capacite)
        if t.type == TypeToken.OCTETUS:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            indice = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return OctetusExpr(indice)
        if t.type == TypeToken.MITTE:
            self._avancer()
            self._attendre(TypeToken.PARENTHESE_OUVRANTE)
            fd = self._analyser_expression()
            self._attendre(TypeToken.VIRGULE)
            nom_tampon = self._attendre(TypeToken.IDENTIFIANT).valeur
            self._attendre(TypeToken.VIRGULE)
            longueur = self._analyser_expression()
            self._attendre(TypeToken.PARENTHESE_FERMANTE)
            return MitteExpr(fd, nom_tampon, longueur)
        if t.type == TypeToken.IDENTIFIANT:
            nom = self._avancer().valeur
            if self._verifier(TypeToken.DE):
                self._avancer()
                structure = self._analyser_primaire()
                return AccesChamp(nom, structure)
            if self._verifier(TypeToken.CROCHET_OUVRANT):
                self._avancer()
                indice = self._analyser_expression()
                self._attendre(TypeToken.CROCHET_FERMANT)
                return AccesIndice(nom, indice)
            if self._verifier(TypeToken.PARENTHESE_OUVRANTE):
                self._avancer()
                arguments = []
                if not self._verifier(TypeToken.PARENTHESE_FERMANTE):
                    arguments.append(self._analyser_expression())
                    while self._verifier(TypeToken.VIRGULE):
                        self._avancer()
                        arguments.append(self._analyser_expression())
                self._attendre(TypeToken.PARENTHESE_FERMANTE)
                return AppelFonction(nom, arguments)
            return Identifiant(nom)

        raise ErreurSyntaxique("expressio exspectatur", t)


if __name__ == "__main__":
    code_test = '''
FUNCTIO ADDITIO REDDENS NUMERUS.
    ACCIPIT a SICUT NUMERUS.
    ACCIPIT b SICUT NUMERUS.

    REDDE a + b.
FIN-FUNCTIO.

FUNCTIO PRINCIPALIS REDDENS NUMERUS.

    DECLARA x SICUT NUMERUS VALENS 5.
    DECLARA somme SICUT NUMERUS VALENS ADDITIO(x, 10).

    DUM x > 0 PERFICE
        PROCLAMA x.
        x = x - 1.
    FIN-DUM.

    SI somme > 10 TUNC
        PROCLAMA somme.
    ALITER
        PROCLAMA 0.
    FIN-SI.

    REDDE 0.

FIN-FUNCTIO.
'''
    tokens = Lexeur(code_test).tokeniser()
    arbre = Analyseur(tokens).analyser()
    for fonction in arbre.fonctions:
        print(fonction)
        print()
