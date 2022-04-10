from cgi import print_environ
import networkx as nx
import matplotlib.pyplot as plt

def add_one_b_one(graph):
    print("Para parar de adicionar, digite '//'")
    x = str(input(">> "))
    while(x != "//"):
        graph.add_node(x)
        x = str(input(">> "))

    return graph

def add_all(graph):
    print("Digite todos com espaços entre eles")
    x = str(input(">> "))
    v_list = x.split(' ')
    c = 0

    while(c < len(v_list)):
        graph.add_node(v_list[c])
        c = c + 1

    return graph

def add_edge_one_b_one(graph, flag):
    print("Para parar de adicionar, digite '//'")
    x = str(input("Origem >> "))


    while(x != "//"):
        y = str(input("Destino >> "))
        if flag == 1:
            w = str(input("Valor >> "))
            graph.add_edge(x, y, weight=int(w))
        else:
          graph.add_edge(x, y)

        x = str(input("Origem >> "))

    return graph

def adde_all(graph, flag):
    print("Digite todos os valores com espaços entre eles")
    if flag == 1:
        print("Exemplo origem destino valor: v1 v2 4 v2 v3 2")
    else:
        print("Exemplo origem destino: v1 v2 v2 v3")

    x = str(input(">> "))
    v_list = x.split(' ')
    c = 0

    while(c < len(v_list)):
        if flag == 1:
            graph.add_edge(v_list[c], v_list[c+1], weight=int(v_list[c+2]))
            c = c + 3
        else:
            graph.add_edge(v_list[c], v_list[c+1])
            c = c + 2

    return graph
