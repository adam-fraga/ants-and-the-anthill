from ssl import Options
from IPython.core.pylabtools import figsize
import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import networkx as nx
import re


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
    def __init__(self, anthillDotTxt: str) -> None:

        self.antHillMatrice = []
        self.antHillFile = anthillDotTxt
        self.totalRooms = None
        self.totalAnt = None
        self.totalTunnels = None
        self.rooms = None
        self.tunnels = None
        self.neighbors = []

        """
            Fonction de nettoyage des données appelée dans le constructeur permet de récupérer les éléments:
            - Nombre de fourmis
            - Salles de la fourmilière
            - Tunnels entre les différentes salles de la fourmilière )
            Et de les set dynamiquement dans les attributs de la fourmilière
            (Clean Data)
        """
        def set_hill():

            file = re.split('\n', self.antHillFile)
            rooms = []
            tunnels = []

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
            rooms.append(0)
            for el in file:
                if len(el) == 2 or len(el) == 3 or "{" in el or "}" in el:
                    el = re.sub("S|}|", "", el)
                    el = re.sub(" ", "", el)
                    el = re.sub("{", ", ", el)
                    rooms.append(el)
            # Récupère le nombre de tunnels/relations entre les salles dans un tableau
                else:
                    tunnels.append(el)
            # Après avoir ajouté toute les salle ajoute une salle en plus dynamiquement correspondant au dortoir
            rooms.append(len(rooms) + 1)
            # Set le nombre de salles (sommets du graphe)
            self.totalRooms = len(rooms)
            # Chemins/porte (arête du graphe)
            self.totalTunnels = len(tunnels)
            # Set les différentes salles ainsi que leurs emplacement dans un tableau
            self.rooms = rooms
            # Set les différentes relations entre les salles dans un tableau
            self.tunnels = tunnels

        """
            Execute les fonctions de nettoyage des données dans le constructeur et initialise la fourmilière.
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
        Initialise une matrice booléenne correspondant à la fourmilière passé en paramètre,
        de salles * salles. (Correspond au graphe de la fourmilière sous forme de matrice)
        Les 0 et 1 materialise les liaisons entre les salles 1 = salle connecté, 0 = Pas de connexion.
    """
    def set_anthill_matrice(self):
        # Créer une matrice de salle * salle rempli de zero
        self.antHillMatrice = np.zeros((self.totalRooms, self.totalRooms))

        # Parcourt la matrice et initialise 1 si 2 salles sont voisine en vérifiant dans le
        # Tableau de tuples initialiser au préalable (neighbors)
        for x in range(self.totalRooms):
            for y in range(self.totalRooms):
                # print("x, y: ", (x, y))
                # print("Position courante", self.antHillMatrice[x][y])
                for n in self.neighbors:
                    if x == n[0] and y == n[1]:
                        self.antHillMatrice[x][y] = 1
        print("Félicitation! Votre fourmilière à bien été générée!")

    """
        Affiche la matrice représentative de la fourmilière
    """
    def print_anthill_matrice(self):
        print()
        print("Matrice booléenne de la fourmilière")
        for row in self.antHillMatrice:
            print(row)
        print()

    """
        Donne le nombre de fourmis, la liste des salles ainsi que leurs emplacements
    """

    def print_anthill_rooms(self):

        print(f"\nVotre fourmiliere est composée de {self.totalAnt} individus. \n")
        print(f"Votre fourmiliere est composée de {self.totalRooms} salles.")
        print("(Vestibule = 0, dortoire = dernière salle)")
        try:
            for room in self.rooms:
                print(room)
        except Exception as e:
            print("Impossible de trouver les salles de votre fourmilière.\n")
            print(e)

    """
        Affiche les relations/tunnels entre les salles de la fourmilières
        (Fonction de debogage permet de visualiser les relations entre les salles)
    """

    def print_anthill_tunnel(self):
        print(f"Votre fourmiliere est composée de {self.totalTunnels} tunnels. \n")
        print("Liste des tunnels de la fourmilière:")
        try:
            for tunnel in self.tunnels:
                print(tunnel)
        except Exception as e:
            print("Impossible de trouver les salles de votre fourmilière")
            print(e)

    """
        Affiche graphiquement les salles de la fourmilière et leurs différentes liaison
        avec le module networkx et matplotlib
    """
    def draw_anthill(self):
        # Initialise le Graphe networkX
        G = nx.Graph()
        # Construit un iterable du nombre de salles incluant sv et sd
        H = nx.path_graph(self.totalRooms)
        print("H", H)
        # Permet l'ajout dynamique de plusieurs noeuds (verticles) dans le graphe nx
        G.add_nodes_from(H)
        # Le nettoyage de la liste de tuples contenu dans neighbors permet l'insertion de toutes les relations
        # (edges) directement dans la methode ci dessous.
        G.add_edges_from(self.neighbors)

        # Choix du spring pour plus de visibilité et éviter les croisements entres les salles
        plt.figure(figsize(10, 8))

        # Titre du graphique
        plt.title("Représentation Graphique D'une fourmilière")

        # Layout du graphique spring plus lisible pour fourmilière minimise les croisements et éparpille les salles
        nx.draw_spring(G, with_labels=True)

        # Affiche le graphique après execution de la console
        plt.show()
