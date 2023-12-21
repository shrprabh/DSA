# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

 

# Example 1:

# ​
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.
# Example 2:

# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3
 

# Constraints:

# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        nums=[]
        for row in range(len(points)):
            nums.append(points[row][0])
        nums.sort()
        maxVal=0
        for i in range(len(nums)-1):
            maxVal=max(maxVal,(nums[i+1]-nums[i]))
        return maxVal
    
# here we are required to find the largest width between two points and there should not be any point in middle 
# so we will be considering the only x points and ingorning y and when we plot we have to calculate widest vertical area between two points
# so we will be sorting this to make it easier and calulate the distances between all the consecutive points to find the max point
res=Solution.maxWidthOfVerticalArea(any,[[8,7],[9,9],[7,4],[9,7]])
print(res)
