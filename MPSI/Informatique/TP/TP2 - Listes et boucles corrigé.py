from math import log

def contient(L,x):
    for y in L:
        if x == y:
            return True
    return False

def positions(L,x):
    R = []
    n = len(L)
    for i in range(n):
        if x == L[i]:
            R.append(i)
    return R

def maximum(L):
    m = L[0]
    for x in L:
        if x>m:
            m = x
    return m

def positions_maximum(L):
    return positions(L, maximum(L))

def positions_maximum(L):
    m = L[0]
    R = []
    for i in range(len(L)):
        if L[i] > m:
            m = L[i]
            R = [i]
        elif L[i] == m:
            R.append(i)
    return R

#Les fonctions maximum, positions et positions_maximum sont de complexité linéaire



# Premier exemple

def f(n):
    r=0
    for i in range(n):
        for j in range(n):
            r = r + j
    return r

def f(n):
    return n*n*(n-1)/2


def somme_double(n,m):
    s = 0
    for i in range(n):
        for j in range(m):
            s += log(i+j**2+1)
    return s


def minmax(L):
    min = maximum(L[0])
    n = len(L)
    for i in range(1, n):
        max = maximum(L[i])
        if max < min :
            min = max
    return min

#recherche d'un facteur dans un texte

texte = " L’informatique, comme discipline scientifique et technique, s’est déployée sur deux siècles environs : 19ème et 20ème siècle. Elle est liée à l’apparition des premiers automates et à la mécanisation : un processus de développement et de généralisation des machines qui a commencé au 18ème siècle en Europe avec l’industrialisation. Nous devons la première programmation binaire (carton/trou) à Joseph-Marie Jacquard en 1801. Il s’agissait d’un procédé industriel visant à accroître la productivité des métiers à tisser. Le développement de l’informatique est lié à la recherche fondamentale en mathématiques et plus précisément à la logique et aux algorithmes mathématiques, apparus au début du 9ème siècle avec les travaux du mathématicien arabe Abu Jaffar Al Khawarizmi. L’informatique a bénéficié en outre de l’introduction du calcul binaire en Europe vers 1697, grâce aux travaux  Gottfried Wilhelm Leibniz , à la formalisation du principe des machines à calculer par Ada Lovelace en 1840 et à la théorisation de la logique binaire par George Boole en 1854."

mot = "informatique"

def facteur_position(texte,mot,i):
    m = len(mot)
    for j in range(m):
        if mot[j] != texte[i+j]:
            return False
    return True

facteur_position('hello world', 'world', 6)
facteur_position('hello world','world',5)


def facteur(texte, mot):
    n = len(texte)
    m=len(mot)
    for i in range(n-m+1):
        if facteur_position(texte, mot, i):
            return True
    return False

facteur(texte, mot)

def liste_occurrences(texte,mot):
    res = []
    n = len(texte)
    m=len(mot)
    for i in range(n-m+1):
        if facteur_position(texte, mot, i):
            res.append(i)
    return res

def facteur2(texte, mot):
    n = len(texte)
    m=len(mot)
    for i in range(n-m+1):
        if texte[i:i+m] == mot:
            return True
    return False

def liste_occurrences2(texte,mot):
    res = []
    n = len(texte)
    m=len(mot)
    for i in range(n-m+1):
        if texte[i:i+m] == mot:
            res.append(i)
    return res


# Deux valeurs les plus proches

def valeurs_plus_proches(L):
    n = len(L)
    dref = abs(L[0]-L[1])
    v1, v2 = L[0], L[1]
    for i in range(n):
        for j in range(i):
            d = abs(L[i]-L[j])
            if d < dref:
                dref = d
                v1, v2 = L[j], L[i]
    return v1, v2

valeurs_plus_proches([-2, 3, 8, 5, -9])

'''
pour chaque i de 0 à n-1, abs est appelée i fois, donc n(n-1)/2 fois en tout.
'''



