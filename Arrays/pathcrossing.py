# 1496. Path Crossing
# Solved
# Easy

# Topics
# Companies

# Hint
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

# Example 1:


# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
    
        direct={'row':0,'col':0}
        listCheck=[[direct['row'],direct['col']]]
        for i in path:
            if i == 'N':
                direct['row']-=1
                if [direct['row'],direct['col']] not in listCheck:
                    listCheck.append([direct['row'],direct['col']])
                else:
                    return True
            elif i == 'E':
                direct['col']+=1
                if [direct['row'],direct['col']] not in listCheck:
                    listCheck.append([direct['row'],direct['col']])
                else:
                    return True
            elif i == 'S':
                direct['row']+=1
                if [direct['row'],direct['col']] not in listCheck:
                    listCheck.append([direct['row'],direct['col']])
                else:
                    return True
            elif i == 'W':
                direct['col']-=1
                if [direct['row'],direct['col']] not in listCheck:
                    listCheck.append([direct['row'],direct['col']])
                else:
                    return True
        return False

# the time complexity is O(n)
# the main logic here is the initial point is 0,0
# when the person go on north the value of row will get decremented 
# when the person go on east the value of col will be incremented
# and similar to that for south and west 
# on every vist when we have not visited the point we will be appending to the list
# if the path is already there then we will Return True

res=Solution.isPathCrossing(any,"NES")
print(res)

res=res=Solution.isPathCrossing(any,"NESWW")
print(res)