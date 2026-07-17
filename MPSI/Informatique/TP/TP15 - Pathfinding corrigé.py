G1 = [[(1,10), (4,5)], [(2,1),(4,2)], [(3,4)], [(2,6),(0,7)],[(1,3),(2,9),(3,2)]]

def chemin(P, u):
    if P[u] == None:
        return [u]
    L = chemin(P, P[u])
    L.append(u)
    return L


def A_etoile(G, s, dest, h):
    n = len(G)
    D = [float("inf")]*n
    D[s] = 0
    P = [None]*n
    marque = [True]*n
    marque[s] = False
    nb_non_marque = 1
    while nb_non_marque > 0:
        min = float("inf")
        for v in range(n):
            pv = D[v] + h(v, dest)
            if not marque[v] and pv < min:
                min = pv
                u = v
        marque[u] = True
        nb_non_marque -=1
        if u == dest:
            return D[dest], chemin(P, dest)
        for v,w in G[u]:
            d2 = D[u] + w
            if d2 < D[v]:
                D[v] = d2
                P[v] = u
                if marque[v]:
                    marque[v] = False
                    nb_non_marque +=1
    return None

pos = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1)]

def h2(u, dest):
    x1,y1 = pos[u]
    x2,y2 = pos[dest]
    return ((x2 - x1)**2 +  (y2 - y1)**2)**0.5

def h0(u, dest):
    return 0


A_etoile(G1, 0, 2, h2)

A_etoile(G1, 0, 2, h0)


#Pour obtenir un exemple où A* ne renvoie pas le chemin optimal, on peut placer 4 très loin des autres sommets (en position, sans changer les poids du graphe)

pos = [(0, 0), (0, 1), (0, 2), (1, 2), (20, 20)]

A_etoile(G1,0,2,h2)


#Pathfinding

import numpy as np


def carte(n,p,q):
    #crée une carte n*p avec une proba q d'obstacles au centre, et plus faible en périphérie
    return [[np.random.binomial(1,q*(1 - 4*((i-(n-1)/2)**2 + (j-(p-1)/2)**2)/((n-1)**2+(p-1)**2))) for j in range(p)] for i in range(n)]

import matplotlib.pyplot as plt

n = 70
p = 70

M = carte(n,p,0.5)
plt.imshow(M)
plt.show()


def voisins(M, u):
    x,y = u
    R = []
    for v in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        x2,y2 = v
        if 0<=x2<n and 0<=y2<p and M[x2][y2] != 1:
            R.append(v)
    return R

def A_etoile_grille(M, s, dest, h):
    n,p = len(M), len(M[0])
    D = {s : 0}
    P = {s : None}
    L = set()
    L.add(s)
    k=0 #compte le nombre de passages dans le while
    while len(L)>0:
        k+=1
        dmin = float('inf')
        for v in L:
            dv = D[v] + h(v, dest)
            if dv < dmin:
                dmin = dv
                u = v
        L.remove(u)
        if u == dest:
            return k, D[dest], chemin(P, dest)
        x,y = u
        for v in voisins(M, u):
            d2 = D[u] + 1
            if v not in D or d2 < D[v]:
                D[v] = d2
                P[v] = u
                L.add(v)
    return None

def h0(u,d):
    #heuristique nulle, ramenant à Dijkstra
    return 0

def h_eucl(u,d):
    #distance euclidienne, terminaison plus rapide
    x1,y1 = u
    x2,y2 = d
    return ((x2 - x1)**2 +  (y2 - y1)**2)**0.5

def h_manhattan(u,d):
    #distance manhattan, terminaison un peu plus rapide
    x1,y1 = u
    x2,y2 = d
    return (abs(x2 - x1) +  abs(y2 - y1))


def h_manhattan_2(u,d):
    #distance manhattan doublée, terminaison plus rapide mais le chemin renvoyé n'est plus forcément optimal
    x1,y1 = u
    x2,y2 = d
    return (abs(x2 - x1) +  abs(y2 - y1))*2


for h in [h0,h_eucl,h_manhattan,h_manhattan_2]:
    k,d,c = A_etoile_grille(M,(0,0),(n-1,p-1),h)
    print("fonction :", h.__name__)
    print("temps :", k, "- distance renvoyée :", d)

from copy import deepcopy

def tracer_progressif(M, s, dest, h):
    n,p = len(M), len(M[0])
    D = {s : 0}
    P = {s : None}
    L = set()
    L.add(s)
    N = deepcopy(M)
    plt.imshow(N)
    while len(L)>0:
        dmin = float('inf')
        for v in L:
            dv = D[v] + h(v, dest)
            if dv < dmin:
                dmin = dv
                u = v
        L.remove(u)
        x,y = u
        N[x][y]=-2
        for x,y in chemin(P,u):
            N[x][y] = -3
        plt.pause(0.001)
        plt.clf()
        plt.imshow(N)
        if u == dest:
            plt.pause(0.001)
            return D[dest], chemin(P,dest)
        for x,y in chemin(P,u):
            N[x][y] = -2
        for v in voisins(M, u):
            x2, y2, = v
            N[x2][y2]=min(-1,N[x2][y2])
            d2 = D[u] + 1
            if v not in D or d2 < D[v]:
                D[v] = d2
                P[v] = u
                L.add(v)
    return None

plt.ion()
tracer_progressif(M,(0,0),(n-1,p-1),h_manhattan)





