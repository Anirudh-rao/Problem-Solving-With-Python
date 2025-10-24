"""
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
"""

def generate_square(n):
    square = []
    for i in range(n):
        square.append('*' * n)
    return square

print(generate_square(10))
print(generate_square(30))
