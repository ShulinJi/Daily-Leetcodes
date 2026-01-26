
# SECOND ATTEMPT
# TIME complexity: O(M * N) which we have toi traverse all the islands, cases: all 1s in the grid.
# Space complexity: O(M * N) in the worst case, the grid is filled with lands, we will have M * N recursive calls on the call stack.
# Not O(1) space because each recursive call takes space on the call stack, O(1) for each call, but we have maximum M * N calls.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(row, col):
            # out of bound index
            if row > m - 1 or col > n - 1 or row < 0 or col < 0:
                return 
            # if it's 0, then return, reach the bound
            if grid[row][col] == "0":
                return 
            
            # turn the current grid to 0 to avoid turning back to form infinite loop
            grid[row][col] = "0"
            # find all four directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return 
        
        # traverse through the matrix, as long as we see a 1, we trigger a dfs starting from that row/col
        # and the dfs will turn all the connected 1's to 0
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1
        return ans
        



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS: set each visitied 1 grid to 0 to track all the one's we visited
        def dfs(grid, row, col):
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0'):
                return 

            grid[row][col] = '0'

            dfs(grid, row - 1, col)
            dfs(grid, row + 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
        
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(grid, row, col)
                    count += 1

        return count
        # Complexity O(V + E) V: nodes, E: Edges 
        # Space complexity O(V + E)
        # General DFS algorithms implementation psudo-code

        # 1. Choose a starting node
        # 2. Check if it is a legit node (limitations), if not, simply return (Dead End)

        # 3. Else we push all adjacent nodes into a stack
        # 4. Pop a node from the stack to visit next
        # 5. Repeat until the stack is empty

        # DFS(G, u)
        #     u.visited = true
        #     for each v ∈ G.Adj[u]
        #         if v.visited == false
        #             DFS(G,v)
            
        # init() {
        #     For each u ∈ G
        #         u.visited = false
        #      For each u ∈ G
        #        DFS(G, u)
        # }



# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
