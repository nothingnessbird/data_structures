"""Create priiority queue data structure."""


class PriorityQ(object):
    """Create priority queue class."""

    def __init__(self):
        """Initialize priority queue instance."""
        self._list = [[] for x in range(100)]
        self._size = 0

    def insert(self, val, priority=99):
        """Insert value into priority queue at priority index."""
        self._list[priority].append(val)
        self._size += 1
        # error handle priority out of range

    def pop(self):
        """Remove and return first value at given priority."""
        self._size -= 1
        priority = self._list.index(self._find_first())
        return self._list[priority].pop(0)
        # error handle empty q

    def _find_first(self):
        """Find first priority with value."""
        for sub_list in self._list:
            if sub_list:
                return sub_list

    def peek(self):
        """Return next value to pop."""
        priority = self._list.index(self._find_first())
        return self._list[priority][0]
