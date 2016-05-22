

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in xrange(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem


class ArrayQueue(object):
    """ Array-based queue implementation."""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
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
