"""Create stack data structure."""

from linked_list.py import LinkedList


class Stack(object):
    """Create a stack class."""

    def __init__(self, iterable=()):
        """Initialize stack with a linked list."""
        self._stack = LinkedList(iterable)

    def push(self, val):
        """Push new value to stack."""
        self._stack.push(val)

    def pop(self):
        """Pop head node from stack."""
        return self._stack.pop()

    def __len__(self):
        """Return size of stack."""
        return self._stack.size()
