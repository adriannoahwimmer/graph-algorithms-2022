""" This algorith creates all minimal spanning tree of an input graph """
from graafi3 import Graph  # import the helping class graph
from itertools import product  # import to calculate cartesian product


def allMinSpanT(g, s):
    pnl = [[] for _ in range(g.nV)]  # creating a list with the same amount of entries as there are vertices,
    # each entrie is also a vertices
    B = {s: 0}  # setting the distance for the starting vertices to zero
    Q = [s]  # adding the starting vertices to the que Q
    pnl[s - 1].append('Nil')  # setting the parent of starting vertices to Nil

    while Q:  # while something is in Q
        u = Q.pop(0)  # take an element after FIFO principal
        d = B[u]  # store the distance of this vertices in d
        try:  # do this
            for v in g.adj(u):  # for each vertex v that is next to u
                if not v in B:  # if we not already have a distance for v
                    B[v] = d + 1  # add the distance of v, which is 1 more than u
                    Q.append(v)  # adding the new vertices to the que
                    pnl[v - 1].append(u)  # storing one parent vertices of the new vertices v in pnl
                else:  # if we already have a distance for v
                    if B[v] == B[u] + 1:  # checking whether the already noted vertices has the same distance as the new
                        pnl[v - 1].append(u)  # adding the new parent vertex to the list
        except:
            pass

    x = 1
    for elm in product(*pnl):  # calculating cartesian product
        file = open("tree_{0}.txt".format(x), "w")  # creating a file
        C = {}
        y = 1
        for y in range(1, g.nV + 1):  # bringing the trees in a right formation
            C[y] = elm[y - 1]
            y = y + 1
        file.write(str(C))  # writing the dictionary's in text files
        x = x + 1
        print(str(C))


if __name__ == "__main__":  # main function
    g = Graph('test_graphs/G03Python.txt')  # creating a graph
    allMinSpanT(g, 4)
