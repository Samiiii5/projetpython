# Projet de groupe Python

## Objectif

Le projet simule un tirage à la courte paille : chaque participant saisit son prénom et la longueur de son bâton. Le programme recherche ensuite le participant qui possède le bâton le plus court.

## Arborescence actuelle

```text
projet/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── participant.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── tirage.py
│   └── input_output/
│       ├── __init__.py
│       ├── input_reader.py
│       └── validator.py
├── tests/
│   ├── __init__.py
│   ├── test_tirage.py
│   └── test_input_reader.py
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
└── test_main.py
```

## Rôle de chaque fichier

### Dossier `src/`

- `src/__init__.py` : transforme `src` en package Python.
- `src/main.py` : point d'entrée de l'application. Il récupère les participants, lance le tirage et affiche le résultat.

### Dossier `src/models/`

- `src/models/__init__.py` : initialise le package des modèles.
- `src/models/participant.py` : définit la classe `Participant` avec deux attributs : `prenom` et `longueur_baton`.

### Dossier `src/services/`

- `src/services/__init__.py` : initialise le package des services.
- `src/services/tirage.py` : contient `trouver_plus_petit_baton`, qui recherche le participant dont le bâton est le plus court.

### Dossier `src/input_output/`

- `src/input_output/__init__.py` : initialise le package de lecture et de validation des entrées.
- `src/input_output/input_reader.py` : demande le nombre de participants et les informations de chaque participant. Il répète la saisie tant que les données sont invalides.
- `src/input_output/validator.py` : valide les prénoms et les longueurs de bâton saisies.

### Dossier `tests/`

- `tests/__init__.py` : transforme `tests` en package Python.
- `tests/test_tirage.py` : vérifie la recherche du bâton le plus court dans plusieurs positions et avec différentes valeurs.
- `tests/test_input_reader.py` : vérifie la validation des saisies, notamment les virgules décimales, les caractères invalides et les informations manquantes ou en trop.

### Fichiers racine

- `README.md` : documentation et repère du projet.
- `requirements.txt` : liste des dépendances Python externes. Elle est actuellement vide, car le projet utilise uniquement la bibliothèque standard.
- `.gitignore` : liste des fichiers qui ne doivent pas être suivis par Git. Il peut notamment contenir les caches Python et les environnements virtuels.
- `main.py` : ancien fichier racine conservé lors du changement d'arborescence. Le point d'entrée actuel est `src/main.py`.
- `test_main.py` : ancien fichier de test racine conservé lors du changement d'arborescence. Les tests actuels se trouvent dans `tests/`.

## Fonctionnement du programme

1. `src/main.py` appelle `lire_participants`.
2. `input_reader.py` demande entre 10 et 100 participants.
3. Chaque saisie est contrôlée par `validator.py`.
4. Les participants valides sont créés avec le modèle `Participant`.
5. `tirage.py` trouve le bâton le plus court.
6. `src/main.py` affiche le prénom du participant qui dormira sans tente.

## Lancer le programme

Depuis le dossier `projet`, exécuter :

```bash
python -m src.main
```

## Lancer les tests

Depuis le dossier `projet`, exécuter :

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Les tests peuvent aussi être lancés avec `pytest` si cet outil est installé :

```bash
pytest
```
