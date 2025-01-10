import unittest
import xmlrunner
from Terrain import Terrain, Case
from Reseau import Reseau
from StrategieReseau import StrategieReseauAuto

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []


class StrategieReseauManuelle(StrategieReseau):
  
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:

        noeuds = {}
        arcs = []
        noeud_entree = -1

        # Affichage du terrain
        print("\nVoici le terrain actuel :")
        t.afficher()

        # Sélection du nœud d'entrée
        print("\nSélectionnez les coordonnées du nœud d'entrée (ligne et colonne) :")
        ligne, colonne = map(int, input("Entrez les coordonnées (exemple : 2 3) : ").split())
        if t[ligne][colonne] == Case.ENTREE:
            noeud_entree = 0
            noeuds[0] = (ligne, colonne)
        else:
            print("Erreur : Les coordonnées sélectionnées ne correspondent pas à une entrée.")
            return -1, {}, []

        # Ajout des nœuds
        print("\nAjoutez les nœuds au réseau.")
        print("Entrez les coordonnées des nœuds (ligne et colonne). Tapez 'fin' pour terminer.")
        identifiant = 1
        while True:
            entree = input(f"Nœud {identifiant} (exemple : 1 2 ou 'fin') : ")
            if entree.lower() == "fin":
                break
            try:
                ligne, colonne = map(int, entree.split())
                if (ligne, colonne) not in noeuds.values():
                    noeuds[identifiant] = (ligne, colonne)
                    identifiant += 1
                else:
                    print("Ce nœud existe déjà.")
            except ValueError:
                print("Coordonnées invalides. Essayez à nouveau.")

        # Ajout des arcs
        print("\nAjoutez les arcs reliant les nœuds.")
        print("Entrez deux identifiants de nœuds séparés par un espace. Tapez 'fin' pour terminer.")
        while True:
            entree = input("Arc (exemple : 0 1 ou 'fin') : ")
            if entree.lower() == "fin":
                break
            try:
                n1, n2 = map(int, entree.split())
                if n1 in noeuds and n2 in noeuds and (n1, n2) not in arcs and (n2, n1) not in arcs:
                    arcs.append((n1, n2))
                else:
                    print("Arc invalide ou déjà existant.")
            except ValueError:
                print("Entrée invalide. Essayez à nouveau.")

        # Résumé de la configuration
        print("\nConfiguration manuelle terminée.")
        print("Nœud d'entrée :", noeud_entree)
        print("Nœuds :", noeuds)
        print("Arcs :", arcs)

        return noeud_entree, noeuds, arcs

