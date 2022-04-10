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

#CRUD VÉRTICE
print("\n1 - Adicionar vértices um a um")
print("2 - Adicionar vértices em bloco")
i = int(input(">> "))

if i == 1:
    Graph = add_one_b_one(Graph)

elif i == 2:
    Graph = add_all(Graph)

#CRUD ARESTA
print("\n1 - Adicionar arestas um a um")
print("2 - Adicionar arestas em bloco")
i = int(input(">> "))

#CRUD ARESTA VALORADO
print("\n1 - Valorado")
print("2 - Não Valorado")
j = int(input(">> "))

if i == 1:
    Graph = add_edge_one_b_one(Graph, j)

if i == 2:
    Graph = adde_all(Graph, j)


print("Grafo finalizado!")

nx.draw_networkx(Graph)
print(Graph.nodes())
print(Graph.edges())

pos = nx.spring_layout(Graph)
nx.draw_networkx(Graph,pos)
labels = nx.get_edge_attributes(Graph,'weight')
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)

from numpy.ma.core import append
#CRUD OPÇÕES
while (i != 0):
    print("\nManipulação do grafo")
    print("0 - Finalizar")
    print("1 - Checar ordem e tamanho")
    print("2 - Checar adjacentes de um vértice")
    print("3 - Checar grau de um vértice")
    print("4 - Checar adjacencia entre dois vértices")
    print("5 - Checar caminho mais curto entre dois vértices")
    i = int(input(">> "))

    # Dado um par de vértices, o sistema deverá retornar a informação do caminho mais curto entre eles, tanto o valor do custo do menor caminho entre os dois vértices como a sequência de vértices deste menor caminho entre eles.
    #Pode-se considerar que os pesos das arestas são sempre números positivos (não há arestas com pesos negativos)

    if i == 1:
        print("Ordem: ", len(Graph.nodes()))
        print("Tamanho: ", len(Graph.edges()))

    elif i == 2:
        vortex = str(input("Vértice >> "))

        if d == 2:
          print("Vertices adjacentes: ", len(Graph[vortex]))

        else:
          inside = []
          outside = []
          for x in Graph.edges():
            if vortex in x[1]:
              inside.append(x)
            elif vortex in x[0]:
              outside.append(x)

          print("Vertices adjacentes: ", len(outside) + len(inside))

          print("Saída: ", outside)
          print("Entrada: ", inside)

    elif i == 3:
        vortex = str(input("Vértice >> "))
        inside = []
        outside = []
        for x in Graph.edges():
          if vortex in x[1]:
            inside.append(x)
          elif vortex in x[0]:
            outside.append(x)

        print("Grau do vértice: ", len(outside) + len(inside))

        print("Grau de adjacência de entrada: ", len(inside))
        print("Grau de adjacência de saída: ", len(outside))


    elif i == 4:
        vortex = str(input("Vértices >> "))
        verticies = vortex.split()
        inside = []
        outside = []
        for x in Graph.edges():
          if verticies[0] in x[0] and verticies[1] in x[1]:
            inside.append(x)
          elif verticies[1] in x[0] and verticies[0] in x[1]:
            outside.append(x)

        if len(inside) == 0 and len(outside) == 0:
            print("Não são adjacentes")
        else:
            if len(inside) > 0:
              print("São adjacentes, de modo que", verticies[0]," aponta para", verticies[1])
            if len(outside) > 0:
              print("São adjacentes, de modo que ", verticies[1]," aponta para", verticies[0])


    elif i == 5:
        vortex = str(input("Vértices >> "))
        verticies = vortex.split()
        short_way = nx.shortest_path(Graph, source=verticies[0], target=verticies[1], weight='weight', method='dijkstra')
        print("Caminho:", short_way)
        if j == 1:
          weight_short = nx.shortest_path_length(Graph, source=verticies[0], target=verticies[1], weight='weight', method='dijkstra')
          print("Custo:", weight_short)
