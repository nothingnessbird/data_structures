"""Tests for directed graph data structure."""

import pytest
import random

TEST_VALS = [random.sample(range(5000), 100) for i in range(100)]


@pytest.fixture
def testing_g():
    """Testing graph."""
    from graph_1 import Graph
    new_g = Graph()
    return new_g


@pytest.fixture(params=TEST_VALS)
def hundreds_of_nodes_no_edges_g(request):
    """Testing graph."""
    from graph_1 import Graph
    new_g = Graph()
    for i in request.param:
        new_g.add_node(i)
    return new_g


def test_empty_graph(testing_g):
    """Test that an empty initialized graph exists."""
    assert testing_g._graph == {}


def test_add_node_inits_node_with_val(testing_g):
    """Test that the add_node method inserts a node with correct val."""
    testing_g.add_node(1)
    assert testing_g.has_node(1) is True


def test_nodes_returns_empty_list_if_no_vals(testing_g):
    """Test nodes method."""
    assert testing_g.nodes() == []


def test_nodes_returns_list_of_extant_nodes(hundred_nodes_no_vals_g):
    """Test nodes method."""
    assert sorted(hundred_nodes_no_vals_g.nodes()) == [i for i in range(100)]
