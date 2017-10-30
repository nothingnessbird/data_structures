# Data Structures


**Author**: Kinley Ramson (github.com/nothingnessbird)

## Overview
This repository will hold sample code for a number of classic data structures implemented in Python.

## Linked-List

### Create empty instance of linked list:

```
from linked_list import LinkedList

new_list = LinkedList()
```

#### Runtime: O(1)


### Create instance of linked list using iterable:

```
from linked_list import LinkedList

l = [1, 2, 3, 4]

new_list = LinkedList(l)
```

#### Runtime: O(n)


### .push:

```
new_list.push(5)
```

#### Runtime: O(1)

### .pop:

```
new_list.pop()
5
```

#### Runtime: O(1)

### len():

```
len(new_list)
4
```

#### Runtime: O(1)


### Search for a value:

```
new_list.search(1)
<linked_list.Node at 0x7fc0ec598ac8>
```

#### Runtime: O(k)

### Remove a value:

```
new_list.remove(1)
```

#### Runtime: O(n)


### Print the linked list:

```
print(new_list)
'(4, 3, 2)'
```

#### Runtime: O(n)




## Resources
Written in Python, tested with pytest and tox.