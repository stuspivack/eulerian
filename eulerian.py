# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# graph = [(1,2),(2,3),(3,1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

import networkx as nx
import matplotlib.pyplot as plt
import random

def draw_graph(graph):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges  
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # draw graph
    nx.draw(G)

    # show graph
    plt.show()

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

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print "Node %s has odd degree" % node
                return False
        except KeyError:
            print "Node %s was not in your tour" % node
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print "Your graph wasn't connected"
        return False
     
def deleteEdge(edge, graph):
    newGraph = []
    for newEdge in graph:
        if newEdge != edge:
            newGraph.append(newEdge)
    return newGraph

def numNodes(graph):
    nodes = []
    for edge in graph:
        for node in edge:
            if node not in nodes:
                nodes.append(node)
    return len(nodes)

def find_eulerian_tour(graph):
    graph = sortGraphEdges(graph)
    traversed = []
    while len(traversed) < len(graph):
        edge = graph[0]
        traversed = [edge]
        startNode = edge[0]
        endNode = edge[1]
        workingGraph = deleteEdge(edge, graph)
        while workingGraph:
##            print 'traversed, graph:', traversed, workingGraph
            goodEdges = []
            for goodEdge in workingGraph:
                if (goodEdge[0] == endNode or goodEdge[1] == endNode):
                    goodEdges.append(goodEdge)
            if all([edge in traversed for edge in goodEdges]):
                break
            betterEdges =[]
            for betterEdge in goodEdges:
                nextGraph = deleteEdge(betterEdge, workingGraph)
                if nextGraph:
                    if numNodes(nextGraph) == len(connected_nodes(nextGraph)):
                        betterEdge.append(betterEdge)
            if betterEdges:
                nextEdge = random.choice(betterEdges)
            elif goodEdges:
                nextEdge = random.choice(goodEdges)
            else:
                break
            traversed.append(nextEdge)
            workingGraph = deleteEdge(nextEdge, workingGraph)
            startNode = endNode
            if nextEdge[0] == endNode:
                endNode = nextEdge[1]
            else:
                endNode = nextEdge[0]
    return nodeTour(traversed)

##graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5), (2,5),(2,6),(5,6),(1,7),(1,8),(2,7),(2,8)]
##graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5), (2,5),(2,6),(5,6)]
##graph = [(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)]
##graph = [(1,2),(2,3),(3,1)]
##graph = [(1,2),(2,3),(3,4),(4,5),(1,5)]
##graph =  [(1, 2), (1,4), (2, 3), (2,4), (2,5), (3,4), (3,5), (3,6), (4,6)]
##graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
##graph = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (1, 4), (5, 2), (2, 4), (5, 3)]
##graph = [(1, 2), (2, 3), (4, 3), (5, 4), (5, 6), (6, 7), (7, 1), (2, 7), (7, 3), (1, 4), (4, 2), (5, 2), (1, 5), (6, 3), (6, 2)]
graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]

print find_eulerian_tour(graph)
draw_graph(graph)

