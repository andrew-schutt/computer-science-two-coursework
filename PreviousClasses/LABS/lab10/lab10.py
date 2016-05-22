from listStack import Stack
from tree import BinaryTree
import operator

def buildParseTree(exp):
    #This is what you write in part A
    pass
    
    

def evaluate(parseTree):
    opers = {'+':operator.add,
             '-':operator.sub,
             '*':operator.mul,
             '/':operator.div }
    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()
    if left and right:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(left),evaluate(right))
    else:
        return int(parseTree.getRootVal())
    

def printTree(parseTree):
    #part b
    pass
    
