def bin(k,n):
    if n==0:
        return []
    else:
        l = bin(k//2,n-1)
        l.append(k%2)
        return l
bin(76,8)

def Horner(L):
    r = 0
    for x in L:
        r = 2*r + x
    return r

Horner([1,1,0,1,0,0,1,1])

def vers_complement_a_2(k,n):
    if k>0:
        return bin(k,n)
    else:
        return bin(k+2**n,n)

def depuis_complement_a_2(L):
    n = len(L)
    if L[0]==0:
        return Horner(L)
    else:
        return Horner(L) - 2**n

def oppose(L):
    n = len(L)
    for i in range(n-1,-1,-1):
        if L[i] == 1:
            return [1-x for x in L[:i]] + L[i:]
    return L

a = 1.0
while 10*a != float("inf"):
    a = a*10
print(a)

a = 1.0
while a/10 != float(0):
    a = a/10
print(a)


a = 1.0
while a != a+1 :
	a = a*10
print(a)

from time import *
def C(n):
    t1 = time()
    r = 0
    k = 10**n
    for _ in range(1000000):
        r = k+k
    return time() - t1

#Ly = [C(10*n) for n in range(100)]

#Lx = [10*n for n in range(100)]

#from matplotlib.pyplot import *

#plot(Lx,Ly)

def addition(L1,L2):
    n = len(L1)
    R = [0]*n
    r = 0
    for i in range(n-1,-1,-1):
        m = L1[i]+L2[i]+r
        R[i] = m%2
        r = m//2
    if (L1[0]==0 and L2[0]==0 and R[0]==1) or (L1[0]==1 and L2[0]==1 and R[0]==0):
        print("Attention : dépassement arithmétique")
    return R

addition([1,1,0,1,1,0,1,0], [1, 0, 1, 1, 0, 0, 1, 0])
addition([0,1,0,1,0,1,1,0], [0, 1, 1, 0, 0, 0, 1, 1])
addition([0, 1, 1, 1, 1, 0, 1, 1],[1, 0, 1, 1, 1, 0, 0, 0])

addition(bin(3,8),bin(-23,8))

def soustraction(L1,L2):
    return addition(L1,oppose(L2))

def racines1(a,b,c):
    delta = b**2-4*a*c
    assert Delta > 0
    s = delta**(1/2)
    return (-b-s)/(2*a), (-b+s)/(2*a)

for i in range(1,8):
    a= 7*(10**(-i))
    x1, x2 = racines1(a,1/a,-a)
    print('a=', a, ', x1=', x1,', x2=', x2, ', x1*x2=', x1*x2 )


def racines2(a,b,c):
    delta = b**2-4*a*c
    assert delta > 0
    s = delta**(1/2)
    if b > 0:
        x1 = (-b-s)/(2*a)
    else:
        x1 = (-b+s)/(2*a)
    x2 = c/(a*x1)
    return x1, x2


for i in range(1,8):
    a= 7*(10**(-i))
    x1, x2 = racines2(a,1/a,-a)
    print('a=', a, ', x1=', x1,', x2=', x2, ', x1*x2=', x1*x2 )

from math import sqrt
M = sqrt(2)*(1+10**(-14))
m = sqrt(2)
print(M-m)