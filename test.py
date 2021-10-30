from certifi import contents
import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import networkx as nx
import random as rn
import re

"""
    Help lib networkx
"""


G2 = nx.Graph()

# Ajouter 1 node
G2.add_node(0)
# Ajouter plusieurs nodes Ajouter 1 à 300 possible avec range()
G2.add_nodes_from([1, 2, 3])

# Ajouter edges
G2.add_edge(0, 1)
# Ajouter plusieurs edges (Liste de tuples passé en paramètre)
G2.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Nombre de sommet et d'arêtes du graphe
print("Number of nodes ", G2.number_of_nodes())
print("Number of edges ", G2.number_of_edges())

# Views

# Liste des nodes
print("G2.nodes ", G2.nodes())
# Liste des edges
print("G2.edges ", G2.edges())
# Liste des degrés
print("G2.degree ", G2.degree())

"""
 Dictionnaire de profondeur 3
 1er niveau de profondeur correspond à la clés du node
 2ème dictionnaire correspond aux différent noeud adjacents (neighbors)
 3 ème correspond aux attributs de l'arête (edge), entre le node du 1er niveau et celui du 2ème et contient donc
 Nom de l'attribut: Valeur de l'attribut
"""
print("G2.adj ", G2.adj, "\n\n")


# Ajouter des attributs dans les noeuds
for i in G2.nodes:
    G2.nodes[i]["smoking"] = False
    G2.nodes[i]["weight"] = rn.choice(range(100, 200))
G2.nodes[1]["smoking"] = True
print("NODES DATA", G2.nodes.data(), "\n\n")

# AJouter des attributs dans les arêtes
for i in G2.edges:
    G2.edges[i]["strength"] = round(rn.random(), 2)
print("NODES DATA", G2.edges.data(), "\n\n")
print("ADJ", G2.adj, "\n\n")

# Itere sur les cellules adjacentes d'un noeuds (neighbors) eutre syntaxe possible mais celle ci = plus lisible
print("Voisins de sommet 2")
for adj in G2.neighbors(2):
    print(adj)

# G = nx.Graph()

# # Permet d'ajouter X nodes d'un seul coups
# H = nx.path_graph(5)

# # On ajoute ensuite les Node dans le graphe G
# G.add_nodes_from(H)


# x = np.linspace(0, 2, 10)
# y = x ** 2

# print("X", x)
# print("Y", y)
# # On peut passer des parametre comme la taille
# plt.figure(figsize(12, 8))
# plt.scatter(x, y, label="quadratique")
# plt.plot(x, x**3, label="cubique")

# plt.title("MatplotlibTest")
# plt.xlabel("axe X")
# plt.ylabel("axe Y")
# plt.legend()

# plt.show()
# # Sauvegarde la figure dans le repertoire courant
# plt.savefig("figure.png")
# # Créer une nouvelle figure
# plt.figure()

# print(type(G))
# print(list(G.nodes()))
