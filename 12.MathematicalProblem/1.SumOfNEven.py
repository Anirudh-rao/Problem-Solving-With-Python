def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    result = 0
    current_eve_number =  2
    for i in range(n):
        result += current_eve_number
        current_eve_number += 2
            
    return result

print(sum_of_even_numbers(4))
print(sum_of_even_numbers(10))