

# Code


# Testcase
# Testcase

# Test Result

# 724. Find Pivot Index
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)

        leftSum=0
        for i in range(len(nums)):
            rightSum=total-nums[i]-leftSum
            if leftSum==rightSum:
                return i
            else:
                leftSum+=nums[i]
        return -1

res=Solution.pivotIndex(any,[1,2,3,4,5,1])
print(res)