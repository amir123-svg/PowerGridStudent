from Terrain import Terrain, Case
from heapq import heappop, heappush

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        noeuds ={}
        arcs = []
        num_noeud = 0
        print("configuration manuelle :")
        print ("terrain actuel:")
        t.afficher()
        while True:
            
            choix = input("ajouter un noeud? (yes/no)").strip().lower()
            
            if choix == 'no':
                break
            elif choix == 'yes':
                x,y = map(int, input("coordonées du noeud (x,y) :").strip().split(','))
                noeuds[num_noeud] = (x,y)
                print(f"noeud {num_noeud} ajouté en position ({x},{y}) ")
                num_noeud +=1
        print ("ajout des arcs:")
        while True :
             
            choix = input("ajouter un arc? (yes/no)").strip().lower()
            
            if choix == 'no':
                break
            elif choix == 'yes':
                voisins = input("ajouter un arcs (numéro des noeuds liés séparés par une virgule)").strip().split(',')
                arcs.append((voisins[0],voisins[1]))
                print (f"noeud {voisins[0]} et {voisins[1]} reliés")

                
        noeud_entree = int( input("numéro du noeud d'entrée :"))
        return noeud_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        entree = t.get_entree()
        clients = t.get_clients()

        if entree == (-1, -1) or not clients:
            return -1, {}, []

        noeuds = {}
        arcs = []
        id_counter = 0

        # Map des positions aux IDs des noeuds
        position_to_id = {}

        # Ajouter le noeud d'entrée
        position_to_id[entree] = id_counter
        noeuds[id_counter] = entree
        id_counter += 1

        # Ajouter les noeuds des clients
        for client in clients:
            position_to_id[client] = id_counter
            noeuds[id_counter] = client
            id_counter += 1

        # Construire un graphe et trouver les chemins les plus courts(on ne prend pas en compte les cases où il y a des obstacles pour éviter de passer dessus)
        # on fait une reconnaissance du terrain
        def voisins(pos):
            i, j = pos
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < t.hauteur and 0 <= nj < t.largeur and t[ni][nj] != Case.OBSTACLE:
                    yield (ni, nj)

        #méthode de dijkstra: trouver le chemin le plus court entre deux postitions (ici l'entrée et les clients) 
        #on essaie d'éviter les obstacles (avec la fonction voisins)
        #on ne visite qu'une seule fois les cases
        def dijkstra(debut):
            dist = {debut: 0}
            prev = {}
            pile = [(0, debut)]
            visited = set()

            #parcours du terrain
            while pile:
                dist_courant, pos_courant = heappop(pile)
                if pos_courant in visited:
                    continue
                visited.add(pos_courant)

                for voisin in voisins(pos_courant):
                    cost = 1 if t[voisin[0]][voisin[1]] == Case.VIDE else 2
                    new_dist = dist_courant + cost
                    if voisin not in dist or new_dist < dist[voisin]:
                        dist[voisin] = new_dist
                        prev[voisin] = pos_courant
                        heappush(pile, (new_dist, voisin))

            return dist, prev

        # Connecter l'entrée à chaque client et faire les arcs entre chaque noeud
        for client in clients:
            dist, prev = dijkstra(entree)
            chemin = []
            current = client

            # Tant que le noeud actuel n'est pas l'entrée et qu'il existe dans le dictionnaire 'prev' (qui stocke les prédecesseurs)
            while current != entree and current in prev:
            # Ajouter le noeud actuel au chemin
                chemin.append(current)
        return noeud_entree, noeuds, arcs

