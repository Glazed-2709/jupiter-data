## 1 Recherche dichotomique

def recherche_dichotomique(L,x):
    g = 0
    d = len(L) - 1
    while g <= d:
        m = (g+d)//2
        if x == L[m]:
            return True
        elif x < L[m]:
            d = m-1
        else:
            g = m+1
    return False

L = [2,4,5,7,11]

assert recherche_dichotomique(L,4)
assert not recherche_dichotomique(L,6)
assert recherche_dichotomique(L,2)
assert recherche_dichotomique(L,11)
assert not recherche_dichotomique(L,0)
assert not recherche_dichotomique(L,12)
assert not recherche_dichotomique([],12)

def indice_dicho(L,x):
    g = 0
    d = len(L) - 1
    while g <= d:
        m = (g+d)//2
        if x == L[m]:
            return m
        elif x < L[m]:
            d = m-1
        else:
            g = m+1
    return None

L = [2,4,5,7,11]

assert indice_dicho(L,4) == 1
assert indice_dicho(L,6) == None
assert indice_dicho(L,2) == 0
assert indice_dicho(L,11) == 4
assert indice_dicho(L,0) == None
assert indice_dicho(L,12) == None
assert indice_dicho([],12) == None

#Dans le pire cas (où x n'est pas dans la liste), si la liste est de longueur 2**(n) - 1, on doit lire n cases (par récurrence : c'est vrai pour n=1, et pour une liste de longueur 2**(n+1) - 1 après lecture de la case du milieu on se ramène à une moitié gauche ou droite de longueur 2**(n) - 1)

## 2 Exponentiation rapide

def puissance(x,k):
    r = 1
    for _ in range(k):
        r = r*x
    return r

def puissance(x,k):
    if k<0:
        assert x != 0
        x = 1/x
        k = -k
    r = 1
    for _ in range(k):
        r = r*x
    return r

# x**16 = x**8 * x**8
# x**8 = x**4 * x**4
# x**4 = x**2 * x**2
# x**2 = x * x

# x**21 = x**10 * x**10 * x
# x**10 = x**5 * x**5
# x**5 = x**2 * x**2
# x**2 = x*x

#On prend initialement y = x et n = k

#Lors d'une itération :
# Si n est pair r ne change pas et y devient y**2
# Si n est impair, r devient r*y et y devient y**2

def puissance_rapide(x,k):
    if k<0:
        assert x != 0
        x = 1/x
        k = -k
    y = x
    n = k
    r = 1
    while n > 0:
        if n%2 == 1:
            r = r * y
        y = y*y
        n = n//2
    return r

def nombre_mult(x,k):
    if k<0:
        assert x != 0
        x = 1/x
        k = -k
    y = x
    n = k
    r = 1
    c = 0
    while n > 0:
        if n%2 == 1:
            r = r * y
            c = c+1
        y = y*y
        c = c+1
        n = n//2
    return c


i = 0
while nombre_mult(1,i)<40:
    i = i+1
print(i)


def frontiere(L,x):
    g = 0
    d = len(L) - 1
    while g<d:
        m = (g+d)//2
        if x <= L[m]:
            d = m
        else:
            g = m+1
    if g>d or x <= L[g]:
        return g
    else:
        return g+1

L = [1,3,4,6]
assert frontiere(L, 4) == 2
assert frontiere(L, 2) == 1
assert frontiere(L, 7) == 4
assert frontiere(L, 0) == 0
assert frontiere([1,3,4,6, 8],4) == 2