"""
Author: Andrew Schutt
Contact: schutta@uni.edu
Last Modified: 10/8/09
File: pa03.py

The first method checks if given string is a palindrome
Assumes that the string contains at least one valid character (alpha or numeric)

The second method checks if given html doc has balanced html tags
"""
from stacks import Stack

def palindromeChecker(string):
    """Checks if 'string' is a palindrome"""
    holder = Stack()
    temp = Stack()
    isTrue = True
    
    for char in string:
        """Check for valid character before pushing to holder stack """
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or 0 <= char <= 9:
            holder.push(char)    
    for i in xrange(len(holder)):
        """Pops from holder and compares value in 'string' """
        if 'a' <= string[i] <= 'z' or 'A' <= string[i] <= 'Z' or '0' <= string[i] <= '9':
            temp.push(string[i])
            item = holder.pop()
            if item != temp.pop():
                isTrue = False
                return isTrue
            
    return isTrue

def htmlChecker(html):
    stk = Stack()
    intag = False

    for index in xrange(len(html)):
        """Loops over html doc searching for tags
            when an opening bracket is found the
            tag is pushed onto the stack"""
        if html[index] == '<':
            intag = True
            count = index
            while intag:
                stk.push(html[count])
                if html[count] == '>':
                    intag = False
                else:
                    count = count + 1
                    
    for index in xrange(len(html)):
        """Loops again over html doc but when
            tag is found it compares to popped item"""
        if html[index] == '<':
            intag = True
            count = index
            while intag:
                if len(stk) <= 0:
                    return True
                else:
                    item = stk.pop()
                    if html[count] == '>':
                        intag = False
                    elif html[count] == '/' or item != '/':   
                        None
                    elif html[count] != '/' and item != '/':
                        if html[count] == '<' and item == '>'\
                           or html[count] == '>' and item == '<':
                            count = count + 1
                        elif html[count] == item:
                            count = count + 1
                        else:
                            print count
                            return False
                    
                    
   
    
