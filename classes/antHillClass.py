import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import networkx as nx
import re

from classes.anthClass import Anth

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
            # Si il s'agit du dortoir ou du vestibule ajoute simplement la salle dans un node ntwrkx
            # Et definit "infinite" dans slot (nombre de places)
            if room == 0 or room == (self.totalRooms - 1):
                self.antHillGraph.add_node(room, slot="infinite", anths=[])
            # Sinon ajoute un attribut slot materialisant le nombre de places disponibles dans chaque salle
            else:
                self.antHillGraph.add_node(room[0], slot=room[1], anths=[])

        # Neighbors contenant une liste de tuples qui materialise la relation entre les salles
        # Passe cette liste à la methode suivante pour définir les edges.
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

    def get_way(self) -> None:

        # Graphe networkX
        G = self.antHillGraph

        # Définit les nodes vestibule et dortoire dans des variables
        vs = G.nodes[0]
        sd = G.nodes[len(G.nodes) - 1]

        # Les fourmis entrent dans le vestibule
        for x in range(self.totalAnt):
            anth_id = 1
            anth = Anth(anth_id)
            vs["anths"].append(anth)
            anth_id += 1

        # Set les salles à non visités
        for n in G.nodes():
            G.nodes[n]["visited"] = False
            print("Noeuds du graphes", G.nodes[n])
            print("EDGES", G[n])

        print("ADJACENTS", G.adj)
