# Longest Common Prefix
# Solved
# Easy

# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res="" # for storing the string
        for i in range(len(strs[0])): #first take the first element and loop until its last index
            for s in strs:  # take each strings from strs
                if len(s)==i or s[i]!=strs[0][i]: #  compare if the lenghth of the string reached the end index of the first elemet 
                    return res   #or is first string chareacter doesn't match with other string characters then return res
            res+=strs[0][i]  # irresoectice of condtion add the character of string to res
        return res
    
    # Time Complexity is O(n) and space complexity is O(1)

res= Solution.longestCommonPrefix(any,["ad","adba","adb"])
print(res)