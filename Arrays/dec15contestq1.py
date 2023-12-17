# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
from collections import defaultdict


class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
        n=len(grid)
        res=[]
        missVal=0
        listRange=[x for x in range(1,(n**2)+1)]
        allKeys=[]
        print(listRange)
        dictgrid=defaultdict(int);
        for row in range(n):
            for col in range(n):
                dictgrid[grid[row][col]]+=1
        for key in dictgrid:
            allKeys.append(key)
            if(dictgrid[key]==2):
                    res.append(key)
        for i in listRange:
             if i not in allKeys:
                  missVal=i
        res.append(missVal)
        return res
       

res=Solution.findMissingAndRepeatedValues(any,[[9,1,7],[8,9,2],[3,4,6]])
print(res)
