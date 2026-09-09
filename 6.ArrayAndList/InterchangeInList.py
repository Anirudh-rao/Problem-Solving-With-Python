def InterchangeValues(lst):
    newlist = lst
    lst[0] , lst[-1] = newlist[-1], newlist[0]
    return newlist

lst = [1, 2, 3, 4, 5]
print(InterchangeValues(lst))