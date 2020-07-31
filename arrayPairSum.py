# Return the number of pairs in a given array who's sum is k
# Array must be sorted in order to work

def arrayPairSum(arr,k):
    # Base case
    if len(arr)<2:
        return
    # Sets for tracking
    seen = set()
    output = set()

    # Loop through array and add nums to seen set
    for num in arr:
        # reate target num by subtracting k from num
        target = num-k

        # If target isn't in the seen set add num
        if target not in seen:
            seen.add(num)
        # If target is in seen set, add it and current num to ouput as tuple
        else:
            output.add((min(target, num), max(target, num)))
    # return length of output set
    print(output)
    return len(output)


print(arrayPairSum([-1,1,2,3,4,5], 4))