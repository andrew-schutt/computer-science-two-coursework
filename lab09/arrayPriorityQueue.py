from arrayQueue import *
from printJob import *

class ArrayPriorityQueue(ArrayQueue):

    def __init(self):
        ArrayQueue._init__(self)

    def enqueue(self, newItem):

        if self.isEmpty() or newItem >= self._items[self._rear]:
            ArrayQueue.enqueue(self, newItem)
        else:
            probe = self._items[self._rear]
            trailer = self._items[self._rear]
            for index in xrange((self._size)-1,-1,-1):
                while newItem >= probe:
                    print "yes"
                    trailer = probe
                    self._items[index + 1] = trailer
                    probe = self._items[index -1]
                if probe == self._items[0]:
                    self._items[0] = newItem
                    self._items[1] = probe
                else:
                    self._items[index] = newItem
                    self._items[index + 1] = trailer
                self._size += 1
                self._rear += 1
                return
