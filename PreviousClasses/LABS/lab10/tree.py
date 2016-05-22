import os

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.left = None
        self.right = None
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
            
    def getRootVal(self,):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setLeftChild(self,val):
        self.left=val

    def setRightChild(self,val):
        self.right=val
