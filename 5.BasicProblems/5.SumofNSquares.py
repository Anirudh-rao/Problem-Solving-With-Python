def generateSquares(n):
    return sum([i**2 for i in 
               range(1, n + 1)])

print(generateSquares(12))