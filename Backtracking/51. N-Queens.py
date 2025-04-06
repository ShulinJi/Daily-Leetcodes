# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def copy_board(board):
            new_board = []
            for row in board:
                new_board.append("".join(row))
            return new_board
        
        def backtrack(row, cols, diagonal, anti_diagonal, state):
            if row == n:
                ans.append(copy_board(state))
                return
            
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                if (col in cols 
                    or curr_diagonal in diagonal 
                    or curr_anti_diagonal in anti_diagonal):
                    continue

                state[row][col] = "Q"
                cols.add(col)
                diagonal.add(curr_diagonal)
                anti_diagonal.add(curr_anti_diagonal)
                backtrack(row + 1, cols, diagonal, anti_diagonal, state)

                cols.remove(col)
                diagonal.remove(curr_diagonal)
                anti_diagonal.remove(curr_anti_diagonal)
                state[row][col] = "."
        
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans