"""Tests pour le Bloc 3 : Ségrégation et Inégalités Spatiales."""
import pytest
import numpy as np
import pandas as pd
from atlas.features.mathematiques.segregation import theil_index, gini_index

def test_gini_perfect_equality():
    """Gini = 0 pour distribution uniforme."""
    values = np.ones(100) * 150.0
    assert abs(gini_index(values)) < 1e-10

def test_gini_range():
    """Gini est dans [0, 1)."""
    values = np.random.uniform(100, 200, 50)
    g = gini_index(values)
    assert 0 <= g < 1

def test_theil_decomposition_additivity(sample_df):
    """La décomposition de Theil doit être additive à ±1e-6."""
    result = theil_index(sample_df, group_col="zone", value_col="ips")
    diff = abs(result["total"] - result["between"] - result["within"])
    assert diff < 1e-6, f"Mismatch Theil: {diff}"

def test_theil_non_negative(sample_df):
    """L'indice de Theil est toujours ≥ 0."""
    result = theil_index(sample_df, group_col="zone", value_col="ips")
    assert result["total"] >= 0
    assert result["within"] >= 0
    assert result["between"] >= 0

def test_theil_perfect_equality():
    """Theil = 0 si toutes les valeurs sont égales."""
    df = pd.DataFrame({"zone": ["A"] * 10 + ["B"] * 10, "ips": [150.0] * 20})
    result = theil_index(df, group_col="zone", value_col="ips")
    assert abs(result["total"]) < 1e-8, f"Erreur Theil: {result['total']}"

@pytest.mark.skip(reason="À implémenter")
def test_pression_segregative_locale():
    """Test de Pression Ségrégative Locale (PSL)"""
    pass
