from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        te=t.get_entree()
        return 0, {0:te}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        te=super(t)
        noeuds={0:te}
        arc=[]
        noeuds_entree=0
        c=0
        i=1
        while c==0:
            t.afficher()
            print("definir les coordonees d'un noeud:")
            x=int(input("x: "))
            y=int(input("y: "))
            if((x,y) not in noeuds.values())
                noeuds{i}=(x,y)
                print("lier ce noeud à un autre :")
                j=int(input())
                if j in noeuds.keys():
                    if  (noeuds[i][0]==noeuds[j][0]-1 and noeuds[i][1]==noeuds[j][1]) or (noeuds[i][0]==noeuds[j][0]+1 and noeuds[i][1]==noeuds[j][1]) or (noeuds[i][1]==noeuds[j][1]-1 and noeuds[j][0]==noeuds[i][0]) or (noeuds[i][1]==noeuds[j][1]+1 and noeuds[i][0]==noeuds[j][0]):
                        arc.append((i,j))
                    else:
                        print("les deux noeuds ne sont pas cote à cote")
                else:
                    print("le noeud choisi n'existe pas")
                while (i,j) not in arc:
                        print("lier ce noeud à un noeud different :")
                        j=int(input())
                        if j in noeuds.keys():
                            if  (noeuds[i][0]==noeuds[j][0]-1 and noeuds[i][1]==noeuds[j][1]) or (noeuds[i][0]==noeuds[j][0]+1 and noeuds[i][1]==noeuds[j][1]) or (noeuds[i][1]==noeuds[j][1]-1 and noeuds[j][0]==noeuds[i][0]) or (noeuds[i][1]==noeuds[j][1]+1 and noeuds[i][0]==noeuds[j][0]):
                                arc.append((i,j))
                            else:
                                print("les deux noeuds ne sont pas cote à cote")
                        else:
                            print("le noeud choisi n'existe pas")
            else:
                print("ce noeud existe deja")
        c=input("voulez vous continuer a configurer le reseau? 0=oui 1=non")    
            
        return noeud_entree, noeuds, arc

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []
