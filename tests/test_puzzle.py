"""
Script de tests unitaires de puzzle.py
"""

import copy, echeance
try:
    import puzzle
except:
    pass

# *********************************************************************************************************
# Tests de la fonction dimensions()
# *********************************************************************************************************

class TestDimensions(object):
    """Tests de la fonction :py:func:`puzzle.dimensions`"""
    pytestmark = echeance.ECHEANCE3

    def test_dimensions_return(self):
        """Teste le type de la valeur de retour"""
        entrepot = [ ["#", "#", "+", "@"], [" ", ".", "$", "*"] ]
        assert( isinstance(puzzle.dimensions(entrepot), list) is True )  # les dimensions sont une liste
        assert( len(puzzle.dimensions(entrepot)) == 2 ) # de 2 élements
        assert( isinstance(puzzle.dimensions(entrepot)[0], int) is True ) # entier
        assert (isinstance(puzzle.dimensions(entrepot)[1], int) is True)  # entier

    def test_dimensions(self):
        """Teste les dimensions calculés sur un entrepot simple"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert( puzzle.dimensions(entrepot) == [2, 4] )

    def test_dimensions_sur_plusieurs_entrepots(self, novoban01, novoban02, novoban03):
        """Teste les dimensions calculés sur plusieurs entrepots de novoban"""
        assert (puzzle.dimensions(novoban01) == [6, 6])  # ayant les bonnes valeurs
        assert( puzzle.dimensions(novoban02) == [9, 6] )
        assert( puzzle.dimensions(novoban03) == [7, 6] )


# *********************************************************************************************************
# Tests de la fonction gagne()
# *********************************************************************************************************

class TestGagne(object):
    """Tests de la fonction :py:func:`puzzle.gagne`"""
    pytestmark = echeance.ECHEANCE2

    def test_gagne_return(self):
        """Teste le type de la valeur de retour"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert (isinstance(puzzle.gagne(entrepot), bool) is True)  # la valeur renvoyée est booléenne

    def test_gagne_puzzle_non_resolu(self, novoban01, novoban02, novoban06):
        """Teste la valeur renvoyée sur plusieurs entrepots non résolus de novoban"""
        assert( puzzle.gagne(novoban01) is False ) # la valeur est correcte pour un puzzle non résolu
        assert( puzzle.gagne(novoban02) is False )
        assert( puzzle.gagne(novoban06) is False )

    def test_gagne_sur_plusieurs_entrepots(self, novoban01_gagne, novoban02_gagne, novoban06_gagne):
        """Teste la valeur renvoyée sur plusieurs entrepots résolus de novoban"""
        assert (puzzle.gagne(novoban01_gagne) is True)
        assert( puzzle.gagne(novoban02_gagne) is True )
        assert( puzzle.gagne(novoban06_gagne) is True )


# *********************************************************************************************************
# Tests de la fonction est_mur()
# *********************************************************************************************************

class TestEstMur(object):
    """Tests de la fonction :py:func:`puzzle.est_mur`"""
    pytestmark = echeance.ECHEANCE3

    def test_est_mur_return(self):
        """Teste le type de la valeur de retour"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert (isinstance(puzzle.est_mur(entrepot, [0, 1]), bool) is True)  # un booléen

    def test_est_mur_entrepot_simple_dans_grille(self):
        """Teste sur un entrepot simple fictif lorsque la case visée est dans la grille"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert( puzzle.est_mur(entrepot, [0, 1]) is True )
        assert( puzzle.est_mur(entrepot, [1, 0]) is False ) # si " "
        assert( puzzle.est_mur(entrepot, [0, 2]) is False ) # si "+"
        assert (puzzle.est_mur(entrepot, [0, 3]) is False)  # si "@"
        assert (puzzle.est_mur(entrepot, [1, 1]) is False)  # si "."
        assert (puzzle.est_mur(entrepot, [1, 2]) is False)  # si "$"
        assert (puzzle.est_mur(entrepot, [1, 3]) is False)  # si "*"


    def test_est_mur_entrepot_simple_hors_grille(self):
        """Teste sur une grille simple lorsque la case visée est en dehors de la grille"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert( puzzle.est_mur(entrepot, [-1, 0]) is None ) # en dehors de l'entrepot à gauche
        assert (puzzle.est_mur(entrepot, [0, -1]) is None)  # en dehors de l'entrepot en haut
        assert (puzzle.est_mur(entrepot, [2, 0]) is None)  # en dehors de l'entrepot à droite
        assert (puzzle.est_mur(entrepot, [0, 4]) is None)  # en dehors de l'entrepot en bas



# *********************************************************************************************************
# Tests de la fonction est_caisse()
# *********************************************************************************************************

class TestCaisse(object):
    """Tests de la fonction :py:func:`puzzle.est_caisse`"""
    pytestmark = echeance.ECHEANCE3

    def test_est_caisse_return(self):
        """Teste de la valeur de retour"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert (isinstance(puzzle.est_caisse(entrepot, [0, 0]), bool) is True) # un booléen

    def test_est_caisse_entrepot_simple_dans_grille(self):
        """Teste de la valeur renvoyée sur un entrepot simple"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert( puzzle.est_caisse(entrepot, [0, 0]) is False)  # la 1ere case n'est pas une caisse
        assert( puzzle.est_caisse(entrepot, [1, 2]) is True)  # la caisse $
        assert( puzzle.est_caisse(entrepot, [1, 3]) is True)  # la caisse *
        assert( puzzle.est_caisse(entrepot, [1, 1]) is False )  # la cible .
        assert( puzzle.est_caisse(entrepot, [0, 3]) is False)  # le gardien @
        assert (puzzle.est_caisse(entrepot, [0, 2]) is False)  # +

    def test_est_caisse_entrepot_simple_hors_grille(self):
        """Teste de la valeur renvoyée sur un entrepot simple"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert( puzzle.est_caisse(entrepot, [-1, 0]) is None)  # en dehors de l'entrepot à gauche
        assert( puzzle.est_caisse(entrepot, [0, -1]) is None)  # en dehors de l'entrepot en haut
        assert( puzzle.est_caisse(entrepot, [2, 0]) is None)  # en dehors de l'entrepot à droite
        assert( puzzle.est_caisse(entrepot, [0, 4]) is None)  # en dehors de l'entrepot en bas


# *********************************************************************************************************
# Tests de la fonction est_cible()
# *********************************************************************************************************

class TestEstCible(object):
    """Tests de la fonction :py:func:`puzzle.est_cible`"""
    pytestmark = echeance.ECHEANCE3

    def test_est_cible_return(self):
        """Teste la valeur de retour"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert (isinstance(puzzle.est_caisse(entrepot, [0, 0]), bool) is True) # un booléen

    def test_est_cible_entrepot_simple_dans_grille(self):
        """Teste si la case est bien identifiée comme cible sur un entrepot simple lorsque la case est dans la grille"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert (puzzle.est_cible(entrepot, [0, 0]) is False)  # la 1ere case n'est pas une caisse
        assert( puzzle.est_cible(entrepot, [1, 1]) is True ) # "."
        assert (puzzle.est_cible(entrepot, [1, 2]) is False)  # $
        assert (puzzle.est_cible(entrepot, [0, 2]) is True)  # la cible +
        assert (puzzle.est_cible(entrepot, [0, 3]) is False)  # le gardien @
        assert (puzzle.est_cible(entrepot, [1, 3]) is True) # *


    def test_est_cible_en_dehors(self):
        """Teste si la case est traitée hors grille"""
        entrepot = [["#", "#", "+", "@"], [" ", ".", "$", "*"]]
        assert (puzzle.est_cible(entrepot, [-1, 0]) is None)  # en dehors de l'entrepot à gauche
        assert (puzzle.est_cible(entrepot, [0, -1]) is None)  # en dehors de l'entrepot en haut
        assert (puzzle.est_cible(entrepot, [2, 0]) is None)  # en dehors de l'entrepot à droite
        assert (puzzle.est_cible(entrepot, [0, 4]) is None)  # en dehors de l'entrepot en bas


# *********************************************************************************************************
# Tests de la fonction deplace()
# *********************************************************************************************************

class TestDeplaceSansCaisse(object):
    """Tests de la fonction :py:func:`puzzle.deplace`"""
    pytestmark = echeance.ECHEANCE4

    def test_deplace_gardien_deplacement_vers_case_vide(self):
        """Test si le gardien est déplacé dans le cas où la case visée est vide"""
        entrepot = [ [' '], ['@'] ]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [ ['@'], [' '] ])  # l'entrepot a-t-il été modifié comme attendu
        assert( reponse == True ) # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], [' ']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [[' '], ['@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [ [' ', '@'] ]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['@', ' '] ])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', ' ']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [[' ', '@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?


    def test_deplace_gardien_sur_cible_simple(self):
        """Teste si le gardien est déplacé dans le cas où la case visée est une cible"""
        entrepot = [['.'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['+'], [' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['.', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['+', ' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

    def test_deplace_gardien_hors_cible_simple(self):
        """Teste si le gardien (sur cible) est déplacé dans le cas où la case visée est vide"""
        entrepot = [['+'], [' ']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [['.'], ['@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['+', ' ']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [['.', '@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

    def test_deplace_gardien_sur_mur(self):
        """Teste si le gardien est déplacé dans le cas où la case visée est un mur"""
        entrepot = [['#', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['#', '@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', '#']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [['@', '#']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], ['#']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [['@'], ['#']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['#'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['#'],
                             ['@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?




class TestDeplaceAvecCaisse(object):
    """Tests de la fonction :py:func:`puzzle.deplace`"""
    pytestmark = echeance.ECHEANCE5


    def test_deplace_gardien_pousse_caisse_simple(self):
        """Teste si le gardien pousse une caisse dans le cas où la caisse est poussée vers une case vide"""
        entrepot = [[' '], ['$'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['$'], ['@'], [' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], ['$'], [' ']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [[' '], ['@'], ['$']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [[' ', '$', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['$', '@', ' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', '$', ' ']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [[' ', '@', '$']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

    def test_deplace_gardien_pousse_caisse_sur_cible(self):
        """Teste si le gardien pousse une caisse dans le cas où la caisse est poussée vers une cible"""
        entrepot = [['.'], ['$'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['*'], ['@'], [' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], ['$'], ['.']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [[' '], ['@'], ['*']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['.', '$', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['*', '@', ' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', '$', '.']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [[' ', '@', '*']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

    def test_deplace_gardien_pousse_caisse_hors_cible(self):
        """Teste si le gardien pousse une caisse (sur une cible) vers une case vide"""
        entrepot = [[' '], ['*'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['$'], ['+'], [' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], ['*'], [' ']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [[' '], ['+'], ['$']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [[' ', '*', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['$', '+', ' ']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', '*', ' ']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [[' ', '+', '$']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == True)  # la réponse booléenne est-elle correcte ?

    def test_deplace_gardien_pousse_caisse_sur_mur(self):
        """Teste si le gardien pousse une caisse contre un mur"""
        entrepot = [['#'], ['$'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['#'], ['$'], ['@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], ['$'], ['#']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [['@'], ['$'], ['#']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['#', '$', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['#', '$', '@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', '$', '#']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [['@', '$', '#']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

    def test_deplace_gardien_pousse_caisse_sur_caisse(self):
        """Teste si le gardien pousse une caisse contre une caisse"""
        entrepot = [['$'], ['$'], ['@']]
        reponse = puzzle.deplace(entrepot, "haut")
        assert (entrepot == [['$'], ['$'], ['@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@'], ['$'], ['$']]
        reponse = puzzle.deplace(entrepot, "bas")
        assert (entrepot == [['@'], ['$'], ['$']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['$', '$', '@']]
        reponse = puzzle.deplace(entrepot, "gauche")
        assert (entrepot == [['$', '$', '@']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?

        entrepot = [['@', '$', '$']]
        reponse = puzzle.deplace(entrepot, "droite")
        assert (entrepot == [['@', '$', '$']])  # l'entrepot a-t-il été modifié comme attendu
        assert (reponse == False)  # la réponse booléenne est-elle correcte ?


# *********************************************************************************************************
# Tests de la fonction undo()
# *********************************************************************************************************

class TestUndo(object):
    """Tests de la fonction :py:func:`puzzle.undo`"""
    pytestmark = echeance.ECHEANCE6

    def test_undo_avec_historique(self):
        """Teste si l'historique est bien manipulé lorsque le joueur a déjà joué plusieurs coups"""
        entrepot_ini = [ [" ", " ", "$", "@"] ]
        entrepot_1 = [ [" ", "$", "@", " "] ]
        entrepot_2 = [ ["$", "@", " ", " "] ]
        joueur_ini = {"score": 2, "historique" : [ entrepot_ini, entrepot_1, entrepot_2 ] }

        # 1er undo
        joueur = copy.deepcopy(joueur_ini)
        entrepot = puzzle.undo( joueur )
        assert( isinstance(entrepot, list) is True ) # une liste 2D est-elle renvoyée ?
        assert( isinstance(entrepot[0], list) is True )
        assert( entrepot == entrepot_1 ) # l'entrepot renvoyé est-il correct ?
        assert( joueur["score"] == 3 ) # le score a-t-il été incrémenté ?
        assert( joueur["historique"] == [entrepot_ini, entrepot_1] ) # l'historique a-t-il été mis à jour ?

        # 2eme undo
        entrepot = puzzle.undo( joueur )
        assert (entrepot == entrepot_ini)  # l'entrepot renvoyé est-il correct ?
        assert (joueur["score"] == 4)  # le score a-t-il été incrémenté ?
        assert (joueur["historique"] == [entrepot_ini])  # l'historique a-t-il été mis à jour ?



    def test_undo_sans_historique(self):
        """Teste si le undo lorsque le joueur n'a pas de coup mémorisé dans l'historique"""
        entrepot_ini = [[" ", " "], ["$", "@"]]
        joueur_ini = {"score": 6, "historique": [entrepot_ini]}

        # 1er undo
        joueur = copy.deepcopy(joueur_ini)
        entrepot = puzzle.undo(joueur)
        assert (isinstance(entrepot, list) is True)  # une liste 2D est-elle renvoyée ?
        assert (isinstance(entrepot[0], list) is True)
        assert ( entrepot == entrepot_ini )  # l'entrepot renvoyé est-il correct ?
        assert (joueur["score"] == joueur_ini["score"])  # le score est-il resté identique ?
        assert (joueur["historique"] == joueur_ini["historique"])  # l'historique a-t-il été mis à jour ?

        # 2eme undo
        entrepot = puzzle.undo(joueur)
        assert (entrepot == entrepot_ini)  # l'entrepot renvoyé est-il correct ?
        assert (joueur["score"] == joueur_ini["score"])  # le score a-t-il été incrémenté ?
        assert ( joueur["historique"] == joueur_ini["historique"] )  # l'historique a-t-il été mis à jour ?



# *********************************************************************************************************
# Tests de la fonction reset()
# *********************************************************************************************************

class TestReset(object):
    """Tests de la fonction :py:func:`puzzle.reset`"""
    pytestmark = echeance.ECHEANCE6

    def test_reset(self, novoban01, jcrazy ):
        """Teste si la partie est bien remise à zéro sur une partie fictive avec jcrazy et novoban01"""
        jcrazy["numero"] = 1
        jcrazy["historique"] = [ novoban01 ] *3
        entrepot = puzzle.reset(jcrazy)
        assert( isinstance(entrepot, list) is True ) # la fonction renvoie un entrepot
        assert( entrepot == novoban01 ) # L'entrepot est-il correct ?
        assert( len(jcrazy["historique"]) == 1 ) # L'historique a-t-il été remise à zéro ?
        assert( jcrazy["historique"][0] == entrepot ) # avec le bon entrepot de départ

# *********************************************************************************************************
# Tests de la fonction incremente_score()
# *********************************************************************************************************

class TestIncrementeScore(object):
    """Tests de la fonction :py:func:`puzzle.incremente_score`"""
    pytestmark = echeance.ECHEANCE3

    def test_incremente_score_return(self, jcrazy):
        """Teste la valeur de retour de incremente_score"""
        assert( puzzle.incremente_score(jcrazy, 1) is None )

    def test_incremente_score(self, jcrazy ):
        """Teste si l'incrémentation du score est effective"""
        puzzle.incremente_score(jcrazy, 1)
        assert( jcrazy["score"] == 4 )
        puzzle.incremente_score(jcrazy, 6)
        assert (jcrazy["score"] == 10)

# *********************************************************************************************************
# Tests de la fonction sauv_historique()
# *********************************************************************************************************

# TODO : vérifier l'historique initial après chargement d'une partie

class TestSauvHistorique(object):
    """Tests de la fonction :py:func:`puzzle.incremente_score`"""
    pytestmark = echeance.ECHEANCE4

    def test_sauv_historique_return(self, jcrazy):
        """Teste la valeur de retour de sauv_historique"""
        assert( puzzle.incremente_score(jcrazy, 1) is None )

    def test_sauv_historique_valeurs(self, jcrazy ):
        """Teste si la sauvegarde de l'historique est effective et conduit à l'ajout d'un entrepot"""
        entrepot = ["#", "+", "@", " "]
        puzzle.sauv_historique(jcrazy, entrepot)
        assert( len(jcrazy["historique"]) == 1)
        assert( jcrazy["historique"][-1] == entrepot )
        puzzle.sauv_historique(jcrazy, entrepot)
        assert (len(jcrazy["historique"]) == 2)
        assert (jcrazy["historique"][-1] == entrepot)

    def test_sauv_historique_copie_en_profondeur(self, jcrazy):
        """Teste si la sauvegarde de l'historique a bien été effectuée avec une copie en profondeur de l'entrepot"""
        entrepot = ["#", "+", "@", " "]
        puzzle.sauv_historique(jcrazy, entrepot)
        puzzle.sauv_historique(jcrazy, entrepot)
        assert (len(jcrazy["historique"]) == 2)
        assert (jcrazy["historique"][-1] is not entrepot) # les objects sont différents ?
        assert (jcrazy["historique"][0] is not jcrazy["historique"][1] )
