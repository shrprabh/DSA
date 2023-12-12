# 1464. Maximum Product of Two Elements in an Array
# Solved
# Easy

# Topics
# Companies

# Hint
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
# Example 2:

# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
# Example 3:

# Input: nums = [3,7]
# Output: 12

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]-1)*(nums[j]-1)>max:
                    max=(nums[i]-1)*(nums[j]-1)
        return max
res=Solution.maxProduct(any,[1,2,5,6,8,9,12])
#9 and 12 index is max here
print(res)

#using inbuilt function
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted(nums)
        return (nums[-1]-1)*(nums[-2]-1)
res=Solution.maxProduct(any,[1,22,5,6,8,9,12])
#9 and 12 index is max here
print(res)