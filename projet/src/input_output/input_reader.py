from ..models.participant import Participant

from .validator import (
    valider_longueur,
    valider_prenom,
)


def lire_participant(numero: int) -> Participant:

    while True:
        print("\n" + "-" * 40)
        print(f"SAISIE DU PARTICIPANT {numero}")
        print("-" * 40)

        print("Format attendu : prénom longueur")
        print("Exemple : samuel 15.5")

        try:
            saisie = input("> ")

        except EOFError:
            print("\nEntrée interrompue.")
            raise SystemExit

        except KeyboardInterrupt:
            print("\nProgramme interrompu.")
            raise SystemExit

        saisie = saisie.strip()

        # Vérification d'une saisie vide
        if not saisie:
            print("\n✗ La saisie ne peut pas être vide.")
            print("Veuillez saisir : prénom longueur")
            print("Exemple : samuel 15.5")
            continue

        # Séparation du prénom et de la longueur
        elements = saisie.split()

        # Vérification du nombre de champs
        if len(elements) < 2:
            print("\n✗ Il manque une information.")
            print(
                "Vous devez saisir le prénom suivi "
                "de la longueur du bâton."
            )
            print("Exemple : samuel 15.5")
            continue

        if len(elements) > 2:
            print("\n✗ Trop d'informations ont été saisies.")
            print(
                "Le format doit être exactement : "
                "prénom longueur"
            )
            print("Le prénom ne doit pas contenir d'espace.")
            print("Exemple : samuel 15.5")
            continue

        prenom, longueur = elements

        # =============================
        # VALIDATION DU PRÉNOM
        # =============================

        prenom_valide, erreurs_prenom = valider_prenom(prenom)

        # =============================
        # VALIDATION DE LA LONGUEUR
        # =============================

        (
            longueur_valide,
            erreurs_longueur,
            longueur_convertie,
        ) = valider_longueur(longueur)

        # =============================
        # AFFICHAGE DE TOUTES LES ERREURS
        # =============================

        if not prenom_valide or not longueur_valide:

            total_erreurs = (
                len(erreurs_prenom)
                + len(erreurs_longueur)
            )

            print(
                f"\n✗ {total_erreurs} erreur"
                f"{'s' if total_erreurs > 1 else ''} "
                f"détectée"
                f"{'s' if total_erreurs > 1 else ''}."
            )

            # Erreurs du prénom
            if erreurs_prenom:
                print(
                    f"\nChamp « prénom » : "
                    f"« {prenom} »"
                )

                for numero_erreur, erreur in enumerate(
                    erreurs_prenom,
                    start=1,
                ):
                    print(
                        f"  {numero_erreur}. {erreur}"
                    )

            # Erreurs de la longueur
            if erreurs_longueur:
                print(
                    f"\nChamp « longueur du bâton » : "
                    f"« {longueur} »"
                )

                for numero_erreur, erreur in enumerate(
                    erreurs_longueur,
                    start=1,
                ):
                    print(
                        f"  {numero_erreur}. {erreur}"
                    )

            print(
                "\nVeuillez corriger les erreurs ci-dessus "
                "et ressaisir le participant."
            )

            continue

        # =============================
        # TOUT EST VALIDE
        # =============================

        print(
            f"\n✓ Prénom : « {prenom} » valide."
        )

        print(
            f"✓ Longueur du bâton : "
            f"« {longueur_convertie:g} » valide."
        )

        participant = Participant(
            prenom=prenom,
            longueur_baton=longueur_convertie,
        )

        print(
            f"\n✓ Participant « {prenom} » enregistré."
        )

        return participant


def lire_participants() -> list[Participant]:

    print("=" * 40)
    print("        COURTE PAILLE")
    print("=" * 40)
    print()

    while True:
        print("Nombre de participants")
        print("Valeur attendue : entre 10 et 100")

        try:
            saisie = input("> ")

        except EOFError:
            print("\nEntrée interrompue.")
            raise SystemExit

        except KeyboardInterrupt:
            print("\nProgramme interrompu.")
            raise SystemExit

        try:
            nombre_participants = int(saisie.strip())

        except ValueError:
            print(
                "✗ Le nombre de participants "
                "doit être un entier."
            )
            print("Exemple : 10")
            continue

        if nombre_participants < 10 or nombre_participants > 100:
            print(
                "✗ Le nombre de participants doit être compris "
                "entre 10 et 100."
            )
            continue

        print(
            f"✓ Nombre de participants valide : "
            f"{nombre_participants}"
        )

        break

    participants = []

    for numero in range(1, nombre_participants + 1):
        participant = lire_participant(numero)
        participants.append(participant)

    return participants