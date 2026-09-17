import itertools


def CumulativeSum(a:list):
    res = list(itertools.accumulate(a))
    print(f"The Cumulative Sum:{res}")
    total = 0
    result = []
    for num in a:
        total += num
        result.append(total)
    print(f"The Cumulative Sum Using For loop:{result}")
l = [1, 2, 3, 4]
CumulativeSum(l)