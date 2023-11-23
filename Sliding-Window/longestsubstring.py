# 3. Longest Substring Without Repeating Characters
# Solved
# Medium


# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet= set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res


res=Solution.lengthOfLongestSubstring(any,"abcabcb")
print(res)

res2=Solution.lengthOfLongestSubstring(any,"pwwkew")
print(res2)


# The set charSet is used to keep track of unique characters in the current substring.
# The two pointers l and r are used to define a window that represents the current substring.
# The while loop ensures that the current substring has no repeating characters, and it dynamically adjusts the window by moving the left pointer (l) to the right.
# The maximum length of the substring without repeating characters is continuously updated in the res variable.