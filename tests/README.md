# Tests et Validation Scientifique

Ce dossier contient les tests automatisés du projet. Ces tests constituent la traduction directe du cadre sociologique et mathématique de l'Atlas en "barrières de sécurité" informatiques.

Tant que l'ensemble de ces tests est validé ("vert"), cela garantit que le code développé respecte strictement la théorie définie dans la documentation.

## Pourquoi est-ce fondamental ?

L'exécution des tests (via la commande `make tests`) assure l'intégrité scientifique de l'Atlas. Si une modification du code altère accidentelement le calcul d'un indicateur, la commande signalera immédiatement une erreur. Cela permet à chaque contributeur de vérifier la justesse mathématique de ses développements avant l'ouverture d'une *Pull Request*.

En règle générale, aucune contribution logicielle ne sera intégrée à l'Atlas si la vérification mathématique automatisée n'a pas été préalablement validée.

## Que fait la commande `make tests` ?

1. Elle initialise l'environnement de test via la bibliothèque `pytest`.
2. Elle exécute les algorithmes et les formules mathématiques du projet en utilisant des jeux de données fictifs et contrôlés.
3. Elle vérifie que les résultats générés par le code correspondent *exactement* aux axiomes théoriques définis dans le document fondateur [docs/SOCLE_1_MATHEMATIQUES.md](../docs/SOCLE_1_MATHEMATIQUES.md).

## Structure des tests

Voici la fonction des trois fichiers fondamentaux de l'environnement de test :

### `conftest.py` (L'échantillon de contrôle)
Il génère un jeu de données fictif (par exemple une vingtaine d'établissements de test) en attribuant des indices de position sociale (IPS) et des variances (`sigma_ips`) aléatoires. Il répartit ensuite ces entités entre différents secteurs (public/privé) et zones géographiques. Ce fichier sert de terrain neutre pour éprouver les équations.

### `test_theil_decomposition.py` (La vérification du socle)
Ce module applique la formule de l'Indice de Theil sur les données générées et vérifie l'invariabilité de sa loi de décomposition : `Théil Total = Théil Intra + Théil Inter`. Le test requiert une précision mathématique stricte, avec une tolérance d'erreur infinitésimale (inférieure à `1e-6`). Toute altération de cette égalité entraîne l'échec du test.

### `test_indices.py` (La cohérence sociologique)
Il vérifie le comportement des scores composites. Il comporte notamment une vérification (`test_entre_soi_high_ips_low_sigma`) garantissant que la fonction du *Score d'Entre-soi* attribue une valeur structurellement plus élevée à une configuration de type "homogénéité d'élite" (IPS très élevé couplé à une variance quasi nulle) comparativement à une configuration hétérogène (IPS moyen et forte diversité interne).
