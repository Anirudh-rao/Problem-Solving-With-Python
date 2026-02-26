def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    square = []
    if n == 1:
        return['*']
    
    square.append('*'* n)
    
    # For middle rows first and last charecters are '*'
    for i in range(n-2):
        square.append('*' + ' ' * (n-2) + '*')
    
    square.append('*' * n)
    return square
        

        
print(generate_hollow_square(5))