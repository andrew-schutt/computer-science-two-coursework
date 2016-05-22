class HashSet:
   def __init__(self,size):
      self._items = []
      for i in xrange(size):
         self._items.append(None)

   def hashfunction(self,item,size):
      return item%size

   def rehash(self,oldhash,size):
      return (oldhash+1)%size
   
   def add(self,item):
      value = 0
      for char in item:
         value += ord(char)
      hashvalue = self.hashfunction(value,len(self._items))
      position=hashvalue
      while self._items[position] != None:
         position = self.rehash(position,len(self._items))
         if position==hashvalue:
            return False
      self._items[position]=item
      return True


   def contains(self,item):
      value = 0
      for char in item:
         value += ord(char)
      startslot = self.hashfunction(value,len(self._items))

      stop = False
      found = False
      position = startslot
      while self._items[position] != None and  \
                           not found and not stop:
         if self._items[position] == item:
           found = True
         else:
           position=self.rehash(position,len(self._items))
           if position == startslot:
               stop = True
      return found

   def __str__(self):
      return str(self._items)

