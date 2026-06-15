"""Tests pour les formules F1, F2, F3, F14, F15."""

import pytest


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 1")
def test_spatial_lag_separation(mock_spatial_matrix):
    """Le modèle sépare proprement l'effet direct (X_i) de contagion (W_ij X_j)."""
    # Test stub condition
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 2")
def test_score_propagation_segregation_hotspot(mock_spatial_matrix):
    """Un lycée ségrégué entouré de voisins ségrégués doit avoir un SPS maximal."""
    # Test stub condition
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 3")
def test_detect_zones_bascule(mock_spatial_matrix):
    """La zone de bascule s'active quand le gradient local s'inverse vs voisins."""
    # Test stub condition
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 14")
def test_moran_categorical(mock_spatial_matrix):
    """L'Indice de Moran détecte la fragmentation si les clusters sont compactés."""
    # Test stub condition
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 15")
def test_kde_entropy():
    """Entropie maximale aux frontières entre deux clusters socio-géographiques."""
    # Test stub condition
    pass
