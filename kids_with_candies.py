class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
                
# get greatest value in array
# loop through array
# check if candies[i] + extraCandies >= greatest
# add true to array, else add false
