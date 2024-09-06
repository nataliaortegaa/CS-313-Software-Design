#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Natalia Ortega
#  Student UT EID: no4432
#  Course Name: CS 313E
#  Unique Number: 52600

import sys


def edge_to_adjacency(edge_list):

    vertices = sorted({vertex for edge in edge_list for vertex in edge[:2]})


    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}


    size = len(vertices)
    adj_matrix = [[0 for _ in range(size)] for _ in range(size)]


    for from_vertex, to_vertex, weight in edge_list:
        i, j = vertex_index[from_vertex], vertex_index[to_vertex]
        adj_matrix[i][j] = weight

    return adj_matrix


# remove formatting and convert to list of tokens
# do not change this method
def clean(text):
    text = text.strip()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("”", "")
    text = text.replace(" ", "")
    text = text.replace("\"", "")
    text = text.split(",")
    return text


''' DRIVER CODE '''

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('adjacency.in')
else:
    in_data = sys.stdin

# get line of input, remove formatting, convert to list of tokens
input_text = in_data.readline()
input_text = clean(input_text)

# convert one string to 2D list of edge data
edges = []
for i in range(0, len(input_text), 3):
    newList = [input_text[i], input_text[i+1], int(input_text[i+2])]
    edges.append(newList)

# convert the 2D list to an adjacency matrix
adj_matrix = edge_to_adjacency(edges)

print('\n'.join([' '.join([str(cell) for cell in row]) for row in adj_matrix]))
