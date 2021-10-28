from IPython.core.pylabtools import figsize
import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import networkx as nx
import re

G = nx.Graph()
# Permet d'ajouter X nodes d'un seul coups
H = nx.path_graph(5)
# On ajoute ensuite les Node dans le graphe G
G.add_nodes_from(H)

x = np.linspace(0, 2, 10)
y = x ** 2

print("X", x)
print("Y", y)
# On peut passer des parametre comme la taille
plt.figure(figsize(12, 8))
plt.scatter(x, y, label="quadratique")
plt.plot(x, x**3, label="cubique")

plt.title("MatplotlibTest")
plt.xlabel("axe X")
plt.ylabel("axe Y")
plt.legend()

plt.show()
# Sauvegarde la figure dans le repertoire courant
plt.savefig("figure.png")
# Créer une nouvelle figure
plt.figure()

# print(type(G))
# print(list(G.nodes()))
