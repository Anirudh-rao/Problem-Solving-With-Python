def OddNumbers(n,m):
    for num in range(1,m+1, 2):
        print(num)

    for num in range(n,m+1):
        if num & 1 :
            print(num)

    res = [num for num in range(n, m + 1) if num % 2 != 0]
    print(res)

OddNumbers(1,10)