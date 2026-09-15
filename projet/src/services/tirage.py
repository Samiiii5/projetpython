from ..models.participant import Participant


def trouver_plus_petit_baton(
    participants: list[Participant],
) -> Participant:
    participant_min = participants[0]

    for participant in participants[1:]:
        if participant.longueur_baton < participant_min.longueur_baton:
            participant_min = participant

    return participant_min

#return min(participants, key=lambda p: p.longueur_baton)