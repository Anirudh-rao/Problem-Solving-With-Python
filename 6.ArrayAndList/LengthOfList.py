def LengthOfListFunctions(lst):
    print(f"The Length of the list {lst} using len function: ",len(lst))
    result = 0
    for i in lst:
        result += 1
    print(f"The Length of the list {lst} using for loop: {result}")


lst =  [1, 2, 3, 4, 5]
LengthOfListFunctions(lst)

    
