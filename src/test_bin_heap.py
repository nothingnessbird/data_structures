"""Tests for binary heap."""

import pytest


@pytest.fixture
def empty_heap():
    """Empty list for testing."""
    from bin_heap import Heap
    new_heap = Heap()
    return new_heap


def test_if_heap_init_with_no_iterable_works(empty_heap):
    """Test for empty heap instance."""
    assert empty_heap._heap_list == []


def test_if_heap_init_with_iterable_works():
    """Test for initialized with iterable."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter, 'min')
    assert new_heap._heap_list == [1, 5, 4, 20, 12, 15]


def test_pushing_to_empty_heap(empty_heap):
    """Test pushing a value to an empty heap."""
    test_val = 1
    empty_heap.push(test_val)
    assert empty_heap._heap_list == [1]
