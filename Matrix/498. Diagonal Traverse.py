
# Code


# Testcase
# Testcase
# Test Result
# 498. Diagonal Traverse
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105


# O(M * N) time complexity, O(min(N, M)) space complexity
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        M, N = len(mat[0]), len(mat)

        results = []
        mid = []

        for d in range(N + M - 1):
            mid.clear()
            # +1 b/c we start at row 1 afyer hits the corner (corner included in the last column)
            row = 0 if d < M else d - M + 1
            # first increase as we traverse col, then fixed at last col
            col = d if d < M else M - 1

            # traverse the diagonal
            while row < N and col >= 0:
                mid.append(mat[row][col])
                row += 1
                col -= 1
            
            # even diagonal needs to be reversed since we need the zigzag pattern
            if d % 2 == 0:
                results.extend(mid[::-1])
            else:
                results.extend(mid)
        
        return results