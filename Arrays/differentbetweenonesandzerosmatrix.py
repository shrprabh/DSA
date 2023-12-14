# 2482. Difference Between Ones and Zeros in Row and Column
# Solved
# Medium

# Topics
# Companies

# Hint
# You are given a 0-indexed m x n binary matrix grid.

# A 0-indexed m x n difference matrix diff is created with the following procedure:

# Let the number of ones in the ith row be onesRowi.
# Let the number of ones in the jth column be onesColj.
# Let the number of zeros in the ith row be zerosRowi.
# Let the number of zeros in the jth column be zerosColj.
# diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
# Return the difference matrix diff.

class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        listRow=[]
        listCol=[]
        for row in range(len(grid)):
            countZero=0
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    countZero+=1
            listRow.append((countZero,len(grid)-countZero)) #number of zeros and ones in a row
        for col in range(len(grid[0])):
            countZero=0
            for row in range(len(grid)):
                if grid[row][col]==0:
                    countZero+=1
            listCol.append((countZero,len(grid[0])-countZero))
        print(listRow)
        print(listCol)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col]=listRow[row][1]+listCol[col][1]-listRow[row][0]-listCol[col][0]
        return grid

res=Solution.onesMinusZeros(any,[[1,1,1],[1,1,1]])
print(res)



class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        listRow=[]
        listCol=[]
        for row in range(len(grid)):
            countZero=0
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    countZero+=1
            listRow.append((countZero,len(grid)-countZero)) #number of zeros and ones in a row
        for col in range(len(grid[0])):
            countZero=0
            for row in range(len(grid)):
                if grid[row][col]==0:
                    countZero+=1
            listCol.append((countZero,len(grid[0])-countZero))
        print(listRow)
        print(listCol)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col]=listRow[row][1]+listCol[col][1]-listRow[row][0]-listCol[col][0]
        return grid