# 118. Pascal's Triangle
# Easy

# Topics
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
    
res=Solution.generate(any,5)
print(res)

# the time complexity of the solution will be O(n^2) and space complexity is constant

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # initialize an array with value 1 considering the constraint
        res=[[1]]
        # iterate through numRows by not considering the first element
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]    # concat [0,last element of previous array res,0] and store in temp to make         calcuation easy
            row=[]
            # create an empty list to calculate next row
            # iterate j from length of previous list +1 
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
    