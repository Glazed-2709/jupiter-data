## Exercice 1

#mystere(563) renvoie 14 (3+6+5)
#la fonction renvoie la somme des chiffres de l'écriture décimale de n

def valuation(p, n):
    if n%p == 0:
        return 1 + valuation(p, n//p)
    else:
        return 0

## Exercice 2


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def int_vers_char(i):
    return alphabet[i]

def char_vers_int(c):
    if c == ' ':
        return None
    else:
        for i in range(26):
            if c == alphabet[i]:
                return i

def char_vers_int(c):
    if c == ' ':
        return None
    else:
        g = 0
        d = 25
        while g <= d:
            m = (g+d)//2
            if c < alphabet[m]:
                d = m-1
            elif c > alphabet[m]:
                g = m+1
            else:
                return m


# 26 est compris entre 2**4 - 1 et 2**5 - 1, donc il faudra comparer c à 5 caractères au maximum

def code_char(c,cle):
    if c == ' ':
        return c
    else :
        return alphabet[(char_vers_int(c)+cle)%26]

def code(m, cle):
    n = len(m)
    m_code =''
    for i in range(n):
        c = code_char(m[i], cle)
        m_code = m_code+c
    return m_code

def indice_max(m):
    compt = 26*[0]
    for i in range(len(m)):
        ind = char_vers_int(m[i])
        if ind != None:
            compt[char_vers_int(m[i])]+=1
    ind_max = 0
    max = compt[0]
    for j in range(26):
        val = compt[j]
        if val>max:
            ind_max = j
            max = val
    return ind_max

def decode(m):
    cle = indice_max(m)-char_vers_int('e')
    return code(m,-cle)

m = code('bonjour je m appelle martin',5)
print(m)
m2 = decode(m)
print(m2)

#Exercice 3

def est_un_palindrome(c):
    n = len(c)
    for i in range(n//2):
        if c[i] != c[n-1-i]:
            return False
    return True

#Cette fonction fait entre 1 et n//2 comparaisons, avec n = len(c)

def longueur_palindromique(c):
    n = len(c)
    lmax = 1
    for j in range(n):
        for i in range(j):
            sous_chaine = c[i:j+1]
            l = len(sous_chaine)
            if est_un_palindrome(sous_chaine) and l > lmax:
                lmax = l
    return lmax

print(longueur_palindromique("truculent"))

#D'après la question précédent chaque appel de est_un_palindrome fait un nombre de comparaison majoré par n//2 (puisque la fonction est appelée sur des chaînes de longueur inférieure à n). Or on fait n(n-1)/2 tels appels (somme des i de 0 à n-1), le nombre total de comparaisons est donc bien majoré par n**3.


#Exercice 4

#Le vainqueur est 'A'

def a_un_doublon(L):
    n = len(L)
    for i in range(n):
        for j in range(i):
            if L[i] == L[j]:
                return True
    return False

#mieux, avec un dictionnaire :

def a_un_doublon(L):
    D = {}
    for x in L:
        if x in D:
            return True
        else:
            D[x] = None
    return False

def vote_valide(lvotes):
    for b in Lvotes:
        if a_un_doublon(b):
            return False
    return True

def depouillement(Lvotes):
    D = {}
    for b in Lvotes:
        for c in b:
            if c in D:
                D[c] += 1
            else:
                D[c] = 1
    return D

def vainqueur(Lvotes):
    D = depouillement(Lvotes)
    vmax = 0
    for c in D:
        if D[c] > vmax:
            vmax = D[c]
            cmax = c
    return cmax


def strategie(L, f, c):
    R = []
    f_avant_c = True
    for x in L:
        if x != f:
            R.append(x)
            if x == c:
                f_avant_c = False

        else:
            if f_avant_c:
                R.append(f)
            return R

def favori_et_challenger(Lvotes):
    D = depouillement(Lvotes)
    vmax = 0
    for c in D:
        if D[c] > vmax:
            vmax = D[c]
            v = c
    vmax = 0
    for c in D:
        if c != v and D[c] > vmax:
            vmax = D[c]
            cmax = c
    return v, cmax

def limite(Lprefs):
    Lvotes = [[L[0]] for L in Lprefs]
    f, c = favori_et_challenger(Lvotes)
    Lvotes2 = [strategie(pref,f, c) for pref in Lprefs]
    while Lvotes != Lvotes2:
        Lvotes = Lvotes2
        f, c = favori_et_challenger(Lvotes)
        Lvotes2 = [strategie(pref,f, c) for pref in Lprefs]
    return vainqueur(Lvotes)



Lprefs = [['Alice', 'Charlie', 'Dave', 'Bob'], ['Bob', 'Charlie', 'Dave', 'Alice'], ['Alice', 'Dave', 'Charlie', 'Bob'], ['Dave', 'Charlie', 'Bob', 'Alice'], ['Alice', 'Bob', 'Charlie', 'Dave'], ['Charlie', 'Dave', 'Bob', 'Alice'], ['Bob', 'Dave', 'Charlie', 'Alice']]


def limite(Lprefs):
    Lvotes = [[L[0]] for L in Lprefs]
    f, c = favori_et_challenger(Lvotes)
    D = {}
    D[f,c] = None
    Lvotes2 = [strategie(pref,f, c) for pref in Lprefs]
    while Lvotes != Lvotes2:
        Lvotes = Lvotes2
        f, c = favori_et_challenger(Lvotes)
        if (f,c) in D:
            R = [f]
            Lvotes = [strategie(pref,f, c) for pref in Lprefs]
            f2, c2 = favori_et_challenger(Lvotes)
            while f2, c2 != f,c:
                R.append(f2)
                Lvotes = [strategie(pref,f2, c2) for pref in Lprefs]
                f2, c2 = favori_et_challenger(Lvotes)
            return R
        else:
            D[f,c] = None
        Lvotes2 = [strategie(pref,f, c) for pref in Lprefs]
    return vainqueur(Lvotes)
