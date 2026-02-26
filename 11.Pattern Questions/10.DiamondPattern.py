def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    diamond = []
    for i in range(1, n+1):
        stars =  '*' * (2*i-1)
        spaces = ' '* (n-i)
        diamond.append(spaces + stars + spaces)
    for i in range(n-1, 0,-1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        diamond.append(spaces + stars + spaces)
    return diamond
    

print(generate_diamond(2))