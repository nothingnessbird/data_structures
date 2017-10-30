"""Tests for linked_list data structure."""

import pytest


@pytest.fixture
def empty_list():
    """."""
    from linked_list import LinkedList
    new_linked_list = LinkedList()
    return new_linked_list


@pytest.fixture
def full_list():
    """."""
    sample_iterable = ['str', 1, -2.57, True, ('a', 'tuple'), ['listception']]
    from linked_list import LinkedList
    new_linked_list = LinkedList(sample_iterable)
    return new_linked_list


def test_if_new_linkedlist_has_empty_head(empty_list):
    """."""
    assert empty_list.head is None


def test_if_new_linkedlist_has_no_size(empty_list):
    """."""
    assert empty_list._tally == 0


def test_if_linked_list_grows_when_pushed_to(empty_list):
    """."""
    empty_list.push('value')
    assert empty_list._tally == 1


def test_if_linked_list_has_size_when_created_with_iterable(full_list):
    """."""
    assert full_list._tally == 6


def test_pop():
    """Test for pop method."""
    from linked_list import LinkedList
    assert LinkedList('s').pop() == 's'
