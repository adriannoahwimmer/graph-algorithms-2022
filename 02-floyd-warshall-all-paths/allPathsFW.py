""" Function to create a path matrix for all existing minimal weighted graphs """

from graafi3 import Graph
import numpy as np
import argparse

"""Implementation function allPathsFW"""
#Input: graph_filename: name of the file with the graph
#Output: path matrix

def allPathsFW(filename):
    g = Graph(filename)
    # Floyd Warshall Algorithm
    d = [[0 for i in range(len(g.V))] for j in range(len(g.V))] #Distance Matrix
    p = [[float('inf') for i in range(len(g.V))] for j in range(len(g.V))] #Parent Matrix minimal path
    #Initialization
    for u in g.V:
        for v in g.V:
            if u == v:
                d[u-1][u-1] = 0          #distance between the same vertices is 0
                p[u-1][u-1] = float('inf')  #parent of the same vertices is inf
            else:
                d[u-1][v-1] = float('inf')  # distance between two different vertices is inf

    # Add the start weights in the distance matrix and the parent of v in the parent matrix
    for item in g.W:
        ver = str(item).split(", ")
        u = int(ver[0].strip("()"))
        v = int(ver[1].strip("()"))
        d[u-1][v-1] = g.W[item]
        p[u-1][v-1] = u

    #Check if ther is a smaller way across vertex k,if so, update the distance matrix and parent matrix
    for k in g.V:
        for i in g.V:
            for j in g.V:
                if d[i-1][j-1] > (d[i-1][k-1] + d[k-1][j-1]):  #smaller way?
                    d[i-1][j-1] = (d[i-1][k-1] + d[k-1][j-1])  #so change distance
                    p[i-1][j-1] = p[k-1][j-1]                  #and parent


    edges_m = np.zeros([len(g.V),len(g.V)]) #Matrix of edges which don't belong to a minimal weighted path (Index 1/0)
    # With a 1 by edges_m[i][j], there is no minimal weighted path from i to j

    #Condition 1: Look which edges don't belong to a minimal weighted path, in accordance to condition 1.
    for i in range(len(d)):
        for j in range(len(d)):
            if d[i][j] == float('inf'):
                edges_m[i][j] = 1
    # Condition 2: Look which edges don't belong to a minimal weighted path, in accordance to condition 2.
    for i in range(len(d)):
        if d[i][i] < 0:
            for j in range(len(d)):
                edges_m[i][j] = 1
                edges_m[j][i] = 1

    # Condition 3: Look which edges don't belong to a minimal weighted path, in accordance to condition 3.
    for i in range(len(d)):
        for j in range(len(d)):
            if d[i][j] != float('inf'):
                for k in range(len(d)):
                    if d[k][k]<0 and d[i][k] != float('inf') and d[k][j] != float('inf'):
                        edges_m[i][j] = 1

    #Create Path matrix
    Path = [['<>' for i in range(len(g.V))] for j in range(len(g.V))]


    #For all existing minimal weigthed graphs (edges_m index = 0) find minimal weighted path with while condition
    for i in range(len(edges_m)):
        for j in range(len(edges_m)):
            if edges_m[i][j] == 0:
                path = []
                x = j+1
                path.insert(0, str(x))
                while x != (i+1):
                    x = int(p[i][x-1])
                    path.insert(0, str(x))  #insert vertex on the left side
                path_str = '<'+",".join(path)+'>'
                Path[i][j] = path_str

    print(np.matrix(Path)) #Print matrix



if __name__ == "__main__":
    filename = 'test_graphs/G03PythonFW.txt' #Put you input graph here
    allPathsFW(filename)  #compute path matrix
