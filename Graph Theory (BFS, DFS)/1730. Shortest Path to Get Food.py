# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

# You are given an m x n character matrix, grid, of these different types of cells:

# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

 

# Example 1:


# Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
# Example 2:


# Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
# Example 3:


# Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
# Example 4:

# Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["O","O","O","O","O","O","O","O"]]
# Output: 5


class Solution:
    def getFood(self, grid: list[list[str]]) -> int:
        # Possible moves: right, left, up, down
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])

        # Find starting position marked as '*'
        start = next(
            (i, j)
            for i in range(rows)
            for j in range(cols)
            if grid[i][j] == "*"
        )

        # BFS queue for level-by-level traversal
        queue = deque([start])
        steps = 1

        # BFS traversal
        while queue:
            # Process all cells at current level
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # Try all four directions
                for dx, dy in dirs:
                    new_row, new_col = row + dx, col + dy

                    if self._is_valid(grid, new_row, new_col):
                        # Found food
                        if grid[new_row][new_col] == "#":
                            return steps

                        # Mark as visited and add to queue
                        grid[new_row][new_col] = "X"
                        queue.append((new_row, new_col))
            steps += 1

        # No path found to food
        return -1

    # Check if position is within bounds and not blocked
    def _is_valid(self, grid: list[list[str]], row: int, col: int) -> bool:
        return (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and grid[row][col] != "X"
        )