def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Initialize an empty list to store the rows of the pyramid
    pyramid = []
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Create leading spaces for centering the numbers
        spaces = ' ' * (n - i)
        # Create a string of numbers from 1 to i, joined by spaces
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        # Add the row with spaces and numbers to the pyramid
        pyramid.append(spaces + numbers + spaces)
    
    # Return the list of pyramid rows
    return pyramid

print(generate_number_pyramid(4))