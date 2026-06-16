# Matrice de Couverture : Socle 1 (Mathématiques)

Ce document prouve que **100% des 31 formules** définies dans le manifeste [SOCLE_1_MATHEMATIQUES.md](../../docs/SOCLE_1_MATHEMATIQUES.md) sont couvertes par un test d'architecture (ignorable par défaut s'il n'est pas encore implémenté).

## Bloc 0 : Statistiques Exploratoires
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Normalisation (Z-Score) | `test_00_statistiques.py` | `test_normalisation_z_score` | ⚠️ Skipped |
| Indice d'Entre-Soi | `test_00_statistiques.py` | `test_entre_soi_high_ips_low_sigma` | ⚠️ Skipped |
| Distance de Mahalanobis | `test_00_statistiques.py` | `test_distance_mahalanobis` | ⚠️ Skipped |
| Indice de Duncan | `test_00_statistiques.py` | `test_indice_dissimilarite_duncan` | ⚠️ Skipped |
| Fragmentation par Établissement | `test_00_statistiques.py` | `test_indice_fragmentation` | ⚠️ Skipped |

## Bloc 1 : Topologie et Distances
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Distance Ultramétrique | `test_01_topologie.py` | `test_distance_ultrametrique` | ⚠️ Skipped |
| Distance Sociale (W_ij) | `test_01_topologie.py` | `test_distance_sociale_similarite` | ⚠️ Skipped |

## Bloc 2 : Théorie des Réseaux et Graphes
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Modularité (Louvain) | `test_02_graphes.py` | `test_modularite_louvain` | ⚠️ Skipped |
| Centralité (Betweenness) | `test_02_graphes.py` | `test_centralite_intermediarite` | ⚠️ Skipped |
| Tension Hiérarchie/Réseau | `test_02_graphes.py` | `test_tension_hierarchie_reseau` | ⚠️ Skipped |

## Bloc 3 : Ségrégation et Inégalités Spatiales
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Indice de Theil | `test_03_segregation.py` | `test_theil_decomposition_additivity` | ⚠️ Skipped |
| Pression Ségrégative (PSL) | `test_03_segregation.py` | `test_pression_segregative_locale` | ⚠️ Skipped |

## Bloc 4 : Modèles Causaux Spatiaux
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Spatial Autoregressive (SAR) | `test_04_econometrie.py` | `test_sar_model` | ⚠️ Skipped |
| Effets Marginaux Spatiaux | `test_04_econometrie.py` | `test_effets_marginaux_spatiaux` | ⚠️ Skipped |

## Bloc 5 : Algorithmique et Seuils
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Critère de Mojena | `test_05_algorithmique.py` | `test_critere_mojena` | ⚠️ Skipped |

## Bloc 6 : Analyse des Résidus et Modèles Causaux
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Résidus Spatiaux | `test_06_modeles_causaux.py` | `test_residus_spatiaux` | ⚠️ Skipped |
| Inférence Causale (DAG) | `test_06_modeles_causaux.py` | `test_inference_causale_graphes` | ⚠️ Skipped |

## Bloc 7 : Dynamique et Topologie Spatiale
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Entropie Transition (CAH) | `test_07_topologie_spatiale.py` | `test_entropie_transition_cah` | ⚠️ Skipped |
| CAH Contrainte | `test_07_topologie_spatiale.py` | `test_cah_contrainte` | ⚠️ Skipped |
| Densité Sociale (KDE) | `test_07_topologie_spatiale.py` | `test_densite_continuite_sociale` | ⚠️ Skipped |

## Bloc 8 : Validation Structurelle des Clusters
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Silhouette Score | `test_08_validation.py` | `test_silhouette_score` | ⚠️ Skipped |
| Gap Statistic | `test_08_validation.py` | `test_gap_statistic` | ⚠️ Skipped |

## Bloc 9 : Fractures et Tensions Structurelles
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Tension Ultramétrique Locale | `test_09_tensions.py` | `test_tension_ultrametrique_reseau` | ⚠️ Skipped |

## Bloc 10 : Modèles Markoviens
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Matrice de Transition | `test_10_markov.py` | `test_matrice_transition` | ⚠️ Skipped |
| Distribution Stationnaire | `test_10_markov.py` | `test_distribution_stationnaire` | ⚠️ Skipped |
| Centralité de Transition | `test_10_markov.py` | `test_centralite_transition` | ⚠️ Skipped |
| Entropie Vitesse Mobilité | `test_10_markov.py` | `test_entropie_transition_flux` | ⚠️ Skipped |

## Bloc 11 : Réseaux Multiplexes
| Formule Théorique | Fichier de Test | Fonction de Test | Statut Actuel |
| :--- | :--- | :--- | :--- |
| Flux entre Couches (F_ab) | `test_11_multiplexes.py` | `test_flux_entre_couches` | ⚠️ Skipped |
| IFC (Perméabilité) | `test_11_multiplexes.py` | `test_indice_fragmentation_inter_couches` | ⚠️ Skipped |
| IFC Pondéré | `test_11_multiplexes.py` | `test_ifc_pondere` | ⚠️ Skipped |
| Asymétrie des Flux | `test_11_multiplexes.py` | `test_asymetrie_flux` | ⚠️ Skipped |
| Entropie Globale des Flux | `test_11_multiplexes.py` | `test_entropie_globale_flux` | ⚠️ Skipped |
