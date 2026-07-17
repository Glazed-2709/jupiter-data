## TRI PAR SÉLECTION


def indice_minimum(L, i):
    j_min = i
    for j in range(i + 1, len(L)):
        if L[j] < L[j_min]:
            j_min = j
    return j_min


def tri_selection(L):
    n = len(L)
    for i in range(n - 1):
        j = indice_minimum(L, i)
        L[i], L[j] = L[j], L[i]


# Caractéristiques du tri par sélection :
# - comparatif : oui
# - en place   : oui
# - stable     : non
# Nombre maximal de comparaisons : n(n-1)/2


## TRI PAR INSERTION

def tri_insertion(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1


# Caractéristiques du tri par insertion :
# - comparatif : oui
# - en place   : oui
# - stable     : oui
# Nombre maximal de comparaisons : n(n-1)/2


## TRI RAPIDE (VERSION NON EN PLACE)

def repartition(L):
    pivot = L[-1]
    inferieurs = []
    egaux = []
    superieurs = []

    for x in L:
        if x < pivot:
            inferieurs.append(x)
        elif x > pivot:
            superieurs.append(x)
        else:
            egaux.append(x)

    return inferieurs, egaux, superieurs


def tri_rapide(L):
    if len(L) <= 1:
        return L
    inf, eg, sup = repartition(L)
    return tri_rapide(inf) + eg + tri_rapide(sup)


# Caractéristiques du tri rapide :
# - comparatif : oui
# - en place   : non (ici)
# - stable     : oui
# Si la liste est déjà triée et que le pivot est le dernier élément, tous les autres éléments sont toujours mis dans la première liste. On fait alors un nombre quadratique de comparaisons.
# Pivot préférable : pivot aléatoire ou pivot médian


## TRI FUSION

def fusion(L1, L2):
    i1, i2 = 0, 0
    resultat = []

    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] <= L2[i2]:
            resultat.append(L1[i1])
            i1 += 1
        else:
            resultat.append(L2[i2])
            i2 += 1

    return resultat + L1[i1:] + L2[i2:]


def tri_fusion(L):
    if len(L) <= 1:
        return L
    milieu = len(L) // 2
    return fusion(tri_fusion(L[:milieu]), tri_fusion(L[milieu:]))


# Caractéristiques du tri fusion :
# - comparatif : oui
# - en place   : non
# - stable     : oui


## TRI PAR COMPTAGE

def tri_comptage(L):
    if L == []:
        return L
    D = {}
    for x in L:
        if x in D:
            D[x] += 1
        else:
            D[x] = 1

    a = b = L[0]
    for x in L:
        if x>b:
            b = x
        elif x < a:
            a = x

    resultat = []

    for x in range(a, b + 1):
        if x in D:
            resultat += [x]*D[x]

    return resultat


# Caractéristiques du tri par comptage :
# - comparatif : non
# - en place   : non
# - stable     : non pertinent pour trier des entiers


## TRI RAPIDE EN PLACE

def repartition_en_place(L, a, b):
    pivot = L[b]
    i = a

    for j in range(a, b):
        if L[j] <= pivot:
            L[i], L[j] = L[j], L[i]
            i += 1

    L[i], L[b] = L[b], L[i]
    return i


def tri_sous_liste(L, a, b):
    if a < b:
        p = repartition_en_place(L, a, b)
        tri_sous_liste(L, a, p - 1)
        tri_sous_liste(L, p + 1, b)


def tri_rapide_en_place(L):
    tri_sous_liste(L, 0, len(L) - 1)


## COMPARAISON DES TEMPS DE CALCUL

import random
import timeit
import matplotlib.pyplot as plt


def mesure_temps(k, n, p, d):
    tris = [tri_selection, tri_insertion, tri_fusion, tri_rapide, tri_comptage, tri_rapide_en_place]
    temps = [[] for _ in range(6)]
    tailles = [i*d for i in range(1, n)]

    for taille in tailles:
        t = [0]*6

        for _ in range(k):
            L = [random.randint(0, p) for _ in range(taille)]

            for j in range(6):
                tri = tris[j]
                copie = L.copy()
                depart = timeit.default_timer()
                tri(copie)
                duree = timeit.default_timer() - depart

                t[j] += duree

        for j in range(6):
            temps[j].append(t[j])

    plt.plot(tailles, temps[0], "-", label="Tri sélection")
    plt.plot(tailles, temps[1], "--", label="Tri insertion")
    plt.plot(tailles, temps[2], "-x", label="Tri fusion")
    plt.plot(tailles, temps[3], ".", label="Tri rapide")
    plt.plot(tailles, temps[4], "-.", label="Tri comptage")
    plt.plot(tailles, temps[5], "+", label="Tri rapide en place")

    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps de calcul (s)")
    plt.legend()
    plt.show()


mesure_temps(k=100, n=100, p=1000, d=2)