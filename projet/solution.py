from dataclasses import dataclass


@dataclass
class Participant:
	prenom: str
	longueur_baton: int


MIN_LONGUEUR_PRENOM = 5
MAX_LONGUEUR_PRENOM = 10

MIN_LONGUEUR = 1
MAX_LONGUEUR = 1000


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
) -> tuple[bool, list[str], int | None]:

	erreurs = []

	valeur = valeur.strip()

	if not valeur:
		erreurs.append(
			"La longueur du bâton ne peut pas être vide."
		)
		return False, erreurs, None

	try:
		longueur = int(valeur)

	except ValueError:
		erreurs.append(
			"La longueur du bâton doit être un nombre."
		)
		return False, erreurs, None

	# Vérification des limites
	if longueur < MIN_LONGUEUR:
		erreurs.append(
			f"La longueur doit être supérieure ou égale à "
			f"{MIN_LONGUEUR}."
		)

	if longueur > MAX_LONGUEUR:
		erreurs.append(
			f"La longueur doit être inférieure ou égale à "
			f"{MAX_LONGUEUR}."
		)

	if erreurs:
		return False, erreurs, None

	return True, [], longueur


def lire_participant(numero: int) -> Participant:

	while True:
		print("\n" + "-" * 40)
		print(f"SAISIE DU PARTICIPANT {numero}")
		print("-" * 40)

		print("Format attendu : prénom longueur")
		print("Exemple : samuel 15")

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
			print("Exemple : samuel 15")
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
			print("Exemple : samuel 15")
			continue

		if len(elements) > 2:
			print("\n✗ Trop d'informations ont été saisies.")
			print(
				"Le format doit être exactement : "
				"prénom longueur"
			)
			print("Le prénom ne doit pas contenir d'espace.")
			print("Exemple : samuel 15")
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
			f"« {longueur_convertie} » valide."
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


def trouver_plus_petit_baton(
	participants: list[Participant],
) -> Participant:
	participant_min = participants[0]

	for participant in participants[1:]:
		if participant.longueur_baton < participant_min.longueur_baton:
			participant_min = participant

	return participant_min

#return min(participants, key=lambda p: p.longueur_baton)


def main():
	participants = lire_participants()
	participant_sans_tente = trouver_plus_petit_baton(participants)
	print(participant_sans_tente.prenom)


if __name__ == "__main__":
	main()
