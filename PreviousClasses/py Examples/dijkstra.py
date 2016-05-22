from minHeap import PriorityQueue
from graph import Graph

def dijkstra(G,start):
    PQ = PriorityQueue()
    start.setDistance(0)
    print [(v.getDistance(),v.getId()) for v in G]
    PQ.buildHeap([(v.getDistance(),v) for v in G])        
    while not PQ.isEmpty():
        w = PQ.delMin()
        for v in w.getAdj():
            newDist = w.getDistance() + w.getCost(v)
            if newDist < v.getDistance():
                v.setDistance( newDist )
                v.setPred(w)
                PQ.decreaseKey(v,newDist)



def buildGraph():
	g = Graph()

	g.addVertex("A")
	g.addVertex("B")
	g.addVertex("C")
	g.addVertex("D")
	g.addVertex("E")
	g.addVertex("F")

	g.addEdge("A","B",10)
	g.addEdge("A","C",15)
	g.addEdge("A","F",5)
	g.addEdge("B","C",7)
	g.addEdge("C","D",7)
	g.addEdge("C","F",10)
	g.addEdge("D","E",7)
	g.addEdge("F","D",5)
	g.addEdge("E","F",13)
	
	return g
