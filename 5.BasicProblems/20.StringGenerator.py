def larger_string(text :str , n:int):
    result = " "
    for i in range(n):
        result = result + text

    return result

print(larger_string('abc', 2))

# Call the "larger_string" function with the arguments '.py' and 3, then print the result
print(larger_string('.py', 3))
