def MaxOfTwoNumbers(a, b):
    if a > b:
        return a
    else:
        return b

a = 5 
b = 7
print(f"Using Max function:", max(a,b))
print(MaxOfTwoNumbers(a,b))
print(f"Using Terneray Operator: ", a if a > b else b)