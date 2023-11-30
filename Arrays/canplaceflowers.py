# 605. Can Place Flowers
# Easy

# Topics
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # to solve this easily we can add a 0 at first and last of flowerbed
        f=[0]+flowerbed+[0]
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i]=1
                n-=1
        return n<=0
# the time complexity of algorithm is O(n) and space complexity is O(1)

res=Solution.canPlaceFlowers(any,[0,0,0,0,0,0,0,0,0],5)
res1=Solution.canPlaceFlowers(any,[0,0,1],1)
res2=Solution.canPlaceFlowers(any,[1,0,1],1)
print(res)
print(res1)
print(res2)
