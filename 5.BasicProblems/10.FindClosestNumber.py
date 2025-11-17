def closest_number(n, m):
    # find the quotient
    closest = 0
    min_difference = float('inf')

    # Check numbers around n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)

            if difference < min_difference or \
            			(difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

  
n = 13
m = 4
print(closest_number(n, m))