# 347. Top K Frequent Elements
# Medium

# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq=[[] for i in range(len(nums)+1)]
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)  # count.get(n,0) this one search for the number n in count dictionary if its not found it return 0 else it return the respective number
        for n,c in count.items():
            freq[c].append(n) # this will append the n value to the respective index(count) (to store the max repeated value) 
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

res=Solution.topKFrequent(any,[1,1,1,2,2,3],2)
print(res)