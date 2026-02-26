def PrimeNumberM1(x,y):
    """Sieve of Ertosthenes Algorithm"""
    primes = [True] * (y+1)
    primes[0],primes[1]= False, False

    for i in range(2, int(y**0.5)+1):
        if primes[i]:
            for j in range(i * i, y+1, i):
                primes[j] = False

    res = [i for i in range(x,y+1) if primes[i]]
    print(res if res else "No")


def PrimeNumberM2(x,y):
    """Using Trail Division"""
    res =[]
    for n in range(x,y +1):
        if n <= 1:
            continue
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i ==0:
                is_prime = False
                break
        if is_prime:
            res.append(n)
    print(res if res else "No")

print("Checking Primes using Sieve of Ertosthenes Algorithm\n")
PrimeNumberM1(2,7)
print("Checking Primes using trailing division\n")
PrimeNumberM2(2,7)
