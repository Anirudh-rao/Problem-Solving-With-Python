def is_palindromic_tuple(tup):
    # Initialize pointers for the start and end of the tuple
    start = 0
    end = len(tup) - 1
    
    # Loop until the start pointer is less than or equal to the end pointer
    while start <= end:
        # If elements at start and end pointers are not equal, it's not a palindrome
        if tup[start] != tup[end]:
            return False
        # Move the pointers towards the center
        start += 1
        end -= 1
    
    # If all elements matched, it is a palindrome
    return True


Input = (1, 2, 3, 2, 1)
print(is_palindromic_tuple(Input))

Input = ('a', 'b', 'c', 'b', 'a')
print(is_palindromic_tuple(Input))


Input = ('x', 'y', 'z', 'x')
print(is_palindromic_tuple(Input))