# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9

# SECOND ATTEMPT
# O(n!) same reason as N-Queens I and O(n) for each set
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtracking(row, cols, diagonal, anti_diagonal):
            # if row reached n, then it means we successfully have a valid answer after traversing all the boards
            if row == n:
                return 1
            
            # conut start at the top of each tree node
            count = 0
            for col in range(n):
                diagonal_value = row - col
                anti_diagonal_value = row + col
                if col in cols or diagonal_value in diagonal or anti_diagonal_value in anti_diagonal:
                    continue
                
                cols.add(col)
                diagonal.add(diagonal_value)
                anti_diagonal.add(anti_diagonal_value)

                # summing up all the viable answers
                count += backtracking(row + 1, cols, diagonal, anti_diagonal)

                anti_diagonal.remove(anti_diagonal_value)
                diagonal.remove(diagonal_value)
                cols.remove(col)

            return count

        ans = backtracking(0, set(), set(), set())
        return ans

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def backtrack(row, cols, diagonal, anti_diagonal):
            nonlocal count
            if row == n:
                count += 1
            
            for col in range(n):
                curr_anti_diagonal = row + col
                curr_diagonal = row - col

                if col in cols or curr_diagonal in diagonal or curr_anti_diagonal in anti_diagonal:
                    continue
                
                cols.add(col)
                diagonal.add(curr_diagonal)
                anti_diagonal.add(curr_anti_diagonal)
                backtrack(row + 1, cols, diagonal, anti_diagonal)
                cols.remove(col)
                diagonal.remove(curr_diagonal)
                anti_diagonal.remove(curr_anti_diagonal)

        backtrack(0, set(), set(), set())
        return count
