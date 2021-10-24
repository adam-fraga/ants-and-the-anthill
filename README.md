# Ants-and-the-anthill
Une colonie de fourmis rouges a construit sa fourmilière sous terre, dans un vaste champ.

Cette colonie de fourmis est composée de F fourmis avec F étant un nombre entier. Une fourmilière est un assemblage de différentes salles, reliées les une aux autres par des tunnels. L’une de ces salles, la plus vaste, est notée Sv et correspond au vestibule de la fourmilière. L’une de ces salles, très vaste aussi, est notée Sd et correspond au dortoir, tout au fond de la fourmilière.
Les autres salles de la fourmilière sont notées S1, S2, S3, .... SN. Une salle notée SN { X } est une salle pouvant accueillir X fourmis simultanément. Un tunnel reliant deux salles est noté ainsi: Sv - S1 Sv - S5 S5 - Sd L’exemple ci-dessus informe: - qu’il existe un tunnel reliant le vestibule de la fourmilière à la salle 1 (S1) - qu’il existe un tunnel reliant le vestibule de la fourmilière à la salle 5 (S5) - qu’il existe un tunnel reliant la salle 5 (S5) de la fourmilière au dortoire (Sd).

Au lit, vite et bien!

A la tombée de la nuit, tous les fourmis se retrouvent dans le vestibule de la fourmilière, se racontent leur journée, et se préparent à rejoindre le dortoir pour se reposer. Le vestibule, étant prêt de la surface, n’est pas un endroit très sûr. L’ensemble des fourmis doit donc rejoindre le dortoir le plus rapidement possible...

CEPANDANT ... 
- Les fourmis se déplacent toutes à la même vitesse. 
- Les salles de la fourmilière ne peuvent accueillir qu’une seule fourmi à la fois (en dehors du vestibule et du dortoir) sauf si spécifié autrement.
- Une fourmi ne peut s’engager dans un tunnel que si la salle de destination est vide (en dehors du dortoir) ou si la fourmi qui l’occupe est en train de partir.
- Les tunnels sont traversés instantanément par les fourmis (c’est plutôt des portes, en fait ...) L'intégralité des fourmis doivent rejoindre le dortoir en un minimum d'étapes. 

Lors d’une étape, chaque fourmis peut: 
- Attendre dans la salle ou elle se trouve 
- Se déplacer dans une salle adjacente Lorsqu’une attend, il n’est pas besoin de le noter. Lors qu’une fourmi se déplace, on note:
F1 - Sv - S1 
Dans l’exemple ci-dessus, la fourmi 1 se déplace du vestibule vers la salle 1.
Une étape se note: 
+++ E1 +++ f1 - Sv - S1 f2 - Sv - S2
Dans l’exemple ci-dessus, 2 fourmis se déplacent depuis le vestibule, l’une vers la salle 1, l’autre vers la salle 2.

Cas simple Soit une fourmilière de 3 fourmis constituée ainsi:

Sv - S1 Sv - S2 S1 - Sd S2 - Sd Une solution serait: 
+++ E1 +++ f1 - Sv - S1 f2 - Sv - S2
+++ E2 +++ f1 - S1 - Sd f2 - S2 - Sd f3 - Sv - S1
+++ E3 +++ f3 - S1 - Sd 

Les 3 fourmis ont rejoint le dortoir en 3 étapes. 

CECI N'EST PAS UN EXERCICE

Pour chaque fourmilière proposée vous aurez à charge de :

- représenter la fourmilière sous forme de graphe en utilisant la librairie / module de votre choix 
- Afficher l’ensemble des étapes nécessaires au déplacement des fourmis, comme montré dans l’exemple ci-dessus.
- afficher graphiquement le déplacement des fourmis au sein de la fourmilière, étape par étape.
