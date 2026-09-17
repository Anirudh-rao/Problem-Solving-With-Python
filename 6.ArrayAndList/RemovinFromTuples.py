def RemoveTupleFromList(a:list):
    res = [t for t in a if t]
    print(f"The Result:{res}")
    result = list(filter(None, a))
    print(f"The Result Using Filter:{result}")
    restl =[]
    for t in a:
        if t:
            restl.append(t)
    print(f"The Result using for Loop:{restl}")

a = [(1, 2), (), (3, 4), (), (5,)]
RemoveTupleFromList(a)