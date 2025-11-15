def sum_list(numbers):
    # Your code goes here
    sum =  0
    for i in numbers:
        sum += i
    return sum

list = [1, 2, 3, 4, 5]
print(sum_list(list))