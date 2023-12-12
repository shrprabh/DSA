

# Code


# Testcase
# Testcase

# Test Result

# 20. Valid Parentheses
# Attempted
# Easy

# Topics
# Companies

# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        keys=["(","{","["]
        values=[")","}","]"]
        mp=dict(zip(keys,values))
        lst=[]
        for i in s:
            if i in keys:
                lst.append(i)
            else:
                if(len(lst)>0):
                    top=lst[-1]  #this will give the last index or top element or we can use lst[len(s)-1]
                    if mp[top]==i: # when the paranthesis that is keys which are pushed are matched with the one in loop else block it will be popper from the list
                        lst.pop()
                    else:
                        return False
                else: return False
        if len(lst)==0:
            return True
        else:
            return False

res=Solution.isValid(any,"(){}()");
print(res)
res=Solution.isValid(any,"(){}}()");
print(res)