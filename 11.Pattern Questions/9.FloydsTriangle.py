def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    Triangle = []
    #Initialize first number to be used in Triangle
    current_num =  1
    for i in range(1, n+1):
        # create a row by collecting the next i numbers
        row  = ' '.join(str(current_num + j) for j in range(i))
        # Append the row to the list
        Triangle.append(row)
        current_num += i
    return Triangle

print(generate_floyds_triangle(3))