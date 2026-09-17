def RemoveElements(a:list, res:list):
    ress = []
    b = a
    for i in a:
        if i in res:
            ress.append(i)
            b.remove(i)

    print(f"The original list:{a}")
    print(f"List after removing :{b}")
    print(f"The Removed elements:{ress}")

    resA = [x for x in a if x not in res ]
    print(f"The List After removing elements using list comphrehension:{resA}")

a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]
RemoveElements(a, remove)