"""
Fonction qui retourne l'entier représenté par cette liste L
L : liste d'entiers de 64 bits
"""
def toint(L):
    res = 0
    i = 0

    while(i < len(L)):
        res = res | (L[i] << 64 * i)
        i += 1

    return res

"""
Fonction qui retourne une liste de deux mots de 64 bits représentant cet entier a
a : entier de 128 bits
"""
def tolist(a):
    L = []

    while(a > 0):
        r = a & ((1 << 64) - 1)
        L.append(r)
        a = a >> 64
    
    return L

"""
Fonction retournant le reste de la division x par Phi = 2^128
x : liste représentant un entier de 256 bits
"""
def modphi(x):
    return x[:2]

"""
Fonction retournant le quotient de la division entière x par R
x : liste représentant un entier de 256 bits
"""
def divphi(x):
    return x[2:]

"""
Fonction réalisant l'addition de deux entiers de 256 bits représentés par des listes de quatre mots
x, y : 2 liste de 2 entiers de 256 bits
"""
def plus(x, y):
    res = []
    retenue = 0
    i = 0

    while(i < len(x)):
        add = (x[i] + y[i] + retenue) 
    return res, retenue



L = [1, 2]
#print(toint(L))

a = 2**64 + 5
#print(tolist(a))

x = [5, 10, 20, 30]
y = [7, 15, 25, 35]
print(plus(x, y))