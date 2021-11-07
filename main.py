import re
import numpy as np

from classes.antHillClass import AntHill

# Just for fun
print(" \n\n Bienvenue dans votre générateur de fourmilière! \n\n")
print("  \\(\")/", "  \\(\")/", "  \\(\")/")
print("  -( )-", "  -( )-", "  -( )-")
print("  /(_)\\", "  /(_)\\", "  /(_)\\ \n\n")

"""
    Ajout de modularité au programme parse le fichier fourmilière.txt passé
    (Celui ci doit se situer dans le dossier anthill).
    Récupère ainsi dynamiquement:
    Le nombre de fourmis, Le nombre de salle, Les emplacements des salles ainsi que les relations entres celle ci.
"""


# Récupère le nom du fichier
fileName = str(input("Entrer le nom du fichier matérialisant les relations de votre fourmilière.\n\n !!!ATTENTION!!!\n\nVotre fichier doit se trouver dans le dossier anthill, être au format .txt, se nommer \"fourmiliere_x.txt \",\npour x le nombre de la fourmilière en toutes lettre, et répondre aux normes imposés.\n(Voir les éxemples de fourmilière présentent dans le dossier anthill.)\n"))

"""
    Ouvre le fichier correspondant à la fourmilière dans le dossier anthill.
    Si il éxiste initialise la fourmilière dans le constructeur de la class antHill.
    Sinon génère une exception.
"""
try:
    file = open(f"anthill/{fileName}", "r")
    strFile = file.read()
except Exception as e:
    print("Le nom de votre fourmilière n'éxiste pas, Vérifier son ortographe ou sa présence dans le dossier \"anthill\"")
    print(e)

# Init la fourmiliere
hill = AntHill(strFile)

# Initialise les cellules voisine dans un tableau de tuples (int, int)
hill.set_neighbors()

# Initialise le graphe de la fourmilière avec networkX
hill.set_anthill_graph()

# Déssine les salles de la fourmilière ainsi que leur tunnels
hill.draw_anthill()

# Affiche les information concernant les Salles de la foumilière
hill.print_anthill_data()

i = 0
dist = 0
hill.fastest_way(dist, i)
