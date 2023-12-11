

# Code


# Testcase
# Testcase

# Test Result

# 28. Find the Index of the First Occurrence in a String
# Easy

# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        needleLen=len(needle)
        haystackLen=len(haystack)
        for i in range(haystackLen-needleLen+1):
            if(haystack[i:i+needleLen]==needle):
                return i
        return -1

res=Solution.strStr(any,"leetcode","leeto")
print(res)
res=Solution.strStr(any,"leetcode","lee")
print(res)

# with inbuild function
class Solution(object):
    def strStr(self, haystack, needle):
      return haystack.find(needle)
    
res2=Solution.strStr(any,"leetcodeocode","code")
print(res2)
res3=Solution.strStr(any,"leetcode","ee")
print(res3)