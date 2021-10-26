import numpy as np
import copy as cp
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
        Définit la matrice booléenne représentative de la fourmilière en fonction du nombre
        de salles et des différentes liaison entres elles.
        (Taille salle * salle) (0 ou un suivant les connexions entre les salles)
    """
    def set_anthill_matrice(self):
        # Tableau de tuple chaque tuple materialise la liaison entre 2 salles
        neighbors = []
        # Tuple contenant les 2 cases voisines
        pair = ()

        # Créer une matrice de salle * salle rempli de zero
        self.antHillMatrice = np.zeros((self.totalRooms, self.totalRooms))

        # Clean la liste des tunnel et remplace Sv par 0 et Sd par Nombre total de salle -1
        for row in self.tunnels:
            row = re.sub("S|-|", "", row)
            row = re.sub("v", "0", row)
            row = re.sub("d", str((self.totalRooms - 1)), row)
            row = re.split(" ", row)
            row.pop(1)
            print("ROW", row)
            for el in row:

    """
        Affiche la matrice représentative de la fourmilière
    """
    def print_anthill_matrice(self):
        print()
        for row in self.antHillMatrice:
            print(row)
        print()

    """
        Affiche la liste des salles ainsi que leurs emplacements
    """

    def print_anthill_rooms(self):
        print(f"Votre fourmiliere est composée de {self.totalRooms} salles (Vestibule et dortoir inclus). \n")
        print("Liste des salles de la fourmilière:\n")
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
