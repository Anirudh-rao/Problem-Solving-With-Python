def remove_duplicates(lst):
    # Your code goes here
    lst.sort()
    #One method is to convert to setattr
    my_set = set(lst)
    my_lst = list(my_set)
    return my_lst


def remove_duplicates_method_2(lst):
    # Your code goes here
    lst.sort()
    unique_lst = []
    #One method is to convert to setattr
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))
#method 2
print(remove_duplicates_method_2(lst))