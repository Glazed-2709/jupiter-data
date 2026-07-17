Imara = {'F' : 10, 'A' : 8, 'R' : 6, 'V' : 5}

def paquet(n, m):
    R = []
    for valeur in range(1, m+1):
        for _ in range(n):
            R.append(valeur)
    return R

from random import *

def melange(L):
    n = len(L)
    for i in range(n-1):
        j = randint(i, n-1)
        L[i], L[j] = L[j], L[i]

def resoudre_defi(perso, defi):
    L = paquet(4, 13)
    melange(L)
    s = 0
    for i in range(4):
        carac = defi[i]
        if L[i] <= perso[carac]:
            s = s+1
    return s

def stats(perso, defi, n):
    R = [0]*5
    for _ in range(n):
        r = resoudre_defi(perso, defi)
        R[r] += 1
    for i in range(5):
        R[i] = R[i] * 100 / n
    return R

def k_plus_petits(L, k):
    n = len(L)
    L2 = [(L[i], i) for i in range(n)]

    for i in range(1, n):
        while i > 0 and L2[i] < L2[i-1]:
            L2[i], L2[i-1] = L2[i-1], L2[i]
            i -= 1

    R = L2[:k]

    for i in range(1, k):
        while i > 0 and R[i][1] < R[i-1][1]:
            R[i], R[i-1] = R[i-1], R[i]
            i -= 1

    return [x[0] for x in R]

def k_plus_grands(L, k):
    n = len(L)
    L2 = [(L[i], i) for i in range(n)]

    for i in range(1, n):
        while i > 0 and L2[i][0] > L2[i-1][0]:
            L2[i], L2[i-1] = L2[i-1], L2[i]
            i -= 1

    R = L2[:k]

    for i in range(1, k):
        while i > 0 and R[i][1] < R[i-1][1]:
            R[i], R[i-1] = R[i-1], R[i]
            i -= 1

    return [x[0] for x in R]

#les deux fonctions précédentes sont en O(n**2)

def resoudre_defi_bonus(perso, defi, bonus):
    L = paquet(4, 13)
    melange(L)
    T = L[0:4+abs(bonus)]
    if bonus > 0:
        T = k_plus_petits(T, 4)
    elif bonus < 0:
        T = k_plus_grands(T, 4)
    s = 0
    for i in range(4):
        carac = defi[i]
        if T[i] <= perso[carac]:
            s = s+1
    return s

def stats_bonus(perso, defi, n, bonus):
    R = [0]*5
    for _ in range(n):
        r = resoudre_defi_bonus(perso, defi, bonus)
        R[r] += 1
    for i in range(5):
        R[i] = R[i] * 100 / n
    return R


#On considère, pour un bonus de +2, les seuils [2, 6, 6, 6] et le tirage [3, 1, 1, 1, 5, 5]. Sans la capacité, on prend les plus petites cartes [3, 1, 1, 1], qui donne 3 succès. Avec la capacité, on peut prendre [1, 1, 1, 5], qui donne 4 succès.

def selection_optimale(seuils, tirage):
    meilleure_selection = []
    max_succes = -1
    n = len(tirage)
    for i1 in range(n - 3):
        for i2 in range(i1 + 1, n - 2):
            for i3 in range(i2 + 1, n - 1):
                for i4 in range(i3 + 1, n):
                    selection_actuelle = [tirage[i1], tirage[i2], tirage[i3], tirage[i4]]
                    succes_actuels = 0
                    for k in range(4)
                        if selection_actuelle[k] <= seuils[k]:
                            succes_actuels += 1
                    if succes_actuels > max_succes:
                        max_succes = succes_actuels
                        meilleure_selection = selection_actuelle
    return meilleure_selection

#Cette fonction est en O(n**4)

### 4/ a) i. si on selectionne 0 carte, on ne peut pas gagner donc 0 succès : ∀i ∈ [[1,n]] ,  mi,0 = 0
### 4/ a) ii. si on pioche 0 carte, on ne peut pas gagner donc 0 succès : ∀j ∈ [[0,4]],  m0,j = 0.

### 4/ b) si si,j = 1, alors  la i-ème carte est inférieure ou égale au j-ième seuil
### donc dans la décomposition on utilisera la j-ème carte en dernier
### donc on ne peut plus considérer les décompositions précédentes en comptant j
### ainsi mi,j peut étre égale à mi-1,j-1 + si,j

### il y à une autre possibilité, la carte qui vient d'être ajouté n'apporte aucun avantage, on ne considère que celles obtenues auparavant
### d'ou mi-1,j-1

### comme m est un maximum ou prends la meilleure de ses deux options
### donc : ∀i ∈ [[1,n]], ∀j ∈ [[0,4]],  mi,j = max(mi−1,j , mi−1,j−1 + si,j )

def nombre_succes_optimal(seuils, tirage):
    n = len(tirage)
    m = [[0] * 5 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, 5):
            s = 1 if tirage[i - 1] <= seuils[j - 1] else 0
            m[i][j] = max(m[i - 1][j], m[i - 1][j - 1] + s)
    return m[n][4]

#Complexité en O(n)

def resoudre_defi_destin(perso,defi,bonus):

    n = len(defi)
    Lpaqinit = paquet(4,13)
    melange(Lpaqinit)
    Lbonus = Lpaqinit[:n + bonus]
    seuil = []

    for i in range(n):
        cle = defi[i]
        seuil.append (perso[cle])
    Mat = nombre_succes_optimal(seuil,Lbonus)
    res = Mat [-1][-1]

    return res

def stats_destin(perso,defi,n,bonus):
    ndefi = len(defi)
    Ldef = [0]*(ndefi+1)
    for i in range(n):
        res = resoudre_defi_destin(perso,defi,bonus)
        Ldef[res]+=1
    L= []
    for i in range (ndefi+1):
        L.append(((Ldef[i]*100)/n))
    print(Ldef)
    return L

# print (stats_destin(Imara, 'RRRV', 10000,2))

#La capacité peut permettre de gagner 3 succès de plus :
#Avec les seuils (8,6,4,2) et le tirage [12,9,7,5,3,12,12], on a 0 succès sans la capacité (on garde [9,7,5,3]) et 3 succès avec (on garde [7,5,3,12])

#la capacité ne permet pas de gagner 4 succès de plus :
#Supposons qu'on a 0 succès sans la capacité, notons c_min la plus petite valeur dans le tirage. c_min fait partie des 4 cartes gardées sans la capacité, donc est strictement supérieure à un seuil puisqu'il y a 0 succès. Ce seuil est donc strictement inférieur à toutes les cartes du tirage, donc aucune sélection ne peut réaliser 4 succès.