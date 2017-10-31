"""Create binary heap data structure."""


class Heap(object):
    """Create heap class."""

    def __init__(self, iterable=(), min_max='max'):
        """Initialize heap instance."""
        self._heap_list = []
        self._size = 0
        if min_max == 'max':
            self._multiplier = 1
        elif min_max == 'min':
            self._multiplier = -1
        else:
            raise ValueError("That is not an acceptable value. Try 'min'.")
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Push new value to heap."""
        self._heap_list.append(val)
        self._size += 1
        if self._size == 1:
            return
        child_index = self._size - 1
        parent_index = self._parent(child_index)
        while val * self._multiplier > self._heap_list[parent_index] * self._multiplier:
            self._heap_list[child_index] = self._heap_list[parent_index]
            self._heap_list[parent_index] = val
            if parent_index:
                parent_index = self._parent(parent_index)
            else:
                return

    def _parent(self, child_index):
        """Return parent index."""
        if child_index % 2:
            return (child_index - 1) // 2
        elif not child_index % 2:
            return (child_index - 2) // 2
