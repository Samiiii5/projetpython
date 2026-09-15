import unittest

from src.models.participant import Participant
from src.services.tirage import trouver_plus_petit_baton


class TestTirage(unittest.TestCase):

    def test_plus_petit_baton_au_milieu(self):
        participants = [
            Participant("samuel", 15.5),
            Participant("moussa", 20.0),
            Participant("patrick", 10.5),
            Participant("kevin", 18.0),
        ]

        resultat = trouver_plus_petit_baton(participants)

        self.assertEqual(resultat.prenom, "patrick")
        self.assertEqual(resultat.longueur_baton, 10.5)

    def test_plus_petit_baton_au_debut(self):
        participants = [
            Participant("samuel", 5.5),
            Participant("moussa", 20.0),
            Participant("patrick", 10.5),
            Participant("kevin", 18.0),
        ]

        resultat = trouver_plus_petit_baton(participants)

        self.assertEqual(resultat.prenom, "samuel")

    def test_plus_petit_baton_a_la_fin(self):
        participants = [
            Participant("samuel", 15.5),
            Participant("moussa", 20.0),
            Participant("patrick", 10.5),
            Participant("kevin", 5.5),
        ]

        resultat = trouver_plus_petit_baton(participants)

        self.assertEqual(resultat.prenom, "kevin")

    def test_longueurs_decimales(self):
        participants = [
            Participant("samuel", 15.8),
            Participant("moussa", 15.5),
            Participant("patrick", 15.6),
        ]

        resultat = trouver_plus_petit_baton(participants)

        self.assertEqual(resultat.prenom, "moussa")
        self.assertEqual(resultat.longueur_baton, 15.5)

    def test_prenoms_identiques(self):
        participants = [
            Participant("samuel", 20.0),
            Participant("samuel", 10.5),
            Participant("patrick", 15.0),
        ]

        resultat = trouver_plus_petit_baton(participants)

        self.assertEqual(resultat.prenom, "samuel")
        self.assertEqual(resultat.longueur_baton, 10.5)


if __name__ == "__main__":
    unittest.main()