# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# By Hasmap and letters

from collections import defaultdict


class Solution:
    def groupanagrams(self,strs):
        res=defaultdict(list)
        for s in strs:
            count=[0]*26 # to keep track of count of characters in each s
            for c in s:
                count[ord(c)-ord("a")]+=1 # subracting the aschi value to store each letter count of a sting in  iterating it based on repetition
            res[tuple(count)].append(s) # converting it to tuple because it is immutable we can't store list as a key. and then appending string
        return res.values();


result=Solution.groupanagrams(any,["ate","eat","mat","tam","rob"])
print(result)

#Time Complexity
#M*N+26 (M*N)
#O(m*n)

# solution 2 using sorting and hashing technique
class Sloution2:
    def groupAnagrams(self,strs):
        res=defaultdict(list)
        for s in strs:
            a=sorted(s)      #Sort  each string this will convert it into list
            print(a)
            sorted_string="".join(a)    #those are joined
            res[sorted_string].append(s) # stored as a key and value will be original string
        return res.values()                #returns only keys


result2=Sloution2.groupAnagrams(any,["sat","tas","man","nam","aman","ram"])
result3=Sloution2.groupAnagrams(any,[""])


print(result2)
print(result3)

#Time Complexity is O(n)
#and space complexity is O(n) because we will be storing the sorted string