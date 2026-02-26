def PrimeNumbers(n):
    if n<= 1:
        print(False)
    else:
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
        print(is_prime)

def is_prime(n):
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]

from math import sqrt

def PrimeRec(n, i):  
    if i == 1 or i == 2:  
        return True
    if n % i == 0:  
        return False

    return PrimeRec(n, i - 1)

n = 13
i = int(sqrt(n) + 1)

print(PrimeRec(n, i))

num = 31
print(is_prime(num))
print(PrimeNumbers(num))