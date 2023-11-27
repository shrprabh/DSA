class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum=0
        m=0
        if len(prices)>=1:
            sum=prices[0]
            m=1
        for i in range(1,len(prices)):
            while m<len(prices)-1:
                if prices[m]<=prices[m+i+1]:
                    sum+=prices[m+1]
                    m=i+1
                else:
                    sum+=prices[m+i+1]
                    m=i+2
        return sum
    
res=Solution.minimumCoins(any,[26,18,6,12,49,7,45,45])
print(res)






