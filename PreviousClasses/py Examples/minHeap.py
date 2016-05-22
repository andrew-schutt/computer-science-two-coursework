class PriorityQueue:
    def __init__(self):
        self.heapList = [0]
        self.valueList = [0]


    def insert(self,priority,value):
        self.heapList.append(priority)
        self.valueList.append(value)
        self.percUp(len(self.heapList)-1)

    def percUp(self,i):
        while i > 1:
            if self.heapList[i] < self.heapList[i/2]:
               self.heapList[i/2],self.heapList[i]=self.heapList[i],self.heapList[i/2]
               self.valueList[i/2],self.valueList[i]=self.valueList[i],self.valueList[i/2]
            i = i/2

    def delMin(self):
        print "check"
        
        retval = self.valueList[1]
        if len(self.heapList)>2:
            self.heapList[1] = self.heapList.pop()
            self.valueList[1] = self.valueList.pop()
            self.percDown(1)
        else:
            self.valueList.pop()
            self.heapList.pop()
        return retval

    def percDown(self,i):
        while (i * 2) < len(self.heapList):
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc],self.heapList[i]
                self.valueList[i], self.valueList[mc] = self.valueList[mc],self.valueList[i]
            i = mc

    def minChild(self,i):
        if i*2 + 1 > len(self.heapList)-1:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
            

    def buildHeap(self,alist):
        for dist,v in alist:
            self.insert(dist,v)

    def show(self):
        return self.heapList
		
    def size(self):
	    return len(self.heapList)-1
		
    def isEmpty(self):
	    return self.size()==0
		
    def findMin(self):
	    return self.heapList[1]
        
    def decreaseKey(self,what,newKey):
        for i in range(len(self.valueList)):
            item=self.valueList[i]
            if what==item:
                self.heapList[i]=newKey
                self.percUp(i)
