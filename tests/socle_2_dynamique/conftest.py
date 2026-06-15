"""Générateurs de données de test pour la Dynamique et les Réseaux (Socle 2)."""

import numpy as np
import pytest


@pytest.fixture
def mock_spatial_matrix() -> np.ndarray:
    """Génère une matrice de voisinage (W) factice (3 lycées)."""
    return np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])


@pytest.fixture
def mock_temporal_trajectories() -> np.ndarray:
    """Génère un panel de trajectoires (3 lycées sur 5 ans)."""
    # Matrice de forme (Lycées=3, Temps=5)
    return np.array(
        [
            [150.0, 148.0, 145.0, 140.0, 135.0],  # Déclin continu
            [110.0, 115.0, 120.0, 122.0, 125.0],  # Ascension lente
            [130.0, 130.0, 130.0, 130.0, 130.0],  # Inertie absolue
        ]
    )


@pytest.fixture
def mock_adjacency_graph() -> np.ndarray:
    """Génère une matrice d'adjacence pour les réseaux (flux d'élèves)."""
    # 4 lycées, avec un "pont" entre (1) et (2)
    return np.array(
        [
            [0.0, 10.0, 0.0, 0.0],
            [10.0, 0.0, 2.0, 0.0],
            [0.0, 2.0, 0.0, 15.0],
            [0.0, 0.0, 15.0, 0.0],
        ]
    )


@pytest.fixture
def mock_ultrametric_distances() -> np.ndarray:
    """Génère une matrice de distance ultramétrique (Dendrogramme)."""
    return np.array(
        [
            [0.0, 5.0, 20.0, 20.0],
            [5.0, 0.0, 20.0, 20.0],
            [20.0, 20.0, 0.0, 3.0],
            [20.0, 20.0, 3.0, 0.0],
        ]
    )
