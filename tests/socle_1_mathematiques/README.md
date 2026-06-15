# Tests Architecturaux : Socle 1 (Mathématiques)

Ce répertoire contient la suite de tests garantissant l'intégrité du **Socle 1 (Mathématiques et Statistiques)**, tel que défini dans le document fondateur [docs/SOCLE_1_MATHEMATIQUES.md](../../docs/SOCLE_1_MATHEMATIQUES.md).

## Philosophie : Le "Test-Driven Architecture" (TDD)

Afin de garantir que l'ensemble des 31 formules théoriques ne soient pas oubliées lors du développement, nous avons traduit ces équations en tests informatiques (assertions mathématiques) répartis dans 12 fichiers logiques.

Actuellement, la vaste majorité de ces tests sont volontairement désactivés (marqués avec l'étiquette `@pytest.mark.skip`). Ils apparaissent en "jaune" (Ignorés) dans l'intégration continue (CI) de GitHub, agissant comme une feuille de route technique (*To-Do List*) pour les contributeurs.

- 👉 **Voir la preuve :** [Matrice de Couverture à 100% des Formules](MATRICE_DE_COUVERTURE_SOCLE_1.md)
- 👉 **Lire le document d'explication :** [Pourquoi les tests sont-ils Ignorés (Jaunes) ?](../README.md)

## Organisation des tests

Les tests sont structurés selon les 12 blocs du Manifeste Mathématique :

- `test_00_statistiques.py` : Base statistique et normalisation
- `test_01_topologie.py` : Algèbre des distances
- `test_02_graphes.py` : Théorie des réseaux et algorithme de Louvain
- `test_03_segregation.py` : Indices macroscopiques (Gini, Theil, PSL)
- `test_04_econometrie.py` : Régressions spatiales
- `test_05_algorithmique.py` : Méthodes de coupe (Mojena)
- `test_06_modeles_causaux.py` : Inférence et causalité avancée
- `test_07_topologie_spatiale.py` : Déformations spatiales
- `test_08_validation.py` : Métriques de cohérence structurelle
- `test_09_tensions.py` : Points de rupture dans les graphes
- `test_10_markov.py` : Transitions et probabilités de flux
- `test_11_multiplexes.py` : Matrices avancées sur la perméabilité sociale
