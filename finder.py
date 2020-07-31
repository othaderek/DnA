# Find return the element in arr2 not in arr1
# my solution
def finder(arr1, arr2):
    frequencyCounter = {}

    for num in arr1:
        if num not in frequencyCounter:
            frequencyCounter[num] = 1
        else:
            frequencyCounter += 1

    for num in arr2:
        if num in frequencyCounter:
            frequencyCounter[num] -= 1

    return [k for k, v in frequencyCounter.items() if v == 1][0]
    


print(finder([1,2,3,4], [3,4,2]))
print(finder([1,2,3,4], [3,2,1]))

