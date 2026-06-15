"""Tests pour les formules F10, F17, F18, F23, F32."""

import numpy as np
import pytest

from atlas.features.dynamique.clustering import (
    compute_algorithmic_divergence,
    detect_multilayer_blocks,
    find_optimal_k_consensus,
    latent_class_worlds,
    temporal_ultrametric_stability,
)


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 10")
def test_temporal_ultrametric_stability():
    """La hiérarchie (arbre) doit être figée (U=1) si la distance sociale entre élite et populaire ne change pas."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 17")
def test_find_optimal_k_consensus():
    """Le nombre K optimal doit être un consensus entre Silhouette, Gap Statistic, et Stabilité Bootstrap."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 18")
def test_compute_algorithmic_divergence():
    """Les lycées classés différemment par KMeans, CAH et Louvain doivent avoir une entropie maximale (Zones grises)."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 23")
def test_detect_multilayer_blocks():
    """Un continent social (Bloc) doit maximiser la similarité d'IPS ET la densité des flux (corridors)."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 32")
def test_latent_class_worlds():
    """Les modèles mixtes latents (LCMM) doivent prouver que l'IPS agit différemment selon le 'Monde' du lycée."""
    pass
