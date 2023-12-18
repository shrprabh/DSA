
# Companies

# Hint
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

# Return the maximum such product difference.


class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=max(nums)
        nums.remove(max1)
        max2=max(nums)
        min1=min(nums)
        nums.remove(min1)
        min2=min(nums)
        return (max1*max2)-(min1*min2)
res=Solution.maxProductDifference(any,[10,2,3,1,3,21,4])
print(res) # this is the most optimized code since unlike the below one where sort function takes nlogn time the max take time complexity of n

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lenNums=len(nums)
        return (nums[lenNums-1]*nums[lenNums-2])-(nums[0]*nums[1])
    
res=Solution.maxProductDifference(any,[10,2,3,1,3,21,4])
print(res)