"""Tests d'architecture pour le SOCLE_2_DYNAMIQUE.md (Monde B)."""

import numpy as np
import pytest

from atlas.features.spatial import score_propagation_segregation


def test_sps_hotspot_detection():
    """Le SPS doit être maximal quand un lycée ségrégué est entouré de lycées ségrégués."""
    # 3 lycées: 0 et 1 sont très ségrégués, 2 ne l'est pas du tout.
    s_vector = np.array([10.0, 10.0, 0.1])
    
    # Matrice W: le lycée 0 est voisin du 1. Le lycée 2 est isolé.
    w_matrix = np.array([
        [0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0]
    ])
    
    sps = score_propagation_segregation(s_vector, w_matrix)
    
    # Le lycée 0 (ségrégué + voisin ségrégué) doit avoir un SPS très élevé
    assert sps[0] == 100.0  # 10 * (1 * 10)
    
    # Le lycée 2 (isolé et non ségrégué) doit avoir un SPS quasi nul
    assert sps[2] < 1.0


def test_sps_no_propagation_if_neighbors_mixed():
    """Un lycée ségrégué entouré de lycées mixtes ne propage pas de ségrégation."""
    # Lycée 0 très ségrégué, mais ses voisins (1 et 2) sont parfaitement mixtes (S=0)
    s_vector = np.array([10.0, 0.0, 0.0])
    w_matrix = np.array([
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.0],
        [0.5, 0.0, 0.0]
    ])
    
    sps = score_propagation_segregation(s_vector, w_matrix)
    
    # L'effet "boule de neige" s'arrête net : le SPS de 0 tombe à zéro
    assert sps[0] == 0.0
