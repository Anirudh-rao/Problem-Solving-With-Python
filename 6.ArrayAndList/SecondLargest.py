import heapq
def SecondLargets(lst):
    lst2 = lst
    lst2.sort(reverse=True)
    print(f"The Second Largest Number :{lst2[1]}")
    res = heapq.nlargest(2, lst)
    print(f"The Second Largest Using heapq :{res[1]}")


a = [10, 20, 4, 45, 99]
SecondLargets(a)