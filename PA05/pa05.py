
"""
Author: Andrew Schutt
Contact: schutta@uni.edu
Last Modified: 10/31/09
File: timer.py

Comments: implemenation of radixSort using linked list.
"""

from linkedQueue import LinkedQueue

def linkedRadixSort(alist):
    #set up the 11 queues
    main = LinkedQueue()
    bins = []
    result = []
    
    for i in range(10):
        bins.append(LinkedQueue())

    #put all of the values from aList into the main queue
    for item in alist:
        main.enqueue(item)

    #determine the length of the longest number in the list
    test=max(alist)
    powers=0
    while test!=0:
        powers=powers+1
        test=test/10
        
    #for each power of 10...
    for i in range(powers):
        
        #sort the individual values into the bins
        while len(main)>0:
            val=main.dequeue()
            div = val/(10**i)%10
            bins[div].enqueue(val)

        #Then put the numbers in the bins back into the main queue
        for j in range(10):
            main.enqueueQueue(bins[j])

    #Finally, take the main queue, reassemble the list, and return it
    return main

        

    
