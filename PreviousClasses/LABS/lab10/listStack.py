class Stack:
    def __init__(self):
        self.items = []

    def push(self,obj):
        self.items.append(obj)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return len(self.items)==0        

    def size(self):
        return len(self.items)

