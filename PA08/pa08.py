"""
Author: Andrew Schutt
Contact: schutta@uni.edu
Last Modified: 12/3/09
File: pa08.py

Comments: this method takes in three parameters and eventually
outpus a concordance.  the first file is the text that you wish to have
a concordance of.  the second is the stop words desired. and the
third file is the name of the output file.

the output file is a listing of the words in alphabetical order as well
as the line that the word appers on within the document.
"""

#import data structures and modules
from hashSet import HashSet
from dictionary import HashDictionary
from bst import BST
from linkedIndexedList import LinkedIndexedList
import re, string

def createConcordance(inputFile, stopWords, outputFile):

    #declare data structures
    stopSet = HashSet(3500)
    dictionary = HashDictionary(10000)
    bst = BST()

    #declare regular expressions
    newLine = re.compile(r'\n')
    exprSpaces = re.compile(r'\s')
    dhyp = re.compile('--')
    notChars = re.compile('\W|-')
    
    #populate hashset with stop words
    stopWords = open(stopWords, 'r')
    for stop in stopWords:
        x = newLine.search(stop)
        stop = stop[:x.start()]
        if stop == "":
            break
        stopSet.add(stop)
    stopWords.close()
    
    #open the input and process into words
    f = open(inputFile, 'r')
    lineNum = 0
    while True:
        line = f.readline()
        lineNum += 1
        if line == "":
            break

        #split lines
        m = dhyp.split(line)
        alist = []
        for i in range(len(m)):
            g = exprSpaces.split(m[i])
            alist = alist + g
            
        #strip down to words
        print alist
        for word in alist:
            if word == None:
                pass
            else:
                word = string.lower(word)
                while True:
                    n = notChars.search(word)
                    if len(word) <= 0:
                        break
                    elif n != None:
                        if n.start() == 0:
                            word = word[n.end():]
                        else:
                            word = word[:n.start()]
                    else:
                        break
                            
                #check if word is stop word
                if not stopSet.contains(word) and len(word) > 0:
                    #if word isn't already in dictionary
                    if dictionary.search(word) == None:
                        linkedValue = LinkedIndexedList()
                        dictionary.store(word, linkedValue)
                        dictionary.search(word).append(lineNum)
                        bst.add(word)
                    #if the word is in the dictionary
                    else:
                        dictionary.search(word).append(lineNum)
    f.close()

    #open output and use BST to print out words
    #   in alphabetical order
    output = open(outputFile, 'w')
    lyst = bst.inorder()
    temp = None
    for item in lyst:
        temp = dictionary.search(item)
        output.write(item + " - " + str(temp)+"\n")
    output.close()
    
