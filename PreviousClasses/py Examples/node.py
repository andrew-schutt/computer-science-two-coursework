class Node:
    def __init__(self,value):
        self.data=value
        self.nextNode=None

    def setData(self,value):
        self.data=value

    def getData(self):
        return self.data

    def setNext(self,newNode):
        self.nextNode=newNode

    def getNext(self):
        return self.nextNode
