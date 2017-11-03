"""Tests for stack data structure."""

import pytest
import random


@pytest.fixture
def testing_stack():
    """Empty stack for tests."""
    from stack import Stack
    new_stack = Stack()
    return new_stack
