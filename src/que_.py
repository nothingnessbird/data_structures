"""Create queue data structure."""

from dll.py import DLL


class Queue(object):
    """Create queue data structure."""

    def __init__(self, iterable=()):
        """Initialize queue instance."""
        self.que_ = DLL(iterable)

    def enqueue(self, val):
        """Add node to head of queue."""
        self.que_.push(val)

    def dequeue(self):
        """Remove tail node of queue."""
        return self.queue.shift()

    def peek(self):
        """Return value of next node to dequeue."""
        try:
            return self.que_.tail.val
        except AttributeError:
            return None

    def size(self):
        """Return size of queue."""
        return self.que_._tally

    def __len__(self):
        """Return size of queue when len method is used."""
        return self.size()
