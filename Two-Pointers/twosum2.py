# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1
        while l<r:
            curSum=numbers[l]+numbers[r]
            if curSum==target:
                return [l+1,r+1]
            elif curSum>target:
                r-=1
            elif(curSum<target):
                l+=1

# Time Complexity is O(n) since it is a sorted array we are using pointers
# Space Complexity is O(n)
            


            



res=Solution.twoSum(any,[2,3,4],6)
print(res)
res=Solution.twoSum(any,[2,3,6,4,8,43],6) # this problem will have exactly one solution
print(res)
# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         array_to_dict = {element: index for index, element in enumerate(numbers)}
#         count=0
#         for num in numbers:
#             count+=1
#             if target-num in set(numbers):
#                 return [count,array_to_dict[target-num]+1]

# this has a time complexity of O(n^2) so it is not efficient