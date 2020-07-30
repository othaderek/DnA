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

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))
        
    return len(output)


print(arrayPairSum([1,2,3,4,5,], 4))