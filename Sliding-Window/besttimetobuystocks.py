# 121. Best Time to Buy and Sell Stock
# Easy

# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         maxProfit=0
#         lengthPrices=len(prices)
#         for a in range(0,lengthPrices-1):
#             b=a+1
#             while b<lengthPrices:
#                 if prices[b]>prices[a]:
#                     profit=prices[b]-prices[a]
#                     maxProfit=max(profit,maxProfit)
#                 b+=1
#         return maxProfit
# prices = [7,1,5,3,6,4]



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit=0
        lengthPrices=len(prices)
        if(lengthPrices==1):
            return 0         #this block is not required but to handle
        else:
            l,r=0,1  # initializing the left pointer  to 0 and right to 1
            while r<=lengthPrices-1:
                if prices[l]<prices[r]:      # we will be buying when stock price is low so checking if prices are less then right
                    profit=prices[r]-prices[l] # to calculate profit
                    maxProfit=max(profit,maxProfit)
                    r+=1 # checking for next profit for same left pointer
                else:
                    l,r=r,r+1 # if left is > then right then we need to but at right so changing the pointer valie left to right valie and moving right to its next location
        return maxProfit
prices = [7,1,5,3,6,4]
res=Solution.maxProfit(any,prices)
print(res)


#The time complexit will be O(n) and space complexity will be O(1)

#The below solution is also same but here we are incrementing right pointer after if else irrespevtive of condition
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit=0
        lengthPrices=len(prices)
        l,r=0,1
        while r<=lengthPrices-1:
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxProfit=max(profit,maxProfit)
            else:
               l=r
            r+=1
        return maxProfit