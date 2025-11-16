def SwapWithArthmeticOperator(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a,b
print(SwapWithArthmeticOperator(12,13))