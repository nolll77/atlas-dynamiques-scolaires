"""Tests pour le Bloc 0 : Statistiques Exploratoires."""

import pytest

from atlas.features.mathematiques.statistiques import entre_soi_score


def test_entre_soi_high_ips_low_sigma():
    """Score entre-soi élevé si IPS haut ET sigma faible."""
    score_elite = entre_soi_score(
        ips=165, sigma=15, ips_mean=150, ips_std=10, sigma_mean=25, sigma_std=5
    )
    score_open = entre_soi_score(
        ips=145, sigma=35, ips_mean=150, ips_std=10, sigma_mean=25, sigma_std=5
    )
    assert score_elite > score_open


@pytest.mark.skip(reason="À implémenter")
def test_normalisation_z_score():
    """Test de Normalisation (Z-Score)"""
    pass


@pytest.mark.skip(reason="À implémenter")
def test_distance_mahalanobis():
    """Test de Distance de Mahalanobis"""
    pass


@pytest.mark.skip(reason="À implémenter")
def test_indice_dissimilarite_duncan():
    """Test de Indice de Dissimilarité de Duncan"""
    pass


@pytest.mark.skip(reason="À implémenter")
def test_indice_fragmentation():
    """Test de Indice de Fragmentation par Établissement (F_i)"""
    pass
