from .input_output.input_reader import lire_participants
from .services.tirage import trouver_plus_petit_baton


def main():
    participants = lire_participants()
    participant_sans_tente = trouver_plus_petit_baton(participants)
    print(f"la personne qui dormira sans tente est {participant_sans_tente.prenom}")


if __name__ == "__main__":
    main()