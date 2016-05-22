"""
Author : Ben Schafer
Contact : schafer@cs.uni.edu
Last Modified : 9/2/2009
File: library.py

This module provides the beginnings of a test function for Book and Patron
"""

def test():
    """Tests the Patron and Book classes."""
    p1 = Patron("Ben Schafer")
    p2 = Patron("Amy Frohardt")
    b1 = Book("Atonement", "McEwan")
    b2 = Book("The March", "Doctorow")
    b3 = Book("Beach Music", "Conroy")
    b4 = Book("Thirteen Moons", "Frazier")
    print b1.borrowMe(p1)
    print b2.borrowMe(p1)
    print b3.borrowMe(p1)
    print b1.borrowMe(p2)
    print b4.borrowMe(p1)
    print p1
    print b1
    print b4
    print b1.returnMe()
    print b2.returnMe()
    print b1
    print b2


   
