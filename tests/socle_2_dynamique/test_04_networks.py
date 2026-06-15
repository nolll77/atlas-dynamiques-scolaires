"""Tests pour les formules F12, F13, F19, F24."""

import numpy as np
import pytest

from atlas.features.dynamique.networks import (
    compute_social_corridors,
    detect_cut_edges,
    detect_ultrametric_violations,
    identify_super_bridges,
)


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 12")
def test_detect_cut_edges(mock_adjacency_graph):
    """Les ponts de fragilité (Cut Edges) doivent maximiser la Betweenness Centrality."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 13")
def test_compute_social_corridors():
    """Un corridor social doit identifier des flux d'élèves anormalement élevés entre deux mondes opposés."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 19")
def test_detect_ultrametric_violations(mock_ultrametric_distances):
    """Une arête du réseau doit être identifiée comme violation si elle relie deux branches distantes du dendrogramme."""
    pass


@pytest.mark.skip(reason="À implémenter par les contributeurs : Formule 24")
def test_identify_super_bridges():
    """Un Super-Pont doit lier deux Blocs massifs, violer l'ultramétrie, et porter un flux élevé d'élèves."""
    pass
