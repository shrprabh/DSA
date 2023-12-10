class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows,cols=len(matrix),len(matrix[0])
        newMatrix = [[0 for _ in range(rows)] for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                newMatrix[row][col]=matrix[col][row]
        return newMatrix
res=Solution.transpose(any,[[1,2,3],[4,5,6],[7,8,9]])
print(res)