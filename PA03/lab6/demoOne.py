from stacks import *

def firstDemo():
    # Test the various implementations with same code
    s = Stack()


    print "Length:", len(s)
    print "Empty:", s.isEmpty()
    print "Push 1-10"
    for i in xrange(10):
        s.push(i + 1)
    print "Peeking:", s.peek() 
    print "Items (bottom to top):",  s
    print "Length:", len(s)
    print "Empty:", s.isEmpty()
    print "Push 11"
    s.push(11)
    print "Popping items (top to bottom):",
    while not s.isEmpty():
        print s.pop()
        print "Length:", len(s)
    print "Empty:", s.isEmpty()

