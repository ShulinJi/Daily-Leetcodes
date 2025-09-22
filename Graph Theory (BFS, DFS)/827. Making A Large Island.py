# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

 

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.

# O(n ^ 4) time complexity, which exceeds the time limit
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_area = 0
        seen = set()

        def dfs(r, c):
            if (r < 0 or r > n - 1 or c < 0 or c > n - 1) or (r, c) in seen:
                return 0
            if grid[r][c] == 0:
                return 0
            seen.add((r, c))

            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)


        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    grid[r][c] = 1
                    max_area = max(dfs(r, c), max_area)
                    grid[r][c] = 0
                    seen.clear()
                else:
                    max_area = max(dfs(r, c), max_area)
                    seen.clear()

        return max_area