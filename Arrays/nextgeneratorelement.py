# 496. Next Greater Element I
# Easy

# Topics
# Companies
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # storing in a hashmap for easy access 
        nums1Idx={n:i for i,n in enumerate(nums1)}
        # if the loop wont reach that iterate value will be by default -1
        res=[-1]*len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            else:
                for j in range(i+1,len(nums2)):
                    if(nums2[j]>nums2[i]):
                        idx=nums1Idx[nums2[i]]
                        res[idx]=nums2[j]
                        break
        return res
res=Solution.nextGreaterElement(any,[2,4],[1,2,3,4])
res2=Solution.nextGreaterElement(any,[2,4,5,6,4,10],[1,2,3,4,7,6,8,2,4,10])
print(res)
print(res2)
# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         res=[]
#         for i in range(len(nums1)):

#             for j in range(len(nums2)):
#                 if(nums1[i]==nums2[j]):
#                     if(j+1<len(nums2) and nums2[j+1]>nums1[i]):
#                         res.append(nums2[j+1])
#                         break
#                     else:
#                         res.append(-1)
#                         break
#         return res

