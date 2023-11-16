class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]*len(nums) #[1,1,1,1]
        prefix=1
        for i in range(len(nums)): #prefix putting array in a row
            res[i]=prefix     # 1,1,2,6 -->
            prefix*=nums[i]#[1,1,2,6] -->
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=postfix      #   1*24 1*12 2*4 6*1 <--
            postfix*=nums[j]  #[24,12,8,6]<--
        return res
    
result=Solution.productExceptSelf(any,[1,2,3,4])
print(result)