def ListCopying(lst:list):
    print(f"The Original List:{lst}")
    a = lst.copy()
    print(f"The Copied List:{a}")
    b = lst[:]
    print(f"The Copied List using Slicing:{b}")
    c = list(lst)
    print(f"The Copied List using list function:{c}")
    d  = [item for item in lst]
    print(f"The Copied List using List comprehension:{d}")


a = [1,2,3,4,5,6]
ListCopying(a)