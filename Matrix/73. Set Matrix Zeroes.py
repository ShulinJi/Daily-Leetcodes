# Ex.
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_col_set = set()
        zero_row_set = set()

        # Record the rows and columns that have zero
        for row in range(m):
            if 0 in matrix[row]:
                zero_row_set.add(row)
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_col_set.add(col)

        # Make the row and column recorded become zero
        for row in range(m):
            for col in range(n):
                if row in zero_row_set or col in zero_col_set:
                    matrix[row][col] = 0



