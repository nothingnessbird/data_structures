"""Tests for binary heap."""

import pytest


@pytest.fixture
def empty_heap():
    """Empty heap for testing."""
    from bin_heap import Heap
    new_heap = Heap()
    return new_heap


def test_if_heap_init_with_no_iterable_works(empty_heap):
    """Test for empty heap instance."""
    assert empty_heap._heap_list == []


def test_if_heap_init_with_iterable_works_for_default_max_heap():
    """Test for maxheap initialized with iterable."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter)
    assert new_heap._heap_list == [20, 12, 15, 1, 5, 4]


def test_if_heap_init_with_iterable_works_for_min_heap():
    """Test for minheap initialized with iterable."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter, 'min')
    assert new_heap._heap_list == [1, 5, 4, 20, 12, 15]


def test_pushing_to_empty_heap(empty_heap):
    """Test pushing a value to an empty heap."""
    test_val = 1
    empty_heap.push(test_val)
    assert empty_heap._heap_list == [1]


def test_pushing_to_full_max_heap():
    """Test that push works for an already built maxheap."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter)
    new_heap.push(16)
    assert new_heap._heap_list == [20, 12, 16, 1, 5, 4, 15]


def test_pushing_to_full_min_heap():
    """Test that push works for an already built minheap."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter, 'min')
    new_heap.push(2)
    assert new_heap._heap_list == [1, 5, 2, 20, 12, 15, 4]


def test_popping_from_max_heap_returns_correct_value():
    """Test that pop returns correct value on a maxheap."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter)
    popped_val = new_heap.pop()
    assert popped_val == 20


def test_popping_from_max_heap():
    """Test that pop works on a maxheap."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter)
    new_heap.pop()
    assert new_heap._heap_list == [15, 5, 12, 1, 4]


def test_popping_from_min_heap_returns_correct_value():
    """Test that pop returns correct value on a minheap."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter, 'min')
    popped_val = new_heap.pop()
    assert popped_val == 1


def test_popping_from_min_heap():
    """Test that pop works on a minheap."""
    from bin_heap import Heap
    test_iter = [1, 20, 4, 5, 12, 15]
    new_heap = Heap(test_iter, 'min')
    new_heap.pop()
    assert new_heap._heap_list == [4, 12, 5, 20, 15]


def test_value_error_raised_when_popping_from_empty_heap(empty_heap):
    """Test that popping from an empty heap raises a value error."""
    with pytest.raises(ValueError):
        empty_heap.pop()


def test_value_error_raised_if_incorrect_optional_parameter():
    """Test that value error raised if incorrect optional parameter given."""
    from bin_heap import Heap
    with pytest.raises(ValueError):
        Heap([1], 'no')


def test_pop_for_max_heap_smaller_than_3_values():
    """Test that pop works on heap smaller than 3."""
    from bin_heap import Heap
    new_heap = Heap([1, 2])
    assert new_heap.pop() == 2


def test_pop_for_min_heap_smaller_than_3_values():
    """Test that pop works on heap smaller than 3."""
    from bin_heap import Heap
    new_heap = Heap([1, 2], 'min')
    assert new_heap.pop() == 1


def test_value_error_raised_for_non_int_input(empty_heap):
    """Test that error is raised if you input a non-integer."""
    with pytest.raises(ValueError):
        empty_heap.push('n')


def test_value_error_raised_if_in_already_in_heap(empty_heap):
    """Test that error is raised if you input a value already in the heap."""
    from bin_heap import Heap
    with pytest.raises(ValueError):
        new_heap = Heap([1, 2])
        new_heap.push(1)


def test_max_heap_pop_always_sorted_order():
    """Test that pop returns sorted values."""
    from bin_heap import Heap
    import random
    random_nums = list(set([random.randint(0, 1000) for i in range(10)]))
    new_heap = Heap(random_nums)
    all_popped = [new_heap.pop() for i in range(new_heap._size)]
    assert all_popped == sorted(random_nums, reverse=True)


def test_min_heap_pop_always_sorted_order():
    """Test that pop returns sorted values."""
    from bin_heap import Heap
    import random
    random_nums = list(set([random.randint(0, 1000) for i in range(10)]))
    new_heap = Heap(random_nums, 'min')
    all_popped = [new_heap.pop() for i in range(new_heap._size)]
    assert all_popped == sorted(random_nums)
