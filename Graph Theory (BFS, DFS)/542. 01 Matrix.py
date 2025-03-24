# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
 

# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = collections.deque()
        seen = set()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    # 0 here means 0 steps
                    queue.append((r, c, 0))
                    seen.add((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if (next_row, next_col) not in seen and 0 <= next_row < m and 0 <= next_col < n:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    mat[next_row][next_col] = steps + 1

        return mat
        