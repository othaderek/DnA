# Return the number of pairs in a given array who's sum is k

def arrayPairSum(arr,k):
    # Base case
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()

    # Loop through array and add nums to seen set
    for num in arr:

        target = k-num

        # If target isn't in the seen set add it
        if target not in seen:
            seen.add(num)
        # If target is in seen set, add it and current num to ouput as tuple
        else:
            output.add((min(num,target), max(num,target)))
    # return length of output set
    return len(output)


print(arrayPairSum([1,2,3,4,5,], 4))