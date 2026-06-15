"""Tests pour les formules F11, F16, F20, F21, F22, F25, F27, F31."""

import numpy as np
import pytest

from atlas.features.dynamique.systemic import (
    causal_fragmentation_model,
    compute_school_autonomy_index,
    detect_masked_hypersegregation,
    detect_tipping_points,
    optimal_structural_permeability,
    simulate_social_mobility,
    structural_coherence_index,
    unified_super_bottlenecks,
)


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 11")
def test_simulate_social_mobility():
    """La vitesse d'ascension sociale d'un lycée doit être freinée par l'effet de gravité de son quartier."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 16")
def test_structural_coherence_index():
    """Un lycée paradoxal (ex: IPS faible mais forte attractivité) doit avoir une faible cohérence structurelle."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 20")
def test_unified_super_bottlenecks():
    """Le Super-Goulot doit être le seul point d'intersection des modèles HMM, GNN, Hiérarchiques et Causaux."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 21")
def test_optimal_structural_permeability():
    """L'optimum systémique doit équilibrer la mobilité des élèves avec la lisibilité hiérarchique de l'arbre."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 22")
def test_causal_fragmentation_model():
    """L'IFC doit être la conséquence modélisée de la sélectivité causale des établissements."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 25")
def test_detect_masked_hypersegregation():
    """L'hyper-ségrégation est maximale quand la variance d'IPS d'une ville est grande, mais la variance intra-lycée est nulle."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 27")
def test_compute_school_autonomy_index():
    """L'Indice d'Autonomie (IAS) doit isoler les lycées s'affranchissant du poids de la démographie locale."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 31")
def test_detect_tipping_points():
    """Le système est instable si le basculement d'un lycée résonne sur l'ensemble du réseau spatial."""
    pass
