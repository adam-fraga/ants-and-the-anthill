from networkx.classes.function import neighbors
import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import networkx as nx
import re

from classes.anthClass import Anth
from classes.queueClass import Queue

"""
    Class fourmilière / Anthill Class
"""


class AntHill:
    """
        Prends en paramètre un fichier .txt materialisant la fourmilière.
        Le format et le nom du fichier doivent scrupuleusement respecter le format des fichier passé en ressource.
        Cette approche permet ainsi de rendre l'objet Anthill adaptable et ce peu importe la fourmilière passé paramètre.
        Permet également l'ajout de nouvelles fourmilières dans le dossier anthill.
    """
    def __init__(self, fileTxt: str) -> None:

        self.antHillMatrice = []
        self.antHillGraph = nx.Graph()
        self.antHillFile = fileTxt
        self.totalRooms = None
        self.totalAnt = None
        self.totalTunnels = None
        self.rooms = []
        self.tunnels = []
        self.neighbors = []

        """
            Fonction de nettoyage des données appelée dans le constructeur permet de récupérer les éléments:
            - Nombre de fourmis
            - Salles de la fourmilière et leurs emplacements
            - Tunnels entre les différentes salles de la fourmilière
            Et de les set dynamiquement dans les attributs de la fourmilière
            (Clean Data)
        """
        def set_hill():

            file = re.split('\n', self.antHillFile)

            # Récupère le nombre de fourmis et retire la ligne correspondante
            if file[0][0] == "F":
                self.totalAnt = int(file[0].removeprefix("F="))
                file.pop(0)
            elif file[0][0] == "f":
                self.totalAnt = int(file[0].removeprefix("f="))
                file.pop(0)
            # Condition permettant de palier au problème d'encodage du fichier en base 10 ajoute un

            # Tableau suplémentaire vide en fin de fichier après nettoyage
            if not file[-1]:
                file.pop()

            # La salle 0 correspond au vestibule
            self.rooms.append(0)
            # Pour chaque ligne du fichier fournis
            for el in file:
                # Règle définissant la ligne concernant les salles
                if len(el) == 2 or len(el) == 3 or "{" in el or "}" in el:
                    el = re.sub("S|}|", "", el)
                    el = re.sub(" ", "", el)
                    el = re.sub("{", ",", el)
                    # Sépare les salle de leurs emplacements dans un tableau
                    splitRoom = el.split(",")
                    # Si longueur du split est de 1 alors pas d'emplacement spécifier donc 1 (consigne)
                    if len(splitRoom) == 1:
                        self.rooms.append((int(splitRoom[0]), 1))
                    # Si emplacement len == 2 donc ajoute un tuple d'int (salle, emplacement)
                    else:
                        self.rooms.append((int(splitRoom[0]), int(splitRoom[1])))
            # Si ce n'est pas une salle c'est un tunnel donc ajoute le tunnel dans un tableau
                else:
                    self.tunnels.append(el)
            # Après avoir ajouté toutes les salles ajoute une salle en plus dynamiquement correspondante au dortoir
            self.rooms.append(len(self.rooms))
            # Set le nombre de salles dans l'attribut totalRooms
            self.totalRooms = len(self.rooms)
            # Set le nombre total de tunnel dans l'attribut totalTunnels
            self.totalTunnels = len(self.tunnels)

        """
            Execute la fonction de nettoyage des données dans le constructeur et initialise la fourmilière.
        """
        set_hill()

    """
        Définit les cellules voisines dans un tableau de tuple(int, int), chaque tuple réference le lien entre deux salles
        voisines
    """
    def set_neighbors(self):
        # Clean la liste des tunnel et remplace Sv par 0 et Sd par Nombre total de salle -1
        for row in self.tunnels:
            row = re.sub("S|-|", "", row)
            row = re.sub("v", "0", row)
            row = re.sub("d", str((self.totalRooms - 1)), row)
            row = re.split(" ", row)
            row.pop(1)
            self.neighbors.append((int(row[0]), int(row[1])))

    """
        Définit le graphe de la fourmiliere sous forme d'objet networkX
    """

    def set_anthill_graph(self):
        # Itère sur la liste de tuple (room, emplacement)
        for room in self.rooms:
            # Definit les différents attributs utilitaire à la gestion des salles pour VS et SD dans le grap
            if room == 0 or room == (self.totalRooms - 1):
                self.antHillGraph.add_node(room, visited=False, slot="infinite", ants=[], dist=None)
            # Definit les attributs utilitaire pour le reste des salles dans le graphe
            else:
                self.antHillGraph.add_node(room[0], visited=False, slot=room[1], ants=[], dist=None)

        # Passe la liste de tuples correspondant aux voisins pour définir les tunnels (edges) du graphe
        self.antHillGraph.add_edges_from(self.neighbors)

    """
        Affiche les informations de la fourmilière:
        Nombre d'individus, nombre de salles et leurs emplacements, nombre de tunnel et leurs liaisons...
    """

    def print_anthill_data(self):
        print(f"\nNombre de fourmis: {self.totalAnt}.")
        print(f"\nListe des salles et leurs emplacements {self.antHillGraph.nodes.data()}.")
        print(f"\nNombre de tunnels {self.antHillGraph.edges}.")
        print(f"\nListe des tunnels de la fourmilière: {self.antHillGraph.edges.data()}")

    """
        Représentation graphique de la fourmilière avec networkX et matplotlib
    """
    def draw_anthill(self):

        # Titre du graphique
        plt.title("Représentation Graphique D'une fourmilière")

        # Layout du graphique spring plus lisible pour fourmilière minimise les croisements et éparpille les salles
        nx.draw_spring(self.antHillGraph, with_labels=True)

        # Affiche le graphique après execution de la console
        plt.show()

    def get_shortest_way(self) -> None:

        # Graphe networkX
        G = self.antHillGraph
        relations = []
        # Compteur de distance
        dist = 0


        # Parcourt les salles de la fourmilière
        for i in G.nodes():
            print("IIIIII", i)

            # Vestibule
            if i == 0:
                print("Vestibule")

                # Définit la distance du vestibule (départ à 0 de lui même)
                G.nodes[0]["dist"] = dist
                G.nodes[0]["visited"] = True

                # Ajoute dans un dictionnaire les relation parenté entre les salles ainsi que leur distance
                relation = {"Room": i, "Neighbors": [x for x in list(G.neighbors(i))], "Distance": dist}
                relations.append(relation)

                # Passe la distance à 1 pour les cases suivantes
                dist = 1

            else:
                print("SALLE", i)
                # Si la salle n'est pas visité et qu'il ne s'agit pas du vestibule
                if G.nodes[i]["visited"] is not True:
                    print("La salle n'est pas encore visité")

                    # Ajoute dans un dictionnaire les relation parenté entre les salles ainsi que leur distance
                    relation = {"Room": i, "Neighbors": [x for x in list(G.neighbors(i))], "Distance": dist}
                    relations.append(relation)

                    # Pour chaque voisins le définit comme visité si non visité et définit sa distance vis à vis de VS
                    # Puis le stock dans une file.
                    for n in list(G.neighbors(i)):
                        print("Pour le voisin", n)
                        G.nodes[n]["dist"] = dist
                        G.nodes[n]["visited"] = True

                    # Augmente la distance de 1
                    dist += 1

                    # Debug affiche la file
            print("Tableau de salle parentes", relations)
            input()

        # print("G de n", G.nodes[i])
        # print("ADJACENTS", G.adj)


# For room in graphe parcourt room
    # Définit la distance de la premiere case à 0 car 0 d'elle même et la set comme visité
    # Vérifie tout les voisins (NON VISITés) de la case courante les définit a distance 1
    # Les définit comme visités
    # Les enregistre dans une File (Node et arêtes)
    # Les definit comme étant visité et les ajoutent dans la file
    # Vérifie les voisins de toute les cases à distance 1 traités précédement
    # Leur applique une distance de 2, les définit comme visités, les enregistre dans une file etc...
