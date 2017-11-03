"""Tests for deque data structure."""

import pytest
import random


@pytest.fixture
def testing_deque():
    """Empty deque for tests."""
    from deque import Deque
    new_deque = Deque()
    return new_deque
