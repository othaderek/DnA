# Return the largest continuous sum for a given array

def largestSum(arr):
    # If array empty return zero
    if len(arr)==0:
        return 0
    # Set both variables to first value in array
    max_sum = current_sum = arr[0]

    # Loop from first index using slice
    for num in arr[1:]:
        # Set current sum to the max of current sum + num or num
        current_sum = max(current_sum+num, num)
        # set max sum to be the max between current sum or max sum
        max_sum = max(current_sum, max_sum)

    # return max sum
    return max_sum
print(largestSum([2,5,4,1,-1,0,10]))

