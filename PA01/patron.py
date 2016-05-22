class Patron(object):

    def __init__(self, name):
        self._name = name
        self._books = 0

    def getName(self):
        return self._name
    
    def getNumberOfBooksOut(self):
        return self._books
    
    def checkOut(self):
        if self._books <  3:
            self._books = self._books + 1
            return True
        else:
            return False
        
    def returnBook(self):
        if self._books > 0:
            self._books = self._books - 1
            return True
        else:
            return False
        
    def __str__(self):
        return str(self._name) + " currently has " + str(self._books) + " books checked out."
