#         Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        longest=0
        for num in nums:
            # check if this is the first number
            if num-1 not in numset:
                length=0
                while num+length in numset:
                    length+=1
                longest=max(length,longest)
        return longest



result=Solution.longestConsecutive(any,[0,3,7,2,5,0,4,6,0,1])
print(result)



import heapq
class Solution2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(N) -> no sorting, no double loops
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        heapq.heapify(nums) #O(n)
        counter = 1
        maxCount = 1
        past = heapq.heappop(nums)
        while len(nums)>0:
            current = heapq.heappop(nums)
            if current - past == 0:
                pass
            elif current - past == 1:
                counter += 1
                if counter > maxCount:
                    maxCount = counter
            else:
                counter = 1
            past = current

        return maxCount
    

result=Solution2.longestConsecutive(any,[0,3,7,2,5,0,4,6,0,1])
print(result)