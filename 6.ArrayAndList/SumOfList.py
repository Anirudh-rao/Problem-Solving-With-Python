from functools import reduce

def SumOfElements(lst):
    res = sum(lst)
    print(f"The Original List:{lst}")
    print(f"The Sum of elements :{res}")
    result = 0
    for i in lst:
        result += i
    print(f"The Sumf of elments using For loop:{result}")
    complst = sum([i for i in lst])
    print(f"The Sum of elments using list Comprehension:{complst}")
    res = 0
    res = reduce(lambda x, y: x+y , lst)
    print(f"The sum of elements using Reduce:{res}")


a = [10, 20, 30, 40, 50]
SumOfElements(a)