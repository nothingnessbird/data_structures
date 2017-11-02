"""Tests for linked list 2."""

import pytest


def test_if_linked_list_has_empty_head():
    """."""
    from linked_list2 import LinkedList
    new_list = LinkedList()
    assert new_list.head is None


def test_if_linked_list_has_no_size_if_not_passed_iterable():
    """."""
    from linked_list2 import LinkedList
    new_list = LinkedList()
    assert new_list._size == 0


def test_if_node_class_has_data_attribute():
    from linked_list2 import Node
    new_node = Node()
    assert new_node.data is None


def test_if_node_class_has_next_attribute():
    from linked_list2 import Node
    new_node = Node()
    assert new_node.next is None


def test_if_push_method_creates_new_node():
    from linked_list2 import LinkedList
    from linked_list2 import Node
    pushed_list = LinkedList()
    pushed_list.push(1)
    assert isinstance(pushed_list.head, Node)


def test_if_size_grows_when_list_pushed_to():
    from linked_list2 import LinkedList
    pushed_list = LinkedList()
    pushed_list.push(1)
    assert pushed_list._size == 1


def test_if_push_works_on_nonempty_list():
    from linked_list2 import LinkedList
    pushed_list = LinkedList()
    pushed_list.push(1)
    pushed_list.push(2)
    assert pushed_list._size == 2


def test_if_nodes_point_to_actuel_next_node():
    from linked_list2 import LinkedList
    pushed_list = LinkedList()
    pushed_list.push(1)
    pushed_list.push(2)
    assert pushed_list.head.next.data == 1
