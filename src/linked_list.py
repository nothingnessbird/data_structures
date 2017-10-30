"""Create singly linked list data structure."""


class Node(object):
    """Create a node class."""

    def __init__(self, val=None, next=None):
        """Initialize each node instance."""
        self.val = val
        self.next = next


class LinkedList(object):
    """Create a linked list class."""

    def __init__(self, iterable=()):
        """Initialize each linked list instance."""
        self.head = None
        self._tally = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add node to beginning of linked list."""
        self.head = Node(val, self.head)
        self._tally += 1

    def pop(self):
        """Remove and return first node of linked list."""
        if not self.head:
            raise IndexError('Empty list: no value to pop.')
        val = self.head.val
        self.head = self.head.next
        self._tally -= 1
        return val

    def size(self):
        """Return length of linked list."""
        return self._tally

    def search(self, val):
        """Search linked list for given value and return corresponding node."""
        current_node = self.head
        while current_node:
            if current_node.val == val:
                return current_node
            else:
                current_node = current_node.next

    def remove(self, val):
        """Remove node with given value from linked list."""
        current_node = self.head
        previous_node = None
        flag = False
        if current_node.val == val:
            self.pop()
            return
        while current_node:
            if current_node.val == val:
                flag = True
                previous_node.next = current_node.next
            else:
                previous_node = current_node
                current_node = current_node.next
        if not flag:
            raise ValueError('That value is not in the list.')

    def __len__(self):
        """Return size of linked list when using len method."""
        return self.size()
