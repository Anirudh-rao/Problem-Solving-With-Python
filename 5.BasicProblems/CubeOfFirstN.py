def CubeOfFirN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i **3
    return sum

n = 4
print(CubeOfFirN(n))
res = sum(i**3 for i in range(1, n+1))
print(res)