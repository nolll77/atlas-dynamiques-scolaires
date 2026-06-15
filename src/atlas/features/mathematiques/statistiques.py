"""
Bloc 0 : Statistiques Exploratoires.
Contient les implémentations pour :
- Normalisation (Z-Score) et Indice d'Entre-Soi
- Distance de Mahalanobis
- Indice de Dissimilarité de Duncan
- Indice de Fragmentation par Établissement
"""

import numpy as np
import pandas as pd


def entre_soi_score(
    ips: float,
    sigma: float,
    ips_mean: float,
    ips_std: float,
    sigma_mean: float,
    sigma_std: float,
) -> float:
    """Score d'entre-soi : IPS élevé + σ faible = entre-soi fort."""
    z_ips = (ips - ips_mean) / ips_std
    z_sigma = (sigma - sigma_mean) / sigma_std
    return z_ips - z_sigma


def duncan_dissimilarity(
    df: pd.DataFrame, area_col: str, group_col: str, value_col: str
) -> float:
    """Indice de dissimilarité de Duncan D."""
    groups = df.groupby([area_col, group_col])[value_col].sum().unstack(fill_value=0)
    if groups.shape[1] < 2:
        return 0.0
    col_a, col_b = groups.columns[0], groups.columns[1]
    total_a = groups[col_a].sum()
    total_b = groups[col_b].sum()
    return 0.5 * np.sum(np.abs(groups[col_a] / total_a - groups[col_b] / total_b))


def distance_mahalanobis(
    x: np.ndarray, mu: np.ndarray, cov_inv: np.ndarray
) -> np.ndarray:
    """
    Distance de Mahalanobis.
    """
    pass


def indice_fragmentation(
    betweenness: float, duncan: float, var_contribution: float, rupture: float
) -> float:
    """
    Indice de Fragmentation par Établissement (F_i).
    """
    pass
