def SwapWithAddition(a,b):
    c = a +b
    b = c-b
    a = c-a
    return a,b
print(SwapWithAddition(12,13))