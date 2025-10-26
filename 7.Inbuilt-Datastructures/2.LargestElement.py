def find_largest(numbers):
    # Your code goes here
    numbers.sort()
    n = len(numbers)
    largest = numbers[n-1]
    return largest
numbers = [3, 8, 2, 10, 5]
largest = find_largest(numbers)
print(largest)