# 303. Range Sum Query - Immutable
# Easy

# Topics
# Companies
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # initializing prefix for calculating the sum of each number and appending it
        self.prefix=[]

        cur=0
        for i in range(len(nums)):
            cur+=nums[i]
            self.prefix.append(cur)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        rightSum=self.prefix[right]
        leftSum=self.prefix[left-1] if left>0 else 0
        return rightSum-leftSum

# We can solve this easily by O(n^2) time complexity but we can optimize the sumRange function from O(n^2) to O(n using the prefix concept
# and by adding the [0] at first of array if there is no element before it.


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)