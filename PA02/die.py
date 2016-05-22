"""
File: die.py 

Provides a simple Die class that allows for any number of sides
"""
from random import randint

class Die:
    
    def __init__(self, sides=6):
        """Constructor for any sided Die that takes an the number of sides 
        as a parameter; if no parameter given then default is 6-sided."""
        
        if isinstance(sides, int):
            self.__numSides = sides
        else:
            print "Usage:  Die() or Die(numberOfSides)"
            return
        
        self.__currentRoll = randint(1, self.__numSides)

    def __str__(self):
        """Overrides the standard method, converts a Die to a string."""
        return str(self.__currentRoll)

    def __cmp__(self, rhs_Die):
        """Overrides the '__cmp__' operator for Dies, to allow for 
         a deep comparison of two Dice."""
        if self.__currentRoll < rhs_Die.__currentRoll:
            return -1
        elif self.__currentRoll == rhs_Die.__currentRoll:
            return 0
        else:
            return 1

    def __add__(self, rhs_Die):
        """Overrides the '__add__' operator for Dies, to allow for
        to allow for a deep comparison of two Dice."""
        return self.__currentRoll + rhs_Die.__currentRoll

    def roll(self):
        """Causes a die to roll itself"""
        self.__currentRoll = randint(1, self.__numSides)
        return self.__currentRoll
    
    def getRoll(self):
        """Returns the value of current Die roll."""
        return self.__currentRoll
    
    def show(self):
        """Displays a Die by printing it."""
        print self.__currentRoll

    def setRoll(self, sides):
        """Sets the die side to the variable given.
        Preconditions: 1 <= sides
        Postconditions: The number of sides on die will be sides"""
        self._numSides = sides
