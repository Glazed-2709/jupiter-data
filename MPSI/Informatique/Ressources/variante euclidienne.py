def chemin(pred,u):
    if pred[u] == None:
        return [u]
    L = chemin(pred,pred[u])
    L.append(u)
    return L

def distance(u,d):
    #distance euclidienne
    x1,y1 = u
    x2,y2 = d
    return ((x2 - x1)**2 +  (y2 - y1)**2)**0.5

from math import *


def visible(M,u,v):
    #teste si il existe un segment de u à v n'intersectant aucun obstacle, avec yu <= yv
    xu,yu = u
    xv,yv = v
    #N = deepcopy(M) (affichage graphique pour voir ce qui se passe)
    if yu == yv: #cas de pente infinie
        for x in range(xu,xv+1):
            if M[x][yu] == -1:
                return False
        return True
    p = (xv - xu)/(yv-yu) #pente du segment
    #d = 0.2*sqrt(1+p**2) + 0.5 (version pour garder une distance de 0.2 avec les obstacles)
    d = 0.5 #distance du centre d'une case à son bord
    if xv <= xu:
        for y in range(yu,yv+1):
            xmin = max(xv,ceil(xu + p*(y-yu+0.5) -d))  #Formule à faire simplifier par une prof de maths
            xmax = min(xu,floor(xu + p*(y-yu-0.5) + d))
            # sur la colonne y, les cases qui peuvent boucher la vue vont des abscisses xmin à xmax
            for x in range(xmin,xmax+1):
                if M[x][y] == -1:
                    return False
                #N[x][y] = max(1,N[x][y])
                #plt.clf()
                #plt.imshow(N)
                #tracer(u,v)
                #plt.pause(0.01)
    else:
        for y in range(yu,yv+1):
            xmin = max(xu,ceil(xu + p*(y-yu-0.5) - d))
            xmax = min(xv,floor(xu + p*(y-yu+0.5) + d))
            for x in range(xmin,xmax+1):
                if M[x][y] == -1:
                    return False
                #N[x][y] = max(1,N[x][y])
                #plt.clf()
                #plt.imshow(N)
                #tracer(u,v)
                #plt.pause(0.01)
    return True




def graphe(M):
    n,p = len(M), len(M[0])
    G = [[[] for j in range(p)] for i in range(n)]
    b = 10 #on ne relie que des cases dont les abscisses et les ordonnees diffèrent d'au plus b
    for i in range(n):
        for j in range(p):
            u = (i,j)
            for x in range(max(0,i-b),i+1):
                for y in range(j+1, min(p,j+b)):
                    v = (x,y)
                    if visible(M,u,v):
                        G[i][j].append(v)
                        G[x][y].append(u)
            for x in range(i+1,min(n,i+b)):
                for y in range(j, min(p,j+b)):
                    v = (x,y)
                    if visible(M,u,v):
                        G[i][j].append(v)
                        G[x][y].append(u)
    return G



def element_min(L,D,d,h):
    dmin = float('inf')
    for u in L:
        du = D[u] + h(u,d)
        if du < dmin:
            umin = u
            dmin = du
    return umin

from copy import deepcopy
def A_etoile_grille(M,G,s,d,h):
    n,p = len(M), len(M[0])
    D = {s : 0}
    P = {s : None}
    L = {s}
    k=0
    while len(L)>0:
        k+=1
        u = element_min(L,D,d,h)
        L.remove(u)
        if u == d:
            return k, D[d], chemin(P,d)
        x,y = u
        for v in G[u[0]][u[1]]:
            x2,y2 = v
            d2 = D[u] + distance(u,v)
            if v not in D or d2 < D[v]:
                D[v] = d2
                P[v] = u
                L.add(v)
    return "destination inaccessible"


import matplotlib.pyplot as plt

def tracer(u,v):
    x1,y1 = u
    x2,y2 = v
    plt.plot([y1,y2],[x1,x2],'k')

def tracer_chemin(chemin):
    for i in range(len(chemin)-1):
        u = chemin[i]
        v = chemin[i+1]
        tracer(u,v)

def afficher(M,s,d,h):
    k, d, chemin = A_etoile_grille(M,s,d,h)
    plt.imshow(M)
    tracer_chemin(chemin)
    plt.show()


import numpy as np


def carte(n,p,q):
    #crée une carte n*p avec une proba q d'obstacles au centre, et plus faible en périphérie
    return [[-np.random.binomial(1,q*(1 - 4*((i-(n-1)/2)**2 + (j-(p-1)/2)**2)/((n-1)**2+(p-1)**2))) for j in range(p)] for i in range(n)]

def tracer_progressif(M,G,s,d,h):
    n,p = len(M), len(M[0])
    D = {s : 0}
    P = {s : None}
    L = {s}
    N = deepcopy(M)
    plt.imshow(N)
    plt.axis("off")
    plt.tight_layout()
    while len(L)>0:
        u = element_min(L,D,d,h)
        L.remove(u)
        x,y = u
        N[x][y] = 2
        plt.pause(0.01)
        plt.clf()
        plt.imshow(N)
        plt.axis("off")
        plt.tight_layout()
        tracer_chemin(chemin(P,u))
        if u == d:
            plt.pause(0.01)
            return D[d], chemin(P,d)
        for v in G[u[0]][u[1]]:
            x2,y2 = v
            N[x2][y2] = max(1,N[x2][y2])
            d2 = D[u] + distance(u,v)
            if v not in D or d2 < D[v]:
                D[v] = d2
                P[v] = u
                L.add(v)
    print("destination inaccessible")

def tracer_par_etape(M,G,s,d,h):
    n,p = len(M), len(M[0])
    D = {s : 0}
    P = {s : None}
    L = {s}
    N = deepcopy(M)
    plt.imshow(N)
    plt.tight_layout()
    for _ in range(10):
        u = element_min(L,D,d,h)
        print(u)
        L.remove(u)
        x,y = u
        N[x][y] = 2
        plt.waitforbuttonpress()
        plt.clf()
        plt.imshow(N)
        plt.tight_layout()
        tracer_chemin(chemin(P,u))
        if u == d:
            plt.waitforbuttonpress()
            return D[d], chemin(P,d)
        for v in G[u[0]][u[1]]:
            x2,y2 = v
            N[x2][y2] = max(1,N[x2][y2])
            d2 = D[u] + distance(u,v)
            if v not in D or d2 < D[v]:
                D[v] = d2
                P[v] = u
                L.add(v)



def hw(w):
    #distance euclidienne multipliée par w
    def h(u,d):
        return distance(u,d)*w
    return h



def comparaison_coeffs():
    for i in range(31):
        w = i/10
        k,d,c = A_etoile_grille(M,G,(0,0),(n-1,p-1),hw(w))
        print("coefficient multiplicatif :", w, "- nombre d'itérations :", k, "- distance :", round(d,2))


n = 60
p = 60

M = carte(n,p,0.4)
G = graphe(M)

plt.ion()
# print(tracer_par_etape(M,G,(0,0),(n-1,p-1),hw(1)))

print(tracer_progressif(M,G,(0,0),(n-1,p-1),hw(1)))

# comparaison_coeffs()
