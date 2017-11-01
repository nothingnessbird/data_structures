"""Create priiority queue data structure."""


class PriorityQ(object):
    """Create priority queue class."""

    def __init__(self, iterable=()):
        """Initialize priority queue instance."""
        self._list = [[] for x in range(100)]
        self._size = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)
        else:
            raise ValueError("Parameter must be iterable")
