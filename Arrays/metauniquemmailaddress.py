# Unique Email Addresses
# Easy

# Topics
# Companies
# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emai

 

# Example 1:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
# Example 2:

# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique=set()
        for e in emails:
            i,local=0,""
            # to store the local name by considering until @ or if + is there eleminating from there
            while e[i] not in ["@","+"]:
                if e[i]!=".":
                    local+=e[i]
                i+=1
            # this below while loop will have the i value which is there after above while loops this will help us to get domain name
            while e[i] !="@":
                i+=1
            # storing domain name
            domain=e[i+1:]
            # adding local and domain name as a tuple to a set so that to find the unique emails
            unique.add((local,domain))
        return len(unique)

res=Solution.numUniqueEmails(any,["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(res)

#Using In buit functions
class Solution1(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique=set()
        for e in emails:
            # spliting into list of 2
            local,domain=e.split("@")
            # neglecting all the values after +
            local=local.split('+')[0]
            # removing . by ""
            local=local.replace(".","")
            unique.add((local,domain))
        return len(unique)

res2=Solution1.numUniqueEmails(any,["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(res2)