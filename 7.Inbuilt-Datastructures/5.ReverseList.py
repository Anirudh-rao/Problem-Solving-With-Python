def reverse_list(lst):
    """
    You are given a list of integers. 
    Write a Python program that reverses the list without using slicing (lst[::-1]).
    The program should return the reversed list.


    """
    # Your code goes here
    #Creating Start and End Index
    start = 0
    end =  len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst
    
    