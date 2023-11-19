#  Container With Most Water
# Solved
# Medium

# Topics
# Companies

# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        maxArea=0
        while l<r:
            if(height[l]<height[r]):
                area=height[l]*(r-l)
                l+=1
            elif(height[l]>height[r]):
                area= height[r]*(r-l)       
                r-=1
            else:
                area= height[r]*(r-l)
                l+=1
            maxArea=max(maxArea,area)    
        return maxArea
    
res=Solution.maxArea(any,[1,8,6,2,5,4,8,3,7])
print(res)

# this is the best solution with linear time complexity we can achieve the same using O(n^2) using two for loops but it is inefficient


# the below logic also works but it takes little  more tine due to usage of min function
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        maxArea=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            if(height[l]<height[r]): 
                l+=1
            else:
                r-=1
            maxArea=max(maxArea,area)    
        return maxArea
res1=Solution1.maxArea(any,[1,8,6,2,5,4,8,3,7])
print(res1)