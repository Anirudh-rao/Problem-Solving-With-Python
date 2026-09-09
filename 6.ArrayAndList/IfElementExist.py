def CheckIfElementExist(lst, n):
    for i in lst:
        if i == n:
            print(f"Element exist in list")
    if n in lst:
        print(f"Element exist in list at position Using method 2")

    flag = any(x == 30 for x in lst)
    if flag:
        print(f"Element exist in list using any function")

a = [10, 20, 30, 40, 50]
CheckIfElementExist(a, 30)