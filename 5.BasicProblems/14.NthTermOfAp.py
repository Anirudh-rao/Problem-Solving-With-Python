def NthTermOfAp(a1,a2,n):
    ntherm = a1
    d = a2-a1
    for i in range(1,n):
        ntherm += d
    return ntherm

a1 = 2
a2 = 3
n = 4
print(NthTermOfAp(a1,a2,n))