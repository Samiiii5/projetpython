import unittest
from unittest.mock import patch

from src.input_output.input_reader import lire_participant


class TestInputReader(unittest.TestCase):

    def test_saisie_valide(self):
        with patch(
            "builtins.input",
            return_value="samuel 15.5"
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")
        self.assertEqual(participant.longueur_baton, 15.5)

    def test_saisie_avec_virgule(self):
        with patch(
            "builtins.input",
            return_value="samuel 15,5"
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")
        self.assertEqual(participant.longueur_baton, 15.5)

    def test_majuscule_puis_saisie_valide(self):
        with patch(
            "builtins.input",
            side_effect=[
                "Samuel 15.5",
                "samuel 15.5",
            ]
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")
        self.assertEqual(participant.longueur_baton, 15.5)

    def test_chiffre_puis_saisie_valide(self):
        with patch(
            "builtins.input",
            side_effect=[
                "samue1 15.5",
                "samuel 15.5",
            ]
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")

    def test_caractere_special_puis_saisie_valide(self):
        with patch(
            "builtins.input",
            side_effect=[
                "samuel@ 15.5",
                "samuel 15.5",
            ]
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")

    def test_longueur_non_numerique_puis_saisie_valide(self):
        with patch(
            "builtins.input",
            side_effect=[
                "samuel abc",
                "samuel 15.5",
            ]
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")
        self.assertEqual(participant.longueur_baton, 15.5)

    def test_information_manquante_puis_saisie_valide(self):
        with patch(
            "builtins.input",
            side_effect=[
                "samuel",
                "samuel 15.5",
            ]
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")
        self.assertEqual(participant.longueur_baton, 15.5)

    def test_trop_d_informations_puis_saisie_valide(self):
        with patch(
            "builtins.input",
            side_effect=[
                "samuel 15.5 quelquechose",
                "samuel 15.5",
            ]
        ):
            participant = lire_participant(1)

        self.assertEqual(participant.prenom, "samuel")
        self.assertEqual(participant.longueur_baton, 15.5)


if __name__ == "__main__":
    unittest.main()