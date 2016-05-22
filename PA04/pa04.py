"""
Author: Andrew Schutt
Contact: schutta@uni.edu
Date: 10/22/09
File: pa04.py

Comments: This is an implmenation of the radix sort
"""

from dataStructures import Queue

def radixSort(alist):

    #intialize variables
    bins = []
    largeQueue = Queue()
    result = []
    
    for i in alist:
        """this loop populates 'largeQueue' with 'alist'
           values."""
        largeQueue.enqueue(i)

    for x in xrange(10):
        """this loop populates 'bins' list with 10 queues."""
        q = Queue()
        bins.append(q)
        
    for lsd in xrange(1,len(str(max(alist)))+1):
        """finds largest number in 'alist' to loop
            over correct number of times to sort
            all numbers contained in 'alist'.

            lsd is also used in calculations for modulo
            and division to extract each digit
            from pieces of elements within
            'alist'."""
        
        for index in xrange(len(alist)):
            """dequeues item from 'largeQueue'
               to be examined and put into proper "bin"
               in 'bins'."""
            item = largeQueue.dequeue()
            element = item%(10**lsd)
            if lsd == 1:
                element = element
            else:
                element = element/(10**(lsd-1))
            bins[element].enqueue(item)
            
        for y in xrange(10):
            """re-populates 'largeQueue' with elements of
               'bins'."""
            while len(bins[y]) > 0:
                largeQueue.enqueue(bins[y].dequeue())

    for z in xrange(len(largeQueue)):
        """populates 'result' list from 'largeQueue'."""
        result.append(largeQueue.dequeue())

    return result
            
