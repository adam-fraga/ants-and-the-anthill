import numpy as np
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
        self.totalRoom = None
        self.totalAnt = None
        self.totalDoors = None
        self.rooms = None
        self.relations = None

        """
            Fonction appelé dans le constructeur permet de récupérer les éléments:
            - Nombre de fourmis
            - Salles de la fourmilière
            - Relations entre les différentes salles de la fourmilière
            Et de les set dynamiquement dans les attributs de la fourmilière
        """
        def set_hill():

            file = re.split('\n', self.antHillFile)
            rooms = []
            relations = []

            # Récupère le nombre de fourmis et retire la ligne correspondante
            if file[0][0] == "F":
                self.totalAnt = int(file[0].removeprefix("F="))
                file.pop(0)
            elif file[0][0] == "f":
                self.totalAnt = int(file[0].removeprefix("f="))
                file.pop(0)

            # Récupère le nombre de salle ainsi que leurs emplacements dans un tableau
            # Récupère le nombre de porte/chemin/relations entre les salles dans un tableau
            for el in file:
                if len(el) == 2 or len(el) == 3 or "{" in el or "}" in el:
                    rooms.append(el)
                else:
                    relations.append(el)

            # Set les différentes relations entre les salles dans un tableau
            # Set les différentes salles ainsi que leurs emplacement dans un tableau
            # Set le nombre de salles (sommets du graphe) et chemins/porte (arête du graphe)
            self.totalRoom = len(rooms)
            self.totalDoors = len(relations)
            self.rooms = rooms
            self.relations = relations

        set_hill()

    """
        Définit la matrice booléenne représentative de la fourmilière en fonction du nombre
        de salles et des différentes liaison entres elles.
        (Taille salle * salle) (0 ou un suivant les connexions entre les salles)
    """
    def set_anthill_matrice(self):
        # Créer une matrice de salle * salle rempli de zero
        self.antHillMatrice = np.zeros((self.totalRoom, self.totalRoom))
        # Trouver un moyen d'initialiser la matrice booléene en exploitant le tableau des realtions entre les salles
        pass

    """
        Affiche la matrice représentative de la fourmilière
    """
    def print_anthill_matrice(self):
        print()
        for row in self.antHillMatrice:
            print(row)
        print()
