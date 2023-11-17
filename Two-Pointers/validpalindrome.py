# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution(object):
    def isValidPalindrome(self,s):
        # we will be solving this using pointers so that we need not to use an extra memory for storing a string for comparision
        # time complexity will be O(n)
        # space complexity will be O(1)
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.isAlphaNumeric(s[l]): #check if the left is less then right and if the left's value is not a alphanumeric character
                l+=1 # if it is not a alphanumeric incremnet left 
            while r>l  and not self.isAlphaNumeric(s[r]): #check if the right is greater then left and if the rights's value is not a alphanumeric character
                r-=1 # if it is not a alphanumeric decrement right 

            if(s[l].lower() != s[r].lower()):
                return False
            l,r=l+1,r-1

        return True

    def isAlphaNumeric(self,c):
        # we will be checking is the number is alpha numeric using our own function using ascii value
        # we can get ascii value using the  ord function of python
        return (ord('A')<=ord(c)<=ord('Z') or # its ascii starts from 65 to and ends at 97
                ord('a')<=ord(c)<=ord('z') or # its ascii starts from 97 to ends at 122
                ord('0')<=ord(c)<=ord('9')  ) # its ascii starts from 48 and ends at 57


# Creating an instance of the Solution class
sol = Solution()

# Now using the instance to call isValidPalindrome
result = sol.isValidPalindrome("A man, a plan, a canal: Panama")
print(result)

result2 = sol.isValidPalindrome("al_l<m:-a")
print(result2)



# Will inbuilt functions

class Solution2(object):
    def isValidPalindrome2(self,s):
        newStr=''
        for c in s:
            if c.isalnum(): #isalnum is used to check whether number of alphanumeric or not
                newStr+=c.lower();
        return newStr==newStr[::-1]
sol1 = Solution2()

# Now using the instance to call isValidPalindrome
result3 = sol1.isValidPalindrome2("A man, a plan, a canal: Panama")
print(result3)
result4 = sol1.isValidPalindrome2("al_l<m:-a")
print(result4)



# In JS
# var isPalindrome = function(s) {
#   s = s.toLowerCase().replace(/[^a-z0-9]/g, '');
#   let left = 0;
#   let right = s.length - 1;

#   while (left < right) {
#     if (s[left] !== s[right]) {
#       return false;
#     }
#     left++;
#     right--;
#   }

#   return true;
# };