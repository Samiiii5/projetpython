import math


MIN_LONGUEUR_PRENOM = 5
MAX_LONGUEUR_PRENOM = 10

MIN_LONGUEUR = 1.0
MAX_LONGUEUR = 1000.0


def valider_prenom(prenom: str) -> tuple[bool, list[str]]:
    erreurs = []

    prenom = prenom.strip()

    if not prenom:
        erreurs.append(
            "Le prénom ne peut pas être vide."
        )
        return False, erreurs

    # Vérification de la longueur
    if len(prenom) < MIN_LONGUEUR_PRENOM:
        erreurs.append(
            f"Le prénom contient {len(prenom)} caractères. "
            f"Il doit en contenir au moins "
            f"{MIN_LONGUEUR_PRENOM}."
        )

    if len(prenom) > MAX_LONGUEUR_PRENOM:
        erreurs.append(
            f"Le prénom contient {len(prenom)} caractères. "
            f"Il ne doit pas en contenir plus de "
            f"{MAX_LONGUEUR_PRENOM}."
        )

    # Vérification des majuscules
    if any(caractere.isupper() for caractere in prenom):
        erreurs.append(
            "Le prénom doit être écrit uniquement en minuscules."
        )

    # Vérification des chiffres
    if any(caractere.isdigit() for caractere in prenom):
        erreurs.append(
            "Le prénom ne doit contenir aucun chiffre."
        )

    # Vérification des caractères spéciaux
    if any(
        not caractere.isalpha() and not caractere.isdigit()
        for caractere in prenom
    ):
        erreurs.append(
            "Le prénom ne doit contenir aucun caractère spécial "
            "ou symbole."
        )

    if erreurs:
        return False, erreurs

    return True, []


def valider_longueur(
    valeur: str,
) -> tuple[bool, list[str], float | None]:

    erreurs = []

    valeur = valeur.strip()

    if not valeur:
        erreurs.append(
            "La longueur du bâton ne peut pas être vide."
        )
        return False, erreurs, None

    # Accepte 15.5 et 15,5
    valeur = valeur.replace(",", ".")

    try:
        longueur = float(valeur)

    except ValueError:
        erreurs.append(
            "La longueur du bâton doit être un nombre."
        )
        return False, erreurs, None

    # Vérification du nombre réel
    if not math.isfinite(longueur):
        erreurs.append(
            "La longueur doit être un nombre réel valide."
        )
        return False, erreurs, None

    # Vérification des limites
    if longueur < MIN_LONGUEUR:
        erreurs.append(
            f"La longueur doit être supérieure ou égale à "
            f"{MIN_LONGUEUR:g}."
        )

    if longueur > MAX_LONGUEUR:
        erreurs.append(
            f"La longueur doit être inférieure ou égale à "
            f"{MAX_LONGUEUR:g}."
        )

    if erreurs:
        return False, erreurs, None

    return True, [], longueur