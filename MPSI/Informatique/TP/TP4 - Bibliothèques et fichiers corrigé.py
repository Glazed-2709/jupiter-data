#Exercice 1
import math

def transformer_liste(L):
    R = []
    for w in L:
        y = math.cos(2*math.pi*w)**2/2
        R.append(y)
    return R

#version plus concise :
def transformer_liste(L):
    return [math.cos(2*math.pi*w)**2/2 for w in L]

import numpy as np

def transformer_tableau(T):
    return np.cos(2*pi*T)**2/2

def moyenne(T):
    return np.sum(T)/len(T)

def coeff_regression_lineaire(X, Y):
    n = len(X)
    a = (n*np.sum(X*Y)-np.sum(X)*np.sum(Y))/(n*np.sum(X*X)-(np.sum(X))**2)
    b = moyenne(Y)-a*moyenne(X)
    return a, b

#Exercice 2

import matplotlib.pyplot as plt   #import des fonctions d'affichage
def f(x):
    return cos(x)

X = [] #Initialisation de la liste des abscisses
Y = [] #Initialisation de la liste des ordonnées
n = 100000 #Nombre de points utilisés dans le tracé
a = 0
b = 2*pi
for i in range(n):
    x = a + i*(b-a)/n   #Calcul de l'abscisse pour un point
    X.append(x)         #Ajout de cette abscisse dans X
    Y.append(f(x))      #Ajout de l'ordonnée correspondante dans Y
plt.plot(X,Y)         #plot prend en entrée les liste d'abscisses et d'ordonnées, et trace la courbe
plt.show()



T = np.linspace(0,2*pi,100000)
C = np.cos(T) #mieux vaut ne calculer les cosinus qu'une seule fois
X = C*(1+C)
Y = np.sin(T)*(1+C)
plt.plot(X, Y, "-r")
plt.title("Cardioïde de paramètre 1")
plt.show()

#Exercice 3

F = open('profits.txt','r')
lignes = F.readlines()
X = []
Y = []

for ligne in lignes:
    ligne = ligne.strip()
    population, profit = ligne.split(',')
    X.append(float(population))
    Y.append(float(profit))
F.close()

X = np.array(X)
Y = np.array(Y)

a,b = coeff_regression_lineaire(X,Y)
plt.plot(X, Y, "x")
plt.plot(X, a*X+b)
plt.show()

#Exercice 4

def correction(gamma,x):
    note = (x**gamma)*(20**(1-gamma))
    arrondi = (np.ceil(note*10))/10
    return arrondi

F1 = open('notes.txt','r',encoding="utf8")
F2 = open('notes2.txt','w',encoding="utf8")

ligne_0 = F1.readline()
F2.write(ligne_0)

lignes = F1.readlines()

for ligne in lignes:
    ligne = ligne.strip()
    nom, prenom, note = ligne.split(';')
    note = float(note)
    somme += note
    F2.write(nom+";"+prenom+";"+str(correction(0.8,note)))
    F2.write("\n")

F1.close()
F2.close()

def est_premier(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

k = 2
nb = 0
F = open("nombres_premiers.txt", 'w')
while nb < 1000:
    if est_premier(k):
        nb += 1
        F.write(str(k)+"\n")
    k += 1
F.close()


def analyse(nom_fichier):
    F = open(nom_fichier, 'r')
    lignes = F.readlines()
    nb_lignes = len(lignes)
    nb_char = 0
    nb_mots = 0
    for ligne in lignes:
        ligne = ligne.strip()
        nb_char += len(ligne)
        mots = ligne.split(' ')
        nb_mots += len(mots)
    F.close()
    return nb_char, nb_mots, nb_lignes

analyse("hello world.txt")
