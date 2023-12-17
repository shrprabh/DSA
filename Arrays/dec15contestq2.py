class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i=0
        j=1
        l=2
        nums.sort()
        print(nums)
        res=[]
        while i < len(nums) - 2:
            j, l = i + 1, i + 2
            count=0
            if abs(nums[i] - nums[j]) <= k and abs(nums[i] - nums[l]) <= k and abs(nums[j] - nums[l]) <= k:
                res.append([nums[i], nums[j], nums[l]])
                i += 3  # Move to the next set of three elements
            else:
                return []
        return res
res=Solution.divideArray(any,[1,3,4,8,7,9,3,5,1],2)
print(res)
