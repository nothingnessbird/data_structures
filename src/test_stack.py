"""Tests for stack data structure."""

import pytest
import random


TEST_VALS_ORDERED = [i for i in range(100)]
TEST_VALS_RANDOM = [random.randint(0, 5000) for i in range(100)]


@pytest.fixture
def testing_stack():
    """Empty stack for tests."""
    from stack import Stack
    new_stack = Stack()
    return new_stack


def test_stack_inits_with_empty_linked_list(testing_stack):
    """Test stack."""
    assert testing_stack._stack.head is None


def test_push_one_val_to_stack(testing_stack):
    """Test push to stack."""
    testing_stack.push(1)
    assert testing_stack._stack.head.val == 1


def test_push_to_stack_creates_node_object(testing_stack):
    """Test push."""
    from linked_list import Node
    testing_stack.push(1)
    assert isinstance(testing_stack._stack.head, Node)


def test_pop_returns_expected_value(testing_stack):
    """Test pop."""
    testing_stack.push(1)
    assert testing_stack.pop() == 1


def test_stack_initialized_with_ordered_nums_pops_in_correct_order():
    """Test pop."""
    from stack import Stack
    new_stack = Stack(TEST_VALS_ORDERED)
    all_popped = []
    for i in range(len(new_stack)):
        all_popped.append(new_stack.pop())
    all_popped.reverse()
    assert all_popped == TEST_VALS_ORDERED


def test_stack_initialized_with_random_nums_pops_in_correct_order():
    """Test pop."""
    from stack import Stack
    new_stack = Stack(TEST_VALS_RANDOM)
    all_popped = []
    for i in range(len(new_stack)):
        all_popped.append(new_stack.pop())
    all_popped.reverse()
    assert all_popped == TEST_VALS_RANDOM
