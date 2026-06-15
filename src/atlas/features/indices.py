"""
Indices de ségrégation scolaire.

⚠️ IMPORTANT : Ces indices mesurent des associations statistiques.
Ils ne démontrent pas de causalité. Voir docs/CAUSALITY_LIMITS.md
"""

import numpy as np
import pandas as pd


def gini_index(values: np.ndarray) -> float:
    """Indice de Gini. Valeur 0 = égalité parfaite, 1 = inégalité maximale."""
    values = np.sort(np.asarray(values, dtype=float))
    n = len(values)
    index = np.arange(1, n + 1)
    return (2 * np.sum(index * values) / (n * np.sum(values))) - (n + 1) / n


def theil_index(df: pd.DataFrame, group_col: str, value_col: str) -> dict:
    """
    Indice de Theil avec décomposition within/between.

    Returns:
        dict: total, within, between, ratio_within, ratio_between
    """
    values = df[value_col].values
    mu = np.mean(values)
    n = len(values)

    total = np.sum((values / mu) * np.log(values / mu)) / n

    groups = df.groupby(group_col)[value_col]
    within = 0.0
    between = 0.0

    for _, group_values in groups:
        nk = len(group_values)
        mu_k = np.mean(group_values)
        weight = nk / n
        # Within
        within += (
            weight
            * (mu_k / mu)
            * np.sum((group_values / mu_k) * np.log(group_values / mu_k))
            / nk
        )
        # Between
        between += weight * (mu_k / mu) * np.log(mu_k / mu)

    return {
        "total": total,
        "within": within,
        "between": between,
        "ratio_within": within / total if total > 0 else 0,
        "ratio_between": between / total if total > 0 else 0,
    }


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
