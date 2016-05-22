"""
Author: Andrew Schutt
Contact: schutta@uni.edu
Last Modified: 9/7/2009
File:book.py

This class creates a book object and keeps track of who has the book
as well as who is on a waiting list for the book.
"""

import Patron

class Book(object):

    def __init__(self, title, author)

        self._title = title
        self._author = author

    def getTitle(self):

        return str(self._title)

    def getAuthor(self):

        return str(self._author)

    def getPatron(self):

    def borrowMe(self):

    def returnMe(self):

    def __str__(self):

        
