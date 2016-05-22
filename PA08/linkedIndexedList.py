
class Node(object):
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class LinkedIndexedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._logicalSize = 0
        
    def _locate(self,index):
        self._currentNode = self._head
        self._previousNode = None
        while index>0:
            self._previousNode = self._currentNode
            self._currentNode = self._currentNode.next
            index -= 1

    def append(self,newItem):
        newNode = Node(newItem,None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail.next = newNode
        self._tail=newNode
        self._logicalSize += 1

    def __setitem__(self,index,item):
        if index<0 or index>=len(self):
            raise IndexError,"Index out of Range"
        else:
            self._locate(index)
            self._currentNode.data=item
            
    def isEmpty(self):
        return len(self)==0
    
    def insert(self,index,newItem):
        """NOTE, this is the one method with which I disagree with your author.
           I have made minor changes."""
        if index>len(self):
            raise IndexError,"Index out of Range"
        elif index==self._logicalSize:
            self.append(item)
        else:
            self._locate(index)
            newNode = Node(newItem,self._currentNode)
            if self._previousNode==None:
                self._head = newNode
            else:
                self._previousNode.next = newNode
            self._logicalSize += 1

    def remove(self,index):
        pass

    def __getitem__(self,index):
        pass

    def index(self,value):
        pass

    ##Other operations
    def __len__(self):
        return self._logicalSize

    def __str__(self):
        output = ""
        if self._head==None:
            return output
        else:
            current=self._head
            while current != None:
                output = output + str(current.data) + " "
                current = current.next
            return output     
