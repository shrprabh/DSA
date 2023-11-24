# 58. Length of Last Word
# Solved
# Easy

# Topics
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterCount=0
        isBreakTheChainFlag=False
        for i in range(len(s)-1,-1,-1):
            if(s[i]==" "): # or ord(s[i]==32) because ascii value of space is 32
                if(isBreakTheChainFlag):
                    return letterCount
            else:
                letterCount+=1
                isBreakTheChainFlag=True
        return letterCount
    
res=Solution.lengthOfLastWord(any,"   fly me   to   the moon  ")
print(res)


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,lengthCount=len(s)-1,0
        while s[i]==" ":
            lengthCount=0   # this will eliminate all spaces and dont consider length
            i-=1
        while s[i]!=" " and i>=0:
            lengthCount+=1  # this will check all the characters in the last word and when it encounters space it ends
            i-=1
        return lengthCount
  
    
res=Solution.lengthOfLastWord(any,"   fly me   to   the moon  ")
print(res)



# The time complexity of above code is O(n) and space complexity is O(1)

# we can reduce the length and code and optimise it using in build function but its not recommended since we are doing it for learning




class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(map(str,s.split()))
        # This part uses the split() method on the string s. The split() method is used to split a string into 
        # a list of substrings based on a specified delimiter. If no delimiter is provided, 
        # it splits the string at spaces. So, if s is a sentence or a string containing words, s.split() will return a list of words.
        # map(str, ...): The map() function is used to apply the str function to each element 
        # of the iterable (in this case, each word in the list obtained from s.split()). 
        # This ensures that each element in the list is converted to a string.
        # s=list(...): Finally, the result of the map() function is converted back to a
        #list and assigned to the variable s. This means that s is now a list where each element is a string, 
        # and these strings correspond to the words in the original sentence or string.
        print(s)

        return len(s[-1])
    
res1=Solution.lengthOfLastWord(any,"   fly me   to   the moonman  ")
print(res1)







   