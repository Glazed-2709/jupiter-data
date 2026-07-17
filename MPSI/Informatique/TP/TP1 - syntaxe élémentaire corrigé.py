def distance(a,b):
    if a<b:
        return b-a
    else:
        return a-b

def distance_manhattan(a,b,c,d):
    return distance(a,c) + distance(b,d)

def mystere(a):
    b = 2
    while a%b == 0:
        b = b + 1
    return b

#Cette fonction renvoie le plus petit entier naturel non nul qui ne divise pas a

def minimum3(a,b,c):
    if a <= b and a <= c:
        return a
    elif b<=c and b <= a:
        return b
    else:
        return c

#4a : n%2 == 0

#4b : n*m >= 0

#4c : x == z or y == t

#4d : (n != 0 and m%n == 0) or (n == m == 0)

#4e : (x-z)**2 + (y-t)**2 <= r**2


def somme_inverse_carres(n):
    r = 0
    for i in range(1, n+1):
        r = r + 1/(i**2)
    return r

print(somme_inverse_carres(1000000))

def nieme_terme(a, n):
    u = a
    for _ in range(n):
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
    return u


def temps_de_vol(a):
    r = 0
    u = a
    while u != 1:
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
        r = r+1
    return r

def altitude_maximale(a):
    r = a
    u = a
    while u != 1:
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
        if u > r:
            r = u
    return r

def test_conjecture(k):
    for a in range(1,k+1):
        temps_de_vol(a)
    return True

def test_conjecture_infini():
    a = 1
    while True:
        b = temps_de_vol(a)
        print(a, " vérifie la conjecture. Temps de vol : ", b)
        a = a + 1

def somme_chiffres(n):
    a = n
    s = 0
    while a>0:
        s = s + a%10
        a = a//10
    return s


def nombre_palindrome(n):
    rev = 0
    m = n
    while m>0:
        rev = rev*10 + m%10
        m = m//10
    return rev==n