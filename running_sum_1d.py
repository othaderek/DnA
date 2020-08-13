class Solution:
    def runningSum(self, nums):
        result = [nums.pop(0)]
        
        while len(nums) != 0:
            result.append(result[-1] + nums.pop(0))

        return result



nums = [1,2,3,4] # => [1,3,6,10]

s1 = Solution()
print(s1.runningSum(nums))
