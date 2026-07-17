def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b,a%b)

def afficher_ligne(n):
    print ('*'*n)

def tracer_triangle(n):
    if n>0:
        afficher_ligne(n)
        tracer_triangle(n-1)

def tracer_triangle2(n):
    if n>0:
        tracer_triangle2(n-1)
        afficher_ligne(n)

#Version de complexité exponentielle
def u(a,n):
    if n==0:
        return a
    return (u(a,n-1)+a/u(a,n-1))/2

#Version de complexité linéaire (donc bien bien mieux)
def u(a,n):
    if n==0:
        return a
    r = u(a,n-1)
    return (r+a/r)/2

def expo_rapide(k,n):
    if n==0:
        return 1
    r = expo_rapide(k,n//2)
    if n%2==0:
        return r*r
    else:
        return k*r*r

def bin(n):
    if n==0:
        return []
    L = bin(n//2)
    L.append(n%2)
    return L


#Version de complexité exponentielle
def fibo(n):
    if n==0 or n==1:
        return 1
    return fibo(n-2) + fibo(n-1)

#Version de complexité linéaire (donc bien bien mieux)
def fibo(n):
    def aux(n): #aux(n) renvoie (F_(n-1),F_(n)), avec F_(-1) = 0
        if n==0:
            return(0,1)
        else:
            a,b = aux(n-1)
            return(b,a+b)
    return aux(n)[1]

def recherche_dicho_bornes(L,x,a,b):
    if a > b:
        return False
    m = (a+b)//2
    if x<L[m]:
        return recherche_dicho_bornes(L,x,a,m-1)
    elif x>L[m]:
        return recherche_dicho_bornes(L,x,m+1,b)
    else:
        return True

def recherche_dicho(L,x):
    return recherche_dicho_bornes(L,x,0,len(L)-1)



def hanoi():
    def aux(d,t,a,n):#d est le numéro de la pile de départ, t le numéro de la pile transitoire et a le numéro de la pile d'arrivée. n est le nombre de disques à déplacer.
        if n>0:
            aux(d,a,t,n-1)
            print(d,"->",a)
            aux(t,d,a,n-1)
    aux(1,2,3,7)


from turtle import *

def tracer_carre():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)


def koch(n,l):
    if n==0:
        forward(l)
    else:
        koch(n-1,l/3)
        left(60)
        koch(n-1,l/3)
        right(120)
        koch(n-1,l/3)
        left(60)
        koch(n-1,l/3)

def flocon(n,l):
    for _ in range(3):
        koch(n,l)
        right(120)

speed('fastest')
flocon(5,300)
bye()




