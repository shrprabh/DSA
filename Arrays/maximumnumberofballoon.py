

# Code


# Testcase
# Testcase

# Test Result

# 1189. Maximum Number of Balloons
# Solved
# Easy

# Topics
# Companies

# Hint
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter=Counter(text)
        balloon=Counter("balloon")
        res=len(text)
        for c in balloon:
            res=min(res,counter[c]//balloon[c])
        return res
res=Solution.maxNumberOfBalloons(any,"Asaswasballasasoon")
print(res)


class Solution(object):
    def maxNumberOfBalloons(self, text):
        l=text.count('l')//2 
        o=text.count('o')//2 
        b=text.count('b') 
        n=text.count('n') 
        a=text.count('a') 
        return min(l,o,b,n,a)