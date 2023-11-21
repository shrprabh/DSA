# 42. Trapping Rain Water
# Solved
# Hard

# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        l,r=0,len(height)-1
        maxLeft,maxRight=height[l],height[r]
        if not height:
            return 0
        while(l<r):
         
            if(maxLeft<=maxRight):
                l+=1
                maxLeft=max(maxLeft,height[l]) #this will make sure -ve is not added to result 
                res+=maxLeft-height[l] #if we swap above and below line
            else:
                r-=1
                maxRight=max(maxRight,height[r])
                res+=maxRight-height[r]
                
        return res

                

res=Solution.trap(any,[0,1,0,2,1,0,1,3,2,1,2,1])
print(res)
res2=Solution.trap(any,[4,2,0,3,2,5])
print(res2)