"""
File: queues.py

Contains four queue implementations from in class and in the textbook
"""

class FrontZeroQueue():
    def __init__(self):
        self._items = []

    def enqueue(self, newItem):
        self._items.append(newItem)

    def dequeue(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self._items)

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        for i in xrange(len(self)):
            result = result + str(self._items[i]) + " "
        return result




class BackZeroQueue():
    def __init__(self):
        self._items = []

    def enqueue(self, newItem):
        self._items.insert(0,newItem)

    def dequeue(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self._items)

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        for i in xrange(len(self)):
            result = str(self._items[i]) + " " + result
        return result

from arrays import Array

class ArrayQueue(object):
    """ Array-based queue implementation."""

    DEFAULT_CAPACITY = 25000  # Class variable applies to all queues
    
    def __init__(self):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._rear = -1
        self._size = 0

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        # Resize array if necessary
        if len(self) == len(self._items):
            temp = Array(2 * self._size)
            for i in xrange(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        # newItem goes at logical end of array
        self._rear += 1
        self._size += 1
        self._items[self._rear] = newItem

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._items[0]
        for i in xrange(len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._rear -= 1
        self._size -= 1
        # Resizing the array is an exercise
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._items[0]

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        for i in xrange(len(self)):
            result += str(self._items[i]) + " "
        return result


from node import Node

class LinkedQueue(object):
    """ Link-based queue implementation."""

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        newNode = Node (newItem, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode  
        self._size += 1

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._front.data

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        probe = self._front
        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next
        return result


