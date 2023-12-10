# 100155. Double Modular Exponentiation
# User Accepted: 3153
# User Tried: 4479
# Total Accepted: 3182
# Total Submissions: 6106
# Difficulty: Medium
# You are given a 0-indexed 2D array variables where variables[i] = [ai, bi, ci, mi], and an integer target.

# An index i is good if the following formula holds:

# 0 <= i < variables.length
# ((aibi % 10)ci) % mi == target
# Return an array consisting of good indices in any order.

class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        #((aibi % 10)ci) % mi == target
        res=[]
        for i in range(0,len(variables)):
            check=(((variables[i][0]**variables[i][1])%10)**variables[i][2])%variables[i][3]
            print(check)
            if(check==target):
                res.append(i)
        return res
    
# res=Solution.getGoodIndices(any,[[2,3,3,10],[3,3,3,1],[6,1,1,4]],2)
# print(res)

# res=Solution.getGoodIndices(any,[[39,3,1000,1000]],17)
# print(res)


res=Solution.getGoodIndices(any,[[2,2,3,2],[1,3,3,2],[3,2,2,3],[3,1,2,3],[1,2,3,1],[2,2,2,2],[2,1,3,1],[3,2,2,2],[2,1,3,1],[3,3,1,3]],0)
print(res)