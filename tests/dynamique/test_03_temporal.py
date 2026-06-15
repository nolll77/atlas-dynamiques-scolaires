"""Tests pour les formules F7, F8, F9, F26, F29."""

import numpy as np
import pytest

from atlas.features.dynamique.temporal import (
    analyze_hotspot_causality,
    compute_mobility_drift,
    detect_temporal_changepoints,
    sankey_cluster_trajectories,
    temporal_dag_causality,
)


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 7")
def test_temporal_dag_causality(mock_temporal_trajectories, mock_spatial_matrix):
    """L'état Y(t) d'un lycée doit dépendre causalement de son Y(t-1) et du W*Y(t-1) de ses voisins."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 8")
def test_sankey_cluster_trajectories():
    """La matrice de transition (Sankey) doit identifier l'entropie de mobilité entre mondes sociaux."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 9")
def test_detect_temporal_changepoints():
    """Une rupture structurelle (ex: réforme) doit déclencher un changepoint de forte magnitude (ARI faible)."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 26")
def test_compute_mobility_drift():
    """Le modèle doit prouver que la mobilité scolaire (tuyauterie) est inerte et path-dependent."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 29")
def test_analyze_hotspot_causality():
    """Une asymétrie temporelle de Granger doit prouver si le hotspot contamine ou est contaminé."""
    pass
