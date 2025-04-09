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


# for Backtracking problem
# Problems that require you to produce a candidate solution.
# Problems that require you to generate all possible solutions.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def copy_board(board):
            new_board = []
            for row in board:
                new_board.append("".join(row))
            return new_board
        
        def backtrack(row, cols, diagonal, anti_diagonal, state):
            # if we have exhausted all the rows, we have an answer here and append it
            if row == n:
                ans.append(copy_board(state))
                return
            
            for col in range(n):
                # to avoid two queens on diagonal, every piece on same diagonal row - col will be the same ex. row(4) - col(4) = 0, row(5) - col(5) = 0, on the same diagonal
                # same for anti_diagonal, row + col will add up to a fixed value if on the same anti_diagonal ex. row(4) + col(4) = 8, row(2) + col(6) = 8
                # then we could use a set to detect if there's a duplicate so that we could place a queen 
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                # if there are any pieces on same col, diagonal, anti_diagonal
                if (col in cols 
                    or curr_diagonal in diagonal 
                    or curr_anti_diagonal in anti_diagonal):
                    continue

                # we update the state and save the state
                state[row][col] = "Q"
                cols.add(col)
                diagonal.add(curr_diagonal)
                anti_diagonal.add(curr_anti_diagonal)
                # we continue the search with next row, so that we assure that we don't have duplicate in rows
                backtrack(row + 1, cols, diagonal, anti_diagonal, state)
                
                # after we reached the final row and it returned, we simply return the result and restore the state for other searches
                cols.remove(col)
                diagonal.remove(curr_diagonal)
                anti_diagonal.remove(curr_anti_diagonal)
                state[row][col] = "."
        
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans