"""Create Linked List data structure."""


class Node(object):
    """."""

    def __init__(self, data=None, next=None):
        """."""
        self.data = data
        self.next = next


class LinkedList(object):
    """."""

    def __init__(self):
        """."""
        self.head = None
        self._size = 0

    def push(self, val):
        """."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self._size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self._size += 1
