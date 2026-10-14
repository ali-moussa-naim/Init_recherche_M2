"""
Fonction principale de réduction modulaire
"""
def reduire(c, n, delta):
    q, r0 = separer(c, n)
    i = 0
    r = r0
    while(i < len(q)):
        qi = mult_list(q[i:], delta)

        bloc_haut = qi[n:]
        bloc_bas = qi[:n] 

        q = q[:i] + bloc_haut
        r = bloc_bas + r
        i += 1
    
    while(r >= delta):
        r = r - delta
    
    return q, r

"""
Fonction pour séparer un entier entre son quotient et reste
pour n = 10^n
c : liste
n : entier
"""
def separer(c, n):
    q0 = c[n:]
    r0 = c[:n]
    return q0, r0

"""
Fonction qui multiplie un entier * delta
c : liste représentant un entier
delta : entier
"""
def mult_list(c, delta):
    res = []
    retenue = 0

    for chiffre in c:
        produit = chiffre * delta + retenue
        res.append(produit % 10)
        retenue = produit // 10

    while retenue > 0:
        res.append(retenue % 10)
        retenue = retenue // 10

    return res
    

# c = 12345678
c = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 3
#print(separer(c, n))
#print(mult_list(c, n))
print(reduire(c, 4, 97))

