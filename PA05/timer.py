"""
Author: Andrew Schutt
Contact: schutta@uni.edu
Last Modified: 10/31/09
File: timer.py

Comments: times both the list based radixSort and linked list.
"""

import time

from pa05 import linkedRadixSort

from pa04 import radixSort

def radixTimer(alist):

    liststart = time.time()
    radixSort(alist)
    total = time.time() - liststart
    linkstart = time.time()
    linkedRadixSort(alist)
    elapsed = time.time() - linkstart
    print "It took "+str(total)+" seconds to sort "+str(len(alist))+" items using the list based."
    print "It took "+str(elapsed)+"seconds to sort "+str(len(alist))+" items using the linked queue."
