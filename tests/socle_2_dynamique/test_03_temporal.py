"""Tests pour les formules F7, F8, F9, F26, F29."""

import pytest


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 7")
def test_temporal_dag_causality(mock_temporal_trajectories, mock_spatial_matrix):
    """Y(t) dépend causalement de Y(t-1) et du W*Y(t-1) des voisins."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 8")
def test_sankey_cluster_trajectories():
    """Matrice Sankey identifie entropie de mobilité entre mondes."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 9")
def test_detect_temporal_changepoints():
    """Rupture structurelle déclenche changepoint de forte magnitude."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 26")
def test_compute_mobility_drift():
    """La mobilité scolaire est inerte et path-dependent."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 29")
def test_analyze_hotspot_causality():
    """Asymétrie temporelle de Granger : qui contamine qui ?"""
    pass
