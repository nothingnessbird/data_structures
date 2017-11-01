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
        if type(val) == int:
            if val not in self._heap_list:
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
            else:
                raise ValueError("Value already in heap.")
        else:
            raise ValueError("Non-integer value.")

    def pop(self):
        """Remove the top value of the heap."""
        if self._size == 0:
            raise ValueError("Empty: no value to pop.")
        elif self._size < 3:
            self._size -= 1
            return self._heap_list.pop(0)
        to_pop = self._heap_list[0]
        new_head = self._heap_list[-1]
        self._heap_list[-1], self._heap_list[0] = to_pop, new_head
        self._heap_list.pop()
        self._size -= 1
        parent_index = 0
        self._trickle_down(parent_index)
        return to_pop

    def _parent(self, child_index):
        """Return parent index."""
        if child_index % 2:
            return (child_index - 1) // 2
        elif not child_index % 2:
            return (child_index - 2) // 2

    def _children(self, parent_index):
        """Return child index."""
        child_list = []
        if self._size > parent_index * 2 + 1:
            child_list.append(parent_index * 2 + 1)
        if self._size > parent_index * 2 + 2:
            child_list.append(parent_index * 2 + 2)
        return child_list

    def _trickle_down(self, parent_index):
        """Trickle value down to proper place in heap."""
        children = self._children(parent_index)
        for child in children:
            if self._heap_list[parent_index] * self._multiplier < self._heap_list[child] * self._multiplier:
                self._heap_list[parent_index], self._heap_list[child] = self._heap_list[child], self._heap_list[parent_index]
                self._trickle_down(child)
