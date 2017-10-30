"""Create doubly linked list data structure."""


class Node(object):
    """Create a node class."""

    def __init__(self, val=None, next=None, prev=None):
        """Initialize each node instance."""
        self.val = val
        self.next = next
        self.prev = prev


class DLL(object):
    """Create doubly linked list class."""

    def __init__(self, iterable=()):
        """Initialize dll instance."""
        self.head = None
        self.tail = None
        self._tally = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add node to head of dll."""
        pushed_node = Node(val)
        if not self.head:
            self.head = pushed_node
            self.tail = pushed_node
            self._tally += 1
        else:
            self.head.prev = pushed_node
            pushed_node.next = self.head
            self.head = pushed_node
            self._tally += 1

    def pop(self):
        """Remove and return first node of dll."""
        if not self.head:
            raise IndexError('Empty: no value to remove.')
        val = self.head.val
        if len(self) == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.next.prev = None
        self._tally -= 1
        return val

    def append(self, val):
        """Add new node to tail of dll."""
        appended_node = Node(val)
        if not self.tail:
            self.head = appended_node
            self.tail = appended_node
            self._tally += 1
        else:
            self.tail.next = appended_node
            appended_node.prev = self.tail
            self.tail = appended_node
            self._tally += 1

    def shift(self):
        """Remove and return last node of dll."""
        if not self.tail:
            raise IndexError('Empty: no value to remove.')
        val = self.tail.val
        self.tail = self.tail.prev
        if len(self) == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.prev.next = None
        self._tally -= 1
        return val

    def remove(self, val):
        """Remove node with given value from dll."""
        current_node = self.head
        if current_node.val == val:
            self.pop()
            return
        if self.tail.val == val:
            self.shift()
            return
        while current_node:
            if current_node.val == val:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self._tally -= 1
                return
            else:
                current_node = current_node.next
        raise ValueError('That value is not in the list.')

    def __len__(self):
        """Return size of dll when using len method."""
        return self._tally
