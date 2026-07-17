import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

img = np.array(plt.imread('tigrenb.jpg'))

plt.figure()
plt.imshow(img, cmap=plt.cm.gray,vmin=0,vmax=255)
plt.show()


##############
# Question 1

def negatif(img):
    n,p = img.shape
    for i in range(n):
        for j in range(p):
            img[i,j] = 255 - img[i,j]

# negatif(img)
# plt.figure()
# plt.imshow(img, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()


#################
# # Question 2
def niveaux_de_gris(img):
    n,p = img.shape
    for i in range(n):
        for j in range(p):
            if 0 <= img[i,j] <= 79:
                img[i,j] = 60
            elif 80<=img[i,j]<=149:
                img[i,j] = 120
            else:
                img[i,j] = 220

# niveaux_de_gris(img)
# plt.figure()
# plt.imshow(img, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()


#########################
# Question 3
def eclaircir(img,m):
    n,p = img.shape
    for i in range(n):
        for j in range(p):
            img[i,j] = img[i,j] + m

# eclaircir(img,50)
# plt.figure()
# plt.imshow(img, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()
# pb : ce n'est pas éclairci : on retrouve du noir là où on s'attendrait à du blanc --> quand la valeur du pixel "dépasse 255", elle revient en fait modulo 256 à une "petite" valeur, donc on voit du noir. Il faut tronquer et laisser à 255 les valeurs supérieures.

def eclaircir2(img,m):
    n,p = img.shape
    for i in range(n):
        for j in range(p):
            if img[i,j] > 255 - m:
                img[i,j] = 255
            else:
                img[i,j] += m

# eclaircir2(img,100)
# plt.figure()
# plt.imshow(img, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()

def assombrir(img,m):
    n,p = img.shape
    for i in range(n):
        for j in range(p):
            if img[i][j] < m:
                img[i][j] = 0
            else:
                img[i][j] = img[i][j] - m

# assombrir(img,100)
# plt.figure()
# plt.imshow(img, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()


#########################
# Question 4
def flip_left(img):
    n,p = img.shape
    img_rot = np.zeros([p,n],np.uint8)
    for i in range(p):
        for j in range(n):
            img_rot[i][j] = img[j][p-1-i]
    return img_rot

# img_rot = flip_left(img)
# plt.figure()
# plt.imshow(img_rot, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()


#####################
# Question 5
def compression(img,n):
    m,p = img.shape
    img_comp = np.zeros([m//n,p//n],np.uint8)
    for i in range(m//n):
        for j in range(p//n):
            img_comp[i][j] = img[n*i][n*j]
    return img_comp

# img_comp = compression(img,3)
# plt.figure()
# plt.imshow(img_comp, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()


# #Variante plus concise, en utilisant les tranches :

# def compression(img,n):
#     img_com=img[::n, ::n]
#     return img_comp

#####################
# Question 6
def filtre(img,A):
    n,p = img.shape
    img2 = np.zeros([n,p],np.uint8)
    for i in range(n):
        for j in range(p):
            if i == 0 or i == n-1 or j == 0 or j == p-1:
                img2[i][j] = img[i][j]
            else:
                B = img[i-1:i+2,j-1:j+2]
                C = A*B
                s = np.sum(C)
                # si A n'est pas à coeff. entiers, s peut ne peut être un entier mais comme img2 est à coeff. dans [|0,255|], c'est en fait la partie entière de s qui est stockée.
                # Attention, si s sort de [|0,255|], il faut tronquer !
                if s < 0:
                    img2[i][j] = 0
                elif s > 255:
                    img2[i][j] = 255
                else:
                    img2[i][j] = s
    return img2

# A = np.array([[1/12,1/12,1/12],[1/12,4/12,1/12],[1/12,1/12,1/12]])
# img2 = filtre(img,A)
# plt.figure()
# plt.imshow(img2, cmap=plt.cm.gray,vmin=0,vmax=255)
# plt.show()


#####################################
#Question 7

Ah = np.array([[0,0,0],[-1,1,0],[0,0,0]])
imgh = filtre(img,Ah)
plt.figure()
plt.imshow(imgh, cmap=plt.cm.gray,vmin=0,vmax=255)
plt.show()

Av = np.array([[0,-1,0],[0,1,0],[0,0,0]])
imgv = filtre(img,Av)
plt.figure()
plt.imshow(imgv, cmap=plt.cm.gray,vmin=0,vmax=255)
plt.show()

# Le fait que imgh et imgv soient au format uint8 impose de calculer soigneusement pour détecter les éventuels dépassement.
def norme(a,b):
    r = np.sqrt(255)
    if a<=r and b<=r:
        if a**2 <= 255 - b**2:
            return np.sqrt(a**2+b**2)
    return 255

n,p = img.shape
imgc = np.zeros([n,p],np.uint8)
r = np.sqrt(255)
for i in range(n):
    for j in range(p):
        imgc[i][j] = norme(imgh[i][j],imgv[i][j])

negatif(imgc)
plt.figure()
plt.imshow(imgc, cmap=plt.cm.gray,vmin=0,vmax=255)
plt.show()

###########################
#Question 8

#En utilisant np.sum, pas de problème de dépassement malgré uint8
def moyenne(img,x1,x2,y1,y2):
    return np.sum(img[x1:x2+1,y1:y2+1])/((x2-x1+1)*(y2-y1+1))

def redimensionnement(img,rh,rl):
    n,p = img.shape
    print(n,p)
    p#our définir la taille de la nouvelle image, il faut faire attention au fait que les ratios rh,rl n'ont pas de raison d'être "bien choisis" donc il faut considérer les parties entières :
    h = int(n*rh)
    l = int(p*rl)
    print(h,l)
    img2 = np.zeros([h,l],np.uint8)
    #on va découper img en rectangles de taille 1/rh et 1/rl : problème ce ne sont pas des entiers !
    pas_h = int(1/rh)
    pas_l = int(1/rl)
    print(pas_h,pas_l)
    for i in range(h):
        for j in range(l):
            img2[i][j] = moyenne(img,int(i/rh),int(i/rh)+pas_h,int(j/rl),int(j/rl)+pas_l)
    return img2
#Noter qu'on perd les dernières pixels à droite et en bas....


img2 = redimensionnement(img,0.9,0.9)
plt.figure()
plt.imshow(img2, cmap=plt.cm.gray,vmin=0,vmax=255)
plt.show()
