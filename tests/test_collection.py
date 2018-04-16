"""
Script de tests unitaires de collection.py
"""

import pytest, echeance
try:
    import collection
except:
    pass


# *********************************************************************************************************
# Tests de la fonction dimensions()
# *********************************************************************************************************

class TestDimensions(object):
    """Tests de la fonction :py:func:`collection.dimensions`"""
    pytestmark = echeance.ECHEANCE2

    def test_dimensions_return(self, change_repertoire_courant):
        """Teste la valeur renvoyée par collection.dimensions() lorsque le fichier existe"""
        fichier = "collections/novoban/novoban01.xsb"
        assert( isinstance(collection.dimensions(fichier), list) is True ) # une liste ?
        assert( len(collection.dimensions(fichier)) == 2 )                 # de 2 éléments
        assert( isinstance(collection.dimensions(fichier)[0], int) )       # entier
        assert( isinstance(collection.dimensions(fichier)[1], int) )       # entier

    def test_dimensions_sur_puzzle_existant(self, change_repertoire_courant):
        """Teste si les dimensions sont correctes sur un puzzle novoban01"""
        fichier = "collections/novoban/novoban01.xsb"
        assert( collection.dimensions(fichier) == [6, 6] ) # La liste renvoyée est correcte


    def test_dimensions_sur_plusieurs_puzzles_existants(self, change_repertoire_courant):
        """Teste si les dimensions sont correctes sur plusieurs puzzles existants"""
        assert( collection.dimensions("collections/novoban/novoban02.xsb") == [9, 6] )
        assert( collection.dimensions("collections/novoban/novoban03.xsb") == [7, 6] )


    def test_dimensions_sur_puzzle_manquant(self, change_repertoire_courant):
        """Teste les dimensions lorsque le puzzle n'existe pas"""
        assert( collection.dimensions("collections/novoban/novoban00.xsb") is None )


# *********************************************************************************************************
# Tests de la fonction charge_puzzle()
# *********************************************************************************************************

class TestChargePuzzle(object):
    """Tests de la fonction :py:func:`collection.charge_puzzle`"""
    pytestmark = echeance.ECHEANCE2

    def test_charge_puzzle_return(self, change_repertoire_courant, novoban01):
        """Teste la valeur renvoyée par le charqement d'un puzzle sur novoban01"""
        assert( isinstance(collection.charge_puzzle("novoban", 1), list) is True)       # Renvoie une liste
        assert( len(collection.charge_puzzle("novoban", 1)) == len(novoban01))          # avec le bon nombre de lignes
        assert( isinstance(collection.charge_puzzle("novoban", 1)[0], list) is True )   # avec des colonnes
        assert( len(collection.charge_puzzle("novoban", 1)[0]) == len(novoban01[0]))    # avec le bon nombre de colonnes
        assert( isinstance(collection.charge_puzzle("novoban", 1)[0][0], str) is True) # avec des éléments str

    def test_charge_puzzle_sur_plusieurs_puzzles_existants(self, change_repertoire_courant, novoban01):
        """Teste l'entrepot renvoyé par le charqement d'un puzzle sur novoban01"""
        assert( collection.charge_puzzle("novoban", 1) == novoban01) # avec le bon contenu

    def test_charge_puzzle_sur_plusieurs_puzzles_existants(self, change_repertoire_courant, novoban02, novoban03):
        """Teste l'entrepot renvoyé par le charqement de différents puzzles de novoban"""
        assert( collection.charge_puzzle("novoban", 2) == novoban02 )
        assert( collection.charge_puzzle("novoban", 3) == novoban03 )


    def test_charge_puzzle_sur_puzzle_manquant(self, change_repertoire_courant):
        """Teste la valeur renvoyée lorsque le puzzle est manquant"""
        e = collection.charge_puzzle("novoban", 99)
        assert( e is None )


# *********************************************************************************************************
# Tests de la fonction est_dans_collection()
# *********************************************************************************************************

class TestEstDansCollection(object):
    """Tests de la fonction :py:func:`collection.est_dans_collection`"""
    pytestmark = echeance.ECHEANCE6

    def test_est_dans_collection_return(self, change_repertoire_courant):
        """Teste la valeur de retour"""
        assert( isinstance(collection.est_dans_collection("novoban", 10), bool) ) # réponse booléenne

    def test_est_dans_collection_puzzle_existant(self, change_repertoire_courant):
        """Teste que le puzzle est déclaré existant sur des puzzles effectifs des collections novoban et sokoban"""
        assert( collection.est_dans_collection("novoban", 10) is True ) # novoban10.xsb
        assert( collection.est_dans_collection("novoban", 2) is True ) # novoban02.xsb
        assert( collection.est_dans_collection("sokoban", 3) is True ) # sokoban03.xsb

    def test_est_dans_collection_puzzle_inexistant(self, change_repertoire_courant):
        """Teste que le puzzle est déclaré non existant sur des puzzles n'existant pas"""
        assert (collection.est_dans_collection("novoban", 99) is False)  # novoban99.xsb n'existe pas
        assert( collection.est_dans_collection("encoreunban", 1) is False ) # la collection encoreunban n'existe oas



# *********************************************************************************************************
# Tests de la fonction nbre_puzzle()
# *********************************************************************************************************

class TestNbrePuzzle(object):
    """Tests de la fonction :py:func:`collection.nbre_puzzle`"""
    pytestmark = echeance.ECHEANCE6

    def test_nbre_puzzle_return(self, change_repertoire_courant):
        """Teste le type de la valeur de retour"""
        assert(isinstance(collection.nbre_puzzle("novoban"), int)) # réponse sous forme d'un entier

    def test_nbre_puzzle_collection_existante(self, change_repertoire_courant):
        """Teste le nombre de puzzles calculés sur des collections existantes"""
        assert(collection.nbre_puzzle("novoban") == 50) # la réponse est-elle correcte ?
        assert(collection.nbre_puzzle("sokoban") == 15)

    def test_nbre_puzzle_collection_inexistante(self, change_repertoire_courant):
        """Teste le nombre de puzzles calculés sur des collections inexistantes"""
        assert(collection.nbre_puzzle("encoreunban") == 0)


# *********************************************************************************************************
# Tests de la fonction debloque_niveau()
# *********************************************************************************************************

class TestDebloqueNiveau(object):
    """Tests de la fonction :py:func:`collection.debloque_niveau`"""
    pytestmark = echeance.ECHEANCE6

    def test_debloque_niveau_return(self, jcrazy):
        """Teste de la valeur de retour de debloque_niveau"""
        assert( isinstance(collection.debloque_niveau(jcrazy), bool) is True)

    def test_debloque_niveau_dans_collection(self, change_repertoire_courant, jcrazy):
        """Teste le débloquage des niveaux au sein de la collection"""
        jcrazy["collection"] = "novoban"
        jcrazy["numero"] = jcrazy["max"]
        res = collection.debloque_niveau(jcrazy)
        assert(res is True) # Le débloquage a été fait
        assert( jcrazy["max"] == 9)

    def test_debloque_niveau_fin_de_collection(self, jcrazy):
        """Teste le débloquage de niveau lorsqu'on atteint la fin de la collection"""
        jcrazy["collection"] = "novoban"
        jcrazy["numero"] = 50
        jcrazy["max"] = 50
        res = collection.debloque_niveau(jcrazy)
        assert (res is False)  # Le débloquage a été fait
        assert (jcrazy["max"] == 50)

# *********************************************************************************************************
# Tests des fonctions restaure et sauv contexte
# *********************************************************************************************************

# TODO : Ajouter le test vérifiant la présence du fichier de sauvagerde

class TestSauvRestaureContexte(object):
    """Tests des focnctions :py:func:`collection.sauv_contexte` et :py:func:`collection.restaure_contexte`"""
    pytestmark = echeance.ECHEANCE5

    def test_sauv_et_restaure_contexte_joueur_existant(self, arborescence_records, jcrazy):
        """Vérifie si la sauvegarde est correcte"""
        res = collection.sauve_contexte(jcrazy)
        assert( res == True )
        joueur = collection.charge_contexte("crazy")
        assert(joueur == jcrazy )