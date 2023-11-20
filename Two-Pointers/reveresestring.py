# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution(object):
    def reverseString(self, s):
        l,r=0,len(s)-1
        a=s
        while l<r:
            tem=s[l]
            s[l]=s[r]
            s[r]=tem
            l+=1
            r-=1
        print(s)
res=Solution.reverseString(any,["h","e","l","l","A"])

# or

class Solution2(object):
    def reverseString(self, s):
        l,r=0,len(s)-1
        a=s
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        print(s)
res1=Solution2.reverseString(any,["h","e","l","l","A"])
