

from time import clock
from stacks import *

def timedTest():
    startSize=10000
    additions=5000
    s = Stack()

    #Puts some initial values onto the Stack
    for i in range(startSize):  
        s.push(i)

    #Times how long it takes to push and pop a set of additional valuesstuff
    start = clock()
    for target in range(additions):
        s.push(target)
    end = clock()
    runTime = end - start

    #Prints results
    print "Time to make %d additional operations is %.6f sec." % \
          (additions,runTime)





