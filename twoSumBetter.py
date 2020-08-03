# O(nlogn)

def twoNumberSumBetter(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1

    while left < right:
        current = array[left] + array[right]
        if current == targetSum:
            return [array[left], array[right]]
        elif current < targetSum:
            left += 1
        elif current > targetSum:
            right -= 1

print(twoNumberSumBetter([2,-1,6,3,4,1], 4))
			