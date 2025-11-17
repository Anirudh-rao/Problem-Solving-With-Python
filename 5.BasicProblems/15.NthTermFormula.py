def nthTermOfAP(a1, a2, n):
    # using formula to find the
    # Nth term t(n) = a(1) + (n-1)*d
    return a1 + (n - 1) * (a2 - a1)


a1 = 2
a2 = 3
n = 4
print(nthTermOfAP(a1, a2, n))