"""Tests for priority queue data structure."""

import pytest


@pytest.fixture
def empty_pq():
    """Empty priority queue for testing."""
    from priorityq import PriorityQ
    new_pq = PriorityQ()
    return new_pq


def test_init_empty_pq(empty_pq):
    """Test that empty pq initializes."""
    assert empty_pq._list == [[] for x in range(100)]
