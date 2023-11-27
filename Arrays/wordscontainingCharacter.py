class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        listContainingWords=[]
        for i in range(len(words)):
            for char in words[i]:
                if x==char:
                    listContainingWords.append(i)
                    break
        return listContainingWords
            

res=Solution.findWordsContaining(any,["abc","bcd","aaaa","cbc"],"z")
print(res)