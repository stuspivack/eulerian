# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)]
##graph = [(1,2),(2,3),(3,1)]
##graph = [(1,2),(2,3),(3,4),(4,5),(1,5)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def nodeTour(tour):
    nodes = []
    pairs = [(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
    pairs.append((tour[-1], tour[0]))
    for pair in pairs:
        if pair[0][0] in pair[1]:
            nodes.append(pair[0][0])
        else:
            nodes.append(pair[0][1])
    last = nodes[0]
    nodes.append(last)
    return nodes
    
def sortGraphEdges(graph):
    l = []
    for edge in graph:
        e = list(edge)
        e.sort()
        l.append(e)
    return l

def deleteEdge(graph, edgeToDel):
    l = []
    for edge in graph:
        if edge != edgeToDel:
            l.append(edge)
    return l

def testTour(graph, tour):
    goodTour = True
    if not graph:
        return None
    if not tour:
        return None
    for edge in graph:
        if edge not in tour:
            goodTour = False
    for edge in tour:
        if edge not in graph:
            goodTour = False
    if goodTour:
        return tour
    
def recEul(graph, start, end):
    nextEdges = filter( (lambda edge: edge[0] == start
                         or edge[1] == start), graph)
    print 'nextEdges', nextEdges
    for edge in nextEdges:
        if [edge] == graph:
            return [edge]
    for edge in nextEdges:
        newGraph = deleteEdge(graph, edge)
        if edge[0] == end:
            newStart = start
            newEnd = edge[1]
        elif edge[0] == start:
            newStart = edge[1]
            newEnd = end
        elif edge[1] == end:
            newEnd = edge[0]
            newStart = start
        else: #edge[1] == start
            newStart = edge[0]
            newEnd = end
        print edge, newGraph, newStart, newEnd
        if testTour(newGraph, recEul(newGraph, newStart, newEnd)):
            return [edge] + recEul(newGraph, newStart, newEnd)
    
def find_eulerian_tour(graph):
    graph = sortGraphEdges(graph)
    print 'start:', graph
    for edge in graph:
        newGraph = deleteEdge(graph, edge)
        start = edge[0]
        end = edge[1]
        print edge, newGraph, start, end
        if testTour(newGraph, recEul(newGraph, start, end)):
            tour = [edge] + recEul(newGraph, start, end)
            print tour
            return nodeTour(tour)

print find_eulerian_tour(graph)
