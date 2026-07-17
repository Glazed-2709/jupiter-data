## Partie 1 : Opérations fondamentales sur les graphes

G1 = [
    [1, 3],         # voisins de 0
    [0, 2, 3],      # voisins de 1
    [1, 3, 4, 5],   # voisins de 2
    [0, 1, 2, 4],   # voisins de 3
    [2, 3, 5],      # voisins de 4
    [2, 4],         # voisins de 5
]

M1 = [
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0],
]


def degre1(G, u):
    return len(G[u])

def degre2(M, u):
    d = 0
    for v in range(len(M)):
        d += M[u][v]
    return d

def ordre1(G):
    return len(G)

def ordre2(M):
    return len(M)


def sont_voisins1(G, u, v):
    for x in G[u]:
        if x==v:
            return True
    return False

def sont_voisins2(M, u, v):
    return M[u][v] == 1


def ajoute_sommet1(G):
    G.append([])

def ajoute_sommet2(M):
    n = len(M)
    for ligne in M:
        ligne.append(0)
    M.append([0] * (n + 1))


def ajoute_arete1(G, a):
    u, v = a
    G[u].append(v)
    G[v].append(u)

def ajoute_arete2(M, a):
    u, v = a
    M[u][v] = 1
    M[v][u] = 1


def nb_aretes1(G):
    s = 0
    for voisins in G:
        s += len(voisins)
    return s // 2

def nb_aretes2(M):
    n = len(M)
    s = 0
    for i in range(n):
        for j in range(i):
            s += M[i][j]
    return s


def regulier1(G):
    if len(G) == 0:
        return True
    d = len(G[0])
    for voisins in G:
        if len(voisins) != d:
            return False
    return True

def regulier2(M):
    n = len(M)
    if n == 0:
        return True
    d0 = degre2(M, 0)
    for u in range(1, n):
        if degre2(M, u) != d0:
            return False
    return True


def aretes1(G):
    L = []
    for u in range(len(G)):
        for v in G[u]:
            if u < v:
                L.append((u, v))
    return L

def aretes2(M):
    n = len(M)
    L = []
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] == 1:
                L.append((i, j))
    return L


# Complexités (en fonction du nombre n de sommets) ------------
# On note m le nombre d'arêtes, avec m <= n(n-1)/2.
#
#   degre1          : O(1)
#   degre2          : O(n)
#   ordre1 / ordre2 : O(1)
#   sont_voisins1   : O(deg(u)) -> O(n) au pire
#   sont_voisins2   : O(1)
#   ajoute_sommet1  : O(1)
#   ajoute_sommet2  : O(n)
#   ajoute_arete1   : O(1)
#   ajoute_arete2   : O(1)
#   nb_aretes1      : O(n + m)  -> O(n^2) au pire
#   nb_aretes2      : O(n^2)
#   regulier1       : O(n)
#   regulier2       : O(n^2)
#   aretes1         : O(n + m)  -> O(n^2) au pire
#   aretes2         : O(n^2)


def liste_vers_matrice(G):
    n = len(G)
    M = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            M[u][v] = 1
    return M


def matrice_vers_liste(M):
    n = len(M)
    G = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if M[u][v] == 1:
                G[u].append(v)
    return G


## Partie 2 : Puissances de la matrice d'adjacence

def produit(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def puissance(M, k):
    n = len(M)
    # on part de la matrice identité (M^0)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = produit(R, M)
    return R

# (M^k)[i][j] est le nombre de chemins de longueur k reliant i à j dans G.
#
# Preuve par récurrence sur k :
#   - k = 1 : (M^1)[i][j] = M[i][j] vaut 1 ssi i et j sont voisins, ce qui
#     correspond bien au nombre de chemins de longueur 1 entre i et j.
#   - Hérédité : (M^{k+1})[i][j] = somme_l (M^k)[i][l] * M[l][j]. Tout chemin
#     de longueur k+1 de i à j se décompose de façon unique en un chemin
#     de longueur k de i vers un voisin l de j, puis l'arête l-j.


#   (M^3)[i][i] compte le nombre de cycles de longueur 3 partant de i.
#   Un tel chemin visite 3 sommets distincts deux à deux voisins, i.e. un
#   triangle contenant i. Chaque triangle {a, b, c} est compté une fois pour
#   chacun de ses trois sommets (choix du sommet de départ), et dans chacun
#   des deux sens de parcours, soit 3 * 2 = 6 fois dans tr(M^3).
#   D'où le nombre de triangles = tr(M^3) / 6.

def nb_triangles(M):
    M3 = puissance(M, 3)
    tr = 0
    for i in range(len(M)):
        tr += M3[i][i]
    return tr // 6

def non_voisins_les_plus_proches(M):
    n = len(M)
    M2 = produit(M, M)
    meilleur = -1
    paire = (-1, -1)
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] == 0 and M2[i][j] > meilleur:
                meilleur = M2[i][j]
                paire = (i, j)
    return paire


def katz(M, u, alpha):
    n = len(M)
    Mk = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    coef = 1
    total = 0.0
    while True:
        Mk = produit(Mk, M)
        coef *= alpha
        terme_k = 0
        for v in range(n):
            terme_k += coef * Mk[v][u]
        total += terme_k
        if abs(terme_k) < 1e-9:
            return total



def _matrice_dict(G):
    """Transforme un dict de listes d'adjacence en un dict de dicts (matrice
    d'adjacence indexée par les noms des sommets). Renvoie aussi la liste
    ordonnée des sommets pour garantir un ordre cohérent dans les itérations."""
    sommets = list(G.keys())
    M = {u: {v: 0 for v in sommets} for u in sommets}
    for u in sommets:
        for v in G[u]:
            M[u][v] = 1
    return M, sommets


def produit_dict(A, B, sommets):
    C = {u: {v: 0 for v in sommets} for u in sommets}
    for i in sommets:
        for j in sommets:
            s = 0
            for k in sommets:
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def puissance_dict(M, k, sommets):
    R = {u: {v: (1 if u == v else 0) for v in sommets} for u in sommets}
    for _ in range(k):
        R = produit_dict(R, M, sommets)
    return R


def nb_triangles_dict(G):
    M, sommets = _matrice_dict(G)
    M3 = puissance_dict(M, 3, sommets)
    tr = 0
    for u in sommets:
        tr += M3[u][u]
    return tr // 6


def non_voisins_les_plus_proches_dict(G):
    M, sommets = _matrice_dict(G)
    M2 = produit_dict(M, M, sommets)
    meilleur = -1
    paire = (None, None)
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            u, v = sommets[i], sommets[j]
            if M[u][v] == 0 and M2[u][v] > meilleur:
                meilleur = M2[u][v]
                paire = (u, v)
    return paire


def katz_dict(G, u, alpha):
    M, sommets = _matrice_dict(G)
    Mk = {x: {y: (1 if x == y else 0) for y in sommets} for x in sommets}
    coef = 1
    total = 0.0
    while True:
        Mk = produit_dict(Mk, M, sommets)
        coef *= alpha
        terme_k = 0
        for v in sommets:
            terme_k += coef * Mk[v][u]
        total += terme_k
        if abs(terme_k) < 1e-9:
            break
    return total
