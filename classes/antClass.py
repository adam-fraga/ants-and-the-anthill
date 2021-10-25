import sys


"""
    Class fourmis/ Ant Class
"""


class Ant:
    """
        Permet de créer une fourmis en lui attribuant en nom F1, F2 etc...
        Pour la création de plusieurs foumis on préfèrera bouclé lors de l'instanciation
    """
    def __init__(self, id) -> None:
        self.id = f"F{id}"
        # Etat move (bool)
        self.move = None
        # Etat stay (bool)
        self.stay = None
        pass

    """
        Ajoute la fourmi dans le vestibule de la fourmilière
        Voir si vestibule = dic ou list
    """

    def goto_vestibule(self, vestibule: list or dict) -> None:
        vestibule.append(self)
        pass
