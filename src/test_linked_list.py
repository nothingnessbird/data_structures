"""Tests for linked_list data structure."""

import pytest

ITERABLES = [

]


def test_pop():
    """Test for pop method."""
    from linked_list import LinkedList
    assert LinkedList('s').pop() == 's'
