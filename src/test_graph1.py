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


def test_nodes_returns_list_of_extant_nodes(testing_g):
    """Test nodes method."""
    for i in range(100):
        testing_g.add_node(i)
    assert sorted(testing_g.nodes()) == [i for i in range(100)]


def test_edges_returns_list_of_extant_edges(testing_g):
    """Test nodes method."""
    test_edges = []
    for i in range(100):
        testing_g.add_node(i + 1)
        testing_g.add_node(-i - 1)
        testing_g.add_edge(i + 1, -i - 1)
        test_edges.append([i + 1, -i - 1])
    assert testing_g.edges() == test_edges


def test_has_node_returns_true_for_one_node(testing_g):
    """Test has node."""
    testing_g.add_node(1)
    assert testing_g.has_node(1) is True
