"""Fonctions spatiales et dynamiques (Socle 2).

Ces fonctions sont actuellement des squelettes (stubs) définis par l'Architecte.
Elles doivent être implémentées par les contributeurs conformément au SOCLE_2_DYNAMIQUE.md.
"""

import numpy as np


def score_propagation_segregation(s_vector: np.ndarray, w_matrix: np.ndarray) -> np.ndarray:
    """Calcule le Score de Propagation de Ségrégation (SPS) / Hotspots.
    
    Formule (SOCLE 2 - Eq 2) : SPS_i = S_i * sum_j (W_ij * S_j)
    
    Args:
        s_vector: Vecteur des scores de ségrégation locaux S_i pour chaque lycée.
        w_matrix: Matrice de pondération spatiale W_ij (ex: KNN ou contiguïté).
        
    Returns:
        Vecteur des scores SPS_i.
    """
    # Implémentation naïve (produit matriciel simple) pour passer les tests d'architecture.
    # Les contributeurs devront l'optimiser (sparse matrices, PySAL, etc.).
    return s_vector * (w_matrix @ s_vector)
