# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 

# Constraints:

# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

# O(MxN) O(1) (no extra space since modified the input array)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # if the first grid is obstacle, then we cannot move
        if obstacleGrid[0][0] == 1:
            return 0
        
        # initialize the first step
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
                continue
            obstacleGrid[i][0] = obstacleGrid[i - 1][0]
        
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
                continue
            obstacleGrid[0][i] = obstacleGrid[0][i - 1]
        
        # the current grid is the sum of the left and top grid number
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    # it is an obstacle at the current grid, set it to 0 since it is not valid path
                    # 0 does not contribute to path numbers
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[m - 1][n - 1]
