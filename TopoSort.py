#  File: TopoSort.py
#  Student Name: Natalia Ortega
#  Student UT EID: no4432


import sys


# You can use this class as needed.
# Do not change.


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack


# You can use this class as needed.
# Do not change.
class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    def current(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Represents a vertex in a graph.
# Do not change.
class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

    def was_visited(self):
        return self.visited

    def get_label(self):
        return self.label

    def __str__(self):
        return str(self.label)


# Represents a directed graph of vertices and edges.
# It uses a 1D list of vertices and a 2D list for an adjacency matrix.
# Change only the methods specified in comments and instructions.
class Graph:
    def __init__(self):
        self.Vertices = []
        self.adjMat = []


    def initialize_graph(self, vertices_list):
        # Initialize Vertices with Vertex objects
        self.Vertices = [Vertex(label) for label in vertices_list]

        # Initialize adjMat as adjacency matrix filled with zeros
        num_vertices = len(self.Vertices)
        self.adjMat = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]


    # check if a vertex is already in the graph
    def has_vertex(self, label):
        # Check if the graph has a vertex with the given label
        return any(vertex.get_label() == label for vertex in self.Vertices)

    # given a label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return
        # Add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # Add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            self.adjMat[i].append(0)

        # Add a new row for the new vertex
        new_row = [0 for _ in range(nVert)]
        self.adjMat.append(new_row)


    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    def print_graph(self):
        num_vertices = len(self.Vertices)
        print(" ", end=" ")
        for i in range(num_vertices):
            print(self.Vertices[i], end=" ")
        print()
        for i in range(num_vertices):
            print(self.Vertices[i], end=" ")
            for j in range(num_vertices):
                print(self.adjMat[i][j], end=" ")
            print()
        print()

    # helper method for dfs()
    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (
                    not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # helper method for dfs()
    # return list of adjacent vertices to vertex v (index)
    def get_adj_vertexes(self, v):
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0):
                verts.append(i)
        return verts

    # helper method for dfs()
    # returns list of verticies to or from vertex v (index)
    def get_adj_back_forth_vertex(self, v):
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0 or self.adjMat[i][v] > 0:
                verts.append(i)
        return verts

    # needed for has_cycle()
    # do the depth first search in a graph from vertex v (index)
    # also determine if there is a cycle for a given path
    # return True if there is a cycle, False otherwise
    def dfs(self, v, visited, stack):
        visited[v] = True
        stack[v] = True

        for i in range(len(self.Vertices)):
            if self.adjMat[v][i] == 1:
                if not visited[i]:
                    if self.dfs(i, visited, stack):
                        return True
                elif stack[i]:
                    return True

        stack[v] = False
        return False
        # determine if a directed graph has a cycle
        # this function should return a boolean and not print the result

    # determine if the graph has a cycle
    # return true if a cycle exists, false otherwise
    def has_cycle(self):
        num_vertices = len(self.Vertices)
        visited = [False] * num_vertices
        stack = [False] * num_vertices

        for i in range(num_vertices):
            if not visited[i]:
                if self.dfs(i, visited, stack):
                    return True
        return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            u_index = self.vertices.index(u)
            v_index = self.vertices.index(v)
            self.adjMat[u_index][v_index] = 1

    def display(self):
        print(" ", end=" ")
        for v in self.vertices:
            print(v, end=" ")
        print()
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], end=" ")
            for val in row:
                print(val, end=" ")
            print()


    # Additional topo_sort() helper methods

    # return a list of vertices after a topological sort
    # returns an empty list if the graph has a cycle

    def toposort(self):
        if self.has_cycle():
            return []

        in_degree = [0] * len(self.Vertices)
        queue = []
        topo_order = []

        for i in range(len(self.Vertices)):
            for j in range(len(self.Vertices)):
                if self.adjMat[i][j] == 1:
                    in_degree[j] += 1

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            vertex = queue.pop(0)
            topo_order.append(self.Vertices[vertex].get_label())

            for i in range(len(self.Vertices)):
                if self.adjMat[vertex][i] == 1:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)

        return topo_order

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('topo.in')
else:
    in_data = sys.stdin

# create a Graph object
theGraph = Graph()

# read the number of vertices
line = in_data.readline()
line = line.strip()
num_vertices = int(line)

# read the vertices and insert them into the graph
for i in range(num_vertices):
    line = in_data.readline()
    vertex = line.strip()
    theGraph.add_vertex(vertex)

# read the number of edges
line = in_data.readline()
line = line.strip()
num_edges = int(line)

# read the edges and insert them into the graph
for i in range(num_edges):
    line = in_data.readline()
    line = line.strip()
    edge = line.split()
    start = theGraph.get_index(edge[0])
    finish = theGraph.get_index(edge[1])
    theGraph.add_directed_edge(start, finish, 1)

if debug:
    theGraph.print_graph()

# test if a directed graph has a cycle
if (theGraph.has_cycle()):
    print("The Graph has a cycle.")
else:
    print("The Graph does not have a cycle.")

# test topological sort
if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print("\nList of vertices after toposort:")
    print(vertex_list)