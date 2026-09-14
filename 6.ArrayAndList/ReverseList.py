def ReverseListFunction(lst):
    result = lst[::-1]
    print(f"The Original List :{lst}")
    print(f"\nThe Reversed List:{result}")
    lst2 = lst
    lst2.reverse()
    print(f"\nThe Reverse of List using Reverse function:{lst2}")
    i,j =0, len(lst)-1
    a = lst
    while i < j:
        a[i], a[j] = a[j], a[i]
        i+= 1
        j -= 1
    print(f"\nThe Reverse of List using  for loop:{a}")


a = [1, 2, 3, 4, 5]
ReverseListFunction(a)