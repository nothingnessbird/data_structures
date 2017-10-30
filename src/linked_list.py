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
            raise IndexError('Empty: no value to remove.')
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
                break
            else:
                previous_node = current_node
                current_node = current_node.next
        if not flag:
            raise ValueError('That value is not in the list.')

    def display(self):
        """Render linked list as unicode string of tuple literal."""
        current_node = self.head
        list_string = u'('
        while current_node:
            list_string += '{}, '.format(current_node.val)
            current_node = current_node.next
        list_string = list_string[:-2] + ')'
        return list_string

    def __len__(self):
        """Return size of linked list when using len method."""
        return self.size()

    def __str__(self):
        """Print the linked list."""
        return self.display()


if __name__ == '__main__':
    sample_itr = ['str', 1, -2.57, True, ('a', 'tuple'), ['listception']]
    sample_linked_list = LinkedList(sample_itr)
    printed = sample_linked_list.display()
    sample_linked_list.push(3)
    pushed = sample_linked_list.display()
    popped = sample_linked_list.pop()
    searched = sample_linked_list.search(1)
    sample_linked_list.remove(True)
    removed = sample_linked_list.display()
    length = len(sample_linked_list)
    print('This module will create a singly linked list given iterable input.\
            sample input: {}\
            displayed output: {}\
            methods:\
                >>>sample_linked_list.push(3)\
                >>>print(sample_linked_list)\
                {}\
                >>>popped_value = sample_linked_list.pop\
                >>>print(popped_value)\
                {}\
                >>>sample_linked_list.search(1)\
                {}\
                >>>sample_linked_list.remove(True)\
                >>>print(sample_linked_list)\
                {}\
                >>>len(sample_linked_list)\
                {}'.format(sample_itr, printed, popped, searched, removed, length))
