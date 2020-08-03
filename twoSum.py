def twoNumberSum(array, targetSum):
    table = {x:True for x in array}
    
    for num in array:
        targetNum = targetSum - num
        if table.get(targetNum) == True and num != targetNum:
                return [num, targetNum]


print(twoNumberSum([2,-1,6,3,4,1], 4))
