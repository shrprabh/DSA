# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

# Example 1:

# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
# Example 2:

# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
# Example 3:

# Input: s = "1111"
# Output: 3
 

# Constraints:

# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.

from collections import defaultdict


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s[:1])
        print(s[1:])
        maxVal=0
        for i in range(1,len(s)): # here the trick is that the string has to split into two parts so we are considering length <len(s)
            score=0
            for num in s[:i]:
                if(num=='0'):
                    score+=1
            for num in s[i:]:
                if(num=='1'):
                    score+=1
            maxVal=max(score,maxVal)
        return maxVal
res=Solution.maxScore(any, "00")
print(res)


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        one=0
        for i in range(1,len(s)): #looping thoughout the string from index 1
            if(s[i]=="1"):
                one+=1
        if s[0]=="1":
            zero=0
            res=one
        if s[0]=="0":
            zero=1
            res=one+1
        for j in range(1,len(s)-1):
            if s[j]=="0":
                zero+=1
            if s[j]=='1':
                one-=1
        res=max(res,zero+one)
        return res
    
# the above solution is most optimized because ir take O(n) time complexity
# the trick is initialy we are calulating the ones and then the first value then we are computinh

res=Solution.maxScore(any, "011101")
print(res)

res=Solution.maxScore(any, "00")
print(res)