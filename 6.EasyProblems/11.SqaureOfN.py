def SquareNaturaNumbers(n):
    res = n * (n + 1) * (2 * n + 1) // 6
    print("The Square of Natural Number :",res)
    res = sum(x * x for x in range(1, n + 1))
    print("The Square of Natural Number Method 2 :",res)
    total = 0

    for i in range(1, n + 1):
        total += i * i
    print("The Square of Natural Number Method 3 :",total)
 
SquareNaturaNumbers(10)
SquareNaturaNumbers(20)
