# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 3
        N = n * n

        # use dictionaries to keep track of the counts of 9 (1-9) digits in each row, column, and box
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        # initialize the dictionaries with the given board, fill in the counts of the digits
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    rows[i][d] += 1
                    cols[j][d] += 1
                    box_index = (i // 3) * 3 + j // 3
                    boxes[box_index][d] += 1
        
        def backtracking(row, col):
            # if we reached the end of the board, we found a solution
            if row == N:
                return True
            
            # move to the next cell from left to right, top to bottom
            if col == N - 1:
                next_row = row + 1
                next_col = 0
            else:
                next_col = col + 1
                next_row = row

            # if the cell is already filled, move to the next cell, skip this cell
            if board[row][col] != ".":
                return backtracking(next_row, next_col)
            
            # try each digit from 1 to 9
            current_box = box_index = (row // 3) * 3 + col // 3
            for d in range(1, 10):
                # check if the digit is not already in the current row, column, and box
                if not (d in rows[row] or d in cols[col] or d in boxes[current_box]):
                    # place the digit in the cell
                    board[row][col] = str(d)
                    rows[row][d] += 1
                    cols[col][d] += 1
                    boxes[current_box][d] += 1

                    # move to the next cell and continue the backtracking
                    if backtracking(next_row, next_col):
                        return True
                    
                    # we only reach here if placing d doesn't lead to a solution, returned a false from backtracking
                    # if placing d doesn't lead to a solution, remove it and try the next digit
                    board[row][col] = "."
                    rows[row][d] -= 1
                    cols[col][d] -= 1
                    boxes[current_box][d] -= 1

                    # clean up the dictionaries to remove the count of 0 to save space
                    # delete ecause when we check if d in rows[row], if count is 0, it still returns True, which is incorrect
                    if rows[row][d] == 0: del rows[row][d]
                    if cols[col][d] == 0: del cols[col][d]
                    if boxes[current_box][d] == 0: del boxes[current_box][d]

            return False
        
        backtracking(0, 0)