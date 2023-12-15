# 1436. Destination City
# Solved
# Easy

# Topics
# Companies

# Hint
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        source=[x[0] for x in paths]
        destination=[x[1] for x in paths]
        for i in destination:
            if i not in source:
                return i
# In thid problem the time complexity is O(n) and here we will be storing all the source in a list and destination in other list
# the catch is the destination wont be having connecting source we can use that logic to code
# we can use dict also to reduce time complexity
res=Solution.destCity(any,[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(res)