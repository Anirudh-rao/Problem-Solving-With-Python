def max_consecutive_difference(lst):
    """
    Find Maximum Difference 
    Between Two Consecutive Elements (Brute Force Approach)
    """
    # Your code goes here
    #Edge Case : If List is empty return zero
    if len(lst) < 2:
        return 0
    #Intialize Max Difference as 0
    max_diff = 0
    #Iterate through the list to calculate consecutive Difference
    for i in range(1, len(lst)):
        current_diff =  abs(lst[i] -  lst[i-1])
        if current_diff > max_diff:
            max_diff =  current_diff
    return max_diff