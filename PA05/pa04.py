from linkedQueue import LinkedQueue
"""
This is a sample solution of PA04 for those who struggled with
a solution.

It uses a LinkedQueue to implement the Radix sort in the
"standard" but less efficient manner.

The complexity of this particular sort is O(nm) where
   n is the number of items to be sorted and
   m is the length of the longest number in the list

The actual runtime for this is 2nm + 2n +"a constant"
as each number is moved twice per power of 10
PLUS the original conversion from list to queuue
and the final conversion from queue back to list
(The "constant" is the time it takes to set up the data
queues and calculate the powers of 10.  It isn't really a
constant but a constant plus m since it takes m moves to calculate
the powers of 10)
"""

def radixSort(aList):
    #set up the 11 queues
    main = LinkedQueue()
    bins = []
    for i in range(10):
        bins.append(LinkedQueue())

    #put all of the values from aList into the main queue
    for item in aList:
        main.enqueue(item)

    #determine the length of the longest number in the list
    test=max(aList)
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
            sub=bins[j]
            while len(sub)>0:
                val=sub.dequeue()
                main.enqueue(val)

    #Finally, take the main queue, reassemble the list, and return it
    output=[]
    while len(main)>0:
        output.append(main.dequeue())
    return output

        

    
