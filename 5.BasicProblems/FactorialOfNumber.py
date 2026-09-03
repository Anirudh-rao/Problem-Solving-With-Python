def factorial(n):
    result = 1
    if n < 0:
        return result
    else:
        return 1 if n <= 1 else n * factorial(n-1)



print(factorial(6))  
print(factorial(-3))
  
    