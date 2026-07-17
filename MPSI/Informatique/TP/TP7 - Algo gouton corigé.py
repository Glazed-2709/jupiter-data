# Partie I

# Question 1
def est_un_systeme(L):
    if L[0] != 1:
        return False
    for i in range(len(L)-1):
        if L[i] >= L[i+1]:
            return False
    return True


# assert est_un_systeme([1,3,6])
# assert not(est_un_systeme([1,3,6,6]))
# assert not(est_un_systeme([2,4,10]))


# Question 2
def glouton_monnaie(x,S):
    r = x
    L = [0 for i in range(len(S))]
    i = len(S)-1
    while r>0:
        if r >= S[i]:
            r += - S[i]
            L[i] += 1
        else:
            i += -1
    return L

#print(glouton_monnaie(27,[1,2,5,10,50]))

# Question 3
def glouton_monnaie_aux(x,S,i):
    if x == 0:
        return [0 for j in range(i)]
    else:
        q = x//S[i-1]
        r = x-S[i-1]*q
        L = glouton_monnaie_aux(r,S,i-1)
        L.append(q)
        return L

def glouton_monnaie_rec(x,S):
    return glouton_monnaie_aux(x,S,len(S))

#print(glouton_monnaie_rec(27,[1,2,5,10,50]))


# Question 4
# Pour rendre 48 : on pourrait rendre 2 pièces de 24. Or l'algorithme glouton rend une pièce de 30, une pièce de 12 puis une pièce de 6, soit 3 pièces. Ainsi le système [1,3,6,12,24,30] n'est pas canonique

# Question 5
# [1,3,4] n'est pas canonique : 6 = 3+3 mais l'algorithme glouton rend 4+1+1

# Question 6
# Soit un système S=[1,s1] contenant deux pièces.
# Soit x la somme à rendre. Notons x=s1*q+r la division euclidienne de x par s1. L'algorithme glouton utilise donc q+r pièces.
# Supposons par l'absurde qu'il existe des entiers positifs q' et r' tels que q'+r'<q+r et x=s1*q'+r'.
# Alors s1*(q-q') = r'-r < (q+r-q') - r = q-q'
# Comme s1>0, on en déduit que q-q'<0, c'est-à-dire q<q', puis r'<r.
# Alors x=s1*q'+r' avec 0 <= r' < r < s1 donc on a écrit la division euclidienne de x par s1. Par unicité, q'=q et r=r' : absurde.




# Partie II

# Question 7

# durée du cours :
# cours 1 : 11h-14h
# cours 2 : 9h-13h
# cours 3 : 13h-17h
# l'algorithme attribue la salle au cours 1 (3h) puis il ne peut pas l'attribuer à d'autres cours ;
# on aurait pu attribuer la salle aux cours 2 et 3

# début du cours
# cours 1 : 8h - 13h
# cours 2 : 9h - 10h
# cours 3 : 11h - 12h
# l'algorithme attribue la salle au cours 1 (début 8h) puis il ne peut pas l'attribuer à d'autres cours ;
# on aurait pu attribuer la salle aux cours 2 et 3

# nombre d'intersections du cours avec un autre cours
# cours 1 : 11h30 - 13h30
# cours 2 : 9h - 10h
# cours 3 : 11h - 12h
# cours 4 : 13h - 14h
# cours 5 : 15h - 16h
# cours 6 : 9h30 - 11h30
# cours 7 : 9h30 - 11h30
# cours 8 : 9h30 - 11h30
# cours 9 : 13h30 - 15h30
# cours 10 : 13h30 - 15h30
# cours 11 : 13h30 - 15h30
# le tri par nombre d'intersections croissant donne :
# 1 (2) --> 2 (3) --> 3 (3) --> 4 (3) --> 5 (3) --> 6 (4) --> 7 (4) --> 8 (4) --> 9 (4) --> 10 (4) --> 11 (4)
# l'algorithme attribue donc la salle au cours 1 puis aux cours 2 et 5 (3 cours)
# alors qu'on pourrait attribuer la salle aux cours 2, 3, 4, 5 (4 cours)


# Question 8
def f(t):
    return t[1]

# Question 9
def reservation_glouton(L):
    list.sort(L,key=f)
    R = [L[0]]
    for i in range(1,len(L)):
        if L[i][0] >= R[-1][1]:
            R.append(L[i])
    return R

L = [[8,10,"1"],[8,9,"2"],[8.5,10,"3"],[9,10,"4"],[9.5,11,"5"],[10,12,"6"],[10,12,"7"],[10.5,12.5,"8"],[10.5,11.5,"9"],[11,13,"10"]]

# print(reservation_glouton(L))

# Question 10
# L'algorithme consiste à trier la liste, en n*log(n) opérations, puis à parcourir une fois la liste en effectuant une comparaison, ce qui est de complexité linéaire. Le temps de la seconde étape est dominé par le temps de la première, donc la complexité totale est en n*log(n).

# Question 11
# Soit f_1,f_2,...,f_k l'ensemble des dates de fin des cours donné par l'algorithme glouton. Pour chaque i entre 1 et k, f_i est la date de fin de cours minimale parmi toutes les dates de fin de cours compatibles avec f_1,...,f_{i-1}.
# On va montrer que pour tout i<=k, il existe une solution optimale commençant par les i premiers cours sélectionnés par l'algorithme glouton.
#Initialisation : pour i=0, toute solution optimale convient
#Hérédité : Soit i < k, on se donne une solution optimale commençant par  les i premiers cours de l'algo glouton, dont les dates de fin de cours sont f_1,...,, f_i, g_(i+1), ..., g_l
# Le (i+1)e cours de l'algorithme glouton et de la solution optimale est compatible avec les i premiers. Par principe de l'algorithme glouton, on a donc f_(i+1) <= g_(i+1). On peut donc remplacer dans la solution optimale le (i+1)e cours par celui de l'algorithme glouton, et obtenir une solution optimale commençant par les i+1 premiers cours de l'algorithme glouton
#En conclusion, il existe une solution optimale commençant par tous les cours sélectionnés par l'algorithme glouton. Par principe de l'algorithme glouton, aucun autre cours n'est compatible, donc cette solution optimale ne contient pas d'autre cours. L'algorithme glouton est donc optimal.



# Question 12

# On écrit d'abord une fonction donnant l'ensemble des sous-listes (parties) d'une liste (ensemble). On peut utiliser une fonction récursive qui, étant donnée une liste, construit l'ensemble des parties de la liste obtenue en excluant le premier élément et qui ensuite ajoute cet éléments aux parties ou non. Pour la même raison qu'à la question 3, on utilise en argument supplémentaire le rang à partir duquel il faut considérer la liste
def parties_aux(L,i):
    if i==len(L):
        return [[]]
    else:
        parties_fin = parties_aux(L,i+1)
        parties_tot = []
        for p in parties_fin:
            parties_tot.append(p)
            parties_tot.append([L[i]]+p)
        return parties_tot

def parties(L):
    return parties_aux(L,0)

# print(parties([1,2,3]))

# On définit une fonction indiquant si une liste de cours correspond à une réservation valide
def resa_valide(L):
    n = len(L)
    for i in range(n):
        for j in range(i+1,n):
            if L[i][0]<L[j][1] and L[i][1]>L[j][0]:
                return False
    return True

def reservation_brute(L):
    part = parties(L)
    M = 0 # nombre max de cours
    for p in part:
        if len(p)>M and resa_valide(p):
            M = len(p)
            resa = p
    return resa

L = [[8,10,"1"],[8,9,"2"],[8.5,10,"3"],[9,10,"4"],[9.5,11,"5"],[10,12,"6"],[10,12,"7"],[10.5,12.5,"8"],[10.5,11.5,"9"],[11,13,"10"]]
# print(reservation_brute(L))
print(len(reservation_brute(L))==len(reservation_glouton(L)))