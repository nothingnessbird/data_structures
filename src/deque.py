"""Create deque data structure."""

from dll.py import DLL


class Deque(object):
    """Create deque class."""

    def __init__(self, iterable=()):
        """Initialize deque instance."""
        self.deque = DLL(iterable)

    def append(self, val):
        """Append a node to end (right) of deque."""
        self.deque.append(val)

    def appendleft(self, val):
        """Append a node to beginning (left) of deque."""
        self.deque.push(val)

    def pop(self):
        """Remove and return last (rightmost) node in deque."""
        return self.deque.shift()

    def popleft(self):
        """Remove and return first (leftmost) node from deque."""
        return self.deque.pop()

    def peek(self):
        """Return value of next node that would be popped."""
        try:
            return self.deque.tail.val
        except AttributeError:
            return None

    def peekleft(self):
        """Return value of next node that would be poplefted."""
        try:
            return self.deque.head.val
        except AttributeError:
            return None

    def size(self):
        """Return size of deque."""
        return self.deque._tally

    def __len__(self):
        """Return size of deque when using len method."""
        return self.size()
