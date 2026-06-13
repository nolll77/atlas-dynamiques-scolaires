"""Fixtures partagées pour tous les tests."""

import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Dataset de test minimal."""
    np.random.seed(42)
    return pd.DataFrame({
        "uai": [f"UAI{i:04d}" for i in range(20)],
        "nom": [f"Lycée Test {i}" for i in range(20)],
        "ips": np.random.uniform(130, 170, 20),
        "sigma_ips": np.random.uniform(15, 35, 20),
        "secteur": ["public"] * 10 + ["prive"] * 10,
        "zone": ["Paris"] * 7 + ["PC"] * 7 + ["GC"] * 6,
        "commune": ["Paris"] * 7 + ["Neuilly"] * 4 + ["Versailles"] * 3 + ["Orsay"] * 6,
    })
