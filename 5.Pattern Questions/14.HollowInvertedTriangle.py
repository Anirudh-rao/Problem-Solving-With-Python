def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []
    
    # Loop through each row from n to 1
    for i in range(n, 0, -1):
        # For the first row, just add 'n' stars
        if i == n:
            triangle.append('*' * n)
        # For the last row, add a single star
        elif i == 1:
            triangle.append('*')
        # For the intermediate rows, add a star, spaces, and another star
        else:
            # Add a star, spaces, and another star
            spaces = ' ' * (i - 2)
            triangle.append('*' + spaces + '*')
    
    # Return the list of triangle rows
    return triangle
print(generate_hollow_inverted_right_angled_triangle(4))