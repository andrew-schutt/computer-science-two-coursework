class Stack:
    def __init__(self):
        self.data = []
        for i in range(100):
            self.data.append("")
        self.nextEmptySlot=0
        

    def push(self,item):
        self.data[self.nextEmptySlot]  = item
        self.nextEmptySlot = self.nextEmptySlot+1
        
    def pop(self):
        self.nextEmptySlot = self.nextEmptySlot-1
        val = self.data[self.nextEmptySlot]
        self.data[self.nextEmptySlot]=""
        return val


    def peek(self):
        return self.data[self.nextEmptySlot-1]

    def isEmpty(self):
        return self.nextEmptySlot==0

        
    def size(self):
        return self.nextEmptySlot

