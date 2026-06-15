# Matrice de Couverture : Socle 2 Dynamique

Ce document prouve la traçabilité complète et la couverture à 100% entre les exigences théoriques de l'Atlas et leur implémentation informatique. Chaque formule du `SOCLE_2_DYNAMIQUE.md` possède son "Test Architectural" dédié, interdisant toute déviation par rapport à la théorie.

| N° | Formule Sociologique (Socle 2) | Fichier Source (Squelette) | Test Architectural (Validation) | Statut Actuel |
|:---|:---|:---|:---|:---|
| **F1** | Décomposition des Effets Directs/Indirects | `spatial_lag.py` | `test_01_spatial_lag.py::test_spatial_lag_separation` | ⚠️ Skipped |
| **F2** | Score Propagation Ségrégation (SPS) | `spatial_lag.py` | `test_01_spatial_lag.py::test_score_propagation_segregation_hotspot` | ⚠️ Skipped |
| **F3** | Zones de Bascule (Gradient spatial) | `spatial_lag.py` | `test_01_spatial_lag.py::test_detect_zones_bascule` | ⚠️ Skipped |
| **F4** | Modèle Latent Spatial (Résidus) | `spatial_models.py` | `test_02_spatial_models.py::test_latent_spatial_model` | ⚠️ Skipped |
| **F5** | Modèle d'Équations Structurelles Spatial (SEM) | `spatial_models.py` | `test_02_spatial_models.py::test_spatial_error_model` | ⚠️ Skipped |
| **F6** | SEM Spatial Multi-Niveaux | `spatial_models.py` | `test_02_spatial_models.py::test_multilevel_sem` | ⚠️ Skipped |
| **F7** | Graphe Causal Inter-Temporel (DAG) | `temporal.py` | `test_03_temporal.py::test_temporal_dag_causality` | ⚠️ Skipped |
| **F8** | Trajectoires de Clusters (Sankey) | `temporal.py` | `test_03_temporal.py::test_sankey_cluster_trajectories` | ⚠️ Skipped |
| **F9** | Ruptures Structurelles (Changepoints) | `temporal.py` | `test_03_temporal.py::test_detect_temporal_changepoints` | ⚠️ Skipped |
| **F10** | Ultramétrie Temporelle | `clustering.py` | `test_05_clustering.py::test_temporal_ultrametric_stability` | ⚠️ Skipped |
| **F11** | Simulation Mobilité Sociale | `systemic.py` | `test_06_systemic.py::test_simulate_social_mobility` | ⚠️ Skipped |
| **F12** | Frontières Scolaires Dures (Cut Edges) | `networks.py` | `test_04_networks.py::test_detect_cut_edges` | ⚠️ Skipped |
| **F13** | Corridors Sociaux | `networks.py` | `test_04_networks.py::test_compute_social_corridors` | ⚠️ Skipped |
| **F14** | Fragmentation Territoriale (Moran) | `spatial_lag.py` | `test_01_spatial_lag.py::test_moran_categorical` | ⚠️ Skipped |
| **F15** | Frontières Floues (KDE Entropie) | `spatial_lag.py` | `test_01_spatial_lag.py::test_kde_entropy` | ⚠️ Skipped |
| **F16** | Indice d'Accord des 3 Critères | `systemic.py` | `test_06_systemic.py::test_structural_coherence_index` | ⚠️ Skipped |
| **F17** | K Optimal Consensuel | `clustering.py` | `test_05_clustering.py::test_find_optimal_k_consensus` | ⚠️ Skipped |
| **F18** | Divergences Algorithmiques | `clustering.py` | `test_05_clustering.py::test_compute_algorithmic_divergence` | ⚠️ Skipped |
| **F19** | Validation Ultramétrique | `networks.py` | `test_04_networks.py::test_detect_ultrametric_violations` | ⚠️ Skipped |
| **F20** | Modèle Unifié Super-Goulots | `systemic.py` | `test_06_systemic.py::test_unified_super_bottlenecks` | ⚠️ Skipped |
| **F21** | Perméabilité Structurelle Optimale | `systemic.py` | `test_06_systemic.py::test_optimal_structural_permeability` | ⚠️ Skipped |
| **F22** | Modèle Causal IFC | `systemic.py` | `test_06_systemic.py::test_causal_fragmentation_model` | ⚠️ Skipped |
| **F23** | Détection Blocs Multi-Couches | `clustering.py` | `test_05_clustering.py::test_detect_multilayer_blocks` | ⚠️ Skipped |
| **F24** | Super-Ponts Inter-Blocs | `networks.py` | `test_04_networks.py::test_identify_super_bridges` | ⚠️ Skipped |
| **F25** | Hyper-ségrégation Masquée | `systemic.py` | `test_06_systemic.py::test_detect_masked_hypersegregation` | ⚠️ Skipped |
| **F26** | Dérive Temporelle Mobilité | `temporal.py` | `test_03_temporal.py::test_compute_mobility_drift` | ⚠️ Skipped |
| **F27** | Indice d'Autonomie Scolaire (IAS) | `systemic.py` | `test_06_systemic.py::test_compute_school_autonomy_index` | ⚠️ Skipped |
| **F28** | Décomposition Indirecte (Quartier/Réseau) | `spatial_models.py` | `test_02_spatial_models.py::test_decompose_indirect_effects` | ⚠️ Skipped |
| **F29** | Causalité des Hotspots | `temporal.py` | `test_03_temporal.py::test_analyze_hotspot_causality` | ⚠️ Skipped |
| **F30** | GAM Spatial Non-Linéaire | `spatial_models.py` | `test_02_spatial_models.py::test_spatial_gam_nonlinear` | ⚠️ Skipped |
| **F31** | Tipping Points Instabilité | `systemic.py` | `test_06_systemic.py::test_detect_tipping_points` | ⚠️ Skipped |
| **F32** | Classification Mondes Latents | `clustering.py` | `test_05_clustering.py::test_latent_class_worlds` | ⚠️ Skipped |

## Lecture de la matrice

Si un contributeur souhaite implémenter l'analyse de l'**Hyper-ségrégation Masquée (F25)** :
1. Il doit consulter la théorie dans le socle (Formule 25).
2. Il écrit le code dans le fichier `src/atlas/features/dynamique/systemic.py` (à la place de l'erreur `NotImplementedError`).
3. Il active et passe avec succès le test `test_detect_masked_hypersegregation` situé dans `tests/dynamique/test_06_systemic.py`.

La boucle est ainsi parfaitement bouclée entre le monde sociologique et le monde informatique.
