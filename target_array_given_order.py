'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Input: nums = [12,22,32,4,0], index = [2,0,1,1,4]
Output: [22,4,32,12,0]

[12]
[22,12]
[22,32,12]
[22,4,32,12]
[22,4,32,12,0]

'''

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        i = 0
        
        for idx in index:
            result.insert(idx, nums[i])
            i += 1
        return result