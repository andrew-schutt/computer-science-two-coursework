"""
File: algorithms.py

Graph processing algorithms
"""
from graph import *

from stack import LinkedStack

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    lyst = []
    return stack

def dfs(g, v, stack):
    v.setMark()
    print "setMark of vertex:",v
    for w in g.neighboringVertices(v):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)
    print "pushing vertex onto stack:",v 

def shortestPaths(g, startLabel):
    total = 0
    vertices = []
    parents = []
    distance=[]
    visited = []
    output = []
    for v in g.vertices():
        if v.getLabel() == startLabel:
            vertices.append(v)
            parents.append(None)
            distance.append(0)
            visited.append(False)
        elif v.getEdgeTo(g.getVertex(startLabel)) != None:
            vertices.append(v)
            parents.append(startLabel)
            distance.append(v.getEdgeTo(g.getVertex(startLabel)).getWeight())
            visited.append(False)
        else:
            vertices.append(v)
            parents.append(None)
            distance.append(10**10)
            visited.append(False)
            
    while True:
        low = max(distance)
        for i in xrange(len(visited)):
            if visited[i] == False and distance[i] <= low:
                low == distance[i]
                vertex = vertices[i]
        current = vertices.index(vertex)
        visited[current] = True
        print vertex
        for x in vertex.neighboringVertices():
            index = vertices.index(x)
            total = vertex.getEdgeTo(x).getWeight()
            if total < distance[index]:
                distance[index] = total
                parents[index] = vertex
        if all(visited):
            break
    for y in xrange(len(vertices)):
        print vertices[y], distance[y], parents[y]
        
def spanTree(g, startLabel):
    # Exercise
    return ["Under development"]


