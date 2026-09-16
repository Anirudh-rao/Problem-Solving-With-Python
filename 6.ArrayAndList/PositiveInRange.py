def PositiveNoInRange(m,n):
    result = []
    for i in range(m,n):
        if i % 2 == 0:
            result.append(i)
    print(f"The Positive Numbers in range {m} to {n} :\n {result}")
    res = [i for i in range(m,n) if i % 2 == 0]
    print(f"The Positive Numbers in range {m} to {n} Using List Comprhenesion :\n {res}")



PositiveNoInRange(1,50)
