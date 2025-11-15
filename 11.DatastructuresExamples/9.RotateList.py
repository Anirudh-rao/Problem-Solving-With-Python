def rotate_list(lst, k):
    # Your code goes here
    if not lst:
        return []
    
    # Modulo to handle the case where k is greater than the length of the list
    k = k % len(lst)
    
    # Brute force approach using loops
    for _ in range(k):
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Insert it at the front
    
    return lst

L = [1,2,2,3,4,45,56]
print(rotate_list(L,2))