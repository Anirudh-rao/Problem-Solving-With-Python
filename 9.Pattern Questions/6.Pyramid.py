def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    pyramid = []
    for i in range(1,n+1):
        # Numbers stars in the current  row is 2*i-1
        stars =  '*' * (2*i-1)
        # Number of leading spaces to center the stars is n-i
        spaces = ' ' * (n-i)
        pyramid.append(spaces + stars + spaces)
    return pyramid

print(generate_pyramid(4))