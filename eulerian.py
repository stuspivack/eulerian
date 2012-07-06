# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
##graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5), (2,5),(2,6),(5,6),(1,7),(1,8),(2,7),(2,8)]
##graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5), (2,5),(2,6),(5,6)]
##graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)]
##graph = [(1,2),(2,3),(3,1)]
##graph = [(1,2),(2,3),(3,4),(4,5),(1,5)]
##graph =  [(1, 2), (1,4), (2, 3), (2,4), (2,5), (3,4), (3,5), (3,6), (4,6)]
##graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
##graph = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (1, 4), (5, 2), (2, 4), (5, 3)]
graph = [(1, 2), (2, 3), (4, 3), (5, 4), (5, 6), (6, 7), (7, 1), (2, 7), (7, 3), (1, 4), (4, 2), (5, 2), (1, 5), (6, 3), (6, 2)]

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

#def deleteEdge(graph, edgeToDel):


def testTour(graph, tour):
    goodTest = True
    for edge in graph:
        if edge not in tour:
            goodTest = False
    for edge in tour:
        if edge not in graph:
            goodTest = False
    return goodTest
     
def recEul(graph, traversed):
    latestEdge = traversed[-1]
    if len(traversed) == 1:
        leadingNode = latestEdge[1]
    else:
        if latestEdge[0] in traversed[-2]:
            leadingNode = latestEdge[1]
        else:
            leadingNode = latestEdge[0]
    nextEdges = []
    for edge in graph:
        if edge not in traversed:
            if edge[0] == leadingNode or edge[1] == leadingNode:
                nextEdges.append(edge)
    for edge in nextEdges:
        newTraversed = traversed + [edge]
        if testTour(graph, newTraversed):
            return [edge]
    for edge in nextEdges:
        newTraversed = traversed + [edge]
        if recEul(graph, newTraversed):
            if testTour(graph, newTraversed + recEul(graph, newTraversed)):
                return newTraversed + recEul(graph, newTraversed)

     
def find_eulerian_tour(graph):
    graph = sortGraphEdges(graph)
    # pick a starting edge
    edge = graph[0]
    traversed = [edge]
    tour = recEul(graph, traversed)
    realTour = tour[-len(graph):]
    return nodeTour(realTour)

print find_eulerian_tour(graph)
