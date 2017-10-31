# Data Structures


**Author**: Kinley Ramson (github.com/nothingnessbird)

## Overview
This repository will hold sample code for a number of classic data structures implemented in Python.

## Linked List

### Create empty instance of linked list:

```
new_list = LinkedList()
```

#### Runtime: ???


### Create instance of linked list using iterable:

```
l = [1, 2, 3, 4]

new_list = LinkedList(l)
```

#### Runtime: ???


### .push:
Add a value to the head.

```
new_list.push(5)
```

#### Runtime: ???

### .pop:
Remove and return value from head

```
new_list.pop()
5
```

#### Runtime: ???

### len():
Return size of list

```
len(new_list)
4
```

#### Runtime: ???


### Search for a value:
Return node of given value

```
new_list.search(1)
<__main__.Node at 0x7fc0ec598ac8>
```

#### Runtime: ???

### Remove a value:
Remove a value from anywhere in list

```
new_list.remove(1)
```

#### Runtime: ???


### Print the linked list:
Display the list a tuple literal in a string

```
print(new_list)
'(4, 3, 2)'
```

#### Runtime: ???


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



## Resources
Written in Python, tested with pytest and tox.