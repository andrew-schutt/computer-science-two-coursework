class Stack():
    def __init__(self):
        self._items = []

    def push(self,obj):
        self._items.append(obj)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def isEmpty(self):
        return len(self._items)==0

    def __len__(self):
        return len(self._items)


    def __str__(self):
        result = ""
        for i in xrange(len(self)):
            result = str(self._items[i]) + " " + result
        return "top "+result+"bottom"
    
class Queue():
    def __init__(self):
        self._items = []

    def enqueue(self, newItem):
        self._items.append(newItem)

    def dequeue(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def __len__(self):
        return len(self._items)

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        result = ""
        for i in xrange(len(self)):
            result = result + str(self._items[i]) + " "
        return result

