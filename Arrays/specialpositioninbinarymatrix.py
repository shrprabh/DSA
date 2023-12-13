# 1582. Special Positions in a Binary Matrix
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:


# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:


# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rowLen=len(mat)
        colLen=len(mat[0])
        res=0
        ans=[]
        for row in range(rowLen):
            for col in range(colLen):
                if(mat[row][col]==1):
                    ans.append((row,col))
        
        count=0
        for i,j in ans:
            done=True
            for row in range(rowLen):
                if(row!=i):
                    if(mat[row][j]==1):
                        done=False
                        break
            if(not done):
                continue
            for col in range(colLen):
                if(col!=j):
                    if(mat[i][col]==1):
                        done=False
                        break
            if done:
                count+=1 


        return count
   

res=Solution.numSpecial(any,[[1,0,0],[0,0,1],[1,0,0]])
print(res)