# An Armstrong number is a number that is equal to the sum of its digits raised to the power of the total number of digits.
def AmstrongNumber(n):
    l = len(str(n))
    t = n
    s = 0
    while t > 0:
        d = t % 10
        s += d ** l 
    if s == n:
        print("Amstrong Number")
    else:
        print("Not Amstrong Number")

print(AmstrongNumber(153))
print(AmstrongNumber(255))