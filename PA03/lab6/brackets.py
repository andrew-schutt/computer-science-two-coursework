"""
File: brackets.py
Checks expressions for matching brackets
"""

from stacks import *

def bracketsBalance(exp):          
    """exp represents the expression"""
    stk = Stack() 
    for ch in exp:
        if ch in ['[', '(']: 
            stk.push(ch)
        elif ch in [']', ')']:
            if stk.isEmpty():
                return False                  
            chFromStack = stk.pop()
            # Brackets must be of same type and match up
            if ch == ']' and chFromStack != '[' or \
               ch == ')' and chFromStack != '(':
                return False
    return stk.isEmpty()


def main():
    exp = raw_input("Enter a bracketed expression: ")
    if bracketsBalance(exp):
        print "OK"
    else:
        print "Not OK"

main()
