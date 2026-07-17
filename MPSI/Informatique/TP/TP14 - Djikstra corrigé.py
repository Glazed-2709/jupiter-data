import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import sqrt


def dijkstra(G,s):
    n = len(G)
    D = [float("inf")]*n
    D[s] = 0
    P = [None]*n
    marque = [False]*n
    for _ in range(n):
        min = float("inf")
        for i in range(n):
            if not marque[i] and D[i] <= min:
                min = D[i]
                u = i
        marque[u] = True
        for v,w in G[u]:
            d2 = D[u] + w
            if d2 < D[v]:
                D[v] = d2
                P[v] = u
    return D,P


def norme(V):
     s = 0
     for v in V:
         s += v*v
     return sqrt(s)

def energie(image):
    n, p, q  = image.shape
    res = np.zeros((n,p))
    for y in range(n):
        for x in range(1,p-1):
            res[y,x] = norme(image[y,x+1,:]-image[y,x-1,:])
    return res

# im_tour = np.array(plt.imread('BroadwayTower.png'))
# energy = deriv_x(im_tour)
# plt.figure()
# plt.imshow(energy,cmap=plt.cm.gray, vmin=0,vmax=1)
# mpimg.imsave("energy.png",energy,cmap=plt.cm.gray, vmin=0,vmax=1)
# #plt.title('energie')
# plt.show()


def min_dico_dist(D, L): 
    # renvoie l'element de L de distance minimale, les
    # distances etant stockees dans le dictionnaire D
    d_min = float('inf')
    for s in L :
        if D[s]< d_min :
            d_min = D[s]
            sommet_min = s
    return sommet_min


def arcs_sortants( energy, noeud):
    n, p = energy.shape # n = nb de lignes, p= nb de colonnes
    x,y = noeud
    if x < 0:
        # Du noeud au-dessus de l'image sortent les arcs vers tous les noeuds 
        #du bord haut de l'image
        return [((0,y),energy[0,y]) for y in range(1,p-1)]
     elif y <= 0:
        # Du bord gauche de l'image ne sort aucun arc
        return []
    elif y >= p-1:
        # Du bord droit de l'image ne sort aucun arc
        return []
    elif x == n-1:
        # D'un pixel du bord bas de l'image sort un arc vers le noeud en 
        #dessous de l'image
        return [((n,0),0)]
    elif x == n:
        return [] 
    elif y == 1:
        # Du pixel juste à droite du bord gauche de l'image il n'y a que deux 
        #arcs (pas d'arc vers le bord gauche)
        return [((x+1,y),energy[x+1,y]), ((x+1,y+1),energy[x+1,y+1])]
    elif y == p-2:
        # Du pixel juste à gauche du bord droit de l'image il n'y a que deux
        #arcs (pas d'arc vers le bord droit)
        return [((x+1,y-1),energy[x+1,y-1]), ((x+1,y),energy[x+1,y])]
    else:
        # D'un pixel loin des bords de l'image sortent 3 arcs, vers le pixel 
        #en bas à gauche, en bas, et en bas à droite
        return [((x+1,y-1),energy[x+1,y-1]), ((x+1,y),energy[x+1,y]), 
                ((x+1,y+1),energy[x+1,y+1])]


def dijkstra_image(image):
    n, p, q = image.shape
    depart = (-1,0)
    arrivee = (n,0)
    energy = energie(image)
    L = {depart}
    D = {depart: 0} # Dictionnaire contenant la plus petite distance calculee 
    #vers chaque noeud
    pere = {depart : None} # Dictionnaire contenant le  predecesseur pour 
    #le plus court chemin
    while True:
        u = min_dico_dist(D, L)
        L.remove(u)
        if u == arrivee:
            return pere, D[arrivee]
        for v, w in arcs_sortants(energy, u):
            distance_new = D[u] + w
            if v not in D or distance_new < D[v]:
                D[v] = distance_new
                pere[v] = u
                L.add(v)

def chemin(pere,depart, arrivee):
    if depart == arrivee:
        return [depart]
    c = chemin(pere, depart, pere[arrivee])
    return c + [arrivee]

def tracer_chemin(image, chemin):
    for x,y in chemin[1:-1]:
        image[x,y,:] = [1,0,0]

def supprimer_chemin(image,chemin):
    n, p, q = image.shape
    c = chemin[1:-1]
    R = np.arange(0,p)
    res = np.array([image[x, (R != c[x][1]), :] for x in range(0,n)] )
    return res

im_tour = np.array(plt.imread('BroadwayTower.png'))
#im_tour = mpimg.imread('BroadwayTower.png')
n, p, q = im_tour.shape

plt.close()
plt.figure()
plt.imshow(im_tour)
plt.title('image de depart')
plt.show()
plt.pause(0.001)
for i in range(50):
    P, d = dijkstra_image(im_tour)
    c = chemin(P,(-1,0),(n,0))
    tracer_chemin(im_tour, c)
    plt.clf()
    plt.title('etape ' + str(i))
    plt.axis([0,p-1,0,n-1])
    plt.gca().invert_yaxis()
    plt.imshow(im_tour)
    plt.show()
    im_tour = supprimer_chemin(im_tour,c)
    plt.pause(0.001)
    
mpimg.imsave("image_finale.png",im_tour)
    
# P, d = dijkstra_image(im_tour, (-1,0), (n,0))
# c = chemin(P,(-1,0),(n,0))
# tracer_chemin(im_tour, c)
# mpimg.imsave("trace_chemin.png",im_tour)
# plt.axis([0,p-1,0,n-1])
# plt.gca().invert_yaxis()
# plt.imshow(im_tour)