# Find return the element in arr2 not in arr1
# my solution

import pdb

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
    


# print(finder([1,2,3,4], [3,4,2]))
# print(finder([1,2,3,4], [3,2,1]))


# Use XOR

def finder1(arr1, arr2):
    result=0
    # perform XOR between the numbers in the array
    for num in arr1+arr2:
        result^=num
        # print(result)
        pdb.set_trace()

    return result

print(finder1([1,2,3,4], [3,4,2]))
print(finder1([1,2,3,4], [3,2,1]))