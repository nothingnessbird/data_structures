"""Tests for priority queue data structure."""

import pytest
import random


@pytest.fixture
def testing_pq():
    """Empty priority queue for testing."""
    from priorityq import PriorityQ
    new_pq = PriorityQ()
    return new_pq


def test_init_empty_pq(testing_pq):
    """Test that empty pq initializes."""
    assert testing_pq._list == [[] for x in range(100)]


def test_insert_one_value_top_priority(testing_pq):
    """Test that one value is inserted at proper priority."""
    testing_pq.insert(1, 0)
    assert testing_pq._list[0] == [1]


def test_popping_one_value_top_priority(testing_pq):
    """Test that popping from top priority returns correct value."""
    testing_pq.insert(1, 0)
    assert testing_pq.pop() == 1


def test_peek_returns_correct_value(testing_pq):
    """Test that peek returns the correct value to pop."""
    testing_pq.insert(1, 0)
    assert testing_pq.peek() == 1


def test_inserted_values_come_out_in_correct_order(testing_pq):
    """."""
    test_values = list(range(100))
    for value in test_values:
        testing_pq.insert(value, value)
    all_popped = [testing_pq.pop() for i in range(testing_pq._size)]
    assert all_popped == sorted(all_popped)


def test_random_values_come_out_in_correct_order(testing_pq):
    """."""
    test_vals = []
    for i in range(100):
        num = random.randint(0, 5000)
        priority = (i % 3) + 1
        test_vals.append([num, priority])
        testing_pq.insert(num, priority)
    all_popped = [testing_pq.pop() for i in range(testing_pq._size)]
    sorted_test_vals = sorted(test_vals, key=lambda vals: vals[1])
    assert all_popped == [val[0] for val in sorted_test_vals]
