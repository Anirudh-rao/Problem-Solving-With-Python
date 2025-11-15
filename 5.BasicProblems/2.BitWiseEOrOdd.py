def BitWiseEvenOrOdd(n):
    if (n & 1) == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return result

print(BitWiseEvenOrOdd(5))