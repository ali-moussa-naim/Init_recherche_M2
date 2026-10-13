# c est une liste
def reduire(c, n, delta):
    q0, r0 = separer(c, n)
    i = 0
    r = r0
    while(q0[i] > 0):
        q0[i+1] = ()
    return q0, r0

def separer(c, n):
    q0 = c[n:]
    r0 = c[:n]
    return q0, r0

def mult_list(c, delta):
    res = []
    for i in range(len(c)):
        retenue = (c[i] * delta) % 10
        

# c = 12345678
c = [8, 7, 6, 5, 4, 3, 2, 1]
n = 3
print(separer(c, n))