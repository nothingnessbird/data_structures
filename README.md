# Data Structures


**Author**: Kinley Ramson (github.com/nothingnessbird)

## Overview
This repository will hold sample code for a number of classic data structures implemented in Python.

## Linked List

### Create empty instance of linked list:

```
new_list = LinkedList()
```

#### Runtime: O(1)


### Create instance of linked list using iterable:

```
l = [1, 2, 3, 4]

new_list = LinkedList(l)
```

#### Runtime: O(n)


### .push:
Add a value to the head.

```
new_list.push(5)
```

#### Runtime: O(1)

### .pop:
Remove and return value from head

```
new_list.pop()
5
```

#### Runtime: O(1)

### len():
Return size of list

```
len(new_list)
4
```

#### Runtime: O(1)


### Search for a value:
Return node of given value

```
new_list.search(1)
<__main__.Node at 0x7fc0ec598ac8>
```

#### Runtime: O(n)

### Remove a value:
Remove a value from anywhere in list

```
new_list.remove(1)
```

#### Runtime: O(n)


### Print the linked list:
Display the list a tuple literal in a string

```
print(new_list)
'(4, 3, 2)'
```

#### Runtime: O(n)


## Stack

### Create empty instance of stack:

```
new_stack = Stack()
```

#### Runtime: ???


### Create instance with iterable:

```
l = [1, 2, 3, 4]
new_stack = Stack(l)
```

#### Runtime: ???


### .push:
Add value to top of stack

```
new_stack.push(5)
'''

#### Runtime: ???


### .pop:
Remove and return value from top of stack

```
new_stack.pop()
5
'''

#### Runtime: ???


### len():
Return size of stack

```
len(new_stack)
4
```

#### Runtime: ???


## Doubly Linked List

### Create empty instance

```
new_dll = DLL()
```

#### Runtime: ???


### Create instance with iterable:

```
l = [1, 2, 3, 4]
new_dll = DLL(l)
```

#### Runtime: ???


### .push:
Add a value to the head.

```
new_dll.push(5)
```

#### Runtime: ???


### .pop:
Remove and return value from head

```
new_dll.pop()
5
```

#### Runtime: ???


### .append:
Add a value to the tail

```
new_dll.append(-1)
```

#### Runtime: ???


### .shift:
Remove and return value from tail

```
new_dll.shift()
-1
```

#### Runtime: ???


### .remove:
Remove value from anywhere in list

```
new_dll.remove(3)
```

#### Runtime: ???


### len():
Return size of list

```
len(new_dll)
3
```

#### Runtime: ???


## Queue

### Create empty instance:

```
new_q = Queue()
```

#### Runtime: ???


### Create instance with iterable:

```
l = [1, 2, 3, 4]
new_q = Queue(l)
```

#### Runtime: ???


### .enqueue:
Add a value to the head

```
new_q.enqueue(5)
```

#### Runtime: ???


### .dequeue:
Remove and return tail node

```
new_q.dequeue()
1
```

#### Runtime: ???


### .peek:
Return next value to dequeue

```
new_q.peek()
2
```

#### Runtime: ???

### len():
Return size of queue

```
len(new_queue)
4
```

#### Runtime O(1)


## Deque

### Init empty:

```
Deque()
```

#### Runtime O(1)


### Init with iterable:

```
l = [1, 2, 3, 4]
new_deque = Deque(l)
```

#### Runtime O(n)


### append:
Add node to left of deque

```
new_deque.append(5)
```

#### Runtime ???

### appendleft:
Add node to right of deque

```
new_deque.appendleft(0)
```

#### Runtime ???


### pop:
Remove and return rightmost node

```
new_deque.pop()
0
```

#### Runtime ???

### popleft:
Remove and return leftmost node

```
new_deque.popleft()
5
```

#### Runtime ???


### peek:
Return value of next node to pop

```
new_deque.peek()
1
```

#### Runtime ???


### peekleft:
Return value of next node to popleft

```
new_deque.peekleft()
4
```

#### Runtime ???

### len():
Return size of deque

```
len(new_deque)
4
```

#### Runtime O(1)


## Binary Heap (min or max, demonstrating default max)

### init empty:

```
Heap()
```

#### Runtime O(1)


### init with iterable:

```
l = [1, 2, 3, 4]
new_heap = Heap(l)
```

#### Runtime O(n)


### push:
Add value to heap

```
new_heap.push(5)
```

#### Runtime O(log(n))


### pop:
Remove top value from heap

```
new_heap.pop()
5
```

#### Runtime O(n)


### _parent:
Return parent index of index

#### Runtime O(1)

### _children:
Return a list of child indexes (if present) of index

#### Runtime O(1)


### _trickle_down:
Trickle value to proper index in heap

#### Runtime O(n)


## Resources
Written in Python, tested with pytest and tox.