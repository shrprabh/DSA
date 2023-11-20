class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        minLen=min(len(s1),len(s2),len(s3))
        operations=0
        totalLen=len(s1)+len(s2)+len(s3)
        maxLen=max(len(s1),len(s2),len(s3))
        for i in range(0,minLen):
            print(s1[i])
            if(s1[i]!=s2[i] or s2[i]!=s3[i]):
                if(i==0):
                    return -1
                else:
                    break
            elif s1[i]==s2[i] and s2[i]==s3[i] and minLen==maxLen and i==minLen:
                return 0
            elif  (s1[i]!=s2[i] or s2[i]!=s3[i])  and minLen==maxLen:
                return 3
            elif s1[i]==s2[i] and s2[i]==s3[i]:
                operations+=1
        res=totalLen-(operations*3)
        return res
res=Solution.findMinimumOperations(any,"bcbb","bccbabb","bcabb")
print(res)