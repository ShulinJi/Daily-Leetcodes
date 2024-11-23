# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.
# Example 2:

# Input: board = [[-1,-1],[-1,3]]
# Output: 1


from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # We need n^2 + 1 cells because we have in total of n x n grid and we start at 1 instead of 0
        cells = [None] * (n * n + 1)
        columns = list(range(0, n))
        label = 1
        for row in range(n - 1, -1, -1):
            for col in columns:
                # for cells, the index represent its value: 1, 2, 3, 4, 5, 6, 7...
                # and cells[index] represents its location at the board
                cells[label] = (row, col)
                label += 1
            columns.reverse()

        distance = [-1] * (n**2 + 1)
        distance[1] = 0
        # basically we store the value of the cells and use it to find its locations
        # to check if we have traversed through all the cells
        queue = deque([1])
        while queue:
            curr = queue.popleft()
            for next in range(curr + 1, min(curr + 6, n * n) + 1):
                row, col = cells[next]
                destination = (board[row][col] if board[col][col] != -1 else next)
                if distance[destination] == -1:
                    distance[destination] = distance[curr] + 1
                    queue.append(destination)

        return distance[n * n]
