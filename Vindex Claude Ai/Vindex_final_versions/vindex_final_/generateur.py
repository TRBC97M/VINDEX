"""
Générateur de code : parcourt l'arbre produit par l'analyseur syntaxique
et pilote l'assembleur pour produire le code machine x86-64 final.
"""

from assembleur import Assembleur, RAX, RBX, RCX, RDX, RSP, RBP, RSI, RDI, R8, R9, R10, R11
from analyseur import (
    Programme, Fonction, Declaration, Affectation, Si, Dum, Per, Redde,
    Proclama, Desine, Perge, AppelFonction, OperationBinaire, Identifiant,
    Nombre, Chaine, DefinitionForma, AccesChamp, AffectationChamp,
    DeclarationSeries, AccesIndice, AffectationIndice, ReservaExpr, LiberaInstr,
    EcritureSeries, AperiExpr, ClaudeInstr, LegeExpr, OctetusExpr,
    ScribeLectusInstr, MitteExpr, InstructionExpr, SedesExpr, ContentumExpr,
    AffectationContentum,
)
import elf

REGISTRES_ARGUMENTS = [RDI, RSI, RDX, RCX, R8, R9]
TAILLE_PILE_LOCALE = 512  # espace réservé par fonction (généreux, simple pour l'instant)
TAILLE_TAS = 65536  # zone mémoire statique utilisée par RESERVA (allocateur "bump" simple)
TAILLE_TAMPON_ECRITURE = 1024  # zone utilisée par SCRIBE pour assembler le texte avant affichage
TAILLE_TAMPON_LECTURE = 2000000   # zone utilisée par LEGE pour recevoir le contenu d'un fichier


class ErreurGeneration(Exception):
    pass


class Generateur:
    def __init__(self):
        self.asm = Assembleur()
        self.compteur_etiquettes = 0
        self.variables = {}
        self.etiquette_retour = None
        self.pile_boucles = []
        self.chaines_statiques = []
        self.chaines_c = []

    def _nouvelle_etiquette(self, base):
        self.compteur_etiquettes += 1
        return f"{base}_{self.compteur_etiquettes}"

    # --- Point d'entrée principal ---

    def generer(self, programme: Programme) -> bytes:
        self.formas = {}
        for forma in programme.formes:
            self.formas[forma.nom] = {
                nom_champ: i for i, (nom_champ, _type) in enumerate(forma.champs)
            }

        for fonction in programme.fonctions:
            self._gen_fonction(fonction)

        self._gen_routine_conversion()
        self._gen_routine_ecriture_serie()
        self._gen_routine_mitte_serie()

        self.asm.etiquette("_debut")
        self.asm.call_etiquette("fn_PRINCIPALIS")
        self.asm.mov_reg_reg(RDI, RAX)
        self.asm.mov_reg_imm64(RAX, 60)  # syscall exit
        self.asm.syscall()

        for nom_etiquette, texte in self.chaines_statiques:
            self.asm.etiquette(nom_etiquette)
            self.asm.code += texte.encode("utf-8") + b"\n"

        for nom_etiquette, texte in self.chaines_c:
            self.asm.etiquette(nom_etiquette)
            self.asm.code += texte.encode("utf-8") + b"\x00"

        self.asm.etiquette("tampon_conversion")
        self.asm.code += bytes(31)
        self.asm.etiquette("tampon_fin")
        self.asm.code += b"\n"
        self.asm.etiquette("tampon_apres")

        self.asm.etiquette("tas_curseur")
        self.asm.code += bytes(8)
        self.asm.etiquette("tas_libre_tete")
        self.asm.code += bytes(8)
        self.asm.etiquette("tas_donnees")
        self.asm.code += bytes(TAILLE_TAS)

        self.asm.etiquette("tampon_ecriture")
        self.asm.code += bytes(TAILLE_TAMPON_ECRITURE)

        self.asm.etiquette("tampon_lecture")
        self.asm.code += bytes(TAILLE_TAMPON_LECTURE)

        decalage_entree = self.asm.etiquettes["_debut"]
        code_final = self.asm.resoudre(elf.BASE_ADDR + elf.DECALAGE_CODE)
        return elf.construire_elf(code_final, decalage_entree)

    # --- Fonctions ---

    def _collecter_declarations(self, instructions):
        """Retourne une liste de (nom, type_ou_None) pour chaque variable déclarée."""
        noms = []
        for instr in instructions:
            if isinstance(instr, Declaration):
                noms.append((instr.nom, instr.type))
            elif isinstance(instr, DeclarationSeries):
                noms.append((instr.nom, f"SERIES:{instr.capacite}"))
            elif isinstance(instr, Si):
                noms += self._collecter_declarations(instr.bloc_tunc)
                if instr.bloc_aliter:
                    noms += self._collecter_declarations(instr.bloc_aliter)
            elif isinstance(instr, Dum):
                noms += self._collecter_declarations(instr.corps)
            elif isinstance(instr, Per):
                noms.append((instr.variable, "NUMERUS"))
                noms += self._collecter_declarations(instr.corps)
        return noms

    def _gen_fonction(self, fonction: Fonction):
        self.asm.etiquette(f"fn_{fonction.nom}")
        self.asm.push_reg(RBP)
        self.asm.mov_reg_reg(RBP, RSP)

        # Table des variables locales. Une variable normale occupe 8 octets ;
        # une variable de type structure occupe (nb_champs * 8) octets,
        # et son "offset" pointe vers son champ d'indice 0.
        self.variables = {}
        self.types_variables = {}
        decalage = -8
        for param in fonction.parametres:
            self.variables[param.nom] = decalage
            self.types_variables[param.nom] = param.type
            decalage -= 8
        for nom, type_ in self._collecter_declarations(fonction.corps):
            if nom in self.variables:
                continue
            self.variables[nom] = decalage
            self.types_variables[nom] = type_
            if type_ in self.formas:
                decalage -= 8 * len(self.formas[type_])
            elif isinstance(type_, str) and type_.startswith("SERIES:"):
                capacite = int(type_.split(":")[1])
                decalage -= 8 * capacite
            else:
                decalage -= 8

        # La pile doit être assez grande pour TOUTES les variables déclarées
        # (calculée dynamiquement, pas une taille fixe qui pourrait déborder).
        taille_necessaire = -decalage
        taille_reservee = ((taille_necessaire + 16 + 15) // 16) * 16  # marge + alignement 16 octets
        self.asm.sub_reg_imm32(RSP, taille_reservee)

        # Copie des arguments (reçus dans les registres) vers leurs emplacements sur la pile
        for i, param in enumerate(fonction.parametres):
            self.asm.mov_pile_reg(self.variables[param.nom], REGISTRES_ARGUMENTS[i])

        self.etiquette_retour = self._nouvelle_etiquette(f"fin_{fonction.nom}")
        self.pile_boucles = []

        self._gen_bloc(fonction.corps)

        self.asm.etiquette(self.etiquette_retour)
        self.asm.mov_reg_reg(RSP, RBP)
        self.asm.pop_reg(RBP)
        self.asm.ret()

    # --- Instructions ---

    def _gen_bloc(self, instructions):
        for instr in instructions:
            self._gen_instruction(instr)

    def _gen_instruction(self, instr):
        if isinstance(instr, Declaration):
            if instr.type in self.formas:
                for i in range(len(self.formas[instr.type])):
                    self.asm.mov_reg_imm64(RAX, 0)
                    self.asm.mov_pile_reg(self.variables[instr.nom] - 8 * i, RAX)
            else:
                if instr.valeur is not None:
                    self._gen_expr(instr.valeur)
                else:
                    self.asm.mov_reg_imm64(RAX, 0)
                self.asm.mov_pile_reg(self.variables[instr.nom], RAX)

        elif isinstance(instr, DeclarationSeries):
            for i in range(instr.capacite):
                self.asm.mov_reg_imm64(RAX, 0)
                self.asm.mov_pile_reg(self.variables[instr.nom] - 8 * i, RAX)

        elif isinstance(instr, AffectationIndice):
            self._gen_expr(instr.valeur)                        # valeur -> RAX
            self.asm.push_reg(RAX)
            self._gen_adresse_indice(instr.nom, instr.indice)   # adresse -> RBX (écrase RAX/RCX, sans souci)
            self.asm.pop_reg(RAX)
            self.asm.mov_indirect_reg(RBX, RAX)

        elif isinstance(instr, LiberaInstr):
            self._gen_expr(instr.valeur)             # RAX = pointeur (charge utile) à libérer
            self.asm.mov_reg_reg(RCX, RAX)             # RCX = ce pointeur
            self.asm.lea_reg_etiquette(RBX, "tas_libre_tete")
            self.asm.mov_reg_indirect(RDX, RBX)        # RDX = tête actuelle de la liste libre
            self.asm.mov_indirect_reg(RCX, RDX)        # on stocke l'ancienne tête DANS le bloc qu'on libère
            self.asm.mov_reg_imm64(RDX, 8)
            self.asm.sub_reg_reg(RCX, RDX)             # RCX = adresse de l'en-tête (charge utile - 8)
            self.asm.mov_indirect_reg(RBX, RCX)        # tas_libre_tete pointe maintenant sur ce bloc

        elif isinstance(instr, EcritureSeries):
            self._gen_expr(instr.longueur)
            self.asm.mov_reg_reg(RCX, RAX)
            self._gen_adresse_base_tableau(instr.nom, RSI)
            self.asm.call_etiquette("routine_ecriture_serie")

        elif isinstance(instr, ClaudeInstr):
            self._gen_expr(instr.valeur)
            self.asm.mov_reg_reg(RDI, RAX)
            self.asm.mov_reg_imm64(RAX, 3)  # syscall close
            self.asm.syscall()

        elif isinstance(instr, ScribeLectusInstr):
            self._gen_expr(instr.longueur)
            self.asm.mov_reg_reg(RDX, RAX)
            self.asm.lea_reg_etiquette(RSI, "tampon_lecture")
            self.asm.mov_reg_imm64(RAX, 1)  # syscall write
            self.asm.mov_reg_imm64(RDI, 1)  # stdout
            self.asm.syscall()

        elif isinstance(instr, InstructionExpr):
            self._gen_expr(instr.expr)  # évalué pour ses effets ; résultat ignoré

        elif isinstance(instr, AffectationContentum):
            self._gen_expr(instr.valeur)
            self.asm.push_reg(RAX)
            self._gen_expr(instr.expr_pointeur)   # RAX = adresse cible
            self.asm.mov_reg_reg(RBX, RAX)
            self.asm.pop_reg(RAX)
            self.asm.mov_indirect_reg(RBX, RAX)

        elif isinstance(instr, AffectationChamp):
            decalage = self._decalage_champ(instr.champ, instr.structure)
            self._gen_expr(instr.valeur)
            self.asm.mov_pile_reg(decalage, RAX)

        elif isinstance(instr, Affectation):
            self._gen_expr(instr.valeur)
            self.asm.mov_pile_reg(self.variables[instr.nom], RAX)

        elif isinstance(instr, Redde):
            self._gen_expr(instr.valeur)
            self.asm.jmp_etiquette(self.etiquette_retour)

        elif isinstance(instr, Proclama):
            self._gen_proclama(instr.valeur)

        elif isinstance(instr, Si):
            self._gen_si(instr)

        elif isinstance(instr, Dum):
            self._gen_dum(instr)

        elif isinstance(instr, Per):
            self._gen_per(instr)

        elif isinstance(instr, Desine):
            if not self.pile_boucles:
                raise ErreurGeneration("DESINE en dehors d'une boucle")
            self.asm.jmp_etiquette(self.pile_boucles[-1][1])

        elif isinstance(instr, Perge):
            if not self.pile_boucles:
                raise ErreurGeneration("PERGE en dehors d'une boucle")
            self.asm.jmp_etiquette(self.pile_boucles[-1][0])

        else:
            raise ErreurGeneration(f"instruction non gérée : {instr}")

    def _gen_si(self, instr: Si):
        etq_aliter = self._nouvelle_etiquette("aliter")
        etq_fin = self._nouvelle_etiquette("fin_si")

        self._gen_expr(instr.condition)
        self.asm.cmp_reg_imm32(RAX, 0)
        self.asm.je_etiquette(etq_aliter if instr.bloc_aliter else etq_fin)

        self._gen_bloc(instr.bloc_tunc)

        if instr.bloc_aliter:
            self.asm.jmp_etiquette(etq_fin)
            self.asm.etiquette(etq_aliter)
            self._gen_bloc(instr.bloc_aliter)

        self.asm.etiquette(etq_fin)

    def _gen_dum(self, instr: Dum):
        etq_debut = self._nouvelle_etiquette("dum")
        etq_fin = self._nouvelle_etiquette("fin_dum")

        self.pile_boucles.append((etq_debut, etq_fin))
        self.asm.etiquette(etq_debut)
        self._gen_expr(instr.condition)
        self.asm.cmp_reg_imm32(RAX, 0)
        self.asm.je_etiquette(etq_fin)
        self._gen_bloc(instr.corps)
        self.asm.jmp_etiquette(etq_debut)
        self.asm.etiquette(etq_fin)
        self.pile_boucles.pop()

    def _gen_per(self, instr: Per):
        etq_debut = self._nouvelle_etiquette("per")
        etq_fin = self._nouvelle_etiquette("fin_per")

        self._gen_expr(instr.debut)
        self.asm.mov_pile_reg(self.variables[instr.variable], RAX)

        self.pile_boucles.append((etq_debut, etq_fin))
        self.asm.etiquette(etq_debut)
        self.asm.mov_reg_pile(RAX, self.variables[instr.variable])
        self._gen_expr(instr.fin)
        self.asm.mov_reg_reg(RBX, RAX)
        self.asm.mov_reg_pile(RAX, self.variables[instr.variable])
        self.asm.cmp_reg_reg(RAX, RBX)
        self.asm.setcc_al("<=")
        self.asm.movzx_rax_al()
        self.asm.cmp_reg_imm32(RAX, 0)
        self.asm.je_etiquette(etq_fin)

        self._gen_bloc(instr.corps)

        self.asm.mov_reg_pile(RAX, self.variables[instr.variable])
        self.asm.mov_reg_imm64(RBX, 1)
        self.asm.add_reg_reg(RAX, RBX)
        self.asm.mov_pile_reg(self.variables[instr.variable], RAX)
        self.asm.jmp_etiquette(etq_debut)
        self.asm.etiquette(etq_fin)
        self.pile_boucles.pop()

    def _gen_proclama(self, expr):
        if isinstance(expr, Chaine):
            etq = self._nouvelle_etiquette("chaine")
            self.chaines_statiques.append((etq, expr.valeur))
            self.asm.lea_reg_etiquette(RSI, etq)
            self.asm.mov_reg_imm64(RDX, len(expr.valeur.encode("utf-8")) + 1)
        else:
            self._gen_expr(expr)
            self.asm.call_etiquette("routine_conversion")
        self.asm.mov_reg_imm64(RAX, 1)   # syscall write
        self.asm.mov_reg_imm64(RDI, 1)   # stdout
        self.asm.syscall()

    # --- Expressions ---

    OPS_COMPARAISON = {"==", "!=", ">", ">=", "<", "<="}

    def _est_tableau(self, nom):
        type_ = self.types_variables.get(nom, "")
        return isinstance(type_, str) and (type_.startswith("SERIES:") or type_.startswith("SERIES_REF"))

    def _gen_adresse_base_tableau(self, nom, registre_dest):
        """Place dans registre_dest l'adresse de l'élément 0 du tableau `nom`
        (qu'il soit stocké localement, ou reçu en paramètre par référence)."""
        if self.types_variables.get(nom, "").startswith("SERIES_REF"):
            self.asm.mov_reg_pile(registre_dest, self.variables[nom])
        else:
            self.asm.lea_reg_pile(registre_dest, self.variables[nom])

    def _decalage_champ(self, nom_champ, expr_structure):
        if not isinstance(expr_structure, Identifiant):
            raise ErreurGeneration("l'accès de champ ne gère pour l'instant qu'une variable locale directe")
        nom_var = expr_structure.nom
        type_var = self.types_variables.get(nom_var)
        if type_var not in self.formas:
            raise ErreurGeneration(f"{nom_var} n'est pas une structure connue")
        index_champ = self.formas[type_var][nom_champ]
        return self.variables[nom_var] - 8 * index_champ

    def _gen_adresse_indice(self, nom, expr_indice):
        """Calcule l'adresse de nom[indice] et la laisse dans RBX."""
        self._gen_expr(expr_indice)
        self.asm.push_reg(RAX)
        self._gen_adresse_base_tableau(nom, RBX)
        self.asm.pop_reg(RAX)
        self.asm.mov_reg_imm64(RCX, 8)
        self.asm.imul_reg_reg(RAX, RCX)
        self.asm.sub_reg_reg(RBX, RAX)

    def _gen_expr(self, expr):
        if isinstance(expr, Nombre):
            # Attention : ne jamais passer par float() ici — un float64 ne peut
            # représenter exactement que ~15-17 chiffres, ce qui corromprait
            # silencieusement les grands entiers (ex : des empreintes de hachage).
            valeur_texte = expr.valeur
            if "." in valeur_texte:
                self.asm.mov_reg_imm64(RAX, int(float(valeur_texte)))
            else:
                self.asm.mov_reg_imm64(RAX, int(valeur_texte))

        elif isinstance(expr, AccesIndice):
            self._gen_adresse_indice(expr.nom, expr.indice)
            self.asm.mov_reg_indirect(RAX, RBX)

        elif isinstance(expr, ReservaExpr):
            etq_vide = self._nouvelle_etiquette("reserva_vide")
            etq_fin = self._nouvelle_etiquette("reserva_fin")

            self.asm.lea_reg_etiquette(RBX, "tas_libre_tete")
            self.asm.mov_reg_indirect(RAX, RBX)   # RAX = tête de la liste des blocs libres
            self.asm.cmp_reg_imm32(RAX, 0)
            self.asm.je_etiquette(etq_vide)

            # Un bloc libre existe : on le retire de la liste et on le réutilise.
            self.asm.mov_reg_reg(RCX, RAX)            # RCX = adresse de l'en-tête du bloc
            self.asm.mov_reg_imm64(RDX, 8)
            self.asm.add_reg_reg(RCX, RDX)            # RCX = adresse de la charge utile
            self.asm.mov_reg_indirect(RDX, RCX)       # RDX = prochain bloc libre (stocké dans la charge utile)
            self.asm.mov_indirect_reg(RBX, RDX)       # tas_libre_tete = RDX
            self.asm.mov_reg_reg(RAX, RCX)             # résultat = adresse de la charge utile
            self.asm.jmp_etiquette(etq_fin)

            # Aucun bloc libre : on avance le curseur du tas, avec un nouvel en-tête.
            self.asm.etiquette(etq_vide)
            self.asm.lea_reg_etiquette(RCX, "tas_curseur")
            self.asm.mov_reg_indirect(R8, RCX)         # R8 = décalage actuel
            self.asm.lea_reg_etiquette(R9, "tas_donnees")
            self.asm.add_reg_reg(R9, R8)               # R9 = adresse de l'en-tête
            self.asm.mov_reg_imm64(RAX, 8)
            self.asm.mov_indirect_reg(R9, RAX)         # en-tête = taille du bloc (8 pour l'instant)
            self.asm.mov_reg_imm64(RDX, 16)
            self.asm.add_reg_reg(R8, RDX)              # nouveau décalage = ancien + en-tête + charge utile
            self.asm.mov_indirect_reg(RCX, R8)         # tas_curseur mis à jour
            self.asm.mov_reg_reg(RAX, R9)
            self.asm.mov_reg_imm64(RDX, 8)
            self.asm.add_reg_reg(RAX, RDX)             # résultat = en-tête + 8 = charge utile

            self.asm.etiquette(etq_fin)

        elif isinstance(expr, AccesChamp):
            decalage = self._decalage_champ(expr.champ, expr.structure)
            self.asm.mov_reg_pile(RAX, decalage)

        elif isinstance(expr, SedesExpr):
            self.asm.lea_reg_pile(RAX, self.variables[expr.nom])

        elif isinstance(expr, ContentumExpr):
            self._gen_expr(expr.expr)
            self.asm.mov_reg_indirect(RAX, RAX)

        elif isinstance(expr, AperiExpr):
            if not isinstance(expr.chemin, Chaine):
                raise ErreurGeneration("APERI_LEGERE/APERI_SCRIBERE nécessitent un chemin littéral pour l'instant")
            etq = self._nouvelle_etiquette("chemin")
            self.chaines_c.append((etq, expr.chemin.valeur))
            self.asm.lea_reg_etiquette(RDI, etq)
            if expr.mode == "legere":
                self.asm.mov_reg_imm64(RSI, 0)          # O_RDONLY
                self.asm.mov_reg_imm64(RDX, 0)
            else:
                self.asm.mov_reg_imm64(RSI, 0x241)      # O_WRONLY | O_CREAT | O_TRUNC
                self.asm.mov_reg_imm64(RDX, 420)        # 0644
            self.asm.mov_reg_imm64(RAX, 2)              # syscall open
            self.asm.syscall()

        elif isinstance(expr, LegeExpr):
            self._gen_expr(expr.fd)
            self.asm.push_reg(RAX)
            self._gen_expr(expr.capacite)
            self.asm.mov_reg_reg(RDX, RAX)
            # Sécurité : quelle que soit la capacité demandée par le programme,
            # on ne dépasse jamais la taille réelle du tampon réservé en mémoire.
            self.asm.cmp_reg_imm32(RDX, TAILLE_TAMPON_LECTURE)
            etq_ok = self._nouvelle_etiquette("lege_capacite_ok")
            self.asm.jle_etiquette(etq_ok)
            self.asm.mov_reg_imm64(RDX, TAILLE_TAMPON_LECTURE)
            self.asm.etiquette(etq_ok)
            self.asm.lea_reg_etiquette(RSI, "tampon_lecture")
            self.asm.pop_reg(RDI)
            self.asm.mov_reg_imm64(RAX, 0)   # syscall read
            self.asm.syscall()

        elif isinstance(expr, OctetusExpr):
            self._gen_expr(expr.indice)
            self.asm.lea_reg_etiquette(RBX, "tampon_lecture")
            self.asm.add_reg_reg(RBX, RAX)
            self.asm.movzx_reg_mem8(RAX, RBX)

        elif isinstance(expr, MitteExpr):
            self._gen_expr(expr.fd)
            self.asm.mov_reg_reg(R9, RAX)
            self._gen_expr(expr.longueur)
            self.asm.mov_reg_reg(RCX, RAX)
            self._gen_adresse_base_tableau(expr.nom_tampon, RSI)
            self.asm.call_etiquette("routine_mitte_serie")

        elif isinstance(expr, Identifiant):
            self.asm.mov_reg_pile(RAX, self.variables[expr.nom])

        elif isinstance(expr, AppelFonction):
            for arg in expr.arguments:
                if isinstance(arg, Identifiant) and self._est_tableau(arg.nom):
                    self._gen_adresse_base_tableau(arg.nom, RAX)
                else:
                    self._gen_expr(arg)
                self.asm.push_reg(RAX)
            for i in reversed(range(len(expr.arguments))):
                self.asm.pop_reg(REGISTRES_ARGUMENTS[i])
            self.asm.call_etiquette(f"fn_{expr.nom}")

        elif isinstance(expr, OperationBinaire):
            self._gen_expr(expr.gauche)
            self.asm.push_reg(RAX)
            self._gen_expr(expr.droite)
            self.asm.mov_reg_reg(RBX, RAX)
            self.asm.pop_reg(RAX)

            op = expr.operateur
            if op == "+":
                self.asm.add_reg_reg(RAX, RBX)
            elif op == "-":
                self.asm.sub_reg_reg(RAX, RBX)
            elif op == "*":
                self.asm.imul_reg_reg(RAX, RBX)
            elif op == "/":
                self.asm.xor_reg_reg(RDX, RDX)
                self.asm.div_reg(RBX)
            elif op == "%":
                self.asm.xor_reg_reg(RDX, RDX)
                self.asm.div_reg(RBX)
                self.asm.mov_reg_reg(RAX, RDX)
            elif op in self.OPS_COMPARAISON:
                self.asm.cmp_reg_reg(RAX, RBX)
                self.asm.setcc_al(op)
                self.asm.movzx_rax_al()
            elif op in ("&", "&&"):
                self.asm.and_reg_reg(RAX, RBX)
            elif op in ("|", "||"):
                self.asm.or_reg_reg(RAX, RBX)
            elif op == "^":
                self.asm.xor_reg_reg(RAX, RBX)
            elif op == "<<":
                self.asm.mov_reg_reg(RCX, RBX)
                self.asm.shl_cl(RAX)
            elif op == ">>":
                self.asm.mov_reg_reg(RCX, RBX)
                self.asm.shr_cl(RAX)
            else:
                raise ErreurGeneration(f"opérateur non géré : {op}")

        else:
            raise ErreurGeneration(f"expression non gérée : {expr}")

    # --- Routine interne : conversion nombre -> texte décimal ---

    def _gen_routine_conversion(self):
        """
        Entrée : RAX = nombre (positif ou négatif) à convertir
        Sortie : RSI = pointeur vers le texte, RDX = longueur (avec saut de ligne inclus)
        """
        self.asm.etiquette("routine_conversion")
        self.asm.push_reg(RBX)
        self.asm.push_reg(RCX)
        self.asm.push_reg(R8)

        self.asm.mov_reg_imm64(R8, 0)  # drapeau "négatif"
        self.asm.cmp_reg_imm32(RAX, 0)
        self.asm.jge_etiquette("conv_pas_negatif_entree")
        self.asm.neg_reg(RAX)
        self.asm.mov_reg_imm64(R8, 1)
        self.asm.etiquette("conv_pas_negatif_entree")

        self.asm.mov_reg_imm64(RBX, 10)
        self.asm.lea_reg_etiquette(RDI, "tampon_fin")

        self.asm.cmp_reg_imm32(RAX, 0)
        self.asm.jne_etiquette("conv_boucle")
        self.asm.dec_reg(RDI)
        self.asm.mov_mem_imm8(RDI, ord("0"))
        self.asm.jmp_etiquette("conv_fin")

        self.asm.etiquette("conv_boucle")
        self.asm.cmp_reg_imm32(RAX, 0)
        self.asm.je_etiquette("conv_fin")
        self.asm.xor_reg_reg(RDX, RDX)
        self.asm.div_reg(RBX)
        self.asm.add_reg_imm32(RDX, ord("0"))
        self.asm.dec_reg(RDI)
        self.asm.mov_mem_reg8(RDI, RDX)
        self.asm.jmp_etiquette("conv_boucle")

        self.asm.etiquette("conv_fin")
        self.asm.cmp_reg_imm32(R8, 0)
        self.asm.je_etiquette("conv_pas_negatif_sortie")
        self.asm.dec_reg(RDI)
        self.asm.mov_mem_imm8(RDI, ord("-"))
        self.asm.etiquette("conv_pas_negatif_sortie")

        self.asm.mov_reg_reg(RSI, RDI)
        self.asm.lea_reg_etiquette(RDX, "tampon_apres")
        self.asm.sub_reg_reg(RDX, RSI)

        self.asm.pop_reg(R8)
        self.asm.pop_reg(RCX)
        self.asm.pop_reg(RBX)
        self.asm.ret()

    # --- Routine interne : écrire un tableau de caractères comme texte ---

    def _gen_routine_ecriture_serie(self):
        """
        Entrée : RSI = adresse du premier élément, RCX = nombre de caractères
        Effet : écrit ces caractères sur la sortie standard, suivis d'un saut de ligne
        """
        self.asm.etiquette("routine_ecriture_serie")
        self.asm.push_reg(RBX)
        self.asm.push_reg(RCX)
        self.asm.push_reg(RDI)
        self.asm.push_reg(R10)
        self.asm.push_reg(R11)

        self.asm.lea_reg_etiquette(RDI, "tampon_ecriture")
        self.asm.mov_reg_reg(R11, RDI)   # R11 = adresse de base du tampon (pour calculer la longueur)
        self.asm.mov_reg_imm64(R10, 0)   # R10 = indice courant

        self.asm.etiquette("scribe_boucle")
        self.asm.cmp_reg_reg(R10, RCX)
        self.asm.jge_etiquette("scribe_fin_boucle")

        self.asm.mov_reg_reg(RAX, R10)
        self.asm.mov_reg_imm64(RBX, 8)
        self.asm.imul_reg_reg(RAX, RBX)
        self.asm.mov_reg_reg(RBX, RSI)
        self.asm.sub_reg_reg(RBX, RAX)      # RBX = adresse de l'élément courant (base - index*8)
        self.asm.mov_reg_indirect(RAX, RBX)  # RAX = code du caractère
        self.asm.mov_mem_reg8(RDI, RAX)      # écrit l'octet bas dans le tampon
        self.asm.inc_reg(RDI)
        self.asm.inc_reg(R10)
        self.asm.jmp_etiquette("scribe_boucle")

        self.asm.etiquette("scribe_fin_boucle")
        self.asm.mov_mem_imm8(RDI, ord("\n"))
        self.asm.inc_reg(RDI)

        self.asm.mov_reg_reg(RDX, RDI)
        self.asm.sub_reg_reg(RDX, R11)   # longueur = curseur final - base
        self.asm.mov_reg_reg(RSI, R11)
        self.asm.mov_reg_imm64(RAX, 1)   # syscall write
        self.asm.mov_reg_imm64(RDI, 1)   # stdout
        self.asm.syscall()

        self.asm.pop_reg(R11)
        self.asm.pop_reg(R10)
        self.asm.pop_reg(RDI)
        self.asm.pop_reg(RCX)
        self.asm.pop_reg(RBX)
        self.asm.ret()

    def _gen_routine_mitte_serie(self):
        """
        Entrée : RSI = adresse du premier élément, RCX = nombre de caractères, R9 = descripteur
        Effet : écrit ces caractères vers le descripteur donné (sans saut de ligne ajouté)
        Sortie : RAX = nombre d'octets réellement écrits
        """
        self.asm.etiquette("routine_mitte_serie")
        self.asm.push_reg(RBX)
        self.asm.push_reg(RCX)
        self.asm.push_reg(RDI)
        self.asm.push_reg(R8)
        self.asm.push_reg(R9)
        self.asm.push_reg(R10)
        self.asm.push_reg(R11)

        self.asm.mov_reg_reg(R11, R9)    # R11 = descripteur (protégé de la boucle)
        self.asm.lea_reg_etiquette(RDI, "tampon_ecriture")
        self.asm.mov_reg_reg(R8, RDI)     # R8 = adresse de base du tampon
        self.asm.mov_reg_imm64(R10, 0)

        self.asm.etiquette("mitte_boucle")
        self.asm.cmp_reg_reg(R10, RCX)
        self.asm.jge_etiquette("mitte_fin_boucle")

        self.asm.mov_reg_reg(RAX, R10)
        self.asm.mov_reg_imm64(RBX, 8)
        self.asm.imul_reg_reg(RAX, RBX)
        self.asm.mov_reg_reg(RBX, RSI)
        self.asm.sub_reg_reg(RBX, RAX)
        self.asm.mov_reg_indirect(RAX, RBX)
        self.asm.mov_mem_reg8(RDI, RAX)
        self.asm.inc_reg(RDI)
        self.asm.inc_reg(R10)
        self.asm.jmp_etiquette("mitte_boucle")

        self.asm.etiquette("mitte_fin_boucle")
        self.asm.mov_reg_reg(RDX, RDI)
        self.asm.sub_reg_reg(RDX, R8)     # longueur = curseur final - base
        self.asm.mov_reg_reg(RSI, R8)
        self.asm.mov_reg_reg(RDI, R11)    # descripteur
        self.asm.mov_reg_imm64(RAX, 1)    # syscall write
        self.asm.syscall()

        self.asm.pop_reg(R11)
        self.asm.pop_reg(R10)
        self.asm.pop_reg(R9)
        self.asm.pop_reg(R8)
        self.asm.pop_reg(RDI)
        self.asm.pop_reg(RCX)
        self.asm.pop_reg(RBX)
        self.asm.ret()
