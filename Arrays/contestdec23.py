class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort( )
        print(nums)
        arr=[0]*len(nums)
        for i in range(len(nums)):
            if i%2==0:
                arr[i]=nums[i+1]
            else:
                arr[i]=nums[i-1]
        return arr
res=Solution.numberGame(any,[5,4,2,3])
print(res)