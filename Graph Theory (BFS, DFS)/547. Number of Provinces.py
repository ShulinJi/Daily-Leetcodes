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

# SECOND ATTEMPT
# DFS Approach, and O(n ^ 2) b/c n nodes and each node have n nodes to reach in isConnected[i], so O(n^2), and O(n) space
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # record visited island to avoid cycles
        visited = [False] * len(isConnected)
        island = 0

        # DFS to keep searching and mark visited on the way, until we couldn't find any more options, we form one province
        def dfs(i):
            visited[i] = True

            for j in range(len(isConnected[i])):
                # not visited and can connect to the next node (isConnected[i][j] == 1)
                if not visited[j] and isConnected[i][j] == 1:
                    dfs(j)

        # we loop through each island to expand from that island and mark all the reachable as visited to form a province
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                island += 1

        return island


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
