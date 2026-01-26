# # https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
 

# Follow up:

# 1. Could you solve it in-place? Remember that the board needs to be updated simultaneously: 
# You cannot update some cells first and then use their updated values to update other cells.

# 2. In this question, we represent the board using a 2D array. In principle, the board is infinite, 
# which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). 
# How would you address these problems?

# SECOND Attempt
# O(M*N) time | O(1) space  because we are modifying the board in place (8 * M * N for counting neighbors)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 8 directions
        directions = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):
                living_count = 0
                for dx, dy in directions:
                    new_row = dx + row
                    new_col = dy + col
                    if 0 <= new_row < m and 0 <= new_col < n and abs(board[new_row][new_col]) == 1:
                        living_count += 1
                
                # if we were 0 (dead), and we becomes alive, we don't want interfere with original board, so assign 2
                if board[row][col] == 0 and living_count == 3:
                    board[row][col] = 2
                
                # if we were 1 and die because of overpopulation or under-population
                # we make it to -1, so when we check the others, abs(-1) still counts as alive
                if board[row][col] == 1 and (living_count > 3 or living_count < 2):
                    board[row][col] = -1
                
                # if we were 1 and we are still alive after check, nothing changes, so don't need to write it
        

        for row in range(m):
            for col in range(n):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]
        m = len(board)
        n = len(board[0])
        
        for row in range(m):
            for col in range(n):
                # count how many living cells are nearby
                living_count = 0
                for direction_row, direction_col in directions:
                    updated_row = row + direction_row
                    updated_col = col + direction_col
                    # Use abs here because 2 is converted by 0, we don't count it
                    # And -1 is converted by 1, we still count it, so asb(-1) = 1, still being counted
                    if m > updated_row >= 0 and n > updated_col >= 0 and abs(board[updated_row][updated_col]) == 1:
                        living_count += 1
                print((row, col))
                print(living_count)
                # rule 4 and set it to 2 to avoid interfere with further living counts
                if board[row][col] == 0 and living_count == 3:
                    board[row][col] = 2
                # rule 1 and 3, set it to -1 to avoid futher interference with living counts 0 or 1
                if board[row][col] == 1 and (living_count < 2 or living_count > 3):
                    board[row][col] = -1

        for row in range(m):
            for col in range(n):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


