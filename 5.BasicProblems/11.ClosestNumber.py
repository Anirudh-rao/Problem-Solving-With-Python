def closestNumber(n,m):
    q = int(n/m)
    #1st possible closest number
    n1 = m * q

    #2nd Possible Closest Number
    if ((n* m)> 0):
        n2 = (m*(q+1))
    else:
        n2 = (m*(q-1))
    if (abs(n-n1) < abs(n-n2)):
        return n1
    return n2

print(closestNumber(13,4))