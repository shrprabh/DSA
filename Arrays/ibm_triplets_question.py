# Given a list of numbers and a  target
# find all the triplets  which will divide the sum by target  [a+b+c]%target =0

#example [1,2,3,4,5,7] target=7
#[[1, 2, 4], [2, 5, 7], [3, 4, 7]] output:3

class Solution:
    def triplets(self,lst,target):
        count=0
        numLst=[]
        for i in range(0,len(lst)):
            for j in range(i+1,len(lst)):
                for k in range(j+1,len(lst)):
                    if((lst[i]+lst[j]+lst[k])%target==0):
                        numLst.append([lst[i],lst[j],lst[k]])
                        count+=1
        return numLst,count;

result=Solution.triplets(any,[1,2,3,4,5,7],7)
print(result[0])
print(result[1])