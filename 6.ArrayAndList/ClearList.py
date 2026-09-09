def ClearnigLst(lst):
    result = lst.clear()
    print(f"The List :{lst}, has been cleard :{result}")
    result_2 = lst
    del result_2[:]
    print(f"The List :{lst}, has been cleard :{result_2} using method 2")

a = [1, 2, 3, 4, 5]
ClearnigLst(a)