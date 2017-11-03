"""Tests for doubly linked list data structure."""

import pytest
import random


@pytest.fixture
def testing_dll():
    """Empty stack for tests."""
    from dll import DLL
    new_dll = DLL()
    return new_dll
