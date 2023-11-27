class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        realTemp=[row[:] for row in mat]
        def leftShift(array,k):
            a=list(reversed(array))
            firstshift=reversed(a[:len(a)-k])
            secondshift=reversed(a[len(a)-k:])
            return list(firstshift)+list(secondshift)
        
        def rightShift(array,k):
            a=list(reversed(array))
            firstshift=reversed(a[:k])
            secondshift=reversed(a[k:])
            return list(firstshift)+list(secondshift)
        
        for i in range(len(realTemp)):
            if(i%2==0):
                realTemp[i]=leftShift(realTemp[i],k % len(mat[0]))
            else:
                realTemp[i]=rightShift(realTemp[i],k % len(mat[0]))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] != realTemp[i][j]):
                    return False
        return True

        
        
        
mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]];
k = 2;
res=Solution.areSimilar(any,mat,k)
print(res)