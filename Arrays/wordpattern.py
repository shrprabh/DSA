# Easy

# Topics
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split(' ')
        charToWord={}
        wordToChar={}
        if len(pattern)!=len(words):
            return False
        for c,w in zip(pattern,words):
            if c in charToWord and charToWord[c]!=w:
                return False
            if w in wordToChar and wordToChar[w]!=c:
                return False
            charToWord[c]=w
            wordToChar[w]=c
        return True
res=Solution.wordPattern(any,"abba","word ana ana word")
print(res)