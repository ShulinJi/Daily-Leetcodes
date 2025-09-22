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

# O(n ^ 2) time complexity, O(n ^ 2) space complexity
# 2 phases solution: first phase to precompute the area of each island and mark them with unique island ids, store in a map
# second phase to iterate through each 0 cell, check its 4-directional neighbours, and calculate the area if we flip this 0 to 1
# and see if it connects to multiple islands, use a set to avoid double counting
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_area = 1
        area_map = dict()
        seen = set()
        # island_id starts from 2 because grid only contains 0 and 1
        def dfs(r, c, island_id):
            if (r < 0 or r > n - 1 or c < 0 or c > n - 1) or (r, c) in seen:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = island_id
            seen.add((r, c))

            return 1 + dfs(r - 1, c, island_id) + dfs(r + 1, c, island_id) + dfs(r, c - 1, island_id) + dfs(r, c + 1, island_id)

        # iterate through the grid to find islands and mark them with unique ids
        island_id = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c, island_id)
                    area_map[island_id] = area
                    max_area = max(max_area, area)
                    island_id += 1
        
        # phase 2: iterate through each 0 cell, check its 4-directional neighbours
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    curr_area = 1
                    neighbours = set()
                    if row + 1 < n and grid[row + 1][col] > 1:
                        island_id = grid[row + 1][col]
                        neighbours.add(island_id)
                    if col + 1 < n and grid[row][col + 1] > 1:
                        island_id = grid[row][col + 1]
                        neighbours.add(island_id)
                    if col - 1 >= 0 and grid[row][col - 1] > 1:
                        island_id = grid[row][col - 1]
                        neighbours.add(island_id)
                    if row - 1 >= 0 and grid[row - 1][col] > 1:
                        island_id = grid[row - 1][col]
                        neighbours.add(island_id)
                    # add up the area of all unique neighbouring islands
                    for x in neighbours:
                        curr_area += area_map[x]
                    max_area = max(max_area, curr_area)
        return max_area

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