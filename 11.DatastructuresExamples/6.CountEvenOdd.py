def count_even_odd(lst):
    
    """
    You are given a list of integers.
    Write a Python program that counts and returns the number of even and odd numbers in the list.
    
    """
    # Your code goes here
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even , odd
            
