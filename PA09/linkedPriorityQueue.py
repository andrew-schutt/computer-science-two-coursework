"""
File: linkedPriorityQueue.py

page 632 of your textbook
"""



class Node(object):
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

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



class LinkedPriorityQueue(LinkedQueue):
    """Sorted list implementation using a linked structure."""

    def __init(self):
        LinkedQueue.__init__(self)

    def enqueue(self, newItem):
        """Inserts newItem after items of greater or equal
        priority or ahead of items of lesser priority.
        A has greater priority than B if A < B."""
        
        if self.isEmpty() or newItem >= self._rear.data:
            # New item goes at rear
            LinkedQueue.enqueue(self, newItem)
        else:
            # Search for a position where it's less
            probe = self._front
            while newItem >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(newItem, probe)
            if probe == self._front:
                # New item goes at front
                self._front = newNode
            else:
                # New items goes between two nodes
                trailer.next = newNode
            self._size += 1
