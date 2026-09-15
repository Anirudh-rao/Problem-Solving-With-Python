from re import L


def EvenNumbersInrange(n,m):
    if n % 2 != 0:
        n = n+ 1
    if m % 2 != 0:
        m = m + 1
    for i in range(n, m, 2):
          print(i)
    res= [i for i in range(n, m+1) if i %2 == 0]
    print(res)


EvenNumbersInrange(1,10)
    