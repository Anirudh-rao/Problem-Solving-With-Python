from unicodedata import digit


def SumOfDigits(a:list):
    res = [sum(int(digit) for digit in str(val)) for val in a]
    print(f"The Sum of Digits Using List Comprehehsion:{res}")
    resM = list(map(lambda val: sum(int(digit) for digit in str(val)), a))
    print(f"The Sum of Digits Using Lambda  Function:{resM}")
    result = []
    for val in a:
        total = 0
        while val> 0:
            total += val % 10
            val //= 10
        result.append(total)
    print(f"The Sum of Digits Using For Loop:{result}")


b = [123, 456, 789] 
SumOfDigits(b)