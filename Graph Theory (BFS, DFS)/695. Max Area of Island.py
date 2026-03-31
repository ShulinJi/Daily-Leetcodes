# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.


# SECOND ATTEMPT
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col):
            # if current row and col is out of bound or current grid is 0, we return 0
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if grid[row][col] == 0:
                return 0

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            # total = 1 because we are currently on a land cell, so we count it as 1
            # and we mark it as 0 to avoid cycle
            total = 1
            grid[row][col] = 0
            for r, c in directions:
                # so that no cycle
                total += dfs(r + row, c + col)

            return total
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    ans = max(ans, dfs(row, col))
        
        return ans


# O(m * n) time complexity
# O(m * n) space complexity
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        # set to store visited cells
        seen = set()

        def dfs(r, c):
            # base case if out of bound or already visited
            if (r < 0 or r >= m or c < 0 or c >= n) or (r, c) in seen:
                return 0
            # base case if it is not 1
            if grid[r][c] == 0:
                return 0
            # mark as visited
            seen.add((r, c))

            # explore all 4 directions, up, down, left, right
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                # if it is 1 and not visited
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area
