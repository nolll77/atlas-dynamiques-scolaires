# Tests Architecturaux : Dynamique et Réseaux

Ce répertoire contient la suite de tests garantissant l'intégrité des modèles spatiaux, graphes causaux, dynamiques temporelles et hiérarchies complexes, tel que défini dans le document fondateur [docs/SOCLE_2_DYNAMIQUE.md](../../docs/SOCLE_2_DYNAMIQUE.md).

## Philosophie : Le "Test-Driven Architecture" (TDD)

Contrairement au Socle 1 (statistique descriptive), la complexité des algorithmes du Socle 2 (Machine Learning, matrices spatiales, graphes) exige une rigueur absolue avant même l'écriture de la première ligne de code.

C'est pourquoi **les 32 formules sociologiques du Socle 2 ont déjà été traduites en 32 tests informatiques (assertions mathématiques) dans ce dossier**.

Actuellement, ces tests sont volontairement désactivés (marqués avec l'étiquette `@pytest.mark.skip`). Ils apparaissent en "jaune" (Ignorés) dans l'intégration continue (CI) de GitHub, agissant comme une feuille de route technique (*To-Do List*) pour les contributeurs.

- 👉 **Voir la preuve :** [Matrice de Couverture à 100% des Formules](MATRICE_DE_COUVERTURE_SOCLE_2.md)
- 👉 **Lire le document d'explication :** [Pourquoi les tests sont-ils Ignorés (Jaunes) ?](../README.md)

## Règle de Contribution

Pour intégrer une nouvelle brique algorithmique du Socle 2, la procédure est stricte :

1. Choisir un test ignoré dans l'un des fichiers de ce répertoire (ex: `test_identify_super_bridges` dans `test_04_networks.py`).
2. Retirer l'étiquette `@pytest.mark.skip`.
3. Coder l'implémentation de la fonction correspondante dans le dossier `src/atlas/features/dynamique/`.
4. Lancer la commande `make tests`.
5. La fonction n'est considérée comme valide et intégrable au projet que lorsque le test passe au vert, prouvant que l'algorithme respecte l'axiome sociologique.

## L'Environnement de Laboratoire (`conftest.py`)

Les algorithmes dynamiques ne peuvent pas être testés sur de simples listes de chiffres. Le fichier `conftest.py` génère automatiquement un environnement de laboratoire complet pour contraindre les algorithmes :
- **Matrices Spatiales ($W$)** : Modélisation mathématique du voisinage kilométrique.
- **Réseaux d'Adjacence** : Simulation de graphes de flux d'élèves (noeuds et arêtes).
- **Séries Temporelles** : Matrices simulant des trajectoires d'Indice de Position Sociale (IPS) sur plusieurs années.
- **Distances Ultramétriques** : Faux arbres hiérarchiques (dendrogrammes) pour éprouver les sauts de classes sociales.

## Structure des Tests

Les 32 axiomes sont classés par thématique :

- **`test_01_spatial_lag.py`** : Séparation des effets directs et de la contagion de quartier (Spatial Lag, Hotspots, Zones de bascule).
- **`test_02_spatial_models.py`** : Modèles avancés purgeant l'autocorrélation (SEM, GAM spatial, classes latentes).
- **`test_03_temporal.py`** : Causalité inter-temporelle, inertie des trajectoires et détection de ruptures (Changepoints).
- **`test_04_networks.py`** : Topologie du système, frontières infranchissables (Cut edges) et "Super-Ponts" transgressifs.
- **`test_05_clustering.py`** : Stabilité des arbres hiérarchiques et détection des zones de conflits algorithmiques.
- **`test_06_systemic.py`** : Les modèles suprêmes d'équilibre (Tipping points, hyper-ségrégation masquée, autonomie des établissements).
