"""Formules 1, 2, 3, 14, 15 : Décalages Spatiaux et Contagion."""

import numpy as np


def compute_spatial_lag(x_vector: np.ndarray, w_matrix: np.ndarray) -> np.ndarray:
    """F1: Décomposition des Effets Directs et Indirects."""
    raise NotImplementedError("À implémenter par les contributeurs.")


def score_propagation_segregation(s_vector: np.ndarray, w_matrix: np.ndarray) -> np.ndarray:
    """F2: Score de Propagation de Ségrégation (SPS) / Hotspots."""
    raise NotImplementedError("À implémenter par les contributeurs.")


def detect_zones_bascule(beta_local: np.ndarray, beta_neighbors: np.ndarray) -> np.ndarray:
    """F3: Zones de Bascule (Effet local non-linéaire)."""
    raise NotImplementedError("À implémenter par les contributeurs.")


def compute_moran_categorical(clusters: np.ndarray, w_matrix: np.ndarray) -> float:
    """F14: Fragmentation Territoriale (Moran sur Clusters)."""
    raise NotImplementedError("À implémenter par les contributeurs.")


def compute_kde_entropy(coords: np.ndarray, clusters: np.ndarray) -> np.ndarray:
    """F15: Frontières Sociales Floues (Gradient KDE & Entropie)."""
    raise NotImplementedError("À implémenter par les contributeurs.")
