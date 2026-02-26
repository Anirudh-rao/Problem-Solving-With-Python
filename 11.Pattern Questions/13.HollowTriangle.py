def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # For the first row, just add one star
        if i == 1:
            triangle.append('*')
        # For the last row, add 'n' stars
        elif i == n:
            triangle.append('*' * n)
        # For the intermediate rows, add a star, spaces, and another star
        else:
            # Add the row: one star, and one star
            triangle.append('*' + ' ' * (i - 2) + '*')
    
    # Return the list of triangle rows
    return triangle
print(generate_hollow_right_angled_triangle(4))