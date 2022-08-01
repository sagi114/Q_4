import numpy as np
import networkx as nx

def turn_to_matrix(Graph):
    n=len(Graph)
    matrix=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(len(Graph[i])):
           index=Graph[i][j]
           matrix[i][index]=1
    matrix=np.array(matrix)
    return matrix

def connected_comp(G):
    matrix = turn_to_matrix(G)
    g = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
    comp_list = list(nx.weakly_connected_components(g))
    comp_list=[list(element) for element in comp_list]
    comp_list.sort(key=len)
    l=len(max(comp_list,key=len))
    #we will return as a tuple 2 different objects
    return comp_list,l

"""""
if __name__ == '__main__':
    G=[[1, 3], [0], [3], [2, 0], []]
    print(connected_comp(G))
"""""