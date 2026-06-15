"""
Bloc 3 : Ségrégation et Inégalités Spatiales.
Contient les implémentations pour :
- Indice de Theil (Décomposition de l'Entropie)
- Pression Ségrégative Locale (PSL)
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


def pression_segregative_locale(heterogeneite: float, distance_sociale: float, betweenness: float, diversite: float) -> float:
    """
    Pression Ségrégative Locale (PSL).
    """
    pass
