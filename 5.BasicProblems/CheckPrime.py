from sympy import isprime

# From sympy method
def CheckPrimeWithSympy(n):
    isPrime = isprime(n)
    return isPrime

#
def CheckPrimeAnother(n):
    if n <= 1:
        print(False)
    else:
        prime = True
        for i in range(2, int(n**0.5) +1):
            if n % i == 0:
                priime = False
                break
        print(prime)

n = 29
print(CheckPrimeWithSympy(n))
CheckPrimeAnother(n)