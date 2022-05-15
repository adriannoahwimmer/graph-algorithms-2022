"""This Algorithm creates a minimal spanning three to a conected input graph """
import copy
from graafi3 import Graph

def MSTCYCLE(g):
    es = g.AL
    col = [None for _ in range(g.nV)]  # creating an array with all the colours
    p = [None for _ in range(g.nV)]  # creating an array with all the parent of the nodes
    u = g.nV
    cycleAll = []

    for x in range(0,
                   (int)(g.nE / 2) - g.nV + 1):  # doing the loop Edges-Nodes +1 times to delete all the useless edges
        for u in range(0, g.nV):  # making the col array white and the parrents array nil
            col[u - 1] = "white"
            p[u - 1] = 'Nil'

        def DFSCYCLE(u):
            col[u - 1] = 'gray'  # node were the algortih have been getting gray
            for v in g.AL[u]:
                if col[v - 1] == 'white':  # if the algorithm not have been there
                    p[v - 1] = u  # make the new node parent node the node were you have been from
                    e = DFSCYCLE(v)  # going to the new node
                    if e != '':  # if it is something in e give it back
                        return e
                else:
                    if col[v - 1] == 'gray' and p[u - 1] != v:  # if you find a cycle give it back
                        return u, v
            col[u - 1] = 'black'  # if you went to a node were you are not able to find a cycle
            return ''
            pass

        e = DFSCYCLE(u)

        # find the circle and write it in the list called cycle
        y = e[0]  # take the first node of the edge which is part of a cycle
        cycle = []
        cycle.append(e[0])  # add the first node of the edge which is part of a cycle to the cycle list
        while (y != e[1]):  # so long y is not the second node of the edge which is part of the cycle
            y = p[y - 1]  # get parent node
            if (y == 'Nil'):  # if we got to the starting node break
                break
            cycle.append(y)  # add the node to the cycle list
        #  collect the detected cycles
        cyclef = copy.deepcopy(cycle)
        cyclef.append(cycle[0])
        cycleAll.append(cyclef)

        # find the biggest edge of the cycle
        cycleW = []  # cycle weight list
        for l in range(0, cycle.__len__() - 1):  # copy all the weights to the cycle weight list
            cycleW.append(g.W[(cycle[l], cycle[l + 1])])
        cycleW.append(g.W[(cycle[0], cycle[cycle.__len__() - 1])])

        max_value = max(cycleW)
        # remove the edge from the es dictionary
        if cycleW.index(max_value) == cycleW.__len__() - 1:  # if they last edge of the cycle edge is to edge which we
            # want to delete then we have to do in differently
            es[cycle[cycleW.index(max_value)]].remove(cycle[0])
            es[cycle[0]].remove(cycle[cycleW.index(max_value)])
        else:
            es[cycle[cycleW.index(max_value)]].remove(cycle[cycleW.index(max_value) + 1])
            es[cycle[cycleW.index(max_value) + 1]].remove(cycle[cycleW.index(max_value)])
    return es, cycleAll

if __name__ == "__main__":  # main function
    g = Graph('test_graphs/G04PythonMST.txt')  # please write the wanted graph in

    mst, detectedCycles = MSTCYCLE(g)
    print("Final MST:")
    print(mst)
    print("Detected Cycles")
    print(detectedCycles)

