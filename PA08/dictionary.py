


class HashDictionary(object):

    def __init__(self,size=100):
        self._items=[]
        for i in xrange(size):
            self._items.append(None)

    def store(self,key,value):
        index = self._hash(key)
        position=index
        while self._items[position]!=None:
            position=self._rehash(position,len(self._items))
            if position==index:
                return
        self._items[position]=Entry(key,value)

    def _rehash(self,oldhash,size):
        return (oldhash+1)%size

    def _hash(self,key):
        """Generates an integer key from a string"""
        """Fundamentals of Python"""
        """by Kenneth Lambert"""
        """pg.792 section 19.3.2"""
        """changed variable sum -> total"""
        """changed variable item -> key"""
        if len(key) >4 and \
           (key[0].islower() or key [0].isupper()):
            key = key[1:]
        total=0
        for ch in key:
            total += ord(ch)
        if len(key) > 2:
            total -= 2 * ord(key[-1])
        return total

    def search(self,key):
        #returns the data value associated with the key item
        #returns None if the key is not in the dictionary
        index = self._hash(key)
        position=index
        while (self._items[position]!=None):
            if (self._items[position].getKey()==key):
                return self._items[position].getValue()
            position=self._rehash(position,len(self._items))
            if position==index:
                break
        return None            
        

class Entry(object):
    def __init__(self,key,value):
        self._key=key
        self._value=value

    def getKey(self):
        return self._key

    def getValue(self):
        return self._value

    def __str__(self):
        return str(self._key)+" : "+str(self._value)
