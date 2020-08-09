def binarySearch(array, target):
    # Create a binary search helper function
	return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    # If left is greater than right, return -1. This means there was no match
	if left > right:
		return -1
    # Get the middle index by adding the current left and right pointers and dividing by 2
	middle = (left+right) // 2
    # set the value in the current middle index to a variable
	potentialMatch = array[middle]
    # if the target number and its potential match are equal, we want to return middle, 
    # which is the index of the potential match
    # if the target is less than the potential match, we recursively call our helper function
    # and reset the right pointer to be the middle minus 1
    # else call the helper fucntion recursively and set the left pointer to equal the middle
    # plus one
	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		return binarySearchHelper(array, target, left, middle - 1)
	else:
		return binarySearchHelper(array, target, middle + 1, right)

print(binarySearch([1,2,3,4,5,6,7], 7))
