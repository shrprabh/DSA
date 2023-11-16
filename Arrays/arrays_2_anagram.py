# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_count_s_dict={};
        letter_count_t_dict={};
        for letter in s:
            if letter=="":
                continue;
            if letter in letter_count_s_dict:
                letter_count_s_dict[letter]+=1
            else:
                letter_count_s_dict[letter]=1
        for letter in t:
            if letter=="":
                continue;
            if letter in letter_count_t_dict:
                letter_count_t_dict[letter]+=1
            else:
                letter_count_t_dict[letter]=1
        if(letter_count_s_dict==letter_count_t_dict):
            return True
        else:
            return False
        
result=Solution.isAnagram(any,"anagram","naagram")
print(result)
result2=Solution.isAnagram(any,"anqagramm","naagram")
print(result2)

#Time Complexity
#M+N since the loop is running one time for set s and then t

print("Time Complexity n")
class Solution2(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
result3=Solution2.isAnagram(any,"anagram","naagram")
print(result3)
result4=Solution2.isAnagram(any,"anqagramm","naagram")
print(result4)
