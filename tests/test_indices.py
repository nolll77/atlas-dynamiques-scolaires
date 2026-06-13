"""Tests pour les indices de ségrégation."""

import numpy as np
import pytest
from atlas.features.indices import gini_index, entre_soi_score


def test_gini_perfect_equality():
    """Gini = 0 pour distribution uniforme."""
    values = np.ones(100) * 150.0
    assert abs(gini_index(values)) < 1e-10


def test_gini_range():
    """Gini est dans [0, 1)."""
    values = np.random.uniform(100, 200, 50)
    g = gini_index(values)
    assert 0 <= g < 1


def test_entre_soi_high_ips_low_sigma():
    """Score entre-soi élevé si IPS haut ET sigma faible."""
    score_elite = entre_soi_score(
        ips=165, sigma=15,
        ips_mean=150, ips_std=10,
        sigma_mean=25, sigma_std=5
    )
    score_open = entre_soi_score(
        ips=145, sigma=35,
        ips_mean=150, ips_std=10,
        sigma_mean=25, sigma_std=5
    )
    assert score_elite > score_open
