# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

# O(n^2) and O(n)
class Solution:
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)
    
    # we need to count how many times we start a new dfs, meaning how many separate groups(provinces) we have
    # a false in visit means a new province, so we need to start a new dfs
    def findCircleNum(self, isConnected):
        size = len(isConnected)
        numberOfComponents = 0
        visit = [False] * size

        for i in range(size):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents