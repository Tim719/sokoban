"""
===================================================================
Script test_terminal.py (pour les fonctions de :py:mod:`terminal`)
===================================================================
"""

import pytest, echeance, sys, io
import re
try:
    import terminal
except:
    pass


# *********************************************************************************************************
# Tests de la fonction affiche_entrepot()
# *********************************************************************************************************

class TestAfficheEntrepot(object):
    """Tests de la fonction :py:func:`terminal.affiche_entrepot`"""

    pytestmark = echeance.ECHEANCE1

    def test_affiche_entrepot(self, capsys, novoban01):
        """Teste si l'affichage d'un entrepot est correct avec celui de novoban01"""
        terminal.affiche_entrepot(novoban01)    # Lance l'affichage
        captured = capsys.readouterr() # Le contenu affiché sur sdtout et sterr
        assert (captured[0] == "####  \n#  ###\n#  $@#\n# *. #\n##   #\n #####\n") # Est-il correct ?



# *********************************************************************************************************
# Tests de la fonction affiche_entrepot_couleur()
# *********************************************************************************************************

class TestAfficheEntrepotCouleur(object):
    """Tests de la fonction :py:func:`terminal.affiche_entrepot_couleur`"""
    pytestmark = echeance.ECHEANCE2

    def test_affiche_entrepot_couleur(self, capsys, novoban01):
        """Teste si l'affichage d'un entrepot est correct avec celui de novoban01"""
        terminal.affiche_entrepot_couleur(novoban01)    # Lance l'affichage
        captured = capsys.readouterr()
        assert ( re.search("\[[3-4][0-9]m+", captured[0]) )  # Des couleurs sont-elles présentes N


# *********************************************************************************************************
# Tests de la fonction interprete_action()
# *********************************************************************************************************

class TestInterpreteAction(object):
    """Tests de la fonctoin :py:func:`terminal.interprete_action`"""
    pytestmark = echeance.ECHEANCE2

    def test_interprete_action_return(self):
        """Teste la valeur de retour"""
        assert( isinstance(terminal.interprete_action("Z"), str) is True )

    def test_interprete_action(self):
        """Teste la conversion d'un caractère en action pour des caractères valides"""
        assert( terminal.interprete_action("Z") == "haut" )
        assert( terminal.interprete_action("Q") == "gauche" )
        assert( terminal.interprete_action("S") == "bas" )
        assert( terminal.interprete_action("D") == "droite" )
        assert( terminal.interprete_action("U") == "undo" )
        assert( terminal.interprete_action("E") == "exit" )


    def test_interprete_action_invalide(self):
        """Teste la conversion d'un caractère en action lorsque le caractère ne fait pas partie des caractères valides"""
        assert( terminal.interprete_action("A") is None )



# *********************************************************************************************************
# Tests de la fonction interprete_menu()
# *********************************************************************************************************

class TestInterpreteMenu(object):
    """Tests de la fonction :py:func:`terminal.interprete_menu`"""
    pytestmark = echeance.ECHEANCE7

    def test_interprete_menu_return(self):
        """Le menu doit être une chaine de caractère"""
        assert (isinstance(terminal.interprete_menu("S"), str) is True)  # l'action est une chaine de caractère

    def test_interprete_menu_sur_plusieurs_options(self):
        """Teste la conversion d'un caractère de menu en menu, lorsque le caractère fait partie des caractères
        possibles hormis l'option PXX."""
        assert( terminal.interprete_menu("S") == "start" )
        assert( terminal.interprete_menu("CN") == "novoban" )
        assert( terminal.interprete_menu("CS") == "sokoban" )
        assert( terminal.interprete_menu("E") == "exit" )

    def test_interprete_menu_sur_option_puzzle(self):
        """Teste la conversion de l'option PXX en menu"""
        assert( terminal.interprete_menu("P1") == "puzzle" )
        assert( terminal.interprete_menu("P5") == "puzzle" )

    def test_interprete_menu_invalide(self):
        """Teste l(interprétation du menu lorsque le caractère ne fait pas partie des menus possibles"""
        assert( terminal.interprete_menu("A") is None )


# *********************************************************************************************************
# Tests de la fonction saisie_action()
# *********************************************************************************************************

class TestSaisieAction(object):
    """Tests de la fonction :py:func:`terminal.sasie_action`"""
    pytestmark = echeance.ECHEANCE2

    def test_saisie_action_valide_majuscule(self):
        """Teste la saisie d'une action valide en majuscule"""
        sys.stdin = io.StringIO("Z\nQ\nE\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_action() == 'Z')
        assert( terminal.saisie_action() == 'Q')
        assert( terminal.saisie_action() == 'E')


    def test_saisie_action_valide_minuscule(self):
        """Teste la saisie d'une action valide en minuscule"""
        sys.stdin = io.StringIO("z\nq\ne\n")  # Enregistre le flux sortant dans un buffer
        assert (terminal.saisie_action() == 'Z')
        assert (terminal.saisie_action() == 'Q')
        assert (terminal.saisie_action() == 'E')


    def test_saisie_action_non_valide_majuscule(self):
        """Teste la saisie d'une action non valide (caractère ou chaine de caractère non reconnus) en majuscule"""
        sys.stdin = io.StringIO("M\nX\nZ\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_action() == 'Z')
        sys.stdin = io.StringIO("apprendalire\nE\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_action() == 'E')


# *********************************************************************************************************
# Tests de la fonction saisie_menu()
# *********************************************************************************************************

class TestSaisieMenu(object):
    """Tests de la fonction :py:func:`terminal.saisie_menu`"""
    pytestmark = echeance.ECHEANCE7

    def test_saisie_menu_valide_majuscule(self, jcrazy ):
        """Teste la saisie de menu valide en majuscule par le joueur crazy hormis le menu puzzle pXX"""
        sys.stdin = io.StringIO("S\nCN\nE\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_menu( jcrazy ) == 'S')
        assert( terminal.saisie_menu( jcrazy ) == 'CN')
        assert( terminal.saisie_menu( jcrazy ) == 'E')


    def test_saisie_menu_valide_minuscule(self, jcrazy):
        """Teste la saisie de menu valide en minuscule par le joueur crazy hormis le menu puzzle pXX"""
        sys.stdin = io.StringIO("s\ncs\ne\n")  # Enregistre le flux sortant dans un buffer
        assert (terminal.saisie_menu( jcrazy ) == 'S')
        assert (terminal.saisie_menu( jcrazy ) == 'CS')
        assert (terminal.saisie_menu( jcrazy ) == 'E')

    def test_saisie_menu_non_valide_majuscule(self, jcrazy):
        """Teste la saisie de menus non valides en majuscule par le joueur crazy"""
        sys.stdin = io.StringIO("M\nT\nS\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_menu( jcrazy ) == 'S')
        sys.stdin = io.StringIO("apprendalire\nCS\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_menu( jcrazy ) == 'CS')

    def test_saisie_menu_puzzle_valide(self, change_repertoire_courant, jcrazy ):
        """Teste la saisie d'un puzzle auquel le joueur a le droit de jouer (car existant et débloqué)"""
        jcrazy["collection"] = "novoban"
        jcrazy["max"] = 10
        sys.stdin = io.StringIO("p3\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_menu( jcrazy ) == 'P3')

    def test_saisie_menu_puzzle_inexistant(self, change_repertoire_courant, jcrazy ):
        """Teste la saisie d'un puzzle auquel le joueur n'a le droit de jouer car n'existant pas"""
        jcrazy["collection"] = "novoban"
        jcrazy["max"] = 99
        sys.stdin = io.StringIO("P99\nP75\nP12\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_menu(jcrazy) == 'P12')

    def test_saisie_menu_puzzle_bloque(self,  change_repertoire_courant, jcrazy ):
        """Teste la saisie d'un puzzle auquel le joueur n'a le droit de jouer car bloqué"""
        jcrazy["collection"] = "novoban"
        jcrazy["max"] = 15
        sys.stdin = io.StringIO("P20\nP25\nP8\n")  # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_menu(jcrazy) == 'P8')



# *********************************************************************************************************
# Tests de la fonction saisie_pseudo()
# *********************************************************************************************************

class TestSaisiePseudo(object):
    """Tests de la fonction :py:func:`terminal.saisie_pseudo`"""
    pytestmark = echeance.ECHEANCE1

    def test_saisie_pseudo_valide(self):
        """Teste la saisie d'un pseudo valide"""
        sys.stdin = io.StringIO("crazy\n")                      # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_pseudo( ) == 'crazy')           # Teste la saisie
        sys.stdin = io.StringIO("moi\n")                        # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_pseudo( ) == 'moi')             # Teste la saisie


    def test_saisie_pseudo_non_valide(self):
        """Teste la saisie d'un pseudo interdit"""
        sys.stdin = io.StringIO("records\ngood\n")              # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_pseudo( ) == 'good')            # Teste la saisie

    def test_saisie_pseudo_defaut(self):
        """Teste la saisie du pseudo par defaut"""
        sys.stdin = io.StringIO("\n")                      # Enregistre le flux sortant dans un buffer
        assert( terminal.saisie_pseudo( ) == 'crazy')           # Teste la saisie

