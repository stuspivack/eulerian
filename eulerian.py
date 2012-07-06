# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
graph = [(1,2),(4,3),(2,3), (4,5), (5,1)]
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
    nextEdges = filter( (lambda edge: edge[0] == start or edge[1] == start), graph)
    for edge in nextEdges:
        if edge[0] == end or edge[1] == end:
            return [edge]
    for edge in nextEdges:
        newGraph = deleteEdge(graph, edge)
        if edge[0] == start:
            newStart = edge[1]
        else:
            newStart = edge[0]
        if testTour(newGraph, recEul(newGraph, newStart, end)):
            return [edge] + recEul(newGraph, newStart, end)
    
def find_eulerian_tour(graph):
    graph = sortGraphEdges(graph)
    print 'start:', graph
    for edge in graph:
        newGraph = deleteEdge(graph, edge)
        start = edge[0]
        end = edge[1]
        if testTour(newGraph, recEul(newGraph, start, end)):
            tour = [edge] + recEul(newGraph, start, end)
            return nodeTour(tour)

print find_eulerian_tour(graph)
