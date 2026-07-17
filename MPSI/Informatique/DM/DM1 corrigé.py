import numpy as np
import matplotlib.pyplot as plt

N = 200

def appartient(z):
    u = z
    for k in range(N):
        if abs(u) > 2:
            return False
        u = u**2 + z
    return True

def afficher_mandelbrot(a, b, c, d):
    X = []
    Y = []
    abscisses = np.linspace(a, b, 1000)
    ordonnees = np.linspace(c, d, 1000)
    for x in abscisses:
        for y in ordonnees:
            z = x + y * 1j
            if appartient(z):
                X.append(x)
                Y.append(y)
    plt.axis('equal')
    plt.plot(X, Y, ".", ms=0.2)
    plt.show()

def rang(z):
    u = z
    for k in range(N):
        if abs(u) > 2:
            return k
        u = u**2 + z
    return N

def afficher_mandelbrot_couleur(a, b, c, d):
    h = 1000
    l = int(h * (b - a) / (d - c))
    img = np.zeros((h, l))
    for i in range(h):
        for j in range(l):
            x = a + j * (b - a) / (l - 1)
            y = d - i * (d - c) / (h - 1)
            z = x + y * 1j
            img[i][j] = rang(z)
    plt.imshow(img, cmap="hot")
    plt.show()

