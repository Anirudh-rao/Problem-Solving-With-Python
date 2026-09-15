import heapq

def NLargestelement(lst,n):
    print(heapq.nlargest(n, lst))
    res = sorted(lst, reverse=True)[:n]
    print(res)
    lst.sort()
    print(lst[-n:])

l = [1000, 298, 3579, 100, 200, -45, 900]
NLargestelement(l, 2)