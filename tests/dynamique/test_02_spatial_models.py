"""Tests pour les formules F4, F5, F6, F28, F30."""

import numpy as np
import pytest

from atlas.features.dynamique.spatial_models import (
    decompose_indirect_effects,
    latent_spatial_model,
    multilevel_sem,
    spatial_error_model,
    spatial_gam_nonlinear,
)


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 4")
def test_latent_spatial_model():
    """Les résidus non expliqués doivent identifier les clusters sociaux cachés (GMM)."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 5")
def test_spatial_error_model(mock_spatial_matrix):
    """Le paramètre rho doit capturer la corrélation spatiale structurelle du système."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 6")
def test_multilevel_sem():
    """La variance doit se décomposer proprement entre Élève, Lycée et Zone Géographique."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 28")
def test_decompose_indirect_effects():
    """La ségrégation indirecte doit être scindée entre l'effet kilométrique (sol) et l'effet réseau (câbles)."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 30")
def test_spatial_gam_nonlinear():
    """Le modèle GAM doit prouver que l'effet d'une variable sature (effet plafond) au lieu d'être linéaire."""
    pass
