"""Test critique : Theil_total = Theil_between + Theil_within"""

import numpy as np
import pytest
from atlas.features.indices import theil_index


def test_theil_decomposition_additivity(sample_df):
    """La décomposition de Theil doit être additive à ±1e-6."""
    result = theil_index(sample_df, group_col="zone", value_col="ips")
    assert abs(result["total"] - result["between"] - result["within"]) < 1e-6, (
        f"Theil total={result['total']:.6f} ≠ between={result['between']:.6f} "
        f"+ within={result['within']:.6f}"
    )


def test_theil_non_negative(sample_df):
    """L'indice de Theil est toujours ≥ 0."""
    result = theil_index(sample_df, group_col="zone", value_col="ips")
    assert result["total"] >= 0
    assert result["within"] >= 0
    assert result["between"] >= 0


def test_theil_perfect_equality():
    """Theil = 0 si toutes les valeurs sont égales."""
    import pandas as pd
    df = pd.DataFrame({"zone": ["A"] * 10 + ["B"] * 10, "ips": [150.0] * 20})
    result = theil_index(df, group_col="zone", value_col="ips")
    assert abs(result["total"]) < 1e-8, f"Theil devrait être 0, obtenu {result['total']}"
