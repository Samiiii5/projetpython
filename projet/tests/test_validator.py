import unittest

from src.input_output.validator import (
    valider_prenom,
    valider_longueur,
)


class TestValidator(unittest.TestCase):

    # =========================
    # TESTS DU PRÉNOM
    # =========================

    def test_prenom_valide(self):
        valide, erreurs = valider_prenom("samuel")

        self.assertTrue(valide)
        self.assertEqual(erreurs, [])

    def test_prenom_trop_court(self):
        valide, erreurs = valider_prenom("sam")

        self.assertFalse(valide)
        self.assertTrue(len(erreurs) > 0)

    def test_prenom_trop_long(self):
        valide, erreurs = valider_prenom("abcdefghijkl")

        self.assertFalse(valide)
        self.assertTrue(len(erreurs) > 0)

    def test_prenom_avec_majuscule(self):
        valide, erreurs = valider_prenom("Samuel")

        self.assertFalse(valide)
        self.assertTrue(len(erreurs) > 0)

    def test_prenom_avec_chiffre(self):
        valide, erreurs = valider_prenom("samue1")

        self.assertFalse(valide)
        self.assertTrue(len(erreurs) > 0)

    def test_prenom_avec_caractere_special(self):
        valide, erreurs = valider_prenom("samuel@")

        self.assertFalse(valide)
        self.assertTrue(len(erreurs) > 0)

    # =========================
    # TESTS DE LA LONGUEUR
    # =========================

    def test_longueur_valide(self):
        valide, erreurs, longueur = valider_longueur("15")

        self.assertTrue(valide)
        self.assertEqual(erreurs, [])
        self.assertEqual(longueur, 15.0)

    def test_longueur_decimale(self):
        valide, erreurs, longueur = valider_longueur("15.5")

        self.assertTrue(valide)
        self.assertEqual(longueur, 15.5)

    def test_longueur_avec_virgule(self):
        valide, erreurs, longueur = valider_longueur("15,5")

        self.assertTrue(valide)
        self.assertEqual(longueur, 15.5)

    def test_longueur_trop_petite(self):
        valide, erreurs, longueur = valider_longueur("0")

        self.assertFalse(valide)
        self.assertIsNone(longueur)

    def test_longueur_trop_grande(self):
        valide, erreurs, longueur = valider_longueur("1001")

        self.assertFalse(valide)
        self.assertIsNone(longueur)

    def test_longueur_non_numerique(self):
        valide, erreurs, longueur = valider_longueur("abc")

        self.assertFalse(valide)
        self.assertIsNone(longueur)


if __name__ == "__main__":
    unittest.main()