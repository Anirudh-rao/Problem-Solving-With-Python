def maxoftwo(n,m):
    print("The First Method:")
    print(f"The max of two numbers {n} and {m} is ", max(n,m))
    print("The Second Method:")
    print(f"The max of two numbers {n} and {m} is ", n if n > m else  m)
    num = [n, m]
    num.sort()
    print("The Third Method:")
    print(f"The max of two numbers {n} and {m} is ",num[-1])  

maxoftwo(10,29)
maxoftwo(30,29)

